---
date: 2025-02-16
draft: true
status: Doing
title: Cấu trúc dữ liệu ngăn xếp
description: ""
author: PhDoanh
authorlink: https://github.com/PhDoanh
tags:
  - dsa
  - coding
  - cpp
  - competitive
  - data-structure
  - stack
aliases:
  - stack
cssclasses:
  - img
  - btn
---
%%  LƯU Ý
- Đinh dạng tên file : "dsa-name" (binary-search, linear-search, ...)
%%

%% banner
<figure style="text-align: center; margin: 20px auto;">
  <img 
    src="images/stack.png"
    alt="Cấu trúc dữ liệu ngăn xếp" 
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
    <em>{chú thích}</em>
  </figcaption>
</figure>
%%

# 👀 Giới thiệu về Stack
**Ngăn xếp (Stack)** là một cấu trúc dữ liệu tuyến tính hoạt động theo nguyên tắc **LIFO (Last In, First Out)**, nghĩa là phần tử được thêm vào sau cùng sẽ được lấy ra đầu tiên. Các thao tác chính trên ngăn xếp bao gồm:

- **Push**: Thêm một phần tử vào đỉnh ngăn xếp.
- **Pop**: Loại bỏ phần tử ở đỉnh ngăn xếp.
- **Peek/Top**: Truy cập phần tử ở đỉnh ngăn xếp mà không loại bỏ nó.

**Ứng dụng của ngăn xếp:**

- **Quản lý bộ nhớ trong các ngôn ngữ lập trình**: Ngăn xếp được sử dụng để lưu trữ các lời gọi hàm và biến cục bộ, giúp theo dõi thứ tự gọi và trả về của các hàm.
- **Đảo ngược chuỗi hoặc cấu trúc dữ liệu**: Sử dụng ngăn xếp để đảo ngược chuỗi ký tự hoặc danh sách bằng cách đẩy từng phần tử vào ngăn xếp và sau đó pop ra theo thứ tự ngược lại.
- **Kiểm tra dấu ngoặc trong biểu thức toán học**: Ngăn xếp giúp xác định xem các dấu ngoặc mở và đóng có khớp nhau hay không trong biểu thức.
- **Chuyển đổi và tính toán biểu thức**: Chuyển đổi giữa các dạng biểu thức (infix, postfix, prefix) và tính giá trị của chúng.
- **Duyệt cây và đồ thị**: Sử dụng trong các thuật toán duyệt cây như duyệt theo chiều sâu (DFS).

> [!check] Ưu điểm
> - **Đơn giản và dễ triển khai**: Cấu trúc và thao tác trên ngăn xếp rất đơn giản, dễ hiểu và dễ cài đặt.
> - **Quản lý bộ nhớ hiệu quả**: Việc sử dụng ngăn xếp giúp quản lý bộ nhớ tự động, đặc biệt trong việc gọi hàm đệ quy.
> - **Tốc độ truy cập nhanh**: Thao tác thêm và loại bỏ phần tử chỉ diễn ra ở đỉnh ngăn xếp, do đó có độ phức tạp thời gian là $O(1)$.

> [!missing] Nhược điểm
> - **Truy cập hạn chế**: Chỉ có thể truy cập phần tử ở đỉnh ngăn xếp, không thể truy cập trực tiếp các phần tử khác.
> - **Kích thước cố định (trong trường hợp ngăn xếp tĩnh)**: Nếu ngăn xếp được triển khai bằng mảng có kích thước cố định, có thể dẫn đến lãng phí bộ nhớ hoặc tràn ngăn xếp.
> - **Dễ gây lỗi tràn ngăn xếp (Stack Overflow)**: Khi thêm quá nhiều phần tử mà không kiểm tra dung lượng, ngăn xếp có thể bị tràn và gây lỗi.

---

# 🛠️ Khai triển Stack trong C++

## Khai triển bằng mảng

> [!caution]- Nội dung đang hoàn thiện
> Quá trình xây dựng nội dung này có thể mất nhiều thời gian ⌛, nhưng bạn có thể thúc đẩy nó bằng cách tham gia [[article-collaboration-guide|cộng tác bài viết]] 🤝
> 
> **Rất mong sự thông cảm của các bạn 🙏**

## Khai triển bằng danh sách liên kết

