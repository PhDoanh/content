---
date: 2025-02-24
draft: false
status: Doing
title: Tính đóng gói trong Java
description: "Khám phá tính đóng gói trong Java, giải thích cách áp dụng để bảo vệ dữ liệu và nâng cao tính bảo mật trong phát triển phần mềm. Tìm hiểu các nguyên tắc, ví dụ thực tế và mẹo hay cho lập trình viên."
author: PhDoanh
authorlink: https://github.com/PhDoanh
tags:
  - java
  - coding
  - oop
  - programming-method
aliases:
  - encapsulation
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
    src="images/encapsulation.png"
    alt="Tính đóng gói trong Java" 
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

Tính đóng gói là một trong những **trụ cột chính của lập trình hướng đối tượng (OOP)** trong `Java` 🛡️. Bài viết này sẽ giúp bạn hiểu rõ hơn về khái niệm đóng gói, các nguyên tắc áp dụng, ví dụ thực tế và cả những mẹo nhỏ để nâng cao chất lượng mã nguồn.

# Giới thiệu về tính đóng gói

Tính đóng gói đề cập đến việc **che giấu dữ liệu** bên trong một `class` và chỉ cho phép truy cập thông qua các phương thức được định nghĩa rõ ràng. Điều này giúp bảo vệ dữ liệu khỏi những thay đổi không mong muốn từ bên ngoài.

**Mục tiêu chính:**  
- Bảo vệ dữ liệu khỏi sự truy cập trực tiếp  
- Giảm thiểu lỗi khi thay đổi cấu trúc nội bộ của `class`  
- Tăng tính bảo mật và bảo trì của ứng dụng

# Nguyên tắc và lợi ích của tính đóng gói

## Định nghĩa tính đóng gói

Tính đóng gói là quá trình **ẩn dữ liệu nội bộ** của một `class` bằng cách sử dụng các truy cập `private` và cung cấp các phương thức truy cập (`getter`, `setter`) công khai (`public`).

**Lợi ích:**  
- **Kiểm soát truy cập:** Giới hạn truy cập trực tiếp đến dữ liệu.
- **Bảo vệ dữ liệu:** Ngăn ngừa thay đổi dữ liệu không hợp lệ.
- **Tăng tính bảo trì:** Cho phép thay đổi triển khai nội bộ mà không ảnh hưởng đến phần còn lại của ứng dụng.

## Lợi ích trong lập trình

Việc áp dụng tính đóng gói mang lại nhiều **lợi ích vượt trội** cho quá trình phát triển phần mềm:

- **Bảo mật:** Chỉ cho phép truy cập dữ liệu thông qua các phương thức được kiểm soát.
- **Giảm lỗi:** Giảm khả năng sai sót do thao tác trực tiếp lên biến.
- **Tính mở rộng:** Dễ dàng thay đổi và mở rộng `class` mà không ảnh hưởng đến code sử dụng nó.
- **Bảo trì:** Dễ dàng cập nhật và kiểm tra, từ đó nâng cao chất lượng sản phẩm.

# 🔎 Ví dụ minh họa
Dưới đây là một ví dụ về cách áp dụng tính đóng gói trong `Java`:

```java {2,3,5,9,13,17,21,26,27-28,34-35,37-39}
public class Person {
    private String name;
    private int age;
    
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
    
    public String getName() {
        return name;
    }
    
    public void setName(String name) {
        this.name = name;
    }
    
    public int getAge() {
        return age;
    }
    
    public void setAge(int age) {
        if(age >= 0) {
            this.age = age;
        } else {
            System.out.println("Invalid age!");
        }
    }
    
    public void display() {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
    }
}

public class Main {
    public static void main(String[] args) {
        Person person = new Person("Alice", 30);
        person.display();
        
        person.setAge(35);
        System.out.println("After update:");
        person.display();
    }
}
```

```txt title="Đầu ra"
Name: Alice
Age: 30
After update:
Name: Alice
Age: 35
```

