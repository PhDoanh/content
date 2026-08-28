---
publish: false
title: Tổng quan về quản lý dự án
description:
tags:
  - project-management
  - overview
  - explorable
socialDescription:
socialImage:
permalink:
lang: vi
aliases:
cssclasses:
  - img
updated: 2026-02-10
---

Có lần, một startup trẻ ở Hà Nội nhận được hợp đồng xây dựng **ứng dụng quản lý sinh viên** cho một trường đại học. Team rất phấn khích 🎉, nghĩ rằng chỉ cần vài lập trình viên là xong. Nhưng chỉ sau vài tuần, mọi thứ bắt đầu rối tung: deadline dí, tính năng bị thay đổi liên tục, khách hàng phàn nàn, chi phí vượt dự toán.

Ngồi lại sau "cơn bão", họ mới nhận ra: vấn đề không nằm ở code, mà là ở **cách quản lý dự án**. Và đó cũng chính là nội dung mà chúng ta sẽ khám phá ngày hôm nay.

# Dự án và các đặc trưng 🎯

Trước hết, chúng ta cần hiểu: **dự án là gì?**

Theo **PMI (Project Management Institute)**, dự án là một **nỗ lực tạm thời** được thực hiện để tạo ra **một sản phẩm, dịch vụ hoặc kết quả duy nhất**.

📌 Các đặc trưng chính của dự án:
- **Có mục tiêu duy nhất**: mỗi dự án nhắm đến một sản phẩm cụ thể (ví dụ: xây app quản lý sinh viên cho một trường).
- **Có thời gian bắt đầu và kết thúc**: không kéo dài vô hạn như công việc vận hành.
- **Nguồn lực hữu hạn**: gồm kinh phí 💰, nhân lực 👨‍💻, thiết bị ⚙️.
- **Nhiều bên liên quan (stakeholders)**: chủ đầu tư, khách hàng, nhóm dự án, người dùng…
- **Môi trường biến động, nhiều rủi ro**: không dự án nào đi thẳng một đường, luôn có thay đổi bất ngờ.

> [!important] Điểm mấu chốt
> - **dự án ≠ công việc thường ngày**. Ví dụ, nghiên cứu chế tạo vaccine mới là dự án; còn sản xuất vaccine hàng loạt trong nhà máy là **vận hành**.
> - **Dự án CNTT ≠ dự án phần mềm**: dự án CNTT bao hàm dự án phần mềm, gồm 5 thành phần (phần cứng, phần mềm, con người, dữ liệu và quy trình)

# Tiêu chí đánh giá sự thành công ✅

Khi nào thì một dự án được coi là thành công? 🤔  
Câu trả lời nằm ở **bộ ba ràng buộc (triple constraint)**: ^929dd7

1. **Phạm vi (Scope)**: có đúng yêu cầu, đủ tính năng không?
2. **Chi phí (Cost)**: có trong ngân sách không?
3. **Thời gian (Time)**: có hoàn thành đúng hạn không?

Nếu một yếu tố thay đổi → hai yếu tố kia sẽ bị ảnh hưởng (ví dụ: thêm tính năng → tốn thêm thời gian và chi phí).

%% mermaid code for image %%

Ngoài ra, ngày nay thành công còn được đo bằng:
1. **Chất lượng sản phẩm** (quality): thỏa mãn bộ 3 ràng buộc
2.  **Mức độ hài lòng của khách hàng**💡: bao hàm cả mục 1 (thực tế sử dụng nhiều do có công việc khảo sát sự hài lòng sau đóng gói sản phẩm)
3. **Sự đồng thuận của tất cả bên liên quan**: bao hàm cả mục 1 và 2 (ideal nhưng khó đạt).

# Khái niệm quản lý dự án 📚

Quản lý dự án (Project Management) = **ứng dụng kiến thức, kỹ năng, công cụ và kỹ thuật** vào hoạt động dự án nhằm đáp ứng yêu cầu đã đề ra.

%% mermaid code for image %%

PMI chia quản lý dự án thành **10 miền tri thức (knowledge areas)**: ^7eeb7c
1. **Phạm vi (Scope)**: Xác định và kiểm soát **những gì cần làm** và **không cần làm** trong dự án.
2. **Thời gian (Time)**: Lập kế hoạch tiến độ, theo dõi deadline, đảm bảo dự án **xong đúng hạn**.
3. **Chi phí (Cost)**: Dự toán ngân sách, kiểm soát chi tiêu để dự án **không vượt kinh phí**.
4. **Chất lượng (Quality)**: Đảm bảo sản phẩm cuối cùng **đáp ứng tiêu chuẩn và mong đợi của khách hàng**.
5. **Nguồn nhân lực (Human Resources)**: Quản lý team, phân công, xây dựng, phát triển và duy trì tinh thần nhóm.
6. **Giao tiếp (Communication)**: Truyền đạt thông tin rõ ràng, đúng người, đúng lúc để tránh hiểu nhầm.
7. **Rủi ro (Risk)**: Nhận diện sớm nguy cơ, phân tích và lên kế hoạch ứng phó khi có sự cố.
8. **Mua sắm (Procurement)**: Quản lý việc mua hàng hóa, dịch vụ từ bên ngoài (như thuê server, mua phần mềm).
9. **Các bên liên quan (Stakeholder)**: Hiểu nhu cầu, kỳ vọng và quản lý sự tham gia của **chủ đầu tư, khách hàng, đội phát triển, nhà cung cấp, các chuyên gia (nhóm chuyên môn)**.
10. **Tích hợp (Integration)**: Đảm bảo mọi mảng trên **ăn khớp với nhau**, tạo thành một dự án thống nhất.

