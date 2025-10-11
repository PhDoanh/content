---
stage: Publish
draft: false
title: Quản lý phạm vi dự án
description:
tags:
  - project-management
  - project-scope
socialDescription:
socialImage:
permalink:
lang: vi
aliases:
cssclasses:
  - img
---
## Định nghĩa về phạm vi dự án 

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

## Tầm quan trọng của phạm vi dự án

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

## Lập kế hoạch quản lý phạm vi dự án
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

## Thu thập yêu cầu
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




