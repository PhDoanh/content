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
  - programming paradigms
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
    src="images/programming-paradigms.png"
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

Dưới đây là sự khác biệt cốt lõi giữa **lập trình thủ tục (procedural)**, **lập trình hàm (functional)** và **lập trình hướng đối tượng (OOP)** – cực kỳ ngắn gọn, thẳng vào trọng tâm:

# **1. Lập trình thủ tục (Procedural Programming)**

> ✅ **Tư duy: Làm theo từng bước.**  
> 🛠 Dựa vào **các thủ tục (hàm)** để thao tác dữ liệu.  
> 📦 Dữ liệu và hàm **tách biệt**.

- Kiểu như: "Làm cái này → rồi cái kia → rồi cái nọ"
    
- Ví dụ: C, Pascal
    
- **Không có "object" hay "class"** gì cả.
    

---

# **2. Lập trình hàm (Functional Programming)**

> ✅ **Tư duy: Biến đổi dữ liệu qua các hàm bất biến.**  
> 🔁 Không có trạng thái (stateless), tránh side-effect.  
> 🧩 Hàm là “công dân hạng nhất”: gán, truyền vào, trả về như biến.

- Kiểu như: Lắp ghép Lego – đầu vào → ra đầu ra → xâu chuỗi.
    
- Ví dụ: Haskell, Scala, Elixir, (hoặc kiểu functional trong JavaScript, Python)
    
- Ưu điểm: Dễ kiểm thử, code “sạch”.
    

---

# **3. Lập trình hướng đối tượng (OOP)**

> ✅ **Tư duy: Mô phỏng thế giới thực bằng đối tượng.**  
> 📦 Dữ liệu + hành vi gói trong **object**.  
> 🔁 Dựa trên **class**, **kế thừa**, **đa hình**, **đóng gói**.

- Kiểu như: "Tôi có class `Xe`, mỗi `Xe` có `chạy()` và `phanh()`"
    
- Ví dụ: Java, C++, Python, C#, Swift
    
- Tốt cho hệ thống lớn, dễ mở rộng.
    

---

# Tóm gọn:

| Tiêu chí             | Thủ tục (Procedural) | Hàm (Functional)          | Hướng đối tượng (OOP)  |
| -------------------- | -------------------- | ------------------------- | ---------------------- |
| Tổ chức chương trình | Theo bước/hàm        | Theo hàm thuần (pure)     | Theo class/object      |
| Trạng thái (state)   | Có                   | Tránh trạng thái          | Có                     |
| Cách quản lý dữ liệu | Biến toàn cục/cục bộ | Bất biến (immutable)      | Gói trong object       |
| Phù hợp với          | Bài toán đơn giản    | Xử lý song song, bất biến | Hệ thống lớn, phức tạp |

---

# Ý kiến cá nhân:
- Muốn **tối ưu performance và dễ hiểu nhanh**: Procedural.
- Muốn **viết code “sạch”, dễ test, dễ bảo trì**: Functional.
- Muốn **mô hình hóa hệ thống lớn, phức tạp**: OOP là vua.
Nếu bạn làm IoT phần mềm:  
→ **Firmware nhỏ gọn?** Procedural.  
→ **Xử lý tín hiệu/stream?** Functional.  
→ **Giao tiếp, quản lý thiết bị phức tạp?** OOP.

Cần triển khai gì cụ thể thì nói, mình gợi ý lối tiếp cận nhanh.

## 🧩 Lập trình Thủ tục (Procedural Programming)

- **Cách tiếp cận**: Xây dựng chương trình như một chuỗi các lệnh thực thi tuần tự.
    
- **Đặc điểm**:
    
    - Tập trung vào các hàm (methods) và quy trình xử lý.
        
    - Dữ liệu được lưu trữ trong biến toàn cục hoặc được truyền qua các hàm.
        
    - Dễ hiểu và triển khai cho các chương trình nhỏ hoặc đơn giản.
        

**Ví dụ: Hoán đổi giá trị hai biến**

```java
int a = 10;
int b = 15;

int temp = b;
b = a;
a = temp;
```

---

## 🧱 Lập trình Hướng Đối tượng (Object-Oriented Programming - OOP)

