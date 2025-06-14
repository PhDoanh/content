---
date: 2025-02-24
draft: false
status: Doing
title: Mô hình thác nước cổ điển trong phát triển phần mềm
description: Mô hình thác nước (Waterfall Model) là mô hình phát triển phần mềm cổ điển, được áp dụng rộng rãi trong nhiều dự án CNTT trên toàn cầu. Bài viết này sẽ giúp bạn hiểu rõ về các giai đoạn của mô hình, những ưu và nhược điểm, cũng như khi nào nên áp dụng.
author: PhDoanh
authorlink: https://github.com/PhDoanh
tags:
  - software-technology
  - development
  - sofware-engineer
  - process-models
aliases:
  - waterfall model
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
    src="images/waterfall-model.png"
    alt="Mô hình thác nước trong công nghệ phần mềm" 
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

# 🌊 Mô hình thác nước là gì?

Mô hình thác nước là một quy trình phát triển phần mềm **tuân theo trình tự nghiêm ngặt** từ bước này sang bước khác, tương tự như nước chảy từ thác xuống. Mỗi giai đoạn chỉ bắt đầu khi giai đoạn trước đã hoàn thành, tạo ra một luồng công việc **liên tục và không quay lại**.

> [!check] Ưu điểm
> - **Dễ hiểu và quản lý** nhờ vào tính tuân thủ và cấu trúc rõ ràng, giúp việc theo dõi tiến độ dễ dàng hơn.
> - **Tài liệu rõ ràng**, giúp dễ dàng bảo trì và nâng cấp do mọi bước đều được ghi chép cụ thể. 
> - **Phù hợp với các dự án nhỏ** có yêu cầu rõ ràng từ đầu, giúp giảm thiểu rủi ro khi thay đổi giữa các giai đoạn.

> [!missing] Nhược điểm
> - **Khó thay đổi** khi đã hoàn tất giai đoạn trước, do mô hình này không cho phép quay lại các bước trước đó mà không gây ảnh hưởng lớn đến tiến độ. 
> - **Tốn nhiều thời gian** trước khi sản phẩm hoàn chỉnh được triển khai, do từng giai đoạn phải hoàn thành 100% trước khi chuyển sang bước tiếp theo.
> - **Không phù hợp với các dự án phức tạp**, đòi hỏi sự thay đổi linh hoạt hoặc có yêu cầu chưa rõ ràng ngay từ đầu.

---

# 🏗️ Các giai đoạn trong mô hình thác nước

## Yêu cầu hệ thống

Giai đoạn này bao gồm việc **thu thập, phân tích và xác định rõ ràng** các yêu cầu từ khách hàng hoặc người dùng cuối. Quá trình này thường bao gồm **phỏng vấn, khảo sát, nghiên cứu tài liệu hiện có và phân tích các hệ thống tương tự**. Kết quả của giai đoạn này sẽ là một tài liệu chi tiết **mô tả yêu cầu hệ thống**, bao gồm các chức năng cốt lõi, yêu cầu hiệu suất, ràng buộc kỹ thuật và các tiêu chí chấp nhận phần mềm.

> [!info] Lưu ý
> Việc xác định yêu cầu đầy đủ và chính xác ngay từ đầu là rất quan trọng, vì những thay đổi sau này có thể gây tốn kém và ảnh hưởng đến tiến độ dự án.

## Thiết kế hệ thống

Sau khi yêu cầu được xác định, nhóm phát triển tiến hành thiết kế **kiến trúc tổng thể** các thành phần, giao diện và cơ chế hoạt động của hệ thống. Giai đoạn này bao gồm việc tạo ra các **mô hình dữ liệu, sơ đồ luồng thông tin và kiến trúc phần mềm** để đảm bảo tính nhất quán và hiệu quả trong triển khai.

