---
date: 2025-02-19
draft: false
status: Doing
title: Thuộc tính và phương thức trong Java
description: Khám phá cách định nghĩa và sử dụng thuộc tính, phương thức trong Java. Bài viết này hướng dẫn chi tiết từ cơ bản đến nâng cao, kèm theo các mẹo hữu ích dành cho lập trình viên Java!
author: PhDoanh
authorlink: https://github.com/PhDoanh
tags:
  - coding
  - java
  - oop
  - programming-method
aliases:
  - attributes methods
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
    src="images/attributes-methods.png"
    alt="Thuộc tính và phương thức trong Java" 
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

Java là một ngôn ngữ lập trình mạnh mẽ với mô hình **lập trình hướng đối tượng (OOP)**. Hai thành phần cốt lõi trong OOP là **thuộc tính** (attributes) và **phương thức** (methods) đóng vai trò quan trọng trong việc mô tả và điều khiển các đối tượng. Trong bài viết này, chúng ta sẽ cùng khám phá chi tiết về các thành phần này qua các phần dưới đây. 🚀

# 🏷️ Khái niệm thuộc tính

**Thuộc tính** là các biến được khai báo bên trong một lớp, dùng để lưu trữ trạng thái của đối tượng.  Chúng giúp lưu giữ thông tin đặc trưng của đối tượng như tên, tuổi, địa chỉ, ... Thông thường, các thuộc tính được khai báo với mức truy cập `private` để **bảo vệ dữ liệu** khỏi truy cập trái phép.

```java {2,3}
public class Person {
	private String name;
	private int age;
}
```

> [!explain]- Giải thích code
> - **Dòng 2**: Thuộc tính kiểu văn bản lưu trữ tên của đối tượng thuộc lớp `Person`
> - **Dòng 3**: Thuộc tính kiểu số nguyên lưu trữ tuổi của đối tượng thuộc lớp `Person`

> [!info] Lưu ý
> - **Đóng gói dữ liệu:** Sử dụng từ khóa `private` để bảo vệ thuộc tính và sử dụng phương thức getter/setter để truy xuất.
> - **Tên biến rõ ràng:** Đặt tên thuộc tính sao cho phản ánh đúng nội dung dữ liệu.
> - **Khởi tạo hợp lệ:** Đảm bảo thuộc tính luôn được khởi tạo giá trị hợp lệ khi đối tượng được tạo ra. Ví dụ: kiểu `int` không thể nhận giá trị `"text"`

---

# ⚙️ Khái niệm phương thức

**Phương thức** là các hàm được khai báo trong lớp, định nghĩa các hành vi của đối tượng. Chúng dùng để thực hiện các thao tác, xử lý logic và tương tác với thuộc tính của đối tượng. Một phương thức bao gồm tên, danh sách tham số và phần thân chứa logic xử lý.

```java
public class Person {
	private String name;

	public void sayHello() {
	    System.out.println("Xin chào! Tôi là " + name);
	}
}
```

> [!explain]- Giải thích code
> **Dòng 4**: Định nghĩa phương thức công khai `sayHello` cho phép đối tượng truy cập để in ra dòng văn bản 

---

# 🗂️ Các loại phương thức

## Phương thức không trả về dữ liệu
Thực hiện hành động nhưng không trả về giá trị.

```java
public void displayInfo() {
	System.out.println("Đây là thông tin của đối tượng.");
}
```

> [!important]- Phương thức khởi tạo
> Được gọi tự động khi tạo đối tượng, có cùng tên với lớp và không có kiểu trả về. Vi dụ: lớp `Person` sẽ có hàm tạo là `public Person(các tham số) { logic khởi tạo }`

## Phương thức trả về dữ liệu
Thực hiện hành động và trả về một giá trị sau khi xử lý.

```java
public int getAge() {
	return age;
}
```

## Phương thức tĩnh (static)
Phương thức này cho phép gọi mà không cần khởi tạo đối tượng.

```java {2,6,13}
class MathUtils {
    public static int add(int a, int b) {
        return a + b;
    }

    public static void printMessage() {
        System.out.println("Welcome to MathUtils!");
    }
}

public class Main {
    public static void main(String[] args) {
        MathUtils.printMessage();
        int sum = MathUtils.add(5, 10);
        System.out.println("Tổng: " + sum);
    }
}
```

```txt title="Đầu ra"
Welcome to MathUtils!
Tổng: 15
```

> [!explain]- Giải thích code
> - **Dòng 2**: Định nghĩa phương thức `add` với từ khóa `static`, nghĩa là phương thức này thuộc về lớp, không phải đối tượng.
> - **Dòng 6**: Định nghĩa phương thức **tĩnh khác** tên `printMessage()` để in ra một thông điệp.
> - **Dòng 13**: Gọi phương thức `printMessage()` bằng tên lớp `MathUtils` mà không cần tạo đối tượng.

> [!info] Lưu ý
> - **Không cần tạo đối tượng để gọi**: Có thể truy cập phương thức tĩnh bằng `TênLớp.tênPhươngThức()`.  
> - Không thể truy cập biến non-static (biến mà không có từ khóa `static` )
> - **Được dùng nhiều trong các lớp tiện ích (utility class)** như `Math`, `Arrays`, `Collections` trong Java.

