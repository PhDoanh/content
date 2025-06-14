---
date: 2025-02-12
draft: false
status: Doing
title: Giới thiệu về Cấu trúc dữ liệu
description: Bài viết này sẽ giúp bạn làm quen với các cấu trúc dữ liệu qua đó hiểu được tại sao việc lựa chọn cấu trúc phù hợp lại là chìa khóa trong việc tối ưu hóa giải pháp.
author: PhDoanh
authorlink: https://github.com/PhDoanh
tags:
  - coding
  - data-structure
  - competitive
  - cpp
  - basic
aliases:
  - data structures intro
cssclasses:
  - img
  - btn
---
%% ĐỊNH DẠNG TÊN FILE: "tên-bài-viết" | VD: jp-typing-guide %%

%% <figure style="text-align: center; margin: 20px auto;">
  <img 
    src="images/data-structures-intro.png"
    alt="Giới thiệu về Cấu trúc dữ liệu" 
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

Các **cấu trúc dữ liệu** xác định cách dữ liệu được tổ chức và quản lý, cho phép thực hiện các thao tác như **chèn, xoá, duyệt** một cách hiệu quả. Mỗi cấu trúc có ưu – nhược điểm riêng, do đó, việc lựa chọn cấu trúc phù hợp với bài toán là rất quan trọng.

> [!info] Lưu ý
> Một cấu trúc dữ liệu không chỉ quyết định cách bạn lưu trữ dữ liệu mà còn ảnh hưởng đến **hiệu suất** của các thao tác xử lý.

# Mảng (Arrays)
**Arrays** (còn được gọi là mảng tĩnh) là một trong những cấu trúc dữ liệu đơn giản và cơ bản nhất. Đây là cấu trúc điển hình thường thấy trong các kì thi đấu lập trình. Dưới đây là một số điểm chính về mảng:

- **Khai báo**  
```cpp
int arr[25];
```

hoặc 

```cpp
#include <array>
std::array<int, 25> arr;
```

- **Phương thức hỗ trợ**
Hầu hết các mảng (bao gồm mảng động như `vector`) đều hỗ trợ các hàm như **`size()`** để lấy số lượng phần tử và **`empty()`** để kiểm tra rỗng.

- **Khởi tạo:**  
```cpp
int arr[25]{};  // C++ khởi tạo các phần tử bằng 0
```

> [!tip]- Mẹo
> Sử dụng các hàm như **`std::fill`** hay **`std::fill_n`** để khởi tạo mảng nếu cần thiết.

---

# Mảng Động (Dynamic Arrays)
Đây là cấu trúc dữ liệu linh hoạt cho phép thay đổi kích thước khi chương trình chạy, rất hữu ích trong các bài toán khi kích thước dữ liệu không xác định trước. Dưới đây là một số điểm chính về mảng động:

- **Sử dụng vector trong C++:**
```cpp
#include <vector>
std::vector<int> v;
for (int i = 1; i <= 10; i++) {
    v.push_back(i);
}

```

- **Lợi ích:**
    - Tự động điều chỉnh kích thước khi thêm hoặc xoá phần tử.
    - Cho phép thao tác thêm, xoá phần tử ở cuối mảng trong **O(1)** thời gian trung bình.

> [!caution]- Cảnh báo
> Chèn hay xoá phần tử ở giữa mảng có độ phức tạp **O(n)**, do phải dịch chuyển các phần tử còn lại.

> [!tip]- Mẹo
> Khi cần mảng với kích thước biến đổi, hãy ưu tiên dùng **`vector`** thay vì các mảng tĩnh.

---

# Duyệt mảng (Iterating)
Mình sẽ giới thiệu về các phương pháp duyệt qua các phần tử của mảng, từ cách duyệt truyền thống bằng vòng lặp for đến sử dụng **iterator** và **for-each loop**.

## Duyệt bằng vòng lặp for
```cpp
for (int i = 0; i < int(v.size()); i++) {
    std::cout << v[i] << " ";
}
```

## Duyệt bằng iterator
```cpp
for (auto it = v.begin(); it != v.end(); ++it) {
    std::cout << *it << " ";
}
```

## Duyệt bằng vòng lặp for-each
```cpp
for (int element : v) {
    std::cout << element << " ";
}
```   

> [!info] Lưu ý
> Mỗi phương pháp đều có ưu nhược điểm riêng; hãy chọn cách phù hợp với bài toán của bạn.

