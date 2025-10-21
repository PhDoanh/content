---
stage: Idea
draft: true
title: Các phương pháp ước lượng công việc
description:
tags:
  - project-management
  - estimation-methods
socialDescription:
socialImage:
permalink:
lang: vi
aliases:
cssclasses:
  - img
---
Trước khi vẽ ra bất kỳ lịch trình, ngân sách, hay biểu đồ Gantt nào, thì **việc đầu tiên** mà nhà quản lý dự án phải đối mặt chính là trả lời câu hỏi: Dự án này tốn bao nhiêu thời gian, bao nhiêu tiền, và cần bao nhiêu người để hoàn thành?

Đây là một câu hỏi **rất khó** theo cả nghĩa đen lẫn nghĩa bóng, vì nó ảnh hưởng đến phần lớn hoạt động của dự án sau này (mọi khủng hoảng deadline, overload, mất niềm tin, ... đều do trả lời câu hỏi trên kém hiệu quả), nên nhà quản lý dự án cần phải có kỹ năng **ước lượng công việc** để tìm ra đáp án tối ưu nhất có thể.

## Ước lượng công việc và tầm quan trọng
Theo PMI (Project Management Institute), **Ước lượng (Estimation)** là quy trình phát triển một giá trị tương đối chính xác về chi phí của các nguồn lực cần thiết để hoàn thành dự án. 

Nói cách khác, ước lượng là *"cầu nối"* giữa **ý tưởng** và **kế hoạch hành động cụ thể** 🧭. Bạn không thể lập tiến độ, phân bổ người hay lên ngân sách nếu chưa có những con số ước lượng ban đầu.

Khi thực hiện ước lượng, ta cần xác định 3 loại thông tin chính cho từng công việc cụ thể trong dự án:

- Thời gian ⏱: Xác định cần bao lâu để hoàn thành. Ví dụ: Hoàn thiện module “đăng nhập” mất 5 ngày
- Chi phí 💰: Tổng chi phí nhân công + tài nguyên + rủi ro dự phòng. Ví dụ: 15 triệu đồng cho công đoạn này
- Nhân lực 👥: Bao nhiêu người cần tham gia, và năng lực ra sao. Ví dụ: 1 lập trình viên backend + 1 tester

Tổng hợp các con số của tất cả đầu việc sẽ giúp bạn ước lượng được **tổng thời gian - tổng chi phí - tổng nguồn lực** cho toàn bộ dự án.

Tầm quan trọng của việc ước lượng:
- **Cơ sở lập kế hoạch dự án**: Không có ước lượng thì không thể tạo được lịch trình hay kế hoạch nguồn lực chính xác.
- **Kiểm soát rủi ro**: Ước lượng sát thực tế giúp bạn thấy trước chỗ nào dễ *"bể deadline"* hoặc *"vượt ngân sách"*.
- **Thuyết phục các bên liên quan**: Khi ước lượng có căn cứ, bạn có thể chứng minh với khách hàng hoặc sếp rằng kế hoạch là khả thi.
- **Tăng độ tin cậy của đội dự án**: Các thành viên hiểu rõ giới hạn công việc của mình, từ đó cam kết tốt hơn với tiến độ.

## Các loại ước lượng
Trong quá trình quản lý dự án phần mềm, việc ước lượng thường **được thực hiện nhiều lần** ở các giai đoạn khác nhau. Mỗi giai đoạn lại yêu cầu **mức độ chi tiết và độ chính xác khác nhau**, vì thông tin về dự án lúc đầu thường còn rất ít và dần được bổ sung qua từng bước. Do đó, các tài liệu quản lý dự án thường phân chia **ước lượng thành 3 loại chính**:

### Ước lượng thô - Rough Order of Magnitude (ROM)

Đây là **loại ước lượng sơ khởi nhất**, thường được thực hiện **trong giai đoạn khởi tạo dự án**, khi thông tin về phạm vi, yêu cầu, và nguồn lực còn hạn chế.
- **Mục đích:** giúp các bên ra **quyết định ban đầu** xem dự án có khả thi hay không, có nên đầu tư không.
- **Độ chính xác:** dao động rất lớn, **từ -50% đến +100%** so với giá trị thực tế.
- **Nguồn dữ liệu:** chủ yếu dựa trên **kinh nghiệm, phỏng đoán hoặc so sánh với các dự án tương tự**.