## {tên thao tác}
%% mô tả %%

```cpp {}

```

> [!explain]- Giải thích code
> Dòng ?: 

---

# ✨ Stack trong thư viện chuẩn C++
Trong C++ STL, `std::stack` là một cấu trúc dữ liệu kiểu **LIFO (Last In, First Out)**, hỗ trợ các thao tác như `push()`, `pop()`, `top()`, `size()`, và `empty()`. Nó được triển khai dựa trên **deque** mặc định, nhưng cũng có thể sử dụng **vector** hoặc **list** để thay thế. `std::stack` giúp quản lý dữ liệu theo ngăn xếp một cách thuận tiện mà không cần tự triển khai cấu trúc dữ liệu thủ công.

| Phương thức |          Kiểu trả về           | Tham số                                  | Mô tả                                                                                       |                    Độ phức tạp                     |
|:-----------:|:------------------------------:|:---------------------------------------- |:------------------------------------------------------------------------------------------- |:--------------------------------------------------:|
|  `empty()`  |             `bool`             | Không có                                 | Kiểm tra xem stack có rỗng không. Trả về `true` nếu rỗng, ngược lại trả về `false`.         |                       $O(1)$                       |
|  `size()`   |             `int`              | Không có                                 | Trả về số phần tử hiện có trong stack.                                                      |                       $O(1)$                       |
|   `top()`   | `T` (kiểu dữ liệu của phần tử) | không có                                 | Trả về phần tử trên cùng của stack mà không xóa nó. Nếu stack rỗng, hành vi không xác định. |                       $O(1)$                       |
|  `push(e)`  |             `void`             | `e`: Phần tử kiểu `T` cần thêm vào stack | Thêm phần tử `e` vào đỉnh của stack                                                         | $O(1)$ trung bình<br>$O(n)$ nếu phải mở rộng bộ nhớ. |
|   `pop()`   |             `void`             | Không có                                 | Xóa phần tử trên cùng của stack. Nếu stack rỗng, hành vi không xác định.                    |                       $O(1)$                       |
|             |                                |                                          |                                                                                             |                                                    |

```cpp {}
#include <iostream>
#include <stack>

using namespace std;

int main() {
    stack<int> s;
    
    s.push(10);
    s.push(20);
    s.push(30);
    
    cout << "Top element: " << s.top() << endl;
    
    s.pop();
    cout << "Top element after pop: " << s.top() << endl;
    
    cout << "Stack size: " << s.size() << endl;
    
    while (!s.empty()) {
        cout << "Popping: " << s.top() << endl;
        s.pop();
    }
    
    cout << "Stack is empty: " << (s.empty() ? "Yes" : "No") << endl;
    
    return 0;
}
```

```txt title="Đầu ra"
Top element: 30
Top element after pop: 20
Stack size: 2
Popping: 20
Popping: 10
Stack is empty: Yes
```

> [!explain]- Giải thích code
> - **Dòng 2**: Thư viện `stack` để sử dụng ngăn xếp.
> - **Dòng 7**: Khai báo một ngăn xếp các số nguyên.
> - **Dòng 9-11**: Thêm các phần tử `10, 20, 30` vào ngăn xếp bằng hàm `push()`.
> - **Dòng 13**: Lấy phần tử ở đỉnh ngăn xếp và in ra
> - **Dòng 15**: Xóa phần tử ở đỉnh ngăn xếp
> - **Dòng 18**: In ra số phần tử có trong ngăn xếp
> - **Dòng 25**: Kiểm tra ngăn xếp rỗng hay không và in **"Yes"** nếu có hoặc **"No"** nếu không

---

# 🔥 Tổng kết
Ngăn xếp (**stack**) là một cấu trúc dữ liệu quan trọng hoạt động theo nguyên tắc **LIFO (Last In, First Out)**, phù hợp cho các bài toán như **quản lý lời gọi hàm, duyệt biểu thức toán học, undo/redo** trong phần mềm. Với các thao tác cơ bản như `push()`, `pop()`, `top()`, `size()` và `empty()`, stack giúp quản lý dữ liệu hiệu quả nhưng bị hạn chế trong việc truy xuất ngẫu nhiên. Khi sử dụng, cần cân nhắc đặc điểm này để chọn cấu trúc dữ liệu phù hợp với yêu cầu bài toán.
