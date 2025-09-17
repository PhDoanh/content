---
stage: Publish
draft: false
title: Biểu đồ ca sử dụng
description:
tags:
  - OOAD
  - usecase-diagram
  - UML
socialDescription:
socialImage:
permalink:
lang: vi
aliases:
cssclasses:
  - img
---
# Biểu đồ ca sử dụng là gì ❓

Biểu đồ ca sử dụng được dùng để **mô hình hóa các khía cạnh động** của hệ thống - tức là cách hệ thống vận hành trong thực tế. Nó cung cấp **khung nhìn từ bên ngoài**, cho thấy:

- Hệ thống sẽ được sử dụng như thế nào trong bối cảnh thực tế.
- Ai (tác nhân) sẽ tương tác với hệ thống.
- Họ tương tác thông qua những chức năng (ca sử dụng) nào.

👉 Nói ngắn gọn: biểu đồ ca sử dụng giúp trả lời câu hỏi **"Người dùng sẽ làm gì với hệ thống?"**.

> [!example] Ví dụ
> Trong hệ thống đăng ký môn học ở trường đại học, một biểu đồ ca sử dụng có thể mô tả các tác nhân như **Sinh viên**, **Giảng viên**, **Phòng đào tạo**, và các ca sử dụng như **Đăng ký môn**, **Xem thời khóa biểu**, **Nhập điểm**.

# Khái niệm cơ sở cho biểu đồ ca sử dụng ✍️

## Tác nhân (Actor)

- Là **vai trò** của một người, tiến trình, hay thiết bị tương tác với hệ thống.
- Một tác nhân không nhất thiết là một cá nhân cụ thể, mà là một **vai trò**. Ví dụ: một người có thể vừa là **Sinh viên** vừa là **Trợ giảng** (hai tác nhân khác nhau).
- Tác nhân có thể là:
    - Con người (user)
    - Hệ thống khác (ví dụ: hệ thống thanh toán online kết nối với hệ thống bán vé)
    - Thiết bị phần cứng (máy quét thẻ, cảm biến IoT,…)

## Ca sử dụng (Use Case)
- Là **một chức năng cụ thể** mà hệ thống cung cấp cho tác nhân.
- Ca sử dụng mô tả **chuỗi tương tác** (messages) giữa hệ thống và tác nhân để đạt được một mục tiêu có ý nghĩa.

> [!example] Vi dụ
> "Đăng nhập", "Đặt vé", "Thanh toán", "Tra cứu kết quả học tập".

%% image here %%
## Quan hệ trong biểu đồ ca sử dụng
Biểu đồ ca sử dụng không chỉ có tác nhân và ca sử dụng, mà còn thể hiện **các quan hệ** giữa chúng:
1. **Quan hệ giao tiếp (Association)**: đường nối giữa tác nhân và ca sử dụng.
2. **Bao gộp (Include)**: một ca sử dụng luôn bao gồm hành vi của một ca sử dụng khác.
3. **Mở rộng (Extend)**: một ca sử dụng có thể mở rộng thêm hành vi trong những tình huống đặc biệt.
4. **Kế thừa (Generalization)**: áp dụng cho cả tác nhân và ca sử dụng khi có chung đặc điểm.

👉 Nhờ các quan hệ này, biểu đồ ca sử dụng giúp **giảm trùng lặp** và **tổ chức lại chức năng** hệ thống hợp lý hơn.

%% image here %%

# Mô hình hóa với biểu đồ ca sử dụng 📊

Biểu đồ ca sử dụng thường được dùng với **hai mục đích chính**:

## Mô hình hóa khung cảnh của hệ thống
- Xác định **biên hệ thống** (system boundary): cái gì nằm trong hệ thống, cái gì nằm ngoài.
- Xác định các tác nhân bên ngoài, gồm:
    1. Nhóm cần được hệ thống trợ giúp để làm việc.
    2. Nhóm cần thiết để hệ thống vận hành (ví dụ: quản trị viên).
    3. Các hệ thống/phần cứng khác liên quan.
    4. Các nhóm quản trị, bảo trì.
- Có thể tổ chức tác nhân thành **kế thừa** để tránh lặp lại.
- Có thể dùng **stereotype** để chú thích thêm (ví dụ: `<<external system>>`).
- Sau đó, nối các tác nhân với các ca sử dụng mà họ tham gia.

> [!example] Ví dụ
> Trong hệ thống ATM, tác nhân gồm **Khách hàng**, **Ngân hàng trung tâm**, **Bộ phận bảo trì**. Ca sử dụng gồm **Rút tiền**, **Xem số dư**, **Nạp tiền**, **Bảo trì ATM**.

## Mô hình hóa yêu cầu của hệ thống 

- Mỗi ca sử dụng chính là **một yêu cầu chức năng**.
- Các bước mô hình hóa yêu cầu với Use Case Diagram:
    1. Xác định danh sách ca sử dụng từ yêu cầu người dùng.
    2. Xác định quan hệ giữa chúng (include, extend, generalization).
    3. Biểu diễn bằng biểu đồ ca sử dụng.
    4. Thêm các chú thích nếu cần (ví dụ: yêu cầu phi chức năng như bảo mật, tốc độ xử lý).

> [!example] Ví dụ
> Trong ứng dụng thương mại điện tử, yêu cầu **“Khách hàng có thể mua sản phẩm online”** có thể triển khai thành các ca sử dụng: **Đăng nhập**, **Xem sản phẩm**, **Thêm vào giỏ hàng**, **Thanh toán**. Ca sử dụng **Thanh toán** có thể **include** ca sử dụng **Xác thực giao dịch**.

# Tóm lại 🔥

- **Biểu đồ ca sử dụng** giúp ta nhìn hệ thống từ **bên ngoài vào**, mô tả cách hệ thống được **sử dụng bởi các tác nhân**.
- Thành phần chính: **tác nhân - ca sử dụng - quan hệ**.
- Có 2 ứng dụng lớn:
    1. Xác định **khung cảnh và biên hệ thống**.
    2. Xác định và tổ chức **yêu cầu chức năng của hệ thống**.

💡 Nếu ví hệ thống như một nhà hàng:
- **Tác nhân**: khách hàng, bếp trưởng, nhân viên giao món.
- **Ca sử dụng**: gọi món, nấu ăn, giao món, thanh toán.
- **Quan hệ include**: "Gọi món" luôn bao gồm "Chọn món từ menu".
- **Quan hệ extend**: "Thanh toán" có thể mở rộng thêm hành vi "Nhập mã giảm giá".
