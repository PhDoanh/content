---
date: 2025-02-16
draft: false
status: Doing
title: "Cấu trúc dữ liệu hàng đợi"
description:
author: PhDoanh
authorlink: https://github.com/PhDoanh
tags:
  - dsa
  - coding
  - cpp
  - competitive
  - data-structure
  - queue
aliases:
  - queue
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
    src="images/queue.png"
    alt="Cấu trúc dữ liệu hàng đợi" 
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

# 👀 Giới thiệu về Queue
**Hàng đợi (Queue)** là một cấu trúc dữ liệu tuyến tính hoạt động theo nguyên tắc **FIFO (First-In, First-Out)**, nghĩa là phần tử được thêm vào trước sẽ được lấy ra trước. Một số ứng dụng của hàng đợi như:

- **Quản lý tác vụ trong hệ điều hành:** Hàng đợi được sử dụng để quản lý các tác vụ, đảm bảo chúng được xử lý theo thứ tự đến trước.
- **Xử lý yêu cầu trong mạng:** Trong các hệ thống mạng, hàng đợi giúp quản lý và xử lý các gói tin hoặc yêu cầu theo thứ tự nhận được.
- **In ấn:** Các lệnh in được xếp vào hàng đợi và xử lý lần lượt theo thứ tự gửi đến.
- **Thuật toán tìm kiếm theo chiều rộng (BFS):** Sử dụng hàng đợi để lưu trữ các đỉnh trong quá trình duyệt đồ thị.

> [!check] Ưu điểm
> - **Đơn giản và dễ triển khai:** Cấu trúc và thao tác trên hàng đợi khá đơn giản, dễ hiểu.
> - **Quản lý dữ liệu theo thứ tự:** Đảm bảo các phần tử được xử lý theo thứ tự thêm vào, phù hợp cho các ứng dụng cần thứ tự xử lý nghiêm ngặt.
> - **Hiệu quả trong quản lý tài nguyên:** Giúp điều phối và quản lý tài nguyên hệ thống một cách hiệu quả, tránh xung đột.

> [!missing] Nhược điểm
> - **Truy cập ngẫu nhiên hạn chế:** Không thể truy cập trực tiếp các phần tử ở giữa hàng đợi mà phải lấy ra tuần tự từ đầu.
> - **Giới hạn kích thước (nếu sử dụng mảng tĩnh):** Khi triển khai bằng mảng tĩnh, kích thước hàng đợi cố định và có thể dẫn đến lãng phí bộ nhớ hoặc tràn nếu không quản lý tốt.
> - **Hiệu suất chèn/xóa ở giữa kém:** Việc chèn hoặc xóa phần tử ở giữa hàng đợi đòi hỏi phải dịch chuyển các phần tử khác, gây tốn kém về thời gian và tài nguyên.

---

# 🛠️ Khai triển Queue trong C++

## Khai triển bằng mảng

### Mảng thông thường

> [!caution]- Nội dung đang hoàn thiện
> Quá trình xây dựng nội dung này có thể mất nhiều thời gian ⌛, nhưng bạn có thể thúc đẩy nó bằng cách tham gia [[article-collaboration-guide|cộng tác bài viết]] 🤝
> 
> **Rất mong sự thông cảm của các bạn 🙏**

### Mảng xoay vòng

> [!caution]- Nội dung đang hoàn thiện
> Quá trình xây dựng nội dung này có thể mất nhiều thời gian ⌛, nhưng bạn có thể thúc đẩy nó bằng cách tham gia [[article-collaboration-guide|cộng tác bài viết]] 🤝
> 
> **Rất mong sự thông cảm của các bạn 🙏**


## Khai triển bằng danh sách liên kết
Queue có thể được triển khai bằng **danh sách liên kết đơn**, trong đó mỗi phần tử (node) chứa **giá trị** và **con trỏ trỏ đến phần tử tiếp theo**. Queue có hai con trỏ chính:

- `front`: Trỏ đến phần tử đầu hàng đợi.
- `back`: Trỏ đến phần tử cuối hàng đợi.  

Khi thêm phần tử (`pushBack()`), phần tử mới sẽ được nối vào cuối danh sách. Khi xóa phần tử (`popFront()`), phần tử đầu sẽ bị loại bỏ và con trỏ `front` được cập nhật.

> [!check] Ưu điểm
> - **Không giới hạn kích thước**: Không cần xác định trước kích thước như mảng, có thể mở rộng động theo nhu cầu.
> - **Thao tác thêm/xóa nhanh**: `pushBack()` và `popFront()` đều có độ phức tạp $O(1)$ do chỉ cần thay đổi con trỏ.
> - **Không bị lãng phí bộ nhớ**: Chỉ sử dụng bộ nhớ cho đúng số phần tử hiện có, không có khoảng trống dư thừa như mảng.

