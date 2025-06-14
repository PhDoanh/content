---
date: 2025-06-01
draft: true
status: Not started
title: 
description: 
author: PhDoanh
authorlink: https://github.com/PhDoanh
tags:
  - oop
aliases:
  - handling collections as streams
cssclasses:
  - img
  - btn
---
%% LƯU Ý 
- Định dạng tên file: "tên-bài-viết" (jp-typing-guide, ...) 
%%

%% banner
<figure style="text-align: center; margin: 20px auto;">
  <img 
    src="images/handling-collections-as-streams.png"
    alt="" 
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
    <em>caption</em>
  </figcaption>
</figure>
 %%

## 🎯 Mục tiêu chính

- Hiểu và sử dụng Stream API để xử lý tập hợp dữ liệu.
    
- Biết cách sử dụng biểu thức lambda.
    
- Nắm vững các phương thức phổ biến của stream và phân biệt giữa các thao tác trung gian (intermediate) và kết thúc (terminal).[Java Programming](https://java-programming.mooc.fi/part-10/?utm_source=chatgpt.com)
    

---

## 🧠 Kiến thức cốt lõi

### 1. Tạo Stream từ Collection

Sử dụng phương thức `stream()` để tạo stream từ các collection như `List`, `Set`, v.v.[Java Programming+1Class Central+1](https://java-programming.mooc.fi/part-10/?utm_source=chatgpt.com)

```java
List<String> list = Arrays.asList("1", "2", "3");
Stream<String> stream = list.stream();
```

### 2. Biểu thức Lambda

Biểu thức lambda cho phép định nghĩa các hàm ngắn gọn.

```java
s -> Integer.valueOf(s)
```

### 3. Các phương thức Stream phổ biến

- **`mapToInt`**: Chuyển đổi các phần tử thành `int`.
- **`filter`**: Lọc các phần tử theo điều kiện.
- **`count`**: Đếm số phần tử.
- **`average`**: Tính trung bình.

---

## 💻 Ví dụ thực tế

Đọc danh sách số từ người dùng, tính số lượng số chia hết cho 3 và trung bình cộng:

```java
Scanner scanner = new Scanner(System.in);
List<String> inputs = new ArrayList<>();

while (true) {
    String row = scanner.nextLine();
    if (row.equals("end")) {
        break;
    }
    inputs.add(row);
}

long divisibleByThree = inputs.stream()
    .mapToInt(s -> Integer.valueOf(s))
    .filter(number -> number % 3 == 0)
    .count();

double average = inputs.stream()
    .mapToInt(s -> Integer.valueOf(s))
    .average()
    .getAsDouble();

System.out.println("Divisible by three: " + divisibleByThree);
System.out.println("Average number: " + average);
```

---

## 📝 Ghi chú nhanh

- **`stream()`**: Tạo stream từ collection.
- **`mapToInt()`**: Chuyển đổi phần tử sang `int`.
- **`filter()`**: Lọc phần tử theo điều kiện.
- **`count()`**: Đếm số phần tử.
- **`average()`**: Tính trung bình.[Java Programming+1Class Central+1](https://java-programming.mooc.fi/part-10/?utm_source=chatgpt.com)[Class Central+3Java Programming+3Java Programming+3](https://java-programming.mooc.fi/part-10/2-interface-comparable/?utm_source=chatgpt.com)

---

## 📌 Mẹo ôn tập
- Thực hành viết các biểu thức lambda đơn giản.
- Luyện tập sử dụng các phương thức `map`, `filter`, `collect`, v.v.
- Hiểu rõ sự khác biệt giữa thao tác trung gian và kết thúc trong stream.
