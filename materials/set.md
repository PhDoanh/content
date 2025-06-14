---
date: 2025-03-09
draft: false
status: Doing
title: Cấu trúc dữ liệu tập hợp
description: ""
author: PhDoanh
authorlink: https://github.com/PhDoanh
tags:
  - dsa
  - coding
  - cpp
  - competitive
  - data-structure
  - set
  - unordered-set
  - multiset
  - unordered-multiset
aliases:
  - set
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
    src="images/set.png"
    alt="Cấu trúc dữ liệu tập hợp" 
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

# 👀 Giới thiệu về Tập hợp
**Cấu trúc dữ liệu tập hợp** là một kiểu dữ liệu trừu tượng dùng để biểu diễn một bộ sưu tập các phần tử duy nhất, không có thứ tự cụ thể (trừ khi được định nghĩa khác). Trong lập trình, cấu trúc này rất hữu ích khi bạn cần lưu trữ một nhóm phần tử mà không quan tâm đến thứ tự của chúng hoặc khi muốn đảm bảo rằng không có phần tử nào bị trùng lặp (trừ trường hợp cho phép trùng lặp). Trong C++, cấu trúc dữ liệu tập hợp được triển khai qua các lớp như `set`, `unordered_set`, `multiset` và `unordered_multiset`. Dưới đây là phân loại chi tiết của từng loại, bao gồm ứng dụng, ưu điểm và nhược điểm.

## Tập hợp có thứ tự
**Set** là một tập hợp các phần tử duy nhất, được sắp xếp theo một thứ tự nhất định (thường là tăng dần). 

**Ứng dụng**:
- Lưu trữ các phần tử không cho phép trùng lặp và cần duy trì thứ tự.
- Sử dụng trong các bài toán cần tìm kiếm, chèn, hoặc xóa phần tử với hiệu suất ổn định.

> [!check] Ưu điểm
> - Duy trì thứ tự của các phần tử (tự động sắp xếp).
> - Hỗ trợ các thao tác như tìm kiếm, chèn, và xóa với độ phức tạp $O(\log n)$.

> [!missing] Nhược điểm
> - Chi phí tính toán cao hơn so với `unordered_set` do phải duy trì thứ tự.

## Tập hợp không có thứ tự
**Unordered Set** là một tập hợp các phần tử duy nhất, không có thứ tự cụ thể, sử dụng bảng băm (hash table) để lưu trữ.

**Ứng dụng**:
- Lưu trữ các phần tử không cho phép trùng lặp và không cần quan tâm đến thứ tự.
- Thích hợp cho các thao tác yêu cầu tốc độ cao như kiểm tra sự tồn tại của phần tử.

> [!check] Ưu điểm
> - Thao tác nhanh với độ phức tạp trung bình O(1) cho tìm kiếm, chèn, và xóa.
> - Hiệu quả cao trong các ứng dụng cần kiểm tra phần tử nhanh chóng.

> [!missing] Nhược điểm
> - Không duy trì thứ tự của các phần tử.
> - Trong trường hợp xấu nhất (xung đột hash), độ phức tạp có thể tăng lên O(n).

## Tập hợp lặp + có thứ tự
**Multi Set** là một tập hợp các phần tử có thể trùng lặp, được sắp xếp theo một thứ tự nhất định.

**Ứng dụng**:
- Lưu trữ các phần tử có thể trùng lặp và cần duy trì thứ tự.
- Dùng trong các bài toán cần đếm số lần xuất hiện của phần tử hoặc xử lý danh sách có thứ tự.

> [!check] Ưu điểm
> - Cho phép các phần tử trùng lặp.
> - Duy trì thứ tự của các phần tử (tự động sắp xếp).

> [!missing] Nhược điểm
> - Chi phí cao hơn so với Set do phải quản lý các phần tử trùng lặp, với độ phức tạp O(log n).

## Tập hợp lặp + không có thứ tự
**Unordered Multi Set** là một tập hợp các phần tử có thể trùng lặp, không có thứ tự cụ thể, sử dụng bảng băm để lưu trữ.

**Ứng dụng**:
- Lưu trữ các phần tử có thể trùng lặp mà không cần quan tâm đến thứ tự.
- Thích hợp cho các thao tác nhanh như đếm số lần xuất hiện hoặc kiểm tra phần tử.

> [!check] Ưu điểm
> - Thao tác nhanh với độ phức tạp trung bình $O(1)$ cho tìm kiếm, chèn, và xóa.
> - Hỗ trợ các phần tử trùng lặp hiệu quả.

> [!missing] Nhược điểm
> - Không duy trì thứ tự của các phần tử.
> - Trong trường hợp xấu nhất (xung đột hash), độ phức tạp có thể là O(n).