> [!missing] Nhược điểm
> - **Tốn bộ nhớ cho con trỏ**: Mỗi node cần thêm một con trỏ (`next`), làm tăng bộ nhớ sử dụng so với queue bằng mảng.  
> - **Không hỗ trợ truy cập ngẫu nhiên**: Không thể truy xuất nhanh phần tử ở giữa như mảng (phải duyệt tuần tự).  
> - **Dễ gây lỗi rò rỉ bộ nhớ**: Nếu không giải phóng bộ nhớ đúng cách (`delete` node khi `popFront()`), có thể gây **memory leak**.

### Định nghĩa Queue
%% mô tả %%

```cpp title="queueLinkedListDeploy.cpp" {9-11,14}
struct Node {
    int data;
    Node* next;
    Node(int value) : data(value), next(nullptr) {}
};

class Queue {
private:
    Node* front;
    Node* back;
    int size;

public:
    Queue() : front(nullptr), back(nullptr), size(0) {}
```

> [!explain]- Giải thích code
> - **Dòng 9-11**: Khai báo con trỏ `front` tham chiếu đến phần tử đầu, `back` đến phần tử cuối, và biến `size` để lưu số phần tử có trong hàng đợi.
> - **Dòng 14**: Hàm khởi tạo hàng đợi rỗng

### Kiểm tra Queue rỗng hay không
%% mô tả %%

```cpp title="queueLinkedListDeploy.cpp" showLineNumbers{15} {16}
bool isEmpty() {
	return size == 0;
}
```

> [!explain]- Giải thích code
> - **Dòng 16**: Trả về `true` (hàng đợi rỗng) nếu số phần tử có trong queue bằng 0 và ngược lại

### Trả về số lượng phần tử trong Queue
%% mô tả %%

```cpp title="queueLinkedListDeploy.cpp" showLineNumbers{18} {19}
int getSize() {
	return size;
}
```

> [!explain]- Giải thích code
> - **Dòng 19**: trả về số lượng phần tử trong hàng đợi, được lưu trong biến `size`

### Trả về phần tử đầu tiên
%% mô tả %%

```cpp title="queueLinkedListDeploy.cpp" showLineNumbers{21} {22-23}
int getFront() {
	if (isEmpty()) throw runtime_error("Queue is empty");
	return front->data;
}
```

> [!explain]- Giải thích code
> - **Dòng 22**: ném ngoại lệ `Runtime Error` với thông điệp "Queue is empty" do không thể truy cập phần tử đàu tiên của một hàng đợi rỗng
> - **Dòng 23**: Trả về dữ liệu phần tử đầu tiên nếu hàng đợi không rỗng

### Trả về phần tử cuối cùng
%% mô tả %%

```cpp title="queueLinkedListDeploy.cpp" showLineNumbers{25} {26-27}
int getBack() {
	if (isEmpty()) throw runtime_error("Queue is empty");
	return back->data;
}
```

> [!explain]- Giải thích code
> - **Dòng 26**: ném ngoại lệ `Runtime Error` với thông điệp "Queue is empty" do không thể truy cập phần tử cuối cùng của một hàng đợi rỗng
> - **Dòng 27**: Trả về dữ liệu phần tử cuối cùng nếu hàng đợi không rỗng

### Thêm phần tử vào cuối Queue
%% mô tả %%

```cpp title="queueLinkedListDeploy.cpp" showLineNumbers{29} {30,32,34-35,37}
void pushBack(int value) {
	Node* newNode = new Node(value);
	if (isEmpty()) {
		front = back = newNode;
	} else {
		back->next = newNode;
		back = newNode;
	}
	size++;
}
```

> [!explain]- Giải thích code
> - **Dòng 30**: tạo phần tử mới với giá trị `value`
> - **Dòng 32**: Nếu hàng đợi rỗng, phần tử mới sẽ vừa là phần tử đầu tiên (`front`) và là phần tử cuối cùng (`back`)   
> - **Dòng 34-35**: Nếu hàng đợi không rỗng, nối phần tử mới vào đuôi phần tử cuối cùng của hàng đợi và gán lại phần tử cuối cùng ấy thành phần tử mới
> - **Dòng 37**: Do thêm thao phần tử nên số lượng phần tử tăng lên 1 

### Xóa phần tử đầu tiên
%% mô tả %%

```cpp title="queueLinkedListDeploy.cpp" showLineNumbers{39} {}
void popFront() {
	if (isEmpty()) throw runtime_error("Queue is empty");
	
	Node* temp = front;
	front = front->next;
	delete temp;
	size--;
	
	if (size == 0) back = nullptr;
}
```

