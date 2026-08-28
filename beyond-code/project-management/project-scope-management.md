---
publish: false
title: Quản lý phạm vi dự án
description:
tags:
  - project-management
  - project-scope
  - triple-constraint
socialDescription:
socialImage:
permalink:
lang: vi
aliases:
cssclasses:
  - img
updated: 2026-02-10
---
## Định nghĩa về phạm vi dự án 📘

Trước khi quản lý phạm vi, ta cần hiểu *"phạm vi"* nghĩa là gì - nghe có vẻ đơn giản, nhưng trong dự án phần mềm thì nó chính là *"ranh giới vàng"* giữa việc **làm đúng** và **làm lan man** 😅. Theo PMI:

- **Phạm vi sản phẩm (Product Scope)**: là toàn bộ **đặc trưng và tính năng** định nghĩa nên sản phẩm, dịch vụ hoặc kết quả mà dự án tạo ra.
- **Phạm vi dự án (Project Scope)**: là **tập hợp các công việc** cần làm để **bàn giao sản phẩm** với đúng các đặc trưng và tính năng đã nêu.

👉 Hiểu đơn giản: phạm vi sản phẩm nói *"cái gì được tạo ra"*, còn phạm vi dự án nói *"cần làm gì để tạo ra nó"*.  

Nhiều tổ chức gộp hai khái niệm này lại luôn, nên phạm vi dự án thường bao gồm luôn cả phạm vi sản phẩm.

Theo Kathy Schwalbe: Phạm vi dự án là **toàn bộ công việc cần thiết** để tạo ra sản phẩm **và** các **quy trình** dùng để tạo ra sản phẩm đó.  Ví dụ, trong một dự án phần mềm, "sản phẩm" không chỉ là phần mềm chạy được, mà còn là **tài liệu đặc tả yêu cầu**, **tài liệu thiết kế**, **kịch bản kiểm thử**, ...

### Quản lý yêu cầu phần mềm

Trong **dự án phần mềm**, quản lý phạm vi gần như gắn liền với **quản lý yêu cầu phần mềm (software requirements)**. IEEE định nghĩa yêu cầu phần mềm theo ba góc độ:
1. Là điều kiện hoặc khả năng mà người dùng cần từ sản phẩm để giải quyết vấn đề hay đạt mục tiêu.
2. Là điều kiện hoặc khả năng mà **hệ thống/thành phần** phải có để thỏa mãn hợp đồng, tiêu chuẩn hoặc đặc tả.
3. Là bản mô tả **tài liệu hóa** về hai loại điều kiện/khả năng trên.

Còn theo IEEE Computer Society, yêu cầu phần mềm là **thuộc tính cần thể hiện để giải quyết vấn đề trong thế giới thực**, ví dụ: Tự động hóa quy trình kế toán, Sinh báo cáo bán hàng tự động, Hoặc tích hợp với hệ thống ERP của doanh nghiệp, ...

Cuối cùng, PMI định nghĩa yêu cầu phần mềm là **toàn bộ điều kiện, khả năng cần có trong sản phẩm hoặc dịch vụ để thỏa mãn các thỏa thuận** - bao gồm cả **mong muốn** của nhà tài trợ, khách hàng, và các bên liên quan. Những yêu cầu này phải được: làm rõ, phân tích, và ghi lại chi tiết để đo lường, quản lý phạm vi trong quá trình của dự án.

Kế hoạch quản lý yêu cầu phần mềm thường bao gồm:
- Cách **lập kế hoạch, theo dõi, báo cáo** yêu cầu,
- Cách **thực hiện hoạt động quản lý yêu cầu**,
- Cách **xác định độ ưu tiên** của yêu cầu,
- Cách **ghi lại, theo dõi và kiểm soát** thay đổi yêu cầu.

### Tài liệu mô tả thông tin sơ bộ dự án

Trước khi chính thức *"khởi động dự án"*, nhóm dự án phải có **Bản mô tả thông tin sơ bộ** hay còn gọi là **Project Charter**. Đây là *"bản tuyên ngôn"* chính thức của dự án - nói cho mọi người biết: *"Dự án này là gì, vì sao tồn tại, ai chịu trách nhiệm và thành công được đo bằng cách nào"*. Nội dung chính gồm:

1. **Thông tin chung**: Tên dự án, ngày bắt đầu - kết thúc, tổng kinh phí, nguồn vốn, chủ đầu tư, đơn vị thụ hưởng, đơn vị thi công, người đại diện, quản lý dự án, thông tin liên hệ.

2. **Mục tiêu của dự án**:  Mô tả mục tiêu rõ ràng mà dự án hướng tới cuối cùng. VD: Xây dựng Hệ thống đăng ký môn học ĐHQGHN cho phép sinh viên tự chọn kế hoạch học tập phù hợp với chương trình đào tạo tín chỉ.

