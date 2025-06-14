---
date: 2025-02-25
draft: false
status: Doing
title: "Mô hình bản mẫu: Giải pháp cho yêu cầu không rõ ràng khi phát triển phần mềm"
description: Bài viết này trình bày chi tiết về mô hình bản mẫu (Prototyping), giúp bạn hiểu cách áp dụng kỹ thuật này khi yêu cầu phần mềm còn mơ hồ. Từ giao tiếp, thiết kế nhanh cho đến triển khai và phản hồi, hãy cùng khám phá các bước để tạo ra sản phẩm phần mềm chất lượng cao qua phương pháp phát triển lặp.
author: PhDoanh
authorlink: https://github.com/PhDoanh
tags:
  - software-technology
  - development
  - sofware-engineer
  - process-models
aliases:
  - prototyping model
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
    src="images/prototyping-model.png"
    alt="Mô hình bản mẫu: Giải pháp cho yêu cầu không rõ ràng khi phát triển phần mềm" 
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

Trong quá trình phát triển phần mềm, **yêu cầu không rõ ràng** là một trong những thách thức lớn. Khi khách hàng chỉ đưa ra mục tiêu tổng quát mà chưa định hình chi tiết các chức năng cần có, hay khi nhà phát triển chưa chắc chắn về hiệu năng của một thuật toán hay giao diện người dùng, **mô hình bản mẫu** chính là giải pháp tối ưu. 

# 🔄 Mô hình bản mẫu là gì?
**Mô hình bản mẫu** là một phương pháp phát triển phần mềm trong đó một phiên bản ban đầu (prototype) của hệ thống được xây dựng nhanh chóng để khách hàng đánh giá. Sau khi khách hàng phản hồi, prototype sẽ được điều chỉnh và cải tiến dần để tạo ra sản phẩm hoàn chỉnh.

**Mô hình bản mẫu** không chỉ có thể được sử dụng như một quy trình độc lập mà còn được tích hợp linh hoạt vào bất kỳ mô hình quy trình nào khác để giúp xác định và làm rõ yêu cầu phần mềm một cách nhanh chóng.

> [!check] Ưu điểm
> - **Giúp khách hàng dễ hình dung sản phẩm**: Prototype trực quan giúp khách hàng đánh giá và điều chỉnh sớm.
> - **Giảm rủi ro do yêu cầu thay đổi**: Dễ dàng cập nhật và cải thiện theo phản hồi của khách hàng.
> - **Tiết kiệm chi phí sửa lỗi về sau**: Phát hiện sớm các vấn đề về yêu cầu và thiết kế, tránh chi phí sửa chữa sau khi triển khai.
> - **Cải thiện giao tiếp giữa đội phát triển và khách hàng**: Giúp cả hai bên có cùng hiểu biết về sản phẩm.

> [!missing] Nhược điểm
> - **Dễ làm khách hàng hiểu sai về tiến độ**: Prototype thường chỉ là mô hình thử nghiệm, nhưng khách hàng có thể nhầm tưởng là sản phẩm gần hoàn thiện.
> - **Tốn thời gian nếu khách hàng thay đổi quá nhiều**: Việc liên tục điều chỉnh prototype có thể kéo dài thời gian phát triển.
> - **Dễ bỏ qua các vấn đề kỹ thuật và hiệu suất**: Prototype thường tập trung vào giao diện và chức năng chính, có thể không phản ánh đúng hiệu suất thực tế.
> - **Khó kiểm soát tài nguyên và ngân sách**: Nếu không giới hạn số lần chỉnh sửa, dự án có thể bị kéo dài và tốn kém hơn dự kiến.

---

# 🏗️ Quy trình mô hình bản mẫu

## Giao tiếp và lập kế hoạch nhanh
**Mục tiêu của giai đoạn này:**
- Xác định các mục tiêu chung của phần mềm
- Thu thập các yêu cầu ban đầu từ khách hàng và các bên liên quan
- Phát hiện các khu vực chưa được định nghĩa rõ ràng, cần bổ sung thông tin trong quá trình phát triển sau này

