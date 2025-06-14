---
date: 2025-02-15
draft: false
status: Done
title: "Maven - Công cụ quản lý dự án Java"
description: ""
author: PhDoanh
authorlink: https://github.com/PhDoanh
tags: 
  - "coding"
  - project-manager
  - java
  - tools
aliases:
  - "maven"
cssclasses:
  - img
  - btn
---
%% ĐỊNH DẠNG TÊN FILE: "tên-bài-viết" | VD: jp-typing-guide %%

%% <figure style="text-align: center; margin: 20px auto;">
  <img 
    src="images/maven.png"
    alt="Maven - Công cụ quản lý dự án Java" 
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
</figure> %%

**Maven** là một công cụ quản lý dự án (project management tool) và hệ thống xây dựng (build automation tool) dành cho các dự án Java. Nó giúp quản lý cấu hình dự án, phụ thuộc (dependencies), và các quy trình xây dựng (build lifecycle). Maven chủ yếu được sử dụng trong phát triển phần mềm để tự động hóa việc biên dịch mã nguồn, kiểm tra, đóng gói và triển khai ứng dụng.

# 🌟 Các tính năng chính của Maven

1. **Quản lý dự án:**

- Maven giúp xác định các thông tin cấu hình cho một dự án, như tên, phiên bản, tác giả, và các phụ thuộc của dự án (dependencies).
- Các dự án Maven được mô tả thông qua một tệp cấu hình gọi là `pom.xml` (Project Object Model), nơi chứa các thông tin về dự án và các cài đặt quan trọng như các plugin, phụ thuộc, v.v.

2. **Quản lý phụ thuộc (Dependency Management):**

- Maven giúp dễ dàng quản lý các thư viện bên ngoài (thư viện Java) mà dự án cần sử dụng. Thay vì phải tải và cấu hình các thư viện thủ công, Maven sẽ tự động tải chúng từ kho lưu trữ trung tâm (Central Repository) hoặc từ các kho khác khi cần.
- Maven sử dụng tệp `pom.xml` để xác định và quản lý các thư viện này, đảm bảo rằng các phụ thuộc được tải đúng phiên bản.

3. **Chu trình xây dựng tự động (Build Lifecycle):**

- Maven định nghĩa một chu trình xây dựng gồm các giai đoạn (phases) như **compile**, **test**, **package**, **install**, và **deploy**. Người dùng có thể chỉ định lệnh Maven để tự động thực hiện các bước xây dựng này.
- Các plugin và mục tiêu (goals) được sử dụng để tự động hóa các tác vụ như biên dịch mã nguồn, chạy kiểm tra, đóng gói ứng dụng, v.v.

4. **Tích hợp kiểm thử (Testing Integration):**

- Maven hỗ trợ tích hợp với các công cụ kiểm thử tự động như JUnit, TestNG, giúp chạy các bài kiểm tra tự động trong quá trình xây dựng.
- Các bài kiểm tra có thể được chạy trong các giai đoạn cụ thể của chu trình xây dựng.

5. **Tạo tài liệu và báo cáo:**

- Maven hỗ trợ tạo các báo cáo tự động về dự án, bao gồm báo cáo kiểm thử, báo cáo chất lượng mã, v.v.
- Ngoài ra, Maven có thể tự động sinh tài liệu API từ mã nguồn, giúp người dùng dễ dàng duy trì tài liệu cho dự án.

6. **Khả năng mở rộng (Extensibility):**

- Maven có thể được mở rộng thông qua các plugin, cho phép người dùng thêm các tính năng tùy chỉnh. Các plugin có thể thực hiện mọi thứ từ xây dựng và kiểm thử, đến tạo tài liệu, triển khai ứng dụng, v.v.
- Ngoài các plugin có sẵn, cộng đồng Maven cũng phát triển rất nhiều plugin hỗ trợ các tính năng đặc biệt.

7. **Khả năng tái sử dụng (Reusability):**
- Một tính năng mạnh mẽ của Maven là khả năng tái sử dụng cấu hình và các plugin trong nhiều dự án khác nhau. Các dự án con có thể chia sẻ các cấu hình và phụ thuộc chung thông qua các "parent projects" trong Maven.

---

# 🔍 Cách sử dụng Maven
Để minh họa việc sử dụng Maven, mình sẽ sử dụng môi trường phát triển tích hợp IntelliJ IDEA để xây dựng dự án **"Hello World"** huyền thoại!

> [!info] Lưu ý
> - **Maven** được tích hợp sẵn trong IntelliJ IDEA nên bạn chỉ cần mở dự án Maven trong IDEA, và nó sẽ tự động nhận diện tệp `pom.xml` và cung cấp giao diện người dùng để quản lý phụ thuộc, xây dựng, và kiểm tra dự án.
> - Giao diện của IntelliJ IDEA ở mỗi phiên bản có thể khác nhau đôi chút! Nên hãy cố gắng hiểu tư tưởng của các bước dưới đây.

