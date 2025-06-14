---
date: 2025-03-09
draft: true
status: Doing
title: Cấu trúc dữ liệu từ điển
description: ""
author: PhDoanh
authorlink: https://github.com/PhDoanh
tags:
  - dsa
  - coding
  - cpp
  - competitive
  - data-structure
  - map
  - unordered-map
  - multimap
  - unordered-multimap
aliases:
  - map
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
    src="images/map.png"
    alt="Cấu trúc dữ liệu từ điển" 
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

# 👀 Giới thiệu về Từ điển
**Từ điển** là cấu trúc dữ liệu ánh xạ các khóa (`key`) đến các giá trị (`value`), cho phép truy xuất, chèn và xóa phần tử theo khóa một cách hiệu quả. Được ứng dụng rộng rãi trong các bài toán cần tìm kiếm nhanh, đếm tần suất, quản lý dữ liệu dạng cặp khóa - giá trị. Dưới đây là ứng dụng, ưu nhược điểm của từng loại từ điển

## Từ điển có thứ tự
**Ứng dụng:** Quản lý dữ liệu có thứ tự, như bảng điểm, lịch sử giao dịch có thứ tự theo thời gian.

> [!check] Ưu điểm
> - Lưu các phần tử theo thứ tự tăng dần của khóa.
> - Các thao tác tìm kiếm, chèn, xóa có độ phức tạp O(log⁡n)\mathcal{O}(\log n)O(logn).

> [!missing] Nhược điểm
> - Tốc độ không nhanh bằng bảng băm trong trường hợp dữ liệu lớn nếu thứ tự không quan trọng.

## Từ điển không có thứ tự
**Ứng dụng:** Ánh xạ dữ liệu khi thứ tự không quan trọng, ví dụ như đếm tần suất từ, tìm kiếm nhanh theo khóa.

> [!check] Ưu điểm
> - Thao tác trung bình có độ phức tạp $O(1)$ do sử dụng bảng băm.

> [!missing] Nhược điểm
> - Không đảm bảo thứ tự các phần tử; hiệu năng có thể giảm nếu hàm băm gặp nhiều va chạm.

## Từ điển lặp + có thứ tự
**Ứng dụng:** Lưu trữ các giá trị khi một khóa có thể xuất hiện nhiều lần, như lưu trữ các giao dịch cùng thời điểm của một người dùng.

> [!check] Ưu điểm
> - Cho phép khóa trùng lặp và sắp xếp các phần tử theo thứ tự tăng dần của khóa.

> [!missing] Nhược điểm
> - Chậm hơn Map do cần xử lý các phần tử có khóa trùng lặp; độ phức tạp thao tác cũng là $O(\log n)$.

## Từ điển lặp + không có thứ tự
**Ứng dụng:** Xử lý các bài toán đòi hỏi tốc độ cao và cho phép khóa trùng lặp, như hệ thống cache hay ánh xạ dữ liệu phức tạp.

> [!check] Ưu điểm
> - Thao tác trung bình có độ phức tạp $O(1)$ nhờ bảng băm, và hỗ trợ khóa trùng lặp.

> [!missing] Nhược điểm
> - Không có thứ tự trong lưu trữ; hiệu suất có thể bị ảnh hưởng bởi chất lượng hàm băm và va chạm.

---

# 🛠️ Khai triển Từ điển trong C++

> [!caution]- Nội dung đang hoàn thiện
> Quá trình xây dựng nội dung này có thể mất nhiều thời gian ⌛, nhưng bạn có thể thúc đẩy nó bằng cách tham gia [[article-collaboration-guide|cộng tác bài viết]] 🤝
> 
> **Rất mong sự thông cảm của các bạn 🙏**

%% 
## {tên thao tác}
 mô tả 

```cpp {}

```

> [!explain]- Giải thích code
> Dòng ?: 

 %%
 
---

# ✨ Từ điển trong thư viện chuẩn C++
Trong **STL C++**, `map`, `multimap`, `unordered_map`, và `unordered_multimap` là các cấu trúc dữ liệu dùng để lưu trữ cặp **key-value**.

