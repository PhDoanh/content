---
date: 2025-03-16
draft: true
status: Doing
title: Hàng đợi ưu tiên
description: ""
author: PhDoanh
authorlink: https://github.com/PhDoanh
tags:
  - dsa
  - coding
  - cpp
  - competitive
  - data-structure
  - queue
  - priority-queue
aliases:
  - priority queue
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
    src="images/priority-queue.png"
    alt="Hàng đợi ưu tiên" 
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

# 👀 Giới thiệu về priority queue
%% mô tả %%

> [!check] Ưu điểm
> 

> [!missing] Nhược điểm
> 

---

# 🛠️ Khai triển priority queue trong C++

## {tên thao tác}
%% mô tả %%

```cpp {}

```

> [!explain]- Giải thích code
> Dòng ?: 

---

# ✨ priority queue trong thư viện chuẩn C++
%% mô tả %%

| Phương thức | Kiểu trả về | Tham số | Mô tả | Độ phức tạp |
|:-----------:|:-----------:|:------- |:----- |:-----------:|
|             |             |         |       |             |

```cpp {}

```

```txt title="Đầu ra"

```

> [!explain]- Giải thích code
> Dòng ?:

---

# 🔥 Tổng kết
%% tóm tắt, nhận xét %%

# Ghi chép nhanh
## Giới thiệu
- Trong lý thuyết, **Priority Queue** thường được định nghĩa là một cấu trúc dữ liệu trong đó mỗi phần tử được lưu dưới dạng một cặp **key-value**, trong đó **key** xác định mức độ ưu tiên của phần tử và **value** là dữ liệu thực tế.
- **Ví dụ**: Trong một hệ thống quản lý tác vụ, ta có thể có các tác vụ với mức ưu tiên khác nhau, nơi mỗi tác vụ có thể có một **key** là mức ưu tiên và **value** là thông tin về tác vụ đó.

> [!info] Lưu ý
> Trong **C++ STL**, **`priority_queue`** không lưu trữ theo kiểu **key-value** vì mục tiêu của nó là đơn giản và hiệu quả, chỉ lưu trữ phần tử và ưu tiên của nó thông qua phép so sánh. Tuy nhiên, bạn có thể dễ dàng lưu trữ các cặp **key-value** bằng cách sử dụng các kiểu dữ liệu như **`std::pair`** và tự định nghĩa cách so sánh chúng để xác định mức độ ưu tiên.

**Các tính chất của Priority Queue ADT**:
- Mỗi phần tử trong priority queue có một **mức ưu tiên** liên quan đến nó.
- Các thao tác **Remove** và **Peek** luôn thao tác với phần tử có ưu tiên cao nhất (hoặc thấp nhất, tùy vào cách xác định ưu tiên).
- Các phần tử có thể được sắp xếp theo thứ tự ưu tiên hoặc theo thứ tự chèn, tùy thuộc vào cách triển khai.

![[Pasted image 20250316215716.png]]
![[Pasted image 20250316215749.png]]

## Triển khai bằng Heep Tree
![[Pasted image 20250316215832.png]]
![[Pasted image 20250316215855.png]]

## 