3. **Sản phẩm bàn giao & mốc thời gian quan trọng**:  Tài liệu đặc tả yêu cầu, Tài liệu thiết kế, Phiên bản kiểm thử chấp nhận, Hệ thống chính thức + tài liệu hướng dẫn

4. **Tiêu chí đánh giá thành công**: Phù hợp với kiến trúc *"Đại học số"*, Thử nghiệm thành công tại 80% đơn vị thành viên, được chấp thuận bởi người dùng

5. **Vai trò & trách nhiệm của các bên liên quan**: Đại diện chủ đầu tư, ban đào tạo, trường thành viên, nhà thầu, ...

6. **Một số rủi ro chính**: Phê duyệt yêu cầu khó vì có nhiều bên tham gia, Khó tuân thủ kiến trúc tổng thể, Nguy cơ trễ tiến độ do lịch gấp, ...

7. **Phần ký phê duyệt chính thức** của chủ đầu tư.

### Đặc thù của phạm vi dự án phần mềm

Khác với các lĩnh vực khác (xây dựng, sản xuất, ...), **sản phẩm phần mềm là vô hình** - bạn không thể *"sờ nắm"* nó như tòa nhà hay linh kiện. Vì vậy, phạm vi của **dự án phần mềm khó kiểm soát hơn**!

Một số lý do chính:

1. **Công việc gắn kết phức tạp**: Một thay đổi nhỏ ở chức năng này có thể ảnh hưởng đến hàng loạt phần khác.

2. **Khác biệt con người**: Thành viên có kỹ năng, thái độ, kỳ vọng khác nhau → quản lý nhân sự khó.

3. **Áp lực từ mục tiêu kinh doanh**: muốn lợi nhuận cao nhưng vẫn đảm bảo chất lượng. Đôi khi phải chọn nhân sự phù hợp (không nhất thiết rẻ nhất).

4. **Tác động đến tổ chức & con người**: ví dụ, phần mềm kế toán mới có thể giúp tăng hiệu quả nhưng khiến một số nhân viên bị thay thế.

5. **Công nghệ thay đổi nhanh**: nếu phát triển quá lâu, nền tảng có thể lỗi thời.

=> Tất cả những yếu tố trên khiến **phạm vi dự án phần mềm** luôn cần được **xác định, giám sát và cập nhật liên tục.**

## Tầm quan trọng của phạm vi dự án 🎯

Phạm vi dự án (**Project Scope**) là phần nền tảng giúp xác định **giới hạn công việc** mà nhóm dự án cần thực hiện. Nó mô tả **những gì sẽ được làm** và **những gì sẽ không được làm**, để đảm bảo tất cả các bên liên quan hiểu và thống nhất về mục tiêu, kết quả đầu ra và các yêu cầu cụ thể của dự án.

Trong các dự án phần mềm, việc xác định rõ phạm vi dự án là vô cùng quan trọng vì:

1. **Giúp thiết lập ranh giới công việc**  
	Phạm vi xác định rõ ràng giúp nhóm phát triển biết chính xác họ cần làm gì và dừng ở đâu. Điều này giúp **tránh phát sinh công việc ngoài kế hoạch (scope creep)**

2. **Là cơ sở cho việc lập kế hoạch và ước lượng**  
    Khi phạm vi được xác định, nhóm quản lý có thể **ước lượng chính xác thời gian, chi phí và nguồn lực** cần thiết. Ngược lại, nếu phạm vi mơ hồ, các hoạt động như lập kế hoạch, ước lượng chi phí hay tiến độ sẽ không đáng tin cậy.
    
3. **Giúp kiểm soát sự thay đổi trong suốt vòng đời dự án**  
    Mọi thay đổi trong yêu cầu hoặc chức năng đều phải được **so sánh với phạm vi ban đầu** để xem xét tác động và ra quyết định có chấp nhận thay đổi hay không. Nhờ vậy, phạm vi đóng vai trò như một *"công cụ kiểm soát"* giúp tránh đi lệch khỏi mục tiêu ban đầu.
    
4. **Tăng cường giao tiếp và hiểu biết giữa các bên liên quan**  
    Tài liệu phạm vi dự án đóng vai trò như một bản *"cam kết chung"* giữa khách hàng, nhà tài trợ và đội dự án. Khi mọi người hiểu giống nhau về mục tiêu và giới hạn dự án, rủi ro hiểu lầm và xung đột sẽ giảm đáng kể.
    
5. **Là cơ sở đánh giá kết quả và thành công của dự án**  
    Cuối cùng, khi dự án hoàn thành, phạm vi chính là **tiêu chí đánh giá** xem dự án có đạt được những gì đã đề ra hay không. Nếu sản phẩm cuối cùng đáp ứng đủ yêu cầu trong phạm vi, dự án được xem là thành công.