- **`map`**: Cấu trúc dạng cây đỏ-đen, key là duy nhất và được sắp xếp theo thứ tự tăng dần.
- **`multimap`**: Giống `map` nhưng cho phép nhiều phần tử có cùng key.
- **`unordered_map`**: Dùng bảng băm để lưu trữ, key là duy nhất nhưng không có thứ tự.
- **`unordered_multimap`**: Giống `unordered_map` nhưng cho phép nhiều phần tử có cùng key.

Sự khác biệt chính là `map/multimap` có thứ tự và chậm hơn do dùng cây, còn `unordered_map/unordered_multimap` không có thứ tự nhưng truy xuất nhanh hơn nhờ băm.

|  Phương thức  | Kiểu trả về                                                                                                     | Tham số                                                                                                                         | Mô tả                                                                                                                                                 | Độ phức tạp                                                                                                                                                                          |   Cấu trúc đặc trưng   |
|:-------------:|:--------------------------------------------------------------------------------------------------------------- |:------------------------------------------------------------------------------------------------------------------------------- |:----------------------------------------------------------------------------------------------------------------------------------------------------- |:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |:----------------------:|
|   `insert`    | - `std::pair<iterator, bool>` (cho `map`, `unordered_map`)<br>-`iterator` (cho `multimap`, `unordered_multimap`) | `const value_type& val`: đối tượng cặp `<key, value>` cần chèn                                                                  | Chèn phần tử `val` vào container. Với container không cho phép trùng `key` (đối với `map`, `unordered_map`), nếu `key` đã tồn tại thì không chèn lại. | - **Ordered**: $\mathcal{O}(\log n)$<br>- **Unordered**: trung bình $\mathcal{O}(1)$, xấu nhất $\mathcal{O}(n)$                                                                      |                        |
|    `find`     | `iterator`                                                                                                      | `const Key& key`: giá trị `key` cần tìm                                                                                         | Tìm kiếm và trả về iterator đến phần tử có `key` tương ứng.                                                                                           | - **Ordered**: $\mathcal{O}(\log n)$<br>- **Unordered**: trung bình $\mathcal{O}(1)$, xấu nhất $\mathcal{O}(n)$                                                                      |                        |
|    `erase`    | `void` hoặc `iterator`                                                                                          | _Overload 1:_ `iterator pos`: iterator chỉ vị trí phần tử cần xóa<br>_Overload 2:_ `const Key\& key`: `key` của phần tử cần xóa | Xóa phần tử tại vị trí `pos` hoặc xóa tất cả các phần tử có `key` cho trước.                                                                          | - **Ordered**: $\mathcal{O}(\log n)$ (xóa theo iterator; nếu xóa theo `key` có thể cần xóa nhiều phần tử)<br>- **Unordered**: trung bình $\mathcal{O}(1)$, xấu nhất $\mathcal{O}(n)$ |                        |
|    `clear`    | `void`                                                                                                          | Không có                                                                                                                        | Xóa tất cả các phần tử có trong container.                                                                                                            | $\mathcal{O}(n)$ (với nnn là số phần tử hiện có)                                                                                                                                     |                        |
|    `size`     | `size_type` (thường là `std::size_t`)                                                                           | Không có                                                                                                                        | Trả về số lượng phần tử hiện có trong container.                                                                                                      | $\mathcal{O}(1)$                                                                                                                                                                     |                        |
|    `empty`    | `bool`                                                                                                          | Không có                                                                                                                        | Kiểm tra container có rỗng hay không.                                                                                                                 | $\mathcal{O}(1)$                                                                                                                                                                     |                        |
| `operator[]`  | `T&`                                                                                                            | `const Key& key`: `key` cần truy cập                                                                                            | Truy cập phần tử có `key`; nếu không tồn tại thì chèn mới phần tử với giá trị mặc định. _Chỉ có ở_ `map` và `unordered_map`                           | - **`map`**: $\mathcal{O}(\log n)$<br>- **`unordered_map`**: trung bình $\mathcal{O}(1)$, xấu nhất $\mathcal{O}(n)$                                                                  | `map`, `unordered_map` |
| `lower_bound` | `iterator`                                                                                                      | `const Key& key`: `key` cần so sánh                                                                                             | Trả về iterator tới phần tử đầu tiên có `key` không nhỏ hơn giá trị `key` cho trước.                                                                  | $\mathcal{O}(\log n)$                                                                                                                                                                |   `map`, `multimap`    |
| `upper_bound` | `iterator`                                                                                                      | `const Key& key`: `key` cần so sánh                                                                                             | Trả về iterator tới phần tử đầu tiên có `key` lớn hơn giá trị `key` cho trước.                                                                        | $\mathcal{O}(\log n)$                                                                                                                                                                |   `map`, `multimap`    |
| `equal_range` | `std::pair<iterator, iterator>`                                                                                 | `const Key& key`: `key` cần xác định phạm vi                                                                                    | Trả về cặp iterator xác định khoảng các phần tử có `key` bằng nhau.                                                                                   | $\mathcal{O}(\log n)$                                                                                                                                                                |   `map`, `multimap`    |