👉 Quản lý dự án không chỉ là "theo dõi tiến độ", mà còn bao quát gần như **mọi khía cạnh sống còn** của dự án.

# Chương trình và danh mục dự án 🗂️

Hai khái niệm dễ gây nhầm lẫn:

- **Chương trình (Program):** tập hợp nhiều dự án có liên quan, nhằm đạt mục tiêu lớn hơn. Ví dụ: chương trình "Chuyển đổi số đại học" bao gồm dự án phát triển hệ thống e-learning, dự án quản lý sinh viên, dự án cổng thông tin.

- **Danh mục dự án (Portfolio):** tập hợp tất cả các chương trình và dự án của tổ chức, được quản lý ở mức chiến lược. Ví dụ: một trường đại học có danh mục gồm cả dự án CNTT, dự án xây dựng cơ sở vật chất, dự án hợp tác quốc tế.

📌 Điểm khác biệt: **Program = thực thi chiến lược, Portfolio = lựa chọn chiến lược.**

> [!question]- Bạn có biết?
> Mỗi phần mềm thường được dùng trong doanh nghiệp như: ERP, CRM, Office 365, Kế toán, Bán hàng, Quản lý kho, HR, ... Tương ứng với **một dự án** được triển khai để đưa vào sử dụng trong doanh nghiệp

# Kỹ năng cần có của nhà quản lý dự án 🧑‍🏫

Nhà quản lý dự án (Project Manager - PM) không chỉ là người "giữ deadline" 😅, mà còn là **linh hồn** của dự án. Các nhóm kỹ năng chính:

## 1. Kỹ năng mềm 
Mô tả những kỹ năng hướng tới con người của nhà quản lý dự án

1. Giao tiếp đa chiều (nghe, nói, viết, thuyết trình, ...)
2. Chính trực, đạo dức và nhất quán 
3. Xây dựng niềm tin
4. Quản lý thời gian và ưu tiên công việc
5. Khả năng thích ứng và linh hoạt tùy bối cảnh

## 2. Chuyên môn
Mô tả những kỹ năng hướng tới kỹ thuật của nhà quản lý dự án

1. Am hiểu quy trình, công cụ (Gantt Chart, Agile, Scrum, PMBOK…).
2. Xây dựng nhóm dự án
3. Phân tích chiến lược
4. Quản lý phạm vi, chi phí, tiến độ, chất lượng
5. Quản lý rủi ro và xây dựng phương án dự phòng
6. Quản lý nguồn nhân lực (nhân sự, vật tư, tài chính)

## 3. Tố chất cá nhân
Mô tả những kỹ năng hướng tới tố chất, tiềm năng của nhà quản lý dự án (là một nhánh của kỹ năng mềm)

1. Quản lý xung đột 
2. Tư duy phản biện và khả năng giải quyết vấn đề
3. Thương lượng
4. Hiểu và cân bằng ưu tiên các công việc
5. Tầm nhìn chiến lược

> [!tip] Mẹo
> Một PM giỏi thường vừa là **"thủ lĩnh"** dẫn dắt team, vừa là **"người cầu nối"** giữa khách hàng, lãnh đạo và đội phát triển.

# Vấn đề đạo đức nghề nghiệp ⚖️

Trong quản lý dự án CNTT/phần mềm, **đạo đức nghề nghiệp** giữ vai trò sống còn.

PMI có **Code of Ethics & Professional Conduct** với 4 giá trị cốt lõi:
- **Trách nhiệm (Responsibility)**: chịu trách nhiệm cho quyết định và hành động của mình (điều mà nhà quản lý dự án khó đạt được nhất)
- **Tôn trọng (Respect)**: với đồng nghiệp, khách hàng, stakeholder.
- **Công bằng (Fairness)**: không thiên vị, minh bạch.
- **Trung thực (Honesty)**: báo cáo rõ ràng, không che giấu rủi ro hay sai sót.

👉 Thiếu đạo đức = mất niềm tin = dự án sụp đổ nhanh hơn cả lỗi kỹ thuật.
 
# Kết luận ✨

Tóm lại, để thành công trong **quản lý dự án phần mềm**, bạn cần:
- Hiểu rõ **đặc trưng dự án** và cách đánh giá thành công.
- Nắm chắc **10 miền tri thức** quản lý dự án.
- Biết phân biệt **program - portfolio** để không bị lẫn lộn cấp độ.
- Trau dồi **kỹ năng cứng + kỹ năng mềm + đạo đức nghề nghiệp**.

Quản lý dự án không chỉ là một nghề, mà còn là một nghệ thuật 🎨 - nơi công nghệ, con người và chiến lược hòa quyện để biến ý tưởng thành hiện thực.