## Lập kế hoạch quản lý phạm vi dự án 🧭
Lập kế hoạch **quản lý phạm vi dự án (Scope Management Plan)** là bước định hướng toàn bộ cách thức **xác định, kiểm soát và xác minh phạm vi công việc** trong suốt vòng đời dự án. Nói cách khác, đây là *"kim chỉ nam"* giúp mọi người hiểu rõ cách các phạm vi dự án được quản lý như thế nào.

### Mục tiêu, đầu ra và kỹ thuật lập kế hoạch

Mục tiêu chính của quy trình này là:
- Xác định **quy trình để xây dựng phạm vi dự án chi tiết**.
- Thiết lập **chuẩn mực để kiểm soát các thay đổi phạm vi** trong quá trình thực hiện.
- Giúp **đội dự án và các bên liên quan** thống nhất cùng một hiểu biết về phạm vi công việc.

Kết quả (đầu ra) là một **tài liệu kế hoạch quản lý phạm vi**, thường là **một phần trong kế hoạch quản lý dự án tổng thể**. Tài liệu này mô tả:
- Cách thức xác định, phê duyệt và kiểm soát phạm vi.
- Mối quan hệ giữa **WBS**, **yêu cầu người dùng**, và **sản phẩm bàn giao**.
- Mức độ chi tiết cần thiết trong mô tả phạm vi để tránh hiểu nhầm.

Các công cụ và kỹ thuật thường dùng để hoàn thiện tài liệu trên:
- **Phỏng vấn (Interviews)** với các bên liên quan chính.
- **Các buổi họp lập kế hoạch (Planning Workshops)** để thống nhất phạm vi.
- **Mẫu tài liệu và hướng dẫn (Templates & Guidelines)** từ tổ chức.
- **Hệ thống quản lý thay đổi** để đảm bảo tính nhất quán.

### Nội dung chính của kế hoạch quản lý phạm vi

Kế hoạch quản lý phạm vi bao gồm các nội dung cốt lõi sau:
1. **Cách xác định phạm vi (Scope Definition Process)**
    - Quy định phương pháp để thu thập yêu cầu và mô tả chi tiết phạm vi sản phẩm/dự án.
    - Ví dụ: sử dụng **workshop**, **phỏng vấn**, **bản mô tả yêu cầu (SRS)** hoặc **mô hình hóa quy trình nghiệp vụ**.

2. **Cách xây dựng Cấu trúc phân rã công việc (WBS - Work Breakdown Structure)**
    - Mô tả phương pháp phân rã phạm vi tổng thể thành các gói công việc nhỏ hơn, có thể quản lý và giao cho nhóm thực hiện.
    - Xác định **ai** chịu trách nhiệm tạo và cập nhật WBS.

3. **Cách xác minh phạm vi (Scope Verification)**
    - Nêu rõ quy trình để xác nhận sản phẩm, hạng mục bàn giao (deliverables) có đáp ứng yêu cầu hay không.
    - Ai là người chấp nhận kết quả – thường là **khách hàng** hoặc **nhà tài trợ (sponsor)**.

4. **Cách kiểm soát phạm vi (Scope Control)**
    - Đưa ra quy trình xử lý khi có yêu cầu thay đổi phạm vi.
    - Liên kết với **hệ thống quản lý thay đổi (Change Control System)** để đảm bảo mọi thay đổi được xem xét và phê duyệt chính thức.

5. **Trách nhiệm và vai trò (Roles & Responsibilities)**
    - Liệt kê rõ ai chịu trách nhiệm xác định, cập nhật, phê duyệt phạm vi.
    - Ví dụ: _Project Manager_ chịu trách nhiệm tổng thể, _Business Analyst_ thu thập yêu cầu, _Customer_ xác nhận phạm vi.

## Thu thập yêu cầu 🗣️
Thu thập yêu cầu là **giai đoạn đầu tiên và nền tảng** trong quy trình phân tích yêu cầu của dự án phần mềm. Mục tiêu là **xác định, làm rõ, và ghi nhận đầy đủ nhu cầu của các bên liên quan**. Nếu làm không tốt, toàn bộ dự án có thể đi sai hướng, vì phần mềm được phát triển ra **không đúng hoặc không đủ chức năng** mà người dùng thực sự cần.

1. Mục tiêu của việc thu thập yêu cầu
	- **Xác định đầy đủ nhu cầu và mong đợi của người dùng** về sản phẩm phần mềm.
	- **Giúp nhà phân tích yêu cầu hiểu rõ nghiệp vụ** của tổ chức, từ đó chuyển hóa các nhu cầu thành các chức năng phần mềm phù hợp.
	- **Xây dựng nền tảng cho các bước tiếp theo**: đặc tả yêu cầu, thiết kế hệ thống và kiểm thử.

