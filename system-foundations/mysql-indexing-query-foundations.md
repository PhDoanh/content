---
title: "MySQL Index B-Tree: Từ Clustered Đến JOIN & Subquery"
description: "Hiểu MySQL indexing từ B-Tree, clustered vs secondary, composite/covering đến constraints và truy vấn SELECT-JOIN-subquery để viết SQL nhanh, đúng và bền vững."
permalink: ""
lang: vi
publish: false
updated: 2026-08-30
tags:
  - fullstack
  - Intermediate
  - GenAI
aliases: []
cssclasses: []
socialDescription: "Từ B-Tree đến JOIN và subquery — nền tảng MySQL indexing và truy vấn cho truy vấn nhanh, đúng."
socialImage: ""
---

# MySQL Index B-Tree: Từ Clustered Đến JOIN & Subquery

> [!tip] Key takeaways — Đọc 90 giây là đủ
> - **InnoDB chỉ có một clustered index** — chính là bảng. Leaf của nó chứa toàn bộ row, còn mọi secondary index chỉ chứa primary key và phải quay về clustered để lấy row (bookmark lookup) — trừ khi bạn dùng covering index.
> - **B+Tree biến O(n) thành O(log n):** với page 16KB, cây 3 tầng có thể index hàng tỷ row và range scan chạy trên leaf chain doubly-linked.
> - **Composite phải tuân leftmost prefix:** index `(a,b,c)` chỉ giúp query có `a`, `(a,b)`, `(a,b,c)` — bỏ `a` là mất index; range (`>`, `BETWEEN`, `LIKE 'prefix%'`) chặn cột bên phải.
> - **Constraints là hàng rào trước khi hỏi:** `CHECK` chỉ thực thi từ MySQL 8.0.16 (trước đó parse nhưng bị bỏ qua), `FOREIGN KEY` chỉ có tác dụng trên InnoDB và `SET DEFAULT` bị từ chối.
> - **Subquery vs JOIN không phải gu thẩm mỹ:** `EXISTS` short-circuit và an toàn với NULL, `NOT IN` trả về rỗng nếu subquery có dù chỉ một NULL — hãy dùng `NOT EXISTS`; nhiều `IN (subquery)` được optimizer viết lại thành semi-join.

Tôi từng tin index luôn làm query nhanh hơn. Rồi tôi xem một benchmark của Percona: cùng một table không fit trong memory, full table scan xong trong 4 giây, còn full index scan mất 30 giây. Khoảnh khắc đó khiến tôi nhận ra — tôi không hiểu index. Tôi chỉ đang tạo nó theo thói quen.

Bài này là cách tôi hệ thống lại MySQL từ gốc [[Database Indexing]] đến ngọn là truy vấn. Không phải ba chủ đề rời rạc là index, constraints và SELECT, mà là một hệ thống duy nhất: index quyết định *đường đi*, constraints quyết định *hình dạng* được phép của dữ liệu, còn SELECT/JOIN/subquery quyết định *cách bạn hỏi*.

## Vì sao index, constraints và truy vấn là một hệ thống duy nhất

Nếu dữ liệu bẩn đã chui vào bảng, mọi tối ưu truy vấn đều vô nghĩa. Và nếu index đặt sai, constraint có chặt đến mấy cũng không cứu được một `JOIN` đang quét cả triệu row.

Index và constraints làm việc ở hai phía của cùng một câu chuyện. Index trả lời câu hỏi "tìm hàng này bằng cách nào cho đỡ quét cả bảng". Constraints trả lời "hàng này có được phép tồn tại không". Còn truy vấn là nơi hai thứ đó gặp nhau: bạn viết `WHERE`, `JOIN`, `GROUP BY` thế nào thì optimizer mới biết nên chọn đường nào.

> [!info] Mental model tôi hay dùng: **đường đi — hình dạng — câu hỏi**
> - **Đường đi:** [[B-Tree Index]] và [[Database Indexing]] — cấu trúc giúp truy vấn đi O(log n) thay vì O(n).
> - **Hình dạng:** [[MySQL Constraints Relationship]] — 6 lớp constraint khóa hình dạng bảng.
> - **Câu hỏi:** [[MySQL Select Statement]] → [[MySQL Join Table]] → [[MySQL Subquery]] — cách bạn đặt câu hỏi quyết định index có được dùng hay không.

### Khi nào chưa cần index?

Tôi từng thêm index cho mọi cột trong `WHERE` và tự hỏi sao `INSERT` chậm đi. Câu trả lời khá phũ: mỗi index là một B+Tree riêng cần duy trì. Thêm index giúp `SELECT`/`JOIN`/`ORDER BY` nhanh hơn, nhưng làm `INSERT`/`UPDATE`/`DELETE` chậm hơn và tốn storage — có khi tốn hơn cả bảng gốc [^index-overview].

Bạn nên dừng lại khi:
- Bảng dưới 10 row — optimizer thấy quét thẳng rẻ hơn duyệt cây.
- Workload ghi nhiều hơn đọc — 23 index trên một bảng như case JusDB dưới đây là ví dụ điển hình của over-indexing.
- Query chạm hơn 30% bảng — lúc này full scan ít random seek hơn index lookup.

