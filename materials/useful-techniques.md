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
  - useful techniques
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
    src="images/useful-techniques.png"
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

## 🧠 Sổ Tay Kiến Thức: Các Kỹ Thuật Hữu Ích Khác (Part 10 - Java MOOC)

### 1. **StringBuilder – Tối Ưu Hóa Nối Chuỗi**

- **Vấn đề**: Sử dụng toán tử `+` để nối chuỗi trong vòng lặp tạo ra nhiều đối tượng `String` mới, gây tốn bộ nhớ và giảm hiệu suất.
    
- **Giải pháp**: Sử dụng `StringBuilder` để nối chuỗi một cách hiệu quả hơn.
    
- **Ví dụ**:
    
```java
StringBuilder numbers = new StringBuilder();
for (int i = 1; i < 5; i++) {
    numbers.append(i);
}
System.out.println(numbers.toString()); // Output: 1234
```
    

Chỉ tạo ra một đối tượng `StringBuilder` duy nhất, giúp tiết kiệm bộ nhớ và tăng hiệu suất.[Reddit+2Java Programming+2Stack Overflow+2](https://java-programming.mooc.fi/part-10/3-other-useful-techniques/?utm_source=chatgpt.com)

---

### 2. **Regular Expressions – Biểu Thức Chính Quy**

- **Khái niệm**: Biểu thức chính quy (regex) là một công cụ mạnh mẽ để kiểm tra định dạng chuỗi.
    
- **Cách sử dụng**: Sử dụng lớp `Pattern` và `Matcher` trong Java để làm việc với regex.
    
- **Ví dụ**: Kiểm tra mã số sinh viên bắt đầu bằng "01" và theo sau là 7 chữ số:[Java Programming](https://java-programming.mooc.fi/part-10/3-other-useful-techniques/?utm_source=chatgpt.com)
    
```java
import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class StudentNumberValidator {
    public static void main(String[] args) {
        String studentNumber = "012345678";
        Pattern pattern = Pattern.compile("01\\d{7}");
        Matcher matcher = pattern.matcher(studentNumber);
        if (matcher.matches()) {
            System.out.println("Mã số hợp lệ");
        } else {
            System.out.println("Mã số không hợp lệ");
        }
    }
}
```
    

Sử dụng regex giúp kiểm tra định dạng chuỗi một cách ngắn gọn và hiệu quả.

---

### 3. **Enum – Kiểu Liệt Kê**

- **Khái niệm**: `enum` là một kiểu dữ liệu đặc biệt trong Java, đại diện cho một tập hợp các hằng số cố định.
    
- **Cách sử dụng**: Định nghĩa `enum` và sử dụng trong chương trình để tăng tính rõ ràng và an toàn.
    
- **Ví dụ**: Định nghĩa các hướng di chuyển:
    
```java
public enum Direction {
    NORTH, EAST, SOUTH, WEST
}

public class Compass {
    public static void main(String[] args) {
        Direction dir = Direction.NORTH;
        System.out.println("Hướng hiện tại: " + dir);
    }
}
```
    

Sử dụng `enum` giúp mã nguồn rõ ràng và dễ bảo trì hơn.

---

### 4. **Iterator – Duyệt Qua Bộ Sưu Tập**

- **Khái niệm**: `Iterator` là một giao diện trong Java, cho phép duyệt qua các phần tử trong một bộ sưu tập (collection).
    
- **Cách sử dụng**: Sử dụng phương thức `iterator()` để lấy `Iterator` từ collection và duyệt qua các phần tử.
    
- **Ví dụ**: Duyệt qua một danh sách chuỗi:
    
```java
import java.util.ArrayList;
import java.util.Iterator;

public class IteratorExample {
    public static void main(String[] args) {
        ArrayList<String> list = new ArrayList<>();
        list.add("Apple");
        list.add("Banana");
        list.add("Cherry");

        Iterator<String> iterator = list.iterator();
        while (iterator.hasNext()) {
            String fruit = iterator.next();
            System.out.println(fruit);
        }
    }
}
```
    

Sử dụng `Iterator` giúp duyệt qua collection một cách an toàn và linh hoạt.

---

### ✅ Tổng Kết

- **StringBuilder**: Sử dụng để nối chuỗi hiệu quả hơn so với toán tử `+`.
    
- **Regular Expressions**: Công cụ mạnh mẽ để kiểm tra định dạng chuỗi.
    
- **Enum**: Định nghĩa các hằng số cố định, giúp mã nguồn rõ ràng và an toàn.
    
- **Iterator**: Duyệt qua các phần tử trong collection một cách an toàn và linh hoạt.