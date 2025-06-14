---
date: 2025-03-19
draft: false
status: Done
title: "Tài Liệu Yêu Cầu Phần Mềm Chuẩn: Hướng Dẫn Requirements Specification Toàn Diện"
description: Bài viết này giải thích chi tiết quy trình requirements specification trong phát triển phần mềm, từ cách viết yêu cầu người dùng đến mô tả yêu cầu hệ thống bằng ngôn ngữ tự nhiên, cấu trúc và các ký hiệu chuyên ngành. Tìm hiểu những lưu ý, ví dụ và mẹo thiết thực để xây dựng tài liệu yêu cầu chất lượng 🚀
author: PhDoanh
authorlink: https://github.com/PhDoanh
tags:
  - software-technology
  - development
  - sofware-engineer
  - requirements-engineering
  - processes
  - specification
aliases:
  - requirements specification
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
    src="images/requirements-specification.png"
    alt="Tài Liệu Yêu Cầu Phần Mềm Chuẩn: Hướng Dẫn Requirements Specification Toàn Diện  " 
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

**Requirements specification** là quá trình ghi chép lại các yêu cầu của người dùng và hệ thống vào một tài liệu yêu cầu chính thức. Mục tiêu của quá trình này là tạo ra một tài liệu **rõ ràng**, **không mập mờ**, **dễ hiểu**, **đầy đủ** và **nhất quán**. Tuy nhiên, trong thực tế, việc đạt được tất cả các tiêu chí này là khá khó khăn do sự đa dạng trong cách hiểu và diễn giải của các **stakeholders**.

# Giới thiệu

Quá trình **requirements specification** đóng vai trò quan trọng trong việc chuyển hóa những ý tưởng ban đầu thành tài liệu cụ thể, là cơ sở cho việc thiết kế, phát triển và kiểm thử hệ thống. Tài liệu này được sử dụng bởi:

- **Người dùng (Users):** Để đảm bảo rằng hệ thống sẽ đáp ứng được các chức năng và tính năng cần thiết.

- **Nhà phát triển (Developers) và Kiểm thử (Testers):** Để hiểu rõ cách thức hoạt động và các ràng buộc của hệ thống.

- **Các bên liên quan khác:** Như quản lý dự án, nhà đầu tư, và bộ phận bảo trì hệ thống.

> [!info] Lưu ý
> Trong tài liệu yêu cầu, **yêu cầu người dùng** nên chỉ mô tả hành vi bên ngoài của hệ thống, tránh sử dụng thuật ngữ kỹ thuật quá phức tạp. Ngược lại, **yêu cầu hệ thống** có thể mở rộng thành các mô tả chi tiết hơn nhằm làm rõ cách hệ thống thực hiện các chức năng đó.

# Yêu cầu người dùng và hệ thống

## Yêu cầu người dùng
**Yêu cầu người dùng** mô tả những gì hệ thống cần làm từ góc nhìn của người sử dụng. Nó không đi sâu vào chi tiết kỹ thuật mà tập trung vào **chức năng và trải nghiệm** của người dùng.

**Đặc điểm**:
- Được viết bằng **ngôn ngữ tự nhiên**, tránh dùng thuật ngữ kỹ thuật phức tạp.
- Dễ đọc, dễ hiểu với mọi đối tượng liên quan (người dùng, quản lý, nhà đầu tư).
- Miêu tả hành vi bên ngoài của hệ thống (hệ thống phải làm gì).

> [!example]- Vi dụ
> **Yêu cầu người dùng** trong hệ thống đặt vé xem phim online:
> - Người dùng có thể **xem danh sách phim** theo ngày chiếu.
> - Người dùng có thể **chọn ghế và đặt vé** trực tuyến.
> - Người dùng có thể **hủy vé đã đặt** trước giờ chiếu 1 tiếng.
> - Người dùng có thể **thanh toán bằng thẻ tín dụng hoặc ví điện tử**.
> 
> Đây là các yêu cầu mô tả những gì người dùng có thể làm, không đề cập đến cách hệ thống thực hiện chúng.

> [!example]- Ví dụ
> **Yêu cầu người dùng** trong ứng dụng học tiếng Nhật:
> - Người dùng có thể **tạo tài khoản và đăng nhập** bằng email hoặc Google.
> - Ứng dụng sẽ **gợi ý bài học phù hợp** dựa trên cấp độ hiện tại của người học.
> - Người dùng có thể **lưu lại từ vựng yêu thích** để ôn tập sau.
> - Ứng dụng sẽ **gửi thông báo nhắc nhở học bài hàng ngày**.

---

## Yêu cầu hệ thống
**Yêu cầu hệ thống** là bản mở rộng của yêu cầu người dùng, giải thích **hệ thống sẽ thực hiện các yêu cầu đó như thế nào**. Nó thường có nhiều chi tiết hơn và có thể bao gồm các yếu tố kỹ thuật.

