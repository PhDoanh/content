---
stage: Draft
draft: true
title: Biểu đồ lớp và đối tượng
description:
tags:
  - OOAD
  - UML
  - class-diagram
  - object-diagram
  - static-view
socialDescription:
socialImage:
permalink:
lang: vi
aliases:
cssclasses:
  - img
---
# Khái niệm cơ sở cho khung nhìn tĩnh ✍️

Biểu đồ lớp (Class Diagram) là **biểu đồ dạng tĩnh** trong UML, dùng để mô tả **cấu trúc tĩnh** của hệ thống. Nó thể hiện:
- Các **lớp (class)** trong hệ thống.
- Các **thuộc tính** (attributes) và **phương thức** (operations) của lớp.
- Các **quan hệ** (relationships) giữa các lớp.

👉 Nói cách khác, nếu coi hệ thống là một "ngôi nhà", thì biểu đồ lớp chính là **bản thiết kế khung xương**: tường, cột, nội thất, … chứ chưa nói chi tiết về cách sinh hoạt bên trong.

> [!example] Ví dụ
> Trong hệ thống quản lý sinh viên, bạn có các lớp: `SinhVien`, `LopHoc`, `MonHoc`
> - `SinhVien` có thuộc tính: tên, mã số, ngày sinh; có phương thức: dangKyMonHoc()
> - `MonHoc` có thuộc tính: tên môn, số tín chỉ; có phương thức: moLop().
> - `LopHoc` liên kết cả `SinhVien` và `MonHoc`.

# Quan hệ trong khung nhìn tĩnh ⛓️‍💥

Các quan hệ thường gặp trong biểu đồ lớp gồm:
1. **Quan hệ kết hợp (Association)** 👫
    - Thể hiện sự **liên kết lô-gic** giữa hai lớp.
    - Ví dụ: Lớp `SinhVien` **học** `MonHoc`.

2. **Quan hệ kết tập (Aggregation)** ⚪➡️
    - Là mối quan hệ **toàn thể – bộ phận** nhưng bộ phận vẫn tồn tại độc lập.
    - Ví dụ: Một `LopHoc` gồm nhiều `SinhVien`, nhưng sinh viên có thể rời lớp này để sang lớp khác.

3. **Quan hệ hợp thành (Composition)** ⬛➡️
    - Cũng là toàn thể – bộ phận nhưng bộ phận **không thể tồn tại độc lập** nếu toàn thể bị hủy.
    - Ví dụ: Một `NgôiNha` có `Phong`, nếu ngôi nhà bị phá, các phòng cũng mất.

4. **Quan hệ thừa kế (Generalization/Inheritance)** 👪
    - Thể hiện mối quan hệ cha – con giữa các lớp.
    - Ví dụ: `GiangVien` và `SinhVien` cùng kế thừa từ lớp `Nguoi`.

5. **Quan hệ phụ thuộc (Dependency)** 📦
    - Một lớp **phụ thuộc** vào thay đổi của lớp khác.
    - Ví dụ: `GiaoDienDangKy` phụ thuộc vào `HeThongDangKy`.

6. **Quan hệ hiện thực hóa (Realization/Implementation)**
    - Thường thấy giữa **interface** và lớp thực hiện interface đó.
    - Ví dụ: Interface `ThanhToan` được lớp `ThanhToanQuaThe` hiện thực.

# Biểu đồ đối tượng 

Biểu đồ đối tượng (Object Diagram) là **một ảnh chụp tức thời** của biểu đồ lớp ở một trạng thái cụ thể. Nếu biểu đồ lớp mô tả "cái khung" thì biểu đồ đối tượng chính là "ảnh chụp thực tế" các đối tượng với giá trị cụ thể tại một thời điểm.

> [!example] Ví dụ
> - Biểu đồ lớp có lớp `SinhVien`
> - Biểu đồ đối tượng sẽ có: `sv1: SinhVien {ten = "An", mssv = "123"}`.

👉 Nó giúp minh họa cách các đối tượng thật sự tồn tại và tương tác trong hệ thống.

# Mô hình hóa với biểu đồ lớp

Ứng dụng của biểu đồ lớp trong mô hình hóa:
- **Đặc tả cấu trúc hệ thống**: Cho ta thấy các thành phần chính và quan hệ của chúng.
- **Thiết kế cơ sở dữ liệu**: Biểu đồ lớp gần gũi với mô hình ERD trong thiết kế CSDL, nên dễ thiết DB hơn khi có biểu đồ lớp rồi
- **Giao tiếp giữa các nhóm phát triển**: Biểu đồ lớp là công cụ chung cho nhà phân tích, thiết kế, lập trình viên.
- **Hỗ trợ tái sử dụng và bảo trì**: Nhờ thấy rõ cấu trúc, quan hệ, kế thừa nên dễ mở rộng hệ thống về sau mà không phải vẽ lại từ đầu.

> [!example] Ví dụ
> Hệ thống Quản lý Thư viện
> - Lớp `DocGia`, `Sach`, `TheThuVien`, `MuonTra`.
> - Quan hệ: `DocGia` – `MuonTra` – `Sach`.
> - `Sach` có thuộc tính: `tenSach`, `tacGia`, `namXuatBan`.
> - `MuonTra` có phương thức: `muon()`, `tra()`.

# Tóm lại 🤌

Biểu đồ lớp là **trái tim của UML**, giúp mô hình hóa phần "xương sống" của hệ thống. Nó cho ta thấy rõ **những ai tham gia, quan hệ thế nào, tồn tại ra sao** trong hệ thống.