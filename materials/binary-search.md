---
date: 2025-02-25
draft: false
status: Doing
title: Thuật toán tìm kiếm nhị phân
description: ""
author: PhDoanh
authorlink: https://github.com/PhDoanh
tags:
  - dsa
  - coding
  - cpp
  - competitive
  - algorithms
  - search
  - ordered-list
aliases:
  - binary search
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
    src="images/binary-search.png"
    alt="Thuật toán tìm kiếm nhị phân" 
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

# 👀 Giới thiệu về Binary search
Thuật toán tìm kiếm nhị phân hoạt động bằng cách chia đôi danh sách đã được **sắp xếp** và kiểm tra phần tử giữa:

- Nếu phần tử giữa là giá trị cần tìm → kết thúc.
- Nếu giá trị cần tìm nhỏ hơn → tìm trong nửa bên trái.
- Nếu giá trị cần tìm lớn hơn → tìm trong nửa bên phải.
- Quá trình lặp lại cho đến khi tìm thấy phần tử hoặc danh sách rỗng.

**Độ phức tạp**:
- **Trung bình và tệ nhất**: $O(\log n)$
- **Tốt nhất**: $O(1)$ (nếu phần tử giữa ngay lập tức là kết quả)

**Ứng dụng**:
- **Tìm kiếm trong mảng đã sắp xếp**: Dữ liệu số, danh sách có thứ tự.
- **Hệ thống cơ sở dữ liệu**: Tìm kiếm trong **B-Tree** hoặc **Indexing** để truy xuất nhanh dữ liệu.
- **Tìm kiếm trong từ điển**: Áp dụng trong **từ điển điện tử** và **tự động sửa lỗi chính tả**.
- **Giải quyết bài toán tối ưu**:
    - **Tìm căn bậc hai**, **tìm nghiệm của phương trình** (dùng tìm kiếm nhị phân trên tập giá trị thực).
    - **Tìm giá trị gần đúng** trong đồ thị và hình ảnh (Binary Search trên khoảng giá trị).

> [!check] Ưu điểm
> - **Nhanh hơn so với tìm kiếm tuyến tính** ($O(log⁡n)$ so với $O(n)$).  
> - **Hiệu quả trên dữ liệu lớn** nếu danh sách đã sắp xếp.  
> - **Có thể áp dụng trên nhiều dạng dữ liệu khác nhau**, kể cả số nguyên, số thực, chuỗi,...  
> - **Tiêu tốn ít bộ nhớ hơn** so với các thuật toán tìm kiếm nâng cao như Hash Table.

> [!missing] Nhược điểm
> - **Chỉ áp dụng cho dữ liệu đã sắp xếp** → Nếu dữ liệu thay đổi liên tục, cần phải sắp xếp lại, làm giảm hiệu suất.  
> - **Không hoạt động tốt trên danh sách động (Linked List)** do không thể truy cập trực tiếp vào phần tử giữa.  
> - **Không phù hợp với tìm kiếm gần đúng hoặc tìm kiếm theo độ tương đồng** (ví dụ: tìm kiếm fuzzy trong AI).  
> - **Độ phức tạp khi cài đặt cao hơn tìm kiếm tuyến tính**, đặc biệt với phiên bản đệ quy.

---

# 🛠️ Khai triển Binary search trong C++

```cpp {5,6,8,9-10,12,16,17,18,20,22-23}
#include <iostream>
using namespace std;

int binarySearch(int arr[], int left, int right, int target) {
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (arr[mid] == target) return mid;
        if (arr[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    return -1;
}

int main() {
    int arr[] = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19};
    int n = sizeof(arr) / sizeof(arr[0]);
    int target = 7;
    
    int result = binarySearch(arr, 0, n - 1, target);
    
    if (result != -1) cout << "Phan tu " << target << " duoc tim thay tai chi so " << result << endl;
    else cout << "Phan tu " << target << " khong ton tai trong mang" << endl;
    
    return 0;
}
```

```txt title="Đầu ra"
Phan tu 7 duoc tim thay tai chi so 3
```

> [!explain]- Giải thích code
> - **Dòng 5:** Lặp lại cho đến khi khoảng tìm kiếm rỗng.
> - **Dòng 6:** Tính chỉ số giữa tránh tràn số.
> - **Dòng 8:** Nếu phần tử giữa bằng `target`, trả về chỉ số của nó.
> - **Dòng 9-10:** Nếu nhỏ hơn, tìm trong nửa phải; ngược lại, tìm trong nửa trái.
> - **Dòng 12:** Trả về `-1` nếu không tìm thấy phần tử.
> - **Dòng 16:** Khởi tạo mảng đã **sắp xếp**.
> - **Dòng 17:** Xác định số phần tử trong mảng.
> - **Dòng 18:** Đặt giá trị cần tìm.
> - **Dòng 20:** Gọi hàm tìm kiếm nhị phân.
> - **Dòng 22-23:** Xuất kết quả tìm kiếm. 

---

# ✨ Binary search trong thư viện chuẩn C++
Tìm kiếm nhị phân trong C++ STL là một thuật toán hiệu quả để tìm kiếm trên **dữ liệu đã sắp xếp**, với độ phức tạp $O(\log n)$. Thư viện `<algorithm>` cung cấp các phương thức như `binary_search`, `lower_bound`, `upper_bound` và `equal_range` để kiểm tra sự tồn tại, tìm vị trí chèn và phạm vi của một phần tử. Đây là giải pháp tối ưu khi làm việc với **vector, array** hoặc các container hỗ trợ truy cập ngẫu nhiên.