> [!example] Ví dụ
> Một công ty phần mềm đang xem xét phát triển hệ thống ERP nội bộ. Từ kinh nghiệm dự án cũ, họ ước lượng thô chi phí có thể khoảng 1 tỷ đồng (theo độ chính xác trên), tức là chi phí thực tế có thể chỉ bằng 50% ước lượng (500 triệu) hoặc vượt quá 100% ước lượng (2 tỷ đồng).

### Ước lượng ngân sách - Budget Estimate

Loại này được thực hiện **sau khi dự án đã được phê duyệt sơ bộ** và đã có thêm dữ liệu cụ thể hơn về phạm vi, yêu cầu, cũng như khối lượng công việc.

- **Mục đích:** phục vụ việc **lập ngân sách chi tiết** cho kế hoạch tổng thể của dự án.
- **Độ chính xác:** tăng lên, nằm trong khoảng **-10% đến +25%**.
- **Nguồn dữ liệu:** sử dụng thông tin thu thập từ các tài liệu yêu cầu, WBS sơ bộ và báo giá từ nhà cung cấp (nếu có).

> [!example] Ví dụ
> Sau khi đã xác định các module cần phát triển, nhóm dự án tính toán chi phí nhân công, phần mềm, thiết bị,... và lập ngân sách chi tiết khoảng 950 triệu (theo độ chính xác trên), tức chi phí thực tế có thể là 855 triệu (=10% ước lượng) hoặc 1 tỷ 187 triệu (vượt lên 25% ước lượng)

### Ước lượng cuối cùng - Definitive Estimate

Đây là loại ước lượng **chính xác nhất**, được thực hiện **khi kế hoạch dự án đã hoàn thiện**: phạm vi rõ ràng, yêu cầu đã ổn định, và WBS chi tiết đã có.

- **Mục đích:** dùng để **quản lý chi phí thực tế** trong quá trình triển khai.
- **Độ chính xác:** rất cao, thường nằm trong khoảng **–5% đến +10%**.
- **Nguồn dữ liệu:** dựa trên tài liệu đặc tả yêu cầu chi tiết, thiết kế hệ thống, kế hoạch nhân sự và lịch trình cụ thể.

> [!example] Ví dụ
> Khi hợp đồng đã ký và bản thiết kế hệ thống ERP hoàn thiện, nhóm dự án ước lượng chi phí thực tế cần là 980 triệu ±10%, tức trong khoảng 882 đến 1.078 triệu đồng.


## Một số phương pháp và công cụ ước lượng

Trong quản lý dự án phần mềm, **ước lượng** là công việc rất khó nhưng vô cùng quan trọng. Bởi dự án phần mềm mang tính **sáng tạo, ít lặp lại** - tức là hầu như mỗi dự án đều có đặc thù riêng, nên không thể áp dụng rập khuôn một công thức duy nhất. Do đó, người quản lý dự án thường phải **kết hợp nhiều phương pháp và công cụ** để có kết quả tin cậy nhất.

Phần này giới thiệu **chín phương pháp và công cụ phổ biến** mà các nhà quản lý dự án thường dùng khi ước lượng quy mô, công sức và chi phí phần mềm.

### 1. Ước lượng từ trên xuống

Phương pháp này bắt đầu bằng cách **ước lượng tổng thể cho toàn bộ dự án**, rồi **phân bổ dần xuống** cho các giai đoạn, module hoặc đầu việc nhỏ hơn.

- Thường dựa trên **kinh nghiệm từ các dự án tương tự** hoặc dựa vào **phán đoán của chuyên gia**.
- Ưu điểm: nhanh, phù hợp giai đoạn đầu khi **chưa có nhiều thông tin chi tiết**.
- Nhược điểm: dễ thiếu chính xác vì **bỏ qua chi tiết kỹ thuật**.

