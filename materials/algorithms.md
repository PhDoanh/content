---
date: 2025-03-20
draft: true
status: Doing
title: Tầm quan trọng của Thuật toán trong thi đấu lập trình
description: ""
author: PhDoanh
authorlink: https://github.com/PhDoanh
tags:
  - dsa
  - coding
  - cpp
  - competitive
  - dsa
  - algorithms
aliases:
  - algorithms
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
    src="images/algorithms.png"
    alt="Thuật toán trong thi đấu lập trình" 
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

# 👀 Giới thiệu về Thuật toán
![[Pasted image 20250320080446.png]]

![[Pasted image 20250320080652.png]]



> [!check] Ưu điểm
> 

> [!missing] Nhược điểm
> 

# Thiết kế thuật toán

![[Pasted image 20250320080606.png]]

---

# Các loại thuật toán

## Thuật toán cơ bản

### Công thức toán học

### Tìm kiếm

### Sắp xếp


## Thuật toán Vét cạn

![[Pasted image 20250320080745.png]]

### Vét cạn bằng kỹ thuật đề quy

![[Pasted image 20250320081050.png]]

![[Pasted image 20250320081057.png]]

> [!example]- Ví dụ
> **Mô tả thuật toán tính giai thừa**:
> 
> ![[Pasted image 20250320081201.png]]
> 
> **Thuật toán tính hàm mũ**:
> 1. Đệ quy tuyến tính
> ![[Pasted image 20250320081417.png]]
> 
> 2. Đệ quy bình phương:
> ![[Pasted image 20250320081516.png]]
> ![[Pasted image 20250320081630.png]]

### Một số bài toán dùng Vét cạn

- [[binary-exponentiation|Lũy thừa nhị phân]]
- Tất cả các hoán vị
- Tất cả các chuỗi nhị phân có độ dài n


## Thuật toán Chia để trị

![[Pasted image 20250320083204.png]]

> [!example]- Ví dụ
> 1. Tìm kiếm nhị phân
> ![[Pasted image 20250320083300.png]]
> ![[Pasted image 20250320083350.png]]
> 
> 2. Sắp xếp trộn
> ![[Pasted image 20250320083434.png]]
> ![[Pasted image 20250320083448.png]]
> ![[Pasted image 20250320083505.png]]
> ![[Pasted image 20250320083558.png]]

> [!info]- Lưu ý
> ![[Pasted image 20250320083631.png]]

### Một số bài toán dùng Chia để trị



## Thuật toán Quy hoạch động

![[Pasted image 20250320084231.png]]

![[Pasted image 20250320084244.png]]

Giải pháp:
![[Pasted image 20250320084321.png]]

![[Pasted image 20250320084411.png]]

Quy trình:
![[Pasted image 20250320084457.png]]


### Một số bài toán dùng Quy hoạch động

- Chuỗi con đối xứng dài nhất - Longest Palindromic Subsequence - LPS
- Biến đổi chuỗi - Edit Distance - Levenshtein Distance
- Dãy con tăng dài nhất - Longest Increasing Subsequence - LIS
- Chuỗi con chung dài nhất - Longest Common Substring

- Bài toán cái túi KnapSack 0-1
```cpp
def knapsack(n, X, weights, values):
    # Khởi tạo mảng dp
    dp = [0] * (X + 1)
    
    # Duyệt qua từng đồ vật
    for i in range(n):
        # Duyệt từ phải qua trái để tránh tính trùng lặp
        for j in range(X, weights[i] - 1, -1):
            # Cập nhật giá trị lớn nhất có thể đạt được
            dp[j] = max(dp[j], dp[j - weights[i]] + values[i])
    
    return dp[X]

# Đọc input
n, X = map(int, input().split())
weights = []
values = []

for _ in range(n):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)

# Tính và in kết quả
result = knapsack(n, X, weights, values)
print(result)
```

Độ phức tạp: O(n × X)


## Thuật toán Tham lam

![[Pasted image 20250320084719.png]]


### Một số bài toán dùng Tham lam

- Knapsack problem
- Bài toán người du lịch - TSP


---

# ✨ Thuật toán trong thư viện chuẩn C++
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

# Các câu hỏi thường gặp

> [!caution]- Nội dung đang hoàn thiện
> Quá trình xây dựng nội dung này có thể mất nhiều thời gian ⌛, nhưng bạn có thể thúc đẩy nó bằng cách tham gia [[article-collaboration-guide|cộng tác bài viết]] 🤝
> 
> **Rất mong sự thông cảm của các bạn 🙏**

---

# 🔥 Tổng kết
%% tóm tắt, nhận xét %%