> [!explain]- Giải thích code
> - **Dòng 40**: ném ngoại lệ `Runtime Error` với thông điệp "Queue is empty" do không thể truy cập phần tử đầu tiên để mà xóa
> - **Dòng 42-45**: Lấy phần tử đầu tiên ra và xóa nó, đồng thời giảm số lượng phần tử của hàng đợi đi 1 do thao tác xóa
> - **Dòng 47**: Nếu hàng đợi bị xóa hết, gán `back` trở lại `nullptr` (`front` tự động thành `nullptr` trong dòng 42-45 khi hàng đợi chỉ có 1 phần tử) 

---

# ✨ Queue trong thư viện chuẩn C++
Trong C++ STL, **queue** là một cấu trúc dữ liệu trong thư viện `<queue>`, hoạt động theo nguyên tắc **FIFO (First In, First Out)**.

|    Phương thức     |     Kiểu trả về      | Tham số                                         | Mô tả                                                | Độ phức tạp |
|:------------------:|:--------------------:|:----------------------------------------------- |:---------------------------------------------------- |:-----------:|
|     `empty()`      |        `bool`        | Không có                                        | Kiểm tra xem queue có rỗng hay không.                |   $O(1)$    |
|      `size()`      |       `size_t`       | Không có                                        | Trả về số lượng phần tử hiện có trong queue.         |   $O(1)$    |
|     `front()`      | `T&` hoặc `const T&` | Không có                                        | Trả về tham chiếu đến phần tử đầu tiên trong queue.  |   $O(1)$    |
|      `back()`      | `T&` hoặc `const T&` | Không có                                        | Trả về tham chiếu đến phần tử cuối cùng trong queue. |   $O(1)$    |
| `push(const T& e)` |        `void`        | `e`:Giá trị của phần tử cần thêm vào cuối queue | Thêm phần tử mới vào cuối queue.                     |   $O(1)$    |
|      `pop()`       |        `void`        | Không có                                        | Xóa phần tử ở đầu queue.                             |   $O(1)$    |

> [!info]- Lưu ý
> - `size_t` là kiểu số nguyên không dấu được định nghĩa trong C/C++ (thường trong `<cstddef>` hoặc `<stddef.h>`). Dùng để biểu diễn kích thước của đối tượng hoặc số lượng phần tử, chẳng hạn như kết quả của toán tử `sizeof`
> - `T&` là kiểu tham chiếu đến một đối tượng thuộc kiểu `T` trong C++. Cho phép truy cập trực tiếp đối tượng mà không cần sao chép, giúp cải thiện hiệu năng và cho phép thay đổi nội dung của đối tượng (trong trường hợp không có `const`).

```cpp title="queueExample.cpp" {2,6,7,10-13,15}
#include <iostream>
#include <queue>
using namespace std;

int main() {
    queue<int> q;
    q.push(10);
    q.push(20);
    q.push(30);
    cout << "Front: " << q.front() << endl;
    cout << "Back: " << q.back() << endl;
    cout << "Size: " << q.size() << endl;
    cout << "Empty: " << (q.empty() ? "true" : "false") << endl;
    
    q.pop();
    cout << "After pop:" << endl;
    cout << "Front: " << q.front() << endl;
    cout << "Size: " << q.size() << endl;
    
    return 0;
}
```

```txt title="Đầu ra"
Front: 10
Back: 30
Size: 3
Empty: false
After pop:
Front: 20
Size: 2
```

> [!explain]- Giải thích code
> - **Dòng 2**: Bao gồm thư viện queue để sử dụng cấu trúc dữ liệu hàng đợi.
> - **Dòng 6**: Khởi tạo một hàng đợi q chứa các số nguyên (int).
> - **Dòng 7**: Thêm số 10 vào cuối hàng đợi.
> - **Dòng 10**: In ra phần tử ở đầu hàng đợi (front) là 10.
> - **Dòng 11**: In ra phần tử ở cuối hàng đợi (back) là 30.
> - **Dòng 12**: In ra số lượng phần tử hiện có trong hàng đợi (size) là 3.
> - **Dòng 13**: Kiểm tra xem hàng đợi có rỗng không và in ra kết quả ("false" vì hàng đợi không rỗng).
> - **Dòng 15**: Xóa phần tử đầu tiên của hàng đợi (loại bỏ số 10).

---

# 🔥 Tổng kết
Queue là một cấu trúc dữ liệu hoạt động theo nguyên tắc **FIFO (First In, First Out)**, giúp quản lý dữ liệu theo trình tự. Trong C++ STL, queue cung cấp các phương thức như `push()`, `pop()`, `front()`, `back()`, `size()`, và `empty()`, đảm bảo thao tác hiệu quả với độ phức tạp `$O(1)$`. Queue được ứng dụng rộng rãi trong lập lịch, xử lý luồng công việc và thuật toán BFS. Tuy nhiên, queue không hỗ trợ truy cập ngẫu nhiên, do đó nếu cần thao tác linh hoạt hơn, có thể cân nhắc sử dụng **deque** hoặc **priority_queue**.