2. Nguồn thu thập yêu cầu
	- **Khách hàng** hoặc **người dùng cuối**: nhóm cung cấp yêu cầu nghiệp vụ và mong muốn cụ thể.
	- **Tài liệu sẵn có** như quy trình hiện tại, quy định của tổ chức, biểu mẫu nghiệp vụ.
	- **Các chuyên gia nghiệp vụ** (domain experts) – người hiểu sâu cách tổ chức đang vận hành.
	- **Các bên liên quan khác** như nhà tài trợ, ban quản lý, cơ quan quản lý nhà nước (với các yêu cầu pháp lý).

3. Phương pháp thu thập yêu cầu
	- **Phỏng vấn (Interview):** Là phương pháp phổ biến nhất. Giúp khai thác sâu nhu cầu, mong đợi và khó khăn của người dùng. Cần chuẩn bị câu hỏi trước và lắng nghe tích cực.
	- **Quan sát (Observation):** Nhà phân tích theo dõi trực tiếp cách người dùng làm việc để phát hiện quy trình thực tế. Giúp phát hiện khoảng cách giữa “quy trình được mô tả” và “quy trình thực sự đang diễn ra”.
	- **Bảng câu hỏi (Questionnaire):** Hữu ích khi có số lượng người dùng lớn, ở nhiều địa điểm khác nhau. Tuy nhiên, khó khai thác sâu các chi tiết nghiệp vụ.
	- **Workshop/Brainstorming:** Tổ chức buổi thảo luận nhóm giữa khách hàng và đội phát triển. Giúp nhanh chóng xác định và thống nhất yêu cầu quan trọng.
	- **Phân tích tài liệu (Document Analysis):** Thu thập và xem xét các tài liệu như quy trình nội bộ, biểu mẫu, quy định pháp lý. Giúp hiểu rõ quy trình nghiệp vụ hiện hành của tổ chức.
	- **Use Case/Scenario:** Mô tả cách người dùng tương tác với hệ thống qua các tình huống cụ thể. Dễ hình dung và giảm nhầm lẫn trong truyền đạt yêu cầu.

4. Khó khăn khi thu thập yêu cầu
	- Người dùng **không diễn đạt rõ ràng được nhu cầu thật sự** của họ.
	- Các bên liên quan có **mục tiêu khác nhau**, dẫn đến xung đột yêu cầu.
	- Một số yêu cầu có thể **thay đổi trong quá trình phát triển** do thay đổi nghiệp vụ hoặc công nghệ.
	- Sự **thiếu kinh nghiệm** của người thu thập yêu cầu dễ dẫn đến bỏ sót hoặc hiểu sai thông tin.

5. Kết quả của quá trình thu thập yêu cầu
	- **Danh sách yêu cầu tổng hợp (Requirement List)**: bao gồm cả yêu cầu chức năng và phi chức năng.
	- **Biểu đồ Use Case sơ bộ** mô tả tương tác giữa người dùng và hệ thống.
	- **Tài liệu yêu cầu ban đầu (Initial Requirement Document)** - làm cơ sở cho giai đoạn phân tích chi tiết và đặc tả yêu cầu.

> [!info] Lưu ý
> - Luôn **xác nhận lại yêu cầu** với người dùng sau mỗi buổi thu thập để tránh hiểu sai.
> - Ghi lại **mọi thay đổi hoặc bổ sung** yêu cầu trong nhật ký dự án.
> - Sử dụng **ngôn ngữ dễ hiểu, không quá kỹ thuật** khi giao tiếp với người dùng.
> - Tích hợp các công cụ như Jira, Trello, Miro,… để **quản lý và theo dõi tiến trình thu thập yêu cầu** hiệu quả hơn.

## Tạo cấu trúc phân rã công việc 🧮

### Xác định phạm vi dự án
Sau khi đã thu thập đầy đủ và chính xác các yêu cầu của phần mềm cần phát triển, **bước tiếp theo** trong quản lý phạm vi là **xác định phạm vi dự án**. Việc này là nền tảng để xây dựng **cấu trúc phân rã công việc (Work Breakdown Structure - WBS)** của dự án.

Nếu như **yêu cầu phần mềm** là những đòi hỏi về **chức năng** và **đặc trưng** mà sản phẩm phải có, thì **phạm vi dự án** lại xác định rõ **những việc cần làm và không cần làm** trong dự án để có thể tạo ra sản phẩm bàn giao cuối cùng.

#### Vai trò và ý nghĩa
Việc xác định phạm vi dự án có **ý nghĩa đặc biệt quan trọng** vì nó:
- Giúp **cải thiện độ chính xác** khi **ước lượng thời gian, chi phí và tài nguyên** cho dự án.
- Đặt ra **các mốc đo lường tiến độ** và **hiệu quả** của dự án.
- Làm **rõ vai trò và trách nhiệm** của từng bên tham gia, tránh trùng lặp hoặc bỏ sót công việc.

