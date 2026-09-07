---
title: "AIDD qua lăng kính SDD: quan điểm thực chiến spec-kit"
description: "Quan điểm cá nhân về AI-Driven Development: Spec-Kit SDD chỉ là một bản cài cụ thể, rút ra từ trải nghiệm thực chiến dùng AI agent."
lang: vi
publish: false
updated: 2026-09-07
tags:
  - GenAI
  - Intermediate
  - spec-driven-development
  - ai-agents
  - software-workflow
  - review-gates
socialDescription: "AIDD là kỷ luật dùng AI agent; Spec-Kit SDD chỉ là một bản cài cụ thể. Quan điểm thực chiến của tôi."
permalink: ""
---

Tôi đưa spec-kit vào một dự án nhỏ để học, với niềm tin rằng cứ có spec là agent sẽ ngoan. Ba tuần sau, tôi có một bài học khác: spec chỉ là một nửa của câu chuyện.

Nửa còn lại là kỷ luật vận hành quanh agent. Tôi gọi nó là AI-Driven Development, và SDD chỉ là một bản cài cụ thể của nó.

> [!tldr] Tóm tắt
> - AIDD là kỷ luật dùng AI agent có kiểm soát, SDD là một bản cài cụ thể của kỷ luật đó
> - Chuỗi specify → plan → tasks → implement giữ mỗi bước agent trong phạm vi review được
> - Review gate giữa các bước là điểm khác biệt lớn nhất với vibe coding
> - SDD nguyên bản hổng mảng UI/UX-as-spec, cần extension như wireframe và refine để lấp lại

## AIDD là gì theo tôi 🔍

> [!note] Trả lời nhanh
> AIDD là workflow dùng AI agent có kỷ luật: spec-first, chia nhỏ task, review gate ở mỗi bước.

Hãy tưởng tượng thuê một thợ mộc rất nhanh nhưng không bao giờ hỏi lại. Tôi đưa bản vẽ sơ sài, thợ đóng xong cả cái tủ trong mười phút, sai kích thước. Lỗi không nằm ở người thợ. Lỗi nằm ở cách tôi giao việc.

AI agent cũng vậy. Vibe coding là đưa prompt mơ hồ rồi nhận code mơ hồ, nhanh nhưng không kiểm soát được. AIDD lật ngược lại: con người giữ quyết định ở những điểm rẻ nhất để sửa sai, agent thi hành trong phạm vi đã chốt.

Tôi đúc kết AIDD thành ba trụ cột. Thứ nhất, spec-first: mọi feature được ghi thành spec trước khi có dòng code nào. Thứ hai, decomposition: feature lớn bị chẻ thành task nhỏ, mỗi task đủ bé để review trong vài phút. Thứ ba, review gate: giữa các pha luôn có điểm dừng để con người phê duyệt hoặc bác bỏ.

Ba trụ cột này không gắn với tool nào. Dùng slash command, dùng skill, hay thậm chí làm thủ công bằng file markdown cũng được, miễn là giữ đủ ba trụ. Đó là lý do tôi xem SDD là một bản cài, không phải bản thân AIDD.

## SDD chỉ là bản cài 📝

> [!note] Trả lời nhanh
> Spec-Kit SDD là một cài đặt cụ thể của AIDD: spec-first cộng review gate, đóng gói thành toolchain.

