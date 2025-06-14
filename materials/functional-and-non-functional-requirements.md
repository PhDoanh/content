---
date: 2025-03-18
draft: false
status: Done
title: Khám Phá Yêu Cầu Chức Năng và Phi Chức Năng Trong Phát Triển Phần Mềm
description: "Bài viết này giải thích chi tiết về yêu cầu chức năng và yêu cầu phi chức năng trong phần mềm, cùng với ví dụ, lưu ý và mẹo hữu ích giúp bạn nắm bắt vai trò và tầm quan trọng của chúng trong quá trình phát triển hệ thống."
author: PhDoanh
authorlink: https://github.com/PhDoanh
tags:
  - software-technology
  - development
  - sofware-engineer
  - requirements
  - functional
  - non-functional
  - requirements-engineering
aliases:
  - functional and non functional requirements
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
    src="images/functional-and-non-functional-requirements.png"
    alt="Khám Phá Yêu Cầu Chức Năng và Phi Chức Năng Trong Phát Triển Phần Mềm" 
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

Trong phát triển phần mềm, việc xác định các yêu cầu của hệ thống là bước quan trọng để đảm bảo sản phẩm cuối cùng đáp ứng nhu cầu của khách hàng. Hai loại yêu cầu cơ bản được phân loại là **yêu cầu chức năng** và **yêu cầu phi chức năng**. Bài viết dưới đây sẽ giúp bạn hiểu rõ:
- **Yêu cầu chức năng**: Những gì hệ thống cần thực hiện.
- **Yêu cầu phi chức năng**: Các ràng buộc, tiêu chuẩn và đặc điểm tổng quát mà hệ thống cần đáp ứng.

Hãy cùng khám phá chi tiết từng loại yêu cầu với các ví dụ minh họa và mẹo hữu ích nhé! 😊

# Yêu cầu chức năng

**Yêu cầu chức năng** mô tả những dịch vụ, chức năng mà hệ thống cần cung cấp. Chúng xác định:
- **Các tác vụ** mà hệ thống thực hiện.
- **Đầu vào và đầu ra** của các chức năng.
- **Xử lý ngoại lệ** trong các tình huống đặc biệt.

> [!example]- Ví dụ
>  - Trong hệ thống **Mentcare**, một yêu cầu chức năng có thể là: *"Người dùng có thể tìm kiếm danh sách cuộc hẹn ở tất cả các phòng khám."*
>  - Một yêu cầu chức năng cụ thể khác trong hệ thống **Mentcare** là: *"Mỗi nhân viên sử dụng hệ thống phải được định danh bằng số nhân viên 8 chữ số."* Điều này đảm bảo mỗi chức năng liên quan đến quản lý dữ liệu người dùng đều có thể truy xuất thông tin một cách chính xác.

> [!info] Lưu ý
> - Việc mô tả yêu cầu phải **rõ ràng** và **không gây hiểu nhầm** để tránh những giải pháp thực thi không đúng ý khách hàng.
> - Hãy sử dụng ngôn ngữ tự nhiên, dễ hiểu cho cả người dùng cuối và đội ngũ phát triển.

> [!tip]- Mẹo
> - **Cẩn thận trong chi tiết**: Bổ sung thông tin về đầu vào, đầu ra, và các trường hợp ngoại lệ.  
> - **Tương tác với khách hàng**: Trao đổi thường xuyên để đảm bảo rằng các yêu cầu phản ánh đúng nhu cầu thực tế.  

---

# Yêu cầu phi chức năng

**Yêu cầu phi chức năng** không tập trung vào chức năng cụ thể của hệ thống mà mô tả các **tiêu chuẩn** và **ràng buộc** mà hệ thống phải đáp ứng. Chúng liên quan đến:

- **Hiệu suất**: Tốc độ xử lý, thời gian phản hồi.
- **Độ tin cậy**: Mức độ ổn định và khả năng chịu lỗi.
- **Bảo mật**: Yêu cầu về an toàn thông tin và quyền truy cập.
- **Khả năng sử dụng**: Tính dễ sử dụng của giao diện và hệ thống.

Các yêu cầu phi chức năng thường được chia thành 3 nhóm chính:

- **Product requirements (Yêu cầu sản phẩm)**: Quy định hành vi của phần mềm trong quá trình vận hành.

> [!example]- Ví dụ
> Hệ thống phải có thời gian phản hồi không quá 2 giây đối với mỗi yêu cầu của người dùng.

- **Organizational requirements (Yêu cầu tổ chức)**: Phát sinh từ các chính sách và quy trình nội bộ của tổ chức.

> [!example]- Ví dụ
> Hệ thống phát triển phải tuân theo tiêu chuẩn `coding guidelines` đã được quy định trong nội bộ."

- **External requirements (Yêu cầu bên ngoài)**: Đến từ các yếu tố ngoại cảnh như quy định pháp luật, tiêu chuẩn ngành.

> [!example]- Ví dụ
> Hệ thống phải đảm bảo tuân thủ quy định về bảo mật thông tin theo tiêu chuẩn quốc gia.

---

# Đo lường hiệu năng

Để đánh giá hiệu năng của hệ thống, có thể sử dụng công thức tính **tốc độ phản hồi**:

$$
RT=\frac{T}{N}
$$

Trong đó:
- $RT$: Thời gian phản hồi trung bình của hệ thống.
- $T$: Tổng thời gian hệ thống xử lý các yêu cầu.
- $N$: Tổng số yêu cầu được xử lý trong khoảng thời gian đó.