> [!explain]- Giải thích code
> - **Dòng 2:** Khai báo biến `name` với phạm vi `private` để **ẩn dữ liệu**.
> - **Dòng 3:** Khai báo biến `age` với phạm vi `private` để bảo vệ dữ liệu khỏi truy cập trực tiếp.
> - **Dòng 5:** Tạo constructor cho class `Person` với tham số `name` và `age` để khởi tạo đối tượng.
> - **Dòng 9:** Định nghĩa phương thức `getName` cho phép truy cập an toàn vào biến `name` thông qua **getter**.
> - **Dòng 13:** Định nghĩa phương thức `setName` cho phép cập nhật giá trị của `name` qua **setter**.
> - **Dòng 17:** Định nghĩa phương thức `getAge` để truy cập giá trị của `age` một cách có kiểm soát.
> - **Dòng 21:** Định nghĩa phương thức `setAge` cho phép cập nhật `age` nhưng có kiểm tra tính hợp lệ trước khi gán giá trị.
> - **Dòng 26:** Định nghĩa phương thức `display` để in thông tin của đối tượng ra màn hình.
> - **Dòng 27-28:** Sử dụng `System.out.println` để hiển thị giá trị của `name` và `age`, minh họa **đóng gói** qua việc truy cập thông qua phương thức.
> - **Dòng 34:** Tạo đối tượng `Person` với tên `"Alice"` và tuổi `30` bằng constructor, áp dụng tính đóng gói để khởi tạo dữ liệu.
> - **Dòng 35:** Gọi phương thức `display` để in thông tin ban đầu của đối tượng.
> - **Dòng 37:** Gọi phương thức `setAge` để cập nhật tuổi thành `35`, đảm bảo thay đổi dữ liệu qua **setter** với kiểm tra hợp lệ.
> - **Dòng 38:** In ra thông báo `"After update:"` để phân biệt kết quả sau khi cập nhật.
> - **Dòng 39:** Gọi lại phương thức `display` để hiển thị thông tin cập nhật của đối tượng.

> [!info] Lưu ý
> - Sử dụng `private` để bảo vệ các biến dữ liệu quan trọng.
> - Sử dụng `public` cho các phương thức getter và setter để kiểm soát cách thức truy cập và thay đổi dữ liệu.

> [!advices]- Lời khuyên
> - Luôn kiểm tra giá trị đầu vào trong các phương thức `setter` để đảm bảo tính hợp lệ của dữ liệu.
> - Khi cần thay đổi logic nội bộ, chỉ cần thay đổi bên trong `class` mà không làm ảnh hưởng đến phần sử dụng bên ngoài.

> [!caution]- Cảnh báo
> - Tránh mở quá nhiều phương thức getter và setter không cần thiết, vì có thể làm mất đi mục đích **ẩn dữ liệu** của tính đóng gói.
> - Cân nhắc sử dụng các phương thức khác như `business methods` để thao tác dữ liệu thay vì chỉ dựa vào getter/setter.

# 🎉 Tổng kết

Tính đóng gói trong `Java` không chỉ là một nguyên tắc cơ bản của OOP mà còn là **yếu tố quan trọng giúp bảo vệ và duy trì chất lượng mã nguồn**. Qua bài viết, chúng ta đã:

- **Hiểu rõ khái niệm** và lợi ích của tính đóng gói.
- **Xem xét ví dụ thực tiễn** với một `class` đơn giản, minh họa cách sử dụng `private`, `getter` và `setter`.

Việc áp dụng tính đóng gói một cách hiệu quả không chỉ giúp bảo vệ dữ liệu mà còn **nâng cao tính bảo trì và mở rộng của ứng dụng**. Hãy luôn nhớ rằng, **đóng gói đúng cách** là nền tảng để xây dựng các ứng dụng mạnh mẽ và an toàn trong thế giới `Java` 🚀