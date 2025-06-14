---
date: 2025-02-19
draft: false
status: Doing
title: Bộ sửa đổi trong Java
description: Bộ sửa đổi (Modifiers) trong Java giúp kiểm soát quyền truy cập và hành vi của các lớp, phương thức, biến. Bài viết này sẽ giúp bạn hiểu rõ từng loại bộ sửa đổi và cách sử dụng chúng hiệu quả.
author: PhDoanh
authorlink: https://github.com/PhDoanh
tags:
  - coding
  - java
  - oop
  - programming-method
aliases:
  - modifiers
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
    src="images/modifiers.png"
    alt="Bộ sửa đổi trong Java" 
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

Bộ sửa đổi (**Modifiers**) trong Java là các từ khóa đặc biệt giúp **xác định phạm vi truy cập, đặc điểm và hành vi** của lớp, phương thức và biến. Chúng được chia thành **hai loại chính**:

- **Access Modifiers** (Bộ sửa đổi truy cập) – kiểm soát mức độ truy cập.
- **Non-access Modifiers** (Bộ sửa đổi phi truy cập) – quy định đặc tính của thành phần trong Java.

Việc hiểu rõ bộ sửa đổi giúp lập trình viên **viết code bảo mật hơn, tối ưu hiệu suất và nâng cao khả năng tái sử dụng**.

# 🔑 Bộ sửa đổi truy cập
**Bộ sửa đổi truy cập** trong Java xác định phạm vi và quyền truy cập của các lớp, phương thức và thuộc tính trong một chương trình. Java cung cấp 3 loại bộ sửa đổi truy cập chính: 
- **`public`**: cho phép truy cập từ mọi nơi
- **`protected`**: truy cập được từ cùng package và lớp con
- **`private`**: chỉ truy cập trong cùng lớp 

Việc sử dụng đúng các bộ sửa đổi này giúp kiểm soát tốt hơn tính đóng gói và bảo mật của mã nguồn

> [!question]- Package là gì?
> - Package trong Java hoạt động giống như **thư mục** chứa các file mã nguồn, có thể có cả package con để tổ chức các lớp và interface một cách hợp lý. Nhưng **Java không tự động coi thư mục là package** mà phải khai báo `package PackageName;` ở đầu mỗi file `.java`  thuộc package đó. Nếu không, lớp sẽ thuộc **default package** và chỉ dùng được trong cùng thư mục.
> - Mỗi file Java có thể chứa nhiều lớp hoặc interface, nhưng chỉ có duy nhất một lớp (hoặc interface) được khai báo với `public` vì quy tắc của Java yêu cầu tên file phải khớp với tên của thành phần `public` duy nhất trong file đó, nhằm đảm bảo tính nhất quán và dễ quản lý mã nguồn.

> [!info] Lưu ý
> Nếu không sử dụng bộ sửa đổi truy cập, phạm vi mặc định (còn gọi là _package-private_) sẽ được áp dụng. Điều này có nghĩa là:
> - Các thuộc tính và phương thức có thể được truy cập bởi bất kỳ lớp nào trong cùng package.
> - Không thể truy cập từ các lớp bên ngoài package, ngay cả khi có quan hệ kế thừa.

## Public - Công khai quyền truy cập
Lớp, phương thức hoặc biến khai báo là `public` có thể được truy cập từ bất kỳ đâu. Khi khai báo thành phần với `public`, bạn tạo ra khả năng chia sẻ và tái sử dụng code một cách linh hoạt, nhưng cần cân nhắc kỹ lưỡng để không làm lộ quá nhiều thông tin nội bộ của lớp

```java title="PackageName/Person.java" {1,2,3,5,10}
public class Person {
    public String name;
    public int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public void displayInfo() {
        System.out.println("Name: " + name + ", Age: " + age);
    }
}
```

> [!explain]- Giải thích code
> - **Dòng 1**: Từ khóa `public` cho phép lớp `Person` được truy cập từ các lớp khác, ví dụ như từ lớp `Main`.
> - **Dòng 2**: Thuộc tính `name` được khai báo `public` cho phép truy cập trực tiếp từ bên ngoài lớp (mặc dù về mặt an toàn, thường nên dùng `private` và sử dụng getter/setter).
> - **Dòng 3**: Tương tự, thuộc tính `age` được khai báo `public` để truy cập từ bên ngoài lớp.
> - **Dòng 5**: Constructor của lớp `Person` được khai báo `public` để có thể khởi tạo đối tượng từ bất kỳ đâu.
> - **Dòng 10**: Phương thức `displayInfo` được khai báo `public` để có thể gọi từ các lớp khác (như trong `Main`).

```java title="PackageName/Main.java" {3,4}
public class Main {
    public static void main(String[] args) {
        Person person = new Person("Alice", 30);
        person.displayInfo();
    }
}
```

```txt title="Đầu ra"
Name: Alice, Age: 30
```

> [!explain]- Giải thích code
> - **Dòng 3**: Khởi tạo đối tượng `person` sử dụng constructor của lớp `Person` được khai báo trong file `PackageName/Person.java`
> - **Dòng 4**: Gọi phương thức `displayInfo` (được khai báo `public` trong lớp `Person`) để hiển thị thông tin.