> [!info] Lưu ý
> Cột **Cấu trúc đặc trưng** cho biết các phương thức tương ứng chỉ có ở cấu trúc đó, còn lại là phương thức chung mà loại từ điển nào cũng có

**Ví dụ về map**:
```cpp {2,7,8,9,14-16,19-21,23,24,32,39,40,42,44-46,48}
#include <iostream>
#include <map>
#include <string>
using namespace std;

int main() {
    map<string, int> myMap;
    myMap.insert({"apple", 3});
    myMap["banana"] = 5;
    myMap.insert({"orange", 2});
    myMap["kiwi"] = 10;
    
    cout << "Initial map:" << endl;
    for(auto it = myMap.begin(); it != myMap.end(); ++it) {
        cout << it->first << " : " << it->second << endl;
    }
    
    auto itFind = myMap.find("banana");
    if(itFind != myMap.end()) {
        cout << "\nFound 'banana' with value: " << itFind->second << endl;
    }
    
    auto itLow = myMap.lower_bound("banana");
    auto itUp = myMap.upper_bound("banana");
    if(itLow != myMap.end()) {
        cout << "\nLower bound of 'banana': " << itLow->first << " : " << itLow->second << endl;
    }
    if(itUp != myMap.end()) {
        cout << "Upper bound of 'banana': " << itUp->first << " : " << itUp->second << endl;
    }
    
    myMap.erase("orange");
    
    cout << "\nMap after erasing 'orange':" << endl;
    for(auto it = myMap.begin(); it != myMap.end(); ++it) {
        cout << it->first << " : " << it->second << endl;
    }
    
    cout << "\nSize of map: " << myMap.size() << endl;
    cout << "Is map empty? " << (myMap.empty() ? "Yes" : "No") << endl;
    
    auto range = myMap.equal_range("kiwi");
    cout << "\nEqual range for 'kiwi':" << endl;
    for(auto it = range.first; it != range.second; ++it) {
        cout << it->first << " : " << it->second << endl;
    }
    
    myMap.clear();
    cout << "\nMap cleared. Size: " << myMap.size() << endl;
    
    return 0;
}
```

```txt title="Đầu ra"
Initial map:
apple : 3
banana : 5
kiwi : 10
orange : 2

Found 'banana' with value: 5

Lower bound of 'banana': banana : 5
Upper bound of 'banana': kiwi : 10

Map after erasing 'orange':
apple : 3
banana : 5
kiwi : 10

Size of map: 3
Is map empty? No

Equal range for 'kiwi':
kiwi : 10

Map cleared. Size: 0
```

