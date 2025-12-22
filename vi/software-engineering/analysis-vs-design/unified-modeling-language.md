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
Đây là loại phần tử **tĩnh** của mô hình, tức là những thứ tồn tại trong hệ thống mà được mô tả bởi **danh từ**. Cũng giống như "viên gạch", "xi măng", ... là những danh từ hay phần tử tĩnh trong kế hoạch xây dựng nhà ở. Trong UML, gồm 7 kiểu phần tử cấu trúc sau:

|        Phần tử cấu trúc        | Mô tả                                                                                                                                                                                                    | Ví dụ                                                                                                                                                                                                  |
| :----------------------------: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|         Lớp<br>(Class)         | Giống như "khuôn mẫu" để tạo ra đối tượng, gồm **tên lớp**, các **thuộc tính** (đặc điểm) và **phương thức** (hành vi)                                                                                   | lớp **Sinh viên** chứa các thuộc tính như mã sinh viên, họ và tên, trường, lớp, ... Hành vi có thể là học, thi, nộp học phí, ...                                                                       |
|    Giao diện<br>(Interface)    | Danh sách các **hành vi** mà một lớp phải triển khai/cài đặt **chi tiết** bên trong chúng (giao diện không phải làm)                                                                                     | Giao diện yêu cầu hành vi **Thanh toán**. Lớp triển khai chi tiết bên trong hành vi này gồm: Kiểm tra số dư, Gọi cổng thanh toán, Cập nhật trạng thái thanh toán và Trả về kết quả thành công/thất bại |
|  Cộng tác<br>(Collaboration)   | Một không gian mô tả sự tương tác giữa nhiều đối tượng để cùng thực hiện hành vi nào đó                                                                                                                  | Cộng tác chứa các đối tượng: Sinh viên, Danh mục khóa học, Hệ thống thanh toán phối hợp để hoàn thành hành vi Đăng ký môn học.                                                                         |
|    Ca sử dụng<br>(Use Case)    | Cho người dùng biết được mình có thể làm được những gì với hệ thống, thường được hiện thực hóa bởi cộng tác                                                                                              | Đăng ký môn học, Nộp học phí, Tham gia lớp học, ...                                                                                                                                                    |
| Lớp tích cực<br>(Active Class) | Là một loại lớp (Class) đặc biệt mà đối tượng của nó tự quản lý một hoặc nhiều tiến trình/luồng xử lý song song, với khả năng chủ động thực thi hành vi mà không cần lời gọi từ bên ngoài như lớp thường | Trình lắng nghe sự kiện là một lớp tích cực vì nó luôn 24/7 để nắm bắt các sự kiện và tự quản lý chúng một cách tuần tự hoặc đồng thời (không cần ai nhắc nhở mới làm)                                 |
|   Thành phần<br>(Component)    | Một mảnh ghép phần mềm/chức năng có thể được thay thế bởi thành phần khác mà không ảnh hưởng đến hệ thống                                                                                                | Thư viện lập trình là một thành phần vì cùng một chức năng, nhiều thư viện có thể có nhiều giải pháp khác nhau                                                                                         |
|         Nút<br>(Node)          | Thực thể vật lý được dùng để triển khai hệ thống trong môi trường thực                                                                                                                                   | Máy chủ, thiết bị điện tử, ...                                                                                                                                                                         |

^c77eec

### Phần tử hành vi - Động từ
Đây là loại phần tử **động** của mô hình, tức biểu diễn các **hoạt động** diễn ra trong hệ thống theo thời gian và không gian. Gồm 2 kiểu phần tử hành vi chính:

- **Tương tác (Interaction):** cách các đối tượng gửi thông điệp qua lại để đạt được mục đích nào đó, thường liên quan đến một số phần tử khác gồm thông điệp, chuỗi các hành động và liên kết giữa các thông điệp.
- **Máy trạng thái (State Machine):** mô tả **sự thay đổi trạng thái** của một **đối tượng/tương tác** diễn ra trong vòng đời của chúng để đáp ứng các sự kiện. Nó thường chứa một vài phần tử như các trạng thái, các chuyển (luồng từ trạng thái này sang trạng thái khác), các sự kiện (các tác nhân kích hoạt các chuyển) và các hoạt động (phản hồi khi chuyển trạng thái)

> [!info] Lưu ý
> - Hành vi của một lớp hay sự cộng tác giữa các lớp có thể được biểu diễn bởi một máy trạng thái.
> - Hành vi của nhóm đối tượng hoặc của một thao tác đối tượng có thể được biểu diễn bởi một tương tác.

### Phần tử nhóm gộp
Đúng như tên gọi, phần tử này đóng vai trò tổ chức - sắp xếp các phần tử khác (bao gồm chính nó) trong mô hình UML thành các nhóm. Nên còn được gọi là "Gói" (giống như thư mục các tệp trên máy tính), giúp người quan sát hệ thống có cái nhìn khái quát, người làm hệ thống dễ quản lý các sản phẩn công việc (chế tác) trong quá trình phát triển. 

### Phần tử chú thích
Đây là phần tử chú giải trong mô hình UML, chứa văn bản giải thích hoặc bổ sung ngữ cảnh thông tin cho hệ thống. Ví dụ: "Module này đã lỗi thời từ phiên bản 2.0".

## Các quan hệ trong UML 🔗

