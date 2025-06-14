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
  - packages
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
    src="images/packages.png"
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

## 🗂️ Java Packages – Ghi chú nhanh

### 1. Packages là gì?

- Packages là cách tổ chức các lớp (classes) và giao diện (interfaces) trong Java thành các nhóm logic, tương tự như thư mục trong hệ thống tập tin.
- Giúp tránh xung đột tên lớp và dễ dàng quản lý mã nguồn trong các dự án lớn.[W3Schools+5Medium+5DataCamp+5](https://medium.com/%40pratik.941/packages-in-java-a-comprehensive-guide-b9ab6fecee20?utm_source=chatgpt.com)

### 2. Cách khai báo package

- Dòng đầu tiên trong file Java:[Wikipedia+2materiaalit.github.io+2DataCamp+2](https://materiaalit.github.io/2013-oo-programming/part2/week-11/?utm_source=chatgpt.com)

```java
package ten_goi;
```

- Tên package thường viết thường và theo cấu trúc thư mục.[Programiz+2DataCamp+2TutorialsPoint+2](https://www.datacamp.com/doc/java/package?utm_source=chatgpt.com)
    

### 3. Tạo package trong IDE

- Trong NetBeans:
    
    - Chuột phải vào `Source Packages` → `New` → `Java Package...`
        
    - Đặt tên package, ví dụ: `library.domain`[TutorialsPoint](https://www.tutorialspoint.com/java/java_packages.htm?utm_source=chatgpt.com)[Java Programming](https://java-programming.mooc.fi/part-11/2-packages/?utm_source=chatgpt.com)
        

### 4. Cấu trúc thư mục tương ứng

- Package `library.domain` tương ứng với thư mục:

```txt
  src/
    library/
      domain/
```

### 5. Ví dụ mã nguồn

#### 📁 `library/domain/Book.java`

```java
package library.domain;

public class Book {
    private String name;

    public Book(String name) {
        this.name = name;
    }

    public String getName() {
        return this.name;
    }
}
```

#### 📁 `library/Program.java`

```java
package library;

import library.domain.Book;

public class Program {
    public static void main(String[] args) {
        Book book = new Book("The ABCs of Packages!");
        System.out.println("Hello packageworld: " + book.getName());
    }
}
```

### 6. Sử dụng `import`

- Để sử dụng lớp từ package khác, dùng câu lệnh `import`:
```java
import library.domain.Book;
```

- Hoặc sử dụng tên đầy đủ khi tạo đối tượng:
```java
library.domain.Book book = new library.domain.Book("Title");
```

### 7. Access Modifiers và Packages

- `private`: Chỉ truy cập được trong cùng một lớp.
- `public`: Truy cập từ bất kỳ đâu.
- Không khai báo (default): Truy cập được trong cùng một package.[DataCamp+1Java Programming+1](https://www.datacamp.com/doc/java/package?utm_source=chatgpt.com)

### 8. Lưu ý

- Tránh sử dụng default package (không khai báo `package`) trong các dự án lớn.
- Tuân thủ quy ước đặt tên package: viết thường, theo cấu trúc thư mục.
- Sử dụng packages để tổ chức mã nguồn rõ ràng, dễ bảo trì.[DataCamp+1Java Programming+1](https://www.datacamp.com/doc/java/package?utm_source=chatgpt.com)