> [!explain]- Giải thích code
> - **Dòng 2:** Bao gồm thư viện chứa định nghĩa của cấu trúc dữ liệu `std::map`.
> - **Dòng 7:** Khởi tạo một đối tượng `std::map` với `key` kiểu `string` và `value` kiểu `int`.
> - **Dòng 8:** Sử dụng phương thức `insert` để thêm cặp `{ "apple", 3 }` vào `myMap`.
> - **Dòng 9:** Sử dụng `operator[]` để truy cập và gán giá trị `5` cho khóa `"banana"`. Nếu `"banana"` không tồn tại, nó sẽ được tạo mới với giá trị mặc định trước khi gán.
> - **Dòng 14-16:** Duyệt qua tất cả các phần tử trong `myMap` theo thứ tự tăng dần của `key` và in ra từng cặp `key : value`.
> - **Dòng 18:** Sử dụng phương thức `find` để tìm phần tử có `key` là `"banana"`.
> - **Dòng 19-21:** Kiểm tra kết quả của `find` và nếu tìm thấy, in ra giá trị của `"banana"`.
> - **Dòng 23:** Dùng phương thức `lower_bound` để tìm iterator đến phần tử có `key` không nhỏ hơn `"banana"`.
> - **Dòng 24:** Dùng phương thức `upper_bound` để tìm iterator đến phần tử có `key` lớn hơn `"banana"`.
> - **Dòng 32:** Sử dụng phương thức `erase` để xóa phần tử có `key` `"orange"` khỏi `myMap`.
> - **Dòng 39:** Sử dụng phương thức `size` để in ra số lượng phần tử hiện có trong `myMap`.
> - **Dòng 40:** Sử dụng phương thức `empty` để kiểm tra và in ra trạng thái rỗng của `myMap`.
> - **Dòng 42:** Dùng phương thức `equal_range` để lấy cặp iterator xác định phạm vi các phần tử có `key = "kiwi"`.
> - **Dòng 44-46:** Duyệt qua phạm vi từ `range.first` đến `range.second` và in ra các phần tử tương ứng với `key = "kiwi"`.
> - **Dòng 48:** Sử dụng phương thức `clear` để xóa tất cả các phần tử trong `myMap`.

> [!info] Lưu ý
> - `std::map` và `std::multimap` được định nghĩa trong thư viện `map`. Còn `std::unordered_map` và `std::unordered_multimap` được định nghĩa trong thư viện `unordered_map`
> - Các phần tử `std::unordered_map` và `std::unordered_map` khi in ra có thứ tự ngẫu nhiên (không đảm bảo thứ tự lúc chèn) và có thể khác nhau ở mỗi lần in

---

# 🔥 Tổng kết
Cấu trúc dữ liệu **từ điển** là một tập hợp ánh xạ giữa **khóa** (key) và **giá trị** (value), cho phép truy xuất nhanh giá trị dựa trên khóa. Trong C++ STL, có bốn loại từ điển chính, mỗi loại có đặc điểm và hiệu suất khác nhau:

1. **`std::map` (Cây đỏ-đen - Ordered Map)**
	- Dữ liệu được sắp xếp theo thứ tự của khóa.
    - Hỗ trợ các phép toán tìm kiếm, chèn, xóa với độ phức tạp trung bình $O(\log n)$.
    - Thích hợp khi cần duy trì thứ tự của các phần tử.

2. **`std::multimap` (Cây đỏ-đen - Ordered Multimap)**
    - Giống `map`, nhưng cho phép nhiều khóa trùng nhau.
    - Các thao tác có độ phức tạp $O(log⁡n)$, nhưng việc truy xuất nhóm phần tử có cùng khóa có thể mất thêm chi phí.

3. **`std::unordered_map` (Bảng băm - Unordered Map)**
    - Sử dụng bảng băm (hash table) giúp tra cứu nhanh với độ phức tạp trung bình $O(1)$.
    - Không duy trì thứ tự của khóa.
    - Dễ bị suy giảm hiệu suất $O(n)$ trong trường hợp xung đột băm lớn.

4. **`std::unordered_multimap` (Bảng băm - Unordered Multimap)**
    - Tương tự `unordered_map`, nhưng cho phép nhiều khóa trùng nhau.
    - Hữu ích trong các bài toán nhóm dữ liệu có cùng khóa mà không cần thứ tự.