**Đặc điểm**:
- Được viết rõ ràng, có thể sử dụng **mô hình UML, thuật toán hoặc biểu đồ** để minh họa.
- Giải thích chi tiết về **cách hệ thống xử lý yêu cầu của người dùng**.
- Có thể chia thành **yêu cầu chức năng** (Functional Requirements) và **yêu cầu phi chức năng** (Non-Functional Requirements).

> [!example]- Ví dụ
> **Yêu cầu hệ thống** trong Hệ thống đặt vé xem phim online:
> - Hệ thống **lấy danh sách phim từ cơ sở dữ liệu** và hiển thị theo ngày chiếu.
> - Khi người dùng đặt vé, hệ thống **kiểm tra số ghế còn trống trước khi xác nhận đơn hàng**.
> - Nếu người dùng hủy vé, hệ thống **tự động hoàn tiền vào ví điện tử trong vòng 24h**.
> - Hệ thống **mã hóa dữ liệu thanh toán theo chuẩn PCI-DSS** để đảm bảo bảo mật.
>
> **Điểm khác biệt so với yêu cầu người dùng:**
> - Có thêm chi tiết về **cách hệ thống xử lý thông tin** (kiểm tra ghế trống, mã hóa dữ liệu).
> - Mô tả các **quy tắc nghiệp vụ** như hoàn tiền trong vòng 24h.

> [!example]- Ví dụ
> **Yêu cầu hệ thống** trong Ứng dụng học tiếng Nhật
> - Hệ thống **lưu điểm số và tiến trình học tập** vào database MongoDB.
> - Khi người dùng chọn từ vựng yêu thích, ứng dụng **lưu từ đó vào danh sách riêng của người dùng**.
> - Hệ thống **gửi thông báo nhắc nhở học tập thông qua Firebase Cloud Messaging (FCM)** mỗi ngày lúc 8 giờ sáng.
> - Hệ thống **sử dụng API Google Translate để cung cấp nghĩa của từ vựng**.
>
> **Điểm khác biệt so với yêu cầu người dùng:**
> - Xác định **công nghệ cụ thể** (MongoDB, Firebase, API Google Translate).
> - Cung cấp chi tiết về **cách hệ thống lưu dữ liệu và xử lý** (lưu điểm số, gửi thông báo).

**So sánh Yêu cầu Người dùng và Yêu cầu Hệ thống**

| Tiêu chí              | Yêu cầu Người dùng                          | Yêu cầu Hệ thống                                                                     |
| --------------------- | ------------------------------------------- | ------------------------------------------------------------------------------------ |
| **Mục tiêu**          | Mô tả chức năng từ góc nhìn của người dùng  | Mô tả cách hệ thống thực hiện các chức năng đó                                       |
| **Độ chi tiết**       | Khái quát, dễ hiểu                          | Chi tiết, mang tính kỹ thuật hơn                                                     |
| **Đối tượng sử dụng** | Người dùng, quản lý, nhà đầu tư             | Nhà phát triển, kỹ sư phần mềm, tester                                               |
| **Ví dụ**             | "Người dùng có thể đặt vé xem phim online." | "Hệ thống kiểm tra ghế trống, lưu thông tin vé vào database, và gửi email xác nhận." |

---

# Các phương pháp ghi chép yêu cầu

Ghi chép yêu cầu là bước quan trọng trong **phát triển phần mềm** để đảm bảo:  
- Hiểu đúng nhu cầu của người dùng.  
- Tránh hiểu sai hoặc thiếu sót khi phát triển.  
- Giúp các bên liên quan (khách hàng, lập trình viên, tester, quản lý) có cùng một nhận thức về hệ thống.  
- Hỗ trợ kiểm tra và đánh giá phần mềm sau khi triển khai.

## Ngôn ngữ tự nhiên
Ghi chép yêu cầu dưới dạng **tài liệu đặc tả (SRS - Software Requirement Specification)** bằng ngôn ngữ tự nhiên. Là cách phổ biến nhất, phù hợp với **mọi dự án**. Dễ viết, dễ đọc, nhưng có thể gây hiểu nhầm do thiếu tính trực quan.

> [!example]- Ví dụ
> **Yêu cầu:** Người dùng có thể **đăng ký tài khoản** bằng email và mật khẩu. 
>
> **Ghi chép theo dạng văn bản:**
> - Hệ thống phải cho phép người dùng nhập địa chỉ email hợp lệ và mật khẩu ít nhất 8 ký tự.  
> - Sau khi đăng ký, hệ thống gửi email xác nhận để kích hoạt tài khoản.

> [!info] Lưu ý
> - **Nhất quán:** Sử dụng định dạng chuẩn cho tất cả các yêu cầu.  
> - **Tô đậm các từ khóa:** Như **"shall"** cho yêu cầu bắt buộc.

> [!tip]- Mẹo
> Ghi kèm **rationale** (lý do) cho mỗi yêu cầu để biết nguồn gốc và mục đích của yêu cầu đó.

## Yêu cầu có cấu trúc
Sử dụng mẫu chuẩn, biểu mẫu hoặc bảng để ghi chép yêu cầu. Giúp giảm thiểu sự mập mờ và đảm bảo các yêu cầu được tổ chức theo một cấu trúc nhất định. Nhưng có thể mất nhiều thời gian để duy trì.

