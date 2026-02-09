---

publish: true
title: Quy trình quản lý dự án
description:
tags:
  - project-management
  - project-management-process
  - waterfall
  - scrum-agile
  - sofware-life-cycle
  - explorable
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
Công việc quản lý dự án xoay quanh [[project-management-overview#^7eeb7c|10 miền tri thức]], nhưng để "triển khai" các miền tri thức này trong thực tế, ta phải đi qua **các nhóm quy trình**. PMI định nghĩa: _nhóm quy trình quản lý dự án là tập hợp logic các quy trình nhằm đạt mục tiêu cụ thể của dự án_. Các quy trình quản lý dự án được chia thành **5 nhóm**:

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

**Mục tiêu chính:** Tạo **bản kế hoạch quản lý dự án** toàn diện - kế hoạch tổng thể và kế hoạch cho từng miền tri thức (phạm vi, thời gian, chi phí, chất lượng, rủi ro, giao tiếp, nhân lực, mua sắm, bên liên quan, tích hợp).

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

> [!info] Lưu ý
> Trong trường hợp các bên liên quan không phản hồi xác nhận cho toàn bộ dự án, nhà quản lý dự án cần thực hiện thủ tục đưa vấn đề lên cấp cao hơn, tức là liên hệ - báo cáo với các cấp cao để họ giải quyết vấn đề

## Mối quan hệ giữa các nhóm quy trình 🤝

%% ![[Pasted image 20250930090014.png|center|500]] %%

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

## Tổng quan về Waterfall 🌊 và Scrum ⚡
Bạn cứ thử hình dung: phát triển phần mềm cũng giống như xây nhà 🏠. Không thể cứ gom gạch, xi măng rồi xây tùy hứng. Ta cần một *"mô hình"* - tức phương pháp, quy trình chuẩn để định hướng, xây dựng một cách hiệu quả.

Trong ngành, nhiều mô hình phát triển phần mềm đã ra đời. Nhưng **hai mô hình** phổ biến nhất tính đến nay là: **Waterfall và Scrum**.

### Mô hình Thác nước - Waterfall
Được giới thiệu bởi **Winston W. Royce (1970)** và sau đó phổ biến trong bài báo của **Bell & Thayer (1976)**. Mô hình thác nước mô tả các công việc phát triển phần mềm được triển khai theo **chuỗi các giai đoạn tuyến tính**. Chỉ khi một giai đoạn hoàn thành, thì mới chuyển sang giai đoạn tiếp theo, giống như nước chảy từ bậc thang cao xuống bậc thang thấp hơn vậy.

%% ![[Pasted image 20250930100512.png|center|500]] %%

Các pha/giai đoạn trong Waterfall:

1. **Định nghĩa yêu cầu**: thu thập và ghi lại yêu cầu đầy đủ của nhà tài trợ và các bên liên quan về sản phẩm, dịch vụ phần mềm. Chúng sẽ được tài liệu hóa để đặc tả các yêu cầu chức năng, phi chức năng, ...
2. **Thiết kế hệ thống**: thiết kế kiến trúc tổng thể & chi tiết, dựa trên phân tích các yêu cầu phần mềm (tài liệu đặc tả).
3. **Cài đặt và kiểm thử đơn vị**: cài đặt toàn bộ đơn vị chương trình và kiểm thử chúng để đảm bảo hoạt động như mong muốn. Lỗi trong quá trình kiểm thử cũng sẽ được sửa trong pha này
4. **Kiểm thử tích hợp và hệ thống**: Kiểm thử các chức năng lớn hơn (được tạo ra nhờ quá trình tích hợp các đơn vị) và kiểm thử toàn bộ hệ thống để đảm bảo chất lượng phần mềm 
5. **Vận hành và bảo trì**: đưa vào sử dụng (bàn giao thành phẩm) và hỗ trợ, sửa lỗi mới được phát hiện bởi người dùng hoặc nâng cấp chức năng nhằm thỏa mãn, hỗ trợ tốt nhất cho công việc của họ

> [!check] Ưu điểm
> - Rõ ràng, dễ hiểu, dễ quản lý tiến độ từng giai đoạn.
> - Có tài liệu đầy đủ, giúp dễ dàng theo dõi, kiểm soát chất lượng và bàn giao.
> - Phù hợp với dự án có yêu cầu ổn định, ít thay đổi.
> - Thích hợp cho dự án lớn, phức tạp, cần tuân thủ nghiêm ngặt về quy trình.
> - Dễ đánh giá hiệu quả, ước lượng chi phí và thời gian từ đầu dự án.

> [!missing] Nhược điểm
> - Khó thích nghi với thay đổi yêu cầu khi dự án đã tiến triển.
> - Giai đoạn sau không thể bắt đầu trước khi giai đoạn trước hoàn thành → kém linh hoạt.
> - Khó phát hiện lỗi sớm, thường chỉ phát hiện khi kiểm thử tích hợp hoặc nghiệm thu.
> - Không phù hợp với dự án cần lặp nhanh, thử nghiệm liên tục hoặc sản phẩm mới chưa rõ yêu cầu.
> - Thường tốn thời gian cho việc chuẩn hóa và tạo tài liệu, có thể làm chậm tiến độ.

> [!info] Lưu ý
> Trong thực tế, Waterfall không tuyến tính *"tuyệt đối"*, mà có sự đan xen, bổ sung và hỗ trợ lẫn nhau giữa các pha/giai đoạn. Vi dụ: chỉ khi tiến hành **thiết kế hệ thống** thì ta mới phát hiện ra một số yêu cầu chưa đủ chi tiết hoặc còn thiếu sót.

### Mô hình Scrum - Agile

%% mô hình Scrum - Agile %%

Nếu Waterfall giống xây nhà từ A-Z theo bản thiết kế cố định, thì **Scrum** lại giống việc làm sản phẩm theo kiểu *"ra bản nháp trước, rồi liên tục cải tiến"* ✨.
- **Đặc trưng chính**: Làm việc theo **Sprint** (chu kỳ ngắn 1-4 tuần).
- **Vai trò trong Scrum**:
    - **Product Owner**: đại diện khách hàng, quyết định tính năng ưu tiên.
    - **Scrum Master**: hỗ trợ nhóm, gỡ vướng mắc.
    - **Development Team**: đội phát triển đa kỹ năng.

Quy trình làm việc trong Scrum:
1. **Product Backlog**: danh sách tất cả tính năng, yêu cầu.
2. **Sprint Planning**: chọn việc sẽ làm trong Sprint.
3. **Sprint Execution**: đội phát triển làm việc & họp ngắn hằng ngày (Daily Scrum).
4. **Sprint Review**: trình bày sản phẩm cho khách hàng.
5. **Sprint Retrospective**: rút kinh nghiệm để cải thiện cho các Sprint kế tiếp.

> [!check] Ưu điểm
> - Linh hoạt, thích ứng nhanh với thay đổi yêu cầu
> - Phát triển sản phẩm theo từng Sprint → có giá trị gia tăng sớm, có thể bàn giao từng phần
> - Tăng tính minh bạch và tương tác giữa đội dự án và khách hàng.
> - Phát hiện lỗi sớm, giảm rủi ro nhờ kiểm thử liên tục và phản hồi nhanh.
> - Thúc đẩy sự chủ động, trách nhiệm của từng thành viên trong nhóm.

> [!missing] Nhược điểm
> - Cần đội ngũ có kỷ luật cao và kỹ năng tự quản lý tốt.
> - Thiếu tài liệu chi tiết có thể gây khó khăn trong việc bàn giao hoặc bảo trì.
> - Quản lý dự án phức tạp hơn khi dự án lớn hoặc đội nhóm phân tán.
> - Cần cam kết liên tục từ khách hàng để duy trì Product Backlog và tham gia Sprint Review.
> - Không dễ dự đoán chi phí, tiến độ chính xác từ đầu.

### Liên hệ tới quản lý dự án

#### Waterfall vs các nhóm quy trình quản lý dự án 🌊

Mô hình **thác nước (Waterfall)** là mô hình tuyến tính, các pha được định nghĩa rõ ràng, tuần tự và ít thay đổi. Mỗi pha có đầu ra cụ thể, dễ quản lý, phù hợp với các dự án có yêu cầu ổn định. Dưới đây là bảng ánh xạ giữa các pha của mô hình này với các nhóm quy trình quản lý dự án:

|                                   | Khởi tạo                             | Lập kế hoạch                       | Thực hiện                                                                   | Kiểm tra - Giám sát                                                      | Đóng dự án                                                 |
| :-------------------------------- | ------------------------------------ | ---------------------------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------------------ | ---------------------------------------------------------- |
| **Định nghĩa yêu cầu**            | Tài liệu mô tả thông tin sơ bộ dự án | Xác nhận, bổ sung chi tiết yêu cầu | Định nghĩa chi tiết yêu cầu, Thiết kế khuôn mẫu, Định nghĩa phạm vi         | Kiểm tra giám sát phạm vi, Quản lý thay đổi                              | Tiêu chí hoàn thành, Tài liệu định nghĩa yêu cầu           |
| **Thiết kế hệ thống**             | –                                    | –                                  | Thiết kế tổng quan, UI/UX, thiết kế chi tiết                                | Kiểm tra giám sát các loại thiết kế                                      | Tài liệu thiết kế hệ thống                                 |
| **Cài đặt và kiểm thử đơn vị**    | –                                    | –                                  | cài đặt và kiểm thử đơn vị                                                  | Kiểm tra giám sát việc cài đặt, kiểm thử đó                              | Hệ thống phần mềm                                          |
| **Kiểm thử tích hợp và hệ thống** | –                                    | –                                  | Kiểm thử tích hợp và kiểm thử hệ thống                                      | Kiểm tra giám sát chất lượng sản phẩm                                    | đối chiếu tiêu chí hoàn thành, kiểm soát sản phẩm bàn giao |
| **Vận hành và bảo trì**           | –                                    | –                                  | Đưa hệ thống lên môi trường sử dụng, đào tạo người dùng và bảo trì hệ thống | Kiểm soát lỗi trong quá trình vận hành, nâng cấp theo nhu cầu người dùng | Nghiệm thu sản phẩm                                        |

> [!important] Nhận xét
> - Pha **định nghĩa yêu cầu** ảnh hưởng đến **tất cả nhóm quy trình quản lý dự án**, vì đội dự án cần theo sát yêu cầu và phối hợp với các bên liên quan suốt quá trình.
> - Các pha còn lại chủ yếu thuộc **thực hiện, kiểm tra giám sát và đóng dự án**, đảm bảo sản phẩm cuối cùng đạt tiêu chuẩn đã đặt ra.

#### Scrum vs các nhóm quy trình quản lý dự án

**Scrum** là mô hình phát triển phần mềm **tinh gọn, hướng kết quả**, các pha/giai đoạn có thể đan xen và lặp lại nhiều lần trong vòng đời dự án thông qua các **chu kỳ/Sprint** (thường từ 1 đến 4 tuần).

%% ![[Pasted image 20250930161049.png|center|500]] %%

**Ví dụ triển khai dự án Scrum kết hợp quy trình quản lý dự án:**
- **Sprint 1 - 2:** Tập trung vào các công việc của **nhóm quy trình khởi tạo và lập kế hoạch**:
    - Thu thập và phân tích yêu cầu tổng quan
    - Tạo lập **tài liệu mô tả thông tin sơ bộ dự án**
    - Lập **kế hoạch quản lý các miền tri thức** và **tích hợp dự án**
- **Các Sprint tiếp theo:** Tập trung vào **nhóm quy trình thực hiện**:
    - Làm rõ yêu cầu chi tiết
    - Thiết kế tổng thể, cơ sở dữ liệu, giao diện và UX
    - **Với dự án phát triển phần mềm mới**[^1]: các pha được thực hiện theo chiều ngang, tức là chúng được diễn ra tuần tự hoặc song song trên **nhiều chức năng** của sản phẩm,  
    - **Với dự án bảo trì phần mềm**[^2]: các pha có thể diễn ra theo chiều dọc, tức là tập trung xử lý **từng chức năng cụ thể** từ pha đầu đến pha cuối, theo thứ tự ưu tiên và kiểm thử song song các chức năng khác để đảm bảo không bị lỗi do thay đổi.  
- **Kết thúc mỗi Sprint:** Có **cuộc họp rà soát** (Sprint Review) để:
    - **Bàn giao** và đánh giá tiến độ, chất lượng sản phẩm
    - Chọn công việc cải thiện cho Sprint tiếp theo (Sprint Backlog Item - SBI)

> [!important] Nhận xét
> - Toàn bộ pha trong Scrum đều liên quan đến **nhóm quy trình đóng dự án**, vì mọi Sprint đều tạo ra các sản phẩm, tài liệu và kết quả cần kiểm tra, nghiệm thu.
> - Scrum cho phép **linh hoạt ứng phó với thay đổi**, phù hợp với môi trường dự án có yêu cầu thay đổi liên tục.
> - Một số chức năng lớn, phức tạp có thể được tiến hành trong vài Sprint

[^1]: **Dự án phát triển phần mềm mới** là dự án tạo ra phần mềm hoàn toàn mới hoặc tái xây dựng hệ thống, với yêu cầu chưa rõ ràng và rủi ro công nghệ cao. Các pha phát triển thường diễn ra theo **chiều ngang**, thực hiện trên nhiều chức năng cùng lúc để xây dựng sản phẩm hoàn chỉnh.

[^2]: **Dự án bảo trì phần mềm** tập trung vào sửa lỗi hoặc phát triển thêm tính năng cho phần mềm đã tồn tại, nhằm đảm bảo vận hành ổn định và kiểm soát ảnh hưởng tới các chức năng khác. Các pha trong dự án bảo trì thường diễn ra theo **chiều dọc**, xử lý toàn bộ các pha trên từng chức năng cụ thể.
