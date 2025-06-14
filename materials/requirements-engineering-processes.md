---
date: 2025-03-18
draft: false
status: Done
title: Quá trình của kỹ thuật yêu cầu trong phát triển phần mềm
description: Bài viết này giải thích chi tiết về quá trình kỹ thuật yêu cầu trong phát triển phần mềm. Tìm hiểu về mô hình spiral trong RE, các hoạt động elicitation, specification, validation và cách quản lý thay đổi hiệu quả.
author: PhDoanh
authorlink: https://github.com/PhDoanh
tags:
  - software-technology
  - development
  - sofware-engineer
  - requirements-engineering
  - processes
aliases:
  - requirements engineering processes
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
    src="images/requirements-engineering-processes.png"
    alt="Quá Trình Kỹ Thuật Yêu Cầu Trong Phát Triển Phần Mềm" 
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

Trong phát triển phần mềm, **kỹ thuật yêu cầu (Requirements Engineering)** đóng vai trò quan trọng trong việc đảm bảo hệ thống cuối cùng đáp ứng đúng nhu cầu của khách hàng. Quá trình này bao gồm ba hoạt động chính: **elicitation và analysis**, **specification** và **validation**. Mặc dù được mô tả theo dạng chuỗi trong các mô hình lý thuyết, thực tế, quá trình này mang tính **lặp lại** và **tương tác** cao nên được minh họa qua mô hình spiral.

# Các hoạt động chính trong quá trình RE

## Elicitation và Analysis
**Mục tiêu:** Tương tác với các bên liên quan để **khám phá** và **phân tích** yêu cầu của hệ thống.

**Chi tiết:**  
- Tìm hiểu các **yêu cầu người dùng** và **yêu cầu kinh doanh**.
- Thu thập thông tin thông qua phỏng vấn, khảo sát, và thảo luận nhóm.

> [!tip]- Mẹo
> Luôn đặt câu hỏi và xác nhận lại thông tin để tránh hiểu lầm.

## Specification
**Mục tiêu:** Chuyển đổi các yêu cầu thu thập được sang một dạng **chuẩn hóa** và dễ hiểu.

**Chi tiết:**  
- Viết tài liệu mô tả yêu cầu bằng ngôn ngữ tự nhiên kết hợp với các biểu đồ, sơ đồ.
- Phân loại yêu cầu thành **chức năng** và **phi chức năng**.

> [!info] Lưu ý
> Sự **rõ ràng** và **chi tiết** trong phần này giúp tránh mâu thuẫn khi triển khai.

## Validation
**Mục tiêu:** Đảm bảo rằng các yêu cầu đã xác định chính xác **nhu cầu của khách hàng**.

**Chi tiết:**  
- Kiểm tra, xác minh yêu cầu thông qua **reviews**, **prototyping** và **thử nghiệm**.
- Xác nhận lại với các bên liên quan để đảm bảo không có sai sót.

> [!caution] Cảnh báo
> Bỏ qua bước này có thể dẫn đến sự phát sinh các lỗi nghiêm trọng trong quá trình phát triển.

---

# Mô hình spiral và tính lặp lại trong RE

Trong quá trình của **Requirements Engineering**, các hoạt động không diễn ra theo một trình tự tuyến tính mà thay vào đó, chúng lặp lại và tương tác với nhau qua nhiều vòng xoắn của mô hình. Điều này giúp đảm bảo rằng các yêu cầu luôn được **tinh chỉnh** và **cải tiến** dựa trên phản hồi từ thực tế phát triển hệ thống.

## Tính chất lặp lại và tương tác

Quá trình RE được tổ chức theo dạng **vòng lặp** (iterations), nghĩa là sau mỗi vòng xoắn, các yêu cầu có thể được **đánh giá lại**, **cập nhật**, hoặc **bổ sung**.

> [!question]- Tại sao cần lặp lại
> - **Hạn chế rủi ro:** Nếu có lỗi hoặc hiểu sai yêu cầu, chúng có thể được phát hiện và sửa sớm.
> - **Thích ứng linh hoạt:** Dự án có thể điều chỉnh theo thay đổi của khách hàng hoặc thị trường.
> - **Cải tiến liên tục:** Các yêu cầu được làm rõ hơn sau mỗi lần lặp.

> [!example]- Ví dụ
> Một công ty đang phát triển ứng dụng quản lý nhân sự.
> - **Vòng lặp đầu tiên**: Xác định các yêu cầu cơ bản như đăng nhập, quản lý thông tin nhân viên.
> - **Vòng lặp thứ hai**: Thêm tính năng báo cáo hiệu suất nhân viên theo phản hồi của người dùng.
> - **Vòng lặp thứ ba**: Cập nhật yêu cầu về quyền truy cập để tăng tính bảo mật.

👉 **Mỗi vòng xoắn giúp cải tiến hệ thống**, thay vì cố định yêu cầu từ đầu.

