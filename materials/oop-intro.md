---
date: 2025-02-18
draft: false
status: Doing
title: Khám phá lập trình hướng đối tượng (OOP) cho người mới bắt đầu
description: Bài viết giới thiệu khái niệm lập trình hướng đối tượng (OOP), giải thích các đặc tính chính như đóng gói, kế thừa, đa hình, trừu tượng. Đồng thời cung cấp ví dụ minh họa, ưu nhược điểm, và một số lưu ý khi áp dụng.
author: PhDoanh
authorlink: https://github.com/PhDoanh
tags:
  - oop
  - java
  - beginners
aliases:
  - oop intro
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
    src="images/oop-intro.png"
    alt="Khám phá lập trình hướng đối tượng (OOP) cho người mới bắt đầu" 
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

# 👀 Giới thiệu lập trình hướng đối tượng
Lập trình hướng đối tượng (Object-Oriented Programming – **OOP**) là một **phương pháp lập trình** dựa trên khái niệm về **đối tượng**, nơi mỗi đối tượng đại diện cho một thực thể có **thuộc tính** (properties) và **phương thức** (methods).

Lập trình hướng đối tượng dựa trên việc mô phỏng thế giới thực thông qua các **lớp** (class) và **đối tượng** (object). Mỗi **lớp** được xem như bản thiết kế, còn **đối tượng** là thực thể cụ thể được tạo ra từ lớp.

Lập trình hướng đối tượng (OOP) được sử dụng rộng rãi trong nhiều lĩnh vực công nghệ, đặc biệt là:

1. **Phát triển phần mềm doanh nghiệp 🏢**
	- Dùng trong các hệ thống quản lý nhân sự, kế toán, quản lý kho hàng...
	- Ví dụ: Hệ thống ERP (Enterprise Resource Planning).

2. **Phát triển ứng dụng di động 📱**   
    - Các nền tảng như Android và iOS sử dụng OOP để phát triển ứng dụng.
    - Ví dụ: Ứng dụng thương mại điện tử, ứng dụng ngân hàng số.

3. **Lập trình game 🎮**   
    - Mô hình hóa các đối tượng trong game như nhân vật, vũ khí, bản đồ bằng các class.
    - Ví dụ: Unity và Unreal Engine sử dụng OOP.

4. **Trí tuệ nhân tạo (AI) 🤖**
    - OOP giúp tổ chức dữ liệu và thuật toán một cách có cấu trúc trong các dự án AI.
    - Ví dụ: Thư viện TensorFlow (Python), OpenCV.

5. **Hệ thống điều khiển nhúng và IoT 🌐**    
    - Giúp phát triển phần mềm cho các thiết bị thông minh (smart home, xe tự hành).
    - Ví dụ: Phần mềm điều khiển robot, hệ thống cảm biến thông minh.

> [!check] Ưu điểm
> - **Tái sử dụng mã nguồn** ♻️: **Kế thừa (Inheritance)** giúp sử dụng lại mã nguồn mà không cần viết lại từ đầu.
> - **Bảo mật tốt hơn** 🔐: **Đóng gói (Encapsulation)** giúp ẩn thông tin quan trọng, ngăn chặn truy cập trái phép.
> - **Dễ bảo trì và mở rộng** 🔧: Các lớp và đối tượng có thể được thay đổi mà không ảnh hưởng đến toàn bộ hệ thống.
> - **Mô hình hóa thực tế dễ dàng** 🎭: Các đối tượng trong lập trình tương tự như các thực thể ngoài đời thực.
> - **Hỗ trợ đa hình (Polymorphism)** 🌀: Cùng một phương thức có thể hoạt động theo nhiều cách khác nhau.

> [!missing] Nhược điểm
> - **Hiệu suất chậm hơn so với lập trình thủ tục** 🐢: Do sử dụng nhiều bộ nhớ hơn và có cơ chế gọi phương thức ảo (Virtual Method).
> - **Mất nhiều thời gian thiết kế ban đầu** ⏳: Cần phân tích kỹ để xây dựng hệ thống lớp và đối tượng phù hợp.
> - **Không phù hợp với các ứng dụng nhỏ** 📏: Đối với chương trình đơn giản, OOP có thể khiến code trở nên cồng kềnh không cần thiết.
> - **Đòi hỏi lập trình viên có tư duy tổ chức tốt** 🧠: Nếu không có kinh nghiệm, dễ dẫn đến thiết kế hệ thống OOP phức tạp, khó bảo trì.

