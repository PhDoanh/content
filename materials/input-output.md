---
date: 2025-01-25
draft: false
status: Done
title: Xử lý vào/ra trong C++
description: ""
author: PhDoanh
authorlink: https://github.com/PhDoanh
tags:
  - coding
  - cpp
  - cph
  - competitive
  - basic
aliases:
  - input output
  - Xử lý vào/ra trong C++
cssclasses:
  - img
  - btn
---
%% ĐỊNH DẠNG TÊN FILE: "tên-bài-viết" | VD: jp-typing-guide %%

%% <figure style="text-align: center; margin: 20px auto;">
  <img 
    src="images/input-output.png"
    alt="Xử lý vào/ra trong C++" 
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
    <em>Xử lý vào/ra trong C++</em>
  </figcaption>
</figure> %%

Trong bài viết này, chúng ta sẽ tìm hiểu về **xử lý vào/ra (I/O)** trong C++ thông qua một bài toán đơn giản, cùng với các phương pháp và công cụ phổ biến như thư viện `<iostream>`, `<cstdio>`, và `<fstream>`. Ngoài ra, chúng ta cũng sẽ khám phá cách làm việc với tệp tin và một số mẹo hữu ích. 🚀

# ❓ Bài toán
Viết một chương trình C++ đọc hai số nguyên từ bàn phím, tính tổng của chúng và in kết quả ra màn hình.

```txt title="Đầu vào mẫu"
1 2
```

```md title="Đầu ra mẫu"
3
```

# ⚖️ Vào/ra tiêu chuẩn
## Thư viện `iostream`
Thư viện `<iostream>` là công cụ chính để thực hiện các thao tác **nhập/xuất tiêu chuẩn** trong C++. Nó cung cấp các đối tượng như `std::cin` (nhập) và `std::cout` (xuất).

```cpp {6-7}
#include <iostream>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;
    cout << a + b << endl;
    return 0;
}
```

> [!explain]- Giải thích code
> - **Dòng 6**: Nhập 2 số nguyên
> - **Dòng 7**: Tính tổng và xuất kết quả

> [!info] Lưu ý
> - `std::cin` tự động bỏ qua **khoảng trắng** và ký tự **xuống dòng**.
> - Sử dụng `std::endl` để xuống dòng và xóa bộ đệm.
> - Để nhập cả dòng văn bản, sử dụng `std::getline`.

## Thư viện `cstdio`
Thư viện `<cstdio>` cung cấp các hàm nhập/xuất kiểu C như `scanf` và `printf`. Nó thường được sử dụng khi cần hiệu suất cao hoặc tương thích với mã C.

```cpp {6-7}
#include <cstdio>
using namespace std;

int main() {
    int a, b;
    scanf("%d %d", &a, &b);  
    printf("%d\n", a + b);  
    return 0;
}
```

> [!explain]- Giải thích code
> - **Dòng 6**: Nhập 2 số nguyên
> - **Dòng 7**: Tính tổng và xuất kết quả

> [!info] Lưu ý
> - `scanf` yêu cầu chỉ định định dạng đầu vào (ví dụ: `%d` cho số nguyên).
> - `printf` cho phép định dạng đầu ra linh hoạt hơn so với `std::cout`. 
> - Luôn kiểm tra giá trị trả về của `scanf` để đảm bảo nhập liệu thành công.

# 📂 Vào/ra tệp
## Hàm `freopen`
Hàm `freopen` cho phép chuyển hướng luồng nhập/xuất tiêu chuẩn (`stdin`, `stdout`) sang tệp tin.

```cpp {5-6}
#include <cstdio>
using namespace std;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int a, b;
    scanf("%d %d", &a, &b);
    printf("%d\n", a + b);
    return 0;
}
```

> [!explain]- Giải thích code
> - **Dòng 1**: Thư viện để sử dụng `freopen`
> - **Dòng 5**: Chuyển hướng nhập từ tệp
> - **Dòng 6**: Chuyển hướng xuất sang tệp

> [!info] Lưu ý
> - `cin` và `cout` cũng hoạt động với `freopen` 
> - `freopen` hữu ích khi cần đọc/ghi dữ liệu từ **tệp tin** thay vì bàn phím/màn hình.
> - Luôn kiểm tra xem tệp tin có tồn tại không trước khi sử dụng.
> - Trong thi đấu lập trình, đuôi tệp đầu vào thường là `.in` còn đuôi tệp đầu ra thường là `.out`

## Thư viện `fstream`
Thư viện `<fstream>` cung cấp các lớp để làm việc với tệp tin, bao gồm `ifstream` (đọc tệp) và `ofstream` (ghi tệp).

```cpp {5-6,8-11}
#include <fstream>
using namespace std;

int main() {
    ifstream inFile("input.txt"); 
    ofstream outFile("output.txt");
    int a, b;
    inFile >> a >> b; 
    outFile << a + b << endl;
    inFile.close(); 
    outFile.close();
    return 0;
}
```

> [!explain]- Giải thích code
> - **Dòng 5**:  Mở tệp để đọc
> - **Dòng 6**: Mở tệp để ghi
> - **Dòng 8**: Đọc dữ liệu từ tệp
> - **Dòng 9**: Ghi kết quả vào tệp
> - **Dòng 10, 11**: Đóng tệp 

> [!info] Lưu ý
> - Luôn đóng tệp sau khi sử dụng bằng phương thức `close()`.
> - Kiểm tra xem tệp có mở thành công không bằng phương thức `is_open()`

# 🔥 Tổng kết
**Vào/ra tiêu chuẩn** thì sử dụng `<iostream>` hoặc `<cstdio>` để nhập/xuất dữ liệu từ bàn phím/màn hình. Còn **vào/ra tệp** thì dùng `freopen` hoặc `<fstream>` để làm việc với tệp tin.  

Mỗi phương pháp có ưu điểm riêng, tùy thuộc vào yêu cầu của bài toán:
- `<iostream>` dễ sử dụng và phù hợp cho các bài toán đơn giản.
- `<cstdio>` hiệu quả hơn về hiệu suất nhưng đòi hỏi cẩn thận khi sử dụng.
- `<fstream>` linh hoạt và mạnh mẽ cho các bài toán liên quan đến tệp tin.