#### Đầu vào của xác định phạm vi
Để thực hiện được bước này, nhóm dự án cần dựa vào các tài liệu:
- **Tài liệu mô tả thông tin sơ bộ của dự án** (Project Charter hoặc các bản ghi nhớ ban đầu).
- **Tài liệu yêu cầu sản phẩm** (Product Requirements).
- **Phân tích của chuyên gia về sản phẩm**, bao gồm đánh giá kỹ thuật, chức năng, và giá trị kinh doanh.

#### Đầu ra của xác định phạm vi
Kết quả của quy trình này là **Tuyên ngôn phạm vi dự án (Project Scope Statement)** và các **cập nhật cần thiết cho các quy trình của dự án**. Thông thường, **bản tuyên ngôn phạm vi** bao gồm:

1. **Mô tả phạm vi sản phẩm** – trình bày chi tiết các chức năng, tính năng và giới hạn của sản phẩm.
2. **Tiêu chí chấp nhận sản phẩm của người dùng** – nêu rõ các điều kiện để sản phẩm được công nhận là hoàn thành, ví dụ như độ chính xác, hiệu năng, giao diện, tính ổn định...
3. **Thông tin chi tiết về các sản phẩm bàn giao (deliverables)** của dự án, bao gồm sản phẩm chính, sản phẩm phụ, tài liệu kèm theo.
4. **Tiêu chí chấp nhận cho từng sản phẩm bàn giao**, ví dụ tiêu chuẩn kiểm thử, kết quả mong đợi, hình thức nghiệm thu.
5. **Các biên, ràng buộc và giả định của dự án**, như giới hạn về nguồn lực, thời gian, công nghệ, hoặc yếu tố pháp lý.

### Tạo bảng phân rã công việc
Bảng phân rã công việc (Work Breakdown Structure - WBS) là **một công cụ nền tảng trong quản lý dự án**, giúp chia nhỏ toàn bộ phạm vi công việc của dự án thành **những phần tử nhỏ hơn, dễ quản lý và dễ kiểm soát**.  

👉 Nói cách khác, WBS giúp biến *"toàn bộ dự án"* thành các phần việc có thể đo lường, theo dõi và giao trách nhiệm cụ thể cho từng người hay nhóm.

Mục tiêu chính:
- Giúp **hiểu rõ phạm vi dự án**.
- Hỗ trợ **ước lượng chi phí, thời gian, và nguồn lực chính xác hơn**.
- Là cơ sở cho việc **lập lịch, phân công nhiệm vụ và kiểm soát tiến độ**.

#### Phương pháp tạo lập WBS

##### Phương pháp sử dụng hướng dẫn

Nếu tổ chức đã có sẵn **hướng dẫn hoặc biểu mẫu** để tạo WBS, ta cần tuân thủ chúng.  
Những hướng dẫn này thường được đúc kết thành *"từ điển WBS"*, mô tả chi tiết các công việc phổ biến trong các dự án trước đó

Ngoài hướng dẫn nội bộ, ta có thể tham khảo **các tổ chức uy tín quốc tế** như:
- PMI (Project Management Institute) - cung cấp mẫu WBS trong sách PMI19.
- Chuẩn **ISO 21511:2018** - hướng dẫn về WBS cho các loại dự án (web, viễn thông, gia công dịch vụ, cài đặt phần mềm, ...)  

> [!check] Ưu điểm
> - Tiết kiệm thời gian: dựa trên các mẫu WBS sẵn có của tổ chức.
> - Đảm bảo **tính nhất quán và chuẩn hóa** giữa các dự án trong cùng doanh nghiệp.
> - Giảm nguy cơ bỏ sót công việc, đặc biệt với **dự án lặp lại hoặc tương tự**.
> - Thường đi kèm **“từ điển WBS”** (WBS Dictionary) giúp mô tả rõ từng hạng mục.

> [!missing] Nhược điểm
> - Có thể **không linh hoạt**, chưa phù hợp hoàn toàn với đặc thù dự án mới.
> - Dễ dẫn đến **tư duy rập khuôn**, bỏ qua cơ hội tối ưu hóa hoặc đổi mới.
> - Nếu mẫu gốc chưa được cập nhật, có thể mang theo lỗi hoặc phần việc không còn cần thiết.

##### Phương pháp tương tự

Phương pháp này dựa trên **kinh nghiệm từ các dự án tương tự trước đó**. Nhà quản lý dự án và đội ngũ xem lại WBS của các dự án có đặc điểm tương đồng (quy mô, lĩnh vực, công nghệ, đối tượng khách hàng) rồi điều chỉnh lại cho phù hợp với dự án mới.  

> [!check] Ưu điểm
> - Dựa trên **kinh nghiệm thực tế** từ các dự án tương tự → đáng tin cậy.
> - Tiết kiệm công sức phân rã vì đã có **mẫu logic về cấu trúc công việc**.
> - Hữu ích khi tổ chức có **cơ sở dữ liệu dự án (project repository)**.