---

# 🛠️ Khai triển Tập hợp trong C++

> [!caution]- Nội dung đang hoàn thiện
> Quá trình xây dựng nội dung này có thể mất nhiều thời gian ⌛, nhưng bạn có thể thúc đẩy nó bằng cách tham gia [[article-collaboration-guide|cộng tác bài viết]] 🤝
> 
> **Rất mong sự thông cảm của các bạn 🙏**

%% 
## Tập hợp có thứ tự
 mô tả 

```cpp {}

```

> [!explain]- Giải thích code
> Dòng ?: 

 %%

---

# ✨ Tập hợp trong thư viện chuẩn C++
Trong C++ STL, **`set`** và **`multiset`** là các tập hợp có thứ tự, được triển khai bằng **cây đỏ đen**, trong đó `set` không cho phép phần tử trùng lặp, còn `multiset` thì cho phép. Ngược lại, **`unordered_set`** và **`unordered_multiset`** sử dụng **bảng băm**, giúp tra cứu nhanh hơn nhưng không đảm bảo thứ tự, với `unordered_multiset` thì cho phép trùng lặp. Sự khác biệt chính giữa chúng nằm ở **thứ tự sắp xếp, hiệu suất và khả năng lưu trữ phần tử trùng lặp**, giúp lập trình viên lựa chọn phù hợp theo nhu cầu.

|   Phương thức   |                       Kiểu trả về                       | Tham số                                                                                                              | Mô tả                                                                                                                                                                                                                                   |                                       Độ phức tạp                                        |     Cấu trúc đặc trưng      |
|:---------------:|:-------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------- |:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |:----------------------------------------------------------------------------------------:|:---------------------------:|
|    `begin()`    |                       `iterator`                        | không có                                                                                                             | Trả về iterator trỏ đến phần tử đầu tiên trong container                                                                                                                                                                                |                                          $O(1)$                                          |                             |
|     `end()`     |                       `iterator`                        | Không có                                                                                                             | Trả về iterator trỏ đến vị trí sau phần tử cuối cùng.                                                                                                                                                                                   |                                          $O(1)$                                          |                             |
|    `empty()`    |                         `bool`                          | Không có                                                                                                             | Kiểm tra container có rỗng hay không.                                                                                                                                                                                                   |                                          $O(1)$                                          |                             |
|    `size()`     |                       `size_type`                       | Không có                                                                                                             | Trả về số lượng phần tử hiện có trong container.                                                                                                                                                                                        |                                          $O(1)$                                          |                             |
|  `max_size()`   |                       `size_type`                       | không có                                                                                                             | Trả về số lượng phần tử tối đa mà container có thể chứa.                                                                                                                                                                                |                                          $O(1)$                                          |                             |
|    `clear()`    |                         `void`                          | Không có                                                                                                             | Xóa tất cả các phần tử trong container.                                                                                                                                                                                                 |                                          $O(n)$                                          |                             |
|   `insert()`    | _Unique:_ `pair<iterator, bool>`<br>_Multi:_ `iterator` | `const value_type& value`: Giá trị cần chèn                                                                          | Chèn phần tử vào container.<br>- Với container không cho phép trùng lặp (như `set`, `unordered_set`) trả về cặp kết quả<br>- Với container cho phép trùng lặp (như `multiset`, `unordered_multiset`) trả về iterator đến phần vừa chèn. |                 _Ordered:_ $O(\log n)$<br>_Unordered:_ $O(1)$ trung bình                 |                             |
|    `erase()`    |                       `iterator`                        | `iterator pos`: Iterator trỏ đến phần tử cần xóa                                                                     | Xóa phần tử tại vị trí `pos` và trả về iterator sau phần bị xóa.                                                                                                                                                                        |                 _Ordered:_ $O(\log n)$<br>_Unordered:_ $O(1)$ trung bình                 |                             |
|    `erase()`    |                       `size_type`                       | `const key_type& key`: Khóa của phần tử cần xóa                                                                      | Xóa phần tử có khóa bằng `key` và trả về số lượng phần tử bị xóa.                                                                                                                                                                       |                 _Ordered:_ $O(\log n)$<br>_Unordered:_ $O(1)$ trung bình                 |                             |
|    `erase()`    |                       `iterator`                        | - `iterator first`: Iterator bắt đầu phạm vi xóa<br>- `iterator last`: Iterator kết thúc phạm vi xóa (không bao gồm) | Xóa các phần tử trong khoảng `[first, last)` và trả về iterator sau phần cuối cùng bị xóa.                                                                                                                                              | _Ordered:_ $O(k \log n)$<br>_Unordered:_ $O(k)$ trung bình, với `k` là số phần tử bị xóa |                             |
|    `swap()`     |                         `void`                          | `container_type& other`: Container cần hoán đổi nội dung                                                             | Hoán đổi nội dung của container hiện tại với `other`.                                                                                                                                                                                   |                                          $O(1)$                                          |                             |
|    `count()`    |                       `size_type`                       | `const key_type& key`: Khóa cần đếm                                                                                  | Đếm số lượng phần tử có khóa bằng `key`.                                                                                                                                                                                                |                 _Ordered:_ $O(\log n)$<br>_Unordered:_ $O(1)$ trung bình                 |                             |
|    `find()`     |                       `iterator`                        | `const key_type& key`: Khóa cần tìm                                                                                  | Tìm phần tử có khóa `key`; nếu tìm thấy trả về iterator tương ứng, ngược lại trả về `end()`.                                                                                                                                            |                 _Ordered:_ $O(\log n)$<br>_Unordered:_ $O(1)$ trung bình                 |                             |
| `equal_range()` |               `pair<iterator, iterator>`                | `const key_type& key`: Khóa để xác định phạm vi                                                                      | Trả về cặp iterator xác định phạm vi các phần tử có khóa bằng `key`.                                                                                                                                                                    |                 _Ordered:_ $O(\log n)$<br>_Unordered:_ $O(1)$ trung bình                 |                             |
| `lower_bound()` |                       `iterator`                        | `const key_type& key`: Khóa để tìm phần tử không nhỏ hơn `key`                                                       | Trả về iterator đến phần tử đầu tiên không nhỏ hơn `key`.                                                                                                                                                                               |                                       $O(\log n)$                                        | `std::set`, `std::multiset` |
| `upper_bound()` |                       `iterator`                        | `const key_type& key`: Khóa để tìm phần tử lớn hơn `key`                                                             | Trả về iterator đến phần tử đầu tiên lớn hơn `key`.                                                                                                                                                                                     |                                       $O(\log n)$                                        | `std::set`, `std::multiset` |
|  `key_comp()`   |                        `Compare`                        | Không có                                                                                                             | Trả về đối tượng so sánh được dùng để sắp xếp các khóa.                                                                                                                                                                                 |                                          $O(1)$                                          | `std::set`, `std::multiset` |
| `value_comp()`  |                        `Compare`                        | Không có                                                                                                             | Trả về đối tượng so sánh giá trị (trong `std::set` thường giống với `key_comp()`).                                                                                                                                                      |                                          $O(1)$                                          | `std::set`, `std::multiset` | 

