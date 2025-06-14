---
date: 2025-03-19
draft: false
status: Done
title: "Hành Trình Khám Phá Yêu Cầu Hệ Thống: Quy Trình Requirements Elicitation Toàn Diện"
description: Quá trình requirements elicitation là bước nền tảng trong việc hiểu và thu thập các yêu cầu từ stakeholders nhằm phát triển một hệ thống phần mềm phù hợp với nhu cầu thực tế. Bài viết này sẽ đưa ra cái nhìn toàn diện về các kỹ thuật elicitation như phỏng vấn, quan sát (ethnography) và sử dụng các câu chuyện (stories) cũng như tình huống (scenarios) để định hình yêu cầu hệ thống.
author: PhDoanh
authorlink: https://github.com/PhDoanh
tags:
  - software-technology
  - development
  - sofware-engineer
  - requirements-engineering
  - processes
  - elicitation
aliases:
  - requirements elicitation
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
    src="images/requirements-elicitation.png"
    alt="Hành Trình Khám Phá Yêu Cầu Hệ Thống: Quy Trình Requirements Elicitation Toàn Diện  " 
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

Trong phát triển phần mềm, **requirements elicitation** là bước khởi đầu quan trọng nhằm hiểu rõ công việc của các bên liên quan và xác định cách một hệ thống mới có thể hỗ trợ công việc đó. Quá trình này không chỉ giúp khám phá các yêu cầu từ phía khách hàng mà còn đóng vai trò quan trọng trong việc tạo ra một sản phẩm phần mềm đạt hiệu quả cao. 💡

# Giới thiệu

Việc **elicitation** yêu cầu đòi hỏi các kỹ sư phần mềm phải tương tác trực tiếp với **các bên liên quan** (stakeholders) để:
- **Khám phá** yêu cầu từ các tài liệu, mô tả công việc và trao đổi trực tiếp.
- **Phân tích** các yêu cầu từ góc nhìn của từng bên liên quan.
- **Đàm phán** và **ưu tiên** các yêu cầu khi có xung đột.

> [!info] Lưu ý
> Các stakeholder có thể không biết rõ họ cần gì, do đó việc lắng nghe kỹ càng và đặt câu hỏi phù hợp là rất quan trọng.

---

# Quy trình elicitation và phân tích yêu cầu

## Khám phá và hiểu yêu cầu

Trong giai đoạn này, kỹ sư phần mềm:
- **Tương tác** với các bên liên quan để thu thập thông tin.
- **Xác định** những yêu cầu ẩn trong mô tả công việc và tài liệu sẵn có.

> [!info] Lưu ý
> Các bên liên quan thường trình bày yêu cầu theo cách riêng của họ, do đó cần thận trọng để tránh hiểu sai.

## Phân loại và tổ chức yêu cầu

Sau khi thu thập, yêu cầu cần được:
- **Nhóm lại** theo các chủ đề và lĩnh vực chức năng.
- **Tổ chức** thành các cụm hợp lý nhằm dễ dàng quản lý.

> [!tip]- Mẹo
> Sử dụng công cụ như `Google Docs` hoặc `Office 365` để tạo không gian làm việc chung giúp dễ dàng cập nhật và chỉnh sửa.

## Ưu tiên và thương lượng yêu cầu

Khi có nhiều yêu cầu từ các stakeholder với mức độ ưu tiên khác nhau:
- **Thương lượng** để tìm ra giải pháp thỏa đáng cho mọi bên.
- **Ưu tiên** các yêu cầu quan trọng, đảm bảo hiệu quả kinh tế và khả thi kỹ thuật.

> [!caution] Cảnh báo
> Nếu không tổ chức các cuộc họp định kỳ, các bên có thể cảm thấy rằng ý kiến của họ bị bỏ qua, dẫn đến xung đột trong quá trình phát triển.

## Tài liệu hóa yêu cầu

Giai đoạn cuối của quá trình **elicitation** là:
- **Ghi chép** lại tất cả các yêu cầu một cách rõ ràng và dễ hiểu.
- **Sử dụng ngôn từ đơn giản** và các sơ đồ minh họa để đảm bảo mọi stakeholder đều có thể nắm bắt được.

