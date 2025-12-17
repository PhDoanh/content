---
stage: Publish
draft: false
title: UML - Ngôn ngữ mô hình hóa chuẩn quốc tế cho dân IT
description:
tags:
  - analysis-and-design
  - modeling-language
  - introduction
  - object-oriented
socialDescription:
socialImage:
permalink:
lang: vi
aliases:
cssclasses:
  - img
---
Hãy tưởng tượng bạn đang xây một ngôi nhà: từ việc phân chia phòng ốc, hệ thống điện nước, đến các thiết bị tự động phải hoạt động hài hòa với nhau. Trước khi đặt viên gạch đầu tiên, bạn cần một **bản thiết kế tổng thể** để mọi thứ được kết nối và vận hành trơn tru. Tương tự, trong phát triển phần mềm, **UML (Unified Modeling Language)** là "bản vẽ kỹ thuật" giúp các nhà phát triển mô hình hóa, trực quan hóa và phối hợp xây dựng hệ thống phần mềm một cách chính xác. Nhờ UML, những ý tưởng phức tạp trở nên rõ ràng, dễ hiểu và dễ triển khai, giống như ngôi nhà trong bản thiết kế của kiến trúc sư vậy!

## Lịch sử ra đời và các mục tiêu thiết kế 📜

UML không phải "tự nhiên sinh ra" mà là kết quả của **quá trình hợp nhất nhiều phương pháp khác nhau** trong thập niên 90. Trước đó, có rất nhiều phương pháp mô hình hóa hướng đối tượng, ví dụ:
- **OMT** (Object Modeling Technique) của Rumbaugh.
- **OOAD** (Object-Oriented Analysis and Design) của Booch.
- **Use Case-driven** của Jacobson.

