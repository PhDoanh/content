---
date: 2025-02-12
draft: false
status: Doing
title: Độ phức tạp thời gian của thuật toán
description: Bài viết này sẽ hướng dẫn bạn cách tính toán Độ phức tạp thời gian trong các thuật toán – từ những ví dụ đơn giản đến các trường hợp phức tạp hơn, qua đó giúp bạn chuẩn bị tốt hơn cho các cuộc thi lập trình
author: PhDoanh
authorlink: https://github.com/PhDoanh
tags:
  - cpp
  - dsa
  - coding
  - competitive
  - cph
  - basic
aliases:
  - time complexity
  - Độ phức tạp thời gian của thuật toán
cssclasses:
  - img
  - btn
---
%% ĐỊNH DẠNG TÊN FILE: "tên-bài-viết" | VD: jp-typing-guide %%

%% <figure style="text-align: center; margin: 20px auto;">
  <img 
    src="images/time-complexity.png"
    alt="Độ phức tạp thời gian của thuật toán" 
    style="
      width: 90%;
      height: auto;
      display: block;
      margin: 0 auto;
      border-radius: 8px;
      box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    "
  >
  <figcaption style="
    font-style: italic;
    color: #666;
    margin-top: 10px;
    font-size: 1em;
    padding: 0 10px;
  ">
    <em>caption</em>
  </figcaption>
</figure> %%

Trong thế giới lập trình và các cuộc thi thuật toán, **Độ phức tạp thời gian của thuật toán** là một khái niệm cốt lõi giúp đánh giá hiệu năng của một thuật toán. Bài viết này sẽ giới thiệu cơ bản về cách đo lường số lượng thao tác thực hiện, giải thích ý nghĩa của Big O notation, và cung cấp các ví dụ minh họa cụ thể. Bạn cũng sẽ được cung cấp các lưu ý, cảnh báo và mẹo giúp nhận biết khi nào thuật toán của bạn có thể bị “chậm” trong những trường hợp xử lý dữ liệu lớn.

# Khái niệm cơ bản về độ phức tạp thời gian

Trong lập trình, **Độ phức tạp thời gian của thuật toán** đo lường số lượng thao tác (operations) mà thuật toán thực hiện khi xử lý đầu vào có kích thước _n_. Để mô tả điều này, chúng ta sử dụng **Big O notation** – một cách biểu diễn giới hạn trên của số thao tác cần thực hiện khi _n_ tăng lên không giới hạn.

