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
  - equals hashcode
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
    src="images/equals-hashcode.png"
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

## 🧠 1. So sánh đối tượng trong Java

### 🔹 equals() mặc định
- Mặc định, `equals()` so sánh **tham chiếu** (địa chỉ bộ nhớ), không phải nội dung.
- Vì vậy, hai đối tượng có cùng giá trị nhưng khác địa chỉ sẽ không được coi là bằng nhau.

**Ví dụ:**

```java
Book book1 = new Book("Java Basics", 2020, "Content");
Book book2 = new Book("Java Basics", 2020, "Content");

System.out.println(book1.equals(book2)); // false
```

### 🔹 Ghi đè equals() để so sánh nội dung

- Để so sánh nội dung, cần ghi đè phương thức `equals()`.
    

**Mẫu triển khai:**

```java
@Override
public boolean equals(Object obj) {
    if (this == obj) return true;
    if (!(obj instanceof Book)) return false;
    Book other = (Book) obj;
    return this.name.equals(other.name) &&
           this.published == other.published &&
           this.content.equals(other.content);
}
```

---

## 🧩 2. hashCode() và HashMap

### 🔹 hashCode() mặc định

- Mặc định, `hashCode()` trả về giá trị dựa trên địa chỉ bộ nhớ.
    
- Điều này gây vấn đề khi sử dụng đối tượng làm **key** trong `HashMap`.
    

**Ví dụ:**

```java
HashMap<Book, String> borrowers = new HashMap<>();
Book book1 = new Book("Java Basics", 2020, "Content");
borrowers.put(book1, "Alice");

Book book2 = new Book("Java Basics", 2020, "Content");
System.out.println(borrowers.get(book2)); // null
```

### 🔹 Ghi đè hashCode() để phù hợp với equals()

- Cần ghi đè `hashCode()` để đảm bảo rằng các đối tượng bằng nhau theo `equals()` cũng có cùng `hashCode()`.
    

**Mẫu triển khai:**

```java
@Override
public int hashCode() {
    return Objects.hash(name, published, content);
}
```

---

## 📚 3. Lưu ý khi sử dụng equals() và hashCode()

- Luôn ghi đè cả `equals()` và `hashCode()` khi định nghĩa lại một trong hai.
- Sử dụng `Objects.equals()` và `Objects.hash()` để đơn giản hóa mã và tránh lỗi null.
- Trong IDE như NetBeans, có thể tự động tạo các phương thức này: **Source → Insert Code → equals() and hashCode()**.[Java Programming](https://java-programming.mooc.fi/part-8/3-similarity-of-objects/?utm_source=chatgpt.com)

---

## ✅ Tóm tắt

| Tình huống                        | Kết quả                              |
| --------------------------------- | ------------------------------------ |
| So sánh tham chiếu                | `==`                                 |
| So sánh nội dung                  | Ghi đè `equals()`                    |
| Sử dụng đối tượng làm key HashMap | Ghi đè cả `equals()` và `hashCode()` |

---

Để hiểu rõ hơn, bạn có thể tham khảo thêm tại: [Similarity of objects](https://java-programming.mooc.fi/part-8/3-similarity-of-objects).[Java Programming](https://java-programming.mooc.fi/part-8/3-similarity-of-objects/?utm_source=chatgpt.com)