Mỗi phương pháp đều có điểm mạnh riêng, nhưng cũng gây phân tán, khó chuẩn hóa. Chính vì thế:
- Năm 1996, tổ chức [OMG](https://www.omg.org/about/) (Object Management Group) đưa ra yêu cầu chuẩn hóa 👉 UML ra đời.
- Năm 1997, UML chính thức được công nhận là **chuẩn công nghiệp** về mô hình hóa phần mềm.
- Sau đó, UML liên tục phát triển, bổ sung tính năng mới. Bản **UML 2.0 (2004)** đã mở rộng thêm nhiều biểu đồ và cho đến nay vẫn được duy trì, cập nhật.

🎯 **Mục tiêu thiết kế UML:**
- Thống nhất các phương pháp mô hình hóa.
- Cung cấp **ngôn ngữ chung** cho các bên liên quan (nhóm lập trình viên, lãnh đạo cấp cao, nhà quản lý dự án, ...) 
- Hỗ trợ mô tả hệ thống xuyên suốt vòng đời (yêu cầu → thiết kế → triển khai).

## Đặc điểm sử dụng 🔍

UML có nhiều "tính cách" nổi bật:
- **Đa năng:** dùng cho nhiều loại hệ thống, không chỉ riêng phần mềm.
- **Hỗ trợ toàn bộ vòng đời phát triển:** xuất hiện trong mọi giai đoạn (phân tích, thiết kế, triển khai đến vận hành và bảo trì)
- **Không phụ thuộc công nghệ:** UML chỉ mô tả, không gắn với công nghệ cụ thể nào . Ví dụ: không phụ thuộc vào ngôn ngữ lập trình như Java, C++ hay SQL cụ thể nào.
- **Kết hợp được với mọi quy trình phát triển:** RUP, Agile, Waterfall… đều dùng được UML.
- **Hỗ trợ tạo tài liệu:** UML giúp lưu giữ kiến thức hệ thống dưới dạng biểu đồ dễ đọc, dễ chia sẻ.
- **Hướng đến cả người kỹ thuật và phi kỹ thuật:**
    - Nhà quản lý: hiểu yêu cầu qua [[usecase-diagram|biểu đồ ca sử dụng]].
    - Developer: hiểu chi tiết qua [[class-object-diagram|biểu đồ lớp]].

👉 Nói nôm na, UML giống như ngôn ngữ **tiếng Anh** trong ngành phần mềm: không phải ngôn ngữ lập trình, nhưng ai cũng có thể hiểu và giao tiếp được với nhau.

## Phần tử mô hình trong UML 🧩

Trong UML, để vẽ được một mô hình thì bạn phải biết **có những viên gạch nào**. UML chia chúng thành 4 loại:

### Phần tử cấu trúc - Danh từ
Đây là loại phần tử **tĩnh** của mô hình, tức là những thứ tồn tại trong hệ thống mà được mô tả bởi **danh từ**. Cũng giống như "viên gạch", "xi măng", ... là những danh từ hay phần tử tĩnh trong kế hoạch xây dựng nhà ở. Trong UML, gồm 7 kiểu phần tử tĩnh sau:


| Phần tử tĩnh                | Mô tả                                                                                                      | Ví dụ                                                                                                                            | Dạng hình ảnh |
| --------------------------- | ---------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| Lớp (Class)                 | Giống như "khuôn mẫu" để tạo ra đối tượng, gồm tên lớp, các thuộc tính (đặc điểm) và phương thức (hành vi) | lớp **Sinh viên** chứa các thuộc tính như mã sinh viên, họ và tên, trường, lớp, ... Hành vi có thể là học, thi, nộp học phí, ... |               |
| Giao diện (Interface)       | Danh sách các chức năng mà một lớp phải triển khai (giao diện không triển khai chúng)                      |                                                                                                                                  |               |
| Cộng tác (Collaboration)    |                                                                                                            |                                                                                                                                  |               |
| Ca sử dụng (Use Case)       | người dùng biết được mình cos thể làm được những gì với hệ thống                                           | Đăng ký môn học, Nộp học phí, ...                                                                                                |               |
| Lớp tích cực (Active Class) |                                                                                                            |                                                                                                                                  |               |
| Thành phần (Component)      | Một mảnh phần mềm/chức năng có thể được thay thế bở thành phần khác                                        | Đăng nhập, Đăng xuất, ...                                                                                                        |               |
| Nút (Node)                  |                                                                                                            |                                                                                                                                  |               |



- **Lớp (Class):** . Ví dụ: 

- **Giao diện (Interface):** . VD: thanh toán, hiển thị thông tin, sắp xếp tăng dần, ...

- **Ca sử dụng (Use Case):** . VD: 

- **Thành phần (Component):** , VD: 

- **Nút (Node):** Thực thể vật lý (máy chủ, thiết bị điện tử, ...) được dùng để triển khai hệ thống.

👉 Nói nôm na: phần tử cấu trúc chính là **"các thực thể có thật"** trong quá trình thiết kế từ đời thực.

### Phần tử hành vi - "Động từ"

- Đây là **hành động, quá trình xảy ra** trong hệ thống.
- Gồm:
    - **Tương tác (Interaction):** cách các đối tượng gửi thông điệp qua lại.
    - **Máy trạng thái (State Machine):** sự thay đổi trạng thái của một đối tượng.

👉 Hãy hình dung: nếu lớp **Sinh viên** là "người", thì hành vi có thể là "nói chuyện, đăng ký môn, nộp học phí".

### Phần tử nhóm gộp (Grouping Elements)
- Đơn giản là **cái hộp đựng** các phần tử khác.
- UML gọi nó là **Package (gói)**.
- Giúp sắp xếp hệ thống gọn gàng (giống như folder trong máy tính).

### Phần tử chú thích (Annotation Elements)
- Dùng để **ghi chú, giải thích** trong mô hình.
- Ví dụ: "Module này đã lỗi thời từ phiên bản 2.0".

## Các quan hệ trong UML 🔗

Các phần tử ở trên giống như các viên gạch, nhưng rời rạc. Vậy làm sao chúng kết nối với nhau? Đó chính là chất kết dính (xi măng), còn được gọi là **quan hệ** trong UML. Có 4 kiểu quan hệ cơ bản:

1. **Phụ thuộc (Dependency):**
    - Một phần tử **phải dựa vào** phần tử khác.
	- VD: lớp **Hóa đơn** phụ thuộc vào lớp **Đơn hàng**.
	- Dễ hiểu: nếu đơn hàng thay đổi → hóa đơn cũng bị ảnh hưởng.

2. **Kết hợp (Association):**
	- Liên kết cố định giữa 2 lớp/đối tượng.
	- VD: Sinh viên **đăng ký** Môn học.
	- Có hai dạng đặc biệt:
		- **Aggregation (tập hợp):** A có B nhưng B vẫn sống riêng được. (Ví dụ: Lớp học có Sinh viên).
		- **Composition (thành phần):** A có B, nhưng B sống chết cùng A. (Ví dụ: Ngôi nhà có căn phòng).

3. **Khái quát hóa (Generalization):**
    - Quan hệ **cha - con**, tức là kế thừa.
    - VD: _Sinh viên cao học_ là một loại _Sinh viên_.

4. **Hiện thực hóa (Realization):**
	- Quan hệ "hợp đồng - thực thi".
	- VD: Lớp **Thanh toán bằng thẻ** triển khai các chức năng mà giao diện **Thanh toán** yêu cầu.

## Các biểu đồ trong UML 📊

Khi bạn có phần tử + quan hệ, thì để dễ nhìn, UML cho phép "chụp ảnh" chúng thành **biểu đồ**. UML chia thành 3 nhóm lớn:

### Biểu đồ cấu trúc
Các biểu đồ thuộc nhóm này cho biết hệ thống bao gồm những gì

- **Biểu đồ lớp:** vẽ lớp, thuộc tính, quan hệ.

- **Biểu đồ đối tượng:** ảnh chụp các đối tượng cụ thể tại một thời điểm.

- **Biểu đồ thành phần:** mô tả module phần mềm.

- **Biểu đồ triển khai:** mô tả server, máy tính, thiết bị chạy phần mềm.

- **Biểu đồ cấu trúc tổng quát:** cho thấy cấu trúc bên trong của một thành phần.

- **Biểu đồ gói:** tổ chức hệ thống thành các gói.

### Biểu đồ hành vi 
Các biểu đồ thuộc nhóm này cho biết hệ thống làm những gì? 

- **Biểu đồ ca sử dụng:** hệ thống phục vụ người dùng như thế nào.

- **Biểu đồ hoạt động:** giống flowchart, mô tả luồng xử lý.

- **Biểu đồ trạng thái:** vẽ các trạng thái mà đối tượng đi qua.

### Biểu đồ tương tác - một nhánh của hành vi 
Các biểu đồ thuộc nhóm này cho biết ai nói chuyện với ai trong từng hành vi của hệ thống

- **Biểu đồ tuần tự:** nhấn mạnh thứ tự thông điệp theo thời gian.

- **Biểu đồ giao tiếp:** nhấn mạnh các mối liên kết khi đối tượng nói chuyện.

- **Biểu đồ tổng quát:** giống sơ đồ hoạt động nhưng dùng các tương tác.

- **Biểu đồ thời gian:** cho thấy thay đổi trạng thái theo dòng thời gian.

👉 Tổng cộng UML hiện có **14 loại biểu đồ** - mỗi loại là một góc nhìn khác nhau của cùng một hệ thống.

## Các luật và ràng buộc trong UML ⚖️

UML không phải muốn vẽ sao thì vẽ. Nó có cả rừng **luật** để đảm bảo biểu đồ **hợp lệ (well-formed model)**.

Các ràng buộc chính:
1. **Quy tắc đặt tên:** phần tử phải có tên rõ ràng, nhất quán ở mọi góc nhìn.

2. **Quy tắc phạm vi (scope):** cùng một tên có thể mang nghĩa khác nhau tùy bối cảnh. Ví dụ: "id" trong lớp SinhVien khác với "id" trong lớp MonHoc.

3. **Quy tắc truy cập (visibility):** mức độ hiển thị các thành phần phải rõ ràng (public, private, protected…)

4. **Quy tắc toàn vẹn (integrity):** mô hình phải nhất quán (không có quan hệ mâu thuẫn).

5. **Quy tắc thực thi (execution semantics):** mô hình động phải dễ hiểu và mô phỏng được hành vi thực tế.

💡 Nói dễ hiểu: UML giống như ngôn ngữ có ngữ pháp. Nếu vi phạm luật sẽ dẫn tới biểu đồ sai ngữ nghĩa, người khác nhìn vào sẽ không hiểu hoặc hiểu nhầm.

## Kết luận 🔥
Bài viết này đã giúp bạn nắm:
- UML ra đời để **chuẩn hóa** nhiều phương pháp cũ.
- UML có **đặc điểm linh hoạt, đa năng**, dùng cho mọi giai đoạn phát triển.
- UML xây dựng từ **phần tử - quan hệ - biểu đồ**, với **14 loại biểu đồ**.
- UML có **luật** để đảm bảo tính đúng đắn và nhất quán.

👉 Nếu coi UML như một **bản thiết kế ngôi nhà**, thì:
- **Viên gạch** = phần tử mô hình.
- **Chất kết dính** = quan hệ + luật ràng buộc.
- **Ngôi nhà** = biểu đồ hoàn chỉnh.