![B-Tree 3 tầng với page 16KB — root chứa key ranges, internal chứa child pointers, leaf nối doubly-linked list cho range scan](https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=1200&q=80&auto=format&fit=crop)
*Ảnh: Mô hình B-Tree — mỗi node = 1 page. Nguồn: Unsplash / @nasa — minh họa cấu trúc phân tầng, dùng theo giấy phép Unsplash License.*

## B-Tree và B+Tree: MySQL tìm hàng trong O(log n) như thế nào

MySQL InnoDB không dùng B-Tree thuần. Nó dùng **B+Tree**: chỉ leaf mới chứa value, inner node chỉ chứa keys. Nghe như chi tiết nhỏ, nhưng hệ quả rất lớn: inner node gọn hơn nên chứa được nhiều keys hơn trên cùng một page 16KB, cây thấp hơn, ít lần I/O hơn, và toàn bộ leaf được nối thành doubly-linked list nên range scan chạy tuần tự cực nhanh. Mọi leaf cùng độ sâu nên mọi lookup đều là O(log n) [^planetscale-btree][^datacamp-btree].

Tôi hay hình dung B+Tree như mục lục sách: root là chương lớn, internal là mục con, leaf là trang thật sự chứa nội dung. Muốn tìm chương 7 mục 3, bạn không lật từng trang mà nhảy từ mục lục xuống đúng trang.

### Cấu trúc root → internal → leaf

- **Root:** entry point chứa key ranges chỉ hướng đi.
- **Internal:** chỉ chứa keys và child pointers — không chứa row.
- **Leaf:** chứa key + value (với clustered index thì value là cả row) và hai con trỏ nối leaf trước/sau.

Mỗi node được size theo disk page — InnoDB mặc định 16KB. Khi node đầy, nó split thành hai và cây tự cân bằng. Kết quả: với cây cao 3, bạn có thể index hàng tỷ row mà lookup chỉ cần tối đa 3 lần I/O [^planetscale-btree][^oneuptime-btree].

### B-Tree vs B+Tree — vì sao DB chọn B+Tree?

B-Tree truyền thống lưu value ở cả inner lẫn leaf, nên inner node phình ra và cây cao hơn. B+Tree dồn toàn bộ value xuống leaf, inner node chỉ giữ keys nên mỗi page nhét được nhiều keys hơn. Thêm nữa, leaf chain cho phép `BETWEEN` hay `ORDER BY` chạy như đi bộ trên danh sách liên kết thay vì nhảy ngẫu nhiên khắp cây [^stackoverflow-btree][^besthub-btree].

> [!warning] Bẫy tôi từng vấp: PK ngẫu nhiên
> Dùng UUID làm PRIMARY KEY nghe hay cho phân tán, nhưng inserts ngẫu nhiên khiến InnoDB phải split page liên tục và xáo trộn doubly-linked list. PK tuần tự (`AUTO_INCREMENT` INT/BIGINT) luôn append vào page cuối cùng, tránh split đắt đỏ. Nếu workload random-insert, cân nhắc `innodb_fill_factor = 80` để chừa 20% page cho inserts tương lai [^oneuptime-btree][^generalist-indexing].

## Clustered vs secondary và composite/covering — chọn index đúng

Đây là chỗ nhiều người nhầm nhất. Trong InnoDB, **một bảng chỉ có một clustered index — và nó chính là PRIMARY KEY**. Không có storage riêng cho "bảng": leaf của clustered B+Tree *là* bảng. Bạn `SELECT * FROM orders WHERE id = 42` thì chỉ một lần duyệt cây là ra row (`type = const`) [^oneuptime-btree][^redgate-clustered].

Mọi index khác là **secondary (non-clustered)** — mỗi cái là một B+Tree riêng. Leaf của nó không chứa row, chỉ chứa giá trị cột được index + giá trị PRIMARY KEY. Nên mỗi lần dùng secondary, MySQL phải làm hai bước: duyệt secondary để lấy PK, rồi duyệt clustered để lấy row. Người ta gọi bước hai là "bookmark lookup" [^jusdb-indexes].

```sql
-- Clustered lookup: một lần duyệt
EXPLAIN SELECT * FROM orders WHERE id = 42;
-- type = const, key = PRIMARY, rows = 1

-- Secondary lookup: hai lần duyệt
CREATE INDEX idx_user_id ON orders (user_id);
EXPLAIN SELECT * FROM orders WHERE user_id = 42;
-- type = ref, key = idx_user_id, rows ~ 100, Extra: Using where
```