> [!example]- Ví dụ
> Một bản nháp ban đầu của tài liệu yêu cầu có thể được duy trì trên các nền tảng chia sẻ như `wiki` hoặc `Google Docs` để dễ dàng theo dõi và đóng góp ý kiến.

---

# Viewpoints - Góc nhìn từ các bên liên quan

**"View Points"** có thể hiểu là các góc nhìn, quan điểm từ các bên liên quan trong một hệ thống, dự án hoặc tình huống cụ thể. Trong ngữ cảnh kỹ thuật, quản lý dự án hoặc phân tích yêu cầu, View Points giúp làm rõ nhu cầu, mục tiêu, và mối quan tâm của từng bên liên quan (stakeholders).

**Mục đích của View Points:**

- Giúp xác định các yêu cầu khác nhau từ các bên liên quan.

- Hỗ trợ việc thiết kế, phát triển và quản lý hệ thống/phần mềm/phương án một cách toàn diện hơn.

- Giúp phát hiện xung đột về yêu cầu giữa các bên liên quan và tìm cách giải quyết.

- Cung cấp một bức tranh tổng thể, giúp đảm bảo hệ thống đáp ứng đầy đủ nhu cầu của tất cả các bên.

Dưới đây là một số ví dụ về các bên liên quan trong một dự án công nghệ, cùng với góc nhìn của họ:

| Bên liên quan                              | Góc nhìn (View Point)                                                                                   |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------- |
| **Khách hàng (Users)**                     | Quan tâm đến trải nghiệm người dùng, tính dễ sử dụng, tốc độ và sự ổn định của hệ thống.                |
| **Nhà phát triển (Developers)**            | Quan tâm đến công nghệ, hiệu suất, bảo trì, tính mở rộng và dễ dàng tích hợp với các hệ thống khác.     |
| **Nhà quản lý dự án (Project Managers)**   | Quan tâm đến tiến độ, ngân sách, quản lý rủi ro và đảm bảo các yêu cầu được thực hiện đúng kế hoạch.    |
| **Nhà đầu tư (Investors)**                 | Quan tâm đến lợi nhuận, tính khả thi kinh tế và khả năng mở rộng thị trường của sản phẩm/dịch vụ.       |
| **Đội QA/QC (Quality Assurance/Control)**  | Quan tâm đến độ ổn định, khả năng kiểm thử và đảm bảo hệ thống hoạt động theo tiêu chuẩn chất lượng.    |
| **Đội vận hành (Operations Team)**         | Quan tâm đến khả năng bảo trì, giám sát hệ thống, phát hiện lỗi và xử lý sự cố nhanh chóng.             |
| **Đối tác kinh doanh (Business Partners)** | Quan tâm đến khả năng tích hợp, tương thích với hệ sinh thái của họ, cũng như lợi ích kinh doanh chung. |

**Ứng dụng của View Points**

- **Trong phát triển phần mềm:** Khi thiết kế hệ thống, việc xem xét View Points từ khách hàng, nhà phát triển, tester và quản lý giúp tạo ra một sản phẩm đáp ứng đầy đủ yêu cầu.

- **Trong quản lý dự án:** Giúp xác định ưu tiên của các bên liên quan, từ đó có chiến lược phân bổ nguồn lực phù hợp.

- **Trong phân tích và thiết kế hệ thống:** Dùng để mô hình hóa các yêu cầu theo góc nhìn của từng bên liên quan, đảm bảo không bỏ sót yếu tố quan trọng.

> [!tip]- Mẹo
> Đừng quên liên tục cập nhật các viewpoint theo sự thay đổi của môi trường kinh doanh và tổ chức.

> [!info] Lưu ý
> - **Chủ động giao tiếp:** Đặt câu hỏi chi tiết để khai thác thông tin ẩn và tránh hiểu lầm.
> - **Ghi chép kỹ lưỡng:** Mọi cuộc trao đổi nên được ghi lại để làm tài liệu tham khảo sau này.
> - **Điều chỉnh linh hoạt:** Quá trình elicitation là **vòng lặp liên tục**; luôn sẵn sàng cập nhật thông tin khi có thay đổi.
> - **Đảm bảo tính minh bạch:** Tổ chức các cuộc họp định kỳ để tất cả các stakeholder đều cảm thấy mình được lắng nghe.

