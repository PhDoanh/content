---
date: 2025-05-27
draft: true
status: Not started
title: 
description: 
author: PhDoanh
authorlink: https://github.com/PhDoanh
tags:
  - dsa
aliases:
  - hash table
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
    src="images/hash-table.png"
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

Trong bảng băm (hash table), **xử lý va chạm (collision resolution)** là kỹ thuật quan trọng để đảm bảo hiệu suất và độ chính xác khi nhiều khóa (key) được ánh xạ đến cùng một chỉ số. Dưới đây là hai kỹ thuật phổ biến trong C++ để xử lý va chạm, cùng với các phương pháp cụ thể và cách thiết kế hàm băm hiệu quả.

---

## 1. Separate Chaining (Liên kết riêng)

### 🔧 Cách hoạt động:

Mỗi vị trí trong bảng băm chứa một danh sách (thường là danh sách liên kết) để lưu trữ tất cả các phần tử có cùng chỉ số băm. Khi xảy ra va chạm, phần tử mới được thêm vào danh sách tại vị trí đó.

### 📌 Ưu điểm:

- Dễ dàng triển khai và mở rộng.
    
- Hiệu quả khi số lượng phần tử không quá lớn.
    
- Không bị giới hạn bởi kích thước của bảng băm.[Youcademy+2John Farrier+2Stack Overflow+2](https://johnfarrier.com/unlocking-the-power-of-stdhash-in-c-programming/?utm_source=chatgpt.com)
    

### ⚠️ Nhược điểm:

- Hiệu suất truy cập giảm khi danh sách tại một vị trí trở nên dài.
    
- Tiêu tốn bộ nhớ bổ sung cho các danh sách.
    

### 🛠️ Phương pháp triển khai:

- Sử dụng danh sách liên kết đơn hoặc đôi.
    
- Sử dụng cấu trúc dữ liệu khác như cây tìm kiếm nhị phân (BST) để cải thiện hiệu suất tìm kiếm.[Courses at UW+1GeeksforGeeks+1](https://courses.cs.washington.edu/courses/cse326/06su/lectures/lecture11.pdf?utm_source=chatgpt.com)

```cpp
#include <iostream>
#include <list>
#include <vector>

class HashTable {
    int capacity;
    std::vector<std::list<int>> table;

    int hashFunction(int key) {
        return key % capacity;
    }

public:
    HashTable(int size) : capacity(size), table(size) {}

    void insert(int key) {
        int index = hashFunction(key);
        table[index].push_back(key);
    }

    void display() {
        for (int i = 0; i < capacity; ++i) {
            std::cout << i;
            for (auto x : table[i])
                std::cout << " --> " << x;
            std::cout << std::endl;
        }
    }
};
```

## 2. Open Addressing (Địa chỉ mở)

### 🔧 Cách hoạt động:

Khi xảy ra va chạm, thuật toán tìm vị trí khác trong bảng băm theo một trình tự xác định để lưu trữ phần tử mới.

### 📌 Ưu điểm:

- Không cần cấu trúc dữ liệu bổ sung.
    
- Tận dụng tốt bộ nhớ đệm (cache) do dữ liệu nằm liền kề.
    

### ⚠️ Nhược điểm:

- Hiệu suất giảm khi bảng băm đầy.
    
- Cần xử lý cẩn thận khi xóa phần tử để tránh làm hỏng trình tự tìm kiếm.[Stack Overflow](https://stackoverflow.com/questions/10217012/hash-table-implementation-using-an-array-of-linked-lists?utm_source=chatgpt.com)
    

### 🛠️ Các phương pháp cụ thể:

#### a. Linear Probing (Thăm dò tuyến tính)

- Tìm vị trí tiếp theo bằng cách tăng chỉ số từng bước một.

```cpp
int hashFunction(int key) {
    return key % capacity;
}

void insert(int key) {
    int index = hashFunction(key);
    while (table[index] != -1) {
        index = (index + 1) % capacity;
    }
    table[index] = key;
}
```

#### b. Quadratic Probing (Thăm dò bậc hai)
- Tìm vị trí tiếp theo bằng cách tăng chỉ số theo bình phương của số lần thử.

```cpp
void insert(int key) {
    int index = hashFunction(key);
    int i = 1;
    while (table[index] != -1) {
        index = (index + i * i) % capacity;
        i++;
    }
    table[index] = key;
}
```

#### c. Double Hashing (Băm kép)
- Sử dụng một hàm băm thứ hai để xác định bước nhảy khi tìm vị trí mới.

```cpp
int secondHash(int key) {
    return 7 - (key % 7);
}

void insert(int key) {
    int index = hashFunction(key);
    int stepSize = secondHash(key);
    while (table[index] != -1) {
        index = (index + stepSize) % capacity;
    }
    table[index] = key;
}
```


## 3. Thiết kế hàm băm hiệu quả

### 🎯 Mục tiêu:

- Phân phối khóa đều trên toàn bộ bảng băm.
    
- Giảm thiểu va chạm.
    
- Tính toán nhanh chóng.[Ian Y.E. Pan+2Stack Overflow+2Stack Overflow+2](https://stackoverflow.com/questions/10217012/hash-table-implementation-using-an-array-of-linked-lists?utm_source=chatgpt.com)
    

### 🛠️ Các phương pháp phổ biến:

#### a. Division Method (Phương pháp chia)

- `hash(key) = key % table_size`
- Chọn `table_size` là số nguyên tố để giảm va chạm.
    

#### b. Multiplication Method (Phương pháp nhân)
- `hash(key) = floor(table_size * (key * A % 1))`
- `A` là hằng số thực giữa 0 và 1.

#### c. Sử dụng hàm băm có sẵn:

- `std::hash` trong C++ cung cấp hàm băm cho các kiểu dữ liệu cơ bản.
```cpp
#include <functional>

std::hash<int> intHash;
size_t hashValue = intHash(42);
```

#### d. Tự định nghĩa hàm băm cho kiểu dữ liệu tùy chỉnh:

- Cần định nghĩa hàm băm riêng khi sử dụng các kiểu dữ liệu do người dùng định nghĩa.
```cpp
struct Person {
    std::string name;
    int age;

    bool operator==(const Person& other) const {
        return name == other.name && age == other.age;
    }
};

namespace std {
    template <>
    struct hash<Person> {
        std::size_t operator()(const Person& p) const {
            return hash<std::string>()(p.name) ^ hash<int>()(p.age);
        }
    };
}
```

## 🧠 Tổng kết

- **Separate Chaining**: Phù hợp khi không biết trước số lượng phần tử hoặc khi cần xử lý xóa phần tử thường xuyên.
- **Open Addressing**: Hiệu quả về bộ nhớ và tốc độ khi bảng băm có tải trọng thấp.
- **Hàm băm hiệu quả**: Giúp giảm thiểu va chạm và cải thiện hiệu suất của bảng băm.

Việc lựa chọn kỹ thuật xử lý va chạm và thiết kế hàm băm phù hợp tùy thuộc vào yêu cầu cụ thể của ứng dụng và đặc điểm của dữ liệu.