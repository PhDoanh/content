---
stage: Publish
draft: false
title: Biểu đồ triển khai
description:
tags:
  - OOAD
  - deployment-diagram
  - UML
  - physical-view
socialDescription:
socialImage:
permalink:
lang: vi
aliases:
cssclasses:
  - img
---
## Khái niệm cơ sở ✍️

Biểu đồ triển khai (Deployment Diagram) trong UML là loại **biểu đồ cấu trúc** dùng để mô tả:
- **Cấu hình phần cứng** (hardware configuration): tức là các **nút (nodes)** như máy chủ, máy trạm, thiết bị di động, cảm biến, router…
- **Cách phần mềm được triển khai** lên các phần tử phần cứng đó: ví dụ ứng dụng web được cài trên server A, cơ sở dữ liệu trên server B, còn app mobile chạy trên smartphone của người dùng.

👉 Nói ngắn gọn: biểu đồ triển khai trả lời câu hỏi **"Hệ thống phần mềm sẽ chạy trên đâu và các thành phần kết nối như thế nào?"**

## Các thành phần chính 🧩

Trong UML, biểu đồ triển khai có những phần tử cơ bản:
- **Nút (Node):** Đại diện cho tài nguyên vật lý hoặc môi trường thực thi. Ví dụ: Server, Máy tính cá nhân, Điện thoại di động, Thiết bị IoT (cảm biến nhiệt độ, camera IP…)
- **Thành phần (Component):** Là các phần mềm, chương trình, module chạy trong nút đó. Ví dụ: Trên server có Web Server (Apache, Nginx), Trên smartphone có ứng dụng Android/iOS
- **Đường kết nối (Association/Communication Path):** Mô tả kênh truyền thông giữa các nút. Ví dụ: HTTP/HTTPS kết nối giữa client và server, JDBC kết nối từ ứng dụng đến cơ sở dữ liệu
- **Artifact (chế tác):** Là sản phẩm phần mềm cụ thể (file .exe, .war, .jar, script…) được triển khai vào node. Được thể hiện bằng kí hiệu «artifact»

%% ![[Pasted image 20250919154740.png]] %%

## Mô hình hóa các bộ xử lý và các thiết bị 🖨️

UML cung cấp cơ chế **mở rộng (stereotype)** để mô tả rõ hơn từng loại **nút (node)** trong biểu đồ triển khai. Có hai loại nút chính:
- **Nút xử lý (processor):** có khả năng tính toán, thực thi các thành phần phần mềm (ví dụ CPU, server).

- **Nút thiết bị (device):** không trực tiếp xử lý, thường đại diện cho các phần cứng có chức năng giao tiếp với thế giới thực qua giao diện (ví dụ máy in, cảm biến, thiết bị ngoại vi).

%% ![[Pasted image 20250919160042.png]] %%

Các bước mô hình hóa:
1. **Xác định** các phần tử tính toán trong hệ thống, rồi biểu diễn chúng dưới dạng các **nút**.
2. **Gán stereotype** để phân biệt đó là **bộ xử lý** hay **thiết bị**.
3. **Xem xét** các thuộc tính và thao tác đã được cài đặt trên các nút khi mô hình hóa lớp (đảm bảo tính nhất quán giữa thiết kế logic và triển khai vật lý).

## Mô hình hóa sự phân tán của các thành phần 🖧

%% ![[Pasted image 20250919160106.png]] %%

Sau khi đã xác định các nút, ta cần mô tả cách các **thành phần phần mềm** được phân bố trên các nút đó. Các bước mô hình hóa:

1. Với mỗi thành phần của hệ thống, **gán nó vào một nút xử lý** cụ thể.
2. **Xem xét khả năng nhân bản** (sao chép) thành phần trên nhiều vị trí khác nhau.
    - Thông thường chỉ các thành phần cùng loại (ví dụ thư viện phần mềm) mới được phân bố trên nhiều nút.
    - Ít khi cùng một thành phần được tách nhỏ và lưu trú ở nhiều nút đồng thời.
3. Có ba cách để biểu diễn sự phân bố này trong UML:
    - Cách 1: Đưa trực tiếp vào phần đặc tả của nút (mô tả bằng văn bản, không cần hình vẽ).
    - Cách 2: Sử dụng **quan hệ phụ thuộc (dependency)** để nối mỗi nút với thành phần được triển khai trên nó.
    - Cách 3: Liệt kê các thành phần triển khai trong một **ngăn mở rộng** bên trong ký pháp nút (cách này trực quan, dễ đọc).

## Ý nghĩa và mục đích 🔥
Biểu đồ triển khai giúp:
1. **Mô tả kiến trúc triển khai thực tế** của hệ thống, gắn liền giữa phần mềm và hạ tầng.
2. **Hiểu rõ sự phụ thuộc phần cứng – phần mềm**, từ đó đưa ra quyết định về hiệu năng, bảo mật, khả năng mở rộng.
3. **Hỗ trợ quản lý triển khai và bảo trì hệ thống**, đặc biệt với các hệ thống phân tán, cloud, IoT.

👉 Đặc biệt quan trọng trong các dự án lớn (ERP, e-commerce, AIoT y tế…) khi cần triển khai trên nhiều server, cloud khác nhau.

## Ví dụ minh họa 📦
Giả sử ta triển khai một **ứng dụng bán hàng trực tuyến**:
- **Client:** người dùng truy cập bằng trình duyệt hoặc ứng dụng mobile.
- **Web Server:** chạy ứng dụng web (Apache + ứng dụng Java).
- **Database Server:** lưu trữ dữ liệu khách hàng, đơn hàng.
- **Payment Gateway (bên thứ ba):** xử lý giao dịch thanh toán.

Trong biểu đồ triển khai UML, ta có thể vẽ:
- Một node "Web Server" chứa artifact "E-commerce.war"
- Một node "Database Server" chứa "MySQL DB"
- Một node "Mobile Device" chứa "ShoppingApp.apk"
- Các đường kết nối: HTTPS giữa client ↔ web server, JDBC giữa web server ↔ DB, API giữa web server ↔ payment gateway.

%% image %%

## Kết luận ✨

- Biểu đồ triển khai là "cầu nối" giữa **thiết kế phần mềm** và **hạ tầng phần cứng**.
- Nó giúp đội ngũ phát triển và vận hành (DevOps, SysAdmin) phối hợp tốt hơn.
- Với xu hướng **Cloud Computing** và **IoT**, biểu đồ triển khai ngày càng quan trọng để mô tả hệ thống phân tán, đa nền tảng.