Các phần tử ở trên giống như các viên gạch, nhưng rời rạc. Vậy làm sao để chúng kết nối với nhau? Đó chính là chất kết dính (xi măng), còn được gọi là **quan hệ** trong UML. Có 4 kiểu quan hệ cơ bản:

1. **Phụ thuộc (Dependency):** Một phần tử **phải dựa vào** phần tử khác để sống. Ví dụ: lớp **Con người** phụ thuộc vào lớp **Nội tạng**, vì người không thể sống thiếu nội tạng.

2. **Kết hợp (Association):** Là kiểu quan hệ liên kết cố định giữa 2 lớp/đối tượng. Ví dụ: Sinh viên **đăng ký** Môn học. Có hai dạng đặc biệt:
	- **Aggregation (tập hợp):** A có B nhưng B vẫn sống riêng được. Ví dụ: Lớp học có Sinh viên.
	- **Composition (hợp thành):** A có B, nhưng B sống chết cùng A. Ví dụ: Ngôi nhà có căn phòng.

3. **Tổng quát hóa (Generalization):** Là kiểu quan hệ kế thừa **cha - con**. Ví dụ: Con chó là một loài Động vật, kế thừa những đặc tính chung như ăn, ngủ, phát ra tiếng, ... Nhưng cũng có đặc tính riêng như lòng trung thành.

4. **Hiện thực hóa (Realization):** Là kiểu quan hệ **triển khai hợp đồng**. Ví dụ: Lớp **Thanh toán bằng thẻ** hiện thực hóa (triển khai) các chức năng mà giao diện (hợp đồng) **Thanh toán** yêu cầu.

## Các biểu đồ trong UML 📊

Khi bạn có phần tử + quan hệ, thì để dễ nhìn, UML cho phép "lắp ghép" chúng thành **biểu đồ**. UML chia thành 3 nhóm lớn:

### Biểu đồ cấu trúc
Các biểu đồ thuộc nhóm này cho biết hệ thống bao gồm những gì.

- [[class-object-diagram|Biểu đồ lớp]]: chứa các lớp (gồm thuộc tính, phương thức) và quan hệ giữa chúng.
- [[class-object-diagram#Biểu đồ đối tượng|Biểu đồ đối tượng]]: ảnh chụp các đối tượng cụ thể tại một thời điểm.
- [[component-diagram|Biểu đồ thành phần]]: mô tả các mô-đun phần mềm có thể linh hoạt thay đổi.
- [[deployment-diagram|Biểu đồ triển khai]]: mô tả các phần cứng để chạy phần mềm.
- **Biểu đồ cấu trúc tổng quát**: cho thấy cấu trúc bên trong của một thành phần.
- **Biểu đồ gói**: tổ chức hệ thống thành các gói.

### Biểu đồ hành vi 
Các biểu đồ thuộc nhóm này cho biết hệ thống làm những gì.
- [[usecase-diagram|Biểu đồ ca sử dụng]]: hệ thống phục vụ người dùng như thế nào.
- [[activity-diagram|Biểu đồ hoạt động]]: giống [Flowchart](https://en.wikipedia.org/wiki/Flowchart), mô tả luồng xử lý.
- [[state-diagram|Biểu đồ trạng thái]]: vẽ các trạng thái mà đối tượng đi qua.

### Biểu đồ tương tác - một nhánh của hành vi 
Các biểu đồ thuộc nhóm này cho biết ai nói chuyện với ai trong từng hành vi của hệ thống

- [[sequence-communication-diagram#Biểu đồ tuần tự|Biểu đồ tuần tự]]: nhấn mạnh thứ tự thông điệp được trao đổi giữa các đối tượng theo thời gian.
- [[sequence-communication-diagram#Biểu đồ giao tiếp|Biểu đồ giao tiếp]]: nhấn mạnh các mối liên kết khi các đối tượng nói chuyện với nhau.
- **Biểu đồ tổng quát**: giống sơ đồ hoạt động nhưng dùng các tương tác.
- **Biểu đồ thời gian**: cho thấy thay đổi trạng thái theo dòng thời gian.

👉 Tổng cộng UML chứa **14 loại biểu đồ** (còn nữa) - mỗi loại là một góc nhìn khác nhau của cùng một hệ thống.

## Các luật và ràng buộc trong UML ⚖️

UML không phải muốn vẽ sao thì vẽ. Nó có cả rừng **luật** để đảm bảo biểu đồ **hợp lệ**. Các ràng buộc chính:
1. **Quy ước đặt tên:** phần tử phải có tên rõ ràng, nhất quán ở mọi góc nhìn.

2. **Quy tắc phạm vi:** cùng một tên có thể mang nghĩa khác nhau tùy bối cảnh. Ví dụ: `id` trong lớp `Sinh viên` khác với `id` trong lớp `Môn học`.

3. **Quy tắc truy cập:** mức độ hiển thị các thành phần phải rõ ràng (công khai, riêng tư, có giới hạn, …). Ví dụ: thuộc tính `password` của lớp `Tài khoản` phải được ẩn đi đối với các lớp bên ngoài và chỉ hiển thị bên trong nó.

4. **Quy tắc toàn vẹn:** mô hình phải nhất quán (không có quan hệ mâu thuẫn). Ví dụ: Một lớp ở biểu đồ A có thuộc tính X, khi đưa vào biểu đồ B thì cũng phải là X chứ không phải x, 1X, ...   

5. **Quy tắc thực thi:** mô hình động phải dễ hiểu và mô phỏng được hành vi thực tế của hệ thống.

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