> [!missing] Nhược điểm
> - Chỉ phù hợp khi **dự án mới thực sự giống** với dự án cũ (về phạm vi, công nghệ, quy mô).
> - Dễ **sao chép thiếu kiểm chứng**, dẫn đến sai lệch khi điều kiện dự án thay đổi.
> - Có thể **bỏ qua các rủi ro hoặc yêu cầu đặc thù** của dự án mới.

##### Phương pháp từ trên xuống

Bắt đầu từ **mục tiêu lớn nhất của dự án**, sau đó **phân rã dần thành các phần nhỏ hơn**: Từ toàn bộ dự án → các giai đoạn → các chức năng → các công việc chi tiết.  

> [!check] Ưu điểm
> - Giúp **duy trì tầm nhìn tổng thể**, đảm bảo mọi công việc đều hướng đến mục tiêu chung.
> - Dễ quản lý và **thống nhất cách tiếp cận trong giai đoạn lập kế hoạch**.
> - Hữu ích khi phạm vi dự án đã rõ, có tài liệu mô tả tổng thể chi tiết.
> - Giúp **nhà quản lý cấp cao dễ tham gia và kiểm soát định hướng**.

> [!missing] Nhược điểm
> - **Nguy cơ bỏ sót công việc nhỏ** nếu chỉ nhìn từ góc độ tổng thể.
> - Có thể thiếu sự tham gia của **nhân viên kỹ thuật**, dẫn đến thiếu chi tiết thực tế.
> - Không phù hợp với **dự án có nhiều phần việc chưa rõ ràng hoặc mới mẻ**.

##### Phương pháp từ dưới lên

Ngược lại với phương pháp trên, phương pháp này **bắt đầu từ việc liệt kê các đầu việc nhỏ nhất**, sau đó **gom nhóm dần thành các hạng mục lớn hơn**.  

> [!check] Ưu điểm
> - Phù hợp khi **thành viên đội dự án hiểu rõ các chi tiết kỹ thuật**.
> - Giúp **bao quát đầy đủ mọi công việc nhỏ**, giảm nguy cơ bỏ sót.
> - Thúc đẩy **sự tham gia và cam kết của các thành viên** vì họ trực tiếp đóng góp.

> [!missing] Nhược điểm
> - **Thiếu cái nhìn tổng thể**, dễ dẫn đến trùng lặp hoặc phân bổ không logic.
> - Mất thời gian tổng hợp và chuẩn hóa cấu trúc.
> - Dễ “sa đà” vào chi tiết kỹ thuật mà quên mất mục tiêu cấp cao.

##### Phương pháp bản đồ tư duy

Đây là phương pháp **trực quan hóa nội dung dự án bằng sơ đồ cây**. Từ **trung tâm là tên dự án**, ta **vẽ nhánh chính cho từng nhóm công việc lớn**, rồi **phân nhánh nhỏ dần** cho các hạng mục chi tiết hơn.  

> [!check] Ưu điểm
> - Cực kỳ **trực quan và dễ hiểu**, phù hợp cho các buổi brainstorming nhóm.
> - Kích thích **tư duy sáng tạo và mở rộng ý tưởng**.
> - Dễ dàng điều chỉnh, thêm hoặc bớt nhánh công việc.
> - Giúp **thấy rõ mối quan hệ giữa các hạng mục** ngay từ đầu.

> [!missing] Nhược điểm
> - Thiếu **tính chuẩn hóa** khi chuyển đổi sang định dạng WBS chính thức.
> - Có thể **khó ước lượng hoặc định nghĩa chi tiết đầu ra** cho từng nhánh nếu không có quy ước rõ ràng.
> - Dễ bị cảm tính nếu nhóm chưa quen phương pháp này.

#### Tiêu chí của một WBS tốt

Một WBS được đánh giá là **“tốt”** khi:
- Bao quát **toàn bộ công việc** cần làm để tạo ra sản phẩm bàn giao.
- Được **tổ chức có hệ thống, dễ hiểu và dễ theo dõi**.
- Là **cơ sở cho lập lịch, ước lượng chi phí, quản lý nguồn lực, kiểm soát thay đổi và rủi ro.**

> [!info] Lưu ý
> - Các **mục công việc trong WBS phải mô tả rõ ràng, có thể đo lường và bàn giao được.**
> - Nên **đảm bảo WBS bao quát toàn bộ phạm vi dự án**, không thừa, không thiếu.
> - WBS cần được **rà soát, thống nhất với các bên liên quan** để đảm bảo tính chính xác.
> - Mỗi phần việc nên có **một người hoặc nhóm chịu trách nhiệm rõ ràng**.

### Trình bày bảng phân rã công việc

