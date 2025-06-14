---
date: 2025-02-19
draft: false
status: Doing
title: Lớp và đối tượng trong Java
description: Bài viết này cung cấp cái nhìn toàn diện về lớp và đối tượng trong Java. Cùng khám phá khái niệm, cách khai báo, tạo đối tượng và các tính năng quan trọng của lập trình hướng đối tượng để nâng cao kỹ năng lập trình của bạn!
author: PhDoanh
authorlink: https://github.com/PhDoanh
tags:
  - coding
  - java
  - oop
  - programming-method
aliases:
  - class objects
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
    src="images/class-objects.png"
    alt="Lớp và đối tượng trong Java" 
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

Trong thế giới lập trình hiện đại, **lập trình hướng đối tượng** là một trong những phương pháp mạnh mẽ và phổ biến nhất. Java, một trong những ngôn ngữ lập trình hàng đầu, tận dụng triệt để khái niệm *lớp* và *đối tượng* để xây dựng các ứng dụng linh hoạt, bảo trì dễ dàng và mở rộng nhanh chóng 🚀.

Lớp và đối tượng là nền tảng của **lập trình hướng đối tượng (OOP)**. Bài viết dưới đây sẽ giúp bạn:
- Hiểu rõ **khái niệm cơ bản** về lớp và đối tượng.
- Tìm hiểu **cách khai báo và khởi tạo** chúng trong Java.
- Nắm bắt **các tính năng nâng cao** cùng với những **lưu ý quan trọng** khi thiết kế hệ thống.

# 🎓 Các khái niệm cơ bản

## Định nghĩa lớp

Trong Java, `class` là một **khuôn mẫu** hoặc **bản thiết kế** để tạo ra đối tượng. Một lớp có thể chứa:
- **Biến thành viên**: lưu trữ dữ liệu.
- **Phương thức**: định nghĩa hành động mà đối tượng có thể thực hiện.
- **Constructor**: phương thức khởi tạo đối tượng.

> [!info] Lưu ý
> Mỗi khi bạn định nghĩa một lớp, hãy đảm bảo rằng nó có mục đích rõ ràng và phản ánh đúng tính chất của đối tượng mà bạn muốn mô phỏng.

## Định nghĩa đối tượng

`Object` là **thực thể** được tạo ra từ lớp. Nó là sự hiện thân cụ thể của một lớp, chứa đầy đủ các giá trị của biến thành viên và có thể thực hiện các phương thức đã được định nghĩa.

**Đặc điểm nổi bật của đối tượng:**
- **Trạng thái:** Các giá trị của biến thành viên.
- **Hành vi:** Các phương thức mà đối tượng có thể gọi.

> [!tip]- Mẹo
> Khi làm việc với đối tượng, hãy sử dụng tính **đóng gói** để bảo vệ dữ liệu bên trong đối tượng khỏi sự truy cập trái phép.

---

# 📣 Cách khai báo lớp và tạo đối tượng

## Khai báo lớp

Để khai báo một lớp trong Java, bạn sử dụng từ khóa `class` theo cú pháp sau:

```java title="class-objects.java" {1,2,5,6,10}
public class Person {
    private String name;
    private int age;
    
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
    
    public void displayInfo() {
        System.out.println("Tên: " + name + ", Tuổi: " + age);
    }
}
```

> [!explain]- Giải thích code
> - **Dòng 1**: Khai báo một lớp `Person` với phạm vi truy cập `public` (cho phép truy cập từ bất kì đâu)
> - **Dòng 2**: Khai báo thuộc tính `name` kiểu văn bản với phạm vi truy cập `private` (chỉ cho phép truy cập từ bên trong lớp)
> - **Dòng 5**: Hàm tạo dùng để khởi tạo các thuộc tính của đối tượng.
> - **Dòng 6**: Tham chiếu đến biến thành viên của đối tượng (`this` = tên đối tượng)
> - **Dòng 10**: Định nghĩa phương thức công khai cho phép đối tượng gọi nó (từ bên ngoài lớp) để hiển thị thông tin của mình

## Tạo đối tượng
Sau khi khai báo lớp, bạn có thể tạo đối tượng từ lớp đó bằng từ khóa `new`:

``` java title="class-objects.java" showLineNumbers{14} {16,17}
public class Main {
    public static void main(String[] args) {
        Person person = new Person("An", 25);
        person.displayInfo();
    }
}
```

```txt title="Đầu ra"
Tên: An, Tuổi: 25
```

> [!explain]- Giải thích code
> Dòng 16: Tạo một đối tượng mới của lớp `Person` và khởi tạo các thuộc tính bằng hàm tạo của lớp đó
> Dòng 17: Truy cập phương thức `displayInfo` để hiển thị thông tin 

---

# 👀 Một số lưu ý khi thiết kế lớp và đối tượng

- **Đảm bảo tính nhất quán:** Các biến thành viên và phương thức nên có ý nghĩa rõ ràng.
- **Tối ưu hóa hiệu năng:** Sử dụng đúng mức các thành phần của lớp để tránh lãng phí bộ nhớ.
- **Quản lý lỗi:** Luôn kiểm tra và xử lý các trường hợp ngoại lệ trong constructor và phương thức.
- **Phân chia trách nhiệm:** Mỗi lớp nên đảm nhận một nhiệm vụ cụ thể, tuân theo nguyên tắc Single Responsibility Principle (SRP) 💡.
- **Bảo trì và mở rộng:** Việc thiết kế lớp hợp lý sẽ giúp cho việc bảo trì và mở rộng hệ thống trở nên dễ dàng hơn.

---

# 🔥 Tổng kết

Bài viết đã cung cấp cái nhìn tổng quan về **lớp và đối tượng trong Java**, từ định nghĩa đến cách khai báo và tạo đối tượng. Bạn đã nắm bắt được:

- **Khái niệm cơ bản:** Lớp như khuôn mẫu và đối tượng như thực thể cụ thể.
- **Cách triển khai:** Từ khai báo lớp đến tạo và sử dụng đối tượng.
- **Một số lưu ý quan trọng:** Đảm bảo tính nhất quán, quản lý lỗi và tối ưu hóa hiệu năng.

Hy vọng rằng với bài viết này, bạn đã có được **cái nhìn sâu sắc** và đầy đủ hơn về cách xây dựng các ứng dụng Java theo mô hình hướng đối tượng. Hãy tiếp tục thực hành và khám phá thêm các tính năng nâng cao của Java để trở thành một lập trình viên chuyên nghiệp hơn nhé! 😊
