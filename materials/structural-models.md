---
date: 2025-03-23
draft: false
status: Doing
title: Các mô hình kiến trúc hệ thống trong phát triển phần mềm
description: Bài viết này giải thích chi tiết về structural models trong phần mềm, từ mô hình tĩnh đến mô hình động, bao gồm class diagrams, generalization và aggregation, giúp bạn hiểu sâu hơn về kiến trúc hệ thống.
author: PhDoanh
authorlink: https://github.com/PhDoanh
tags:
  - software-technology
  - development
  - sofware-engineer
  - system-modeling
  - structural-models
aliases:
  - structural models
cssclasses:
  - img
  - btn
---
%% LƯU Ý 
- Định dạng tên file: "tên-bài-viết" (jp-typing-guide, ...) 
%%

%% banner
<figure style="text-align: center; margin: 20px auto;">
  <img 
    src="images/structural-models.png"
    alt="Khám phá Structural Models: Kiến trúc hệ thống từ lớp, đối tượng đến mối quan hệ" 
    style="
      width: 90%;
      height: auto;
      display: block;
      margin: 0 auto;
      border-radius: 8px;
      box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    "
  >
  <figcaption style="
    font-style: italic;
    color: #666;
    margin-top: 10px;
    font-size: 1em;
    padding: 0 10px;
  ">
    <em>caption</em>
  </figcaption>
</figure>
 %%

**Structural models** của phần mềm thể hiện tổ chức của hệ thống dưới dạng các thành phần cấu tạo và mối quan hệ giữa chúng. Các mô hình này có thể là **mô hình tĩnh** (hiển thị cấu trúc thiết kế hệ thống) hoặc **mô hình động** (cho thấy cách hệ thống vận hành khi đang chạy). Việc hiểu rõ sự khác biệt giữa chúng giúp các nhà phát triển đưa ra quyết định thiết kế chính xác nhằm tối ưu hiệu suất và độ tin cậy của hệ thống. 

# Giới thiệu

**Structural models** là bước quan trọng khi thảo luận và thiết kế kiến trúc hệ thống. Chúng không chỉ hỗ trợ việc hình dung các thành phần chính của hệ thống mà còn giúp xác định **mối quan hệ** giữa chúng. Từ đó đảm bảo rằng thiết kế hệ thống đáp ứng được yêu cầu của dự án.  Có 2 kiểu mô hình chính như sau:

- **Mô hình tĩnh:**  Đưa ra cái nhìn tổng quan về các thành phần (như các lớp trong hệ thống) và mối quan hệ giữa chúng.  

> [!example]- Ví dụ
> Class diagrams, component diagrams, package diagrams, ...

- **Mô hình động:** Mô phỏng hành vi của hệ thống khi đang chạy, ví dụ như sự tương tác giữa các luồng hoặc đối tượng.  
  
> [!example]- Ví dụ
> Sequence diagrams, statecharts, activity diagrams, ...

> [!info] Lưu ý
> Mô hình tĩnh chỉ thể hiện cấu trúc "khung xương" của hệ thống, trong khi mô hình động cần mô phỏng các luồng tương tác thực tế khi hệ thống đang chạy, nên đừng nhầm lẫn giữa hai loại mô hình này, vì mô hình động thường phức tạp hơn và cần được thiết kế cẩn thận để phản ánh đúng hành vi của hệ thống.

---

# Class Diagrams

**Class diagrams** là công cụ chủ yếu trong việc mô hình hóa cấu trúc tĩnh của hệ thống **hướng đối tượng**.

- **Class:** Một định nghĩa chung cho một loại đối tượng, chứa các thuộc tính (attributes) và phương thức (operations).
- **Association:** Liên kết giữa các lớp, biểu thị mối quan hệ tồn tại giữa chúng.
- **Multiplicity:** Chỉ ra số lượng đối tượng tham gia trong mối quan hệ (ví dụ: 1:1, 1..*, 1..4).