**Các hoạt động chính:**    
- **Giao tiếp:**
	- Nhóm phát triển tiến hành họp với khách hàng và các bên liên quan
    - Trao đổi thông tin về mục tiêu kinh doanh, nhu cầu chức năng và các giới hạn kỹ thuật
    - Xác định những yêu cầu đã biết và các vấn đề cần làm rõ
- **Lập kế hoạch nhanh (Quick Plan):**
    - Dựa trên kết quả giao tiếp, xây dựng một kế hoạch sơ bộ ngay lập tức
    - Đưa ra lịch trình ngắn hạn cho phiên bản prototype đầu tiên, nhằm nhanh chóng hiện thực hóa ý tưởng
    - Lập kế hoạch nhanh giúp tạo ra một “quick design” – một thiết kế sơ bộ tập trung vào các yếu tố giao diện và hiển thị mà người dùng cuối có thể thấy (ví dụ: bố cục giao diện, cách thức hiển thị kết quả)

**Đầu ra mong đợi của giai đoạn:**
- Phát triển được một prototype ban đầu phản ánh được các đặc điểm chính của hệ thống
- Tạo điều kiện cho việc thu thập phản hồi nhanh từ khách hàng, từ đó điều chỉnh và hoàn thiện yêu cầu cho các vòng phát triển sau
- Xác định rõ ràng các điểm mạnh và hạn chế của ý tưởng ban đầu, giúp định hướng cho quá trình xây dựng sản phẩm chính thức sau này

> [!info] Lưu ý
> - Quá trình giao tiếp cần được tiến hành một cách cởi mở, minh bạch và chủ động lắng nghe ý kiến của tất cả các bên liên quan
> - Việc lập kế hoạch nhanh đòi hỏi sự linh hoạt, cho phép điều chỉnh kế hoạch dựa trên phản hồi thực tế và các yêu cầu mới phát sinh
> - Giai đoạn này không nhằm mục đích hoàn thiện toàn bộ sản phẩm mà chủ yếu để làm rõ và hình thành một khung cơ bản, từ đó xây dựng các vòng lặp cải tiến sau này.

## Thiết kế nhanh

**Mục tiêu của Thiết kế nhanh:**
- Tập trung vào việc mô hình hóa các khía cạnh của phần mềm mà người dùng cuối sẽ nhìn thấy, như giao diện người dùng (UI) và định dạng hiển thị.
- Xác định và trực quan hóa các chức năng cơ bản, giúp các bên liên quan có cái nhìn sơ bộ về sản phẩm ngay từ đầu .

**Các hoạt động chính:**
- Tạo ra một bản thiết kế sơ khởi với tốc độ cao, tập trung vào việc thể hiện các yếu tố trực quan.
- Ưu điểm là tốc độ và tính đơn giản, chỉ tập trung vào các yếu tố hiển thị mà không đi sâu vào chi tiết kỹ thuật phức tạp.
- Có thể sử dụng các thành phần phần mềm có sẵn hoặc các công cụ hỗ trợ để rút ngắn thời gian phát triển prototype .

**Đầu ra mong đợi của giai đoạn:**
- **Prototype giao diện sơ khởi:** Một bản mẫu trực quan thể hiện bố cục và giao diện chính giúp khách hàng dễ hình dung hệ thống.
- **Mô hình chức năng cốt lõi:** Danh sách các chức năng chính kèm sơ đồ minh họa quá trình xử lý, làm rõ cách thức hoạt động cơ bản.
- **Tài liệu thiết kế sơ khởi:** Tài liệu tóm tắt cấu trúc và giao diện hệ thống, cung cấp các chỉ dẫn ban đầu cho việc triển khai.
- **Định hướng phát triển tiếp theo:** Xác định các yêu cầu bổ sung hoặc làm rõ để làm nền tảng cho giai đoạn thiết kế và phát triển chính thức.

> [!tip]- Mẹo
> Sử dụng các công cụ hỗ trợ như `window managers` hay `report generators` để tạo mẫu nhanh chóng.

## Xây dựng và triển khai nguyên mẫu

