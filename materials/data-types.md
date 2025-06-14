---
date: 2025-01-26
draft: false
status: Done
title: Kiểu dữ liệu C++ phổ biến trong thi đấu lập trình
description: ""
author: PhDoanh
authorlink: https://github.com/PhDoanh
tags:
  - coding
  - cpp
  - basic
  - competitive
  - cph
aliases:
  - data types
  - Kiểu dữ liệu C++ phổ biến trong thi đấu lập trình
cssclasses:
  - img
  - btn
---
%% ĐỊNH DẠNG TÊN FILE: "tên-bài-viết" | VD: jp-typing-guide %%

%% <figure style="text-align: center; margin: 20px auto;">
  <img 
    src="images/data-types.png"
    alt="Kiểu dữ liệu C++ phổ biến trong thi đấu lập trình" 
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
    <em>Data Types in C++</em>
  </figcaption>
</figure> %%

Trong các cuộc thi lập trình, việc hiểu rõ và sử dụng hiệu quả các **kiểu dữ liệu** là rất quan trọng. Bài viết này sẽ giới thiệu các kiểu dữ liệu phổ biến trong C++ cùng với ví dụ, lưu ý và mẹo để giúp bạn tối ưu hóa code của mình. 🚀

> [!caution]- Cảnh báo
> - Bài viết này cho rằng bạn đã có kiến thức căn bản về ngôn ngữ C++, trong đó có kiểu dữ liệu và cách sử dụng chúng. Mình chỉ giới thiệu các kiểu xuất hiện phổ biến trong thi đấu lập trình!
> - Kiểu dữ liệu khác cấu trúc dữ liệu!

# 🔢 Số nguyên
- **Số nguyên** là kiểu dữ liệu dùng để lưu trữ các giá trị nguyên không có phần thập phân.
- Các kiểu số nguyên phổ biến: `int`, `long long`.

```cpp {5-6}
#include <iostream>
using namespace std;

int main() {
    int a = 42;
    long long b = 123456789012345LL;
    cout << "a = " << a << ", b = " << b << endl;
    return 0;
}
```

> [!info] Lưu ý
> - `int` thường có kích thước **4 byte** (32 bit), phạm vi từ **-2^31 đến 2^31 - 1**.
> - `long long` có kích thước **8 byte** (64 bit), phạm vi từ **-2^63 đến 2^63 - 1**. 
> - Sử dụng `long long` khi cần lưu trữ số nguyên lớn. 
> - Thêm hậu tố `LL` khi gán giá trị lớn cho `long long`.

# ♾️ Số thực
- **Số thực** là kiểu dữ liệu dùng để lưu trữ các giá trị có phần thập phân.
- Các kiểu số thực phổ biến: `double`.

```cpp {5}
#include <iostream>
using namespace std;

int main() {
    double e = 2.718281828459045;
    cout << "e = " << e << endl;
    return 0;
}
```

> [!info] Lưu ý
> - `double` có độ chính xác khoảng **15-16 chữ số thập phân**. 
> - Sử dụng `double` khi cần độ chính xác cao. 

# ❌ Logic đúng/sai
- **Logic đúng/sai** được biểu diễn bằng kiểu `bool`.
- Giá trị: `true` (1) hoặc `false` (0).

```cpp {5-6}
#include <iostream>
using namespace std;

int main() {
    bool isRaining = true;
    bool isSunny = false;
    cout << "isRaining = " << isRaining << ", isSunny = " << isSunny << endl;
    return 0;
}
```

> [!info] Lưu ý
> - `bool` thường được sử dụng trong các biểu thức điều kiện và vòng lặp.
> - Khi in ra màn hình, `true` hiển thị là **1**, `false` hiển thị là **0**. 
> - Sử dụng `std::boolalpha` để in ra dạng chữ (`true` hoặc `false`).

# 🔡 Kí tự và văn bản
- **Ký tự** được lưu trữ bằng kiểu `char`.
- **Văn bản** có thể được lưu trữ bằng mảng ký tự (C-style string) hoặc lớp `std::string`.

```cpp {6-7}
#include <iostream>
#include <string>
using namespace std;

int main() {
    char ch = 'A';
    string text = "Hello, World!";
    cout << "ch = " << ch << ", text = " << text << endl;
    return 0;
}
```

> [!info] Lưu ý
> - `string` là thư viện để dùng `std::string` 
> - `char` lưu trữ một ký tự đơn, có kích thước **1 byte**.
> - `std::string` linh hoạt hơn, tự động quản lý bộ nhớ. 
> - Sử dụng `std::string` để tránh các lỗi liên quan đến quản lý bộ nhớ.

# 🔥 Tổng kết
| Kiểu dữ liệu | Tên gọi                      | Kích cỡ byte | Phạm vi giá trị             | Ví dụ                              |
| ------------ | ---------------------------- | ------------ | --------------------------- | ---------------------------------- |
| `int`        | Số nguyên 32-bit             | 4            | -2³¹ đến 2³¹-1              | -10, 0, 10, ...                    |
| `long long`  | Số nguyên 64-bit             | 8            | -2⁶³ đến 2⁶³-1              | các số lớn mà `int` không lưu được |
| `double`     | Số thực với độ chính xác kép | 8            | `-1.7E+308` đến `+1.7E+308` | -3.14, 1.0, 3.14, ...              |
| `bool`       | Giá trị logic                | 1            | 0 hoặc 1                    | `true`, `false`                    |
| `char`       | Kí tự 8-bit                  | 1            | -2⁷ đến 2⁷-1                | `'A'`, `'Z'`, ...                  |
| `string`     | Văn bản (Chuỗi kí tự)        |              |                             | `"this is a text"`                 |

> [!info] Lưu ý
> - Tùy vào hệ thống máy hoặc trình biên dịch, các số liệu ở bảng trên có thể khác nhau một chút
> - `string` là kiểu dữ liệu động nên kích cỡ và phạm vi giá trị không cố định
> - Xem đầy đủ kiểu dữ liệu tại [đây](https://en.cppreference.com/w/cpp/language/types)