---

# Ước tính chi phí Elicitation

Công thức ước tính chi phí trong **requirements elicitation** thường được xây dựng dựa trên các yếu tố như **thời gian thực hiện**, **độ phức tạp của dự án**, **chi phí nhân công**, và **các yếu tố khác liên quan đến quy trình phát triển phần mềm**. Một công thức sử dụng các yếu tố quan trọng có thể trông như sau:

$$
\mathrm{Cost}=\alpha\cdot T+\beta\cdot C+\gamma\cdot S+\delta\cdot R
$$

Trong đó:
- $\alpha$: Hệ số chi phí thời gian (đơn vị: tiền tệ/giờ). Phản ánh mức lương của nhân sự tham gia vào quá trình elicitation.
- $T$: Tổng thời gian thực hiện (đơn vị: giờ). Tính tổng số giờ làm việc của toàn bộ nhóm thực hiện elicitation.
- $\beta$: Hệ số độ phức tạp (đơn vị: tiền tệ/độ phức tạp). Hệ số này phản ánh chi phí tăng thêm khi dự án có mức độ phức tạp cao hơn.
- $C$: Độ phức tạp của dự án (đơn vị: mức độ). Được xác định bằng các tiêu chí như: số lượng stakeholder, số lượng yêu cầu cần phân tích, mức độ không chắc chắn trong yêu cầu, v.v.
- $\gamma$: Hệ số liên quan đến phạm vi dự án (đơn vị: tiền tệ/scope level). Phạm vi càng lớn, yêu cầu càng nhiều thì chi phí cũng tăng lên.
- $S$: Phạm vi dự án (đơn vị: mức độ). Ví dụ: 1 cho dự án nhỏ, 2 cho dự án trung bình, 3 cho dự án lớn.
- $\delta$: Hệ số rủi ro (đơn vị: tiền tệ/mức rủi ro). Dự án có mức độ rủi ro cao (ví dụ như thay đổi yêu cầu thường xuyên, không có tài liệu rõ ràng) sẽ cần ngân sách cao hơn.
- $R$: Mức độ rủi ro của dự án (đơn vị: mức độ). Được đánh giá dựa trên lịch sử dự án tương tự, khả năng thay đổi yêu cầu từ khách hàng, v.v.

> [!example]- Ví dụ
> Giả sử chúng ta có một dự án với các thông số như sau:
> - $\alpha=120$ (120 đơn vị tiền tệ/giờ)
> - $T=60$ giờ làm việc
> - $\beta=250$ (250 đơn vị tiền tệ/độ phức tạp)
> - $C=3$ (mức độ phức tạp trung bình)
> - $\gamma = 300$ (300 đơn vị tiền tệ/phạm vi)
> - $S=2$ (phạm vi trung bình)
> - $\delta = 400$ (400 đơn vị tiền tệ/mức rủi ro)
> - $R=2$ (rủi ro trung bình)
>
> Áp dụng vào công thức:
> $$
> \mathrm{Cost}=120\times60+250\times3+300\times2+400\times2=7200+750+600+800=9350
> $$

> [!info] Lưu ý
> - Công thức này giúp ước tính sơ bộ chi phí thực hiện **requirements elicitation** bằng cách kết hợp nhiều yếu tố quan trọng: thời gian, độ phức tạp, phạm vi và rủi ro.  
> - Doanh nghiệp có thể tùy chỉnh các hệ số $\alpha,~\beta,~\gamma,~\delta$ dựa trên dữ liệu lịch sử của họ để có ước tính chính xác hơn.  
> - Khi rủi ro cao hoặc phạm vi dự án rộng, chi phí sẽ tăng đáng kể do yêu cầu phát sinh nhiều hơn và cần nhiều nỗ lực để quản lý.