> [!info] Lưu ý
> Cột **Cấu trúc đặc trưng** cho biết các phương thức tương ứng chỉ có ở cấu trúc đó, còn lại là phương thức chung mà loại tập hợp nào cũng có

**Ví dụ về `set`**:
```cpp {2,6,7-11,13-15,18,19,21-22,26,29-30,34,40-41,42-43,45,51,67,77-78}
#include <iostream>
#include <set>
using namespace std;

int main() {
    set<int> s;
    s.insert(5);
    s.insert(1);
    s.insert(3);
    s.insert(7);
    s.insert(2);
    
    cout << "Elements: ";
    for (auto it = s.begin(); it != s.end(); ++it)
        cout << *it << " ";
    cout << endl;
    
    cout << "Size: " << s.size() << endl;
    cout << "Empty: " << (s.empty() ? "true" : "false") << endl;
    
    auto it = s.find(3);
    cout << "Find 3: " << (it != s.end() ? *it : -1) << endl;
    it = s.find(10);
    cout << "Find 10: " << (it != s.end() ? *it : -1) << endl;
    
    cout << "Count 3: " << s.count(3) << endl;
    cout << "Count 10: " << s.count(10) << endl;
    
    auto lb = s.lower_bound(3);
    auto ub = s.upper_bound(3);
    cout << "Lower bound of 3: " << (lb != s.end() ? *lb : -1) << endl;
    cout << "Upper bound of 3: " << (ub != s.end() ? *ub : -1) << endl;
    
    auto er = s.equal_range(3);
    cout << "Equal range of 3: ";
    for (auto it = er.first; it != er.second; ++it)
        cout << *it << " ";
    cout << endl;
    
    auto comp = s.key_comp();
    cout << "Key comparison (compare 1 and 5): " << (comp(1,5) ? "true" : "false") << endl;
    auto comp_val = s.value_comp();
    cout << "Value comparison (compare 7 and 5): " << (comp_val(7,5) ? "true" : "false") << endl;
    
    s.erase(3);
    cout << "After erasing 3, elements: ";
    for (auto it = s.begin(); it != s.end(); ++it)
        cout << *it << " ";
    cout << endl;
    
    it = s.find(7);
    if (it != s.end())
        s.erase(it);
    cout << "After erasing 7, elements: ";
    for (auto it = s.begin(); it != s.end(); ++it)
        cout << *it << " ";
    cout << endl;
    
    set<int> s2;
    s2.insert(100);
    s2.insert(200);
    cout << "s2 elements before swap: ";
    for (auto e : s2)
        cout << e << " ";
    cout << endl;
    
    s.swap(s2);
    cout << "s elements after swap: ";
    for (auto e : s)
        cout << e << " ";
    cout << endl;
    cout << "s2 elements after swap: ";
    for (auto e : s2)
        cout << e << " ";
    cout << endl;
    
    s.clear();
    cout << "s size after clear: " << s.size() << endl;
    
    return 0;
}
```

