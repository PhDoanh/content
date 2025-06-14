---
date: 2025-02-16
draft: true
status: Doing
title: "Danh sách liên kết đôi"
description: ""
author: PhDoanh
authorlink: https://github.com/PhDoanh
tags: 
  - dsa
  - coding
  - cpp
  - competitive
  - "data-structure"
  - linked-list
  - doubly-linked-list
aliases:
  - "doubly linked list"
cssclasses:
  - img
  - btn
---
%% ĐỊNH DẠNG TÊN FILE: "tên-cấu-trúc-dữ-liệu-hoặc-thuật-toán" | VD: binary-search %%

%% <figure style="text-align: center; margin: 20px auto;">
  <img 
    src="images/doubly-linked-list.png"
    alt="Danh sách liên kết đôi" 
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
    <em>dsa_name</em>
  </figcaption>
</figure> %%

# 👀 Giới thiệu về Doubly Linked List
Danh sách liên kết (**Linked List**) là một cấu trúc dữ liệu động bao gồm các **nút (node)**, mỗi nút chứa **dữ liệu** và một **con trỏ** trỏ đến nút tiếp theo. Không giống như mảng, danh sách liên kết không yêu cầu bộ nhớ liên tục, giúp tối ưu việc cấp phát bộ nhớ động. 

Danh sách được gọi là **liên kết đôi** nếu mỗi nút có hai con trỏ, một trỏ đến nút trước, một trỏ đến nút sau, cho phép duyệt linh hoạt theo cả hai hướng

---

# 🛠️ Khai triển Doubly Linked List trong C++

## Định nghĩa nút
```cpp {2,4,6,8-11}
struct Node {
    int data;

    Node* prev;

    Node* next;
  
    Node(int d) {
       data = d;
       prev = next = nullptr;      
    }
};
```

> [!explain]- Giải thích code
> Dòng 2: phần **dữ liệu** của nút
> Dòng 4: Con trỏ trỏ tới nút **trước đó**
> Dòng 6: Con trỏ trỏ tới nút **tiếp theo**
> Dòng 8-11: Hàm tạo để **khởi tạo** dữ liệu nút

## Thao tác duyệt phần tử 
Thao tác này sẽ in ra dữ liệu của từng nút trong danh sách

### Duyệt xuôi
Duyệt theo chiều thuận từ trái sang phải

```cpp {3,5,7,9}
void printForward(Node* head) {
  
    Node* curr = head;

    while (curr != nullptr) {
      
        cout << curr->data << " ";

        curr = curr->next;
    }

    cout << '\n';
}
```

> [!explain]- Giải thích code
> Dòng 3: Bắt đầu từ đầu danh sách (con trỏ `head`)
> Dòng 5: Duyệt danh sách đến khi phần tử là `nullptr` thì dừng lại
> Dòng 7: In dữ liệu của nút hiện tại
> Dòng 9: Di chuyển tới nút tiếp theo

### Duyệt ngược
Duyệt theo chiều nghịch từ phải sang trái

```cpp {3,5,7,9}
void printBackward(Node* tail) {
  
    Node* curr = tail;

    while (curr != nullptr) {
      
        cout << curr->data << " ";

        curr = curr->prev;
    }

    cout << '\n';
}
```

> [!explain]- Giải thích code
> Dòng 3: Bắt đầu từ cuối danh sách (con trỏ `tail`)
> Dòng 5: Duyệt danh sách đến khi phần tử là `nullptr` thì dừng lại
> Dòng 7: In dữ liệu của nút hiện tại
> Dòng 9: Di chuyển tới nút trước đó

## Thao tác tìm kiếm
Thao tác này sẽ cho biết phần tử cần tìm có nằm trong danh sách hay không

```cpp {3,5-7,9,12}
bool find(Node* head, int target)
{
    while (head != nullptr) {

        if (head->data == target) {
            return true;
        }

        head = head->next;
    }

    return false;
}
```

> [!explain]- Giải thích code
> Dòng 3: Duyệt toàn bộ danh sách liên kết
> Dòng 5-7: Phần tử được tìm thấy nếu dữ liệu nút hiện tại bằng với nó
> Dòng 9: Di chuyển tới nút tiếp theo
> Dòng 12: Không tìm thấy phần tử do đã duyệt và kiểm tra hết danh sách mà không thỏa mãn dòng 5-7

## Thao tác lấy chiều dài danh sách
Thao tác này sẽ trả về số phần tử có trong danh sách

```cpp {2,4-5,7}
int len(Node* head) {
    int count = 0;

    for (Node* cur = head; cur != nullptr; cur = cur -> next)
        count++;
        
    return count;
}
```

