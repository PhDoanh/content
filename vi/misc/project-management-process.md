---
stage: Idea
draft: true
title: Quy trình quản lý dự án
description:
tags:
  - project-management
  - project-management-process
socialDescription:
socialImage:
permalink:
lang: vi
aliases:
cssclasses:
  - img
---
Khi nói đến **quản lý dự án**, ta không chỉ nhìn vào từng công việc riêng lẻ, mà phải đặt chúng trong một **quy trình tổng thể**. PMI (Project Management Institute) đã hệ thống hóa thành **các nhóm quy trình quản lý dự án**, giúp dự án đi đúng hướng từ khởi đầu cho đến khi kết thúc.

## Nhóm quy trình quản lý dự án 🔄
Công việc quản lý dự án xoay quanh [[project-management#^7eeb7c|10 miền tri thức]], nhưng để "triển khai" các miền tri thức này trong thực tế, ta phải đi qua **các nhóm quy trình**. PMI định nghĩa: _nhóm quy trình quản lý dự án là tập hợp logic các quy trình nhằm đạt mục tiêu cụ thể của dự án_. Các quy trình quản lý dự án được chia thành **5 nhóm**:

### Nhóm quy trình Khởi tạo

**Mục tiêu chính:** Khởi động dự án một cách chính thức - xác định lý do, mục tiêu, quyền hạn và nguồn lực ban đầu; gắn tên người chịu trách nhiệm và nhà tài trợ.

**Hoạt động tiêu biểu**
- Lập **tài liệu thông tin sơ bộ dự án** (Project Charter).
- Xác định **nhà tài trợ** (sponsor), người đứng đầu dự án và các bên liên quan cốt lõi.
- Thực hiện các cuộc họp khởi động ban đầu (kick-off).

> [!example]- Ví dụ
> Công ty A quyết định xây hệ thống CRM mới → Khởi tạo gồm: soạn Project Charter (mục tiêu, phạm vi sơ bộ, ngân sách ước tính), chọn PM, phê duyệt ngân sách ban đầu.

**Kết quả/đặc trưng hoàn thành**
- Project Charter / tài liệu mô tả thông tin sơ bộ dự án được phê duyệt.
- Rõ ràng về ai là nhà tài trợ, ai là PM, phạm vi sơ bộ và các ràng buộc ban đầu.
- Dự án chính thức được “bật” để vào giai đoạn lập kế hoạch.  

### Nhóm quy trình Lập kế hoạch

**Mục tiêu chính:** Tạo **bản kế hoạch quản lý dự án** toàn diện — kế hoạch tổng thể và kế hoạch cho từng miền tri thức (phạm vi, thời gian, chi phí, chất lượng, rủi ro, giao tiếp, nhân lực, mua sắm, bên liên quan, tích hợp).

**Hoạt động tiêu biểu**
- Xác định và phân tích yêu cầu, tạo **WBS** (Work Breakdown Structure).
- Ước lượng thời gian và chi phí, lập lịch, phân bổ nguồn lực.
- Lập kế hoạch quản lý rủi ro, kế hoạch chất lượng, kế hoạch giao tiếp, v.v.
- Thiết lập chỉ số đo lường hiệu suất (KPIs) và phương pháp theo dõi.

> [!example]- Ví dụ
> Với hệ thống CRM, Lập kế hoạch gồm: WBS chi tiết cho các module, lịch 6 tháng, ước lượng nhân lực & chi phí, plan test, plan deploy, kế hoạch chuyển giao và đào tạo người dùng.

**Kết quả/đặc trưng hoàn thành**
- **Kế hoạch quản lý dự án** hoàn chỉnh (và các kế hoạch ở từng miền tri thức).
- Tài liệu ước lượng, WBS, lịch trình và ngân sách được chốt.
- Tiêu chí chấp nhận, quy trình quản lý thay đổi và kế hoạch giao tiếp đã sẵn sàng để thực hiện.  

### Nhóm quy trình Thực hiện

**Mục tiêu chính:** Thực hiện công việc theo kế hoạch để **sản xuất sản phẩm/bàn giao** của dự án.

**Hoạt động tiêu biểu**
- Thi công, phát triển, cấu hình, kiểm thử theo kế hoạch.
- Quản lý đội dự án: giao việc, huấn luyện, giải quyết vấn đề nhân sự.
- Triển khai các hoạt động mua sắm, hợp đồng với nhà cung cấp.
- Quản lý chất lượng trong quá trình thực hiện.

> [!example]- Ví dụ
> Đội dev xây các module CRM, QA chạy test, DBA cấu hình DB, đội triển khai tiến hành deploy môi trường staging; PM điều phối, team leads báo cáo tiến độ.

**Kết quả/đặc trưng hoàn thành**
- Các **sản phẩm bàn giao (deliverables)** được tạo ra: code, module, báo cáo kiểm thử, tài liệu vận hành…
- Các kết quả nghiệm thu từng phần (interim acceptances) nếu có.
- Khi tất cả deliverables hoàn thành và đạt chuẩn kỹ thuật, nhóm Thực hiện chuyển sang bước Bàn giao/nghiệm thu (và nhóm Đóng).

### Nhóm quy trình Kiểm tra - Giám sát

**Mục tiêu chính:** Theo dõi tiến độ, đo lường hiệu suất, phát hiện sai lệch so với kế hoạch và **thực hiện hành động điều chỉnh** để đưa dự án trở lại quỹ đạo.

**Hoạt động tiêu biểu**
- Đo lường tiến độ, chi phí (EVM nếu áp dụng), chất lượng.
- Quản lý thay đổi (Change Control): nhận yêu cầu, đánh giá tác động, phê duyệt thay đổi.
- Kiểm soát rủi ro: theo dõi rủi ro đã nhận diện, áp dụng response.
- Báo cáo trạng thái định kỳ cho nhà tài trợ và các bên liên quan.

> [!example]- Ví dụ
> Trong CRM, phát hiện module X trễ 2 tuần → PM phân tích ảnh hưởng, đàm phán điều chỉnh phạm vi (cắt bớt tính năng không quan trọng) hoặc tăng nguồn lực; cập nhật lịch và thông báo cho sponsor.

**Kết quả/đặc trưng hoàn thành**
- **Báo cáo trạng thái**, nhật ký thay đổi, quyết định phê duyệt/không phê duyệt các change requests.
- Các hành động điều chỉnh (replan, reassign resources, escalate) được thực hiện và ghi nhận.
- Dự án được giữ ổn định hơn theo các ràng buộc về phạm vi/chi phí/thời gian.

### Nhóm quy trình Đóng dự án

**Mục tiêu chính:** Hoàn tất mọi hoạt động, đạt **sự chấp nhận chính thức** cho toàn bộ sản phẩm, lưu trữ tài liệu và rút kinh nghiệm.

**Hoạt động tiêu biểu**
- Xác nhận và thu nhận chữ ký chấp nhận từ khách hàng / sponsor.
- Đóng hợp đồng, thanh toán cho nhà cung cấp.
- Tập hợp, lưu trữ tài liệu dự án (lessons learned, tài liệu bàn giao, người chịu trách nhiệm vận hành).
- Giải thể đội dự án hoặc chuyển nhân lực sang các nhiệm vụ khác.


> [!example]- Ví dụ
> CRM: khách hàng ký biên bản nghiệm thu, PM nộp báo cáo đóng dự án, chuyển giao tài liệu hướng dẫn vận hành cho bộ phận vận hành, họp rút kinh nghiệm.

**Kết quả/đặc trưng hoàn thành**
- **Biên bản chấp nhận toàn bộ sản phẩm bàn giao**; tài liệu đóng dự án; cập nhật kho tri thức tổ chức (lessons learned).
- Dự án chính thức kết thúc; tài nguyên tái phân bổ cho tổ chức.

## Mối quan hệ giữa các nhóm quy trình 🤝

![[Pasted image 20250930090014.png|center|500]]

1. Dự án bắt đầu với các công việc trong nhóm quy trình **Khởi tạo**.
2. Sau đó tiến hành các nhóm quy trình **Lập kế hoạch - Thực hiện - Giám sát** một cách liên tục và lặp lại. Khi thực hiện, luôn có những yêu cầu phát sinh hoặc sai khác so với kế hoạch, nên ta cần kiểm tra giám sát thay đổi để giữ dự án không chệch quy đạo ban đầu. Điều này có thể dẫn đến một số điều chỉnh trong phương pháp thực hiện hoặc cập nhật kế hoạch cho phù hợp với tình huống
3. Khi đạt được mục tiêu của dự án, các công việc trong nhóm quy trình **Đóng dự án** được thực hiện. 
4. Mọi kinh nghiệm, bài học rút ra sẽ trở thành **cải tiến cho các dự án tương lai**.

> [!info] Lưu ý
> - **Quy trình** là một dãy các hành động hướng đến một kết quả cụ thể nào đó
> - Mỗi dự án có thể có nhiều pha/giai đoạn nhưng **tất cả các pha/giai đoạn đều có 5 nhóm quy trình quản lý dự án**.

## Ánh xạ 5 nhóm quy trình tới 10 miền tri thức

Các nhóm quy trình và miền tri thức **không tồn tại độc lập** mà bổ trợ cho nhau.
- **Nhóm quy trình** trả lời: *"Làm khi nào?"*
- **Miền tri thức** trả lời: *"Làm cái gì và như thế nào?"*

Khi kết hợp, chúng tạo nên một *"bản đồ toàn diện"* cho dự án - từ khởi tạo đến đóng dự án, mọi công việc đều có chỗ đứng rõ ràng, giúp PM biết rõ ở từng giai đoạn phải gắn với miền tri thức nào.

> [!example]- Ví dụ
> khi khởi tạo dự án, việc quan trọng là **nhận diện các bên liên quan** và **tài liệu thông tin sơ bộ**. Còn khi đi vào thực hiện, trọng tâm lại chuyển sang **quản lý công việc, chất lượng, nhân lực, giao tiếp…**

|                       | Khởi tạo                                                    | Lập kế hoạch                                                                             | Thực hiện                                           | Kiểm tra - Giám sát                                      | Đóng dự án                                    |
|:--------------------- | ----------------------------------------------------------- | ---------------------------------------------------------------------------------------- | --------------------------------------------------- | -------------------------------------------------------- | --------------------------------------------- |
| **Tích hợp**          | Soạn _Project Charter_ (Tài liệu khởi tạo dự án)            | Xây dựng kế hoạch quản lý dự án (Project Management Plan)                                | Điều phối công việc, quản lý tri thức dự án         | Theo dõi tiến độ tổng thể, xử lý thay đổi tích hợp       | Kết thúc toàn bộ dự án/pha, bàn giao sản phẩm |
| **Phạm vi**           | –                                                           | Thu thập yêu cầu, xác định phạm vi, lập WBS                                              | –                                                   | Thẩm định phạm vi, kiểm soát phạm vi                     | –                                             |
| **Thời gian**         | –                                                           | Xác định hoạt động, ước lượng thời gian, sắp xếp thứ tự, phân bổ tài nguyên, lập tiến độ | –                                                   | Theo dõi tiến độ, cập nhật lịch trình, xử lý chậm trễ    | –                                             |
| **Chi phí**           | –                                                           | Ước lượng chi phí từng hạng mục, xác định ngân sách, phân bổ vốn                         | –                                                   | So sánh chi phí thực tế với kế hoạch, kiểm soát vượt chi | –                                             |
| **Chất lượng**        | –                                                           | Xác định tiêu chuẩn chất lượng, chỉ số kiểm thử                                          | Thực hiện bảo đảm chất lượng, tuân thủ quy trình    | Kiểm tra sản phẩm, chạy test, kiểm soát sai lỗi          | –                                             |
| **Nhân lực**          | –                                                           | Lập kế hoạch nhân sự, mô tả vai trò – trách nhiệm                                        | Tuyển chọn/điều phối nhân sự, đào tạo, gắn kết nhóm | Đánh giá hiệu suất, điều chỉnh nhân sự                   | –                                             |
| **Giao tiếp**         | –                                                           | Xác định thông tin cần trao đổi, chọn kênh (họp, email, chat), tần suất báo cáo          | Tổ chức họp, truyền thông tin, cập nhật tình hình   | Theo dõi hiệu quả truyền thông, xử lý hiểu lầm           | –                                             |
| **Rủi ro**            | –                                                           | Nhận diện rủi ro, phân tích định tính & định lượng, lập kế hoạch ứng phó                 | Triển khai hành động ứng phó (dự phòng, giảm thiểu) | Theo dõi rủi ro, phát hiện mới, cập nhật kế hoạch        | –                                             |
| **Mua sắm**           | –                                                           | Xác định nhu cầu thuê ngoài/mua sắm, lập HĐ & tiêu chí lựa chọn NCC                      | Tiến hành đấu thầu, ký hợp đồng, quản lý NCC        | Theo dõi tiến độ & chất lượng NCC cung cấp               | Nghiệm thu, thanh lý hợp đồng                 |
| **Các bên liên quan** | Nhận diện stakeholder chính, phân tích quyền lực – quan tâm | Lập chiến lược tham gia của stakeholder, kế hoạch tương tác                              | Tổ chức họp stakeholder, duy trì quan hệ            | Giám sát sự tham gia, xử lý xung đột lợi ích             | –                                             |

## Tổng quan về Waterfall và Scrum

