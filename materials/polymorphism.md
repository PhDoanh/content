---
date: 2025-02-24
draft: false
status: Doing
title: Tính đa hình trong Java
description: Bài viết này giải thích chi tiết về tính đa hình trong Java, bao gồm các ví dụ thực tế, mẹo hay và lưu ý quan trọng. Hãy cùng khám phá cách ứng dụng đa hình để tối ưu hóa thiết kế phần mềm của bạn!
author: PhDoanh
authorlink: https://github.com/PhDoanh
tags:
  - coding
  - java
  - oop
  - programming-method
aliases:
  - polymorphism
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
    src="images/polymorphism.png"
    alt="Tính đa hình trong Java" 
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

Tính đa hình là một trong những **khái niệm cốt lõi** của lập trình hướng đối tượng trong **Java**. Nó cho phép các đối tượng có thể thể hiện nhiều hình thái khác nhau, giúp mã nguồn trở nên linh hoạt, dễ bảo trì và mở rộng. Trong bài viết này, chúng ta sẽ đi sâu vào từng khía cạnh của tính đa hình, kèm theo **ví dụ minh họa**, lưu ý và mẹo hữu ích.

# Giới thiệu về tính đa hình

Tính đa hình (Polymorphism) cho phép một đối tượng có thể được sử dụng bằng nhiều kiểu dữ liệu khác nhau. Điều này giúp cho việc viết code trở nên **linh hoạt** và **tái sử dụng** được nhiều hơn. 💡  

> [!check] Ưu điểm
> - **Tăng tính linh hoạt:** Cho phép xử lý các đối tượng theo cách tổng quát mà không cần quan tâm đến kiểu dữ liệu cụ thể.
> - **Dễ bảo trì và mở rộng:** Khi cần thay đổi hành vi, chỉ cần cập nhật trong lớp con mà không ảnh hưởng đến cấu trúc lớp cha.
> - **Giảm thiểu mã lặp:** Tận dụng tính kế thừa và ghi đè phương thức để tránh việc viết lại code.

> [!missing] Nhược điểm
> - **Khó kiểm soát lỗi:** Nếu không hiểu rõ mối quan hệ giữa các lớp, việc sử dụng đa hình có thể dẫn đến lỗi khó phát hiện.
> - **Hiệu năng:** Trong một số trường hợp, việc sử dụng đa hình có thể ảnh hưởng nhỏ đến hiệu năng do quá trình xác định phương thức tại thời điểm chạy.