> [!example] Ví dụ
> Nếu dự án ERP trước đó mất 10 tháng và 2 tỷ đồng, thì dự án mới với quy mô tương đương có thể ước lượng khoảng như vậy, sau đó chia 20% cho phân tích, 50% cho phát triển, 30% cho kiểm thử và triển khai.

### 2. Ước lượng từ dưới lên

Trái ngược với phương pháp trên, **ước lượng từ dưới lên** đi từ các **đầu việc nhỏ nhất** trong bảng phân rã công việc **WBS (Work Breakdown Structure)**

- Từng tác vụ được ước lượng riêng, sau đó **cộng dồn** lại thành tổng thời gian, chi phí cho toàn dự án.
- Ưu điểm: chính xác cao, vì dựa vào chi tiết thực tế.
- Nhược điểm: **mất nhiều thời gian** và phụ thuộc vào chất lượng của WBS.

> [!example] Ví dụ
> Nếu "Phát triển module quản lý sản phẩm" gồm 3 tác vụ: thiết kế cơ sở dữ liệu (20h), lập trình giao diện (30h), kiểm thử (10h) → tổng module này mất 60h. Cộng tất cả các module lại → ra tổng ước lượng dự án.

### 3. Ước lượng có tham số

Phương pháp này **dựa vào mối quan hệ toán học** giữa các biến đầu vào (ví dụ: số dòng code, số chức năng, số trang giao diện…) với **nỗ lực** hoặc **chi phí**.

- Cần **cơ sở dữ liệu lịch sử** để xây dựng hệ số trung bình.
- Công thức thường có dạng:  _Nỗ lực = Hệ số × Quy mô sản phẩm_

> [!example] Ví dụ
> Nếu dữ liệu lịch sử cho thấy trung bình 1 giao diện người dùng cần khoảng 10 giờ công, và dự án có 30 giao diện người dùng → tổng nỗ lực ước lượng = 10 × 30 ≈ **300 giờ công**.

### 4. Phương pháp Delphi

Đây là **phương pháp dựa vào ý kiến chuyên gia** nhưng có **tính ẩn danh và lặp lại** để tăng độ khách quan. Cách làm:
1. Tập hợp nhóm chuyên gia → mỗi người ước lượng độc lập.
2. Thu thập kết quả, tổng hợp, gửi lại cho nhóm (ẩn danh).
3. Các chuyên gia xem lại, điều chỉnh nếu cần.
4. Lặp lại 2-3 vòng cho đến khi các giá trị **hội tụ**.

- Ưu điểm: tránh thiên lệch cá nhân, tận dụng kinh nghiệm tập thể.  
- Nhược điểm: tốn thời gian nếu quá nhiều vòng.

### 5. Ước lượng dựa trên WBS

Phương pháp này dùng **cấu trúc phân rã công việc (WBS)** làm cơ sở ước lượng.  
Tức là ta sẽ **xác định từng gói công việc**, rồi **ước lượng thời gian, chi phí và nguồn lực** cho từng gói, sau đó tổng hợp.
- Giúp kiểm soát được **tính đầy đủ** của các công việc cần làm.
- Có thể kết hợp với phương pháp **từ dưới lên** để đạt độ chính xác cao.

> [!example] Ví dụ
> Trong WBS của hệ thống thương mại điện tử, ta tách riêng module "Giỏ hàng" → ước lượng 20h phát triển, 10h kiểm thử, 5h tài liệu hướng dẫn, v.v.

### 6. Phương pháp ba điểm