> [!info] Lưu ý
> Big O chỉ tính đến phần tăng trưởng của hàm số, bỏ qua các hệ số hằng số và các số hạng bậc thấp hơn.  [Tham khảo thêm về Big O notation](https://en.wikipedia.org/wiki/Big_O_notation)

---

# Tính toán độ phức tạp
## Thao tác hằng số
Đoạn mã sau có độ phức tạp **O(1)**, nghĩa là thời gian thực thi không thay đổi dù kích thước đầu vào có thay đổi:

```cpp
int a = 5;
int b = 7;
int c = 4;
int d = a + b + c + 153;
```

## Thao tác tuyến tính
Hai đoạn mã sau sẽ chạy với số lần lặp tỷ lệ thuận với *n* (độ phức tạp $O(n)$):

```cpp
for (int i = 1; i <= n; i++) {
    // xử lý thời gian hằng số ở đây
}
```

```cpp
int i = 0;
while (i < n) {
	// xử lý thời gian hằng số ở đây
	i++;
}
```

Vì bỏ qua các hằng số và số hạng bậc thấp hơn nên độ phức tạp các đoạn mã sau vẫn là $O(n)$ :

```cpp
for (int i = 1; i <= 5 * n + 17; i++) {
	// xử lý thời gian hằng số ở đây
}
```

## Câu lệnh vòng lặp
- **Vòng lặp đơn:** Khi sử dụng vòng lặp duy nhất chạy từ 1 đến _n_, thời gian chạy là **O(n)**.
- **Vòng lặp lồng nhau:** Nếu có vòng lặp bên trong chạy _m_ lần cho mỗi vòng lặp ngoài, ta sẽ có **O(n.m)**.

> [!caution]- Cảnh báo
> Khi thiết kế các thuật toán với vòng lặp lồng nhau, hãy cân nhắc đến trường hợp **worst-case** vì số lượng thao tác có thể tăng nhanh theo cấp số mũ.

## Tích hợp nhiều khối lệnh
Khi thuật toán bao gồm nhiều khối lệnh (blocks), tổng thời gian chạy được xác định bởi khối có độ phức tạp cao nhất:

```cpp
for (int i = 1; i <= n; i++) {
	for (int j = 1; j <= n; j++) {
		// xử lý thời gian hằng số ở đây
	}
}
for (int i = 1; i <= n + 2048; i++) {
	// xử lý thời gian hằng số ở đây
}
```

Một khối lệnh với độ phức tạp **O(n²)** kết hợp với một khối lệnh **O(n)** thì tổng độ phức tạp vẫn là **O(n²)**.

Nếu các khối lệnh có các độ phức tạp khác nhau và không thể bỏ qua số hạng nào, ta biểu diễn tổng bằng cách cộng các hàm số, nhưng trong Big O chỉ lấy phần tăng trưởng cao nhất:

```cpp
for (int i = 1; i <= n; i++) {
	for (int j = 1; j <= n; j++) {
		// xử lý thời gian hằng số ở đây
	}
}
for (int i = 1; i <= m; i++) {
	// xử lý thời gian hằng số ở đây
}
```

Đoạn code này có độ phức tạp **O(n² + m)**. Nếu _m_ không lớn bằng _n²_, phần **O(n²)** sẽ quyết định.

---

# Các độ phức tạp thông dụng và giới hạn đầu vào

## Các ví dụ phổ biến về độ phức tạp

Một số thuật toán và cấu trúc dữ liệu thường gặp cùng với độ phức tạp của chúng:
- **O(1):** Các phép tính toán học đơn giản, truy cập mảng.
- **O(log n):** Tìm kiếm nhị phân, thao tác trên cây cân bằng.
- **O(n):** Duyệt mảng, đọc dữ liệu từ input.
- **O(n log n):** Sắp xếp sử dụng thuật toán như mergesort, heapsort.
- **O(n²):** Các thuật toán có vòng lặp lồng nhau đơn giản.
- **O(2ⁿ) hoặc O(n!):** Các thuật toán duyệt tất cả các khả năng (exhaustive search).

## Giới hạn đầu vào và lựa chọn thuật toán

Tùy vào giới hạn của dữ liệu đầu vào, bạn cần chọn giải thuật phù hợp:

|      n       |   Độ phức tạp có thể xảy ra    |
|:------------:|:------------------------------:|
|   $n\le10$   |    $O(n!),~O(n^7),~O(n^6)$     |
|   $n\le20$   |       $O(2^n.n),~O(n^5)$       |
|   $n\le80$   |            $O(n^4)$            |
|  $n\le400$   |            $O(n^3)$            |
|  $n\le7500$  |            $O(n^2)$            |
| $n\le7.10^4$ |         $O(n\sqrt n)$          |
| $n\le5.10^5$ |          $O(n\log n)$          |
| $n\le5.10^6$ |             $O(n)$             |
|  $n\le10^8$  | $O(\log^2 n),~O(\log n),~O(1)$ |

- Với **n bé**: Bạn có thể dùng các thuật toán với độ phức tạp cao như **O(n!)** hoặc **O(2ⁿ)**.
- Với **n lớn**: Chỉ nên sử dụng các thuật toán tối ưu với độ phức tạp thấp như **O(n)**, **O(n log n)** hoặc **O(n²)** nếu có tối đa các tối ưu nhỏ.

> [!info] Lưu ý
> Sự lựa chọn thuật toán không chỉ phụ thuộc vào độ phức tạp lý thuyết mà còn vào **hệ số hằng số** – một yếu tố quan trọng trong thực tế.

---

# Hệ số hằng số và tác động thực tế
**Constant factors (hệ số hằng số)** trong thuật toán là những hằng số không phụ thuộc vào kích thước đầu vào *n* nhưng vẫn ảnh hưởng đến thời gian chạy thực tế của thuật toán (Mặc dù **Big O notation** bỏ qua chúng)

> [!example]- Ví dụ
> Giả sử ta có hai thuật toán cùng độ phức tạp Big O nhưng có tốc độ khác nhau trong thực tế:
> - **Thuật toán A**: Chạy trong **5n** bước → Độ phức tạp là **O(n)**
> - **Thuật toán B**: Chạy trong **100n** bước → Cũng là **O(n)** nhưng chậm hơn trong thực tế.
> 
> Cả hai thuật toán đều có **O(n)**, nhưng thuật toán B có **constant factor = 100**, nghĩa là nó thực hiện gấp **20 lần** số thao tác so với thuật toán A.

Khi đối mặt với **thời gian giới hạn** trong các cuộc thi, việc tối ưu hệ số hằng số (như giảm số phép tính dư thừa) có thể tránh được lỗi TLE (Time Limit Exceeded).

> [!tip] Mẹo tối ưu hiệu suất
> - **Phân tích kỹ vòng lặp:** Hãy kiểm tra xem có vòng lặp nào có thể gộp lại hoặc tối ưu không.
> - **Sử dụng cấu trúc dữ liệu phù hợp:** Ví dụ, ưu tiên **binary search** thay vì vòng lặp duyệt toàn bộ mảng khi dữ liệu đã được sắp xếp.
> - **Tránh lặp lại tính toán:** Lưu trữ kết quả trung gian nếu cần thiết (kỹ thuật memoization).
> - Đừng quên rằng ngay cả với cùng một Big O, việc cải thiện hệ số hằng số có thể đem lại lợi thế thực sự trong các bài toán cạnh tranh.

---

# Định nghĩa toán học của Big O
Giả sử có hai hàm số **f(n)** và **g(n)** không âm, nếu tồn tại các hằng số **c > 0** và **n₀** sao cho với mọi **n ≥ n₀**, ta có **f(n) ≤ c ⋅ g(n)**, thì nói **f(n) = O(g(n))**. Nói cách khác, khi _n_ đủ lớn, **f(n) không lớn hơn một bội số của g(n)**.

> [!example]- Ví dụ
> Xét 2 thuật toán với số bước chạy như sau:
> - $f(n)=5n^2+3n+10$
> - $g(n)=n^2$
> 
> Có thể chứng minh: $5n^2+3n+10 \lt 6n^2$ khi $n\ge10$
> $\Rightarrow f(n)=O(n^2)$. Điều này có nghĩa là khi _n_ đủ lớn, $f(n)$ không lớn hơn một bội số của $n^2$

> [!info] Lưu ý
> Trong Big O, ta luôn chọn biểu thức đơn giản nhất mô tả tốc độ tăng trưởng của hàm số.

---

# Tổng kết
Trong bài viết này, chúng ta đã cùng nhau khám phá:
- **Khái niệm cơ bản** về Độ phức tạp thời gian của thuật toán và **Big O notation**.
- **Phân tích các vòng lặp** và cách tính toán độ phức tạp từ các khối lệnh khác nhau.
- Các **độ phức tạp thông dụng** và **giới hạn đầu vào** giúp bạn chọn thuật toán phù hợp.
- **Hệ số hằng số** – yếu tố không được tính trong Big O nhưng rất quan trọng trong thực hành.

Hãy nhớ rằng, việc nắm vững **Độ phức tạp thời gian của thuật toán** không chỉ giúp bạn viết mã hiệu quả hơn mà còn cải thiện khả năng giải quyết các bài toán cạnh tranh. Đừng ngần ngại thử sức với các bài tập thực hành và tham gia các cộng đồng lập trình để trao đổi và học hỏi thêm nhiều mẹo hữu ích! 🌟