# 🔡 Các thuật ngữ cơ bản
- **Lớp (Class):** Bản thiết kế mô tả thuộc tính và hành vi của đối tượng.  
- **Đối tượng (Object):** Thực thể cụ thể được khởi tạo từ lớp.  
- **Thuộc tính (Property/Attribute):** Biến (hoặc trường dữ liệu) lưu trữ thông tin của đối tượng.  
- **Phương thức (Method):** Hàm (hoặc thủ tục) thể hiện hành vi của đối tượng.
- **Message Passing**: cơ chế gửi thông điệp giữa các đối tượng để yêu cầu thực hiện một hành động.
- **Dynamic Binding**: cơ chế xác định phương thức sẽ được gọi tại thời điểm thực thi, dựa trên kiểu thực tế của đối tượng.

> [!info] Lưu ý
> - Trong một số ngôn ngữ, **class** có thể được khai báo với các **access modifier** như `public`, `private`, `protected` để kiểm soát phạm vi truy cập.
> - **Message Passing** và **Dynamic Binding** là các cơ chế giúp hỗ trợ thực hiện các đặc tính cơ bản của OOP như **đa hình** và **trừu tượng**

# 🌟 Các tính chất quan trọng
Dưới đây là bốn đặc tính chính của OOP giúp bạn khai thác tối đa sức mạnh của phương pháp này.

## Tính đóng gói (Encapsulation) 📦
**Đóng gói** là cơ chế **gom nhóm** các thuộc tính và phương thức vào cùng một lớp, đồng thời **ẩn** các chi tiết bên trong. Giúp **bảo vệ** dữ liệu và **giảm thiểu** phụ thuộc giữa các phần của chương trình.  

> [!example]- Ví dụ thực tế
> Khi bạn lái **một chiếc xe**, bạn chỉ cần **nhấn ga để tăng tốc, nhấn phanh để dừng lại**. Bạn **không cần biết** cách động cơ hoạt động bên trong như thế nào.
> 
> **Giải thích:**
> - Hệ thống động cơ, hộp số, hệ thống phanh được **đóng gói** bên trong xe và bạn không thể tự ý thay đổi nó.
> - Bạn chỉ có thể tương tác với nó thông qua các **giao diện bên ngoài** như **bàn đạp ga, phanh, vô lăng**.
> - Điều này giúp tránh hư hỏng và đảm bảo **tính an toàn**.

## Tính kế thừa (Inheritance) 🧬
**Kế thừa** cho phép một lớp **mở rộng** (hoặc **thừa kế**) từ lớp khác, dùng lại các thuộc tính và phương thức sẵn có. Tái sử dụng mã nguồn, **giảm trùng lặp** và dễ bảo trì.  
> [!example]- Ví dụ thực tế
> Con cái **thừa hưởng** đặc điểm từ cha mẹ, như **màu tóc, chiều cao, nhóm máu**,... nhưng cũng có thể **có thêm những đặc điểm riêng**.
> 
> **Giải thích:**
> - Một **đứa trẻ sinh ra** có **mắt của mẹ, chiều cao của cha** – đây là **kế thừa** đặc điểm di truyền.
> - Tuy nhiên, **đứa trẻ cũng có thể phát triển những tính cách riêng biệt** như thích hội họa hoặc giỏi toán.

## Tính đa hình (Polymorphism) 🎭
**Đa hình** cho phép một hành động có thể được thực hiện theo **nhiều cách khác nhau**, tùy thuộc vào đối tượng gọi hành động. Giúp **linh hoạt** trong việc xử lý hành vi của các đối tượng cùng kiểu.  

> [!example]- Ví dụ thực tế
> Một họa sĩ có thể **vẽ tranh bằng nhiều cách khác nhau**:
> - **Bằng bút chì** ✏️ – tranh phác thảo.
> - **Bằng sơn dầu** 🎨 – tranh nghệ thuật.
> - **Bằng kỹ thuật số** 💻 – tranh điện tử.
> 
> **Giải thích:**
> - Mặc dù hành động **"vẽ tranh"** là giống nhau, nhưng **cách thực hiện lại khác nhau** tùy vào công cụ mà họ sử dụng.
> - Tương tự, trong OOP, **một phương thức có thể hoạt động khác nhau tùy vào từng đối tượng cụ thể**.