Đây là phương pháp dựa trên **xác suất** (một phương pháp thuộc loại [[#3. Ước lượng có tham số|ước lượng có tham số]]), được PMI khuyến nghị. Ba giá trị được dùng:
- **O (Optimistic):** thời gian tốt nhất, ít rủi ro (lý tưởng nhất)
- **M (Most Likely):** thời gian khả dĩ nhất (có khả năng xảy ra nhất)
- **P (Pessimistic):** thời gian xấu nhất (trường hợp tồi tệ nhất)

Công thức tính ước lượng trung bình có trọng số (theo phân phối Beta):
$$
E=\frac{O+4M+P}{6}
$$

Và độ lệch chuẩn:
$$
SD=\frac{P - O}{6}​
$$

> [!example] Ví dụ
> Một tác vụ có O = 4h, M = 6h, P = 10h →  E = (4 + 4×6 + 10)/6 = 6.33h và SD = 1h → Nỗ lực trung bình là **6.33 ± 1 giờ**.

> [!info] Lưu ý
> Phần mẫu số trong 2 công thức trên là hệ số có thể thay đổi tùy dự án, nhưng thường là 6 do minh chứng từ lịch sử nghiên cứu phân phối!  

### 7. Phương pháp điểm chức năng
Phương pháp này đo quy mô phần mềm **không theo dòng code (LOC)** mà theo **chức năng người dùng nhìn thấy**.

- Mỗi loại chức năng (nhập liệu, báo cáo, giao tiếp ngoài, ...) có **trọng số riêng**, thể hiện mức độ khó tương ứng thường là: 5 (khó), 3 (trung bình) và 1 (dễ)
- Tổng số điểm chức năng được quy đổi sang nỗ lực hoặc chi phí dựa trên cơ sở dữ liệu lịch sử.

> [!example] Ví dụ
> - Một phần mềm có 10 form nhập liệu (trọng số 1), 5 báo cáo (trọng số 3) → tổng điểm = 10×1 + 5×3 = 25 FP. 
> - Nếu 1 FP ≈ 8 giờ công → tổng nỗ lực ≈ 200 giờ.

### 8. Mô hình COCOMO - Constructive Cost Model

Đây là **mô hình toán học nổi tiếng của Boehm**, dùng để ước lượng công sức và chi phí phát triển phần mềm (là một công cụ thuộc loại [[#3. Ước lượng có tham số|ước lượng có tham số]]). Công thức COCOMO cơ bản:

- Công sức: $E=a×L^b$ (tháng công)
- Thời gian: $T=c\times E^d$ (tháng)
- Số người: $N=E/T$ (người)

Trong đó:
- L là **số nghìn dòng lệnh** (KLOC)
- a, b là **hệ số thực nghiệm** tùy loại dự án được cho trong bảng dưới đây.


> [!example] Ví dụ
> Một phần mềm 20 KLOC, với a = 2.5, b = 1.05 →  E = 2.5 × (20)^1.05 ≈ 54 người-tháng.


> [!info] Lưu ý
> - Phiên bản **COCOMO II** mở rộng hơn, bao gồm cả **yếu tố phức tạp, rủi ro, ngôn ngữ lập trình, năng suất nhóm**...
> - Tham số L (số nghìn dòng lệnh), 

### 9. Phương pháp sử dụng các lá bài

Phương pháp này phổ biến trong **Scrum và Agile**, nhằm giúp đội phát triển **thảo luận và đồng thuận** về mức độ phức tạp của từng hạng mục.
Cách làm:
1. Mỗi thành viên có bộ thẻ với các giá trị (ví dụ: 1, 2, 3, 5, 8, 13, 21, ... ).
2. Product Owner mô tả task/user story.
3. Mỗi người **đưa ra thẻ ẩn danh** thể hiện ước lượng của bản thân.
4. Mọi người thảo luận, giải thích sự chênh lệch và lặp lại cho đến khi thống nhất.

- Ưu điểm: khuyến khích thảo luận, xây dựng hiểu biết chung.  
- Nhược điểm: mang tính chủ quan, không thay thế cho dữ liệu thực tế.

> [!info] Lưu ý
> Thông thường, việc tiến hành ước lượng chỉ nên tối đa 3 lượt/task trong danh sách các đầu việc của từng Sprint (SBI), nếu vẫn chưa đạt được sự đồng thuận thì đội dự án cần có cơ chế để ra quyết định cuối cùng (biểu quyết hoặc quyết định từ một người có kinh nghiệm) 

## Vấn đề trong ước lượng của dự án phần mềm