> [!question]- Đây là công thức chuẩn à?
> Không có một **công thức chuẩn duy nhất** để ước tính chi phí trong **requirements elicitation**, vì chi phí phụ thuộc vào nhiều yếu tố như **loại dự án, quy trình phát triển, mức độ phức tạp**, ... Tuy nhiên, công thức ở trên là một cách tiếp cận tổng quát để tính toán chi phí dựa trên các biến số quan trọng.

---

# Kỹ thuật Elicitation

Quá trình **elicitation** bao gồm nhiều kỹ thuật khác nhau, trong đó hai phương pháp cơ bản nhất là **phỏng vấn** và **quan sát thực tế**.

## Phỏng vấn

Kỹ thuật **`interviewing`** là phương pháp tiếp cận trực tiếp với các **stakeholders** để trao đổi về những gì họ làm, hệ thống hiện tại và những mong đợi cho hệ thống mới. Có hai dạng chính:

**Phỏng vấn có cấu trúc:**  
- **Đặc điểm:** Sử dụng một bộ câu hỏi định sẵn để thu thập thông tin.  
- **Ưu điểm:** Giúp định hướng buổi phỏng vấn, đảm bảo thu được các thông tin cần thiết.  
- **Nhược điểm:** Có thể giới hạn khả năng khám phá thêm thông tin ngoài phạm vi câu hỏi đã định.

**Phỏng vấn tự do:**  
- **Đặc điểm:** Không có bộ câu hỏi cố định, mở ra cuộc trao đổi để khám phá các vấn đề mới.  
- **Ưu điểm:** Khai thác được nhiều thông tin sâu sắc, giúp người phỏng vấn nắm bắt các vấn đề tiềm ẩn.  
- **Nhược điểm:** Dễ đi lạc đề nếu không có sự điều phối hợp lý.

> [!tip]- Mẹo
> Hãy sử dụng sự kết hợp giữa **phỏng vấn có cấu trúc** và **tự do**. Bắt đầu với các câu hỏi định hướng để duy trì chủ đề, sau đó mở rộng ra những vấn đề khác mà **stakeholders** đề cập.

## Quan sát thực tế

**Ethnography** là kỹ thuật quan sát trực tiếp môi trường làm việc của người dùng nhằm hiểu rõ cách họ tương tác với hệ thống hiện tại. Qua đó, ta có thể phát hiện:

- **Các tác vụ thực tế:** Những hành vi và thủ tục làm việc mà người dùng thực hiện hàng ngày.  

- **Yêu cầu ẩn:** Những yếu tố mà người dùng xem là hiển nhiên nhưng lại quan trọng trong thực tiễn.  

- **Tương tác xã hội:** Cách mà người dùng phối hợp và hỗ trợ lẫn nhau trong công việc.

> [!example]- Vi dụ
> Trong một nghiên cứu về hệ thống quản lý không lưu, một chuyên gia đã nhận ra rằng các kiểm soát viên hàng không thường tự điều chỉnh quy trình của họ dựa trên kinh nghiệm cá nhân và sự phối hợp nhóm, mặc dù tài liệu quy định lại cách hoạt động chuẩn.

> [!caution] Cảnh báo
> Một số người dùng có thể cảm thấy ngại khi có người ngoài quan sát, vì vậy hãy đảm bảo môi trường quan sát được tạo ra một cách tự nhiên và tôn trọng quyền riêng tư.

---

# Câu chuyện người dùng và kịch bản tương tác

Để minh họa cho các yêu cầu của hệ thống, **stories** và **scenarios** là những công cụ mạnh mẽ giúp chuyển đổi các thông tin thu thập được thành các tình huống cụ thể:

**Stories:**  
- **Đặc điểm:** Được viết dưới dạng văn bản tự sự, mô tả một cách tổng quát về cách hệ thống sẽ được sử dụng.  
- **Ưu điểm:** Giúp tất cả các bên liên quan dễ dàng hình dung bức tranh tổng thể về hệ thống.  

> [!tip]- Mẹo
> Sử dụng **stories** để kích thích cuộc thảo luận và mở ra các ý tưởng mới.