Trong mô hình Spiral RE, các hoạt động **tương tác với nhau** thay vì diễn ra theo thứ tự cứng nhắc. Các hoạt động chính gồm:

1. **Elicitation (Thu thập yêu cầu)** 📋
2. **Specification (Đặc tả yêu cầu)** 📝
3. **Validation (Xác thực yêu cầu)** ✅
4. **Management (Quản lý yêu cầu thay đổi)** 🔄

> [!question]- Tại sao cần có sự tương tác?
> - **Phát hiện sớm vấn đề**: Trong quá trình xác thực, nếu phát hiện yêu cầu không thực tế, nó sẽ quay lại bước đặc tả để điều chỉnh.
> - **Liên tục cập nhật**: Khi quản lý thay đổi, nhóm phát triển có thể quay lại bước thu thập để lấy thêm thông tin từ khách hàng.

> [!example]- Ví dụ
> Công ty phát triển một ứng dụng thương mại điện tử.
>
> - 📋 **Thu thập yêu cầu:** Khách hàng muốn có tính năng giỏ hàng.
> - 📝 **Đặc tả yêu cầu:** Định nghĩa chi tiết cách giỏ hàng hoạt động.
> - ✅ **Xác thực yêu cầu:** Kiểm tra với người dùng thử nghiệm, họ yêu cầu thêm tính năng "Lưu giỏ hàng".
> - 🔄 **Quản lý thay đổi:** Cập nhật yêu cầu, quay lại vòng lặp tiếp theo để tinh chỉnh.

👉 **Quá trình này không đi theo đường thẳng mà là một vòng xoắn liên tục, giúp hệ thống phát triển tốt hơn.**

## Ước tính nỗ lực qua mỗi vòng spiral
Một ví dụ đơn giản về công thức ước tính nỗ lực theo từng vòng có thể được biểu diễn như sau:

$$
E = I \times \left(E_{e} + E_{s} + E_{v}\right)
$$

Trong đó
- $\textbf{E}$: Tổng nỗ lực (effort) của quá trình RE.
- $\textbf{I}$: Số vòng spiral (iterations).
- $\textbf{E}_{e}$: Nỗ lực cho giai đoạn elicitation và analysis.
- $\textbf{E}_{s}$: Nỗ lực cho giai đoạn specification.
- $\textbf{E}_{v}$: Nỗ lực cho giai đoạn validation.

> [!example]- Ví dụ
> Nếu trong một vòng spiral, các nỗ lực tương ứng là: $E_{e} = 10$ giờ, $E_{s} = 8$ giờ, $E_{v} = 6$ giờ. Với $I = 3$ vòng, tổng nỗ lực sẽ là:
> $$
> E = 3 \times (10 + 8 + 6) = 3 \times 24 = 72 \text{ giờ}
> $$
>
> **Lưu ý:** Công thức này chỉ mang tính chất tham khảo. Thực tế, các yếu tố như độ phức tạp của hệ thống và kinh nghiệm của đội ngũ cũng ảnh hưởng đáng kể đến tổng nỗ lực.

---

# Quản lý thay đổi trong quá trình RE
Trong thực tế phát triển phần mềm, yêu cầu luôn có xu hướng thay đổi theo thời gian do hiểu biết của các bên liên quan được làm rõ hơn và sự thay đổi trong môi trường hoạt động:

- **Khách hàng thay đổi nhu cầu**: Họ có thể nhận ra rằng một tính năng không còn cần thiết hoặc muốn thêm chức năng mới.

- **Công nghệ thay đổi**: Một công nghệ mới có thể xuất hiện, khiến nhóm phát triển phải điều chỉnh yêu cầu để tận dụng lợi thế của nó.

- **Môi trường kinh doanh thay đổi**: Các quy định pháp lý, chính sách công ty hoặc thị trường có thể ảnh hưởng đến yêu cầu phần mềm.

- **Phát hiện lỗi hoặc thiếu sót**: Khi hệ thống được phát triển và thử nghiệm, có thể xuất hiện các vấn đề khiến yêu cầu ban đầu cần chỉnh sửa.

> [!example]- Ví dụ
> Một công ty đang phát triển một ứng dụng thương mại điện tử. Ban đầu, khách hàng chỉ yêu cầu tích hợp thanh toán qua thẻ tín dụng. Tuy nhiên, sau khi khảo sát thị trường, họ nhận ra rằng nhiều khách hàng thích sử dụng ví điện tử (Momo, ZaloPay). Do đó, yêu cầu mới được thêm vào để hỗ trợ các phương thức thanh toán này.

Việc thay đổi yêu cầu cần được kiểm soát chặt chẽ để tránh ảnh hưởng tiêu cực đến tiến độ và chất lượng phần mềm. Dưới đây là **quy trình cơ bản** để quản lý thay đổi:

