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
  - design pattern
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
    src="images/design-pattern.png"
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

# SOLID

### 1. **Single Responsibility Principle (SRP) – Nguyên tắc trách nhiệm đơn lẻ**

- **Định nghĩa**: Mỗi lớp chỉ nên có một lý do duy nhất để thay đổi, tức là chỉ đảm nhận một trách nhiệm cụ thể.

**Ví dụ**: Giống như một học sinh chỉ nên tập trung vào việc học, không nên kiêm nhiệm quá nhiều công việc như lau bảng hay phát tài liệu.

- **Lợi ích**: Giúp mã nguồn dễ bảo trì, dễ hiểu và dễ kiểm thử.
- **Ví dụ**:[Viblo+5200Lab+5Quochung.cyou+5](https://200lab.io/blog/solid-la-gi?srsltid=AfmBOopz5Nw46gdn24nXGhEgcdKqByLuGsCMoPeTOk8mOuZwpPz0SvTM&utm_source=chatgpt.com)[Quochung.cyou+1stanford.com.vn+1](https://quochung.cyou/tim-hieu-solid-5-nguyen-tac-thiet-ke-huong-doi-tuong-bang-java/?utm_source=chatgpt.com)

```java
class Order {
	void calculateTotal() { /* ... */ }
}

class InvoicePrinter {
	void printInvoice(Order order) { /* ... */ }
}
```

Ở đây, `Order` chỉ xử lý tính toán đơn hàng, còn `InvoicePrinter` đảm nhận việc in hóa đơn, tuân thủ SRP.[200Lab](https://200lab.io/blog/solid-la-gi?srsltid=AfmBOopz5Nw46gdn24nXGhEgcdKqByLuGsCMoPeTOk8mOuZwpPz0SvTM&utm_source=chatgpt.com)

---

### 2. **Open/Closed Principle (OCP) – Nguyên tắc mở/đóng**

- **Định nghĩa**: Lớp nên **mở** để mở rộng nhưng **đóng** để sửa đổi.

**Ví dụ**: Như việc thêm một môn học mới vào thời khóa biểu mà không làm thay đổi các môn học đã có.

- **Lợi ích**: Cho phép thêm tính năng mới mà không làm thay đổi mã nguồn hiện có, giảm rủi ro lỗi.
    
- **Ví dụ**:
    
```java
  interface Shape {
      double area();
  }

  class Circle implements Shape {
      public double area() { /* ... */ }
  }

  class Rectangle implements Shape {
      public double area() { /* ... */ }
  }
```

Thêm hình mới chỉ cần tạo lớp mới mà không sửa đổi các lớp hiện tại.[GP Coder](https://gpcoder.com/4200-cac-nguyen-ly-thiet-ke-huong-doi-tuong/?utm_source=chatgpt.com)

---

### 3. **Liskov Substitution Principle (LSP) – Nguyên tắc thay thế Liskov**

- **Định nghĩa**: Đối tượng của lớp con có thể thay thế cho lớp cha mà không làm thay đổi tính đúng đắn của chương trình.

**Ví dụ**: Giống như thay thế một chiếc bút bi bằng một chiếc bút chì, bạn vẫn có thể viết bình thường mà không gặp vấn đề gì.

- **Lợi ích**: Đảm bảo tính kế thừa đúng đắn và tránh lỗi khi sử dụng đa hình.
    
- **Ví dụ**:[Từ coder đến developer - Tôi đi code dạo+1GP Coder+1](https://toidicodedao.com/2015/03/24/solid-la-gi-ap-dung-cac-nguyen-ly-solid-de-tro-thanh-lap-trinh-vien-code-cung/?utm_source=chatgpt.com)
    

```java
  class Rectangle {
      void setWidth(int width) { /* ... */ }
      void setHeight(int height) { /* ... */ }
  }

  class Square extends Rectangle {
      void setWidth(int width) {
          super.setWidth(width);
          super.setHeight(width);
      }

      void setHeight(int height) {
          super.setWidth(height);
          super.setHeight(height);
      }
  }
```

`Square` không tuân thủ LSP vì thay đổi hành vi của `Rectangle`.[GP Coder](https://gpcoder.com/4200-cac-nguyen-ly-thiet-ke-huong-doi-tuong/?utm_source=chatgpt.com)

---

### 4. **Interface Segregation Principle (ISP) – Nguyên tắc phân tách giao diện**

- **Định nghĩa**: Không nên ép các lớp phụ thuộc vào những giao diện mà chúng không sử dụng.

**Ví dụ**: Như việc không yêu cầu một học sinh chỉ học môn Toán phải tham gia vào câu lạc bộ bóng đá.

- **Lợi ích**: Giảm sự phụ thuộc không cần thiết và tăng tính linh hoạt.
    
- **Ví dụ**:
    

```java
  interface Printer {
      void print();
  }

  interface Scanner {
      void scan();
  }

  class MultiFunctionPrinter implements Printer, Scanner {
      public void print() { /* ... */ }
      public void scan() { /* ... */ }
  }

  class SimplePrinter implements Printer {
      public void print() { /* ... */ }
  }
```

Tách giao diện giúp `SimplePrinter` không phải triển khai phương thức `scan()` không cần thiết.

---

### 5. **Dependency Inversion Principle (DIP) – Nguyên tắc đảo ngược phụ thuộc**

- **Định nghĩa**: Các mô-đun cấp cao không nên phụ thuộc vào mô-đun cấp thấp; cả hai nên phụ thuộc vào các trừu tượng.

**Ví dụ**: Giống như việc bạn có thể sử dụng nhiều loại bút khác nhau (bút bi, bút chì) để viết, miễn là chúng đều có thể viết được.

- **Lợi ích**: Tăng tính linh hoạt và dễ dàng thay thế các thành phần.
    
- **Ví dụ**:
```java
  interface MessageService {
      void sendMessage(String message);
  }

  class EmailService implements MessageService {
      public void sendMessage(String message) { /* ... */ }
  }

  class Notification {
      private MessageService service;

      public Notification(MessageService service) {
          this.service = service;
      }

      public void notify(String message) {
          service.sendMessage(message);
      }
  }
```

`Notification` phụ thuộc vào `MessageService` (trừu tượng), không phụ thuộc trực tiếp vào `EmailService` (cụ thể).

---

## 📌 Tổng kết

| Nguyên tắc | Mục tiêu chính                | Lợi ích                        |
| ---------- | ----------------------------- | ------------------------------ |
| SRP        | Một trách nhiệm duy nhất      | Dễ bảo trì, dễ hiểu            |
| OCP        | Mở rộng không sửa đổi         | Dễ mở rộng, giảm lỗi           |
| LSP        | Thay thế lớp cha bằng lớp con | Đảm bảo tính kế thừa đúng đắn  |
| ISP        | Giao diện chuyên biệt         | Giảm phụ thuộc không cần thiết |
| DIP        | Phụ thuộc vào trừu tượng      | Tăng tính linh hoạt            |


# Singleton

## 🧠 Mẫu Thiết Kế Singleton

### 🎯 Mục Đích

Đảm bảo một lớp chỉ có duy nhất một thể hiện (instance) và cung cấp điểm truy cập toàn cục đến thể hiện đó.[Refactoring Guru+2Refactoring Guru+2Refactoring Guru+2](https://refactoring.guru/design-patterns/java?utm_source=chatgpt.com)

### 🧩 Vấn Đề Giải Quyết

- Kiểm soát số lượng thể hiện của một lớp, thường để quản lý tài nguyên dùng chung như kết nối cơ sở dữ liệu hoặc trình ghi log.
- Cung cấp một điểm truy cập toàn cục đến thể hiện duy nhất này.

### ✅ Ưu Điểm
- Kiểm soát chặt chẽ việc truy cập tài nguyên dùng chung.
- Hỗ trợ khởi tạo lười (lazy initialization) khi cần thiết.
- Cung cấp một điểm truy cập toàn cục đến thể hiện.[Wikipedia](https://de.wikipedia.org/wiki/Singleton_%28Entwurfsmuster%29?utm_source=chatgpt.com)

### ⚠️ Nhược Điểm
- Vi phạm Nguyên tắc Trách nhiệm Đơn (Single Responsibility Principle) vì lớp phải tự quản lý việc khởi tạo thể hiện của chính nó.
- Khó kiểm thử đơn vị do phụ thuộc vào trạng thái toàn cục.
- Có thể gây ra vấn đề trong môi trường đa luồng nếu không được triển khai đúng cách.

---

## 🛠️ Các Cách Triển Khai Singleton trong Java
### 1. Khởi Tạo Sớm (Eager Initialization)
Thể hiện được tạo ngay khi lớp được tải.[Refactoring Guru+1Refactoring Guru+1](https://refactoring.guru/design-patterns/singleton?utm_source=chatgpt.com)

```java
public class Singleton {
    private static final Singleton instance = new Singleton();

    private Singleton() {}

    public static Singleton getInstance() {
        return instance;
    }
}
```

- Đơn giản và an toàn trong môi trường đa luồng.
- Không hỗ trợ khởi tạo lười; thể hiện được tạo ngay cả khi không được sử dụng.[Wikipedia](https://fr.wikipedia.org/wiki/Singleton_%28patron_de_conception%29?utm_source=chatgpt.com)[Refactoring Guru](https://refactoring.guru/design-patterns/java?utm_source=chatgpt.com)

### 2. Khởi Tạo Lười với Đồng Bộ Hóa (Lazy Initialization with Synchronized)

Thể hiện được tạo khi cần, với đồng bộ hóa để đảm bảo an toàn trong môi trường đa luồng.

```java
public class Singleton {
    private static Singleton instance;

    private Singleton() {}

    public static synchronized Singleton getInstance() {
        if (instance == null) {
            instance = new Singleton();
        }
        return instance;
    }
}
```

- Hỗ trợ khởi tạo lười.
    
- Hiệu suất có thể bị ảnh hưởng do đồng bộ hóa.

#### 🔒 Phương Thức `synchronized` Là Gì?
Khi một phương thức được khai báo với từ khóa `synchronized`, Java đảm bảo rằng chỉ một luồng có thể thực thi phương thức đó trên một đối tượng cụ thể tại bất kỳ thời điểm nào. Điều này được thực hiện thông qua việc sử dụng khóa (lock) nội tại (intrinsic lock) của đối tượng.

```java
public class Counter {
    private int count = 0;

    public synchronized void increment() {
        count++;
    }

    public synchronized int getCount() {
        return count;
    }
}
```

Trong ví dụ trên, các phương thức `increment()` và `getCount()` được đồng bộ hóa, đảm bảo rằng khi một luồng đang thực thi một trong các phương thức này, các luồng khác phải chờ cho đến khi luồng hiện tại hoàn thành.

### 3. Khởi Tạo Lười với Double-Checked Locking

Cải thiện hiệu suất bằng cách giảm thiểu việc sử dụng đồng bộ hóa.

```java
public class Singleton {
    private static volatile Singleton instance;

    private Singleton() {}

    public static Singleton getInstance() {
        if (instance == null) {
            synchronized(Singleton.class) {
                if (instance == null) {
                    instance = new Singleton();
                }
            }
        }
        return instance;
    }
}
```

- Hỗ trợ khởi tạo lười và an toàn trong môi trường đa luồng.
    
- Phức tạp hơn trong việc triển khai.
    

### 4. Sử Dụng Enum (Khuyến Nghị từ Java 1.5+)

Cách đơn giản và an toàn nhất để triển khai Singleton trong Java.[Refactoring.Guru+13Refactoring Guru+13Wikipedia+13](https://refactoring.guru/design-patterns/singleton/java/example?utm_source=chatgpt.com)

```java
public enum Singleton {
    INSTANCE;

    public void doSomething() {
        // Thực hiện hành động
    }
}
```

- Đảm bảo an toàn trong môi trường đa luồng.
- Tự động xử lý việc khởi tạo và bảo vệ chống lại việc tạo thể hiện mới thông qua serialization hoặc reflection.[Refactoring Guru+3Wikipedia+3Wikipedia+3](https://fr.wikipedia.org/wiki/Singleton_%28patron_de_conception%29?utm_source=chatgpt.com)

---

## 📌 Ghi Nhớ Nhanh

| Phương Pháp Triển Khai | Khởi Tạo Lười | An Toàn Đa Luồng | Ghi Chú                                    |
| ---------------------- | ------------- | ---------------- | ------------------------------------------ |
| Eager Initialization   | ❌            | ✅               | Đơn giản, nhưng không hỗ trợ khởi tạo lười |
| Synchronized Method    | ✅            | ✅               | Dễ triển khai, nhưng hiệu suất thấp hơn    |
| Double-Checked Locking | ✅            | ✅               | Hiệu suất tốt, nhưng phức tạp hơn          |
| Enum                   | ✅            | ✅               | Khuyến nghị sử dụng trong Java 1.5+        |

---

## 📚 Ví Dụ Thực Tế trong Java API
- `java.lang.Runtime.getRuntime()`
- `java.awt.Desktop.getDesktop()`

# Factory Method

## 🧠 Factory Method Pattern – Ghi chú nhanh

### ✅ Mục đích

Cung cấp một giao diện để tạo đối tượng trong lớp cha, cho phép các lớp con quyết định loại đối tượng cụ thể sẽ được tạo.[Refactoring Guru](https://refactoring.guru/design-patterns/factory-method?utm_source=chatgpt.com)

### 🧱 Thành phần chính

- **Product**: Giao diện hoặc lớp trừu tượng định nghĩa các phương thức chung cho các đối tượng được tạo.
- **ConcreteProduct**: Các lớp cụ thể triển khai `Product`.
- **Creator**: Lớp trừu tượng khai báo phương thức factory (`factoryMethod()`) trả về `Product`.
- **ConcreteCreator**: Lớp con của `Creator`, triển khai `factoryMethod()` để trả về một `ConcreteProduct` cụ thể.[Baeldung](https://www.baeldung.com/java-factory-pattern?utm_source=chatgpt.com)[GeeksforGeeks+1Wikipedia+1](https://www.geeksforgeeks.org/factory-method-design-pattern-in-java/?utm_source=chatgpt.com)

### 📌 Khi nào sử dụng?
- Khi lớp không biết trước loại đối tượng cần tạo.
- Khi muốn ủy quyền việc khởi tạo đối tượng cho các lớp con.
- Khi muốn tách biệt logic khởi tạo khỏi phần sử dụng đối tượng.[GeeksforGeeks](https://www.geeksforgeeks.org/factory-method-design-pattern-in-java/?utm_source=chatgpt.com)

### ✅ Ưu điểm

- Tuân thủ nguyên lý Mở-Đóng (Open/Closed Principle).
- Giảm sự phụ thuộc giữa các lớp (loose coupling).
- Dễ dàng mở rộng và bảo trì hệ thống.[Java Revisited](https://javarevisited.blogspot.com/2011/12/factory-design-pattern-java-example.html?utm_source=chatgpt.com)

### ❌ Nhược điểm

- Tăng số lượng lớp trong hệ thống.
- Có thể làm cho cấu trúc hệ thống trở nên phức tạp hơn.

---

## 🧪 Ví dụ Java – Giao thông vận tải

```java
// Product
interface Transport {
    void deliver();
}

// Concrete Products
class Truck implements Transport {
    public void deliver() {
        System.out.println("Deliver by land in a box.");
    }
}

class Ship implements Transport {
    public void deliver() {
        System.out.println("Deliver by sea in a container.");
    }
}

// Creator
abstract class Logistics {
    public void planDelivery() {
        Transport transport = createTransport();
        transport.deliver();
    }

    protected abstract Transport createTransport();
}

// Concrete Creators
class RoadLogistics extends Logistics {
    protected Transport createTransport() {
        return new Truck();
    }
}

class SeaLogistics extends Logistics {
    protected Transport createTransport() {
        return new Ship();
    }
}

// Client code
public class Main {
    public static void main(String[] args) {
        Logistics logistics;

        logistics = new RoadLogistics();
        logistics.planDelivery(); // Output: Deliver by land in a box.

        logistics = new SeaLogistics();
        logistics.planDelivery(); // Output: Deliver by sea in a container.
    }
}
```

---

## 🔁 So sánh với Abstract Factory

- **Factory Method**: Tạo một đối tượng duy nhất thông qua một phương thức.
- **Abstract Factory**: Tạo một nhóm các đối tượng liên quan thông qua một tập hợp các phương thức.

---

## 📚 Tài liệu tham khảo
- Refactoring Guru: [Factory Method](https://refactoring.guru/design-patterns/factory-method)
- GeeksforGeeks: Factory Method Design Pattern in Java

# Abstract Factory

### ✅ Mục Đích

Abstract Factory là mẫu thiết kế khởi tạo (creational pattern) cho phép tạo ra **các họ sản phẩm liên quan** (ví dụ: `Chair`, `Sofa`, `CoffeeTable`) mà **không cần biết lớp cụ thể** của chúng.


### 🧱 Cấu Trúc
1. **Abstract Products**: Khai báo giao diện cho từng loại sản phẩm (`Chair`, `Sofa`, `CoffeeTable`).
2. **Concrete Products**: Triển khai cụ thể cho từng loại sản phẩm theo từng biến thể (`ModernChair`, `VictorianChair`, v.v.).
3. **Abstract Factory**: Khai báo giao diện với các phương thức tạo sản phẩm (`createChair()`, `createSofa()`, v.v.).
4. **Concrete Factories**: Triển khai cụ thể của Abstract Factory để tạo ra các sản phẩm cụ thể theo biến thể (`ModernFurnitureFactory`, `VictorianFurnitureFactory`, v.v.).
5. **Client**: Sử dụng Abstract Factory và Abstract Products để tạo và sử dụng các sản phẩm mà không phụ thuộc vào các lớp cụ thể.[Java Design Patterns](https://java-design-patterns.com/patterns/abstract-factory/?utm_source=chatgpt.com)

---

### 📌 Ưu Điểm

- Tách biệt mã khách hàng khỏi các lớp cụ thể của sản phẩm.
- Dễ dàng mở rộng để hỗ trợ các họ sản phẩm mới.
- Đảm bảo tính nhất quán giữa các sản phẩm trong cùng một họ.[Refactoring Guru](https://refactoring.guru/design-patterns/abstract-factory?utm_source=chatgpt.com)

---

### ⚠️ Nhược Điểm
- Có thể dẫn đến sự phức tạp khi số lượng họ sản phẩm và biến thể tăng lên.
- Khó khăn trong việc mở rộng để hỗ trợ các sản phẩm mới nếu giao diện Abstract Factory không được thiết kế linh hoạt.

---

### 📄 Ví Dụ Java

```java
// Abstract Products
interface Chair {
    void sitOn();
}

interface Sofa {
    void lieOn();
}

// Concrete Products
class ModernChair implements Chair {
    public void sitOn() {
        System.out.println("Sitting on a modern chair.");
    }
}

class VictorianChair implements Chair {
    public void sitOn() {
        System.out.println("Sitting on a Victorian chair.");
    }
}

class ModernSofa implements Sofa {
    public void lieOn() {
        System.out.println("Lying on a modern sofa.");
    }
}

class VictorianSofa implements Sofa {
    public void lieOn() {
        System.out.println("Lying on a Victorian sofa.");
    }
}

// Abstract Factory
interface FurnitureFactory {
    Chair createChair();
    Sofa createSofa();
}

// Concrete Factories
class ModernFurnitureFactory implements FurnitureFactory {
    public Chair createChair() {
        return new ModernChair();
    }
    public Sofa createSofa() {
        return new ModernSofa();
    }
}

class VictorianFurnitureFactory implements FurnitureFactory {
    public Chair createChair() {
        return new VictorianChair();
    }
    public Sofa createSofa() {
        return new VictorianSofa();
    }
}

// Client
public class Application {
    private Chair chair;
    private Sofa sofa;

    public Application(FurnitureFactory factory) {
        chair = factory.createChair();
        sofa = factory.createSofa();
    }

    public void useFurniture() {
        chair.sitOn();
        sofa.lieOn();
    }

    public static void main(String[] args) {
        FurnitureFactory factory = new ModernFurnitureFactory();
        Application app = new Application(factory);
        app.useFurniture();
    }
}
```

---

### 🧠 Ghi Nhớ Nhanh

- **Abstract Factory**: Tạo ra các họ sản phẩm liên quan mà không cần biết lớp cụ thể.
- **Factory Method**: Tạo ra một sản phẩm cụ thể thông qua một phương thức.
- Sử dụng khi cần đảm bảo tính nhất quán giữa các sản phẩm trong cùng một họ.

---

### 📚 Tham Khảo

- Refactoring Guru: [Abstract Factory](https://refactoring.guru/design-patterns/abstract-factory)

# Prototype

## 🧬 Prototype Pattern – Mẫu thiết kế Prototype

### ✅ Mục đích

Tạo ra các đối tượng mới bằng cách sao chép (clone) các đối tượng hiện có, thay vì khởi tạo từ đầu. Điều này giúp giảm chi phí tạo đối tượng và tránh phụ thuộc vào lớp cụ thể của đối tượng.[Medium+1Medium+1](https://medium.com/%40CodeWithTech/efficient-object-creation-using-the-prototype-pattern-with-real-world-examples-ba87082befba?utm_source=chatgpt.com)

### 📌 Khi nào sử dụng?

- Khi việc tạo đối tượng mới tốn kém tài nguyên hoặc phức tạp.
    
- Khi cần tạo nhiều đối tượng giống nhau với các cấu hình khác nhau.
    
- Khi muốn tránh việc tạo nhiều lớp con chỉ để cấu hình khác nhau.
    

### 🧱 Cấu trúc

1. **Prototype Interface**: Khai báo phương thức `clone()`.
    
2. **Concrete Prototype**: Triển khai phương thức `clone()` để sao chép chính nó.
    
3. **Client**: Sử dụng phương thức `clone()` để tạo bản sao của đối tượng.[GeeksforGeeks](https://www.geeksforgeeks.org/prototype-design-pattern/?utm_source=chatgpt.com)
    

---

## 💻 Ví dụ Java: Hệ thống hình học

### 1. Giao diện Prototype

```java
public interface Shape extends Cloneable {
    Shape clone();
    void draw();
}
```

### 2. Triển khai cụ thể: Hình tròn

```java
public class Circle implements Shape {
    private String color;

    public Circle(String color) {
        this.color = color;
    }

    @Override
    public Circle clone() {
        return new Circle(this.color);
    }

    @Override
    public void draw() {
        System.out.println("Vẽ hình tròn màu " + color);
    }
}
```

### 3. Sử dụng trong Client

```java
public class PrototypeDemo {
    public static void main(String[] args) {
        Circle original = new Circle("Đỏ");
        Circle copy = original.clone();

        original.draw(); // Vẽ hình tròn màu Đỏ
        copy.draw();     // Vẽ hình tròn màu Đỏ
    }
}
```

---

## 🧠 Ghi chú nhanh

- Java hỗ trợ `clone()` thông qua giao diện `Cloneable` và phương thức `Object.clone()`.
- Cần ghi đè phương thức `clone()` để thực hiện sao chép sâu (deep copy) nếu đối tượng chứa các tham chiếu đến đối tượng khác.
- Có thể sử dụng một "Prototype Registry" (bộ đăng ký nguyên mẫu) để lưu trữ và quản lý các nguyên mẫu sẵn có.[Wikipedia+5Wikipedia+5refactoring.guru+5](https://it.wikipedia.org/wiki/Prototype_pattern?utm_source=chatgpt.com)

---

## 🧪 Tình huống thực tế

- Trong ứng dụng đồ họa, khi cần tạo nhiều hình với cấu hình tương tự, sử dụng Prototype giúp tiết kiệm thời gian và tài nguyên.
- Trong trò chơi, khi cần tạo nhiều kẻ địch với các thuộc tính giống nhau, có thể clone từ một nguyên mẫu ban đầu.

---

Để hiểu rõ hơn về mẫu thiết kế Prototype, bạn có thể tham khảo bài viết chi tiết tại Refactoring Guru: [Prototype Design Pattern](https://refactoring.guru/design-patterns/prototype).

# Adapter
## 🎯 Mục đích

Adapter cho phép các đối tượng với giao diện không tương thích có thể cộng tác bằng cách chuyển đổi giao diện của một lớp thành giao diện mà lớp khác mong đợi.[refactoring.guru](https://refactoring.guru/design-patterns/adapter?utm_source=chatgpt.com)

---

## 🧩 Thành phần

- **Target (Giao diện mục tiêu)**: Giao diện mà client mong đợi.
- **Adaptee (Đối tượng cần thích nghi)**: Lớp hiện có với giao diện không tương thích.
- **Adapter (Bộ chuyển đổi)**: Lớp chuyển đổi giao diện của Adaptee thành Target.[Java Design Patterns+1Stack Overflow+1](https://java-design-patterns.com/patterns/adapter/?utm_source=chatgpt.com)[Wikipedia+1refactoring.guru+1](https://en.wikipedia.org/wiki/Adapter_pattern?utm_source=chatgpt.com)

---

## 🔧 Cách triển khai

### 1. **Object Adapter (Sử dụng thành phần)**

Adapter chứa một instance của Adaptee và ủy quyền các lời gọi phương thức.[Wikipedia+1refactoring.guru+1](https://it.wikipedia.org/wiki/Adapter_pattern?utm_source=chatgpt.com)
**Ưu điểm**: Linh hoạt, có thể thích nghi với các lớp Adaptee khác nhau.[Java Design Patterns+5refactoring.guru+5refactoring.guru+5](https://refactoring.guru/design-patterns/adapter?utm_source=chatgpt.com)

### 2. **Class Adapter (Sử dụng kế thừa)**

Adapter kế thừa từ cả Target và Adaptee.
**Lưu ý**: Chỉ khả dụng trong ngôn ngữ hỗ trợ đa kế thừa (ví dụ: C++).

---

## 💡 Khi nào sử dụng?

- Khi bạn muốn sử dụng một lớp hiện có nhưng giao diện của nó không phù hợp với hệ thống hiện tại.
- Khi bạn muốn tạo một lớp tái sử dụng mà không thay đổi mã nguồn của các lớp hiện có.

---

## ✅ Ưu điểm

- Tách biệt giao diện với triển khai.
- Tăng khả năng tái sử dụng mã.
- Dễ dàng tích hợp với hệ thống hiện có.[refactoring.guru+3Wikipedia+3refactoring.guru+3](https://it.wikipedia.org/wiki/Adapter_pattern?utm_source=chatgpt.com)

---

## ⚠️ Nhược điểm

- Có thể làm tăng độ phức tạp của hệ thống.
- Quá nhiều adapter có thể dẫn đến khó khăn trong việc bảo trì.

---

## 📌 Ví dụ Java: Adapter cho cổng sạc điện thoại

```java
// Giao diện mục tiêu
interface MicroUsbPhone {
    void recharge();
    void useMicroUsb();
}

// Adaptee
interface LightningPhone {
    void recharge();
    void useLightning();
}

// Lớp cụ thể của Adaptee
class Iphone implements LightningPhone {
    private boolean connector;

    public void useLightning() {
        connector = true;
        System.out.println("Lightning connected");
    }

    public void recharge() {
        if (connector) {
            System.out.println("Recharge started");
            System.out.println("Recharge finished");
        } else {
            System.out.println("Connect Lightning first");
        }
    }
}

// Adapter
class LightningToMicroUsbAdapter implements MicroUsbPhone {
    private final LightningPhone lightningPhone;

    public LightningToMicroUsbAdapter(LightningPhone lightningPhone) {
        this.lightningPhone = lightningPhone;
    }

    public void useMicroUsb() {
        System.out.println("MicroUsb connected");
        lightningPhone.useLightning();
    }

    public void recharge() {
        lightningPhone.recharge();
    }
}

// Client
public class AdapterDemo {
    public static void main(String[] args) {
        Iphone iPhone = new Iphone();
        MicroUsbPhone adapter = new LightningToMicroUsbAdapter(iPhone);

        adapter.useMicroUsb();
        adapter.recharge();
    }
}
```

---

## 📝 Tóm tắt nhanh

- **Mẫu thiết kế**: Adapter (Bộ chuyển đổi)
- **Loại**: Cấu trúc
- **Cách triển khai**: Object Adapter (thành phần), Class Adapter (kế thừa)
- **Mục đích**: Cho phép các lớp với giao diện không tương thích làm việc cùng nhau
- **Ví dụ**: Chuyển đổi cổng sạc Lightning sang MicroUSB[refactoring.guru](https://refactoring.guru/design-patterns/adapter/csharp/example?utm_source=chatgpt.com)[refactoring.guru+3Wikipedia+3refactoring.guru+3](https://en.wikipedia.org/wiki/Adapter_pattern?utm_source=chatgpt.com)[refactoring.guru+1Java Design Patterns+1](https://refactoring.guru/design-patterns/adapter?utm_source=chatgpt.com)

---

Để hiểu rõ hơn, bạn có thể tham khảo thêm tại trang Refactoring.Guru: [Adapter Design Pattern](https://refactoring.guru/design-patterns/adapter).

# Decorator

## 🧱 Mẫu Thiết Kế Decorator (Wrapper)

### ✅ Mục đích

Cho phép thêm hành vi mới vào đối tượng một cách linh hoạt tại thời điểm chạy mà không cần sửa đổi cấu trúc lớp ban đầu.[refactoring.guru](https://refactoring.guru/design-patterns/decorator/java/example?utm_source=chatgpt.com)

### 📌 Khi nào sử dụng?

- Muốn thêm chức năng cho đối tượng mà không thay đổi mã nguồn gốc.
    
- Tránh việc tạo quá nhiều lớp con để mở rộng chức năng.
    
- Cần kết hợp linh hoạt các hành vi (ví dụ: thêm nhiều topping cho pizza).[LinkedIn+1Medium+1](https://www.linkedin.com/pulse/decorator-design-pattern-tutorial-java-example-youve-been-digest?utm_source=chatgpt.com)[Reddit+2GeeksforGeeks+2Medium+2](https://www.geeksforgeeks.org/decorator-design-pattern-in-java-with-example/?utm_source=chatgpt.com)
    

### 🧩 Cấu trúc

- **Component**: Giao diện chung cho các đối tượng.
    
- **ConcreteComponent**: Triển khai mặc định của Component.
    
- **Decorator**: Lớp trừu tượng triển khai Component và chứa một tham chiếu đến Component.
    
- **ConcreteDecorator**: Mở rộng Decorator để thêm hành vi mới.
    

---

## ☕ Ví dụ Java: Mô phỏng đơn giản

```java
// Component
interface Coffee {
    String getDescription();
    double cost();
}

// ConcreteComponent
class SimpleCoffee implements Coffee {
    public String getDescription() { return "Simple Coffee"; }
    public double cost() { return 5.0; }
}

// Decorator
abstract class CoffeeDecorator implements Coffee {
    protected Coffee coffee;
    public CoffeeDecorator(Coffee coffee) { this.coffee = coffee; }
    public String getDescription() { return coffee.getDescription(); }
    public double cost() { return coffee.cost(); }
}

// ConcreteDecorator A
class MilkDecorator extends CoffeeDecorator {
    public MilkDecorator(Coffee coffee) { super(coffee); }
    public String getDescription() { return super.getDescription() + ", Milk"; }
    public double cost() { return super.cost() + 1.0; }
}

// ConcreteDecorator B
class SugarDecorator extends CoffeeDecorator {
    public SugarDecorator(Coffee coffee) { super(coffee); }
    public String getDescription() { return super.getDescription() + ", Sugar"; }
    public double cost() { return super.cost() + 0.5; }
}

// Sử dụng
public class DecoratorPatternDemo {
    public static void main(String[] args) {
        Coffee coffee = new SimpleCoffee();
        System.out.println(coffee.getDescription() + " $" + coffee.cost());

        Coffee milkCoffee = new MilkDecorator(coffee);
        System.out.println(milkCoffee.getDescription() + " $" + milkCoffee.cost());

        Coffee sugarMilkCoffee = new SugarDecorator(milkCoffee);
        System.out.println(sugarMilkCoffee.getDescription() + " $" + sugarMilkCoffee.cost());
    }
}
```

**Kết quả:**

```txt
Simple Coffee $5.0
Simple Coffee, Milk $6.0
Simple Coffee, Milk, Sugar $6.5
```

---

## 📚 Ghi nhớ nhanh

| Đặc điểm          | Mô tả                                                                                                |
| ----------------- | ---------------------------------------------------------------------------------------------------- |
| **Loại mẫu**      | Cấu trúc (Structural)                                                                                |
| **Ưu điểm**       | - Thêm hành vi mà không sửa đổi lớp gốc  <br>- Kết hợp linh hoạt các hành vi                         |
| **Nhược điểm**    | - Có thể tạo nhiều lớp nhỏ  <br>- Khó theo dõi khi có nhiều lớp bao bọc                              |
| **Ví dụ thực tế** | - Java I/O: `BufferedReader`, `InputStream`  <br>- Giao diện người dùng: thêm thanh cuộn, viền, v.v. |

---

## 🔗 Tham khảo thêm

- Refactoring Guru: [Decorator Pattern](https://refactoring.guru/design-patterns/decorator)
    
- GeeksforGeeks: Decorator Design Pattern in Java
