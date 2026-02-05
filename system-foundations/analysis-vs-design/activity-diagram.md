---
stage: Update
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
## Tổng quan 🔭

**Biểu đồ hoạt động** là một loại biểu đồ mô hình hóa **khía cạnh động** của hệ thống, mô tả các **luồng hoạt động/dòng chảy** xử lý những gì di chuyển trên chúng. Cụ thể:

- Diễn tả **trình tự các bước** mà hệ thống thực hiện.
- Cho thấy luồng xử lý **rẽ nhánh/song song/hợp nhất** các bước trong tiến trình.
- Giúp hình dung rõ ràng cách **dữ liệu và tín hiệu điều khiển luân chuyển** giữa các bước.

👉 Bạn có thể tưởng tượng biểu đồ hoạt động là biến thể cao cấp hơn của biểu đồ [sơ đồ khối](https://en.wikipedia.org/wiki/Flowchart) (flowchart), vì ngoài tuần tự và rẽ nhánh, nó còn hỗ trợ các khả năng khác như **đồng bộ** và **xử lý song song**.

## Bên trong biểu đồ hoạt động 🔬
### Hoạt động
[Hoạt động](https://www.uml-diagrams.org/activity-diagrams.html#activity) là một nút **thực thi câu lệnh** trong một thủ tục hoặc **thực hiện một bước** trong luồng công việc, nó được biểu diễn bằng **hình chữ nhật bo góc** và được kết nối bởi các **mũi tên** dưới dạng các luồng điều khiển và các luồng dữ liệu.

Nút hoạt động thường chỉ bắt đầu khi có **tín hiệu điều khiển** trên mỗi luồng đầu vào của nó. Khi nút được thực hiện xong, sự thực thi sẽ tiếp tục với các nút kế tiếp từ luồng đầu ra của nút này. Các luồng hoạt động giống như các [[state-diagram#Chuyển|chuyển]] trong máy trạng thái, chúng xảy ra chỉ khi thực thi hoàn tất nhưng khác ở chỗ là có thể rơi vào **trạng thái chờ** cho một số sự kiện nào đó ngay cả khi đã đáp ứng đầy đủ đầu vào.

> [!example]- Ví dụ
> Một luồng phức tạp như **"Đặt hàng trực tuyến"** bao gồm chuỗi các hoạt động: chọn sản phẩm → thanh toán → xác nhận đơn hàng thành công/thất bại. Trong đó, hoạt động  chọn sản phẩm và thanh toán có thể rơi vào trạng thái chờ người dùng tương tác (chờ chọn, chờ điền thông tin, ...)

### Hành động
[Hành động](https://www.uml-diagrams.org/activity-diagrams-actions.html) là **đơn vị thực thi nhỏ nhất**, mô tả những **diễn biến cụ thể** xảy ra bên trong hoạt động. Nói cách khác, hoạt động có thể được chia thành nhiều hành động cụ thể nhưng những hành động cụ thể không thể được chia nhỏ hơn do là đơn vị thực thi nhỏ nhất.

> [!example]- Ví dụ
> Trong quy trình đặt hàng, các hành động cụ thể (không thể chia nhỏ hơn nữa) bao gồm: "Nhập mã giảm giá", "Nhấn nút Xác nhận", hoặc "Hiển thị thông báo lỗi", ...

### Nút điều khiển
[Nút điều khiển](https://www.uml-diagrams.org/activity-diagrams-controls.html) là nút điều phối và kiểm soát các luồng điều khiển di chuyển theo những hướng khác nhau dựa trên khả năng của các hoạt động như tuần tự, song song, đồng bộ, ... Một số nút điều khiển điển hình bao gồm: **rẽ nhánh/quyết định** (khi hoạt động có nhiều đầu ra), **phân tách/đồng bộ** (khi hoạt động chạy song song được), **hợp nhất** (tập hợp nhiều luồng nhưng chỉ cho 1 luồng đi qua), ...

> [!example]- Ví dụ
> - **Nút quyết định (Decision):** Sau hành động "Kiểm tra tồn kho", nếu hàng "Còn" thì đi tiếp đến "Xác nhận đơn", nếu "Hết" thì chuyển đến "Thông báo hết hàng".
> - **Nút phân tách (Fork):** Sau khi thanh toán thành công, hệ thống thực hiện đồng thời hai luồng: "Gửi email xác nhận cho khách" và "Thông báo cho bộ phận kho".
> - **Nút đồng bộ (Join):** Chỉ khi cả hai luồng gửi email và thông báo kho hoàn tất, hệ thống mới chuyển trạng thái đơn hàng sang "Chờ giao".

### Luồng đối tượng
[Luồng đối tượng](https://www.uml-diagrams.org/activity-diagrams.html#object-flow-edge) là luồng **chứa một đối tượng** dưới dạng **đầu vào/đầu ra** của một hoạt động. Được biểu diễn bằng một hình chữ nhật góc cạnh với tên và các giá trị của đối tượng bên trong, một mũi tên hướng từ hoạt động trước tới đối tượng và một mũi tên hướng từ đối tượng tới hoạt động sau.

> [!example]- Ví dụ
> Một đối tượng "Hóa đơn" với trạng thái chưa thanh toán được tạo ra từ hành động "Xuất hóa đơn" và truyền cho hành động "Xử lý thanh toán". Lúc này, "Hóa đơn" chính là đối tượng di chuyển trên luồng.

### Phân vùng
[Phân vùng](https://www.uml-diagrams.org/activity-diagrams.html#partition) là các đường kẻ **phân tách** biểu đồ thành các vùng để **gom nhóm** các hoạt động theo **vai trò/trách nhiệm**, giúp tổ chức các phần tử gọn gàng và rõ ràng hơn về cả hình thức lẫn nội dung.

> [!example]- Ví dụ
> Trong biểu đồ hoạt động của cả hệ thống "Quản lý đăng ký học", ta có thể chia thành các phân vùng sau:
> - **Quản lý sinh viên**: lưu thông tin cá nhân, hồ sơ học tập, ...
> - **Quản lý môn học**: lưu danh sách môn học, tín chỉ, lịch học, ...
> - **Thanh toán học phí**: xử lý hóa đơn, giao dịch, ...
> - **Báo cáo**: xuất bảng biểu, thống kê, ...

## Mục đích của biểu đồ hoạt động 🎯
### Mô hình hóa luồng công việc 

Dùng khi ta muốn biểu diễn **quy trình nghiệp vụ** hoặc **tương tác với tác nhân bên ngoài** hệ thống. Cách làm:
1. Xác định ranh giới cho luồng công việc bằng **điểm bắt đầu và kết thúc**. Kèm theo các điều kiện phải có trước khi bắt đầu (tiền điều kiện) và sau khi kết thúc (hậu điều kiện) luồng đó.

2. Chọn những đối tượng nghiệp vụ đóng vai trò chính trong luồng công việc và tạo các phân vùng cho từng đối tượng này.

3. Bắt đầu từ trạng thái khởi đầu, mô tả các hoạt động và hành động diễn ra tiếp theo. Với hoạt động phức tạp, có thể tách ra biểu đồ riêng và tham chiếu lại trong biểu đồ này.

4. Kết nối các hoạt động/hành động bằng luồng tuần tự trước, sau đó thêm rẽ nhánh, song song, và hợp nhất luồng.

### Mô hình hóa thao tác

Dùng khi ta muốn mô tả chi tiết **cách một hàm/phương thức** được chạy. Cách làm:
1. Liệt kê các trừu tượng liên quan như tham số đầu vào, kết quả trả về, các thuộc tính lớp và đối tượng liên quan.

2. Xác định tiền/hậu điều kiện và các thành phần bất biến (như hằng số chẳng hạn). *Ví dụ*: giỏ hàng không được rỗng trước khi thanh toán.

3. Bắt đầu từ trạng thái khởi đầu của thao tác, mô tả các bước (hoạt động/hành động) diễn ra tiếp theo

4. Sử dụng các nút điều khiển như rẽ nhánh để mô tả các điều kiện và vòng lặp. Chỉ dùng đồng bộ khi thao tác thuộc về [[unified-modeling-language#^c77eec|lớp tích cực]].

## Chốt lại 📌
Biểu đồ hoạt động là sơ đồ quy trình nâng cao của UML. Có thể dùng để mô tả **quy trình nghiệp vụ** hoặc **chi tiết thao tác/hàm**. Giúp **trực quan hóa luồng xử lý** → cực kỳ hữu ích khi phân tích yêu cầu và trao đổi giữa các [[|bên liên quan]] (team BA, dev và khách hàng, ...)
