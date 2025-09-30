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


