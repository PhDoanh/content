---
stage: Publish
draft: false
title: Biểu đồ hoạt động
description:
tags:
  - analysis-and-design
  - modeling-language
  - activity-diagram
  - workflow-modeling
  - operation-modeling
socialDescription:
socialImage:
permalink:
lang: vi
aliases:
cssclasses:
  - img
---
**Biểu đồ hoạt động (Activity Diagram)** là một trong những loại biểu đồ dễ hình dung nhất vì nó giống sơ đồ quy trình công việc mà ta hay thấy trong đời sống hàng ngày. Tuy đơn giản, nhưng lại có vai trò rất mạnh mẽ trong phân tích và thiết kế hệ thống 🚀

## Các khái niệm về biểu đồ hoạt động ✍️
Trước hết, biểu đồ hoạt động là một loại **biểu đồ động** của UML, mô tả **luồng hoạt động (workflow)** hay **dòng chảy xử lý** trong hệ thống. Nó có thể:

- Diễn tả **trình tự các bước** mà hệ thống thực hiện.

- Cho thấy luồng xử lý **rẽ nhánh, song song, hợp nhất** trong tiến trình.

- Giúp hình dung rõ ràng cách **dữ liệu và điều khiển luân chuyển** giữa các bước.

👉 Bạn có thể tưởng tượng biểu đồ hoạt động như một **sơ đồ khối (flowchart)** nhưng **cao cấp** hơn: ngoài tuần tự và rẽ nhánh, nó còn hỗ trợ **đồng bộ** và **xử lý song song**.

Các thành phần cơ bản:
1. **Hoạt động (Activity):**
    - Là bước xử lý trong hệ thống.
    - Được vẽ bằng hình **chữ nhật bo góc**.
    - Một hoạt động chỉ bắt đầu khi có đủ "token" (dấu hiệu điều khiển) ở các luồng đầu vào của nó.
2. **Hành động (Action):**
    - Là đơn vị cơ bản nhất của hoạt động, ví dụ: tạo đối tượng, hủy đối tượng, đọc/ghi thuộc tính.
    - Nằm ở phần "lá" của biểu đồ hoạt động, không thể chia thành các action nhỏ hơn!
    - Lưu ý: Bản thân activity có thể là action, nhưng ngược lại chưa chắc đúng
3. **Luồng điều khiển (Control Flow):**
    - Mũi tên nối giữa các hoạt động.
    - Cho biết trình tự thực thi.
4. **Luồng đối tượng (Object Flow):**
    - Thể hiện việc **truyền dữ liệu/đối tượng** từ hoạt động này sang hoạt động khác.
5. **Nút điều khiển:**
    - **Rẽ nhánh (Decision/Merge):** dùng hình thoi, tương tự if-else.
    - **Phân tách/Hợp nhất (Fork/Join):** dùng các thanh gạch ngang để biểu diễn song song - ví dụ một tiến trình có thể tách ra thành nhiều luồng chạy đồng thời.
6. **Phân vùng (Partition/Swimlane):**
    - Giúp nhóm hoạt động theo **vai trò hoặc bộ phận** (ví dụ: khách hàng, nhân viên, hệ thống).
    - Thường được vẽ như các "“làn bơi" để dễ phân biệt trách nhiệm.

%% image %%

## Mô hình hóa biểu đồ hoạt động

Biểu đồ hoạt động không đi sâu chi tiết cách tính toán, mà chỉ tập trung mô tả **luồng hoạt động**. Nó thường được dùng ở giai đoạn đầu để:
- Đặc tả **ca sử dụng (Use Case)**.
- Làm rõ **quy trình nghiệp vụ**.
- Chuẩn bị cho bước thiết kế hệ thống.

Có hai cách ứng dụng chính:
### Mô hình hóa luồng công việc 

Dùng khi ta muốn biểu diễn **quy trình nghiệp vụ** hoặc **tương tác với tác nhân bên ngoài**. Các bước cơ bản:
1. **Xác định phạm vi (scope):**
    - Đặt ranh giới cho luồng công việc.
    - Định nghĩa **điểm bắt đầu và kết thúc** (với tiền điều kiện và hậu điều kiện rõ ràng).

2. **Chọn đối tượng nghiệp vụ chính:**
    - Ví dụ: khách hàng, phòng ban, hệ thống con.
    - Tạo **swimlane** cho từng đối tượng này.

3. **Đặc tả hoạt động:**
    - Bắt đầu từ trạng thái khởi đầu, liệt kê các bước theo trình tự.
    - Với hoạt động phức tạp, có thể tách ra biểu đồ riêng.

4. **Kết nối bằng luồng:**
    - Đầu tiên vẽ luồng tuần tự.
    - Sau đó thêm rẽ nhánh, song song, và hợp nhất luồng.

%% image %%

👉 Ứng dụng: thường dùng trong **Business Process Modeling** (mô hình hóa quy trình nghiệp vụ).

### Mô hình hóa thao tác

Dùng khi ta muốn đặc tả chi tiết **cách một hàm/phương thức chạy**. Các bước:
1. **Liệt kê các trừu tượng liên quan:**
    - Tham số đầu vào, kết quả trả về.
    - Các thuộc tính lớp và đối tượng liên quan.

2. **Xác định tiền/hậu điều kiện & bất biến:**
    - Ví dụ: "giỏ hàng không được rỗng trước khi thanh toán".

3. **Vẽ biểu đồ hoạt động cho thao tác:**
    - Bắt đầu từ trạng thái khởi đầu.
    - Mô tả các bước, điều kiện rẽ nhánh, vòng lặp.

4. **Chỉ dùng song song (fork/join) khi thao tác thuộc về lớp tích cực (active class)**.

%% image %%

👉 Ứng dụng: thường dùng trong **thiết kế chi tiết** để đội dev hiểu chính xác logic bên trong một hàm hay module nào đó.

## Chốt lại 📌

- Biểu đồ hoạt động = **sơ đồ quy trình nâng cao** của UML.
- Có thể dùng để mô tả **workflow nghiệp vụ** hoặc **chi tiết thao tác/hàm**.
- Các yếu tố chính: **hoạt động, hành động, luồng điều khiển, luồng đối tượng, rẽ nhánh, song song, swimlane**.
- Giúp **trực quan hóa luồng xử lý** → cực kỳ hữu ích khi phân tích yêu cầu và trao đổi giữa team BA, dev và khách hàng.