## Private - Đóng quyền truy cập với bên ngoài 
Chỉ cho phép truy cập trong cùng lớp chứa nó. Dùng để bảo vệ dữ liệu khỏi bị truy cập trực tiếp từ bên ngoài.

```java title="PackageName/Person.java" {1-2}
public class Person {
    private String name;
    private int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public void displayInfo() {
        System.out.println("Name: " + name + ", Age: " + age);
    }
}
```

> [!explain]- Giải thích code
> - **Dòng 1-2**: Cả hai thuộc tính `name` và `age` được khai báo là `private`, nghĩa là chúng không thể được truy cập từ bên ngoài lớp `Person`. 

```java title="PackageName/Main.java"
public class Main {
    public static void main(String[] args) {
        Person person = new Person("Alice", 30);
        
        // Cố gắng truy cập thuộc tính private trực tiếp
        person.name = "Bob";
        person.displayInfo();
    }
}
```

> [!bug]- Lỗi truy cập biến riêng tư
> ```txt
> error: name has private access in Person
> 	person.name = "Bob";
> ```

## Protected - Hạn chế quyền truy cập
Có thể truy cập trong cùng package và các lớp con (subclass). Thường được dùng trong kế thừa (Inheritance).

```java title="PackageName/Animal.java" {2,8,13,15,19}
public class Animal {
    protected String name;

    public Animal(String name) {
        this.name = name;
    }

    protected void displayInfo() {
        System.out.println("Animal name: " + name);
    }
}

class Dog extends Animal {
    public Dog(String name) {
        super(name);
    }

    public void displayDogInfo() {
        displayInfo();
        System.out.println("This is a dog.");
    }
}
```

> [!explain]- Giải thích code
> - **Dòng 2**: Khai báo thuộc tính `name` kiểu `protected`, cho phép các lớp trong cùng `PackageName` có thể truy cập
> - **Dòng 8**: Để các lớp trong cùng `PackageName` có thể truy cập phương thức `displayInfo`, ta gán nó kiểu `protected`
> - **Dòng 13**: Định nghĩa lớp con `Dog` kế thừa từ lớp cha `Animal` 
> - **Dòng 15**: Gọi constructor của lớp cha và truyền tên cho đối tượng (`super(name) = Animal(name)`)
> - **Dòng 19**: Gọi phương thức `displayInfo` từ lớp cha `Animal`, vì phương thức này có quyền truy cập `protected`.

```java title="PackageName/Main.java" {3-6}
public class Main {
    public static void main(String[] args) {
        Dog dog = new Dog("Buddy");
        dog.displayDogInfo();
        dog.name = "Goofy";
        dog.displayInfo();
    }
}
```

```txt title="Đầu ra"
Animal name: Buddy
This is a dog.
Animal name: Goofy
```

> [!explain]- Giải thích code
> - **Dòng 3**: Khởi tạo đối tượng mới từ lớp `Dog` trong file `PackageName/Animal.java` 
> - **Dòng 4**: gọi phương thức của lớp `Dog` để in ra thông tin đối tượng
> - **Dòng 5**: thay đổi trực tiếp thuộc tính `name` của lớp `Animal` mà không gặp lỗi truy cập do thuộc tính kiểu `protected`  
> - **Dòng 6**: gọi phương thức của lớp `Animal` từ đối tượng `dog` do nó kế thừa từ lớp đó và phương thức thuộc kiểu `protected`

## Packaged - Truy cập trong cùng gói

> [!caution]- Nội dung đang hoàn thiện
> Quá trình xây dựng nội dung này có thể mất nhiều thời gian ⌛, nhưng bạn có thể thúc đẩy nó bằng cách tham gia [[article-collaboration-guide|cộng tác bài viết]] 🤝
> 
> **Rất mong sự thông cảm của các bạn 🙏**

---

# ⚙️ Bộ sửa đổi phi truy cập

> [!caution]- Nội dung đang hoàn thiện
> Quá trình xây dựng nội dung này có thể mất nhiều thời gian ⌛, nhưng bạn có thể thúc đẩy nó bằng cách tham gia [[article-collaboration-guide|cộng tác bài viết]] 🤝
> 
> **Rất mong sự thông cảm của các bạn 🙏**

%% 
{mô tả}

## Static - Phương thức & biến tĩnh
- Thuộc về lớp chứ không phải đối tượng cụ thể.
- Có thể gọi trực tiếp mà không cần tạo đối tượng.


## Final - Không thể thay đổi
- Dùng cho biến: không thể gán lại giá trị.
- Dùng cho phương thức: không thể ghi đè (override).  
- Dùng cho lớp: không thể kế thừa.

## Abstract - Trừu tượng
Chỉ có thể khai báo mà không có phần thân (nếu là phương thức) hoặc không thể tạo đối tượng trực tiếp (nếu là lớp).

## Synchronized - Đồng bộ hóa
Dùng để kiểm soát truy cập trong môi trường đa luồng (multithreading)


## Volatile - Biến có thể thay đổi
Giúp đảm bảo giá trị biến được cập nhật đúng trong môi trường đa luồng.
%%

---

# 🎉 Tổng kết
Bộ sửa đổi trong Java là công cụ quan trọng giúp kiểm soát truy cập và định nghĩa hành vi của các thành phần trong chương trình. Chúng bao gồm Access Modifiers (Public, Private, Protected) và Non-access Modifiers (Static, Final, Abstract, Synchronized, Volatile, ...)

