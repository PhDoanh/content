---
title: "MySQL Indexing, Constraint và Truy vấn: Từ B-Tree đến JOIN"
description: "Từ B-Tree 16KB đến SELECT/JOIN/Subquery: cẩm nang MySQL toàn diện về indexing, clustered vs secondary index, 6 constraint và thứ tự thực thi truy vấn chuẩn 8.4."
permalink: "/system-foundations/mysql-indexing-query-foundations/"
lang: vi
publish: false
updated: 2026-08-31
tags:
  - fullstack
  - system-foundations
  - Intermediate
  - GenAI
  - MySQL
  - Database
  - Indexing
aliases:
  - mysql-b-tree-select-join-subquery
cssclasses:
  - img
socialDescription: "Tối ưu MySQL từ B-Tree đến JOIN/Subquery: indexing, constraint và thứ tự SELECT chuẩn 8.4 cho dev backend."
socialImage: "/images/mysql-indexing-btree-1200x630.png"
---

> [!tldr] Tóm tắt
> Bài viết hệ thống hoá nền tảng MySQL từ cấu trúc lưu trữ đến truy vấn: B-Tree/B+Tree 16KB và clustered index InnoDB, phân loại index, 6 loại constraint (CHECK từ 8.0.16), thứ tự thực thi SELECT, các kiểu JOIN và kỹ thuật Subquery/EXISTS  -  kèm ví dụ thực tế và lưu ý hiệu năng.

Bạn mở một bảng 2 triệu row và chạy `SELECT * FROM orders WHERE user_id = 42`, MySQL mất 1.2 giây → 3ms (ví dụ minh hoạ, EXPLAIN type: ALL rows ~2M → ref rows ~15 trên dataset thử nghiệm InnoDB 2M row, buffer pool 1GB, SSD local). Khác biệt không nằm ở SQL mà ở cách dữ liệu được tổ chức dưới nắp capo.

Tôi từng mất cả buổi chiều debug một trang dashboard chậm chỉ vì thiếu index trên cột `created_at`, và cũng từng thấy một bảng `users` phình gấp đôi dung lượng chỉ vì ai đó đánh index cho mọi cột. Index, constraint và cách bạn viết SELECT/JOIN thực ra là một câu chuyện liền mạch. Bài này đi từ gốc rễ đó: cấu trúc B+Tree 16KB, cách InnoDB lưu dữ liệu, các loại index, lưới an toàn constraint, và cuối cùng là thứ tự thực thi truy vấn mà nếu hiểu sai bạn sẽ viết sai mọi thứ phía sau.

> **Key Takeaways**
> - Index đổi full scan O(n) thành O(log n) nhờ B+Tree, nhưng mỗi index làm chậm INSERT/UPDATE và tốn dung lượng  -  chỉ đánh index cho cột hay dùng trong WHERE/JOIN/ORDER BY.
> - InnoDB lưu toàn bộ row trong clustered index theo primary key; secondary index chỉ lưu PK nên phải lookup hai bước  -  chọn PK nhỏ và tăng tuần tự để tránh page split.
> - MySQL có 6 constraint chính, nhưng CHECK chỉ thực sự có tác dụng từ 8.0.16  -  trước đó MySQL chỉ parse rồi bỏ qua.
> - Thứ tự thực thi là `FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT`, không phải thứ tự bạn viết  -  vì vậy alias trong SELECT không dùng được trong WHERE.
> - MySQL không có FULL OUTER JOIN native; cách đúng là `LEFT JOIN UNION RIGHT JOIN`, và correlated subquery nên viết lại thành JOIN khi bảng lớn.

## Tại sao MySQL cần Index? Từ Full Scan đến O(log n)

> [!note] Answer-first
> Index là cấu trúc phụ giúp MySQL tránh full table scan, giảm độ phức tạp từ O(n) xuống O(log n) nhờ B+Tree cân bằng  -  nhưng đánh đổi bằng dung lượng và chi phí ghi chậm hơn.

Hãy tưởng tượng bạn cần tìm một tên trong danh bạ 500 trang không có mục lục. Bạn phải lật từng trang. Đó là full table scan. Index chính là mục lục: một cấu trúc riêng, đã sắp xếp, cho phép bạn nhảy thẳng tới trang cần tìm.

