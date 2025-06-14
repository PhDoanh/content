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
  - type parameters
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
    src="images/type-parameters.png"
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

## 🧠 Tổng quan

- **Type Parameters** cho phép tạo các lớp và phương thức có thể làm việc với nhiều kiểu dữ liệu khác nhau mà không cần viết lại mã cho từng kiểu cụ thể.
    
- Các cấu trúc dữ liệu như `ArrayList<T>` và `HashMap<K, V>` sử dụng type parameters để xử lý dữ liệu một cách linh hoạt.[Class Central](https://www.classcentral.com/course/mooc-fi-java-programming-89476?utm_source=chatgpt.com)
    

---

## 🧰 Cách khai báo lớp generic

```java
public class Locker<T> {
    private T element;

    public void setValue(T element) {
        this.element = element;
    }

    public T getValue() {
        return element;
    }
}
```

- `T` là một tham số kiểu đại diện cho bất kỳ kiểu dữ liệu nào.
    
- Khi tạo đối tượng, bạn chỉ định kiểu cụ thể:
    

```java
Locker<String> stringLocker = new Locker<>();
stringLocker.setValue("Hello");
System.out.println(stringLocker.getValue()); // Output: Hello
```

---

## 🧑‍🤝‍🧑 Lớp với nhiều tham số kiểu

```java
public class Pair<T, K> {
    private T first;
    private K second;

    public void setValues(T first, K second) {
        this.first = first;
        this.second = second;
    }

    public T getFirst() {
        return this.first;
    }

    public K getSecond() {
        return this.second;
    }
}
```

- Sử dụng:
    

```java
Pair<String, Integer> pair = new Pair<>();
pair.setValues("Age", 30);
System.out.println(pair.getFirst());  // Output: Age
System.out.println(pair.getSecond()); // Output: 30
```

---

## 🧪 Ví dụ sử dụng generic

```java
Locker<Integer> intLocker = new Locker<>();
intLocker.setValue(100);
System.out.println(intLocker.getValue()); // Output: 100

Locker<Random> randomLocker = new Locker<>();
randomLocker.setValue(new Random());
System.out.println(randomLocker.getValue().nextDouble()); // Output: [random double]
```

---

## 🧩 Giao diện generic

```java
public interface List<T> {
    void add(T value);
    T get(int index);
    T remove(int index);
}
```

- Khi một lớp triển khai giao diện này, nó có thể xác định kiểu cụ thể cho `T` hoặc tiếp tục sử dụng generic.[Materiaalit](https://materiaalit.github.io/2013-oo-programming/part1/week-3/?utm_source=chatgpt.com)

---

## 🧠 Ghi nhớ

- Sử dụng type parameters giúp mã linh hoạt và dễ bảo trì hơn.
- Các lớp và giao diện generic cho phép tái sử dụng mã với nhiều kiểu dữ liệu khác nhau.
- Luôn chỉ định kiểu cụ thể khi tạo đối tượng từ lớp generic để tránh lỗi tại thời điểm biên dịch.
