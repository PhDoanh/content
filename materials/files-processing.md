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
  - files processing
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
    src="images/files-processing.png"
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

## 📘 Sổ Tay: Đọc Dữ Liệu Từ Tệp Trong Java

### 🧰 1. Đọc Dữ Liệu Từ Bàn Phím

Sử dụng `Scanner` để đọc dữ liệu từ người dùng:

```java
Scanner scanner = new Scanner(System.in);
while (true) {
    String line = scanner.nextLine();
    if (line.equals("end")) {
        break;
    }
    System.out.println(line);
}
```

---

### 📂 2. Tệp Tin và Hệ Thống Tệp
- Tệp tin là tập hợp dữ liệu được lưu trữ trên ổ đĩa.
- Có thể chứa văn bản, hình ảnh, âm thanh, v.v.
- Hệ thống tệp quản lý cách lưu trữ và truy cập các tệp tin.[Java Programming](https://java-programming.mooc.fi/part-4/3-files-and-reading-data/?utm_source=chatgpt.com)

---

### 📄 3. Đọc Dữ Liệu Từ Tệp Tin

Sử dụng `Scanner` để đọc dữ liệu từ tệp:

```java
import java.nio.file.Paths;
import java.util.Scanner;

public class FileReaderExample {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(Paths.get("filename.txt"))) {
            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                System.out.println(line);
            }
        } catch (Exception e) {
            System.out.println("Lỗi: " + e.getMessage());
        }
    }
}
```

---

### 📝 4. Phân Tích Dữ Liệu Từ Tệp

Ví dụ: Đọc tệp chứa thông tin người dùng và xử lý từng dòng:

```java
try (Scanner scanner = new Scanner(Paths.get("users.txt"))) {
    while (scanner.hasNextLine()) {
        String line = scanner.nextLine();
        String[] parts = line.split(",");
        String name = parts[0];
        int age = Integer.parseInt(parts[1]);
        System.out.println(name + " is " + age + " years old.");
    }
} catch (Exception e) {
    System.out.println("Lỗi: " + e.getMessage());
}
```

---

### ✅ 5. Ghi Nhớ
- Sử dụng `Scanner` với `Paths.get("filename")` để đọc tệp.
- Xử lý ngoại lệ khi làm việc với tệp để tránh lỗi chương trình.
- Sử dụng `split()` để phân tách dữ liệu trong dòng.

#### 🖥️ Ghi dữ liệu vào tệp tin

```java
import java.io.PrintWriter;

public class Storer {
    public void writeToFile(String fileName, String text) throws Exception {
        PrintWriter writer = new PrintWriter(fileName);
        writer.println(text);
        writer.close();
    }

    public static void main(String[] args) throws Exception {
        Storer storer = new Storer();
        storer.writeToFile("diary.txt", "Dear diary, today was a good day.");
    }
}
```

- `println`: Ghi chuỗi và xuống dòng.
- `print`: Ghi chuỗi mà không xuống dòng.
- `close()`: Đóng tệp và lưu dữ liệu.

---

#### ⚠️ Xử lý ngoại lệ
- `PrintWriter` có thể ném ngoại lệ khi tạo đối tượng.
- Cần sử dụng `throws Exception` hoặc khối `try-catch` để xử lý.

---

#### 🔄 Ghi thêm vào tệp hiện có
- Dùng `FileWriter` với tham số `true` để thêm dữ liệu vào tệp mà không ghi đè.

```java
import java.io.FileWriter;
import java.io.PrintWriter;

public class Appender {
    public void appendToFile(String fileName, String text) throws Exception {
        PrintWriter writer = new PrintWriter(new FileWriter(fileName, true));
        writer.println(text);
        writer.close();
    }

    public static void main(String[] args) throws Exception {
        Appender appender = new Appender();
        appender.appendToFile("diary.txt", "Another great day!");
    }
}
```

---

#### 📚 Tài liệu tham khảo

- [Xử lý tệp tin - MOOC.fi Java Programming](https://java-programming.mooc.fi/part-11/4-processing-files/)