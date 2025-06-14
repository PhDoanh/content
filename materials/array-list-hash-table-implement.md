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
  - array list hash table implement
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
    src="images/array-list-hash-table-implement.png"
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

## 📦 Mảng (Array) trong Java

- Mảng có kích thước cố định, được xác định khi khởi tạo.
- Truy cập phần tử qua chỉ số (index), bắt đầu từ 0.

```java
int[] numbers = new int[3];
numbers[0] = 2;
numbers[2] = 5;
System.out.println(numbers[0]); // 2
System.out.println(numbers[2]); // 5
```

---

## 📋 Tự triển khai `List` (giống `ArrayList`)

### Khởi tạo lớp `List`:

```java
public class List<Type> {
    private Type[] values;
    private int size;

    public List() {
        this.values = (Type[]) new Object[10];
        this.size = 0;
    }
}
```

### Thêm phần tử:

```java
public void add(Type value) {
    if (size == values.length) {
        grow();
    }
    values[size] = value;
    size++;
}
```

### Lấy phần tử:

```java
public Type get(int index) {
    if (index < 0 || index >= size) {
        throw new IndexOutOfBoundsException("Index out of bounds");
    }
    return values[index];
}
```

### Kiểm tra sự tồn tại:

```java
public boolean contains(Type value) {
    for (int i = 0; i < size; i++) {
        if (values[i].equals(value)) {
            return true;
        }
    }
    return false;
}
```

### Xóa phần tử:
```java
public void remove(Type value) {
    for (int i = 0; i < size; i++) {
        if (values[i].equals(value)) {
            remove(i);
            return;
        }
    }
}

private void remove(int index) {
    for (int i = index; i < size - 1; i++) {
        values[i] = values[i + 1];
    }
    values[size - 1] = null;
    size--;
}
```

### Tăng kích thước mảng:

```java
private void grow() {
    int newSize = values.length + values.length / 2;
    Type[] newValues = (Type[]) new Object[newSize];
    for (int i = 0; i < values.length; i++) {
        newValues[i] = values[i];
    }
    values = newValues;
}
```


## 🗃️ Tự triển khai `HashTable` (giống `HashMap`)

### Cấu trúc lớp `HashTable`:

```java
public class HashTable<K, V> {
    private List<Pair<K, V>>[] buckets;
    private int size;

    public HashTable() {
        this.buckets = new List[32];
        this.size = 0;
    }
}
```

### Lớp `Pair` để lưu trữ cặp khóa-giá trị:

```java
public class Pair<K, V> {
    private K key;
    private V value;

    public Pair(K key, V value) {
        this.key = key;
        this.value = value;
    }

    public K getKey() { return key; }
    public V getValue() { return value; }
    public void setValue(V value) { this.value = value; }
}
```

### Thêm cặp khóa-giá trị:

```java
public void add(K key, V value) {
    int hash = Math.abs(key.hashCode() % buckets.length);
    if (buckets[hash] == null) {
        buckets[hash] = new List<>();
    }

    for (int i = 0; i < buckets[hash].size(); i++) {
        if (buckets[hash].get(i).getKey().equals(key)) {
            buckets[hash].get(i).setValue(value);
            return;
        }
    }

    buckets[hash].add(new Pair<>(key, value));
    size++;
}
```

### Lấy giá trị theo khóa:

```java
public V get(K key) {
    int hash = Math.abs(key.hashCode() % buckets.length);
    if (buckets[hash] == null) {
        return null;
    }

    for (int i = 0; i < buckets[hash].size(); i++) {
        if (buckets[hash].get(i).getKey().equals(key)) {
            return buckets[hash].get(i).getValue();
        }
    }

    return null;
}
```

### Xóa cặp khóa-giá trị:

```java
public void remove(K key) {
    int hash = Math.abs(key.hashCode() % buckets.length);
    if (buckets[hash] == null) {
        return;
    }

    for (int i = 0; i < buckets[hash].size(); i++) {
        if (buckets[hash].get(i).getKey().equals(key)) {
            buckets[hash].remove(i);
            size--;
            return;
        }
    }
}
```

---

## 🔍 Ghi nhớ

- **Mảng**: Kích thước cố định, truy cập nhanh qua chỉ số.
- **ArrayList**: Mảng động, tự động tăng kích thước khi cần.
- **HashMap**: Bảng băm, cho phép truy cập nhanh theo khóa.
- **Tự triển khai**: Hiểu rõ cơ chế hoạt động bên trong giúp tối ưu hóa và xử lý lỗi hiệu quả hơn.