> [!info]- Lưu ý
> - Khi sử dụng tính đa hình, hãy đảm bảo rằng bạn hiểu rõ mối quan hệ giữa các lớp và cách **override** hay **overload** phương thức.
> - **Sử dụng đúng lúc:** Đa hình rất hữu ích khi xử lý các hành vi chung của nhiều đối tượng, nhưng không nên lạm dụng khi chỉ cần các thao tác đơn giản.
> - **Kiểm tra kiểu dữ liệu:** Sử dụng các từ khóa như **instanceof** và ép kiểu (casting) một cách cẩn thận để tránh lỗi thời gian chạy.
> - **Tài liệu tham khảo:** Bạn có thể tìm hiểu thêm về **[đa hình trong Java](https://docs.oracle.com/javase/tutorial/java/IandI/polymorphism.html)** trên trang chính thức của Oracle.

# Các loại đa hình trong Java

## Đa hình tại thời điểm biên dịch

Đa hình tại thời điểm biên dịch, hay còn gọi là **method overloading**, cho phép định nghĩa nhiều phương thức cùng tên nhưng khác nhau về số lượng hoặc kiểu tham số. Điều này giúp cải thiện tính rõ ràng và khả năng tái sử dụng của code.  

```java {2,6,11-13}
public class OverloadingDemo {
    public int sum(int a, int b) {
        return a + b;
    }
    
    public int sum(int a, int b, int c) {
        return a + b + c;
    }
    
    public static void main(String[] args) {
        OverloadingDemo demo = new OverloadingDemo();
        int result1 = demo.sum(10, 20);
        int result2 = demo.sum(5, 15, 25);
        System.out.println("Kết quả của sum(10, 20) là: " + result1);
        System.out.println("Kết quả của sum(5, 15, 25) là: " + result2);
    }
}
```

```txt title="Đầu ra"
Kết quả của sum(10, 20) là: 30
Kết quả của sum(5, 15, 25) là: 45
```

> [!explain]- Giải thích code
> - **Dòng 2:** Định nghĩa phương thức **sum** nhận 2 tham số kiểu int, minh họa **method overloading** với số lượng tham số khác nhau.
> - **Dòng 6:** Định nghĩa một phiên bản khác của phương thức **sum** nhận 3 tham số kiểu int, thể hiện thêm tính đa hình tại thời điểm biên dịch.
> - **Dòng 11:** Tạo đối tượng **demo** của lớp **OverloadingDemo** để gọi các phương thức đã định nghĩa.
> - **Dòng 12:** Gọi phương thức **sum** với 2 đối số; phiên bản này được chọn dựa trên số lượng tham số, minh họa tính đa hình tại thời điểm biên dịch.
> - **Dòng 13:** Gọi phương thức **sum** với 3 đối số; phiên bản này được chọn tương ứng với số lượng tham số được truyền vào.

> [!tip]- Mẹo
> Khi viết method overloading, nên đặt tên phương thức sao cho dễ hiểu và phản ánh chức năng chính của nó. 🔍

## Đa hình tại thời điểm chạy

Đa hình tại thời điểm chạy, hay còn gọi là **method overriding**, xảy ra khi một lớp con định nghĩa lại phương thức của lớp cha để thực hiện hành vi riêng. Điều này giúp cho chương trình có thể quyết định cách thực thi cụ thể tại thời điểm chạy dựa trên đối tượng thực tế.  

```java {7-12,14-19,23-24,26-27}
class Animal {
    public void sound() {
        System.out.println("Animal makes a sound");
    }
}

class Dog extends Animal {
    @Override
    public void sound() {
        System.out.println("Dog barks");
    }
}

class Cat extends Animal {
    @Override
    public void sound() {
        System.out.println("Cat meows");
    }
}

public class Main {
    public static void main(String[] args) {
        Animal animal1 = new Dog();
        Animal animal2 = new Cat();
        
        animal1.sound();
        animal2.sound();
    }
}
```

```txt title="Đầu ra"
Dog barks
Cat meows
```

> [!explain]- Giải thích code
> - **Dòng 7-12:** Tạo lớp con kế thừa, ghi đè phương thức của lớp cha để cung cấp hành vi cụ thể cho đối tượng thuộc lớp này.
> - **Dòng 14-19:** Tương tự như trên, lớp con khác cũng ghi đè phương thức của lớp cha để minh họa hành vi khác biệt.
> - **Dòng 23-24:** Trong hàm chính, khởi tạo các đối tượng kiểu lớp cha nhưng thực chất là các đối tượng của lớp con; khi gọi phương thức, hệ thống quyết định thực thi phiên bản của lớp con tương ứng, thể hiện tính đa hình tại thời điểm chạy.
> - **Dòng 26-27:** Khi gọi phương thức `sound()`, đối tượng sẽ tự động chọn phiên bản ghi đè phù hợp dựa trên kiểu đối tượng thực tế, cho phép chương trình linh hoạt và mở rộng.

> [!info] Lưu ý
> Khi sử dụng method overriding, hãy luôn chú ý đến từ khóa `@Override` để tránh nhầm lẫn và lỗi khi biên dịch.

# Các khái niệm nâng cao liên quan đến đa hình

## Casting và `instanceof`

Trong quá trình sử dụng tính đa hình, việc ép kiểu (casting) và kiểm tra kiểu dữ liệu bằng **instanceof** là rất quan trọng.

```java {21-22,24-25,29-30}
class Animal {
    public void makeSound() {
        System.out.println("Animal makes a sound");
    }
}

class Dog extends Animal {
    public void bark() {
        System.out.println("Woof! Woof!");
    }
}

class Cat extends Animal {
    public void meow() {
        System.out.println("Meow! Meow!");
    }
}

public class TestPolymorphism {
    public static void main(String[] args) {
        Animal animal1 = new Dog();
        Animal animal2 = new Cat();
        
        if(animal1 instanceof Dog) {
            Dog dog = (Dog) animal1;
            dog.bark();
        }
        
        if(animal2 instanceof Cat) {
            Cat cat = (Cat) animal2;
            cat.meow();
        }
    }
}
```

```txt title="Đầu ra"
Woof! Woof!
Meow! Meow!
```

> [!explain]- Giải thích code
> - **Dòng 21:** Tạo đối tượng với kiểu tham chiếu là lớp cha nhưng thực thể là của lớp con (Dog), thể hiện tính đa hình trong Java.
> - **Dòng 22:** Tương tự, tạo đối tượng với kiểu tham chiếu lớp cha nhưng thực thể là của lớp con (Cat).
> - **Dòng 24:** Sử dụng `instanceof` để kiểm tra xem đối tượng có thuộc kiểu của lớp con Dog hay không.
> - **Dòng 25:** Nếu kết quả kiểm tra đúng, thực hiện ép kiểu đối tượng sang kiểu Dog để có thể gọi được các phương thức đặc trưng của lớp này.
> - **Dòng 29:** Sử dụng `instanceof` để kiểm tra xem đối tượng có thuộc kiểu của lớp con Cat hay không.
> - **Dòng 30:** Nếu kết quả kiểm tra đúng, ép kiểu đối tượng sang kiểu Cat để có thể gọi được phương thức riêng của lớp Cat.

> [!info] Lưu ý
> Ép kiểu không đúng có thể dẫn đến lỗi **ClassCastException**.

## Thiết kế hướng đối tượng và tính đa hình

Tính đa hình là một phần không thể thiếu trong **thiết kế hướng đối tượng**. Nó giúp bạn tạo ra các lớp có tính mở rộng cao và dễ dàng bảo trì.  

> [!tip]- Mẹo
> Áp dụng nguyên tắc **"lập trình với giao diện, không phải với triển khai"** để tận dụng tối đa lợi ích của đa hình.

# Ví dụ minh họa

Giả sử bạn đang phát triển một ứng dụng quản lý các phương tiện giao thông trong Garage. Bạn có thể định nghĩa một lớp cha `Vehicle` và các lớp con như `Car`, `Motorcycle`... sử dụng đa hình để xử lý các hành vi chung như `start()`.  

```java {}
class Vehicle {
    void start() {
        System.out.println("Phương tiện đang khởi động");
    }
}

class Car extends Vehicle {
    @Override
    void start() {
        System.out.println("Ô tô đang khởi động");
    }
}

class Motorcycle extends Vehicle {
    @Override
    void start() {
        System.out.println("Xe máy đang khởi động");
    }
}

class Garage {
    void park(Vehicle v) {
        System.out.println("Đỗ một phương tiện");
    }

    void park(Car c) {
        System.out.println("Đỗ một ô tô");
    }

    void park(Motorcycle m) {
        System.out.println("Đỗ một xe máy");
    }
}

public class Main {
    public static void main(String[] args) {
        Vehicle myVehicle = new Vehicle();
        Vehicle myCar = new Car();
        Vehicle myMotorcycle = new Motorcycle();

        myVehicle.start();
        myCar.start();
        myMotorcycle.start();

        Garage garage = new Garage();
        garage.park(myVehicle);
        garage.park(myCar);
        garage.park(myMotorcycle);

        if (myCar instanceof Car) {
            Car specificCar = (Car) myCar;
            System.out.println("Ép kiểu thành công từ Vehicle sang Car");
        }

        if (myMotorcycle instanceof Motorcycle) {
            Motorcycle specificMotorcycle = (Motorcycle) myMotorcycle;
            System.out.println("Ép kiểu thành công từ Vehicle sang Motorcycle");
        }
    }
}
```

```txt title="Đầu ra"
Phương tiện đang khởi động
Ô tô đang khởi động
Xe máy đang khởi động
Đỗ một phương tiện
Đỗ một ô tô
Đỗ một xe máy
Ép kiểu thành công từ Vehicle sang Car
Ép kiểu thành công từ Vehicle sang Motorcycle
```

> [!explain]- Giải thích code
> - **Dòng 9:** Định nghĩa lớp `Car` kế thừa `Vehicle` và ghi đè phương thức `start()`.
> - **Dòng 16:** Định nghĩa lớp `Motorcycle` kế thừa `Vehicle` và ghi đè phương thức `start()`.
> - **Dòng 21:** Định nghĩa lớp `Garage` với các phương thức `park()` nạp chồng cho các loại phương tiện khác nhau.
> - **Dòng 37-39:** Tạo các đối tượng `Vehicle`, `Car` và `Motorcycle`, tất cả đều được tham chiếu bởi biến kiểu `Vehicle`.
> - **Dòng 41-43:** Gọi phương thức `start()` trên các đối tượng; do tính đa hình, phương thức tương ứng của từng lớp được thực thi.
> - **Dòng 46-48:** Gọi phương thức `park()` với các tham số khác nhau; do nạp chồng, phương thức phù hợp được chọn dựa trên tham số.
> - **Dòng 50:** Sử dụng `instanceof` để kiểm tra xem `myCar` có phải là đối tượng của `Car` không.
> - **Dòng 51:** Nếu đúng, ép kiểu `myCar` từ `Vehicle` sang `Car`.

# 🎉 Tổng kết

Tính đa hình trong Java không chỉ là một **khái niệm lý thuyết** mà còn là công cụ mạnh mẽ trong thực tiễn phát triển phần mềm. Bằng cách sử dụng đa hình, bạn có thể:

- **Tối ưu hóa mã nguồn:** Giảm sự lặp lại và tăng tính tái sử dụng.
- **Tăng tính mở rộng:** Dễ dàng bổ sung các tính năng mới mà không ảnh hưởng đến cấu trúc hiện tại.
- **Cải thiện khả năng bảo trì:** Dễ dàng sửa lỗi và nâng cấp hệ thống khi cần thiết.

Hy vọng bài viết đã cung cấp cho bạn cái nhìn tổng quan cũng như **ví dụ cụ thể** về cách áp dụng tính đa hình trong Java. Hãy luôn **cẩn trọng** và **sáng tạo** khi thiết kế phần mềm để tận dụng tối đa các tính năng của lập trình hướng đối tượng. Happy coding! 😊