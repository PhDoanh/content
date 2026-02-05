---

draft: false
title: Biểu đồ trạng thái
description:
tags:
  - analysis-and-design
  - state-diagram
  - finite-state-machine
  - modeling-language
socialDescription:
socialImage:
permalink:
lang: vi
aliases:
cssclasses:
  - img
---
## Tổng quan 🔭

[Biểu đồ trạng thái](https://www.uml-diagrams.org/state-machine-diagrams-examples.html) là một trong những biểu đồ quan trọng của UML, được dùng để mô tả hành vi động của các đối tượng theo thời gian bằng cách mô hình hóa **vòng đời** của chúng trong hệ thống. Nó cho ta thấy:

- Một đối tượng có thể **ở những trạng thái nào** trong suốt vòng đời.
- Những **sự kiện** nào sẽ làm đối tượng chuyển từ trạng thái này sang trạng thái khác.
- Các **hoạt động** xảy ra khi chuyển trạng thái.

👉 Bạn có thể hình dung biểu đồ trạng thái giống như cuốn album chụp hình bạn từ lúc bé đến lớn, mỗi tấm ảnh tương ứng với một **trạng thái** của bạn tại thời điểm đó và những ghi chép trên album chính là các **sự kiện và hoạt động** đã diễn ra trong hành trình khôn lớn của bạn. 

## Bên trong biểu đồ trạng thái 🔬

### Sự kiện

[Sự kiện](https://www.uml-diagrams.org/event.html) là **tác nhân kích hoạt** việc thay đổi trạng thái của một đối tượng. Bản thân nó cũng được kích hoạt bởi đa dạng yếu tố như người dùng, hệ thống, hay một điều kiện nội bộ nào đó, ... Nên cũng đa dạng thể loại sự kiện được sinh ra từ đó, cụ thể: 

- **Sự kiện tín hiệu**: dựa trên tín hiệu được gửi từ đối tượng này sang đối tượng khác, *ví dụ*: máy chủ gửi tín hiệu `timeout` cho máy khách, máy khách chuyển sang trạng thái "lỗi/thử lại"
- **Sự kiện gọi**: dựa trên lời gọi hàm/phương thức của đối tượng, *ví dụ*: gọi hàm `withdraw()` trên đối tượng ATM sẽ khiến đối tượng này chuyển sang trạng thái "đang rút tiền"
- **Sự kiện thời gian**: dựa trên các điều kiện về thời gian để kích hoạt thay đổi trạng thái, *ví dụ*: sau 30 giây không thao tác thì ATM tự thoát (chuyển về trạng thái "đã thoát").
- **Sự kiện thay đổi**: dựa trên sự thay đổi logic đúng ↔ sai mà chuyển trạng thái, *ví dụ*: nhiệt độ > 100°C thì nồi cơm chuyển sang trạng thái tắt.

### Tín hiệu

Tín hiệu là **phương tiện giao tiếp** giữa đối tượng gửi và đối tượng nhận, nó mang **thông tin sự kiện** được tạo ra bởi đối tượng gửi để đối tượng tiếp nhận thông tin đó thực hiện các hành động tương ứng (chuyển trạng thái, tính toán, phản hồi, ...)

> [!example]- Ví dụ
> Cảm biến nhiệt độ gửi tín hiệu "hot" (thông tin từ sự kiện cháy) đến thiết bị báo cháy để kích hoạt hệ thống dập lửa.

### Trạng thái

[Trạng thái](https://www.uml-diagrams.org/state-machine-diagrams.html#simple-state) là sự **ổn định** trong vòng đời của một đối tượng, tại đó đối tượng thỏa mãn một số điều kiện, thực hiện một hoạt động hoặc chờ đợi một sự kiện. Do đó, có thể mô tả trạng thái theo 3 cách sau:

1. Trạng thái như việc **đáp ứng một số điều kiện**. *Ví dụ*: Đèn ở trạng thái "Bật" do đáp ứng điều kiện về điện, môi trường, ...  
2. Trạng thái như một **hoạt động đang diễn ra**. *Ví dụ*: Đèn ở trạng thái "Đang chiếu sáng".
3. Trạng thái như một **tình huống chờ**. *Ví dụ*: Đèn ở trạng thái "Chờ người dùng tắt".

> [!info] Lưu ý
> Tất cả các đối tượng cùng một trạng thái sẽ phản ứng theo cùng một cách đối với một sự kiện.

### Trạng thái phức hợp

[Trang thái phức hợp](https://www.uml-diagrams.org/state-machine-diagrams.html#composite-state) là trạng thái được **phân rã** thành các vùng trong đó chứa một/nhiều **trạng thái con**, một số hoặc tất cả các vùng có thể diễn ra đồng thời trong trạng thái phức hợp. Điều này cho phép mô hình hóa hành vi phức tạp và giúp biểu đồ trạng thái trông gọn hơn.

> [!example]- Ví dụ
> Trạng thái "Đang xử lý đơn hàng" có thể chia thành 3 vùng (1 trạng thái/vùng): Vùng 1 chứa "Xác minh thanh toán" → Vùng 2 chứa "Chuẩn bị hàng" → Vùng 3 chứa "Đóng gói". Ba vùng này không xảy ra đồng thời do ràng buộc bởi quy luật tự nhiên trong quy trình xử lý đơn hàng.

### Chuyển
[Chuyển](https://www.uml-diagrams.org/state-machine-diagrams.html#behavioral-transition) là sự di chuyển từ trạng thái này sang trạng thái khác khi sự kiện xảy ra. Được biểu diễn bằng một mũi tên hướng đến trạng thái đích, có thể bao gồm các điều kiện và hành động khi chuyển

**Chuyển bên trong** là loại chuyển được xử lý ngay trong **trạng thái hiện tại**, không làm thay đổi sang trạng thái khác. Do đó nó không có trạng thái đích.

> [!example]- Ví dụ
> - **Chuyển**: sự kiện cúp máy sẽ chuyển trạng thái từ "Đang gọi điện" sang "Kết thúc cuộc gọi".
> - **Chuyển bên trong**: sự kiện tăng âm lượng chỉ thay đổi độ to/nhỏ của âm thanh nhưng vẫn giữ ở trạng thái "Đang gọi điện".

### Máy trạng thái
**Máy trạng thái** là một đồ thị gồm các **trạng thái** và các **chuyển** nối chúng lại với nhau, nó có thể phản ánh **một phần hoặc toàn bộ** biểu đồ trạng thái vì chức năng của máy trạng thái chính là **mô hình hóa lịch sử vòng đời** có thể có của các đối tượng trong hệ thống. Những đối tượng này có thể thuộc về một lớp, hành vi, ca sử dụng hay cộng tác ... 

Khi đối tượng phát hiện một sự kiện từ bên ngoài, tùy theo trạng thái hiện thời mà nó phản hồi theo các cách khác nhau. Phản hồi ở đây bao gồm cả việc thực thi gây ra các thay đổi trong ngoài đối tượng trước khi chuyển sang trạng thái mới.

## Mục đích của biểu đồ trạng thái 🔄
Biểu đồ trạng thái sử dụng một/nhiều máy trạng thái trong nó để mô hình hóa vòng đời các đối tượng dưới dạng các thể hiện của lớp, ca sử dụng, hệ thống, ... Khi mô hình hóa bằng UML, ta sử dụng các ký hiệu tiêu chuẩn sau:
- **Hình tròn màu đen**: Trạng thái bắt đầu.
- **Đường tròn chứa hình tròn đen bên trong**: Trạng thái kết thúc.
- **Hình chữ nhật bo tròn**: Biểu diễn trạng thái với tên được đặt trong hình.
- **Mũi tên**: Biểu diễn chuyển trạng thái.
- **Sự kiện/điều kiện** ghi trên đường chuyển dưới dạng `event [guard] / action`.

Quy trình xây dựng biểu đồ trạng thái:
1. **Xác định đối tượng** cần mô hình hóa vòng đời.
2. **Liệt kê các trạng thái chính** mà đối tượng có thể có.
3. **Xác định các sự kiện** có thể xảy ra.
4. **Vẽ các chuyển trạng thái** tương ứng, gắn sự kiện và điều kiện lên chúng.
5. **Đặt các hoạt động** (nếu cần) trên các chuyển hoặc trong trạng thái.

## Tóm lại🎬

Biểu đồ trạng thái là bản đồ vòng đời đối tượng. Nó giúp ta quản lý các trạng thái và sự kiện bên trong hệ thống, đảm bảo không bỏ sót kịch bản hành vi nào.
