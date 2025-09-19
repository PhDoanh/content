---
stage: Draft
draft: true
title: Biểu đồ trạng thái
description:
tags:
  - OOAD
  - state-diagram
  - finite-state-machine
socialDescription:
socialImage:
permalink:
lang: vi
aliases:
cssclasses:
  - img
---
Biểu đồ trạng thái là một trong những biểu đồ quan trọng của UML, được dùng để **mô hình hóa vòng đời (lifecycle) của một đối tượng** trong hệ thống. Nó cho ta thấy:

- Một đối tượng có thể **ở những trạng thái nào** trong suốt vòng đời.
- Những **sự kiện (event)** nào sẽ làm đối tượng chuyển từ trạng thái này sang trạng thái khác.
- Các **hoạt động (action)** xảy ra khi chuyển trạng thái.

👉 Bạn có thể hình dung biểu đồ trạng thái như một "bản đồ hành trình cuộc đời" của một đối tượng.

> [!example] Ví dụ
> - Một đơn hàng online 📦 có thể trải qua các trạng thái: _Được tạo_ → _Đang xử lý_ → _Đang giao_ → _Hoàn thành_ hoặc _Hủy bỏ_.
> - Những sự kiện như _Khách hàng xác nhận_, _Hệ thống duyệt thanh toán_, _Shipper giao thành công_ chính là các **event** dẫn đến thay đổi trạng thái.

# Khái niệm cơ sở cho biểu đồ trạng thái 🌀

Biểu đồ trạng thái được xây dựng dựa trên khái niệm **máy trạng thái hữu hạn (Finite State Machine – FSM)**.  
Trong đó:

- **Trạng thái (State):** Tình huống tại một thời điểm cụ thể mà đối tượng đang ở.

- **Sự kiện (Event):** Một kích hoạt (trigger) làm thay đổi trạng thái.

- **Chuyển trạng thái (Transition):** Mũi tên thể hiện việc di chuyển từ trạng thái này sang trạng thái khác khi có sự kiện xảy ra.

- **Hoạt động (Action):** Công việc được thực hiện ngay khi xảy ra chuyển trạng thái.

- **Trạng thái bắt đầu (Initial state):** Nơi vòng đời bắt đầu.

- **Trạng thái kết thúc (Final state):** Nơi vòng đời chấm dứt.

✨ Điểm mạnh của biểu đồ trạng thái:
- Mô tả trực quan vòng đời đối tượng.
- Giúp phát hiện những tình huống chưa lường trước (ví dụ trạng thái bị bỏ sót).
- Hữu ích cho cả **phân tích yêu cầu** và **thiết kế chi tiết**.


> [!example] Ví dụ
> Đối tượng _Máy bán hàng tự động_:
> - Trạng thái: _Chờ khách hàng_, _Đang chọn hàng_, _Đang trả hàng_, _Hết hàng_.
> - Sự kiện: _Khách nhấn nút chọn_, _Khách đưa tiền_, _Hết sản phẩm_.

# Mô hình hóa biểu đồ trạng thái 🔄

Khi mô hình hóa bằng UML, ta sử dụng các ký hiệu chuẩn:
- **Nút đen đặc**: Trạng thái bắt đầu.
- **Hình tròn kép**: Trạng thái kết thúc.
- **Hình chữ nhật bo tròn**: Biểu diễn trạng thái.
- **Mũi tên**: Biểu diễn chuyển trạng thái.
- **Sự kiện/điều kiện** ghi trên đường chuyển: `event [guard] / action`.

Quy trình xây dựng biểu đồ trạng thái:
1. **Xác định đối tượng** cần mô hình hóa vòng đời.
2. **Liệt kê các trạng thái chính** mà đối tượng có thể có.
3. **Xác định các sự kiện** có thể xảy ra.
4. **Vẽ các chuyển trạng thái** tương ứng, gắn sự kiện và điều kiện.
5. **Đặt hoạt động (action)** nếu cần trên các cạnh hoặc trong trạng thái.


> [!example] Ví dụ
> UML cho đối tượng _Đơn hàng_:
> 
> %% image %%
> 
> `[Trạng thái bắt đầu] → Tạo đơn   Tạo đơn → Đang xử lý (khi Thanh toán thành công)   Đang xử lý → Đang giao (khi Giao cho shipper)   Đang giao → Hoàn thành (khi Giao thành công)   Đang giao → Hủy (nếu Khách hủy hoặc Giao thất bại)`  
> 
> 👉 Nhìn vào biểu đồ, ta thấy ngay toàn bộ vòng đời của đơn hàng từ lúc được tạo đến khi hoàn tất/hủy.

# Tóm lại 🤌

- **Biểu đồ trạng thái** = "bản đồ vòng đời đối tượng".
- Nó giúp ta quản lý các trạng thái và sự kiện trong hệ thống, đảm bảo không bỏ sót kịch bản.
- UML cung cấp ký pháp rõ ràng, dễ dùng, phục vụ tốt cho cả phân tích và thiết kế.