## Tính trừu tượng (Abstraction) 🕶
**Trừu tượng** là việc **ẩn** các chi tiết phức tạp và **chỉ hiển thị** những thông tin cần thiết. Giảm độ phức tạp, tập trung vào **bản chất** vấn đề.  

> [!example]- Ví dụ thực tế
> Khi bạn sử dụng **máy ATM**, bạn chỉ cần:  Nhập **thẻ và mã PIN**, Chọn **số tiền cần rút** rồi Nhận tiền và kết thúc giao dịch
> 
> **Giải thích:**
> - Bạn **không cần biết** bên trong ATM hoạt động thế nào, hệ thống ngân hàng xử lý giao dịch ra sao.
> - Những chi tiết phức tạp **được ẩn đi**, chỉ cung cấp cho bạn **giao diện đơn giản** để sử dụng.

# 🔎 Ví dụ minh họa
Dưới đây là ví dụ về cách OOP hoạt động trong ngôn ngữ Java:

```java {1,17,35,55-56,58-59,63-64}
abstract class Vehicle {  
    protected String brand;   
    protected int speed;
    
    public Vehicle(String brand, int speed) {
        this.brand = brand;
        this.speed = speed;
    }
    
    public void showInfo() {
        System.out.println("Brand: " + brand + ", Speed: " + speed + " km/h");
    }
    
    public abstract void honk(); 
}

class Car extends Vehicle {
    private int numDoors;
    
    public Car(String brand, int speed, int numDoors) {
        super(brand, speed);
        this.numDoors = numDoors;
    }
    
    public void showInfo() {
        super.showInfo();
        System.out.println("Number of doors: " + numDoors);
    }
    
    public void honk() {
        System.out.println("Car honks: Beep beep!");
    }
}

class Motorcycle extends Vehicle {
    private boolean hasSideCar;
    
    public Motorcycle(String brand, int speed, boolean hasSideCar) {
        super(brand, speed);
        this.hasSideCar = hasSideCar;
    }
    
    public void showInfo() {
        super.showInfo();
        System.out.println("Has sidecar: " + (hasSideCar ? "Yes" : "No"));
    }
    
    public void honk() {
        System.out.println("Motorcycle honks: Peep peep!");
    }
}

public class Main {
    public static void main(String[] args) {
        Vehicle car = new Car("Toyota", 180, 4);
        Vehicle motorcycle = new Motorcycle("Yamaha", 120, false);
        
        car.showInfo();
        car.honk();
        
        System.out.println();
        
        motorcycle.showInfo();
        motorcycle.honk();
    }
}
```

```txt title="Đầu ra"
Brand: Toyota, Speed: 180 km/h
Number of doors: 4
Car honks: Beep beep!

Brand: Yamaha, Speed: 120 km/h
Has sidecar: No
Motorcycle honks: Peep peep!
```

> [!explain]- Giải thích code
> - **Dòng 1:** Định nghĩa lớp **trừu tượng (Abstraction)** tên `Vehicle` và **đóng gói (Encapsulation)** các thuộc tính, phương thức dùng làm khuôn mẫu để triển khai các lớp con.
> - **Dòng 17:** Lớp `Car` **kế thừa (Inheritance)** từ `Vehicle` và mở rộng thêm thuộc tính `numDoors`.
> - **Dòng 35:** Lớp `Motorcycle` kế thừa từ `Vehicle` và mở rộng thêm thuộc tính `hasSideCar`.
> - **Dòng 55-56:** Khởi tạo đối tượng `Car` và `Motorcycle` từ lớp `Vehicle` 
> - **Dòng 58-59, 63-64:** gọi phương thức `showInfo()` và `honk()` của từng đối tượng (**Đa hình - Polymorphism**).

# 🔥 Tổng kết
Lập trình hướng đối tượng là một **phương pháp mạnh mẽ** và **linh hoạt** trong việc xây dựng các hệ thống phần mềm hiện đại. Bằng cách **đóng gói** dữ liệu, **kế thừa** từ lớp cha, **đa hình** hành vi và **trừu tượng** chi tiết thừa, OOP giúp mã nguồn dễ **hiểu**, **bảo trì** và **mở rộng**.

> [!tip]- Mẹo
> Khi bắt đầu học OOP, hãy tập trung vào việc **nhận diện các đối tượng** trong bài toán và **xác định thuộc tính, hành vi** của chúng.