```txt title="Đầu ra"
Elements: 1 2 3 5 7 
Size: 5
Empty: false
Find 3: 3
Find 10: -1
Count 3: 1
Count 10: 0
Lower bound of 3: 3
Upper bound of 3: 5
Equal range of 3: 3 
Key comparison (compare 1 and 5): true
Value comparison (compare 7 and 5): false
After erasing 3, elements: 1 2 5 7 
After erasing 7, elements: 1 2 5 
s2 elements before swap: 100 200 
s elements after swap: 100 200 
s2 elements after swap: 1 2 5 
s size after clear: 0
```

> [!explain]- Giải thích code
> - **Dòng 2:** Thư viện định nghĩa cho `std::set` trong C++ STL.
> - **Dòng 6:** Khởi tạo một Set lưu các số nguyên, tự động sắp xếp theo thứ tự tăng dần và không cho phép phần tử trùng lặp.
> - **Dòng 7-11:** Sử dụng `insert()` để thêm các giá trị vào set; các phần tử được lưu theo thứ tự tăng dần.
> - **Dòng 13-15:** Duyệt set từ `begin()` đến `end()` và in ra các phần tử, hiển thị các phần tử theo thứ tự sắp xếp.
> - **Dòng 18:** In ra số lượng phần tử hiện có trong set qua `size()`.
> - **Dòng 19:** Kiểm tra set có rỗng hay không bằng `empty()` và in kết quả.
> - **Dòng 21-22:** Dùng `find(3)` để tìm phần tử có giá trị `3` và in ra nếu tìm thấy; nếu không thì in `-1`.
> - **Dòng 26:** Dùng `count()` để đếm số lượng phần tử bằng `3` trong set.
> - **Dòng 29-30:** Sử dụng `lower_bound(3)` để lấy iterator tới phần tử không nhỏ hơn `3` và `upper_bound(3)` để lấy phần tử lớn hơn `3`
> - **Dòng 34:** Lấy phạm vi các phần tử bằng `3` qua `equal_range(3)`
> - **Dòng 40-41:** Lấy hàm so sánh khóa với `key_comp()` và sử dụng để so sánh `1` và `5`, in kết quả.
> - **Dòng 42-43:** Lấy hàm so sánh giá trị với `value_comp()` và dùng để so sánh `7` và `5`, in kết quả.
> - **Dòng 45:** Xóa phần tử có giá trị `3` bằng `erase(3)`.
> - **Dòng 51:** Tìm phần tử có giá trị `7`
> - **Dòng 67:** Sử dụng `swap()` để hoán đổi nội dung của `s` và `s2`.
> - **Dòng 77-78:** Dùng `clear()` để xóa tất cả phần tử của `s` và in ra kích thước của `s` sau khi xóa.

> [!info] Lưu ý
> - `std::set` và `std::multiset` được định nghĩa trong thư viện `set`. Còn `std::unordered_set` và `std::unordered_multiset` được định nghĩa trong thư viện `unordered_set`
> - Các phần tử `std::unordered_set` và `std::unordered_multiset` khi in ra có thứ tự ngẫu nhiên (không đảm bảo thứ tự lúc chèn) và có thể khác nhau ở mỗi lần in

---

# 🔥 Tổng kết
Cấu trúc dữ liệu **tập hợp** giúp lưu trữ các phần tử không trùng lặp (hoặc có giới hạn trùng lặp) và hỗ trợ các thao tác như chèn, xóa, tìm kiếm hiệu quả. Trong C++ STL, các tập hợp được chia thành hai loại chính: **có thứ tự** (`set`, `multiset`) sử dụng cây đỏ đen, và **không có thứ tự** (`unordered_set`, `unordered_multiset`) sử dụng bảng băm, mỗi loại có ưu điểm riêng về tốc độ và cách sắp xếp dữ liệu. Việc lựa chọn cấu trúc phù hợp giúp tối ưu hiệu suất và đáp ứng yêu cầu cụ thể của bài toán!