Tại sao phải làm vậy? Bởi vì trong một dự án, **mỗi vai trò** (như nhà tài trợ, nhà quản lý, lập trình viên, tester,…) có **mối quan tâm và trách nhiệm khác nhau**. Do đó, cùng một bảng phân rã công việc (Work Breakdown Structure - WBS) nhưng sẽ có **nhiều cách trình bày khác nhau** tùy theo góc nhìn. Có **ba cách phổ biến để trình bày WBS**, cụ thể như sau 👇

#### Trình bày theo sản phẩm

%% ![[Pasted image 20251011165311.png]] %%

Đây là **cách trình bày được quan tâm nhiều nhất** bởi cả **nhà tài trợ dự án**, **các bên liên quan**, và **nhà quản lý dự án**.  
Nhà tài trợ - người bỏ vốn cho dự án, thường chỉ quan tâm: *"Khi nào tôi sẽ nhận được sản phẩm hoặc từng phần chức năng của sản phẩm?"*

Do đó, **WBS theo hướng sản phẩm** giúp họ dễ dàng nhìn thấy **thời điểm hoàn thành của từng thành phần** trong sản phẩm tổng thể.  

Nhà quản lý dự án (PM) cũng thường xuyên làm việc với các bên này, nên cách trình bày này **giúp PM nắm bắt rõ mong đợi của khách hàng** và có thể **trao đổi, thương lượng phạm vi hoặc tiến độ phù hợp** để đảm bảo sự hài lòng.

#### Trình bày theo trình tự công việc

%% ![[Pasted image 20251011165348.png]] %%

Khác với góc nhìn của nhà tài trợ, nhà quản lý dự án phải đặc biệt quan tâm đến **lịch trình và thứ tự công việc**. Trong các dự án phần mềm, trình tự này thường được **tổ chức theo các pha của quy trình phát triển phần mềm** (ví dụ: Thu thập yêu cầu → Phân tích → Thiết kế → Lập trình → Kiểm thử → Triển khai).

Với WBS được tổ chức theo **trình tự công việc**, người quản lý sẽ dễ dàng nhận biết:
- Nếu **chưa hoàn thành thu thập yêu cầu**, thì **chưa thể thiết kế**.
- Nếu **chưa thiết kế xong**, thì **chưa thể lập trình được**.

Nhờ đó, PM có thể **can thiệp hoặc điều chỉnh kế hoạch kịp thời** để đưa dự án quay lại đúng tiến độ. Nói chung, cách trình bày này cực kỳ hữu ích cho việc **kiểm soát tiến độ dự án**.

#### Trình bày theo vai trò trong dự án

%% ![[Pasted image 20251011165413.png]] %%

Cách này nhìn dự án **theo góc độ nhân sự và trách nhiệm cá nhân**.  
Trong một dự án phần mềm, mỗi thành viên đảm nhận một vai trò riêng: Nhân viên phân tích nghiệp vụ (BA), Kiến trúc sư phần mềm (Architect), Nhà thiết kế giao diện UI/UX, ...

Mỗi người có **nhiệm vụ cụ thể**, và họ quan tâm nhất đến **phần việc mình chịu trách nhiệm**.  👉 Do đó, **WBS theo vai trò** giúp từng thành viên **thấy rõ phần công việc của mình**, dễ **theo dõi và kiểm soát tiến độ cá nhân**.

## Thẩm định phạm vi dự án ✅

Thẩm định phạm vi dự án (Project Scope Validation) là **quá trình xem xét và xác nhận kết quả công việc của dự án** (tức là các sản phẩm, dịch vụ, hoặc kết quả trung gian) để đảm bảo rằng chúng **được hoàn thành đúng theo yêu cầu và tiêu chuẩn đã được phê duyệt** trong tài liệu phạm vi. 

1. Mục đích của quá trình thẩm định
	- **Đảm bảo tính đầy đủ và chính xác** của phạm vi dự án đã được thực hiện.
	- **Xác nhận sự chấp nhận của khách hàng hoặc người bảo trợ** đối với sản phẩm bàn giao.
	- **Phát hiện sớm các sai sót hoặc khác biệt** giữa sản phẩm thực tế và yêu cầu đã định.
	- **Tăng tính minh bạch và trách nhiệm** giữa nhóm dự án và bên liên quan.

2. Đầu vào cho quá trình thẩm định
	- **Kế hoạch quản lý phạm vi dự án**: (mô tả cách thức xác định, xác minh và kiểm soát phạm vi).
	- **Tuyên bố phạm vi dự án (Project Scope Statement)** - mô tả chi tiết phạm vi và tiêu chí chấp nhận sản phẩm.
	- **Các yêu cầu của khách hàng hoặc hợp đồng dự án.**
	- **Kết quả công việc đã hoàn thành.**
	- **Sổ đăng ký yêu cầu thay đổi** (nếu có thay đổi đã được phê duyệt).