**Bước 1: Ghi nhận yêu cầu thay đổi**
- Yêu cầu thay đổi có thể đến từ khách hàng, nhóm phát triển hoặc các bên liên quan.
- Sử dụng **mẫu đề xuất thay đổi (Change Request Form)** để ghi lại thông tin, bao gồm:
    - **Mô tả thay đổi**
    - **Lý do thay đổi**
    - **Tác động dự kiến đến hệ thống**
    - **Mức độ ưu tiên** (Cao, Trung bình, Thấp)

> [!example]- Ví dụ
> Một khách hàng đề xuất thêm tính năng **đăng nhập bằng Google** để tăng tiện lợi cho người dùng. Nhóm phát triển ghi nhận yêu cầu này và phân tích tác động của nó.

**Bước 2: Phân tích tác động**
Đánh giá xem thay đổi có ảnh hưởng đến:
- **Các yêu cầu khác** không? (ví dụ: thêm tính năng mới có làm thay đổi giao diện không?)
- **Lịch trình và ngân sách** không? (mất bao lâu để thực hiện thay đổi?)
- **Hiệu suất và bảo mật** của hệ thống?

> [!example]- Ví dụ
> Thêm tính năng **đăng nhập bằng Google** có thể yêu cầu tích hợp với Google OAuth, đòi hỏi đội ngũ phát triển phải dành thời gian để nghiên cứu API và đảm bảo bảo mật.

**Bước 3: Phê duyệt thay đổi**
Sau khi đánh giá, nhóm quản lý dự án hoặc khách hàng sẽ quyết định **Chấp nhận** thay đổi nếu có lợi cho hệ thống. Hoặc **Từ chối** nếu nó không khả thi hoặc gây ảnh hưởng tiêu cực.

> [!example]- Ví dụ
> Nếu việc tích hợp đăng nhập Google tốn quá nhiều thời gian và ngân sách, khách hàng có thể quyết định hoãn tính năng này đến phiên bản sau.

**Bước 4: Thực hiện thay đổi**
- Nếu thay đổi được phê duyệt, đội phát triển sẽ cập nhật tài liệu yêu cầu, thiết kế lại hệ thống và triển khai.
- **Sử dụng hệ thống kiểm soát phiên bản** (như Git) để theo dõi thay đổi.

> [!example]- Ví dụ
> Sau khi yêu cầu **đăng nhập bằng Google** được phê duyệt, đội phát triển cập nhật tài liệu, thiết kế giao diện đăng nhập mới và triển khai tính năng.

**Bước 5: Kiểm thử và xác nhận thay đổi**
- Chạy **kiểm thử hồi quy** để đảm bảo các tính năng cũ không bị ảnh hưởng bởi thay đổi.
- Xác nhận với khách hàng rằng yêu cầu đã được thực hiện đúng.

> [!example]- Ví dụ
> Sau khi tích hợp thành công đăng nhập Google, đội phát triển kiểm tra xem tính năng hoạt động đúng không, đồng thời kiểm thử lại các chức năng khác như đăng nhập bằng email.

**Công cụ hỗ trợ quản lý thay đổi trong RE**:
- **Trello/Jira**: Theo dõi và quản lý yêu cầu thay đổi.
- **Git/GitHub/GitLab**: Kiểm soát phiên bản mã nguồn để theo dõi thay đổi.
- **Confluence/Google Docs**: Cập nhật tài liệu yêu cầu và chia sẻ với nhóm.

> [!caution] Cảnh báo
>  Không quản lý thay đổi một cách hiệu quả có thể dẫn đến việc mất kiểm soát dự án và tăng chi phí phát triển.

---

# Các câu hỏi thường gặp

> [!caution]- Nội dung đang hoàn thiện
> Quá trình xây dựng nội dung này có thể mất nhiều thời gian ⌛, nhưng bạn có thể thúc đẩy nó bằng cách tham gia [[article-collaboration-guide|cộng tác bài viết]] 🤝
> 
> **Rất mong sự thông cảm của các bạn 🙏**

---

# Tổng kết
Quá trình **kỹ thuật yêu cầu** là một hoạt động **lặp lại** và **tương tác** giữa các hoạt động elicitation, specification và validation. Mô hình **spiral** giúp:
- Tăng cường sự linh hoạt và khả năng điều chỉnh.
- Phân bổ nỗ lực hợp lý qua các vòng lặp dựa trên mức độ chi tiết và yêu cầu của hệ thống.
- Quản lý thay đổi hiệu quả, đảm bảo hệ thống phát triển đúng hướng và đáp ứng đúng nhu cầu của khách hàng.

Việc hiểu rõ quá trình này không chỉ giúp bạn xây dựng một tài liệu yêu cầu hoàn chỉnh mà còn tạo nền tảng vững chắc cho **phát triển phần mềm** chất lượng. Hãy luôn **cập nhật**, **đánh giá** và **quản lý thay đổi** trong suốt quá trình phát triển để đạt được thành công tối đa! 👍