- **Thiết kế kiến trúc**: Xác định cách các thành phần hệ thống liên kết với nhau, bao gồm cơ sở dữ liệu, máy chủ và giao diện người dùng. 
- **Thiết kế giao diện**: Tạo các mô hình UI/UX để đảm bảo trải nghiệm người dùng tốt nhất. 
- **Thiết kế mô-đun**: Phân chia hệ thống thành các mô-đun nhỏ hơn để dễ dàng phát triển và bảo trì.

> [!info] Lưu ý
> Một thiết kế tốt giúp giảm thiểu rủi ro trong quá trình lập trình và kiểm thử, đồng thời cải thiện khả năng bảo trì sau này.

## Triển khai và lập trình

Giai đoạn này bắt đầu với việc các lập trình viên viết mã **dựa trên thiết kế chi tiết đã xác định**. Họ sử dụng các công nghệ, ngôn ngữ lập trình phù hợp và tuân theo các tiêu chuẩn mã hóa để đảm bảo tính hiệu quả và bảo trì dễ dàng.

- **Quy trình phát triển**: Mã nguồn được viết theo các module đã thiết kế, tích hợp từng phần một để đảm bảo hệ thống hoạt động đúng như mong đợi.
- **Kiểm soát phiên bản**: Áp dụng các công cụ như Git để theo dõi và quản lý mã nguồn, giúp kiểm soát các thay đổi trong suốt quá trình phát triển.
- **Tài liệu mã nguồn**: Ghi chú chi tiết trong mã để giúp việc bảo trì sau này dễ dàng hơn.

> [!info] Lưu ý
> Việc tuân thủ chặt chẽ các quy tắc mã hóa và kiểm soát phiên bản sẽ giúp tránh lỗi và nâng cao hiệu suất phát triển phần mềm.

## Kiểm thử hệ thống

Sau khi lập trình, hệ thống được **kiểm thử tất cả các chức năng** nhằm phát hiện và khắc phục lỗi. Giai đoạn này bao gồm nhiều cấp độ kiểm thử như **kiểm thử đơn vị (Unit Testing), kiểm thử tích hợp (Integration Testing), kiểm thử hệ thống (System Testing) và kiểm thử chấp nhận (Acceptance Testing)** để đảm bảo rằng phần mềm hoạt động đúng theo yêu cầu.

- **Kiểm thử đơn vị**: Mỗi thành phần nhỏ của hệ thống được kiểm tra độc lập để phát hiện lỗi ngay từ sớm.
- **Kiểm thử tích hợp**: Các module được kết nối với nhau và kiểm tra khả năng tương tác giữa chúng.
- **Kiểm thử hệ thống**: Đánh giá toàn bộ hệ thống để đảm bảo tính toàn vẹn và ổn định. 
- **Kiểm thử chấp nhận**: Kiểm tra phần mềm từ góc độ người dùng cuối trước khi triển khai chính thức.

> [!info] Lưu ý
> Việc kiểm thử kỹ lưỡng giúp giảm thiểu rủi ro và đảm bảo sản phẩm có chất lượng cao trước khi phát hành.

## Triển khai và bảo trì

Phần mềm được triển khai cho khách hàng thông qua các phương thức như cài đặt trực tiếp, cập nhật từ xa hoặc triển khai trên nền tảng đám mây. Quá trình bảo trì bao gồm **sửa lỗi, nâng cấp tính năng, tối ưu hiệu suất và hỗ trợ người dùng** để đảm bảo hệ thống hoạt động ổn định.

- **Bảo trì sửa lỗi**: Khắc phục các lỗi phát sinh sau khi triển khai.
- **Bảo trì thích ứng**: Điều chỉnh phần mềm để tương thích với môi trường mới. 
- **Bảo trì hoàn thiện**: Cải thiện hiệu suất và nâng cấp tính năng dựa trên phản hồi từ người dùng. 
- **Bảo trì phòng ngừa**: Dự đoán và sửa lỗi tiềm ẩn để tránh sự cố trong tương lai.