> [!example]- Ví dụ
> Ghi chép dưới dạng bảng:
> 
> |ID|Mô tả yêu cầu|Loại yêu cầu|Mức độ ưu tiên|
> |---|---|---|---|
> |FR001|Người dùng có thể đăng ký tài khoản bằng email|Chức năng|Cao|
> |FR002|Hệ thống gửi email xác nhận khi đăng ký|Chức năng|Trung bình|
> |NFR001|Hệ thống xử lý đăng ký trong vòng 3 giây|Phi chức năng|Cao|

## Các ký hiệu đồ họa và mô hình UML
Sử dụng sơ đồ **use case, sequence diagram và state chart** để minh họa cách thức tương tác giữa người dùng và hệ thống. Cách này giúp trực quan, dễ hiểu, phù hợp với phân tích hệ thống, nhưng không mô tả chi tiết từng bước. Nên phù hợp với các nhà phát triển và tester có nền tảng kỹ thuật hơn.

> [!caution]- Nội dung đang hoàn thiện
> Quá trình xây dựng nội dung này có thể mất nhiều thời gian ⌛, nhưng bạn có thể thúc đẩy nó bằng cách tham gia [[article-collaboration-guide|cộng tác bài viết]] 🤝
> 
> **Rất mong sự thông cảm của các bạn 🙏**

## Use cases
Mô tả các tình huống tương tác cụ thể giữa người dùng và hệ thống.

> [!example]- Ví dụ
> **Use case "Setup consultation":** Cho phép nhiều bác sĩ từ các văn phòng khác nhau cùng xem và chỉnh sửa hồ sơ bệnh nhân, với một bác sĩ khởi tạo cuộc tư vấn và các bác sĩ khác chỉ xem thông tin.

> [!tip]- Mẹo
> Dùng sơ đồ use case để tổng hợp các tương tác chính, sau đó phát triển các **scenario** chi tiết nếu cần.

---

# Tài liệu yêu cầu phần mềm

Tài liệu **SRS** là bản cam kết giữa khách hàng và đội ngũ phát triển, bao gồm:
- **Phần mở đầu:** Giới thiệu mục đích, đối tượng độc giả và lịch sử phiên bản.
- **Yêu cầu người dùng:** Mô tả các dịch vụ và tính năng mà hệ thống cần cung cấp.
- **Kiến trúc hệ thống:** Tổng quan về cách phân chia các chức năng giữa các module.
- **Yêu cầu hệ thống chi tiết:** Bao gồm cả yêu cầu chức năng và phi chức năng.
- **Mô hình hệ thống:** Sơ đồ mối quan hệ, luồng dữ liệu, và các mô hình UML.
- **Dự đoán phát triển hệ thống:** Những thay đổi dự kiến trong tương lai.
- **Phụ lục và chỉ mục:** Thông tin chi tiết bổ sung và danh mục các mục lục để dễ dàng tra cứu.

> [!info] Lưu ý
> Khi tài liệu yêu cầu quá chi tiết, đặc biệt với các hệ thống phức tạp, cần có bảng mục lục và chỉ mục rõ ràng để người đọc dễ dàng tra cứu thông tin.

---

# Các câu hỏi thường gặp

> [!caution]- Nội dung đang hoàn thiện
> Quá trình xây dựng nội dung này có thể mất nhiều thời gian ⌛, nhưng bạn có thể thúc đẩy nó bằng cách tham gia [[article-collaboration-guide|cộng tác bài viết]] 🤝
> 
> **Rất mong sự thông cảm của các bạn 🙏**

---

# Tổng kết

**Requirements specification** là quá trình quan trọng giúp chuyển hóa các yêu cầu từ dạng ý tưởng thành một tài liệu chính thức, làm cơ sở cho thiết kế và phát triển hệ thống.  

- **Yêu cầu người dùng** phải rõ ràng, dễ hiểu và chỉ tập trung vào hành vi bên ngoài của hệ thống.  

- **Yêu cầu hệ thống** cung cấp chi tiết hơn về cách hệ thống thực hiện các chức năng đó, thường sử dụng các ký hiệu đồ họa và mô hình kỹ thuật.  

- **Các phương pháp ghi chép yêu cầu** như sử dụng ngôn ngữ tự nhiên, cấu trúc yêu cầu và mô hình UML giúp đảm bảo tài liệu không chỉ đầy đủ mà còn dễ hiểu đối với mọi đối tượng người đọc.  

Nhờ vào việc kết hợp chặt chẽ giữa các phương pháp này, bạn có thể xây dựng một **tài liệu yêu cầu phần mềm** chất lượng, góp phần đảm bảo thành công cho dự án phát triển hệ thống 🚀. Hãy luôn nhớ rằng, **sự nhất quán**, **tính rõ ràng** và **đầy đủ thông tin** là chìa khóa để tạo ra một tài liệu SRS hiệu quả.