---

# Chèn và xoá (Inserting and Erasing)
Mình sẽ làm rõ cách thực hiện **chèn** và **xoá** phần tử trong mảng động, cùng với những lưu ý về độ phức tạp thời gian của các thao tác này.

- **Chèn phần tử:**  
    Dùng hàm **`push_back`** để thêm phần tử ở cuối mảng (thao tác **O(1)**).
- **Xoá phần tử:**  
```cpp
v.erase(v.begin() + 1); // Xóa phần tử thứ 2 trong mảng động
```

> [!tip]- Mẹo
> Nếu cần xoá phần tử nhiều lần ở giữa của `vector`, hãy cân nhắc các cấu trúc dữ liệu khác hỗ trợ thao tác này tốt hơn. Vì xoá phần tử ở giữa `vector` có độ phức tạp **O(n)** do cần dịch chuyển các phần tử sau đó.

---

# Chuỗi (Strings)
**Strings** là cấu trúc dữ liệu rất quen thuộc, được sử dụng để lưu trữ và thao tác với văn bản:

- Hỗ trợ các thao tác như nối chuỗi, cắt chuỗi và truy cập ký tự theo chỉ số.
- Các hàm thông dụng: **`getline`**, **`substr`**, **`size()`**.

---

# Cặp (Pairs) và Bộ (Tuples)
Trong một số bài toán, bạn cần lưu trữ nhiều giá trị cùng lúc. **Pairs** và **Tuples** cho phép bạn kết hợp các giá trị lại với nhau, giúp mã nguồn gọn gàng và dễ hiểu hơn.

- **Pairs:**
```cpp
std::pair<string, int> myPair = std::make_pair("Example", 123);
```

- **Tuples:**
```cpp
#include <tuple>
std::tuple<int, int, int> t = std::make_tuple(3, 4, 5);
std::get<0>(t);  // truy cập phần tử đầu tiên
```

> [!tip]- Mẹo
> Sử dụng **pairs/tuples** khi cần trả về nhiều giá trị từ một hàm, giúp mã nguồn trở nên trực quan hơn.

---

# Phân bổ bộ nhớ (Memory Allocation)
Việc quản lý bộ nhớ là một khía cạnh quan trọng khi làm việc với mảng (đặc biệt là mảng lớn) trong các cuộc thi lập trình. Phần này sẽ giải thích cách tính toán giới hạn bộ nhớ và các lưu ý khi sử dụng bộ nhớ.

- **Giới hạn bộ nhớ:**
    - Ví dụ, USACO thường có giới hạn **256 MB**.
    - Để ước lượng số lượng phần tử có thể lưu trữ, hãy chia tổng dung lượng cho kích thước của kiểu dữ liệu (ví dụ: 4 byte cho `int`).
- **Program overhead:**
    - Cần chú ý đến bộ nhớ sử dụng cho các hàm đệ quy hay các overhead khác trong chương trình.

> [!info] Lưu ý
> Luôn kiểm tra giới hạn bộ nhớ khi thiết kế giải pháp cho bài toán để tránh lỗi **Memory Limit Exceeded (MLE)**.

---

# Tổng Kết
Trong bài viết này, chúng ta đã cùng nhau khám phá:
- **Khái niệm cơ bản** về **cấu trúc dữ liệu** và tầm quan trọng của chúng trong lập trình.
- **Mảng tĩnh và mảng động:** Cách khai báo, khởi tạo và thao tác với chúng.
- **Kỹ thuật duyệt, chèn và xoá:** Các phương pháp duyệt mảng, cũng như lưu ý về độ phức tạp của thao tác chèn/xoá.
- **Xử lý chuỗi:** Các thao tác cơ bản với **std::string** và các hàm liên quan.
- **Pairs và Tuples:** Cách kết hợp nhiều giá trị trong cùng một cấu trúc để xử lý bài toán hiệu quả.
- **Quản lý bộ nhớ:** Cách ước tính và quản lý bộ nhớ trong các bài toán cạnh tranh.

Nắm vững các **cấu trúc dữ liệu** không chỉ giúp bạn giải quyết bài toán một cách hiệu quả mà còn là nền tảng để tiếp cận các vấn đề phức tạp hơn trong lập trình. Hãy thường xuyên luyện tập và tìm hiểu sâu hơn qua các tài nguyên bổ sung để trở thành một lập trình viên **chuyên nghiệp**! 🌟