> [!info] Lưu ý
> Việc bảo trì định kỳ giúp kéo dài tuổi thọ phần mềm và tối ưu trải nghiệm người dùng.

---

# 🔍 Khi nào nên dùng mô hình thác nước?
Mô hình "thác nước" (Waterfall) thường được áp dụng trong các dự án có yêu cầu rõ ràng, ít thay đổi trong suốt quá trình thực hiện. Dưới đây là một số đặc điểm của dự án phù hợp để áp dụng mô hình này:

1. **Dự án có yêu cầu rõ ràng ngay từ đầu**
	- Mô hình thác nước là tuyến tính và từng bước, vì vậy các yêu cầu cần được xác định rõ ràng từ đầu, và ít có sự thay đổi trong suốt quá trình phát triển.
	- Thường áp dụng cho các dự án có yêu cầu ổn định và không thay đổi nhiều.

> [!example]- Ví dụ
> **Hệ thống phần mềm cho các doanh nghiệp có yêu cầu chắc chắn** (như hệ thống kế toán, phần mềm quản lý nhân sự).

2. **Dự án có quy trình phát triển dễ hiểu và chuẩn hóa**
	- Mô hình này thích hợp cho các dự án có quy trình phát triển dễ dàng chuẩn hóa và có thể áp dụng các bước tuần tự mà không cần quá nhiều điều chỉnh.

3. **Dự án không cần phải tương tác nhiều với khách hàng trong suốt quá trình phát triển**
	- Các dự án như xây dựng phần mềm cho các hệ thống hoặc ứng dụng có tính chất tương đối ổn định, ít yêu cầu thay đổi trong suốt quá trình phát triển.
	- Thường không cần liên tục phản hồi với khách hàng hoặc người sử dụng trong suốt quá trình.

4. **Dự án có thời gian và nguồn lực không thay đổi**
	- Dự án này thường có ngân sách và thời gian được xác định rõ ràng từ ban đầu.
	- Mô hình thác nước không linh động như Agile, do đó rất thích hợp cho các dự án có yêu cầu khối lượng công việc và thời gian hoàn thành cụ thể.

> [!example]- Ví dụ
> **Dự án xây dựng hạ tầng phần mềm cho các ứng dụng cố định**: Các ứng dụng này không cần phải thay đổi và nâng cấp liên tục.

5. **Dự án cần tính chính xác và độ tin cậy cao**
	- Dự án như phát triển phần mềm trong các ngành y tế, tài chính, hoặc các hệ thống yêu cầu tính chính xác, kiểm tra nghiêm ngặt, và không thể có sai sót trong quá trình phát triển.

> [!example]- Ví dụ
> Phát triển phần mềm cho các hệ thống nhúng, hệ thống phần cứng, hoặc phần mềm có tính chất bảo mật cao, không cần nhiều thay đổi về yêu cầu.

6. Dự án quy mô nhỏ đến vừa
	- Mô hình thác nước thích hợp cho các dự án không quá phức tạp, có thể quản lý và triển khai một cách tuần tự từ đầu đến cuối mà không gặp phải sự cố lớn.

---

# ❓ Các câu hỏi thường gặp

> [!caution]- Nội dung đang hoàn thiện
> Quá trình xây dựng nội dung này có thể mất nhiều thời gian ⌛, nhưng bạn có thể thúc đẩy nó bằng cách tham gia [[article-collaboration-guide|cộng tác bài viết]] 🤝
> 
> **Rất mong sự thông cảm của các bạn 🙏**

---

# 🎉 Tổng kết

Mô hình thác nước **có tính kỷ luật cao**, phù hợp với những dự án đầy đủ yêu cầu từ đầu. Tuy nhiên, nếu bạn cần linh hoạt hơn, hãy xem xét các mô hình linh hoạt như Agile hoặc Scrum! 🚀