> [!example]- Ví dụ
> Nếu hệ thống xử lý 100 yêu cầu trong 20 giây, thời gian phản hồi trung bình sẽ là:
> $$
> RT=20/100=0.2~\text{s/request}
> $$
> 
> **Lưu ý:** Các con số thực tế cần được xác định dựa trên điều kiện thực tế của hệ thống và phải được kiểm định thông qua quá trình thử nghiệm.

---

# Mối quan hệ giữa các yêu cầu

Một điểm quan trọng là **yêu cầu chức năng** và **yêu cầu phi chức năng** không tồn tại độc lập mà chúng thường **tương tác** và **phụ thuộc lẫn nhau**: Một **yêu cầu phi chức năng** như bảo mật có thể tạo ra các **yêu cầu chức năng** bổ sung, ví dụ như cơ chế xác thực người dùng. Ngược lại, một chức năng cụ thể có thể bị ràng buộc bởi các yêu cầu về hiệu suất hoặc độ tin cậy. Cụ thể:

- **Phụ thuộc (Dependency)**: Một yêu cầu chỉ có thể được thực hiện khi một yêu cầu khác được hoàn thành trước.

> [!example]- Ví dụ
> - Yêu cầu A: "Người dùng có thể đặt hàng trực tuyến."
> - Yêu cầu B: "Hệ thống phải hỗ trợ thanh toán trực tuyến."
> 
> Yêu cầu B là bắt buộc để hoàn thành yêu cầu A.

- **Mâu thuẫn (Conflict)**: Hai yêu cầu có thể mâu thuẫn nhau khi một yêu cầu làm cho yêu cầu kia không thể thực hiện được.

> [!example]- Ví dụ
> - Yêu cầu X: "Hệ thống phải cung cấp xác thực hai yếu tố để tăng cường bảo mật."
> - Yêu cầu Y: "Người dùng có thể đăng nhập nhanh mà không cần nhập mã xác nhận."
> 
> Hai yêu cầu này có thể mâu thuẫn vì xác thực hai yếu tố làm chậm quá trình đăng nhập nhanh.

- **Bổ sung (Complementary)**: Một yêu cầu có thể giúp hoàn thiện hoặc tăng cường một yêu cầu khác.

> [!example]- Ví dụ
> - Yêu cầu C: "Người dùng có thể đặt hàng trên trang web."
> - Yêu cầu D: "Người dùng có thể theo dõi trạng thái đơn hàng qua email."
>
> Yêu cầu D bổ sung cho yêu cầu C bằng cách cải thiện trải nghiệm người dùng.

- **Tổng hợp (Aggregation)**: Một yêu cầu có thể được chia thành nhiều yêu cầu con để dễ dàng quản lý và phát triển.

> [!example]- Ví dụ
> - Yêu cầu chính: "Hệ thống quản lý tài khoản người dùng."
> - Yêu cầu con:
> 	- "Người dùng có thể đăng ký tài khoản.
> 	- "Người dùng có thể đặt lại mật khẩu."
> 	- "Người dùng có thể cập nhật thông tin cá nhân."

- **Ưu tiên (Priority)**: Một số yêu cầu quan trọng hơn và cần được thực hiện trước so với những yêu cầu khác.

> [!example]- Ví dụ
> - Yêu cầu quan trọng: "Hệ thống phải đảm bảo an toàn dữ liệu người dùng."
> - Yêu cầu ít quan trọng hơn: "Giao diện trang chủ có thể tùy chỉnh màu sắc."
> 
> Yêu cầu quan trọng sẽ được ưu tiên phát triển trước.

> [!info] Lưu ý
> Việc không xác định rõ ràng mối quan hệ giữa các yêu cầu có thể dẫn đến sự mâu thuẫn trong quá trình triển khai và gây ra chi phí phát triển tăng cao.

---

# Các câu hỏi thường gặp

> [!caution]- Nội dung đang hoàn thiện
> Quá trình xây dựng nội dung này có thể mất nhiều thời gian ⌛, nhưng bạn có thể thúc đẩy nó bằng cách tham gia [[article-collaboration-guide|cộng tác bài viết]] 🤝
> 
> **Rất mong sự thông cảm của các bạn 🙏**

---

# Tổng kết

Trong bài viết này, chúng ta đã khám phá chi tiết về:
- **Yêu cầu chức năng**: Mô tả các dịch vụ mà hệ thống cần cung cấp, từ việc xử lý đầu vào, đầu ra cho đến xử lý ngoại lệ.
- **Yêu cầu phi chức năng**: Định nghĩa các tiêu chuẩn và ràng buộc về hiệu suất, độ tin cậy, bảo mật và khả năng sử dụng của hệ thống.
- **Mối quan hệ chặt chẽ** giữa hai loại yêu cầu, nơi một yêu cầu có thể tạo ra hoặc ràng buộc yêu cầu khác.

Hiểu rõ và xây dựng đúng **yêu cầu chức năng** và **yêu cầu phi chức năng** là yếu tố **quan trọng** để đảm bảo hệ thống hoạt động ổn định, đáp ứng nhu cầu người dùng và tuân thủ các tiêu chuẩn kỹ thuật. Hãy luôn cập nhật và kiểm định các yêu cầu này qua từng giai đoạn của dự án để đạt được **sự thành công** trong phát triển phần mềm. 👍

Hy vọng bài viết đã cung cấp cho bạn những thông tin hữu ích và những mẹo thiết thực trong quá trình xác định và phát triển yêu cầu hệ thống! Nếu có bất kỳ thắc mắc hoặc cần trao đổi thêm, đừng ngần ngại để lại bình luận phía dưới nhé! 💬
