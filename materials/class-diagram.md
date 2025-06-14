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
  - uml
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
    src="images/uml.png"
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

## 🧱 1. Tổng quan về Class Diagram

- **Class Diagram** là sơ đồ mô tả cấu trúc tĩnh của hệ thống phần mềm, thể hiện các lớp, thuộc tính, phương thức và mối quan hệ giữa chúng.
- Được sử dụng trong thiết kế và mô hình hóa phần mềm, cho phép hiểu rõ cấu trúc hệ thống mà không cần xem mã nguồn.

---

## 📦 2. Cấu trúc của một lớp trong Class Diagram

Một lớp được biểu diễn bằng một hình chữ nhật chia thành ba phần:
1. **Tên lớp**: Được đặt ở phần trên cùng.
2. **Thuộc tính (Attributes)**: Liệt kê các biến thành viên của lớp.
3. **Phương thức (Methods)**: Liệt kê các hàm thành viên của lớp.

**Ký hiệu truy cập**:

- `+`: public
- `-`: private
- `#`: protected
- `~`: package (không có từ khóa cụ thể)

**Ví dụ**:

```java
public class Person {
    private String name;
    private int age;

    public Person(String initialName) {
        this.name = initialName;
        this.age = 0;
    }

    public void printPerson() {
        System.out.println(this.name + ", age " + this.age + " years");
    }

    public String getName() {
        return this.name;
    }
}
```

**Class Diagram tương ứng**:

```txt
-------------------------
|        Person         |
-------------------------
| - name: String        |
| - age: int            |
-------------------------
| + Person(initialName: String) |
| + printPerson(): void |
| + getName(): String   |
-------------------------
```

---

## 🔗 3. Mối quan hệ giữa các lớp

### a. **Association (Liên kết)**

- Thể hiện mối quan hệ giữa các đối tượng của hai lớp.
- Ví dụ: Một `Person` có một `Address`.

```java
public class Address {
    private String street;
    private String city;
}

public class Person {
    private String name;
    private Address address;
}
```

**Class Diagram**:

```txt
Person --------> Address
```

- **Biểu diễn**: Đường nét liền giữa hai lớp.
- **Mũi tên**: Có thể có hoặc không.
    - **Không có mũi tên**: Mối quan hệ **hai chiều**; cả hai lớp đều biết về nhau.
    - **Có mũi tên**: Mối quan hệ **một chiều**; lớp ở đầu mũi tên biết về lớp ở đuôi mũi tên.
- **Mũi tên từ A đến B**: Lớp A biết về lớp B; A có thể gọi các phương thức hoặc truy cập thuộc tính của B.

### b. **Aggregation (Tập hợp)**

- Mối quan hệ "có" mà các thành phần có thể tồn tại độc lập.
- Ví dụ: Một `Team` có nhiều `Player`.

```java
public class Player {
    private String name;
}

public class Team {
    private List<Player> players;
}
```

**Class Diagram**:

```txt
Team ◇-------- Player
```

### c. **Composition (Thành phần)**

- Mối quan hệ "bao gồm" mà các thành phần không thể tồn tại độc lập.
- Ví dụ: Một `House` có nhiều `Room`.

```java
public class Room {
    private String name;
}

public class House {
    private List<Room> rooms;
}
```

**Class Diagram**:

```txt
House ◆-------- Room
```

### d. **Inheritance (Kế thừa)**

- Thể hiện mối quan hệ "là một" giữa lớp con và lớp cha.
- Ví dụ: `Student` kế thừa từ `Person`.

```java
public class Person {
    private String name;
}

public class Student extends Person {
    private int studentId;
}
```

**Class Diagram**:

```txt
Person <|---- Student
```
**Mũi tên rỗng hình tam giác** tại đầu lớp cha, chỉ hướng kế thừa.

Lưu ý: Đối với triển khai giao diện, dùng mũi tên nét đứt hình tam giác rỗng tại lớp giao diện, chỉ hướng triển khai!

---

## 📝 4. Lưu ý khi đọc Class Diagram
- **Chỉ mô tả cấu trúc**, không thể hiện chi tiết thực thi của phương thức.
- **Không thể hiện logic nội bộ** của các phương thức hoặc luồng dữ liệu.
- **Hữu ích trong giai đoạn thiết kế** để hiểu tổng quan hệ thống.

---

## 🔢 **Multiplicity (Bội số)**

Bội số xác định số lượng thể hiện của một lớp có thể liên kết với một thể hiện của lớp khác. Chúng được ghi gần đầu mối quan hệ và có ý nghĩa như sau:

- `1`: Chính xác một thể hiện.
- `0..1`: Không hoặc một thể hiện.
- `0..*` hoặc `*`: Không giới hạn số lượng thể hiện (bao gồm cả không có).
- `1..*`: Ít nhất một thể hiện.[Stack Overflow](https://stackoverflow.com/questions/14529185/can-someone-explain-this-uml-diagram?utm_source=chatgpt.com)[Gleek+1Stack Overflow+1](https://www.gleek.io/blog/class-diagram-arrows?utm_source=chatgpt.com)

---

## 🔍 5. Tài liệu tham khảo

- [Java Programming MOOC - Phần 11: Class Diagrams](https://java-programming.mooc.fi/part-11/1-class-diagrams/)
- [Wikipedia - Class Diagram](https://en.wikipedia.org/wiki/Class_diagram)