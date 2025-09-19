---
stage: Publish
draft: false
title: Biểu đồ thành phần
description:
tags:
  - OOAD
  - UML
  - component-diagram
  - physical-view
socialDescription:
socialImage:
permalink:
lang: vi
aliases:
cssclasses:
  - img
---
Nếu ví phần mềm như một căn nhà thì [[class-object-diagram|biểu đồ lớp (class diagram)]] giống như bản vẽ chi tiết từng phòng (lớp, thuộc tính, quan hệ), còn **biểu đồ thành phần (component diagram)** thì giống như bản sơ đồ **các khối module lớn**: phòng khách, nhà bếp, nhà vệ sinh, và cách chúng kết nối với nhau bằng cửa hoặc hành lang.

Nói cách khác, UML cung cấp **biểu đồ thành phần** để mô tả **cấu trúc vật lý của hệ thống phần mềm**, tức là cách hệ thống được chia thành **các module/thành phần** và **mối quan hệ phụ thuộc giữa chúng**.

# Khái niệm cơ bản ✍️

- **Thành phần (component)** trong UML là một **khối mô-đun** độc lập, đại diện cho một phần của hệ thống. Nó có thể là:
    - Một gói thư viện (library).
    - Một file mã nguồn/nhị phân.
    - Một dịch vụ web.
    - Một module phần mềm lớn.

- **Biểu đồ thành phần (component diagram)** dùng để:
    - Mô hình hóa **cấu trúc thực thi của hệ thống**.
    - Thể hiện cách các thành phần **phụ thuộc, liên kết, hoặc giao tiếp** với nhau.
    - Giúp nhóm phát triển hiểu rõ **kiến trúc triển khai phần mềm**.

👉 Điểm thú vị: thành phần **không phải lớp**, nhưng có thể **chứa nhiều lớp, giao diện hoặc tài nguyên** bên trong.

# Ký hiệu trong UML 🧩

Trong UML, ký hiệu **component** thường được biểu diễn như **hình chữ nhật có 2 "tai" nhỏ** ở bên trái (trông giống một tài liệu có tab), thường nằm ở góc trên bên phải của một hình chữ nhật lớn hơn, hình chữ nhật này được dùng để mô tả tên và/hoặc cấu trúc bên trong của thành phần

%% ![[Pasted image 20250919151655.png]] %%

Ngoài ra, UML còn cho phép:
- **Interface (giao diện)** được vẽ bằng vòng tròn (lollipop) hoặc đường kẻ gắn vào component.
- **Dependency (phụ thuộc)** được vẽ bằng mũi tên nét đứt từ component này đến component khác.

%% ![[Pasted image 20250919153233.png]] %%

# Các mối quan hệ trong biểu đồ thành phần 🔗

Trong Component Diagram, có một số quan hệ quan trọng:
1. **Quan hệ sử dụng (usage dependency)**
    - Một component **cần dịch vụ** từ component khác.
    - Vẽ bằng mũi tên nét đứt.
    - Ví dụ: `Payment Module` phụ thuộc vào `User Auth Module`.

2. **Quan hệ giao diện (interface relationship)**
    - Một component **cung cấp** hoặc **yêu cầu** giao diện.
    - Biểu diễn bằng hình tròn (provided interface) hoặc hình ổ cắm (required interface).
    - Ví dụ: `Payment Module` cung cấp interface `IPayment`, `E-Commerce App` sử dụng interface này.

# Mô hình hóa các thực thi được (executables) và các thư viện ⚙️

Biểu đồ thành phần thường được dùng để mô hình hóa **các đơn vị triển khai** làm nên bản cài đặt của hệ thống, ví dụ như **các file thực thi (.exe)** hoặc **các thư viện đối tượng (.dll, .so, .jar, …)**.

Việc mô hình hóa thành phần cho phép chúng ta:
- **Trực quan hóa** cấu trúc hệ thống ở mức vật lý.
- **Đặc tả chi tiết** các thành phần phần mềm.
- **Xây dựng và đưa ra quyết định** về việc tổ chức, tích hợp và triển khai hệ thống.
- **Quản lý cấu hình và bảo trì** hệ thống tốt hơn trong suốt vòng đời.

%% ![[Pasted image 20250919152816.png]] %%