## Phương thức nạp chồng và ghi đè

- **Nạp chồng (Overloading):** Định nghĩa nhiều phương thức cùng tên nhưng khác tham số trong cùng một lớp.
- **Ghi đè (Overriding):** Cung cấp cài đặt mới cho phương thức được kế thừa từ lớp cha.

```java {8-9,12,15}
class Animal {
    public void sound() {
        System.out.println("Animal sound");
    }
}

class Dog extends Animal {
    @Override
    public void sound() {
        System.out.println("Dog barks");
    }

    public void play() {
        System.out.println("Dog plays");
    }

    public void play(String toy) {
        System.out.println("Dog plays with " + toy);
    }
}

public class Main {
    public static void main(String[] args) {
        Animal animal = new Animal();
        animal.sound();

        Dog dog = new Dog();
        dog.sound();
        dog.play();
        dog.play("ball");
    }
}
```

```txt title="Đầu ra"
Animal sound
Dog barks
Dog plays
Dog plays with ball
```

> [!explain]- Giải thích code
> - **Dòng 8-9:** Sử dụng `@Override` để chỉ ra phương thức `sound()` trong `Dog` sẽ ghi đè phương thức cùng tên từ lớp cha.
> - **Dòng 12:** Khai báo phương thức `play()` không tham số trong lớp `Dog`, là một ví dụ của **nạp chồng** (overloading).
> - **Dòng 15:** Khai báo phương thức `play(String toy)` với tham số, tiếp tục minh họa cho **nạp chồng** (overloading) của phương thức `play` trong cùng một lớp.

> [!info] Lưu ý
> Khi một lớp (lớp con) kế thừa từ lớp khác (lớp cha), từ khóa `extends` được sử dụng để mở rộng lớp cha, tức là giữ nguyên cái sẵn có trong lớp cha và thêm cái mới của lớp con
> Các lớp vẫn tự hiểu phương thức nạp chồng mà không cần `@Override` nhưng khuyến khích sử dụng vì khi sai tên phương thức hoặc kiểu tham số, Java sẽ không báo lỗi và coi đó là phương thức mới, cộng thêm việc báo lỗi ghi đè nếu phương thức cha có từ khóa `final`, `static` hay `private` (không thể bị ghi đè)

> [!question]- Bạn có biết?
> Ngoài các phương thức trên, còn có **Phương thức trừu tượng (Abstract Method)** được khai báo trong lớp trừu tượng (`abstract`), không có phần thân mà bắt buộc các lớp con phải triển khai.

---

# 📦 Đảm tính đóng gói bằng Getter và Setter

Để **bảo vệ dữ liệu** của đối tượng, thuộc tính thường được khai báo `private`. Các **getter** và **setter** cho phép truy xuất và cập nhật dữ liệu một cách kiểm soát:

- **Getter:** Phương thức trả về giá trị của thuộc tính.
- **Setter:** Phương thức cập nhật giá trị cho thuộc tính với các kiểm tra cần thiết.

```java {4,8}
public class Person {
    private String name;
    
    public String getName() {
        return name;
    }
    
    public void setName(String name) {
        // Có thể kiểm tra tính hợp lệ cho tên trước khi thiết lập
        this.name = name;
    }
}
```

---

# 🔥 Một số mẹo nâng cao

- **Kết hợp biểu thức Lambda:** Trong Java 8 trở lên, bạn có thể sử dụng lambda để đơn giản hóa một số phương thức, đặc biệt trong xử lý sự kiện.

- **Sử dụng `final`:** Đối với những thuộc tính không thay đổi, từ khóa `final` giúp đảm bảo giá trị không bị thay đổi sau khi khởi tạo (bản chất là hằng dữ liệu)
   
- **Tối ưu hóa hiệu năng:** Gọi phương thức tĩnh cho các thao tác không phụ thuộc vào trạng thái của đối tượng.

---

# 🎉 Tổng kết

- **Thuộc tính** là các biến lưu trữ trạng thái của đối tượng, trong khi **phương thức** định nghĩa hành vi và tương tác của đối tượng.
- **Đóng gói dữ liệu** với từ khóa `private` cùng với **getter/setter** giúp bảo vệ thông tin và tăng tính bảo trì.
- Java hỗ trợ nhiều **loại phương thức** như `static`, `void`, có trả về, nạp chồng và ghi đè, cho phép bạn thiết kế các hành vi linh hoạt.
- Các **mẹo nâng cao** như sử dụng biểu thức Lambda, `final` hay tối ưu hóa hiệu năng sẽ giúp mã nguồn của bạn trở nên chuyên nghiệp và hiệu quả hơn.

Hy vọng rằng bài viết này đã cung cấp cho bạn cái nhìn toàn diện về **thuộc tính** và **phương thức** trong Java. Hãy tiếp tục thực hành và khám phá thêm các tính năng của Java để phát triển kỹ năng lập trình của bạn nhé! 🚀😊
