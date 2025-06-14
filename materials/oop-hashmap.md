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
  - oop hashmap
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
    src="images/oop-hashmap.png"
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

## 🧠 Tổng Quan về HashMap

- **HashMap** là một cấu trúc dữ liệu lưu trữ các cặp khóa-giá trị (key-value).
- Mỗi khóa là duy nhất và ánh xạ đến một giá trị.
- Các thao tác chính:
    - `put(key, value)`: Thêm hoặc cập nhật một cặp khóa-giá trị.
    - `get(key)`: Truy xuất giá trị dựa trên khóa.
    - `remove(key)`: Xóa cặp khóa-giá trị.
    - `containsKey(key)`: Kiểm tra sự tồn tại của khóa.
    - `containsValue(value)`: Kiểm tra sự tồn tại của giá trị.
- Nếu truy xuất một khóa không tồn tại, `get` sẽ trả về `null`.[GeeksforGeeks](https://www.geeksforgeeks.org/java-util-hashmap-in-java-with-examples/?utm_source=chatgpt.com)[Reddit+1Java Programming+1](https://www.reddit.com/r/javahelp/comments/o35y3a/java_mooc_part_2_exercise_8_airport_could_use/?utm_source=chatgpt.com)[Java Programming](https://java-programming.mooc.fi/part-8/2-hash-map/?utm_source=chatgpt.com)

---

## 🛠️ Cách Sử Dụng HashMap

### 1. Khởi tạo và thêm dữ liệu
```java
import java.util.HashMap;

HashMap<String, String> postalCodes = new HashMap<>();
postalCodes.put("00710", "Helsinki");
postalCodes.put("90014", "Oulu");
postalCodes.put("33720", "Tampere");
postalCodes.put("33014", "Tampere");
```

### 2. Truy xuất dữ liệu
```java
System.out.println(postalCodes.get("00710")); // Output: Helsinki
System.out.println(postalCodes.get("99999")); // Output: null
```

### 3. Ghi đè giá trị với cùng khóa

```java
HashMap<String, String> numbers = new HashMap<>();
numbers.put("Uno", "One");
numbers.put("Uno", "Ein"); // Ghi đè giá trị cũ
System.out.println(numbers.get("Uno")); // Output: Ein
```

---

## 🔄 Duyệt Qua HashMap

```java
for (String key : postalCodes.keySet()) {
    System.out.println(key + " => " + postalCodes.get(key));
}
```

---

## 📚 Sử Dụng Đối Tượng Làm Giá Trị

```java
public class Book {
    private String name;
    private int published;
    private String content;

    public Book(String name, int published, String content) {
        this.name = name;
        this.published = published;
        this.content = content;
    }

    public String getName() {
        return name;
    }

    public int getPublished() {
        return published;
    }

    public String getContent() {
        return content;
    }
}

HashMap<String, Book> books = new HashMap<>();
books.put("Clean Code", new Book("Clean Code", 2008, "A Handbook of Agile Software Craftsmanship"));
Book book = books.get("Clean Code");
System.out.println(book.getContent()); // Output: A Handbook of Agile Software Craftsmanship
```

---

## 🧩 Lưu Ý

- **Hiệu suất**: HashMap cho phép truy xuất dữ liệu nhanh chóng, thường với độ phức tạp thời gian trung bình là O(1) cho các thao tác cơ bản.
- **Khóa duy nhất**: Mỗi khóa trong HashMap là duy nhất; thêm một cặp với khóa đã tồn tại sẽ ghi đè giá trị cũ.
- **Null**: HashMap cho phép một khóa null và nhiều giá trị null.[Medium](https://medium.com/%40reetesh043/understanding-hashmap-in-java-f2fddb1f3b44?utm_source=chatgpt.com)

---

## 📘 Tài Nguyên Học Tập

- [Java Programming MOOC – Part 8, Mục 2: Hash Map](https://java-programming.mooc.fi/part-8/2-hash-map/)
- GeeksforGeeks: HashMap in Java
- Baeldung: A Guide to Java HashMap

