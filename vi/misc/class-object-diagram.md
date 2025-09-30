---
stage: Publish
draft: false
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
## Khái niệm cơ sở cho khung nhìn tĩnh ✍️

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

## Quan hệ trong khung nhìn tĩnh ⛓️‍💥

Các quan hệ thường gặp trong biểu đồ lớp gồm:

### Quan hệ kết hợp (Association)
- **Định nghĩa**: Là quan hệ cấu trúc cơ bản nhất giữa hai lớp, cho biết **một lớp có liên quan đến lớp khác** trong mô hình.
- **Ký hiệu**: Đường nối đơn giản giữa hai lớp. Có thể thêm nhãn, vai trò, bội số (multiplicity: 1, 0.., 1..).

> [!example] Ví dụ
> %% ảnh về quan hệ kết hợp cho VD %%
> 
> - Lớp `SinhVien` **học** `MonHoc`.
> - Bội số: Một `SinhVien` có thể học _nhiều_ `MonHoc`, một `MonHoc` có thể có _nhiều_ `SinhVien`.

👉 Đây chính là cách ta mô tả "ai liên quan tới ai" trong hệ thống.

### Quan hệ kết tập (Aggregation)
- **Định nghĩa**: Là một dạng đặc biệt của kết hợp, biểu diễn **mối quan hệ toàn thể - bộ phận** (whole-part). Điểm khác biệt: **các bộ phận có thể tồn tại độc lập với toàn thể**.
- **Ký hiệu**: Hình thoi rỗng ở phía "toàn thể".

> [!example] Ví dụ
> %% ảnh %%
> 
> - `LopHoc` **gồm** `SinhVien`.
> - Một lớp học có nhiều sinh viên, nhưng sinh viên có thể tồn tại ngay cả khi lớp học bị giải thể.

👉 Hiểu nôm na: kết tập = "sở hữu nhưng không kiểm soát sự sống còn".

### Quan hệ hợp thành (Composition)
- **Định nghĩa**: Cũng là toàn thể - bộ phận nhưng **bộ phận không thể tồn tại độc lập** nếu toàn thể bị hủy.
- **Ký hiệu**: Hình thoi đen ở phía "toàn thể".

> [!example] Ví dụ
> %% ảnh %%
> 
> - `NgôiNha` **chứa** `Phong`.
> - Nếu ngôi nhà bị phá hủy thì các phòng cũng không thể tồn tại độc lập.

👉 Đây là quan hệ “sống chết có nhau”, chặt chẽ hơn kết tập.

### Quan hệ thừa kế (Generalization/Inheritance)
- **Định nghĩa**: Là quan hệ phân cấp cho thấy một lớp **con kế thừa** thuộc tính và hành vi từ một lớp **cha**.
- **Ký hiệu**: Mũi tên rỗng, hướng từ lớp con đến lớp cha.

> [!example] Ví dụ
> %% ảnh %%
> 
> - `SinhVien`, `GiangVien` **là** `ConNguoi`
> - `SinhVien` và `GiangVien` đều có các thuộc tính chung từ `ConNguoi` (tên, tuổi, địa chỉ) và có thể mở rộng thêm hành vi riêng.

👉 Đây là cơ sở cho **tái sử dụng** và **đa hình** trong lập trình hướng đối tượng.

### Quan hệ phụ thuộc (Dependency)
- **Định nghĩa**: Thể hiện rằng **sự thay đổi của một lớp có thể ảnh hưởng đến lớp khác**, nhưng không phải là mối quan hệ lâu dài (thường là tạm thời, yếu hơn association).
- **Ký hiệu**: Đường nét đứt với mũi tên chỉ từ lớp "khách" (client) đến lớp "cung cấp" (supplier).

> [!example] Ví dụ
> %% ảnh %%
> 
> - `GiaoDienDangKy` **sử dùng** `HeThongDangKy`.
> - Nếu thay đổi trong `HeThongDangKy` thì `GiaoDienDangKy` có thể phải thay đổi theo.

Bảng tổng hợp các loại quan hệ phụ thuộc trong UML:

| Loại phụ thuộc          | Từ khóa UML   | Mô tả                                                                                            |
| ----------------------- | ------------- | ------------------------------------------------------------------------------------------------ |
| **Truy cập**            | `access`      | Một lớp truy cập trực tiếp nội dung (thuộc tính/phương thức) của lớp khác.                       |
| **Ràng buộc khuôn mẫu** | `bind`        | Gán tham số cụ thể vào một khuôn (template) để tạo phần tử mô hình mới.                          |
| **Gọi phương thức**     | `call`        | Một phương thức của lớp gọi thao tác (operation) của lớp khác.                                   |
| **Tạo đối tượng**       | `create`      | Một lớp tạo ra thể hiện (instance) của lớp khác.                                                 |
| **Suy dẫn**             | `derive`      | Một thông tin/đối tượng có thể tính toán hoặc rút ra từ đối tượng khác.                          |
| **Khởi tạo**            | `instantiate` | Một phương thức chuyên dùng để tạo các đối tượng của lớp khác.                                   |
| **Cấp quyền**           | `permit`      | Cho phép một phần tử được dùng nội dung của phần tử khác.                                        |
| **Hiện thực hóa**       | `realize`     | Liên hệ giữa bản đặc tả (ví dụ interface) và bản cài đặt (class).                                |
| **Tinh chỉnh**          | `refine`      | Đặc tả ở mức khái quát được làm chi tiết hơn thành mô hình cụ thể.                               |
| **Gửi tín hiệu**        | `send`        | Quan hệ giữa lớp gửi và lớp nhận một tín hiệu.                                                   |
| **Thay thế**            | `substitute`  | Một lớp có thể thay thế lớp khác nhờ hỗ trợ cùng giao diện.                                      |
| **Vết vạch (theo dõi)** | `trace`       | Kết nối giữa các phần tử ở mô hình khác nhau để theo dõi (ví dụ: yêu cầu → thiết kế → kiểm thử). |
| **Sử dụng**             | `use`         | Một lớp cần sự hiện diện của lớp khác để hoạt động đúng.                                         |

👉 Phụ thuộc thường xuất hiện khi rơi vào các trường hợp của bảng trên, nhất là khi lớp **gọi phương thức** hoặc **sử dụng tạm thời** một lớp khác.

### Quan hệ hiện thực hóa (Realization/Implementation)
- **Định nghĩa**: Cho biết một **interface** (giao diện) được một hoặc nhiều lớp cụ thể **cài đặt**.
- **Ký hiệu**: Đường nét đứt với mũi tên rỗng, từ lớp thực hiện đến interface.

> [!example] Ví dụ
> %% ảnh %%
> 
> - Interface `ThanhToan` **được cài đặt bởi** `ThanhToanQuaThe`, `ThanhToanQuaTienMat`.
> - Cả hai lớp này đều phải **thực hiện (implement)** các phương thức đã được định nghĩa trong interface `ThanhToan`.

👉 Đây là cầu nối quan trọng để thiết kế hệ thống **linh hoạt, dễ thay thế**.

## Biểu đồ đối tượng 

Biểu đồ đối tượng (Object Diagram) là **một ảnh chụp tức thời** của biểu đồ lớp ở một trạng thái cụ thể. Nếu biểu đồ lớp mô tả "cái khung" thì biểu đồ đối tượng chính là "ảnh chụp thực tế" các đối tượng với giá trị cụ thể tại một thời điểm.

%% ảnh ví dụ về 1 biểu đồ đối tượng hoàn chỉnh %%

> [!example] Ví dụ
> - Biểu đồ lớp có lớp `SinhVien`
> - Biểu đồ đối tượng sẽ có: `sv1: SinhVien {ten = "An", mssv = "123"}`.

👉 Nó giúp minh họa cách các đối tượng thật sự tồn tại và tương tác trong hệ thống.

## Mô hình hóa với biểu đồ lớp

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

## Tóm lại 🤌

Biểu đồ lớp là **trái tim của UML**, giúp mô hình hóa phần "xương sống" của hệ thống. Nó cho ta thấy rõ **những ai tham gia, quan hệ thế nào, tồn tại ra sao** trong hệ thống.