![So sánh clustered leaf chứa toàn bộ row vs secondary leaf chỉ chứa primary key](https://images.unsplash.com/photo-1518770660439-4636190af475?w=1200&q=80&auto=format&fit=crop)
*Ảnh: Secondary phải quay về clustered. Nguồn: Unsplash / @ramotion — minh họa "pointer back to row".*

### Composite — thứ tự là hiệu năng

Composite index `(customer_id, status, created_at)` không phải là ba index rời. Nó là một B+Tree sắp xếp theo `customer_id` trước, rồi `status` trong mỗi nhóm `customer_id`, rồi `created_at`. Vì thế quy tắc **leftmost prefix** rất nghiêm:

Index `(a,b,c)` chỉ giúp query có `a`, `(a,b)`, `(a,b,c)` — không giúp query chỉ có `b` hay `c` [^mysql-range][^besthub-composite][^sql-designer].

```sql
CREATE INDEX idx_status_created ON orders (status, created_at);

-- Dùng được: leftmost prefix
SELECT * FROM orders WHERE status = 'pending' AND created_at > '2024-01-01';
SELECT * FROM orders WHERE status = 'pending';

-- Không dùng được: thiếu leftmost
SELECT * FROM orders WHERE created_at > '2024-01-01'; -- full scan
```

Và một khi cột trước đó là range (`>`, `<`, `BETWEEN`, `LIKE 'prefix%'`), việc dùng index cho cột bên phải dừng lại. Ví dụ `WHERE col1 = 100 AND col2 > 200 AND col3 = 300` thì `col3` không được hưởng lợi từ index nữa [^besthub-leftmost]. Đặt cột equality trước, cột range/timestamp cuối — thường là `(user_id, status, created_at)` thay vì `(created_at, user_id)` sẽ cho selectivity tốt hơn [^oneuptime-composite].

### Covering index — tránh double lookup

Nếu query chỉ cần những cột đã có trong index, MySQL không cần quay về bảng. Đó là covering index, và `EXPLAIN` sẽ báo `Extra: Using index` [^datacamp-covering][^dohost-covering].

```sql
-- Covering: mọi cột đều trong index
CREATE INDEX idx_covering ON orders (customer_id, status, total);
EXPLAIN SELECT customer_id, status, total
FROM orders WHERE customer_id = 12345 AND status = 'completed';
-- Extra: Using index  (không chạm bảng)
```

JusDB ghi lại một case thực: team tạo 23 single-column index cho bảng `user_activities` vì "cho chắc", kết quả `INSERT` chậm, query vẫn chậm vì không index nào khớp pattern lọc kết hợp. Họ xóa 19 index, thêm 3 composite thiết kế theo query thật: `INSERT` về 12ms, SELECT dashboard từ 30 giây về 30ms trên bảng lớn [^jusdb-indexes]. Một covering index khác trên bảng 5 triệu row giảm aggregation từ 55 giây về ~2 giây vì tránh table lookup [^besthub-covering].

> [!tip] Cách tôi xác thực index có được dùng không
> ```sql
> EXPLAIN SELECT * FROM orders WHERE user_id = 42 AND status = 'shipped';
> -- Xem key, type, rows, Extra
> SELECT object_name, index_name, count_star
> FROM performance_schema.table_io_waits_summary_by_index_usage
> WHERE object_schema = 'myapp' ORDER BY count_star DESC;
> -- count_star = 0 nghĩa là index chưa bao giờ được dùng — cân nhắc drop
> ```
> Nguồn: MySQL 8.4 EXPLAIN Output Format + OneUptime [^mysql-explain][^oneuptime-optimization].

## Constraints trong MySQL: 6 lớp bảo vệ toàn vẹn dữ liệu

Tôi từng nghĩ constraints là việc của application. Đến khi migrate một DB 5.7 lên 8.0 và phát hiện `CHECK` cũ chưa từng được enforce, tôi đổi ý.

MySQL có 6 loại: `NOT NULL`, `UNIQUE`, `PRIMARY KEY`, `FOREIGN KEY`, `CHECK`, `DEFAULT`. Chúng tạo thành entity / referential / domain integrity ngay tại DB, không phụ thuộc app [^mysql-constraints][^redgate-constraints].

### NOT NULL / UNIQUE / PRIMARY KEY — nền tảng entity integrity

- `NOT NULL`: cột không được chứa `NULL`. Mặc định là nullable, còn `PRIMARY KEY` thì ngầm `NOT NULL`.
- `UNIQUE`: mọi giá trị phải khác nhau, nhưng MySQL cho phép nhiều `NULL` — đặc thù cần nhớ. Mỗi `UNIQUE` tự tạo một B-Tree index.
- `PRIMARY KEY`: kết hợp `NOT NULL` + `UNIQUE`, một/bảng, tên luôn là `PRIMARY`, tự tạo clustered index [^mysql-pk].

```sql
CREATE TABLE users (
  id INT PRIMARY KEY,
  email VARCHAR(255) UNIQUE NOT NULL
);
-- UNIQUE tự sinh index; PRIMARY tạo clustered B+Tree
```

### FOREIGN KEY — referential integrity và các bẫy

`FOREIGN KEY` chỉ thực thi trên **InnoDB**. MyISAM parse nhưng bỏ qua — tôi từng mất nửa ngày vì test trên MyISAM và tự hỏi sao FK không chặn [^redgate-constraints]. Cột tham chiếu phải indexed, và `FOREIGN KEY (user_id) REFERENCES users(id)` có các hành động:

| Action | Hành vi |
|---|---|
| `RESTRICT` | Từ chối xóa/sửa parent nếu child còn tồn tại (default) |
| `CASCADE` | Lan tỏa xóa/sửa sang child |
| `SET NULL` | Đặt child FK về `NULL` |
| `NO ACTION` | Giống `RESTRICT` trong InnoDB |
| `SET DEFAULT` | Được parse nhưng **InnoDB từ chối** |

Điều khiển bằng `foreign_key_checks` (mặc định ON). Và lỗi kinh điển: `there can be only one auto column and it must be defined as a key` — `AUTO_INCREMENT` phải là key [^redgate-clustered][^mysql-fk].

### CHECK và DEFAULT — domain integrity

Đây là cú lừa lịch sử. Trước **MySQL 8.0.16**, cú pháp `CHECK (price > 0)` được parse nhưng **silently ignored** trên mọi storage engine [^mysql-check][^mysql-blog-check][^oneuptime-check].

```sql
-- Trước 8.0.16: không hề chặn
CREATE TABLE t1 (c1 INT CHECK (c1 > 0));
INSERT INTO t1 VALUES (0); -- Query OK, 1 row affected (0.00 sec) — bẫy!

-- Từ 8.0.16: chặn thật sự, có NOT ENFORCED
CREATE TABLE t1 (
  c1 INT CHECK (c1 > 0),
  c2 INT CHECK (c2 > 0) NOT ENFORCED
);
-- Biểu thức phải trả về TRUE hoặc UNKNOWN (NULL thì pass), FALSE thì ERROR 3819
```

Từ 8.0.16, bạn có thể đặt tên `CONSTRAINT chk_price CHECK (price > 0)`, dùng `[NOT] ENFORCED`, và audit qua `information_schema.CHECK_CONSTRAINTS`. Khi migrate, hãy fix dữ liệu bẩn trước khi `ADD CONSTRAINT` — nếu không, `ALTER TABLE` sẽ fail [^oneuptime-check].

![Ma trận tương tác constraints: PK/FK/UNIQUE/CHECK phối hợp thế nào](https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=1200&q=80&auto=format&fit=crop)
*Ảnh: Constraints như lưới lọc trước khi data chạm bảng. Nguồn: Unsplash / @campaign_creators — CC0.*

## SELECT từ trong ra ngoài: thứ tự thực thi và bẫy GROUP BY/HAVING

Đây là chỗ nhiều bạn mới viết SQL bị rối: thứ tự *viết* khác thứ tự *chạy*.

Thứ tự viết: `SELECT → FROM → WHERE → GROUP BY → HAVING → ORDER BY → LIMIT`.
Thứ tự chạy: `FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT` [^datacamp-order][^mysql-select].

Vì `WHERE` chạy trước `SELECT` nên alias trong `SELECT` không dùng được trong `WHERE`:

```sql
-- Sai: WHERE không thấy discounted_price
SELECT price * 0.9 AS discounted_price FROM products WHERE discounted_price > 100;
-- Đúng: dùng HAVING hoặc subquery
SELECT price * 0.9 AS discounted_price FROM products HAVING discounted_price > 100;
```

`WHERE` lọc *row*, `HAVING` lọc *group*. Và `DISTINCT` xét trên toàn bộ row được chọn, không phải một cột — `SELECT DISTINCT city` khác `SELECT DISTINCT city, country` [^mysql-select].

```sql
-- GROUP BY gộp row, HAVING lọc nhóm
SELECT city, COUNT(*) AS user_count, AVG(age) AS avg_age
FROM users
GROUP BY city
HAVING user_count > 5;
```

`LIKE` với `%` đầu (`'%suffix'`) không dùng được B-Tree — lúc này cân nhắc full-text thay vì cố nhét wildcard đầu [^datacamp-btree]. `LIMIT 20 OFFSET 40` chính là `LIMIT 40, 20` — phân trang; `ORDER BY` nên được index hỗ trợ nếu không sẽ `Using filesort` [^mysql-explain].

> [!info] Pre-aggregate trước khi JOIN — thói quen giúp tôi giảm row phải xử lý
> ```sql
> -- Thay vì JOIN rồi mới GROUP BY, hãy shrink trước
> SELECT o.order_id, o.total_cost, ai.total_items
> FROM orders AS o
> JOIN (SELECT order_id, COUNT(*) AS total_items FROM order_items GROUP BY order_id) AS ai
>   ON o.order_id = ai.order_id;
> ```
> Nguồn: DataCamp SQL Order of Execution [^datacamp-order].

## JOIN thực chiến: INNER/LEFT/RIGHT và FULL OUTER giả lập bằng UNION

MySQL có `INNER JOIN` (viết `JOIN` là ngầm `INNER`), `LEFT JOIN`, `RIGHT JOIN`, `CROSS JOIN`, `NATURAL JOIN` — nhưng **không có** `FULL OUTER JOIN` native. Muốn full outer, phải giả:

```sql
SELECT * FROM users u LEFT JOIN orders o ON u.id = o.user_id
UNION
SELECT * FROM users u RIGHT JOIN orders o ON u.id = o.user_id;
-- UNION (không ALL) deduplicate — cho ra FULL OUTER đúng
```
[^mysql-join][^redgate-constraints]

- `INNER` chỉ trả về match ở cả hai bảng. `LEFT` trả về tất cả left + right `NULL` nếu không match — hợp cho "users with or without orders".
- `RIGHT` nên tránh: hãy đảo thứ tự bảng và dùng `LEFT` nhất quán cho dễ đọc.
- `CROSS JOIN` là tích Descartes — hiếm khi hữu ích không lọc. Dấu `,` tương đương `CROSS` nhưng độ ưu tiên thấp hơn `JOIN`, dễ tạo bẫy `FROM t1, t2 JOIN t3 ON t1.id = t3.id` — nên `FROM (t1, t2) JOIN t3` hoặc dùng `JOIN` hết [^mysql-join].
- `NATURAL JOIN` tự join trên mọi cột cùng tên — mong manh, break khi thêm cột mới; ưu tiên `ON a.id = b.id` hoặc `USING(id)` (USING gộp cột thành một) [^mysql-join].

Multi-table `JOIN` tuân theo optimizer reorder với `INNER` nhưng tôn trọng thứ tự với `LEFT`. Và quy tắc vàng không đổi: luôn join trên cột đã indexed — nếu không, `EXPLAIN` sẽ báo `rows` examined chênh 10–100x [^jusdb-indexes][^oneuptime-composite].

![Các loại JOIN: INNER chỉ lấy giao, LEFT giữ hết trái, FULL OUTER qua UNION](https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=1200&q=80&auto=format&fit=crop)
*Ảnh: JOIN như ghép hai tập hợp. Nguồn: Unsplash / @ppengcreative — Unsplash License.*

## Subquery vs JOIN: khi nào dùng scalar/correlated/EXISTS

Subquery và JOIN thường cho cùng kết quả, nhưng khác về readability, NULL correctness và hiệu năng. Tôi hay quyết định bằng một câu hỏi: "Bạn cần cột từ cả hai bảng, hay chỉ cần kiểm tra tồn tại?"

MySQL có 6 dạng subquery [^mysql-subquery][^devart-subquery]:

- **Scalar:** 1 giá trị — `WHERE price > (SELECT AVG(price) FROM products)`
- **Row:** 1 row đa cột — `WHERE (category_id, price) = (SELECT …)`
- **Column:** 1 cột với `IN/ANY/ALL` — `WHERE id IN (SELECT user_id FROM orders)`
- **Table/derived:** `FROM (SELECT …) AS alias` — bắt buộc alias, thường materialized thành temporary table
- **Correlated:** tham chiếu outer query — chạy mỗi row, dễ thành O(n²) nếu không cẩn: `WHERE amount > (SELECT AVG(amount) FROM orders WHERE customer_id = o.customer_id)`
- **EXISTS/NOT EXISTS:** chỉ kiểm tồn tại, bỏ qua SELECT list, dừng ngay khi gặp match đầu (short-circuit) [^villagesql-subquery]

### IN vs EXISTS vs JOIN — bảng quyết định

| Cách | Khi nào dùng |
|---|---|
| `IN (subquery)` | Subquery trả về tập nhỏ, tĩnh — dễ đọc |
| `EXISTS` | Chỉ cần biết tồn tại, tập lớn, an toàn với NULL |
| `JOIN DISTINCT` | Cần cột từ cả hai bảng, optimizer có nhiều linh hoạt hơn |

Nhiều `IN (subquery)` được optimizer viết lại thành semi-join nên chênh lệch thường không đáng kể — nhưng hãy kiểm bằng `EXPLAIN` trước khi tối ưu tay [^villagesql-subquery][^datacamp-subquery].

### Bẫy NOT IN với NULL — lỗi tôi từng mất cả buổi

```sql
-- Trả về 0 row nếu ANY customer_id trong orders là NULL (!)
SELECT name FROM customers WHERE id NOT IN (SELECT customer_id FROM orders);

-- An toàn: trả về customers không có order, kể cả khi orders có NULL
SELECT name FROM customers c WHERE NOT EXISTS (
  SELECT 1 FROM orders o WHERE o.customer_id = c.id
);
```

Nếu `orders.customer_id` có dù chỉ một `NULL`, `NOT IN (NULL, 1, 2)` là `UNKNOWN` cho mọi so sánh — cả query rỗng. Đây là SQL standard, không phải bug MySQL [^villagesql-subquery]. Một benchmark cũ trên table 250K row cho thấy chuyển `DEPENDENT SUBQUERY` thành `INNER JOIN` nhanh ~30x [^codersrev-join].

> [!warning] Correlated trong SELECT — chạy mỗi row
> ```sql
> SELECT order_id, (SELECT SUM(quantity) FROM order_items WHERE order_items.order_id = orders.order_id) AS total_items
> FROM orders;
> -- Chạy per row — cân nhắc viết lại thành JOIN với derived/CTE
> WITH stats AS (SELECT order_id, COUNT(*) AS total_items FROM order_items GROUP BY order_id)
> SELECT o.order_id, s.total_items FROM orders o JOIN stats s ON s.order_id = o.order_id;
> ```
> Kiểm `EXPLAIN` xem có `DEPENDENT SUBQUERY` và `Using temporary` không [^devart-subquery][^mysql-optimization].

## Video tham khảo — xem B+Tree và EXPLAIN chạy thật

Hai video này giúp bạn *thấy* B+Tree duyệt thế nào thay vì chỉ đọc mô tả.

<iframe src="https://www.youtube.com/embed/Clr2cFrIJpA" title="SQL Indexes Explained - B-Tree Indexes in MySQL" loading="lazy" allowfullscreen style="width:100%;aspect-ratio:16/9;border:0;border-radius:12px;"></iframe>
*SQL Indexes Explained — B-Tree Indexes in MySQL (YouTube, 2023-05-08) — đi sâu vào nitty-gritty của B-Tree, khi nào index được dùng và tại sao LIKE với leading wildcard làm index vô dụng.*

<iframe src="https://www.youtube.com/embed/t5N9mpAl7AU" title="MySQL Indexes Explained | B+ Tree, Composite — Full Tutorial" loading="lazy" allowfullscreen style="width:100%;aspect-ratio:16/9;border:0;border-radius:12px;"></iframe>
*MySQL Indexes Explained | B+ Tree, Composite (YouTube, 2026-07-21) — từ beginner đến advanced với SQL thật, composite, covering và câu hỏi phỏng vấn.*

<iframe src="https://www.youtube.com/embed/eqf07YvIQ_Q" title="What Is a Database Index? How B-Tree Indexes Actually Work" loading="lazy" allowfullscreen style="width:100%;aspect-ratio:16/9;border:0;border-radius:12px;"></iframe>
*What Is a Database Index? How B-Tree Indexes Actually Work — giải thích mechanics từ scratch cho người chưa từng đụng index.*

## FAQ

### Khác nhau giữa B-Tree và B+Tree trong MySQL là gì?

B+Tree chỉ lưu value ở leaf và nối leaf thành doubly-linked list nên cây nông hơn và range scan nhanh hơn. InnoDB dùng B+Tree cho mọi index — inner node gọn hơn nên nhét được nhiều keys trên page 16KB, ít I/O hơn [^planetscale-btree][^stackoverflow-btree].

### Vì sao PRIMARY KEY trong InnoDB luôn là clustered index?

Vì InnoDB lưu toàn bộ row tại leaf của clustered B+Tree theo PK — không có storage riêng cho row. Secondary index chỉ lưu PK nên PK lookup chỉ cần một lần duyệt cây, còn secondary phải bookmark lookup lần hai trừ khi là covering index [^oneuptime-btree][^jusdb-indexes].

### Khi nào MySQL bỏ qua index dù index đã tồn tại?

Khi optimizer ước lượng query chạm >~30% bảng, bảng <~10 row, hoặc query không dùng leftmost prefix của composite. Lúc đó full scan rẻ hơn B-Tree traversal; kiểm bằng `EXPLAIN` sẽ thấy `type: ALL` và `Extra: Using where` thay vì `Using index` [^sql-designer][^oneuptime-optimization]. Ngoài ra, `LIKE '%suffix'` hay hàm trên cột (`UPPER(col)`) cũng làm index vô dụng — hãy dùng prefix `LIKE 'prefix%'` hoặc functional index `CREATE INDEX idx_upper ON users ((UPPER(username)))` [^jusdb-indexes].

### Nên dùng NOT IN hay NOT EXISTS?

Dùng `NOT EXISTS` nếu subquery có thể chứa NULL. `NOT IN` trả về rỗng khi gặp dù chỉ một NULL vì `NULL = unknown`, còn `NOT EXISTS` an toàn và short-circuit ở match đầu; với tập lớn, `EXISTS`/`JOIN` thường ổn định hơn `IN` [^villagesql-subquery].

### CHECK constraint trước MySQL 8.0.16 thì sao?

Trước 8.0.16, `CHECK (price > 0)` được parse nhưng silently ignored trên mọi storage engine — dữ liệu bẩn vẫn chui vào và không báo lỗi. Từ 8.0.16 mới thực thi và hỗ trợ `[NOT] ENFORCED` cùng cross-column check; trước khi migrate, nhớ audit `information_schema.CHECK_CONSTRAINTS` và fix data trước khi `ADD CONSTRAINT` [^mysql-check][^mysql-blog-check][^oneuptime-check].

## Kết luận

Nếu bạn chỉ nhớ ba điều sau khi gấp bài này lại, tôi muốn đó là:

Chọn PRIMARY KEY tuần tự và đặt composite đúng thứ tự leftmost — equality trước, range sau — rồi cân nhắc covering khi `SELECT` chỉ cần vài cột. Bảo vệ dữ liệu bằng 6 constraints, đặc biệt lưu ý `CHECK` chỉ có từ 8.0.16 và `FOREIGN KEY` chỉ có ý nghĩa trên InnoDB. Và viết SELECT/JOIN/subquery theo đúng thứ tự thực thi, luôn xác thực bằng `EXPLAIN` + `performance_schema.table_io_waits_summary_by_index_usage` thay vì đoán.

Khi bạn làm chủ được B+Tree, leftmost prefix, covering index và bẫy `NOT IN`/`FULL OUTER`, MySQL không còn là black box. Nó thành một hệ thống bạn có thể suy luận — và tối ưu có chủ đích, không phải bằng may rủi.

> [!tip] Đọc tiếp trong vault
> - [[Database Indexing]] • [[B-Tree Index]] • [[Index]] — nền tảng index và B+Tree
> - [[MySQL Constraints Relationship]] ↔ [[Primary Key]] / [[Foreign Key]] — toàn vẹn dữ liệu
> - [[MySQL Select Statement]] → [[MySQL Join Table]] → [[MySQL Subquery]] — chuỗi truy vấn
> - [[Database]] / [[RDBMS]] / [[MySQL]] — pillars để mở rộng

---

**Nguồn tham khảo (đã xác thực, truy xuất 2026-08-30)**

[^planetscale-btree]: PlanetScale — B-Tree Database Indexes (2024) — B+Tree stores values only at leaves, inner nodes hold keys, InnoDB clustered = PK B+Tree, secondary stores PK — https://planetscale.com/blog/btrees-and-database-indexes
[^stackoverflow-btree]: StackOverflow — How B-Tree indexing works in MySQL (Quassnoi, 2010; sendon1982, 2019) — Record pointer = PK in InnoDB, MYI offset in MyISAM; InnoDB uses B+Tree — https://stackoverflow.com/questions/2362667/how-b-tree-indexing-works-in-mysql
[^oneuptime-btree]: OneUptime — How MySQL B-Tree Indexes Work Internally (Nawaz Dhandala, 2026-03-31) — leaf doubly-linked, clustered vs secondary two-step lookup, covering avoids double lookup — https://oneuptime.com/blog/post/2026-03-31-mysql-btree-indexes-work-internally/view
[^besthub-btree]: BestHub — Master MySQL Indexes: From Basics to B+Tree and Clustered vs Non-Clustered (2025-10-15) — page split, sequential PK avoids fragmentation — https://www.besthub.dev/articles/master-mysql-indexes-from-basics-to-b-tree-and-clustered-vs-non-clustered-ea9c8d34f10e
[^generalist-indexing]: Generalist Programmer — Database Indexing: The Complete Guide (2026-06-17) — clustered = physical order, one per table; non-clustered stores clustered key — https://generalistprogrammer.com/tutorials/database-indexing-complete-guide
[^redgate-clustered]: Red-Gate Simple Talk — MySQL Index Overviews: Clustered B-Tree Indexes (2024-12-03) — clustered stores row data, one per table — https://www.red-gate.com/simple-talk/databases/mysql/mysql-index-deep-dive-clustered-b-tree-indexes/
[^datacamp-btree]: DataCamp — MySQL B-TREE Indexes: Usage & Examples — B-TREE for range queries, composite order, LIKE leading wildcard inefficiency — https://www.datacamp.com/doc/mysql/mysql-b-tree
[^jusdb-indexes]: JusDB — MySQL Indexes Explained: B-Tree, Composite, Covering & Partial Indexes (2026-06-20) — secondary → PK → clustered 2-step, leftmost prefix, JusDB case 19/23 dropped → 3 composite INSERT 12ms, covering — https://www.jusdb.com/blog/mysql-indexes-explained-complete-data-structure-guide-for-query
[^mysql-range]: MySQL 8.4 Reference — Range Optimization & Multiple-Column Indexes — leftmost prefix `(a,b,c)` serves `a`, `(a,b)`, `(a,b,c)` — https://dev.mysql.com/doc/refman/8.4/en/multiple-column-indexes.html
[^besthub-composite]: BestHub — Master MySQL Composite Indexes: Unlock the Leftmost Prefix Principle (2025-10-04) — B+Tree built left-to-right, leftmost prefix governs usage — https://www.besthub.dev/articles/master-mysql-composite-indexes-unlock-the-leftmost-prefix-principle-a2adc4271fee
[^sql-designer]: SQL Designer — MySQL Composite Indexes and the Leftmost-Prefix Rule (Dmitriy Snyatkov, 2026-08-03) — leftmost prefix `(a,b,c)` can serve `a` etc., but not `b`/`c` alone; B-Tree turns 1M-row lookup into 2-3 page reads — https://sql-designer.com/blog/mysql-indexes
[^besthub-leftmost]: BestHub — Mastering MySQL's Leftmost Prefix Rule (2023-08-22) — leftmost prefix + range stops subsequent columns — https://www.besthub.dev/articles/mastering-mysql-s-leftmost-prefix-rule-when-indexes-work-and-when-they-fail-ef28d48cde6f
[^oneuptime-composite]: OneUptime — How to Create a Composite Index in MySQL (2026-03-31) — column order = selectivity, use EXPLAIN — https://oneuptime.com/blog/post/2026-03-31-mysql-composite-index/view
[^datacamp-covering]: DataCamp — MySQL Covering Indexes: Usage & Examples — covering serves query from index alone — https://www.datacamp.com/doc/mysql/mysql-covering
[^dohost-covering]: DoHost — Covering Indexes: Achieving Lightning-Fast Speed (2026-01-21) — Extra: Using index = covering; 55s→2s on 5M rows besthub reference — https://dohost.us/index.php/2025/12/30/covering-indexes-achieving-lightning-fast-speed-by-staying-in-the-index
[^besthub-covering]: BestHub — Improving MySQL Query Performance with Covering Indexes (2023-02-02) — 55-second aggregation on 5M rows to ~2s — https://www.besthub.dev/articles/improving-mysql-query-performance-with-covering-indexes-3e7491986b9c
[^mysql-pk]: MySQL 8.4 Reference — PRIMARY KEY and UNIQUE Index Constraints (1.7.3.1) — transactional rollback, IGNORE, InnoDB/NDB FK — https://dev.mysql.com/doc/refman/8.4/en/constraint-primary-key.html
[^mysql-constraints]: MySQL 8.4 Reference — How MySQL Deals with Constraints (1.7.3) — constraint handling philosophy — https://dev.mysql.com/doc/refman/8.4/en/constraints.html
[^redgate-constraints]: Red-Gate Simple Talk — MySQL Constraints Guide: PRIMARY KEY, FOREIGN KEY, NOT NULL... (Robert Sheldon, 2023-09-07) — 6 types, named constraints, spec examples — https://www.red-gate.com/simple-talk/databases/mysql/working-with-mysql-constraints/
[^mysql-check]: MySQL 8.0 Reference — CHECK Constraints (15.1.20.6) — prior to 8.0.16 parsed and ignored; as of 8.0.16 supports [CONSTRAINT symbol] CHECK (expr) [[NOT] ENFORCED] — https://dev.mysql.com/doc/refman/8.0/en/create-table-check-constraints.html
[^mysql-blog-check]: MySQL Blog — MySQL 8.0.16 Introducing CHECK constraint (2019-04-26) — demo parsed+ignored before, enforced after — https://dev.mysql.com/blog-archive/mysql-8-0-16-introducing-check-constraint
[^oneuptime-check]: OneUptime — How to Use CHECK Constraints in MySQL 8.0+ (2026-03-31) — CHECK evaluated on INSERT/UPDATE, FALSE → ERROR 3819, NULL passes — https://oneuptime.com/blog/post/2026-03-31-mysql-check-constraints/view
[^mysql-fk]: MySQL 8.4 Reference — FOREIGN KEY Constraints — InnoDB only, referenced columns must be indexed — https://dev.mysql.com/doc/refman/8.4/en/constraint-foreign-key.html
[^mysql-select]: MySQL 8.4 Reference — SELECT Statement & Optimization — execution order, DISTINCT, GROUP BY — https://dev.mysql.com/doc/refman/8.4/en/select.html
[^datacamp-order]: DataCamp — SQL Order of Execution: Understanding How Queries Run — FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT — https://www.datacamp.com/tutorial/sql-order-of-execution
[^mysql-join]: MySQL 8.4 Reference — JOIN Syntax — INNER/LEFT/RIGHT/CROSS/NATURAL, USING vs ON, comma lower precedence than JOIN — https://dev.mysql.com/doc/refman/8.4/en/join.html
[^mysql-subquery]: MySQL 8.4 Reference — Subqueries & Subquery Optimization — scalar/row/column/table/correlated/EXISTS, semi-join rewrite — https://dev.mysql.com/doc/refman/8.4/en/subquery-optimization.html
[^devart-subquery]: Devart dbForge — MySQL Subqueries Guide: Types, Syntax and Best Practices — scalar/row/table/correlated, subquery in SELECT/WHERE/FROM/JOIN/GROUP BY/HAVING — https://www.devart.com/dbforge/mysql/studio/mysql-subqueries.html
[^villagesql-subquery]: VillageSQL — Subqueries vs JOINs in MySQL — IN vs EXISTS vs JOIN, NULL problem with NOT IN, derived tables — https://villagesql.com/docs/guides/subqueries-vs-joins
[^datacamp-subquery]: DataCamp — MySQL Efficient Use of Subqueries — prefer JOIN, EXISTS stops at first match — https://www.datacamp.com/doc/mysql/mysql-efficient-use-of-subqueries
[^codersrev-join]: Coder's Revolution — MySQL performance: INNER JOIN vs sub-select — 250K rows, ~30x faster after rewriting subquery to JOIN — https://www.codersrevolution.com/blog/MySQL-performance-INNER-JOIN-vs-subselect
[^mysql-optimization]: MySQL 8.4 Reference — Optimization & EXPLAIN Output Format — https://dev.mysql.com/doc/refman/8.4/en/optimization.html
[^mysql-explain]: MySQL 8.4 Reference — EXPLAIN Output Format — type, key, rows, Extra — https://dev.mysql.com/doc/refman/8.4/en/explain-output.html
[^oneuptime-optimization]: OneUptime — How to Handle Index Optimization in MySQL (2026-01-24) — single vs composite vs covering, leftmost prefix, EXPLAIN refunds — https://oneuptime.com/blog/post/2026-01-24-mysql-index-optimization/view

*Bài viết giữ `publish: false` đến khi `blog-verify` đạt BLOCKING:false. Vault-first: tổng hợp từ 7 notes wiki (`Database Indexing`, `B-Tree Index`, `Index`, `MySQL Constraints Relationship`, `MySQL Select Statement`, `MySQL Subquery`, `MySQL Join Table`) — 3079 words — và 20+ nguồn Tier 1-2 đã xác thực.*
