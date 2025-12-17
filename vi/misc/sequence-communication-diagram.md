---
stage: Publish
draft: false
title: Biểu đồ tuần tự và giao tiếp
description:
tags:
  - analysis-and-design
  - sequence-diagram
  - communication-diagram
  - interaction-diagram
  - modeling-language
socialDescription:
socialImage:
permalink:
lang:
aliases:
cssclasses:
---
## Biểu đồ tương tác ✍️

Biểu đồ tương tác (Interaction Diagrams) là công cụ giúp chúng ta **mô tả cách các đối tượng trong hệ thống giao tiếp với nhau thông qua việc trao đổi thông điệp**.  
👉 Nói cách khác, nó trả lời câu hỏi:
- Khi thực hiện một chức năng nào đó, đối tượng nào nói chuyện với đối tượng nào?
- Thứ tự diễn ra như thế nào?

Trong UML, có hai loại biểu đồ tương tác chính:
1. **Biểu đồ tuần tự (Sequence Diagram)**: tập trung vào **thứ tự thời gian** của các thông điệp.
2. **Biểu đồ giao tiếp (Communication Diagram)**: tập trung vào **cấu trúc quan hệ** giữa các đối tượng.

💡 Hãy tưởng tượng bạn gọi đồ ăn trên một app giao hàng. Các đối tượng có thể là: Người dùng (bạn), Ứng dụng đặt đồ ăn, Nhà hàng, Shipper, ... Các biểu đồ tương tác sẽ mô tả các tương tác bên trong từng giai đoạn. Từ lúc bạn gửi yêu cầu → app xử lý → nhà hàng nhận đơn → shipper đi giao → bạn nhận đồ.

## Biểu đồ tuần tự 

Biểu đồ tuần tự (Sequence Diagram) cho thấy **trình tự gửi và nhận thông điệp giữa các đối tượng theo dòng thời gian**.

Thành phần chính:
- **Đối tượng (Object / Actor):** được vẽ ở đầu với tên mô tả rõ ràng.
- **Thanh sống (Lifeline):** đường thẳng đứng biểu diễn sự tồn tại của đối tượng theo thời gian.
- **Thông điệp (Message):** mũi tên thể hiện việc gọi phương thức/hành động.
- **Thanh hoạt động (Activation Bar):** khối chữ nhật nhỏ trên lifeline, biểu thị khoảng thời gian mà đối tượng đang thực hiện hành động.

%% ảnh ví dụ về 1 biểu đồ tuần tự đầy đủ  %%

Ưu điểm:
- Giúp hiểu rõ **thứ tự thực hiện**.
- Thích hợp khi cần diễn giải các ca sử dụng phức tạp.


> [!example] Ví dụ
> Trong ca sử dụng "Đăng nhập hệ thống":
> 1. Người dùng → gửi yêu cầu đăng nhập đến Ứng dụng.
> 2. Ứng dụng → gửi thông tin đến CSDL để kiểm tra.
> 3. CSDL → trả kết quả cho Ứng dụng.
> 4. Ứng dụng → thông báo thành công/thất bại cho Người dùng.

## Biểu đồ giao tiếp 

Biểu đồ giao tiếp (Communication/Collaboration Diagram) thể hiện **cấu trúc quan hệ giữa các đối tượng** và cách chúng gửi thông điệp cho nhau.

Thành phần chính:
- **Đối tượng (Object / Actor):** vẽ dưới dạng hình chữ nhật.
- **Liên kết (Link):** đường nối giữa các đối tượng (có thể là ).
- **Thông điệp:** mũi tên kèm số thứ tự (1, 1.1, 2...) để thể hiện trình tự.

%% ảnh ví dụ về 1 biểu đồ giao tiếp đầy đủ  %%

Ưu điểm:
- Nhấn mạnh vào **quan hệ tĩnh giữa các đối tượng**.
- Dễ nhìn ra các **liên kết** cần thiết trong hệ thống.

> [!example] Ví dụ
> Trong ca sử dụng "Đặt vé máy bay", Người dùng ↔ Ứng dụng đặt vé ↔ Hệ thống thanh toán ↔ Hãng hàng không. Thông điệp có thể là:
> 1. Người dùng gửi yêu cầu đặt vé.
> 2. Ứng dụng liên hệ hệ thống thanh toán.
> 3. Hệ thống thanh toán gửi xác nhận đến Hãng hàng không.
> 4. Kết quả trả về cho Người dùng.

## Mô hình hóa với biểu đồ tương tác 📊

Trong thực tế, khi mô hình hóa hệ thống bằng UML:
- Người phân tích thường **kết hợp cả hai loại biểu đồ**.
- Biểu đồ tuần tự giúp thấy rõ **thứ tự thực hiện**.
- Biểu đồ giao tiếp giúp thấy rõ **quan hệ giữa các đối tượng**.

👉 Quy trình thường là:
1. Lấy một ca sử dụng (Use Case).
2. Xác định các đối tượng tham gia.
3. Vẽ biểu đồ tuần tự để mô tả luồng sự kiện.
4. Vẽ biểu đồ giao tiếp để kiểm tra mối liên hệ giữa các đối tượng.

> [!tip]- Mẹo
> - Dùng **biểu đồ tuần tự** khi bạn muốn kể lại "chuyện gì xảy ra trước - sau".
> - Dùng **biểu đồ giao tiếp** khi bạn muốn nhìn "ai kết nối với ai".

## Tổng kết 🎬

Biểu đồ tương tác là **cầu nối** giữa phân tích và thiết kế hệ thống. Nó cho chúng ta hình dung trực quan:
- Ai tham gia (Actor, Object).
- Họ nói chuyện với nhau ra sao (Message).
- Thứ tự và mối quan hệ như thế nào (Sequence & Communication).

Nếu ví hệ thống phần mềm là một bộ phim 📽️ thì:
- **Biểu đồ tuần tự** giống như kịch bản chi tiết từng cảnh quay.
- **Biểu đồ giao tiếp** giống như sơ đồ quan hệ giữa các nhân vật trong phim.
