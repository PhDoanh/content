---

draft: false
title: Các phương pháp ước lượng công việc
description:
tags:
  - project-management
  - estimation-methods
  - work-estimation
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

## Ước lượng công việc và tầm quan trọng ⚖️
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

## Các loại ước lượng 📚
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


## Một số phương pháp và công cụ ước lượng 🧮
 
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
Đây là **một mô hình tham số (parametric model)** rất nổi tiếng do **Barry Boehm** phát triển cuối thập niên 1970, dùng để **ước lượng công sức, thời gian và chi phí** cho việc phát triển phần mềm dựa trên **kích thước của phần mềm** (tính theo nghìn dòng lệnh - KLOC).

COCOMO được xây dựng dựa trên dữ liệu thực tế từ **63 dự án phần mềm** do TRW Systems thu thập, với mục tiêu giúp nhà quản lý có thể:
- Ước lượng được **công sức (Effort)** tính theo người-tháng,
- Ước lượng **thời gian phát triển (Time)**,
- Và xác định **nhân lực cần thiết (Staffing)**,  
    chỉ dựa trên quy mô phần mềm.

Mô hình [COCOMO 81](https://www.geeksforgeeks.org/software-engineering/software-engineering-cocomo-model/) (1981) bao gồm **ba cấp độ** có độ chi tiết tăng dần:

#### COCOMO 81 cơ bản
Là mức đơn giản nhất, dùng cho **ước lượng sớm** khi chưa có nhiều thông tin chi tiết. Công thức tổng quát:
- Công sức: $E = a \times L^b$
- Thời gian: $T = c \times E^d$
- Số người: $N=E/T$

Trong đó: L là số nghìn dòng mã nguồn (KLOC) và a, b, c, d là các hằng số thực nghiệm phụ thuộc loại dự án được cho trong bảng dưới đây.

| Kiểu dự án    | a   | b    | c   | d    |
| ------------- | --- | ---- | --- | ---- |
| Organic       | 3.2 | 1.05 | 2.5 | 0.38 |
| Semi-detached | 3.0 | 1.12 | 2.5 | 0.35 |
| Embeded       | 2.8 | 1.20 | 2.5 | 0.32 |

#### COCOMO 81 trung gian
Đây là mức **chính xác hơn**, vì bổ sung thêm **hệ số điều chỉnh công sức (EAF - Effort Adjustment Factor)** để phản ánh các yếu tố thực tế của dự án. Công thức tổng quát:

$$
E = a \times (KLOC)^b \times EAF
$$

Trong đó: EAF là tích của **15 yếu tố điều chỉnh (Cost Drivers)**, thuộc 4 nhóm chính:
1. **Sản phẩm** (Product attributes): độ tin cậy, độ phức tạp, kích cỡ cơ sở dữ liệu.
2. **Phần cứng** (Hardware attributes): thời gian chạy, ràng buộc bộ nhớ, độ ổn định nền tảng.
3. **Nhân sự** (Personnel attributes): năng lực phân tích, lập trình, kinh nghiệm ứng dụng.
4. **Dự án** (Project attributes): công cụ hỗ trợ, lịch trình, phương pháp quản lý.

💡 Mỗi yếu tố có trọng số từ rất thấp đến rất cao, tương ứng giá trị hệ số (thường trong khoảng 0.7 – 1.46). Mô hình này cho phép **tùy chỉnh linh hoạt** theo đặc điểm từng dự án cụ thể.

#### COCOMO 81 chi tiết
Là cấp cao nhất, kết hợp cả công thức của **mô hình cơ bản và trung gian**, nhưng thêm khả năng **phân rã nỗ lực theo từng giai đoạn** phát triển phần mềm. Ví dụ: yêu cầu, thiết kế, lập trình, kiểm thử, bảo trì…

Ở mỗi giai đoạn, người quản lý có thể ước lượng phần trăm công sức tương ứng. Ví dụ (theo mô hình gốc của Boehm): Thiết kế (15%), Phát triển (50%), Kiểm thử (20%), Tài liệu, bảo trì, quản lý (15%)

Nhờ đó, mô hình chi tiết giúp **theo dõi tiến độ và chi phí thực tế** trong từng giai đoạn cụ thể.

> [!info]- COCOMO II
> [COCOMO II](https://www.softstarsystems.com/cocomo2.htm) là phiên bản mở rộng hơn, bao gồm cả **yếu tố phức tạp, rủi ro, ngôn ngữ lập trình, năng suất nhóm**... Nó ra đời nhằm thích ứng với sự phổ biến của môi trương hướng đối tượng, tái sử dụng mã nguồn và các mô hình phát triển phần mềm mới như Agile, Incremental, Component-based, ... Gồm 3 mô hình con:
> - **Application Composition Model:** cho ước lượng sớm trong giai đoạn thiết kế giao diện, prototype.
> - **Early Design Model:** khi đã có thông tin cơ bản về kiến trúc, nhưng chưa chi tiết.
> - **Post-Architecture Model:** dùng khi đã hoàn tất thiết kế kiến trúc và biết rõ các thành phần.
> 
> Mô hình này được coi là **chuẩn mực công nghiệp hiện đại**, thường được cài trong các công cụ ước lượng tự động.

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

## Một số vấn đề trong ước lượng của dự án phần mềm 🚧
Khi tiến hành ước lượng, ta không thể áp dụng công thức cứng nhắc cho mọi loại dự án. Dự án phần mềm mang trong nó nhiều **đặc thù riêng biệt**, nên để có ước lượng chính xác, người quản lý cần **cân nhắc kỹ** một số điểm sau 👇

1. **Công việc sáng tạo**
Phát triển phần mềm là **một công việc sáng tạo**, không giống như dây chuyền sản xuất trong nhà máy. Mỗi đầu việc, dù tên gọi giống nhau, vẫn có thể phải **làm lại từ đầu** do sự khác biệt về:
- môi trường kỹ thuật,
- yêu cầu phi chức năng,
- hoặc sự thay đổi về công nghệ, hạ tầng, quy mô hệ thống.

👉 Vì thế, **nỗ lực thực tế có thể khác xa ước lượng ban đầu**.  

> [!example] Ví dụ
> Một chức năng *"kết nối cơ sở dữ liệu"* trong dự án A có thể hoàn thành nhanh vì môi trường quen thuộc, nhưng trong dự án B lại phức tạp hơn do yêu cầu bảo mật, cấu trúc cơ sở dữ liệu hoặc công nghệ hoàn toàn khác.

Điều đó có nghĩa: nếu một nhân viên hoàn thành một việc "ước lượng 2 ngày" chỉ trong 2 giờ, **không thể kết luận ngay** rằng ước lượng sai hoặc người đó quá xuất sắc - vì bản chất công việc có thể khác.

2. **Loại dự án**
Mỗi loại dự án khác nhau sẽ dẫn đến ước lượng khác nhau.  

> [!example] Ví dụ
> - Trong **dự án phát triển phần mềm mới**, việc *"tạo chức năng đơn hàng"* phải xây dựng toàn bộ mã nguồn từ đầu.
> - Còn trong **dự án bảo trì hoặc nâng cấp**, phần lớn thành phần (hàm dùng chung, kết nối CSDL, template code) **đã sẵn có**, nên effort nhỏ hơn nhiều.

👉 Vì vậy, **không thể dùng lại ước lượng** từ một dự án này cho dự án khác nếu bản chất của chúng khác nhau.

3. **Mức độ yêu cầu chất lượng**
Khi **yêu cầu chất lượng cao**, công sức để kiểm thử, rà soát, viết tài liệu cũng tăng tương ứng.  

> [!example] Ví dụ
> - **Dự án cho khách hàng** (hợp đồng chi phí cố định): thường khách hàng muốn giảm chi phí nên cắt bớt kiểm thử, review, chỉ đảm bảo *"chạy được"*.
> - **Dự án nội bộ** (phát triển cho chính tổ chức): yêu cầu độ tin cậy cao, vận hành lâu dài, nên cần đầu tư kiểm thử, code review, quản lý cấu hình kỹ hơn.

👉 Do đó, **chi phí và thời gian ước lượng** cũng phải phản ánh đúng yêu cầu chất lượng tương ứng.

Ngoài những đặc thù nêu trên, việc ước lượng dự án phần mềm thường gặp một số vấn đề say đâu làm cho ước lượng thiếu đi sự chính xác:

- **Ước lượng quá nhanh**: Khi đội dự án **chưa phân tích kỹ yêu cầu** hoặc chịu áp lực cần con số sớm, các ước lượng đưa ra thường **vội vã và thiếu cơ sở**. Dẫn tới sai số lớn, tiến độ không thực tế. ➡️ Luôn rà soát và dành đủ thời gian cho bước phân tích trước khi chốt estimate.

- **Người ước lượng thiếu kinh nghiệm**: Nếu người thực hiện ước lượng **chưa có kinh nghiệm hoặc hiểu biết về lĩnh vực dự án**, họ dễ bỏ sót các công việc phụ, hoặc đánh giá thấp độ phức tạp. ➡️ Do đó, **nên để thành viên giàu kinh nghiệm rà soát lại ước lượng** để tránh sai sót.

- **Con người có xu hướng ước lượng thấp**: Tâm lý phổ biến trong nhiều tổ chức là "đưa con số thấp để được chọn, được duyệt" hoặc đơn giản là **quá lạc quan**. Điều này dẫn đến ước lượng thiếu thực tế, deadline chật hẹp, áp lực cao, ảnh hưởng chất lượng sản phẩm. ➡️ Nên thực hiện ước lượng khách quan, có cơ chế kiểm chứng, và luôn thêm phần dự phòng (contingency).

- **Các cấp lãnh đạo đòi hỏi sự chính xác cao**: Các lãnh đạo hoặc chủ đầu tư thường **muốn có con số thật chính xác** để: lên kế hoạch ngân sách, hoặc tham gia đấu thầu. Điều này khiến nhóm dự án **bị ép phải "rút ngắn" ước lượng**, khiến bản estimate trở nên thiếu thực tế. ➡️ Nhiệm vụ của nhà quản lý dự án là phải **bảo vệ ước lượng hợp lý** bằng năng lực **lãnh đạo và thương lượng**, đồng thời cập nhật khi yêu cầu hoặc phạm vi thay đổi.