Các bước tiến hành:
1. **Xác định sự phân chia của hệ thống vật lý.**
    - Xem xét các yếu tố về quản lý cấu hình, ràng buộc kỹ thuật và vấn đề tái sử dụng.
    - Ví dụ: phần mềm có thể chia thành các module như "xử lý dữ liệu", "giao diện người dùng", "truy cập cơ sở dữ liệu".

2. **Biểu diễn các thực thi được hoặc các thư viện ở dạng thành phần.**
    - Trong một số trường hợp, dùng **stereotype** (kiểu mở rộng) để làm rõ ý nghĩa đặc thù của từng thành phần.
    - Ví dụ: đánh dấu một thành phần là «executable» hay «library».

3. **Xác định các giao diện thiết yếu** mà thành phần sử dụng hoặc hiện thực hóa.
    - Điều này giúp làm rõ cách các thành phần trao đổi với nhau.

4. **Mô hình hóa quan hệ giữa các thực thi, thư viện và giao diện.**
    - Đặc biệt nhấn mạnh vào **các mối quan hệ phụ thuộc** giữa chúng (dependency).
    - Ví dụ: chương trình chính (executable) phụ thuộc vào thư viện toán học để xử lý phép tính.

# Mô hình hóa các bảng, tệp, tài liệu 📂

Ngoài việc mô hình hóa các file thực thi và thư viện, chúng ta còn có thể dùng **biểu đồ thành phần** để mô tả **các phần tử không thực thi được** của hệ thống, gọi là **các thành phần phụ**, ví dụ:

- Các **bảng dữ liệu** trong cơ sở dữ liệu.
- Các **tập tin** (files).
- Các **tài liệu trợ giúp** (documentation, manuals).

%% ![[Pasted image 20250919152924.png]] %%

Ý nghĩa:
- Đây là một phần quan trọng trong **quản lý cấu hình**.
- Chúng ta cần chỉ ra **quan hệ phụ thuộc** giữa các thành phần thực thi và các thành phần phụ. Ví dụ: một chương trình quản lý sinh viên phụ thuộc vào bảng “SinhVien” trong cơ sở dữ liệu.

Ngoài ra, biểu đồ thành phần còn có thể được dùng trong các tình huống khác như:
- Mô hình hóa **các API (Application Programming Interface)**.
- Mô hình hóa **mã nguồn chương trình**.

# Vai trò của biểu đồ thành phần 🎯

Biểu đồ thành phần đóng vai trò **rất quan trọng trong giai đoạn thiết kế và triển khai**:
- Giúp xác định rõ **các khối kiến trúc chính**.
- Hỗ trợ **tái sử dụng** thành phần: ví dụ, module `Login` có thể dùng lại trong nhiều ứng dụng khác.
- Cho phép kiểm soát **phụ thuộc giữa các module**, hạn chế việc hệ thống bị "rối dây".
- Là tài liệu để giao tiếp giữa **kiến trúc sư hệ thống** và **lập trình viên**, đảm bảo mọi người hiểu đúng cách các module kết nối với nhau.

# Ví dụ minh họa 🛒

Hãy tưởng tượng bạn xây dựng một hệ thống **Thương mại điện tử (E-Commerce System)**.  
Biểu đồ thành phần có thể gồm các module chính:
- `User Management Component`
- `Product Catalog Component`
- `Shopping Cart Component`
- `Payment Component`
- `Notification Component`

Quan hệ:
- `Shopping Cart` phụ thuộc vào `Product Catalog` (để lấy thông tin sản phẩm).
- `Payment` cung cấp interface `IPayment`, được `Shopping Cart` gọi khi khách hàng thanh toán.
- `Notification` nhận sự kiện từ `Payment` để gửi email xác nhận.

%% image %%

# Tổng kết 🔥

- **Biểu đồ thành phần (Component Diagram)** cho ta cái nhìn **"vĩ mô"** về cấu trúc hệ thống.
- Nó giúp quản lý **sự phức tạp** trong các dự án phần mềm lớn bằng cách **chia nhỏ hệ thống thành các module rõ ràng**.
- Khi kết hợp với [[deployment-diagram|biểu đồ triển khai (Deployment Diagram)]], chúng ta có thể biết **một component sẽ chạy trên node nào**, đảm bảo hệ thống được triển khai hợp lý.