> [!explain]- Giải thích code
> Dòng 2: Khởi tạo biến đếm số phần tử 
> Dòng 4-5: Tăng biến đếm lên 1 đơn vị trong quá trình duyệt toàn bộ danh sách
> Dòng 7: Trả về số phần tử đã đếm được

## Thao tác chèn phần tử
Thao tác này dùng để chèn 1 nút mới vào danh sách tại 1 vị trí cụ thể

```cpp {3,5-13,15-18,20-24,26,28,30,32-33}
Node* insertNode(Node* head, int pos, int new_data) {

    Node *new_node = new Node(new_data);

    if (pos == 1) {
        new_node->next = head;

        if (head != nullptr)
            head->prev = new_node;

        head = new_node;
        return head;
    }

    Node* curr = head;
    for (int i = 1; i < pos - 1 && curr != nullptr; i++) {
        curr = curr->next;
    }

    if (curr == nullptr) {
        cout << "Invalid Position" << endl;
        delete new_node;
        return head;
    }

    new_node->prev = curr;

    new_node->next = curr->next;

    curr->next = new_node;

    if (new_node->next != nullptr)
        new_node->next->prev = new_node;

    return head;
}
```

> [!explain]- Giải thích code
> Dòng 3: Tạo 1 nút mới
> Dòng 5-13: Xử lý trường hợp chèn tại vị trí đầu tiên
> Dòng 8-9: Thiết lập con trỏ `prev` của nút `head` thành `new_node` nếu danh sách không rỗng
> Dòng 11: Thiết lập nút đầu tiên thành `new_node`
> Dòng 15-18: Duyệt danh sách để tìm ra nút đứng trước vị trí cần chèn
> Dòng 20-24: Xử lý trường hợp vị trí cần chèn lớn hơn số nút
> Dòng 26: Gán con trỏ `prev` của nút `new_node` thành nút hiện tại (nút đứng trước vị trí cần chèn)
> Dòng 28: Gán con trỏ `next` của nút `new_node` thành nút kế tiếp của nút hiện tại
> Dòng 30: Cập nhật con trỏ `next` của nút hiện tại thành `new_node`
> Dòng 32-33: Nếu `new_node` không phải nút được chèn vào cuối danh sách, cập nhật con trỏ `prev` của nút kế tiếp `new_node` thành `new_node` 

## Thao tác xóa phần tử
Thao tác dùng để xóa 1 nút khỏi danh sách tại 1 vị trí cụ thể

```cpp {2-3,5-8,10-11,13-14,16-17,19-20,22}
Node* eraseNode(Node* head, int pos) {
    if (head == nullptr)
        return head;

    Node* curr = head;
    for (int i = 1; curr && i < pos; i++) {
        curr = curr -> next;
    }

    if (curr == nullptr)
        return head;

    if (curr -> prev)
        curr -> prev -> next = curr -> next;

    if (curr -> next)
        curr -> next -> prev = curr -> prev;

    if (head == curr)
        head = curr -> next;

    delete curr;
    return head;
}
```

> [!explain]- Giải thích code
> Dòng 2-3: Xử lý trường hợp đặc biệt khi danh sách rỗng
> Dòng 5-8: Duyệt danh sách để tìm ra nút tại vị trí cần xóa
> Dòng 10-11: Xử lý trường hợp vị trí cần xóa lớn hơn số nút
> Dòng 13-14: Cập nhật con trỏ `next` của nút đứng trước nút hiện tại `curr`
> Dòng 16-17: Cập nhật con trỏ `prev` của nút kế tiếp nút hiện tại `curr`
> Dòng 19-20: Đặt nút đầu tiên trong danh sách thành nút kế tiếp nếu nút cần xóa là `head`
> Dòng 22: Xóa nút `curr` (nút cần xóa tại vị trí `pos`) 

---

# ✨ Doubly Linked List trong thư viện chuẩn C++

> [!caution]- Nội dung đang hoàn thiện
> Quá trình xây dựng nội dung này có thể mất nhiều thời gian ⌛, nhưng bạn có thể thúc đẩy nó bằng cách tham gia [[article-collaboration-guide|cộng tác bài viết]] 🤝
> 
> **Rất mong sự thông cảm của các bạn 🙏**

---

# 🔥 Tổng kết
Danh sách liên kết đôi khắc phục nhược điểm của danh sách đơn nhờ **duyệt hai chiều**, giúp việc **truy xuất, chèn/xóa linh hoạt hơn**. Điều này đặc biệt hữu ích trong các bài toán **cần thao tác nhiều trên giữa danh sách**. Tuy nhiên, nó **tốn bộ nhớ hơn** do mỗi nút lưu hai con trỏ, và việc quản lý con trỏ **phức tạp hơn** so với danh sách liên kết đơn.