> [!example]- Ví dụ
> Trong một hệ thống y tế, lớp `Patient` có thể được liên kết với lớp `PatientRecord` theo mối quan hệ 1:1 (một bệnh nhân chỉ có một hồ sơ bệnh án duy nhất). Ngoài ra, lớp `Patient` có thể có mối quan hệ 1..* với lớp `Condition`, cho thấy một bệnh nhân có thể mắc nhiều tình trạng bệnh khác nhau.

> [!tip]- Mẹo
> Bắt đầu bằng cách xác định các đối tượng quan trọng trong "thế giới thực" và chuyển chúng thành các lớp trong hệ thống. Sau đó, xác định rõ ràng mối quan hệ giữa các lớp để có được sơ đồ rõ ràng.

---

# Generalization

Generalization (tổng quát hóa) là kỹ thuật quản lý sự phức tạp bằng cách nhóm các đối tượng có đặc điểm chung thành một lớp cha.

**Generalization** cho phép các lớp con (subclasses) kế thừa các thuộc tính và phương thức của lớp cha (superclass). Giúp tái sử dụng thông tin, giảm thiểu việc lặp lại và dễ dàng quản lý thay đổi ở mức độ tổng quát.

> [!example]- Ví dụ
> Trong hệ thống y tế, các loại bác sĩ như `GeneralPractitioner` và `HospitalDoctor` có thể được tổng quát hóa thành lớp `Doctor`. Các thuộc tính chung như `Name` và `Phone` được định nghĩa trong lớp `Doctor`, trong khi các lớp con có thể bổ sung thêm thuộc tính riêng như `StaffNumber` hoặc `PracticeAddress`.

> [!info] Lưu ý
> Khi sử dụng **generalization**, hãy đảm bảo rằng các đặc tính chung thật sự phù hợp với tất cả các lớp con để tránh gây nhầm lẫn.

---

# Aggregation

Aggregation (tập hợp) biểu thị mối quan hệ "toàn phần - bộ phận" giữa các lớp. Một mối quan hệ đặc biệt trong đó một đối tượng (toàn phần) được tạo thành từ các đối tượng khác (bộ phận). Trong UML, aggregation được biểu diễn bằng hình thoi trống ở phía đối tượng toàn phần.

> [!example]- Ví dụ
> 
> Một `PatientRecord` có thể được xem là một tổng hợp của đối tượng `Patient` và nhiều đối tượng `Consultation`. Điều này có nghĩa là hồ sơ bệnh nhân sẽ chứa thông tin cá nhân cũng như các cuộc tư vấn riêng lẻ của bệnh nhân với bác sĩ.

> [!tip]- Mẹo
> Sử dụng **aggregation** để biểu diễn cấu trúc của dữ liệu một cách trực quan và dễ hiểu. Điều này giúp trong việc thiết kế cơ sở dữ liệu và cải thiện khả năng bảo trì hệ thống.

---

# Các câu hỏi thường gặp

> [!caution]- Nội dung đang hoàn thiện
> Quá trình xây dựng nội dung này có thể mất nhiều thời gian ⌛, nhưng bạn có thể thúc đẩy nó bằng cách tham gia [[article-collaboration-guide|cộng tác bài viết]] 🤝
> 
> **Rất mong sự thông cảm của các bạn 🙏**

---

# Tổng kết

**Structural models** là một phần không thể thiếu trong **thiết kế kiến trúc hệ thống phần mềm**.  
- **Mô hình tĩnh** cung cấp cái nhìn tổng quan về các thành phần của hệ thống và các mối quan hệ giữa chúng, được thể hiện qua **class diagrams**, **generalization** và **aggregation**.
- **Mô hình động** giúp mô phỏng hành vi của hệ thống khi đang chạy, tạo điều kiện để phát hiện sớm các vấn đề tương tác.

Bằng cách sử dụng các **structural models** một cách hợp lý, bạn có thể đảm bảo rằng hệ thống được xây dựng một cách vững chắc, dễ bảo trì và mở rộng trong tương lai. Hãy nhớ rằng một thiết kế rõ ràng ngay từ đầu sẽ giúp tiết kiệm chi phí và thời gian phát triển, đồng thời nâng cao hiệu suất của hệ thống! 😊