**Mục tiêu:**
- **Giảm thiểu rủi ro:** Thử nghiệm nhanh các giải pháp kỹ thuật để phát hiện và xử lý sớm các vấn đề tiềm ẩn.
- **Định hình hướng phát triển:** Thu thập phản hồi từ người dùng để cải tiến yêu cầu và thiết kế cho phiên bản hoàn thiện sau này.

**Các hoạt động chính:**
- **Construction:**
    - **Phát triển mã nguồn (`code`)** dựa trên thiết kế đã được duyệt.
    - **Kiểm thử (`test`)** nhanh để đảm bảo các chức năng cơ bản hoạt động đúng.
- **Deployment:**
    - Triển khai nguyên mẫu cho khách hàng và người dùng cuối trải nghiệm.
    - Thu thập **phản hồi (feedback)** từ các bên liên quan để xác định các điểm cần cải tiến.

**Đầu ra mong đợi:**
- **Nguyên mẫu hoạt động:** Một phiên bản ban đầu của hệ thống (prototype) thể hiện được giao diện và chức năng cơ bản, giúp khách hàng “thấy” được sản phẩm.
- **Danh sách phản hồi và yêu cầu:** Các thông tin, đề xuất cải tiến được tổng hợp từ phản hồi của khách hàng và người dùng.
- **Cơ sở để phát triển:** Dữ liệu ban đầu về tính khả thi của giải pháp, từ đó định hướng cho các giai đoạn thiết kế, phát triển tiếp theo.

> [!info] Lưu ý
> Trong quá trình này, có thể xảy ra các cải tiến tạm thời (vì mục tiêu là kiểm tra ý tưởng, không phải hoàn thiện sản phẩm).

> [!caution]- Cảnh báo
> Đừng để nguyên mẫu “bị kéo dài” thành sản phẩm cuối cùng vì thường sẽ gặp các vấn đề về chất lượng và bảo trì.

## Lặp lại và cải tiến

**Mục tiêu:**
- **Xác định và làm rõ yêu cầu:**
    - Khắc phục những điểm mơ hồ và mâu thuẫn trong yêu cầu ban đầu
    - Định hướng phát triển dựa trên phản hồi thực tế từ người dùng
- **Giảm thiểu rủi ro:** Phát hiện sớm các lỗi về thiết kế và hiệu năng, từ đó điều chỉnh kịp thời
- **Tăng cường sự phù hợp với nhu cầu thực tế:** Đảm bảo sản phẩm dần dần tiến gần hơn đến giải pháp cuối cùng đáp ứng đúng mong đợi của khách hàng

**Các hoạt động chính:**
- Điều chỉnh thiết kế, tối ưu hóa chức năng và khắc phục lỗi dựa trên phản hồi
- Lập kế hoạch cho vòng lặp cải tiến tiếp theo, qua đó tiến hành lại quá trình xây dựng và kiểm tra

**Đầu ra mong đợi:**
- **Phiên bản prototype được cải tiến rõ rệt:** Mô hình phát triển dần hoàn thiện, thể hiện sự tiến bộ qua mỗi vòng lặp
- **Tài liệu phản ánh quá trình cải tiến:** Ghi chép chi tiết các thay đổi, lỗi phát sinh và cách khắc phục đã được thực hiện
- **Cơ sở để phát triển sản phẩm hoàn chỉnh:** Phản hồi và kết quả của các vòng lặp giúp định hướng cho quá trình chuyển đổi prototype thành sản phẩm cuối cùng đáp ứng yêu cầu thực tiễn

> [!quote]- "Plan to throw one away. You will do that, anyway."
>  Đây là lời khuyên của Frederick P. Brooks, nhấn mạnh rằng nguyên mẫu ban đầu thường chỉ mang tính chất thử nghiệm và cần được xây dựng lại với chất lượng cao hơn sau khi đã hiểu rõ yêu cầu .

---

# 🤔 Mô hình bản mẫu phù hợp với dự án nào?

Mô hình bản mẫu (prototyping) thường được áp dụng cho các dự án có đặc điểm sau:

