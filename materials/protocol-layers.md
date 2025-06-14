---
date: 2025-02-13
draft: false
status: Doing
title: "Hiểu Về Lớp Giao Thức và Mô Hình Dịch Vụ Trong Mạng Máy Tính"
description: ""
author: PhDoanh
authorlink: https://github.com/PhDoanh
tags: 
  - "computer-network"
  - internet
aliases:
  - "protocol layers"
cssclasses:
  - img
  - btn
---
%% ĐỊNH DẠNG TÊN FILE: "tên-bài-viết" | VD: jp-typing-guide %%

%% <figure style="text-align: center; margin: 20px auto;">
  <img 
    src="images/protocol-layers.png"
    alt="Hiểu Về Lớp Giao Thức và Mô Hình Dịch Vụ Trong Mạng Máy Tính" 
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

Mạng Internet là một hệ thống phức tạp với nhiều thành phần như ứng dụng, giao thức, thiết bị đầu cuối, bộ chuyển mạch gói và phương tiện truyền dẫn. Để đơn giản hóa sự phức tạp này, người ta áp dụng mô hình **phân lớp (layered architecture)** giúp tổ chức mạng theo từng tầng có chức năng riêng biệt.

Hãy tưởng tượng hệ thống vận hành của một hãng hàng không ✈️. Khi bạn di chuyển bằng máy bay:

1. Bạn mua vé 🏷️.

2. Kiểm tra hành lý 🎒.
  
3. Lên máy bay ✈️.

4. Máy bay cất cánh, di chuyển theo tuyến đường hàng không 🛤️.
  
5. Máy bay hạ cánh, bạn nhận lại hành lý và ra khỏi sân bay 🎫.

Mỗi giai đoạn trong quá trình trên tương tự như một **tầng giao thức** trong mạng máy tính. Điều này giúp quản lý hệ thống phức tạp theo từng phần chức năng riêng biệt.

# 📚 Mô hình phân lớp trong mạng Internet 

Trong mô hình phân lớp, mỗi tầng thực hiện một chức năng cụ thể và cung cấp dịch vụ cho tầng phía trên nó. Các tầng giao thức có thể được triển khai dưới dạng phần mềm, phần cứng hoặc kết hợp cả hai.

> [!example]- Ví dụ
> Tầng ứng dụng như HTTP hoặc SMTP thường được triển khai bằng phần mềm, trong khi tầng vật lý và tầng liên kết dữ liệu thường có sự hỗ trợ của phần cứng như card mạng Ethernet hoặc WiFi.

Mạng Internet sử dụng **mô hình phân lớp gồm 5 tầng** như sau:

- **Tầng ứng dụng (Application Layer):** Xử lý giao tiếp giữa ứng dụng mạng, như trình duyệt web hoặc email. 

- **Tầng giao vận (Transport Layer):** Cung cấp giao tiếp dữ liệu giữa hai điểm cuối, ví dụ như TCP và UDP. 

- **Tầng mạng (Network Layer):** Định tuyến gói tin giữa các thiết bị trong mạng, sử dụng giao thức như IP. 

- **Tầng liên kết dữ liệu (Link Layer):** Điều khiển truyền dữ liệu giữa hai thiết bị lân cận, ví dụ như Ethernet hoặc WiFi. 

- **Tầng vật lý (Physical Layer):** Chịu trách nhiệm truyền tín hiệu điện hoặc quang qua phương tiện truyền dẫn.

> [!info] Lưu ý
> Bên cạnh mô hình 5 tầng của Internet, còn có mô hình **OSI 7 tầng**, bổ sung thêm tầng phiên (Session) và tầng trình bày (Presentation) để xử lý dữ liệu chuyên sâu hơn.

---

# 📦 Kỹ thuật đóng gói dữ liệu (Encapsulation)

Một khía cạnh quan trọng của phân lớp là kỹ thuật **đóng gói dữ liệu**. Khi dữ liệu truyền đi trong mạng, mỗi tầng sẽ thêm thông tin điều khiển vào dữ liệu gốc để đảm bảo quá trình truyền tải đúng cách.

> [!example]- Ví dụ
> - Tầng ứng dụng tạo ra một **thông điệp (message)** 📩.
> - Tầng giao vận đóng gói thông điệp thành một **đoạn tin (segment)** 📦.
> - Tầng mạng tiếp tục đóng gói thành **gói tin (packet/datagram)** 📜.
> - Tầng liên kết dữ liệu thêm thông tin để tạo **khung (frame)** 🏗️.
> - Cuối cùng, tầng vật lý chuyển đổi thành tín hiệu điện hoặc quang 📡.
> 
> Khi đến đích, quá trình này sẽ diễn ra theo chiều ngược lại để khôi phục dữ liệu ban đầu.

---

# ⚖️ Ưu điểm và nhược điểm của mô hình phân lớp

> [!check] Ưu điểm
> - **Tính modular (mô-đun hóa):** Dễ dàng sửa đổi hoặc nâng cấp từng tầng mà không ảnh hưởng đến các tầng khác.
> - **Tính trừu tượng:** Người dùng chỉ cần làm việc với tầng giao thức liên quan thay vì toàn bộ hệ thống. 
> - **Tính tương thích:** Hỗ trợ nhiều loại thiết bị và giao thức khác nhau, giúp Internet mở rộng dễ dàng.

> [!missing] Nhược điểm
> - **Trùng lặp chức năng:** Một số chức năng có thể bị lặp lại giữa các tầng (ví dụ: kiểm tra lỗi ở cả tầng liên kết dữ liệu và tầng giao vận).
> - **Thiếu tối ưu hóa:** Tách biệt các tầng có thể làm giảm hiệu suất khi cần tối ưu hóa toàn diện hệ thống mạng.

---

# 🎯 Tổng kết
Mô hình phân lớp là một cách tiếp cận mạnh mẽ để tổ chức và quản lý hệ thống mạng phức tạp như Internet. Nó giúp chia nhỏ các chức năng, tạo sự linh hoạt trong thiết kế và triển khai. Tuy nhiên, cũng cần cân nhắc các hạn chế để tối ưu hiệu suất mạng.