> [!question]- Nếu dùng Maven CLI thì sao?
> Các bước sẽ tương tự nhưng bạn phải thực hiện thủ công qua các dòng lệnh. Xem thêm tại bài viết [này](https://www.geeksforgeeks.org/maven-commands-and-options/)

## Cài đặt IntelliJ IDEA ⬇️

1. **Tải IntelliJ IDEA**: Tải và cài đặt IntelliJ IDEA từ [trang chủ của JetBrains](https://www.jetbrains.com/idea/download/).

2. **Cài đặt Maven**: IntelliJ IDEA thường đã tích hợp sẵn Maven, vì vậy bạn không cần phải cài đặt riêng. Tuy nhiên, nếu cần, bạn có thể cài đặt Maven theo hướng dẫn trên trang [Maven website](https://maven.apache.org/download.cgi).

## Tạo một dự án Maven mới 📂

1. **Mở IntelliJ IDEA** và chọn **Create New Project**.

2. Trong cửa sổ **New Project**, chọn **Maven** ở mục **Project SDK** và nhấn **Next**.
    - Nếu bạn chưa cài JDK, bạn có thể tải xuống từ trang [Oracle](https://www.oracle.com/java/technologies/javase-jdk11-downloads.html) hoặc sử dụng OpenJDK.

3. Chọn **Create from Archetype** (chọn mẫu) nếu bạn muốn sử dụng mẫu dự án Maven có sẵn. Nếu không, bỏ qua bước này và tiếp tục.

4. Đặt **GroupId** và **ArtifactId** cho dự án của bạn:
    - **GroupId**: Được sử dụng để phân loại các nhóm dự án. Ví dụ: `com.example`.
    - **ArtifactId**: Tên của dự án hoặc ứng dụng. Ví dụ: `my-maven-project`.

5. Chọn vị trí lưu trữ cho dự án và nhấn **Finish**.

> [!info]- Cấu trúc thư mục chuẩn của một dự án Maven


## Cấu hình Maven trong dự án ⚙️

1. **Tạo tệp `pom.xml`**: IntelliJ IDEA sẽ tự động tạo một tệp `pom.xml` cho bạn trong thư mục gốc của dự án. Tệp này là nơi bạn định nghĩa các phụ thuộc (dependencies), plugin và thông tin cấu hình khác cho Maven.

Một tệp `pom.xml` cơ bản sẽ trông như sau:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.example</groupId>
    <artifactId>my-maven-project</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>jar</packaging>

    <dependencies>
        <!-- Add dependencies here -->
    </dependencies>
</project>
```

## Thêm phụ thuộc vào `pom.xml` 📦

1. Mở tệp `pom.xml`.

2. Bạn có thể thêm các phụ thuộc (thư viện cần thiết) vào trong thẻ `<dependencies>`. Ví dụ, để thêm thư viện `JUnit` (dùng cho kiểm thử), bạn có thể thêm đoạn sau vào tệp `pom.xml`:

```xml
<dependencies>
    <!-- JUnit dependency -->
    <dependency>
        <groupId>junit</groupId>
        <artifactId>junit</artifactId>
        <version>4.13.2</version>
        <scope>test</scope>
    </dependency>
</dependencies>

```
   
3. Khi bạn lưu tệp `pom.xml`, Maven sẽ tự động tải xuống các phụ thuộc này từ kho **Maven Central**.

## Tạo mã nguồn 📝

1. **Tạo thư mục `src/main/java`**: Tạo thư mục con trong thư mục gốc của dự án để chứa mã nguồn chính của bạn:
	- `src/main/java/com/example/`
	- Tạo một lớp Java đơn giản, ví dụ `App.java`:

```java
package com.example;

public class App {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

## Xây dựng và chạy dự án Maven 🏗️

1. **Chạy Maven Build**:
    - Mở cửa sổ **Maven Tool Window** trong IntelliJ IDEA bằng cách vào **View > Tool Windows > Maven**.
    - Bạn có thể chạy lệnh `clean`, `install` hoặc `package` để xây dựng ứng dụng của mình. Ví dụ:
        - **clean**: Dọn dẹp các tệp xây dựng cũ.
        - **install**: Xây dựng dự án và cài đặt vào kho cục bộ.
        - **package**: Đóng gói ứng dụng thành một JAR/WAR.

2. **Chạy ứng dụng**: Trong IntelliJ IDEA, bạn có thể chạy ứng dụng Java trực tiếp bằng cách nhấp chuột phải vào tệp `App.java` và chọn **Run 'App'**.    

## Kiểm tra trong Maven Tool Window 🔎

- Sau khi chạy lệnh `clean install`, bạn có thể kiểm tra kết quả trong phần **Maven Tool Window**.
- Maven sẽ tạo ra các tệp `target/` chứa các bản dựng của ứng dụng (như `my-maven-project-1.0-SNAPSHOT.jar`).

## Kiểm tra hoạt động của ứng dụng 📱

Sau khi xây dựng thành công, bạn có thể kiểm tra đầu ra của ứng dụng trong tab **Run** của IntelliJ IDEA. Nếu mọi thứ được cấu hình đúng, bạn sẽ thấy dòng **"Hello, World!"** in ra màn hình.

Với các bước trên, bạn đã hoàn thành việc tạo một dự án Java sử dụng Maven trong IntelliJ IDEA. Maven giúp bạn quản lý phụ thuộc và quy trình xây dựng dự án một cách dễ dàng, đồng thời giúp dự án của bạn dễ bảo trì và mở rộng hơn trong tương lai.

---

# 👀 Các công cụ tương tự Maven
**Maven** là một trong những lựa chọn phổ biến và mạnh mẽ nhất trong phát triển ứng dụng Java, nhưng nó không phải là lựa chọn duy nhất. Quyết định chọn **Maven** hay một công cụ xây dựng khác (như Gradle, Ant, v.v.) tùy thuộc vào yêu cầu và sở thích của dự án. Dưới đây là các thông tin bạn có thể cân nhắc khi lựa chọn cho dự án Java của mình:

|                      Tên công cụ                      | Mô tả                                                                                                                                                                                                                                                                                                | Ưu điểm                                                                                                                                                     |
|:-----------------------------------------------------:| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
|             [Gradle](https://gradle.org/)             | **Gradle** một công cụ xây dựng hiện đại, mạnh mẽ và linh hoạt, hỗ trợ cả Java và nhiều ngôn ngữ khác. Nó sử dụng một DSL (Domain-Specific Language) dựa trên Groovy hoặc Kotlin để định nghĩa quy trình xây dựng. Gradle nhanh và có khả năng tùy chỉnh cao hơn Maven, đặc biệt là trong các dự án lớn. | Tùy chỉnh cao, thời gian xây dựng nhanh nhờ tính năng caching và parallel execution.                                                                        |
|            [Ant](https://ant.apache.org/)             | **Ant** là một công cụ xây dựng rất linh hoạt và được sử dụng rộng rãi trong cộng đồng Java. Khác với Maven, Ant không có khái niệm về phụ thuộc tự động, mà bạn phải tự định nghĩa các quy trình và nhiệm vụ.                                                                                           | Linh hoạt, dễ dàng cấu hình với các dự án có yêu cầu đặc thù.                                                                                               |
|      [Apache Buildr](https://buildr.apache.org/)      | **Buildr** là một công cụ xây dựng cho Java và các dự án JVM khác. Nó sử dụng Ruby để định nghĩa quy trình xây dựng thay vì XML như Maven.                                                                                                                                                               | Cấu hình đơn giản, dễ sử dụng, hỗ trợ các dự án đa ngôn ngữ.                                                                                                |
| [SBT (Simple Build Tool)](https://www.scala-sbt.org/) | **SBT** là công cụ xây dựng chủ yếu dành cho các dự án Scala, nhưng cũng hỗ trợ tốt cho Java. SBT sử dụng Scala để định nghĩa các tác vụ và quy trình xây dựng.                                                                                                                                          | SBT là công cụ xây dựng chủ yếu dành cho các dự án Scala, nhưng cũng hỗ trợ tốt cho Java. SBT sử dụng Scala để định nghĩa các tác vụ và quy trình xây dựng. |
|             [Grav](https://getgrav.org/)              | **Grav** là công cụ xây dựng mới hơn, nhẹ và dễ sử dụng. Nó hỗ trợ đa ngôn ngữ, nhưng có thể được sử dụng cho các dự án Java với các plugin phù hợp.                                                                                                                                                     | Cấu hình đơn giản, dễ dàng tích hợp vào các dự án Java nhỏ.                                                                                                 |

# 🔥 Tổng kết

Maven là một công cụ mạnh mẽ giúp quản lý và xây dựng các dự án Java. Nó hỗ trợ quản lý phụ thuộc, xây dựng tự động, và kiểm thử, đồng thời cung cấp một cấu trúc và quy trình chuẩn để phát triển phần mềm hiệu quả

> [!question]- Tại sao nên sử dụng Maven?
> - **Quản lý phụ thuộc dễ dàng**: Maven tự động tải các thư viện cần thiết, giảm bớt việc quản lý thủ công.
> - **Tính nhất quán**: Các dự án Maven đều tuân theo cấu trúc thư mục chuẩn, giúp dễ dàng làm việc với nhiều dự án.
> - **Tích hợp kiểm thử**: Tích hợp sẵn các công cụ kiểm thử, giúp tự động hóa quy trình kiểm tra phần mềm.
> - **Tính mở rộng**: Maven có một hệ sinh thái plugin phong phú và có thể được mở rộng để phục vụ nhiều mục đích khác nhau.