SDD trả lời câu hỏi *xây cái gì và theo thứ tự nào*. Git workflow như [GitHub Flow](https://docs.github.com/en/get-started/using-github/github-flow) trả lời câu hỏi *phân phối code ra sao*. Hai lớp này bổ sung cho nhau, không thay thế nhau.

SDD cũng đứng cao hơn TDD một mức. TDD định nghĩa hành vi kỳ vọng ở mức test, từng hàm từng case. SDD định nghĩa scope ở mức feature: hệ thống gồm những gì, luồng chính ra sao, tiêu chí chấp nhận là gì. Trong dự án của tôi, cả hai cùng tồn tại, SDD dẫn đường ở tầm feature, test dẫn đường ở tầm implementation.

Điều khiến SDD đáng chú ý năm 2026 là nó đã thành một category tool, không còn là ý tưởng lẻ. [Spec Kit của GitHub](https://github.com/github/spec-kit) là bản cài mã nguồn mở, agent-agnostic, hỗ trợ hàng chục coding agent. Bên cạnh đó còn có Kiro gắn với IDE, Claude skills dạng lightweight, OpenSpec tối giản cho codebase có sẵn. Mỗi tool đặt cược khác nhau giữa portability và integration depth, nhưng xương sống đều giống nhau: requirements, design, tasks, implementation, validation.

Tôi chọn Spec Kit vì nó lưu spec dưới dạng markdown ngay trong repo, không khóa vào IDE nào. Quyết định này mang tính thực dụng hơn triết lý: dự án học tập của tôi đổi agent liên tục, artifact phải sống độc lập với tool.

## Chuỗi specify đến implement ⚙️

> [!note] Trả lời nhanh
> Bốn bước specify → plan → tasks → implement, mỗi bước sinh artifact review được trong thư mục specs theo từng feature.

Chuỗi lệnh chạy như một dây chuyền. `/speckit.specify` biến mô tả tự nhiên thành spec cùng các contract. `/speckit.plan` sinh design và implementation artifact từ spec. `/speckit.tasks` sinh task list có thứ tự phụ thuộc mà không cần prompt thêm. `/speckit.implement` thi hành toàn bộ hoặc một phần task list.

Hãy tưởng tượng xây nhà. Specify là bản vẽ kiến trúc: mấy phòng, cửa hướng nào, chịu lực ra sao. Plan là bản vẽ kết cấu và điện nước: dầm ở đâu, ống đi đường nào. Tasks là lịch thi công từng đội theo thứ tự. Implement là ngày khởi công. Không ai đổ bê tông khi bản vẽ kiến trúc còn đang tranh cãi.

Nguyên tắc tôi rút ra từ thực chiến: specify chỉ viết WHAT và WHY, cấm tech stack, API và cấu trúc code ở bước này. Mọi chi tiết HOW dồn xuống plan. File prompt của dự án tôi tách hai lớp này triệt để, mỗi requirement xuất hiện đúng một lần ở đúng lớp sở hữu nó. Cách tách này giữ spec ngắn gọn và giữ plan khỏi việc tranh cãi nghiệp vụ.

Mỗi feature có một thư mục riêng chứa spec, plan, tasks, contracts và wireframes. Task ID mang prefix theo domain thay vì ID ngẫu nhiên, nhờ đó traceability chạy xuyên suốt từ task ngược về spec rồi tới code. Dự án học tập của tôi có tám feature theo đúng pipeline này, từ nền tảng auth đến phân loại phản hồi bằng AI và bàn giao ticket.

Điểm tôi thích nhất: `/speckit.specify` tự tạo feature branch từ nhánh tích hợp trước khi viết spec. Nhờ đó mỗi spec gắn với đúng một branch, không bao giờ lẫn.

## Review gate giữ agent 🛡️

> [!note] Trả lời nhanh
> Review gate giữa spec và plan là nơi bắt ambiguity rẻ nhất, trước khi nó khóa cứng vào code.

Tài liệu workflow chính thức của Spec Kit mô tả gate chuẩn: specify xong thì dừng chờ approve hoặc reject, plan xong lại gate một lần nữa, xem [tham khảo workflow](https://github.com/github/spec-kit/blob/main/docs/reference/workflows.md). Gate không phải lễ nghi. Đó là nơi con người làm đúng một việc mà agent làm dở nhất: phát hiện yêu cầu mơ hồ.

Tôi từng chứng kiến agent "tối ưu" ra hành vi không ai yêu cầu, chỉ vì spec viết lửng một câu. Không có gate, câu lửng đó đi thẳng vào plan, thành task, thành code, thành bug production. Có gate, tôi bắt nó ở spec trong năm phút đọc. Sửa ambiguity ở spec rẻ hơn sửa code đã khóa cả chục lần.

Dự án của tôi còn đi xa hơn template mặc định. File constitution của repo ghi rõ nguyên tắc bất khả xâm phạm, trong đó có điều khoản override: không bắt library-first, không bắt test-first cứng nhắc ở giai đoạn này. Verification lúc đó chỉ gồm CI lint và manual check. Nghe thì lỏng lẻo, nhưng đó là quyết định có ý thức cho dự án học tập: gate dồn vào spec và plan, implementation được phép chạy nhanh.

Bài học xương máu của tôi: SDD mà bỏ review gate thì chỉ là vibe coding chậm hơn. Vẫn prompt, vẫn nhận code, chỉ thêm vài file markdown trung gian không ai đọc. Gate là thứ duy nhất biến đống artifact thành kiểm soát thực sự.

## Lỗ hổng UI/UX 🧩

> [!note] Trả lời nhanh
> SDD nguyên bản không xử lý UI/UX-as-spec: mockup trôi khỏi spec mà không cơ chế nào báo.

Đây là khoảng trống lớn nhất tôi vấp phải. Spec thay đổi liên tục qua các vòng refine, nhưng UI mockup đứng yên. Không ai báo cho tôi biết bản vẽ giao diện đã stale. Đến lúc implement, agent code theo spec mới, giao diện theo mockup cũ, ráp lại lệch nhau.

Vấn đề thứ hai tinh vi hơn: design token. Dự án có file design quy định màu sắc, font, spacing, kèm nguyên tắc do và don't. Nhưng agent không đọc file đó trừ khi bị ép. Thiếu token, agent đoán mò mã màu và kích thước pixel. Mỗi lần đoán là một lần design system rò rỉ.

Hãy tưởng tượng tủ quần áo chung của cả nhà. Quy định ghi rõ áo khoác treo ngăn trên, nhưng không ai kiểm tra. Mỗi người treo một kiểu, một tháng sau không ai tìm được gì. Design token không có gate cũng thành mớ hỗn độn như vậy.

Tôi kết luận: spec của SDD nguyên bản là spec của backend mindset. Nó mô tả data model, API contract, task graph rất tốt, nhưng xem UI như chi tiết implementation để agent tự lo. Với sản phẩm có giao diện thật, quan điểm đó sụp đổ nhanh.

## Extension lấp khoảng trống 🔧

> [!note] Trả lời nhanh
> Bộ extension refine và wireframe biến UI mockup thành contract có gate STALE và SIGNED_OFF.

Thay vì than phiền tool thiếu, tôi mở rộng nó. Hệ sinh thái extension địa phương trong dự án gồm bốn mảnh: bug, git, refine và wireframe. Hai mảnh sau là lời giải cho lỗ hổng UI/UX.

Cơ chế gọi là UI Impact Gate, chạy tự động giữa refine spec và lan tỏa thay đổi. Mỗi lần spec được refine, hệ thống phân loại change thành UI-AFFECTING hoặc NON-UI. Nếu change chạm tới giao diện, contract UI Mockup trong spec bị đánh dấu STALE. Lệnh lan tỏa thay đổi từ chối chạy khi contract còn STALE, trừ khi người dùng ép bằng flag force kèm cảnh báo in rõ.

Vòng lặp wireframe render mockup thành file SVG có version. Chỉ khi vòng review ký duyệt, contract mới chuyển từ STALE sang SIGNED_OFF và gate mở lại. Nhờ đó mockup không bao giờ âm thầm trôi khỏi spec nữa.

Hai extension còn lại giữ nhịp cho phần còn lại của workflow. Extension bug chuẩn hóa quy trình assess, fix và test cho defect. Extension git chuẩn hóa tạo branch, commit và validate tên branch. Tất cả sống dưới dạng file markdown versioned trong repo, tái tạo skill agent bằng một script đồng bộ duy nhất.

Quan điểm của tôi sau trải nghiệm này: đừng đánh giá SDD qua toolchain gốc. Hãy đánh giá qua khả năng mở rộng của nó. Một workflow tốt không phải workflow đủ cho mọi thứ, mà là workflow cho phép lấp gap mà không phá vỡ xương sống.

<!-- Video suggestion: GitHub Spec Kit overview, url="https://youtube.com/watch?v=..." (review and embed after publish approval) -->

<!-- Video suggestion: Demo wireframe review loop với UI Impact Gate, url="https://youtube.com/watch?v=..." (review and embed after publish approval) -->

## Câu hỏi thường gặp ❓

> [!question] SDD có phải là AIDD không?
> Không. SDD là một bản cài của AIDD. AIDD là kỷ luật chung gồm spec-first, decomposition và review gate. SDD cụ thể hóa kỷ luật đó bằng chuỗi specify đến implement.

> [!question] Khi nào không cần SDD?
> Task nhỏ, độc lập, không mơ hồ thì viết trực tiếp nhanh hơn. SDD đáng giá khi feature cần phối hợp nhiều bước agent hoặc nhiều người cùng review một spec chung.

> [!question] Review gate có làm chậm quá không?
> Gate ở spec chuyển sang plan là rẻ nhất trong cả chuỗi. Sửa một câu mơ hồ trong spec tốn vài phút, sửa code đã khóa theo câu đó tốn gấp nhiều lần.

> [!question] Bắt đầu SDD từ đâu trên repo có sẵn?
> Khởi tạo Spec Kit trên repo hiện tại, viết spec cho một feature nhỏ nhất có thể, giữ gate thủ công ở mỗi bước. Chỉ automate gate sau khi đã quen đọc spec nhanh.

## Kết luận 📌

SDD là bản cài tốt nhất của AIDD mà tôi đã dùng trực tiếp, nhưng giá trị thật nằm ở kỷ luật chứ không nằm ở tool: spec-first, gate rõ ràng, extension lấp gap. Tool đổi theo năm, kỷ luật ở lại.

Nếu đang dùng AI agent mỗi ngày, tôi đề xuất bắt đầu từ một gate duy nhất giữa spec và plan. Giữ được gate đó, phần còn lại của AIDD tự nhiên thành hình.

<!--
## Vùng liên kết nội bộ (Internal Linking Zones)
- spec-driven-development — bài draft có sẵn cùng folder (chưa publish, chưa link vội)
- GitHub Flow — candidate cho bài tiếp theo
- Stacked Pull Requests — candidate cho bài tiếp theo
- TDD Red-Green-Refactor — candidate cho so sánh SDD vs TDD
-->

<!--
## Khoảng trống nội dung cần khai thác (Content Gaps to Exploit)
1. So sánh định lượng SDD vs vibe coding trên cùng task (thời gian, số vòng sửa)
2. Case study wireframe gate chặn regression UI cụ thể
3. Khi nào KHÔNG dùng SDD — checklist ra quyết định
-->

<!--
SEO & GEO
Primary: AI-Driven Development workflow
Secondary: Spec-Driven Development, spec-kit, review gate, specify plan tasks implement, stacked pull requests, AI agent workflow
Intent: informational / opinion
Word count plan: ~2820w (6 H2 × ~350w + FAQ 4 × 80w + intro/conclusion 400w) — planning estimate only; actual count measured by blog-write wc command
Template: thought-leadership / opinion
Flesch target: 60-70
-->