**Scenarios:**  
- **Đặc điểm:** Mô tả chi tiết một phiên tương tác cụ thể giữa người dùng và hệ thống.  
- **Ưu điểm:** Cung cấp thông tin cụ thể về đầu vào, quá trình xử lý, và đầu ra của hệ thống.  

> [!example]- Ví dụ
> Một **scenario** có thể mô tả quá trình tải ảnh lên một trang web chia sẻ ảnh như `KidsTakePics`, trong đó có quy trình kiểm duyệt của giáo viên, xử lý trùng tên file và gửi thông báo qua email.

> [!info] Lưu ý
> Các **stories** và **scenarios** không chỉ hỗ trợ quá trình thu thập yêu cầu mà còn là công cụ hữu ích để truyền đạt ý tưởng giữa các thành viên dự án.


> [!important] Quan trọng
> - **Kết hợp nhiều kỹ thuật:** Sử dụng kết hợp **phỏng vấn**, **ethnography** và **stories/scenarios** để đảm bảo thu thập được thông tin đầy đủ.
> - **Đặt câu hỏi mở:** Tránh chỉ hỏi “hãy cho tôi biết bạn muốn gì”; thay vào đó, hãy đặt các câu hỏi cụ thể, kích thích người trả lời chia sẻ chi tiết về công việc của họ.
> - **Chú ý đến ngôn ngữ chuyên ngành:** **Stakeholders** có thể sử dụng từ ngữ chuyên ngành mà bạn không quen thuộc. Đừng ngại hỏi rõ ý nghĩa của các thuật ngữ này.
> - **Ghi chép cẩn thận:** Luôn ghi lại các cuộc trao đổi và quan sát để có tài liệu tham khảo cho giai đoạn phân tích và phát triển hệ thống.
> - **Tôn trọng quyền riêng tư:** Khi tiến hành **ethnography**, hãy đảm bảo rằng các bên liên quan được thông báo và đồng ý với việc quan sát để tránh vi phạm quyền riêng tư.

---

# Các câu hỏi thường gặp

> [!caution]- Nội dung đang hoàn thiện
> Quá trình xây dựng nội dung này có thể mất nhiều thời gian ⌛, nhưng bạn có thể thúc đẩy nó bằng cách tham gia [[article-collaboration-guide|cộng tác bài viết]] 🤝
> 
> **Rất mong sự thông cảm của các bạn 🙏**

---

# Tổng kết

Quá trình **requirements elicitation** đóng vai trò then chốt trong việc đảm bảo dự án phần mềm thành công. Từ việc **khám phá** yêu cầu ban đầu, **phân loại** và **ưu tiên** chúng, đến **tài liệu hóa** chi tiết, mỗi bước đều đòi hỏi sự tỉ mỉ và kỹ lưỡng thông qua các kỹ thuật sau:

- **Phỏng vấn** cung cấp cái nhìn tổng quan và giúp phát hiện các yêu cầu ban đầu.  
- **Ethnography** mở ra những khía cạnh thực tế và các yêu cầu ẩn mà người dùng thường xem là hiển nhiên.  
- **Stories** và **scenarios** giúp chuyển đổi thông tin thành các tình huống cụ thể, hỗ trợ thảo luận và định hình chi tiết yêu cầu.  

> [!important] Quan trọng
> - Việc giao tiếp rõ ràng và định kỳ với các **stakeholders** là chìa khóa giúp phát hiện và giải quyết sớm các xung đột.  
> - Một hệ thống được phát triển dựa trên yêu cầu chính xác và đầy đủ sẽ dễ dàng thích nghi với các thay đổi của môi trường kinh doanh và công nghệ.  

Nhờ vào sự kết hợp chặt chẽ của các kỹ thuật trên, bạn có thể **khai thác thông tin** một cách hiệu quả và xây dựng được hệ thống đáp ứng đúng nhu cầu của các **stakeholders**. Hãy luôn nhớ rằng **sự linh hoạt** và **tương tác thường xuyên** là chìa khóa trong quá trình elicitation để đảm bảo không bỏ sót bất kỳ thông tin quan trọng nào 🚀

