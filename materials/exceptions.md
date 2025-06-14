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
  - exceptions
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
    src="images/exceptions.png"
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

## Tổng quan về Ngoại lệ (Exception)

- **Ngoại lệ (Exception)** là lỗi xảy ra trong quá trình thực thi chương trình, làm gián đoạn luồng xử lý bình thường.
    
- Ví dụ:
    - `NullPointerException`: khi gọi phương thức trên đối tượng null.
    - `IndexOutOfBoundsException`: khi truy cập phần tử ngoài phạm vi mảng.
    - `NumberFormatException`: khi chuyển đổi chuỗi không hợp lệ sang số.

---

## 🛠️ Xử lý ngoại lệ với `try-catch`

- Sử dụng khối `try-catch` để bắt và xử lý ngoại lệ:
    
```java
try {
    // Mã có thể gây ra ngoại lệ
} catch (Exception e) {
    // Xử lý khi xảy ra ngoại lệ
}
```
    
- Ví dụ: Xử lý khi người dùng nhập không phải số:
    
```java
Scanner reader = new Scanner(System.in);
System.out.print("Nhập số: ");
int number = -1;

try {
    number = Integer.parseInt(reader.nextLine());
    System.out.println("Bạn đã nhập: " + number);
} catch (NumberFormatException e) {
    System.out.println("Đầu vào không hợp lệ.");
}
```

---

## 🚨 Tự ném ngoại lệ với `throw`

- Sử dụng `throw` để ném ngoại lệ một cách chủ động:
    
```java
public void setGrade(int grade) {
    if (grade < 0 || grade > 5) {
        throw new IllegalArgumentException("Điểm phải từ 0 đến 5.");
    }
    this.grade = grade;
}
```

---

## 📌 Ngoại lệ bắt buộc và không bắt buộc

- **Checked exceptions**: Phải xử lý hoặc khai báo bằng `throws`. Ví dụ: `IOException`, `FileNotFoundException`.
- **Unchecked exceptions**: Không bắt buộc xử lý. Ví dụ: `NullPointerException`, `IllegalArgumentException`.

---

## 🔗 Ngoại lệ trong Interface
- Interface có thể khai báo phương thức ném ngoại lệ:
```java
public interface FileServer {
    String load(String fileName) throws Exception;
    void save(String fileName, String textToSave) throws Exception;
}
```
- Lớp triển khai phải xử lý hoặc khai báo lại ngoại lệ tương ứng.

---

## `try-with-resources` – Tự động đóng tài nguyên

- **Khái niệm**: `try-with-resources` là cú pháp trong Java giúp tự động đóng các tài nguyên (như file, kết nối cơ sở dữ liệu) sau khi sử dụng, giảm thiểu rủi ro rò rỉ tài nguyên.[IOFlood](https://ioflood.com/blog/java-try-with-resources/?utm_source=chatgpt.com)
    
- **Cách sử dụng**:
    
```java
try (ResourceType resource = new ResourceType()) {
    // Sử dụng tài nguyên
} catch (Exception e) {
    // Xử lý ngoại lệ
}
```
    

Trong đó, `ResourceType` phải triển khai giao diện `AutoCloseable` hoặc `Closeable`.

- **Ví dụ**:
    
```java
try (BufferedReader reader = new BufferedReader(new FileReader("file.txt"))) {
    String line = reader.readLine();
    System.out.println(line);
} catch (IOException e) {
    e.printStackTrace();
}
```
    

Ở ví dụ trên, `BufferedReader` sẽ được tự động đóng sau khi khối `try` kết thúc, dù có xảy ra ngoại lệ hay không.[Jenkov+5Programiz+5Oracle Documentation+5](https://www.programiz.com/java-programming/try-with-resources?utm_source=chatgpt.com)

- **Đặc điểm**:
    
    - Đảm bảo tài nguyên được đóng tự động mà không cần khối `finally`.
        
    - Hỗ trợ nhiều tài nguyên trong cùng một khối `try`:
        
```java
try (FileReader fr = new FileReader("input.txt");
     BufferedReader br = new BufferedReader(fr)) {
    // Sử dụng tài nguyên
} catch (IOException e) {
    e.printStackTrace();
}
```
        
    - Nếu cả khối `try` và phương thức `close()` của tài nguyên đều ném ngoại lệ, ngoại lệ từ khối `try` sẽ được ném ra, còn ngoại lệ từ `close()` sẽ được thêm vào danh sách ngoại lệ bị ức chế (suppressed exceptions).
        

---

## 📌 Lưu ý quan trọng

- **Tài nguyên phải đóng**: Chỉ các đối tượng triển khai `AutoCloseable` hoặc `Closeable` mới có thể sử dụng trong `try-with-resources`.
- **Java 9 trở lên**: Có thể sử dụng biến đã được khai báo bên ngoài khối `try` nếu biến đó là hiệu quả cuối cùng (effectively final).

---

## ✅ Ghi nhớ nhanh
- **`try-catch`**: Bắt và xử lý ngoại lệ.
- **`throw`**: Ném ngoại lệ một cách chủ động.
- **`throws`**: Khai báo ngoại lệ có thể ném trong phương thức.
- **Checked exceptions**: Phải xử lý hoặc khai báo.
- **Unchecked exceptions**: Không bắt buộc xử lý.
- **Tự động đóng tài nguyên**: Giảm thiểu rủi ro rò rỉ tài nguyên.
- **Cú pháp ngắn gọn**: Giảm thiểu mã nguồn và dễ đọc.
- **Hỗ trợ nhiều tài nguyên**: Quản lý nhiều tài nguyên trong một khối `try`.
- **Quản lý ngoại lệ hiệu quả**: Ngoại lệ từ `close()` được ức chế nếu có ngoại lệ từ khối `try`.