|     Phương thức      |                  Kiểu trả về                  | Tham số                                                                                                                                                            | Mô tả                                                                                                                                                                     | Độ phức tạp |
|:--------------------:|:---------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------ |:------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |:-----------:|
| `std::binary_search` |                    `bool`                     | - `ForwardIterator first`: Iterator bắt đầu dãy đã sắp xếp.<br>- `ForwardIterator last`: Iterator kết thúc dãy đã sắp xếp.<br>- `const T& value`: Giá trị cần tìm. | Kiểm tra xem `value` có tồn tại trong dãy đã sắp xếp `[first, last)` hay không.                                                                                           | $O(\log n)$ |
|  `std::lower_bound`  |               `ForwardIterator`               | - `ForwardIterator first`: Iterator bắt đầu dãy đã sắp xếp.<br>- `ForwardIterator last`: Iterator kết thúc dãy đã sắp xếp.<br>- `const T& value`: Giá trị cần tìm. | Trả về iterator trỏ đến phần tử đầu tiên **≥ `value`** trong `[first, last)`.                                                                                             | $O(\log n)$ |
|  `std::upper_bound`  |               `ForwardIterator`               | - `ForwardIterator first`: Iterator bắt đầu dãy đã sắp xếp.<br>- `ForwardIterator last`: Iterator kết thúc dãy đã sắp xếp.<br>- `const T& value`: Giá trị cần tìm. | Trả về iterator trỏ đến phần tử đầu tiên **> `value`** trong `[first, last)`.                                                                                             | $O(\log n)$ |
|  `std::equal_range`  | `std::pair<ForwardIterator, ForwardIterator>` | - `ForwardIterator first`: Iterator bắt đầu dãy đã sắp xếp.<br>- `ForwardIterator last`: Iterator kết thúc dãy đã sắp xếp.<br>- `const T& value`: Giá trị cần tìm. | Trả về cặp iterator `(lower, upper)`, trong đó `lower` là `lower_bound(value)` và `upper` là `upper_bound(value)`, xác định phạm vi chứa tất cả các phần tử bằng `value`. | $O(\log n)$ | 

> [!info] Lưu ý
> - **Tất cả các phương thức trên chỉ hoạt động chính xác khi dãy đã được sắp xếp.**
> - **Iterator có thể là `vector<T>::iterator`, `array<T, N>::iterator`, hoặc bất kỳ iterator nào của một container STL hỗ trợ truy cập tuần tự.**
> - **Nếu `value` không tồn tại, `lower_bound` và `upper_bound` sẽ trỏ đến vị trí mà `value` có thể được chèn vào để duy trì thứ tự.**

```cpp {2,8-9,11-12,14-15,17-18,20-21}
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    vector<int> arr = {1, 3, 3, 5, 7, 9, 11, 13, 15, 17};
    int target = 3;
    
    bool found = binary_search(arr.begin(), arr.end(), target);
    cout << "binary_search: " << (found ? "Tim thay" : "Khong tim thay") << endl;
    
    auto lower = lower_bound(arr.begin(), arr.end(), target);
    cout << "lower_bound: Chi so " << (lower - arr.begin()) << endl;
    
    auto upper = upper_bound(arr.begin(), arr.end(), target);
    cout << "upper_bound: Chi so " << (upper - arr.begin()) << endl;
    
    auto range = equal_range(arr.begin(), arr.end(), target);
    cout << "equal_range: Tu chi so " << (range.first - arr.begin()) << " den " << (range.second - arr.begin()) << endl;
    
    return 0;
}
```

```txt title="Đầu ra"
binary_search: Tim thay
lower_bound: Chi so 1
upper_bound: Chi so 3
equal_range: Tu chi so 1 den 3
```

> [!explain]- Giải thích code
> - **Dòng 2:** Import thư viện để sử dụng `binary_search`, `lower_bound`, `upper_bound` và `equal_range`
> - **Dòng 8:** Khởi tạo vector đã **sắp xếp**.
> - **Dòng 9:** Giá trị cần tìm.
> - **Dòng 11:** Kiểm tra `target` có tồn tại trong `arr` không.
> - **Dòng 12:** Xuất kết quả `"Tim thay"` hoặc `"Khong tim thay"`.
> - **Dòng 14:** Tìm vị trí phần tử **đầu tiên** có giá trị **≥ target**.
> - **Dòng 15:** Xuất chỉ số của phần tử đó.
> - **Dòng 17:** Tìm vị trí phần tử **đầu tiên** có giá trị **> target**.
> - **Dòng 18:** Xuất chỉ số của phần tử đó.
> - **Dòng 20:** Trả về **khoảng (first, second)** trong mảng có giá trị **== target**.
> - **Dòng 21:** Xuất chỉ số từ `first` đến `second`.

---

# 🔥 Tổng kết
Tìm kiếm nhị phân là thuật toán tìm kiếm hiệu quả trên **dữ liệu đã sắp xếp** với độ phức tạp $O(\log n)$. Nhanh hơn **tìm kiếm tuyến tính** $O(n)$, đặc biệt khi kích thước dữ liệu lớn. C++ STL giúp triển khai dễ dàng và tối ưu hóa hiệu suất với 4 phương thức sau:

- `binary_search`: Kiểm tra sự tồn tại của một phần tử.
- `lower_bound`: Tìm phần tử đầu tiên **≥ giá trị cần tìm**.
- `upper_bound`: Tìm phần tử đầu tiên **> giá trị cần tìm**.
- `equal_range`: Xác định phạm vi chứa tất cả các phần tử bằng giá trị cần tìm.

Tìm kiếm nhị phân là lựa chọn hàng đầu khi tìm kiếm trên **dữ liệu tĩnh đã sắp xếp**, đặc biệt trong **cấu trúc dữ liệu mảng hoặc vector**. 🚀