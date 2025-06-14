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
  - comparable interface
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
    src="images/comparable-interface.png"
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

## 🧠 Giao diện `Comparable` trong Java

### ✅ Mục đích

Giao diện `Comparable` cho phép định nghĩa thứ tự tự nhiên (natural ordering) cho các đối tượng của một lớp.[Software Testing Help+3GeeksforGeeks+3HowToDoInJava+3](https://www.geeksforgeeks.org/comparable-interface-in-java-with-examples/?utm_source=chatgpt.com)

### 🧩 Cách sử dụng

- Khai báo lớp triển khai `Comparable<T>` với `T` là chính lớp đó.
    
- Cài đặt phương thức `compareTo(T other)` để so sánh đối tượng hiện tại với đối tượng khác.[Codecademy+2CodeRanch+2DigitalOcean+2](https://coderanch.com/t/664863/java/Java-Abstract-Classes-Comparable?utm_source=chatgpt.com)
    

### 🔢 Quy ước của `compareTo`

- Trả về **âm** nếu đối tượng hiện tại nhỏ hơn `other`.
    
- Trả về **0** nếu bằng nhau.
    
- Trả về **dương** nếu lớn hơn `other`.[Oracle Docs+9Codecademy+9W3Schools+9](https://www.codecademy.com/resources/docs/java/comparable?utm_source=chatgpt.com)
    

---

## 🧪 Ví dụ: Sắp xếp thành viên theo chiều cao

```java
public class Member implements Comparable<Member> {
    private String name;
    private int height;

    public Member(String name, int height) {
        this.name = name;
        this.height = height;
    }

    public String getName() {
        return this.name;
    }

    public int getHeight() {
        return this.height;
    }

    @Override
    public String toString() {
        return this.name + " (" + this.height + ")";
    }

    @Override
    public int compareTo(Member other) {
        return this.height - other.height;
    }
}
```

---

## 📚 Sắp xếp danh sách

```java
List<Member> members = new ArrayList<>();
members.add(new Member("Mikael", 182));
members.add(new Member("Matti", 187));
members.add(new Member("Ada", 184));

// Sắp xếp bằng Collections.sort
Collections.sort(members);

// Hoặc sử dụng Stream API
members.stream()
       .sorted()
       .forEach(System.out::println);
```

---

## ⚠️ Lưu ý
- `compareTo` chỉ cho phép sắp xếp theo một tiêu chí.
- Để sắp xếp theo nhiều tiêu chí, sử dụng `Comparator`.
- `Stream.sorted()` không thay đổi danh sách gốc; để sắp xếp danh sách gốc, sử dụng `Collections.sort()`.[Baeldung+1DigitalOcean+1](https://www.baeldung.com/java-comparator-comparable?utm_source=chatgpt.com)
    

---

## 📌 Tổng kết
- Sử dụng `Comparable` khi muốn định nghĩa thứ tự tự nhiên cho đối tượng.
- Triển khai `compareTo` để xác định cách so sánh.
- Sử dụng `Collections.sort()` hoặc `Stream.sorted()` để sắp xếp danh sách.

---

Tham khảo chi tiết tại: [The Comparable Interface - Java Programming MOOC](https://java-programming.mooc.fi/part-10/2-interface-comparable/)[DigitalOcean+2Java Programming+2Java Programming+2](https://java-programming.mooc.fi/part-10/2-interface-comparable/?utm_source=chatgpt.com)

## 🧠 Giao diện `Comparator` trong Java

### ✅ Mục đích

- Cho phép định nghĩa cách so sánh tùy chỉnh giữa các đối tượng.
- Hữu ích khi không thể hoặc không muốn thay đổi thứ tự tự nhiên (`Comparable`).

### 🧩 Cách sử dụng

- Sử dụng `Collections.sort(List<T> list, Comparator<? super T> c)` để sắp xếp danh sách với `Comparator` tùy chỉnh.
- Sử dụng `Stream.sorted(Comparator<? super T> comparator)` để sắp xếp luồng dữ liệu.
- Sử dụng `Comparator.comparing(Function<? super T, ? extends U> keyExtractor)` để tạo `Comparator` dựa trên thuộc tính cụ thể.

---

## 🧪 Ví dụ: Sắp xếp danh sách `Person` theo năm sinh

```java
public class Person {
    private String name;
    private int birthYear;

    public Person(String name, int birthYear) {
        this.name = name;
        this.birthYear = birthYear;
    }

    public String getName() {
        return this.name;
    }

    public int getBirthYear() {
        return this.birthYear;
    }

    @Override
    public String toString() {
        return this.name + " (" + this.birthYear + ")";
    }
}
```

Sắp xếp danh sách `persons` theo năm sinh:

```java
List<Person> persons = new ArrayList<>();
persons.add(new Person("Ada Lovelace", 1815));
persons.add(new Person("Irma Wyman", 1928));
persons.add(new Person("Grace Hopper", 1906));
persons.add(new Person("Mary Coombs", 1929));

// Sắp xếp bằng Comparator và lambda expression
persons.sort((p1, p2) -> p1.getBirthYear() - p2.getBirthYear());

// Hoặc sử dụng Comparator.comparing
persons.sort(Comparator.comparing(Person::getBirthYear));

// Sử dụng Stream API để sắp xếp và in ra
persons.stream()
       .sorted(Comparator.comparing(Person::getBirthYear))
       .forEach(System.out::println);
```

---

## ⚠️ Lưu ý

- `Comparator` cho phép sắp xếp theo nhiều tiêu chí bằng cách sử dụng `thenComparing`.
    
- Sử dụng `reversed()` để đảo ngược thứ tự sắp xếp.
    

Ví dụ: Sắp xếp theo năm sinh giảm dần, sau đó theo tên:

```java
persons.sort(
    Comparator.comparing(Person::getBirthYear).reversed()
              .thenComparing(Person::getName)
);
```

---

## 📌 Tổng kết

- Sử dụng `Comparator` khi cần sắp xếp theo tiêu chí tùy chỉnh hoặc nhiều tiêu chí.
- Kết hợp với `Collections.sort` hoặc `Stream.sorted` để sắp xếp danh sách hoặc luồng dữ liệu.
- Sử dụng `Comparator.comparing` và các phương thức liên quan để xây dựng `Comparator` một cách linh hoạt.