- **Yêu cầu không rõ ràng hoặc chưa đầy đủ:** Khi khách hàng chỉ xác định các mục tiêu tổng quát mà chưa đưa ra chi tiết về chức năng, giao diện hay các tính năng cần có.

- **Nhu cầu đánh giá tính khả thi sớm:** Khi cần nhanh chóng xây dựng một nguyên mẫu để kiểm tra hiệu quả của các giải pháp kỹ thuật, giao diện người dùng hoặc khả năng tương tác của hệ thống.

- **Giảm thiểu rủi ro kỹ thuật và giao diện:** Trong trường hợp các thuật toán, công nghệ hay cách tiếp cận về giao diện còn mang tính rủi ro, việc thử nghiệm với nguyên mẫu giúp phát hiện và khắc phục sớm các vấn đề.

- **Tăng cường phản hồi của khách hàng:** Khi cần khách hàng có cái nhìn trực quan về sản phẩm ban đầu để từ đó đưa ra những góp ý, cải tiến và làm rõ yêu cầu.

- **Áp lực về thời gian và thị trường:** Khi dự án có thời gian giới hạn, cần đưa sản phẩm ra thị trường nhanh chóng với phiên bản cơ bản (core product) và sau đó tiếp tục cải tiến theo phản hồi từ người dùng.

---

# 🔥 Ví dụ thực tế

Giả sử bạn được giao phát triển một ứng dụng quản lý công việc, nhưng khách hàng chỉ đưa ra yêu cầu chung như “cần quản lý công việc hiệu quả”. Bạn có thể:

- **Giao tiếp:** Tổ chức họp với khách hàng để làm rõ các chức năng cơ bản như tạo, chỉnh sửa và theo dõi tiến độ công việc.
- **Thiết kế nhanh:** Vẽ sơ đồ giao diện hiển thị danh sách công việc và các nút thao tác chính.
- **Xây dựng nguyên mẫu:** Dùng `HTML/CSS` và `JavaScript` để tạo giao diện đơn giản, giúp khách hàng hình dung sản phẩm.
- **Triển khai & Phản hồi:** Cho khách hàng trải nghiệm và ghi nhận các ý kiến như “giao diện chưa thân thiện” hay “thiếu chức năng sắp xếp theo mức ưu tiên”.
- **Lặp lại:** Sau đó, cải tiến nguyên mẫu dựa trên phản hồi và dần dần hoàn thiện sản phẩm.

---

# ❓ Câu hỏi thường gặp

> [!caution]- Nội dung đang hoàn thiện
> Quá trình xây dựng nội dung này có thể mất nhiều thời gian ⌛, nhưng bạn có thể thúc đẩy nó bằng cách tham gia [[article-collaboration-guide|cộng tác bài viết]] 🤝
> 
> **Rất mong sự thông cảm của các bạn 🙏**

---

# 🎉 Tổng kết

**Mô hình bản mẫu (Prototyping)** là một chiến lược hiệu quả trong **phát triển phần mềm** khi yêu cầu không rõ ràng hoặc khi cần làm rõ các chức năng trước khi xây dựng hệ thống hoàn chỉnh. Bằng cách thực hiện một chu trình gồm **giao tiếp**, **thiết kế nhanh**, **xây dựng nguyên mẫu**, và **triển khai cùng phản hồi**, bạn có thể:

- Giúp khách hàng và nhà phát triển cùng hiểu rõ yêu cầu phần mềm.
- Giảm thiểu rủi ro và bất định trong quá trình phát triển.
- Tạo điều kiện cho việc cải tiến và tối ưu hóa sản phẩm theo hướng chất lượng cao.

> [!advices] Lời khuyên
> Nhớ rằng, nguyên mẫu chỉ là bước đầu tiên trong hành trình phát triển phần mềm và **không nên kéo dài thành sản phẩm cuối cùng** nếu không có các biện pháp kiểm soát chất lượng nghiêm ngặt. Hãy luôn giữ vững tinh thần cải tiến và chấp nhận sự thay đổi theo phản hồi của khách hàng để đảm bảo thành công của dự án