- **Cách tiếp cận**: Mô hình hóa chương trình bằng cách sử dụng các đối tượng (objects) và lớp (classes).
    
- **Đặc điểm**:
    
    - Dữ liệu và hành vi được đóng gói trong các đối tượng.
        
    - Hỗ trợ kế thừa, đa hình và đóng gói, giúp tái sử dụng mã và mở rộng dễ dàng.
        
    - Phù hợp với các ứng dụng lớn và phức tạp.
        

**Ví dụ: Mô hình đồng hồ**

```java
public class Clock {
    private int hours;
    private int minutes;
    private int seconds;

    public void tick() {
        seconds++;
        if (seconds > 59) {
            seconds = 0;
            minutes++;
            if (minutes > 59) {
                minutes = 0;
                hours++;
                if (hours > 23) {
                    hours = 0;
                }
            }
        }
    }

    public void printTime() {
        System.out.printf("%02d:%02d:%02d\n", hours, minutes, seconds);
    }
}
```

---

## 🧠 Lập trình Hàm (Functional Programming)

- **Cách tiếp cận**: Xây dựng chương trình bằng cách sử dụng các hàm thuần (pure functions) và tránh thay đổi trạng thái (immutability).
    
- **Đặc điểm**:
    
    - Hàm là công dân hạng nhất (first-class citizens): có thể được truyền như tham số, trả về từ hàm khác, hoặc gán cho biến.
        
    - Tránh tác dụng phụ (side effects) và trạng thái thay đổi.
        
    - Ưu tiên sử dụng các cấu trúc dữ liệu bất biến và đệ quy.
        

**Ví dụ: Sử dụng biểu thức lambda và Stream API**

```java
import java.util.Arrays;
import java.util.List;

public class FunctionalExample {
    public static void main(String[] args) {
        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);

        // Tính tổng các số chẵn
        int sum = numbers.stream()
                         .filter(n -> n % 2 == 0)
                         .mapToInt(Integer::intValue)
                         .sum();

        System.out.println("Tổng các số chẵn: " + sum);
    }
}
```

---

## 🚀 Hỗ trợ Lập trình Hàm trong Java

Java bắt đầu hỗ trợ các khái niệm lập trình hàm từ phiên bản Java 8, bao gồm:

- **Biểu thức lambda**: Cho phép viết các hàm ẩn danh ngắn gọn.
    
- **Functional interfaces**: Giao diện với một phương thức trừu tượng duy nhất (ví dụ: `Function`, `Predicate`, `Consumer`).
    
- **Stream API**: Cung cấp một cách tiếp cận khai báo để xử lý tập hợp dữ liệu.
    
- **Phương thức tham chiếu (method references)**: Cách viết ngắn gọn để tham chiếu đến phương thức.
    
- **Optional**: Lớp giúp xử lý giá trị có thể null một cách an toàn.
    

**Ví dụ: Sử dụng biểu thức lambda và phương thức tham chiếu**

```java
import java.util.Arrays;
import java.util.List;

public class LambdaExample {
    public static void main(String[] args) {
        List<String> names = Arrays.asList("An", "Bình", "Cường");

        // In ra tên viết hoa
        names.stream()
             .map(String::toUpperCase)
             .forEach(System.out::println);
    }
}
```

---

## 🔍 So sánh Nhanh

| Tiêu chí             | Thủ tục          | Hướng Đối tượng    | Hàm (Functional)         |
| -------------------- | ---------------- | ------------------ | ------------------------ |
| Tổ chức chương trình | Dựa trên hàm     | Dựa trên đối tượng | Dựa trên hàm thuần       |
| Quản lý dữ liệu      | Biến toàn cục    | Dữ liệu đóng gói   | Dữ liệu bất biến         |
| Tái sử dụng mã       | Hạn chế          | Cao                | Cao                      |
| Phù hợp với          | Chương trình nhỏ | Ứng dụng lớn       | Xử lý dữ liệu, song song |

---

## ✅ Ghi nhớ
- **Thủ tục**: Tốt cho các tác vụ tuần tự và đơn giản.
- **Hướng Đối tượng**: Tốt cho việc mô hình hóa các hệ thống phức tạp và dễ bảo trì.
- **Hàm**: Tốt cho xử lý dữ liệu, lập trình song song và tránh tác dụng phụ.