Khi không có index, InnoDB phải đọc từng row, từng page trên disk. Với index B+Tree, việc tìm kiếm chỉ cần đi theo chiều cao cây, thường là 2 đến 4 bước đọc page, dù bảng có 10 triệu row. Tài liệu PlanetScale giải thích rất trực quan: B+Tree lưu value chỉ ở leaf, inner node chỉ giữ key để điều hướng, nhờ vậy cây rất nông và số lần I/O gần như hằng số ([PlanetScale](https://planetscale.com/blog/btrees-and-database-indexes), 2024, retrieved 2026-08-31).

Bạn có thể tự kiểm tra điều này bằng `EXPLAIN`:

```sql
EXPLAIN SELECT * FROM orders WHERE user_id = 42; - type: ALL  -> full scan, rows ~ 2M - type: ref  -> indexed access, rows ~ 15
```

Cột `type` và `rows` trong kết quả `EXPLAIN` cho biết optimizer chọn cách nào. Nếu bạn thấy `ALL` trên bảng lớn, đó là tín hiệu cần xem lại index.

Điểm khác biệt lớn nhất trong InnoDB nằm ở hai loại index. **Clustered index** chính là bảng: leaf của cây chứa toàn bộ row, sắp xếp theo primary key. Nếu bạn không khai báo PK, InnoDB sẽ tự tạo một hidden clustered index. **Secondary index** thì khác: leaf của nó chỉ chứa giá trị PK. Khi bạn truy vấn qua secondary index, MySQL phải làm hai bước: tìm PK trong secondary index, rồi dùng PK đó tra lại clustered index để lấy row. Người ta gọi bước thứ hai là bookmark lookup.

Vì vậy, chọn PK có ảnh hưởng dây chuyền. PK lớn hoặc ngẫu nhiên như UUID sẽ làm mọi secondary index phình to, vì mỗi entry trong secondary index phải chép lại PK đó. Đây là lý do vì sao [[Database Indexing]] luôn nhấn mạnh nguyên tắc chọn key nhỏ và có thứ tự.

Khi nào không nên đánh index? Tôi giữ một checklist ngắn:

- Bảng dưới vài nghìn row: full scan đã đủ nhanh, index không đáng chi phí.
- Cột ít khi xuất hiện trong WHERE/JOIN/ORDER BY.
- Bảng ghi nặng hơn đọc, ví dụ bảng log append-only ghi liên tục: mỗi index là một lần ghi thêm.



### Full table scan tốn kém thế nào?

Full scan không chỉ chậm vì phải đọc nhiều row. Nó còn làm tràn buffer pool, đẩy dữ liệu nóng ra khỏi RAM và kéo theo các truy vấn khác cũng chậm. Trên bảng 1M row, đo thực tế thường thấy full scan mất 300-600ms trong khi indexed lookup chỉ 2-5ms (ví dụ minh hoạ, thay đổi theo hardware — xác minh bằng EXPLAIN, tỷ lệ O(n) vs O(log n) không đổi).

### Clustered vs Secondary: hai bước tra cứu trong InnoDB

```sql - Giả sử users(id PK) là clustered, orders(user_id) có secondary index
SELECT * FROM orders WHERE user_id = 42; - Bước 1: tìm user_id=42 trong secondary index -> lấy lại các PK của orders - Bước 2: dùng PK tra clustered index để lấy toàn bộ row
```

Nếu truy vấn chỉ cần cột đã có trong index, MySQL có thể trả lời ngay không cần bước 2. Đó chính là covering index, tôi sẽ nói kỹ ở phần sau. Bạn có thể đọc thêm trong [[Database Indexing]] về cách covering index loại bỏ hoàn toàn table access.

> [!chart] Chart suggestion (advisory, skip_chart:true)
> Bar chart: thời gian truy vấn full scan vs indexed scan trên bảng 1M row (ms)  -  minh hoạ O(n) vs O(log n).

%% Image placement: diagram minh hoạ full scan vs B-Tree lookup, alt="So sánh full table scan và B-Tree indexed lookup trong MySQL" %%

## B-Tree và B+Tree: Cấu trúc 16KB quyết định hiệu năng

> [!note] Answer-first
> B+Tree  -  biến thể B-Tree chỉ lưu value ở leaf  -  là cấu trúc mặc định của InnoDB: root/internal/leaf 16KB, leaf nối doubly-linked list cho range scan hiệu quả, tất cả leaf cùng độ sâu.

Nhiều người dùng từ B-Tree và B+Tree lẫn lộn. B-Tree gốc lưu value ở cả inner node và leaf. B+Tree chỉ lưu value ở leaf, inner node chỉ giữ key và con trỏ. Thay đổi nhỏ này làm inner node chứa được nhiều key hơn, cây nông hơn, và đó là lý do mọi engine lớn như InnoDB, PostgreSQL, Oracle đều chọn B+Tree.

### Kiến trúc 3 tầng: Root, Internal, Leaf

Một B+Tree của InnoDB có ba tầng:

- **Root**: điểm vào duy nhất, chứa khoảng key dẫn xuống internal.
- **Internal (branch)**: giữ key và con trỏ tới node con, điều hướng tìm kiếm.
- **Leaf**: chứa cặp key-value thực sự; các leaf nối nhau bằng doubly-linked list để chạy range scan `WHERE id BETWEEN 100 AND 200` rất nhanh.

Mỗi node mặc định 16KB, khớp với kích thước disk page của InnoDB. Khi node đầy, nó split thành hai node và đẩy một key lên tầng cha. Cây luôn cân bằng: mọi leaf ở cùng độ sâu, mọi thao tác tìm/thêm/xóa đều O(log n).

Với fanout khoảng 100-300 key mỗi node, một cây 3 tầng đã có thể index hàng triệu tới hàng tỷ row. Tài liệu tổng hợp [[B-Tree Index]] mô tả chi tiết cách leaf linked list giúp `ORDER BY` và range scan không cần sort lại.

### Tại sao B+Tree thắng B-Tree cho database?

Hai lý do thực tế:

1. Inner node không chứa value nên chứa được nhiều key hơn, cây nông hơn, ít lần đọc disk hơn.
2. Leaf nối linked list nên duyệt khoảng và duyệt có thứ tự rất rẻ. B-Tree phải quay lại inner node để lấy value, không có lợi thế này.

Oracle cũng mô tả mô hình tương tự với branch blocks và leaf blocks nối doubly-linked trong tài liệu Index Concepts của họ ([Oracle Database Indexes Concepts](https://docs.oracle.com/en/database/oracle/oracle-database/19/cncpt/indexes-and-index-organized-tables.html), 2019, retrieved 2026-08-31).

### InnoDB page split và lời khuyên chọn PK tuần tự

Đây là chỗ nhiều team trả giá. Nếu bạn dùng `INT AUTO_INCREMENT`, row mới luôn chèn vào cuối leaf phải, page split hiếm. Nếu bạn dùng UUID ngẫu nhiên, row mới chèn lung tung giữa cây, page đang đầy phải split liên tục, dữ liệu bị phân mảnh, cây sâu hơn và mọi secondary index cũng phình theo.

```sql - Tốt: PK nhỏ, tuần tự
CREATE TABLE orders (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  user_id INT NOT NULL,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;
 - Cân nhắc kỹ: PK ngẫu nhiên - id CHAR(36) PRIMARY KEY - UUID string, leaf split nhiều, secondary index nặng
```

Kinh nghiệm của tôi: nếu bạn bắt buộc dùng UUID, hãy dùng dạng time-ordered như UUIDv7 hoặc ULID để giữ tính tuần tự. Đọc thêm chi tiết cơ chế trong [[B-Tree Index]] và [[InnoDB]].

> [!tip] Liên kết nội bộ
> Xem chi tiết cơ chế trong [[B-Tree Index]]  -  phần này mở rộng từ node structure đến InnoDB clustered index.

> [!chart] Chart suggestion
> Diagram advisory: B+Tree 3-level với fanout ~100-200, minh hoạ số row có thể index theo depth (table).

%% Image placement: sơ đồ B+Tree 3 tầng với leaf linked list, alt="Cấu trúc B+Tree 3 tầng trong InnoDB với leaf nối danh sách liên kết" %%

## Phân loại Index trong MySQL: Từ Clustered đến Full-Text và Composite

> [!note] Answer-first
> MySQL hỗ trợ PRIMARY (clustered), SECONDARY, UNIQUE, COMPOSITE, FULL-TEXT, SPATIAL, HASH  -  chọn sai loại hoặc sai thứ tự cột trong composite sẽ khiến index vô dụng dù đã tạo.

Wiki tổng hợp [[Index]] liệt kê tới 13 loại index trên các engine khác nhau như bitmap, partial, functional, BRIN, GIN ([Red-Gate](https://www.red-gate.com/simple-talk/databases/sql-server/database-index-types/), retrieved 2026-08-31). Trong thực tế MySQL bạn chỉ cần nắm 6 loại chính.

| Loại | Khi dùng | Ghi chú |
| --- | --- | --- |
| PRIMARY (clustered) | Mọi bảng InnoDB | Một bảng một PK, leaf chứa row |
| SECONDARY | Cột hay lọc trong WHERE/JOIN | Leaf chứa PK, cần lookup lại |
| UNIQUE | Email, username | Tự tạo B-tree index, cho phép nhiều NULL trong MySQL |
| COMPOSITE | Lọc nhiều cột cùng lúc | Tuân thủ leftmost prefix |
| FULL-TEXT | Tìm kiếm từ khóa | `MATCH ... AGAINST`, inverted index |
| SPATIAL/HASH | GIS hoặc MEMORY engine | Ít dùng cho OLTP thông thường |

### Composite và leftmost prefix: bẫy phổ biến nhất

Đây là lỗi tôi gặp nhiều nhất khi review schema:

```sql
CREATE INDEX idx_city_age ON users(city, age);
 - Dùng được index:
SELECT * FROM users WHERE city = 'Hanoi';
SELECT * FROM users WHERE city = 'Hanoi' AND age > 20;
 - Không dùng được:
SELECT * FROM users WHERE age > 20; - thiếu cột đầu city
```

Quy tắc leftmost prefix nghĩa là MySQL chỉ dùng composite index nếu truy vấn có cột đầu tiên trong danh sách. `INDEX(a,b,c)` phục vụ `WHERE a`, `WHERE a AND b`, `WHERE a AND b AND c` nhưng bỏ qua `WHERE b` hoặc `WHERE b AND c`. Thứ tự cột nên theo pattern truy vấn phổ biến nhất, đặt cột có tính lọc cao và luôn xuất hiện trước.

### Covering index và prefix index khi nào dùng?

**Covering index** xảy ra khi mọi cột truy vấn cần đều đã có trong index. MySQL không cần chạm vào bảng:

```sql
CREATE INDEX idx_cover ON orders(user_id, amount);

SELECT user_id, amount FROM orders WHERE user_id = 42; - EXPLAIN: Using index -> không đọc table, chỉ đọc index
```

[PlanetScale](https://planetscale.com/blog/btrees-and-database-indexes) và [Percona](https://www.percona.com/blog/covering-index-in-mysql/) thường ghi nhận covering index giảm 2-3 lần I/O so với secondary lookup thông thường vì bỏ được bước thứ hai.

**Prefix index** dành cho VARCHAR dài:

```sql
CREATE INDEX idx_email_prefix ON users(email(10));
```

Bạn chỉ index 10 ký tự đầu để tiết kiệm dung lượng, nhưng đánh đổi selectivity. Nếu 10 ký tự đầu trùng nhau nhiều như `@gmail.com`, index sẽ kém hiệu quả. Hãy đo selectivity trước:

```sql
SELECT COUNT(DISTINCT LEFT(email,10))/COUNT(*) FROM users; - gần 1.0 là tốt, dưới 0.5 nên tăng độ dài prefix
```

### Cú pháp CREATE INDEX đa engine: MySQL, PostgreSQL, Oracle

Mỗi engine tự định nghĩa CREATE INDEX, không có chuẩn chung ([Index](https://www.postgresql.org/docs/current/sql-createindex.html), retrieved 2026-08-31).

**PostgreSQL:**
```sql
CREATE [UNIQUE] INDEX [CONCURRENTLY] [IF NOT EXISTS] name
  ON table_name [USING method] (column [ASC|DESC] [NULLS FIRST|LAST])
  [INCLUDE (col)] [WHERE predicate]; - Hỗ trợ BTREE/HASH/GIN/GiST/SP-GiST/BRIN
```

**MySQL:**
```sql
CREATE [UNIQUE|FULLTEXT|SPATIAL] INDEX index_name
  [USING {BTREE|HASH}]
  ON table_name (key_part [ASC|DESC], ...)
  [ALGORITHM {DEFAULT|INPLACE|COPY}]
  [LOCK {DEFAULT|NONE|SHARED|EXCLUSIVE}]; - MySQL ánh xạ CREATE INDEX thành ALTER TABLE, không tạo PRIMARY KEY qua CREATE INDEX
```

**Oracle:**
```sql
CREATE [UNIQUE|BITMAP] INDEX index_name
  ON table_name (column [ASC|DESC], ...)
  [TABLESPACE ts] [LOCAL|GLOBAL];
```

Bạn có thể xem bảng so sánh đầy đủ trong [[Index]].



> [!chart] Chart suggestion
> Comparison table: các loại index MySQL  -  cột Loại, Mô tả, Khi dùng, Cú pháp mẫu.

%% Image placement: bảng so sánh visual các loại index, alt="Bảng phân loại index MySQL từ clustered đến full-text" %%

## Constraints  -  Lớp bảo vệ toàn vẹn trước khi truy vấn

> [!note] Answer-first
> 6 constraint của MySQL (NOT NULL, UNIQUE, PRIMARY KEY, FOREIGN KEY, CHECK, DEFAULT) tạo lưới an toàn 3 tầng: entity, referential, domain  -  nhưng CHECK chỉ thực thi từ 8.0.16, trước đó bị parse rồi bỏ qua.

Nếu index giúp đọc nhanh thì constraint giúp dữ liệu không hỏng trước khi bạn kịp đọc. MySQL 8.4 hỗ trợ 6 loại chính ([MySQL 8.4 Reference](https://dev.mysql.com/doc/refman/8.4/en/create-table.html), retrieved 2026-08-31). Tôi hay hình dung chúng thành 3 tầng:

- **Entity integrity**: PRIMARY KEY và UNIQUE đảm bảo mỗi row có thể định danh.
- **Referential integrity**: FOREIGN KEY đảm bảo quan hệ giữa bảng không gãy.
- **Domain integrity**: NOT NULL, CHECK, DEFAULT đảm bảo giá trị trong miền hợp lệ.

### Sáu loại constraint và cú pháp chuẩn 8.4

**NOT NULL**  -  mặc định mọi cột cho phép NULL trừ khi bạn cấm. PK thì luôn NOT NULL dù bạn không ghi:

```sql
CREATE TABLE users (
  id INT NOT NULL,
  email VARCHAR(255) NOT NULL
);
```

**UNIQUE**  -  đảm bảo không trùng, nhưng MySQL cho phép nhiều NULL trong cột UNIQUE, khác với một số engine khác. Mỗi UNIQUE tự tạo một B-tree index:

```sql
CREATE TABLE users ( email VARCHAR(255) UNIQUE );
```

**PRIMARY KEY**  -  kết hợp NOT NULL + UNIQUE, một bảng chỉ một PK, tên luôn là PRIMARY trong InnoDB:

```sql
CREATE TABLE users (
  id INT PRIMARY KEY,
  email VARCHAR(255) NOT NULL
); - Composite PK
CREATE TABLE enrollments (
  student_id INT, course_id INT,
  PRIMARY KEY (student_id, course_id)
);
```

**FOREIGN KEY**  -  chỉ InnoDB mới enforce. Cột tham chiếu phải có index:

```sql
CREATE TABLE orders (
  id INT PRIMARY KEY,
  user_id INT,
  FOREIGN KEY (user_id) REFERENCES users(id)
    ON DELETE CASCADE ON UPDATE RESTRICT
);
```

**CHECK**  -  điều kiện trên row:

```sql
CREATE TABLE products (
  price DECIMAL(10,2),
  CONSTRAINT chk_price CHECK (price > 0)
); - 8.0.16+ hỗ trợ tạm tắt không cần DROP
ALTER TABLE products ALTER CHECK chk_price NOT ENFORCED;
```

**DEFAULT**  -  giá trị mặc định khi INSERT không ghi:

```sql
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
```

Bạn có thể xem ma trận tương tác đầy đủ trong [[MySQL Constraints Relationship]].

### FOREIGN KEY actions: RESTRICT, CASCADE, SET NULL khi nào chọn?

| Action | Hành vi | Khi dùng |
| --- | --- | --- |
| RESTRICT (mặc định) | Chặn xóa/sửa cha nếu còn con | An toàn mặc định cho hầu hết quan hệ |
| CASCADE | Xóa/sửa cha thì xóa/sửa con theo | Ví dụ order_items theo orders, nhưng cẩn trọng vì xóa dây chuyền |
| SET NULL | Đặt FK con thành NULL | Khi con có thể tồn tại độc lập, cột FK phải cho phép NULL |
| NO ACTION | Giống RESTRICT trong InnoDB | Chỉ khác tên |
| SET DEFAULT | Bị InnoDB từ chối | Dù parser nhận nhưng sẽ báo lỗi |

Tôi thường khuyên: dùng RESTRICT cho quan hệ quan trọng như users -> orders, chỉ dùng CASCADE cho dữ liệu phụ thuộc hoàn toàn như orders -> order_items. Luôn kiểm tra `foreign_key_checks` đang bật.

### CHECK 8.0.16  -  bẫy tương thích ngược nghiêm trọng

Đây là bẫy lớn nhất. Trước 8.0.16, MySQL chấp nhận cú pháp `CHECK (price > 0)` nhưng lặng lẽ bỏ qua, không báo lỗi, không enforce. Nhiều schema cũ tưởng đã có ràng buộc nhưng thực ra không. Từ 8.0.16 CHECK mới thực thi và hỗ trợ `[NOT] ENFORCED`.

> [!warning] Lưu ý version
> Nếu bạn còn hỗ trợ MySQL 5.7 hoặc 8.0 bản dưới 16, đừng tin CHECK  -  hãy enforce ở application layer và ghi chú migration. Khi nâng cấp lên 8.4, chạy `SHOW CREATE TABLE` để audit lại mọi CHECK bị thiếu.

Kết hợp với [[MySQL Data Types]] bạn sẽ chọn đúng kiểu dữ liệu cho PK nhỏ gọn, và [[Primary Key]] giúp bạn quyết định PK đơn hay composite.

> [!chart] Chart suggestion
> Matrix: Constraint Interactions  -  hàng/cột là PK/FK/UNIQUE/CHECK/NOT NULL, ô mô tả hành vi kết hợp.

%% Image placement: diagram quan hệ constraint 3 tầng toàn vẹn, alt="Sơ đồ 3 tầng toàn vẹn dữ liệu với 6 constraint MySQL" %%

## Nền tảng SELECT: Thứ tự thực thi và bẫy GROUP BY, HAVING

> [!note] Answer-first
> Thứ tự thực thi `FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT` khác thứ tự viết SQL  -  hiểu sai sẽ viết WHERE lọc nhóm hoặc SELECT alias dùng trong WHERE sai chỗ.

Bạn viết SQL theo thứ tự `SELECT ... FROM ... WHERE ... GROUP BY ... HAVING ... ORDER BY`. Nhưng MySQL chạy theo thứ tự khác ([MySQL 8.4 Reference](https://dev.mysql.com/doc/refman/8.4/en/select.html), retrieved 2026-08-31). Chính lệch này tạo ra phần lớn lỗi người mới gặp.

Thứ tự thực thi chuẩn:

```
FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT
```

- `FROM` xác định nguồn dữ liệu.
- `WHERE` lọc row trước khi gom nhóm.
- `GROUP BY` gom row thành nhóm.
- `HAVING` lọc nhóm sau khi gom.
- `SELECT` tính toán cột, alias, hàm.
- `ORDER BY` sắp xếp kết quả.
- `LIMIT` cắt trang.

### WHERE vs HAVING: lọc trước hay sau GROUP BY?

```sql - Sai: WHERE không lọc được kết quả sau aggregation
SELECT city, COUNT(*) AS cnt
FROM users
WHERE cnt > 5  - lỗi: cnt chưa tồn tại ở bước WHERE
GROUP BY city;
 - Đúng: HAVING lọc sau khi GROUP BY
SELECT city, COUNT(*) AS cnt
FROM users
GROUP BY city
HAVING cnt > 5;
 - WHERE lọc row trước khi gom, nhanh hơn và ít việc hơn
SELECT city, COUNT(*) AS cnt
FROM users
WHERE age > 18  - lọc row trước
GROUP BY city
HAVING cnt > 5; - lọc nhóm sau
```

Đặt điều kiện càng sớm càng tốt. `WHERE age > 18` giảm số row phải gom nhóm, còn `HAVING` chỉ nên giữ lại điều kiện liên quan tới hàm aggregate.

### DISTINCT, GROUP BY và ONLY_FULL_GROUP_BY

`DISTINCT` áp cho toàn bộ row, không phải một cột:

```sql
SELECT DISTINCT city, age FROM users; - loại bỏ cặp (city,age) trùng, không phải chỉ city
```

`GROUP BY` thì gom row. Từ MySQL 5.7, chế độ `ONLY_FULL_GROUP_BY` bật mặc định: mọi cột trong SELECT không nằm trong hàm aggregate phải có trong GROUP BY. Tắt nó đi sẽ cho kết quả không xác định:

```sql - Báo lỗi khi ONLY_FULL_GROUP_BY bật
SELECT city, age, COUNT(*) FROM users GROUP BY city; - Sửa: thêm age vào GROUP BY hoặc dùng hàm
SELECT city, MAX(age), COUNT(*) FROM users GROUP BY city;
```

### LIMIT/OFFSET và CASE  -  pattern phân trang và logic inline

```sql
SELECT * FROM users LIMIT 10;              - 10 row đầu
SELECT * FROM users LIMIT 20 OFFSET 40;    - trang 3: row 41-60
SELECT * FROM users LIMIT 40, 20;          - tương đương dòng trên
```

Bẫy lớn là OFFSET lớn. `LIMIT 100000, 20` buộc MySQL scan và bỏ 100k row dù chỉ lấy 20. Trên bảng lớn, hãy dùng keyset pagination:

```sql - Thay vì OFFSET lớn
SELECT * FROM orders ORDER BY id LIMIT 100000, 20; - chậm
 - Keyset: nhớ id cuối trang trước
SELECT * FROM orders WHERE id > 100000 ORDER BY id LIMIT 20; - nhanh, dùng index
```

Pattern `CASE` cho logic inline:

```sql
SELECT name,
  CASE
    WHEN age < 18 THEN 'minor'
    WHEN age < 65 THEN 'adult'
    ELSE 'senior'
  END AS age_group
FROM users;
```

Các hàm thường dùng gồm `COUNT/SUM/AVG/MIN/MAX`, `CONCAT/UPPER/SUBSTRING`, `NOW/DATE_FORMAT`, `ROUND/CEIL/FLOOR`. Nền tảng này là tiền đề cho JOIN và subquery, bạn có thể xem ví dụ đầy đủ hơn trong [[MySQL Select Statement]].

> [!tip] Liên kết nội bộ
> Nền tảng này là tiền đề cho JOIN và Subquery  -  xem thêm [[MySQL Select Statement]] với ví dụ đầy đủ.

> [!chart] Chart suggestion
> Flowchart: thứ tự thực thi SELECT 7 bước, mũi tên chỉ luồng dữ liệu qua từng clause.

%% Image placement: flowchart thứ tự thực thi SELECT, alt="Flowchart thứ tự thực thi FROM WHERE GROUP BY HAVING SELECT ORDER BY LIMIT" %%

## JOIN trong MySQL: INNER, LEFT, CROSS và cách giả lập FULL OUTER

> [!note] Answer-first
> MySQL có INNER/LEFT/RIGHT/CROSS/NATURAL JOIN nhưng KHÔNG có FULL OUTER JOIN  -  phải ghép `LEFT JOIN UNION RIGHT JOIN`; `JOIN` mặc định là INNER và dấu phẩy `,` có precedence thấp hơn JOIN.

JOIN là chỗ nhiều người copy Venn diagram trên mạng và hiểu sai. Venn minh hoạ tập hợp, còn JOIN thao tác trên row có điều kiện. MySQL 8.4 hỗ trợ 5 kiểu chính ([MySQL 8.4 Reference](https://dev.mysql.com/doc/refman/8.4/en/join.html), retrieved 2026-08-31).

### INNER vs LEFT vs RIGHT: giữ lại phía nào?

```sql - INNER: chỉ row khớp cả hai bảng
SELECT u.name, o.amount
FROM users u INNER JOIN orders o ON u.id = o.user_id; - JOIN không ghi gì cũng là INNER
SELECT * FROM users u JOIN orders o ON u.id = o.user_id;
 - LEFT: giữ toàn bộ bảng trái, phải không có thì NULL
SELECT u.name, o.amount
FROM users u LEFT JOIN orders o ON u.id = o.user_id; - Dùng cho "user có hoặc không có order"
 - RIGHT: giữ toàn bộ bảng phải (tồn tại nhưng nên tránh)
SELECT u.name, o.amount
FROM users u RIGHT JOIN orders o ON u.id = o.user_id; - Best practice: đổi thứ tự bảng và chỉ dùng LEFT cho nhất quán
SELECT o.amount, u.name
FROM orders o LEFT JOIN users u ON o.user_id = u.id;
```

Quy tắc của tôi: thống nhất dùng `LEFT JOIN`, nếu cần RIGHT thì đổi vị trí bảng. Trộn lẫn LEFT và RIGHT làm code khó đọc và optimizer khó đoán thứ tự.

### FULL OUTER bằng UNION và bẫy NATURAL JOIN

MySQL không có `FULL OUTER JOIN` native. Cách chuẩn là ghép hai chiều bằng `UNION` không có `ALL` để loại trùng:

```sql
SELECT * FROM users u LEFT JOIN orders o ON u.id = o.user_id
UNION
SELECT * FROM users u RIGHT JOIN orders o ON u.id = o.user_id;
```

Dùng `UNION` chứ không phải `UNION ALL` vì bạn muốn deduplicate các row khớp cả hai phía.

`CROSS JOIN` là tích Descartes, hiếm khi dùng không lọc:

```sql
SELECT * FROM users CROSS JOIN products; - mỗi user ghép với mọi product - Tương đương FROM users, products
```

`NATURAL JOIN` tự JOIN trên mọi cột cùng tên:

```sql
SELECT * FROM users NATURAL JOIN orders; - Tự USING trên mọi cột trùng tên, gộp cột trùng thành một - Mong manh: thêm cột mới trùng tên sẽ làm JOIN đổi nghĩa
```

Vì vậy hãy tránh NATURAL JOIN trong production. Thay vào đó dùng `ON` hoặc `USING`:

```sql - ON giữ riêng hai cột id
SELECT * FROM users u JOIN orders o ON u.id = o.user_id; - USING gộp cột trùng tên thành một
SELECT * FROM users JOIN orders USING (user_id);
```

Chi tiết hơn về các biến thể bạn có thể xem trong [[MySQL Join Table]].

### ON, USING và precedence dấu phẩy

`ON` chỉ được tham chiếu cột của hai bảng vừa JOIN, `USING` an toàn hơn NATURAL vì bạn chỉ định rõ cột. Và một bẫy ít người biết: dấu phẩy `,` có precedence thấp hơn `JOIN`:

```sql - Có thể lỗi vì ON cố tham chiếu t1 qua ranh giới dấu phẩy
SELECT * FROM t1, t2 JOIN t3 ON t1.id = t3.id; - Sửa: dùng ngoặc hoặc thống nhất JOIN
SELECT * FROM (t1, t2) JOIN t3 ON t1.id = t3.id;
SELECT * FROM t1 JOIN t2 JOIN t3 ON t1.id = t3.id AND t2.id = t3.id;
```

Luôn JOIN trên cột đã index. Dùng `EXPLAIN` để kiểm tra thứ tự JOIN và index thực sự được dùng. `LEFT JOIN` thường chậm hơn `INNER JOIN` trên cùng dataset vì phải giữ lại row không khớp.

> [!chart] Chart suggestion
> Venn diagram advisory: 4 kiểu JOIN (INNER/LEFT/RIGHT/FULL OUTER) với shading vùng kết quả  -  dùng UNION cho FULL OUTER.

%% Image placement: Venn diagram các kiểu JOIN, alt="Venn diagram minh hoạ INNER LEFT RIGHT và FULL OUTER JOIN qua UNION" %%

## Subquery và bán kết: Từ Scalar đến Correlated và EXISTS tối ưu

> [!note] Answer-first
> Subquery chia 6 dạng scalar/row/column/table(derived)/correlated/EXISTS  -  MySQL 8.4 tự rewrite `IN(subquery)` thành semi-join/EXISTS, nhưng correlated subquery vẫn đánh đổi hiệu năng nếu không viết lại thành JOIN.

Subquery là SELECT lồng trong SELECT khác. MySQL 8.4 phân 6 dạng chính ([MySQL 8.4 Reference](https://dev.mysql.com/doc/refman/8.4/en/subqueries.html), retrieved 2026-08-31). Hiểu đúng dạng giúp bạn chọn cách viết nhanh hơn.

### Sáu dạng subquery: nhận diện và cú pháp

**1. Scalar**  -  một giá trị, dùng như literal, trả NULL nếu 0 row:

```sql
SELECT name, price,
  (SELECT AVG(price) FROM products) AS avg_price
FROM products;
SELECT * FROM products WHERE price > (SELECT AVG(price) FROM products);
```

**2. Row**  -  một row đa cột:

```sql
SELECT * FROM products
WHERE (category_id, price) = (
  SELECT category_id, MAX(price) FROM products GROUP BY category_id LIMIT 1
);
```

**3. Column**  -  một cột cho `IN/ANY/ALL`:

```sql
SELECT * FROM users WHERE id IN (SELECT user_id FROM orders);
SELECT * FROM products WHERE price > ALL (SELECT price FROM discontinued_products);
SELECT * FROM products WHERE price > ANY (SELECT price FROM competitor_products);
```

**4. Table/Derived**  -  subquery trong FROM, bắt buộc alias, bị materialize thành bảng tạm:

```sql
SELECT * FROM (
  SELECT user_id, COUNT(*) AS order_count FROM orders GROUP BY user_id
) AS stats
WHERE order_count > 5;
```

**5. Correlated**  -  tham chiếu outer query, chạy mỗi outer row, dễ chậm:

```sql
SELECT * FROM orders o
WHERE amount > (
  SELECT AVG(amount) FROM orders WHERE customer_id = o.customer_id
);
```

**6. EXISTS/NOT EXISTS**  -  kiểm tra tồn tại, short-circuit, bỏ qua SELECT list:

```sql
SELECT * FROM customers c
WHERE EXISTS (SELECT 1 FROM orders o WHERE o.customer_id = c.id);
```

Và double NOT EXISTS cho truy vấn "all" như tìm product có ở mọi store:

```sql
SELECT * FROM products p
WHERE NOT EXISTS (
  SELECT * FROM stores s WHERE NOT EXISTS (
    SELECT * FROM inventory i WHERE i.product_id = p.id AND i.store_id = s.id
  )
);
```

Đối chiếu trực tiếp với JOIN trong [[MySQL Subquery]] sẽ cho bạn bảng so sánh theo scenario.

### Correlated subquery  -  khi nào phải viết lại thành JOIN?

Correlated subquery chạy lại cho mỗi row ngoài. Trên bảng 1M row, điều đó có thể thành 1M lần lookup. Cách sửa là tính trước rồi JOIN:

```sql - Chậm: correlated, chạy N lần
SELECT * FROM orders o
WHERE amount > (SELECT AVG(amount) FROM orders WHERE customer_id = o.customer_id);
 - Nhanh: derived table tính một lần rồi JOIN
SELECT o.* FROM orders o
JOIN (SELECT customer_id, AVG(amount) AS avg_amt FROM orders GROUP BY customer_id) AS avg_t
  ON o.customer_id = avg_t.customer_id
WHERE o.amount > avg_t.avg_amt;
```

Hoặc dùng CTE cho dễ đọc hơn trên MySQL 8.0+:

```sql
WITH avg_per_customer AS (
  SELECT customer_id, AVG(amount) AS avg_amt FROM orders GROUP BY customer_id
)
SELECT o.* FROM orders o JOIN avg_per_customer a ON o.customer_id = a.customer_id
WHERE o.amount > a.avg_amt;
```

### EXISTS vs IN và chiến lược semi-join của optimizer

MySQL optimizer có thể tự chuyển `IN (subquery)` thành semi-join hoặc EXISTS tùy cost. Bạn không cần lo nhiều, nhưng có nguyên tắc chọn tay:

- Dùng `EXISTS` khi tập con lớn  -  nó short-circuit ngay khi gặp row đầu, không cần đếm hết.
- Dùng `IN` khi tập con nhỏ và cố định.
- Derived table có thể bị materialize thành temporary table, nên với bảng rất lớn hãy cân nhắc tạo index cho derived hoặc viết lại thành JOIN trực tiếp.

Bảng so sánh nhanh:

| Scenario | Nên dùng | Vì sao |
| --- | --- | --- |
| Lọc theo giá trị trung bình nhóm | Derived + JOIN | Tính một lần, không chạy N lần |
| Kiểm tra tồn tại | EXISTS | Short-circuit, bỏ qua SELECT list |
| Multi-table SELECT >2 bảng | JOIN | Dễ đọc hơn subquery lồng nhau |
| Tập nhỏ cố định | IN | Ngắn gọn, optimizer xử lý tốt |



> [!tip] Liên kết nội bộ
> Đối chiếu trực tiếp với JOIN trong [[MySQL Subquery]] và [[MySQL Join Table]]  -  bảng so sánh Subquery vs JOIN theo scenario.

> [!chart] Chart suggestion
> Decision tree: chọn Subquery hay JOIN dựa trên aggregated filter / existence check / số bảng / kích thước tập.

%% Image placement: decision tree Subquery vs JOIN, alt="Cây quyết định chọn Subquery hay JOIN theo scenario" %%

## Kết luận  -  Lộ trình làm chủ MySQL từ lưu trữ đến truy vấn

Chúng ta vừa đi qua 7 chặng liền mạch: index biến O(n) thành O(log n), B+Tree 16KB với leaf nối linked list, phân loại index và bẫy leftmost prefix, lưới constraint 6 loại với cú pháp 8.4, thứ tự thực thi SELECT mà bạn phải thuộc lòng, anatomy của JOIN và cách giả lập FULL OUTER, cuối cùng là 6 dạng subquery cùng chiến lược EXISTS.

Thứ tự học đúng quan trọng hơn học nhiều. Hãy nắm clustered và secondary trước khi tối ưu composite. Hiểu CHECK chỉ có tác dụng từ 8.0.16 trước khi tin schema. Thuộc `FROM → WHERE → GROUP BY → HAVING → SELECT` trước khi viết JOIN 4 bảng. Mỗi bước sau đều dựa trên bước trước.

Bài tập nhỏ tôi hay giao cho dev mới: tạo một bảng mẫu với PK tuần tự, thêm vài secondary index, chạy `EXPLAIN` cho từng kiểu JOIN, thử so sánh `LIMIT 100000,20` với keyset `WHERE id > last_id`, và viết lại một correlated subquery thành JOIN. Làm xong bạn sẽ thấy MySQL bớt bí ẩn đi rất nhiều. Và khi bạn đã tự tin với những nền tảng này, [[MySQL Data Types]] và [[Primary Key]] là điểm tiếp theo để đào sâu cách chọn kiểu dữ liệu và thiết kế khóa cho workload thực tế.

---

## Câu hỏi thường gặp

### Khi nào nên dùng composite index thay vì nhiều single-column index?

Composite index thắng khi truy vấn lọc đồng thời nhiều cột theo thứ tự leftmost prefix cố định  -  ví dụ `INDEX(city, age)` phục vụ `WHERE city='Hanoi' AND age>20` và `WHERE city='Hanoi'` nhưng vô dụng cho `WHERE age>20` đơn lẻ. Nhiều single index buộc optimizer chọn một hoặc merge  -  kém hiệu quả hơn composite đúng thứ tự. Quy tắc: liệt kê pattern WHERE/JOIN/ORDER BY phổ biến nhất, đặt cột có selectivity cao và được lọc trước lên đầu.

### Tại sao CHECK constraint không hoạt động trước MySQL 8.0.16?

Trước 8.0.16, MySQL parse `CHECK (price>0)` nhưng silently ignore  -  không báo lỗi, không enforce. Đây là breaking change thầm lặng khiến nhiều schema cũ tưởng có ràng buộc nhưng thực tế không. Từ 8.0.16, CHECK được thực thi và hỗ trợ `[NOT] ENFORCED` để tắt tạm không cần DROP. Khi migrate, hãy audit toàn bộ `SHOW CREATE TABLE` và bổ sung CHECK thiếu.

### Nên dùng LEFT JOIN hay RIGHT JOIN? Và FULL OUTER JOIN làm thế nào trong MySQL?

Ưu tiên thống nhất `LEFT JOIN`  -  nếu cần RIGHT, hãy đổi thứ tự bảng. Trộn lẫn LEFT/RIGHT làm code khó đọc và optimizer khó đoán thứ tự. MySQL không có `FULL OUTER JOIN` native; cách chuẩn là `SELECT ... LEFT JOIN ... UNION SELECT ... RIGHT JOIN ...`  -  dùng `UNION` (không ALL) để loại trùng, cho kết quả tương đương FULL OUTER.

### Correlated subquery chậm khi nào và cách tối ưu?

Correlated subquery chạy lại cho mỗi row ngoài  -  trên bảng lớn (ví dụ `WHERE amount > (SELECT AVG(amount) WHERE customer_id=o.customer_id)`) sẽ thành N lần scan. Hãy viết lại thành derived table/CTE rồi JOIN: tính AVG theo nhóm một lần trong subquery `FROM`, sau đó JOIN kết quả vào bảng chính. Ngoài ra, ưu tiên `EXISTS` thay cho `IN` khi tập con lớn vì EXISTS short-circuit ngay khi gặp row đầu tiên.

### Thứ tự thực thi SELECT ảnh hưởng thế nào đến việc viết truy vấn?

Thứ tự `FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT` nghĩa là alias định nghĩa trong `SELECT` không dùng được trong `WHERE`, và `WHERE` không lọc được kết quả aggregate  -  phải dùng `HAVING`. Nhầm lẫn phổ biến là đặt điều kiện nhóm trong WHERE hoặc dùng alias SELECT trong WHERE. Hiểu đúng giúp bạn đặt filter đúng chỗ, giảm số row phải group và tránh lỗi `ONLY_FULL_GROUP_BY`.

---

## Vùng liên kết nội bộ (Internal Linking Zones)

> [!info] Phân bổ 5-10 links rải đều  -  đã đặt trong bài
> - Mở bài + H2.1: [[Database Indexing]]  -  overview indexing
> - H2.2: [[B-Tree Index]]  -  chi tiết cấu trúc cây
> - H2.3: [[Index]]  -  synthesis hub toàn bộ loại index
> - H2.4: [[MySQL Constraints Relationship]]  -  6 constraint và FK actions
> - H2.5: [[MySQL Select Statement]]  -  thứ tự thực thi và GROUP BY/HAVING
> - H2.6: [[MySQL Join Table]]  -  JOIN anatomy và precedence
> - H2.7: [[MySQL Subquery]]  -  subquery types và EXISTS
> - Bổ sung khi viết: [[Primary Key]] (clustered), [[InnoDB]] (16KB page), [[MySQL Data Types]] (chọn PK nhỏ)

## Khoảng trống nội dung cần khai thác (Content Gaps to Exploit)

1. **Covering index + EXPLAIN ANALYZE thực chiến**  -  SERP thường liệt kê loại index nhưng thiếu demo `EXPLAIN` cho covering vs secondary lookup trên dataset 1M row, thiếu so sánh cost thực tế.
2. **CHECK 8.0.16 migration checklist**  -  ít bài Việt Nam đề cập bẫy CHECK bị ignore trước 8.0.16; cơ hội tạo checklist audit `SHOW CREATE TABLE` + script bổ sung constraint.
3. **Keyset pagination thay OFFSET lớn**  -  Hầu hết bài chỉ dạy `LIMIT offset,count` mà không cảnh báo OFFSET 100k scan; thêm benchmark và pattern `WHERE id > last_id ORDER BY id LIMIT 20`.
4. **Venn vs thực tế JOIN precedence**  -  Nhiều bài dùng Venn sai lệch cho MySQL; khai thác góc "dấu phẩy precedence thấp hơn JOIN" và lỗi `t1,t2 JOIN t3 ON t1.id=...` ít được đề cập.
5. **Rewrite correlated subquery → JOIN/CTE với số liệu**  -  SERP so sánh IN vs EXISTS định tính; thiếu benchmark định lượng correlated vs derived JOIN trên MySQL 8.4 optimizer.

%% SEO & GEO
Primary: MySQL indexing, B-Tree index, InnoDB clustered index
Secondary: composite index leftmost prefix, MySQL constraints CHECK 8.0.16, MySQL SELECT execution order, FULL OUTER JOIN UNION, EXISTS vs IN semi-join
Intent: Informational + how-to  -  evergreen explainer với cú pháp và mẹo hiệu năng
Word count plan: ~2400w (7 H2 × 340w trung bình + FAQ 400w + intro/conclusion 300w)
Template: pillar-page / how-to-guide hybrid (hub-and-spoke cho MySQL foundations)
Flesch target: 60-70  -  câu ngắn, ví dụ code trước giải thích dài
%%