3. Phương pháp thẩm định phạm vi
	- **Xem xét tài liệu (Document Review):** so sánh sản phẩm đầu ra với yêu cầu đã ghi nhận.
	- **Kiểm tra trực quan (Inspection):** kiểm tra thực tế sản phẩm, tính năng hoặc bản demo.
	- **Thử nghiệm, trình diễn (Testing/Demo):** cho khách hàng dùng thử hoặc chứng minh kết quả.
	- **Hội thảo, họp đánh giá (Review Meeting):** thảo luận trực tiếp giữa các bên liên quan để xác nhận kết quả.

4. Kết quả (đầu ra) của thẩm định phạm vi
	- **Danh sách hạng mục được chấp nhận** - những phần đã được khách hàng hoặc các bên liên quan ký duyệt.
	- **Danh sách hạng mục bị từ chối hoặc cần sửa đổi**, kèm lý do và kế hoạch xử lý.
	- **Tài liệu xác nhận bàn giao sản phẩm (Acceptance Documentation).**

> [!info] Lưu ý
> - Quá trình thẩm định **không phải là kiểm thử kỹ thuật (testing)** mà là **kiểm thử về phạm vi** - tức là xác định xem *đã làm đúng cái cần làm chưa*, chứ không phải *làm đúng cách chưa*.
> - Nếu dự án phần mềm, thẩm định thường diễn ra sau mỗi **phiên bản bàn giao (iteration hoặc sprint)**, thông qua **các buổi review hoặc demo** cho khách hàng.    
> - Việc ghi nhận rõ ràng biên bản chấp thuận giúp **tránh tranh chấp về sau**, đặc biệt trong hợp đồng dự án phần mềm theo mô hình Waterfall.

## Giám sát phạm vi dự án 🔍
Trong quá trình triển khai, việc **phạm vi dự án bị thay đổi** là điều hầu như không thể tránh khỏi - đặc biệt là với **dự án phần mềm**. Người dùng thường **chưa xác định rõ** họ muốn gì trên từng giao diện chức năng, hoặc **hệ thống cần bao nhiêu chức năng** để hoàn thành một nghiệp vụ cụ thể. Ngược lại, **đội dự án** cũng **chưa chắc chắn** rằng thiết kế hiện tại của họ (luồng nghiệp vụ, giao diện, chức năng, ...) đã **đáp ứng đúng nhu cầu của người dùng** hay chưa.

Chính vì vậy, **giám sát phạm vi dự án** đóng vai trò **kiểm soát toàn bộ các thay đổi xảy ra trong phạm vi**, nhưng **vẫn phải đảm bảo mục tiêu ban đầu của dự án và chiến lược kinh doanh của tổ chức** được giữ nguyên. Đây là **nhiệm vụ trung tâm** của giai đoạn giám sát.

1. Mục tiêu của quản lý thay đổi phạm vi:
	- Mục tiêu chính là **tác động đến những yếu tố có thể làm thay đổi phạm vi**, nhằm đảm bảo rằng **mọi thay đổi đều được quản lý theo quy trình đã xác định trước** trong **kế hoạch quản lý phạm vi dự án**.  
	- Nói cách khác, khi có một thay đổi được đề xuất (ví dụ: bổ sung chức năng, điều chỉnh yêu cầu, thêm màn hình, thay đổi quy trình nghiệp vụ, v.v.), thì thay đổi đó **chỉ được phê duyệt và thực hiện** nếu nó đi **đúng quy trình** đã quy định.

2. Cơ chế kiểm soát thay đổi
	Trong những **dự án lớn**, việc kiểm soát thay đổi không chỉ do một người phụ trách, mà thường được **thực hiện bởi một "Ban kiểm soát thay đổi"** (_Change Control Board – CCB_). Ban này chịu trách nhiệm:
	- Tiếp nhận và xem xét các đề xuất thay đổi.
	- Đánh giá tác động của thay đổi đến thời gian, chi phí, chất lượng, và phạm vi.
	- Quyết định phê duyệt hoặc từ chối thay đổi.
	- Ghi nhận và cập nhật thay đổi được duyệt vào tài liệu dự án.

3. Điều kiện tiên quyết để quản lý thay đổi hiệu quả
	Công tác **quản lý thay đổi** chỉ có thể thực hiện **hiệu quả khi các bước thu thập yêu cầu và xác định phạm vi dự án ban đầu được làm tốt**.  Nếu phạm vi dự án chưa được xác định rõ hoặc khách hàng chưa đồng ý với các tiêu chí chấp nhận sản phẩm trong danh sách sản phẩm bàn giao, thì **không thể nói rằng phạm vi dự án đã thay đổi**, vì về bản chất, phạm vi đó **vẫn chưa được xác lập rõ ràng ngay từ đầu**.
