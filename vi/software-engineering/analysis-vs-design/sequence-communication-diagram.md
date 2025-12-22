---
stage: Publish
draft: false
title: Biểu đồ tuần tự và giao tiếp
description:
tags:
  - analysis-and-design
  - sequence-diagram
  - communication-diagram
  - interaction-diagram
  - modeling-language
socialDescription:
socialImage:
permalink:
lang:
aliases:
cssclasses:
---
## Biểu đồ tương tác 🤝

Biểu đồ tương tác là công cụ giúp mô tả cách các đối tượng trong hệ thống **giao tiếp** với nhau thông qua việc trao đổi thông điệp. Trong UML, có hai loại biểu đồ tương tác chính:
- **Biểu đồ tuần tự** (Sequence Diagram): tập trung vào **trình tự thời gian** của các thông điệp.
- **Biểu đồ giao tiếp** (Communication/Collaboration Diagram): tập trung vào **cấu trúc quan hệ** giữa các đối tượng.

👉 "Tập trung" ở đây chỉ nhấn mạnh khả năng làm rõ một khía cạnh nào đó của từng biểu đồ (không chỉ riêng 2 biểu đồ này), tức là biểu đồ tuần tự cũng có khả năng thể hiện cấu trúc quan hệ nhưng không rõ ràng và ngược lại. Do đó, chúng có thể được thay thế cho nhau trong một số tình huống (mặc dù biểu đồ tuần tự được ưa chuộng hơn)  

## Biểu đồ tuần tự ⏱️

[Biểu đồ tuần tự](https://www.uml-diagrams.org/sequence-diagrams-examples.html) cho thấy **trình tự gửi và nhận** thông điệp giữa các đối tượng **theo dòng thời gian** nhằm mô hình hóa [[unified-modeling-language#^c77eec|cộng tác]] (cái mà hiện thực hóa ca sử dụng). Nó biểu diễn tương tác ở dạng biểu đồ 2 chiều:
- **Chiều dọc**: trục thời gian (tính từ trên xuống).
- **Chiều ngang**: các đối tượng tham gia tương tác, gồm **tên** (thường được đặt trong hình hộp với stereotype để phân biệt vai trò) và [đường chu kỳ sống](https://www.uml-diagrams.org/sequence-diagrams.html#lifeline) (đường nét đứt dọc) đại diện cho vòng đời tồn tại của đối tượng.

Trong vòng đời tồn tại của một đối tượng, khoảng thời gian từ lúc tham gia tương tác bằng cách thực hiện một thủ tục đến lúc hoàn tất thủ tục đó được gọi là [đặc tả thực thi](https://www.uml-diagrams.org/sequence-diagrams.html#execution) (activation). Nó được biểu diễn bằng một **thanh chữ nhật dọc** theo đường chu kỳ sống. Bản thân thanh này cũng có thể chứa thanh của các đối tượng khác sau nó như một **tiến trình con bên trong**. *Ví dụ: đối tượng A tương tác với B thì B là tiến trình con vì phải chờ B chạy xong thì A mới thực thi được tiếp.*  

[Thông điệp](https://www.uml-diagrams.org/interaction-message.html) là cầu nối giữa các thanh đặc tả thực thi nói riêng và đối tượng nói chung, thanh sau chỉ hoạt động (đối tượng chứa thanh đấy bắt đầu tham gia tương tác) khi thanh trước **gửi thông điệp** và ngừng hoạt động để **trả về phản hồi** khi kết thúc tương tác. Trong khi thông điệp trả về được biểu diễn bởi **mũi tên nét đứt** (có thể không thể hiện trong biểu đồ nếu dễ hiểu) thì thông điệp gửi đi có 3 cách biểu diễn tương ứng 3 loại thông điệp: 
^e913c5

- **Thông điệp đồng bộ**: Bên gửi chờ cho đến khi bên nhận xử lý xong rồi mới tiếp tục, được vẽ bằng mũi tên nét liền có đầu tam giác đặc hướng về bên nhận. Ví dụ: Gọi một phương thức trong Java/C++ thì chương trình dừng lại cho đến khi phương thức trả về.

- **Thông điệp không đồng bộ**: Bên gửi không chờ kết quả mà tiếp tục thực hiện công việc khác ngay sau khi gửi, được vẽ bằng mũi tên nét liền có đầu tam giác rỗng hướng về bên nhận. Vi dụ: Trong lúc chờ phản hồi tin nhắn từ sếp, bạn có thể pha một cốc cà phê và ngồi xem một bộ phim yêu thích của mình.

- **Thông điệp cho chính đối tượng gửi** (đệ quy): Tương tự như cách bạn độc thoại nội tâm với chính mình, tự gửi thông điệp rồi tự phản hồi nó. Điều này khiến bên gửi tạo thêm một thanh đặc tả thực thi mới chồng lên thanh ban đầu và một mũi tên nét liền quay ngược trở lại chính thanh mới đó.

Đối với các tương tác phức tạp, biểu đồ tuần tự hỗ trợ các [phân đoạn](https://www.uml-diagrams.org/sequence-diagrams-combined-fragment.html) (combined fragments) để đơn giản hóa khung nhìn và tăng tính dễ đọc. Phân đoạn là một cái khung chứa 2 thành phần:
- **Tên khung** (toán tử - operator): xác định loại thao tác (cấu trúc điều khiển) áp dụng cho nội dung trong khung như lặp (loop), rẽ nhánh (alt), song song (par), tùy chọn (opt), ... 
- **Nội dung trong khung** (toán hạng của tương tác - interaction operands): Một hoặc nhiều nội dung cụ thể tham gia vào thao tác. Ví dụ: phân đoạn có nhãn loop (thao tác lặp) thì toàn bộ nội dung trong phân đoạn dưới dạng tương tác (kiểm tra sức khỏe chẳng hạn) chính là toán hạng của tương tác đó, và chỉ dừng lại khi thỏa một điều kiện nào đó (con bệnh khỏe lại chẳng hạn)

> [!challenge]- Thử thách
> Trong ca sử dụng "Đăng nhập hệ thống":
> 1. Người dùng → gửi yêu cầu đăng nhập đến Ứng dụng.
> 2. Ứng dụng → gửi thông tin đến CSDL để kiểm tra người dùng tồn tại hay không.
> 3. CSDL → trả kết quả cho Ứng dụng.
> 4. Ứng dụng → thông báo đăng nhập thành công/thất bại cho Người dùng.
>    
> Từ mô tả biểu đồ tuần tự trên, hãy thử tự giải quyết các vấn đề sau và gửi lời giải vào <a href="#comment-box">hộp nhận xét</a> bài viết:
> - Xác định các đối tượng tham gia vào tương tác/cộng tác
> - Có bao nhiêu tiến trình con của đối tượng Ứng dụng?
> - Có đối tượng nào gửi thông điệp cho chính nó không?
> - Loại thông điệp được dùng trong biểu đồ này là gì?
> - Những thiếu sót của biểu đồ này (nếu có) được trình bày ra sao nếu dùng phân đoạn?
> - Vẽ biểu đồ này mà bạn cho là đúng (not easy)

## Biểu đồ giao tiếp 🧩

[Biểu đồ giao tiếp](https://www.uml-diagrams.org/communication-diagrams-examples.html) chỉ rõ **cấu trúc quan hệ** giữa các đối tượng tham gia tương tác (điều mà biểu đồ tuần tự biểu diễn không rõ ràng), nhằm mô hình hóa một **luồng xử lý/thủ tục** nào đó khi thiết kế chi tiết. Nó được minh họa dưới dạng đồ thị các nút được liên kết với nhau. Cụ thể:
- [Nút](https://www.uml-diagrams.org/communication-diagrams.html#lifeline): là các đối tượng tham gia tương tác, được vẽ bằng một hình hộp với stereotype để phân biệt vai trò
- **Liên kết**: là quan hệ tương tác giữa hai đối tượng, được vẽ bằng một đường nét liền giữa chúng (tùy vào chiều giao tiếp sẽ có thêm mũi tên)

Quan hệ (liên kết) giữa hai đối tượng không chỉ đơn thuần là đường nối mà còn chứa đựng các thông tin làm rõ quan hệ, thể hiện nên **cấu trúc** của nó. Những thông tin trong cấu trúc quan hệ bao gồm:
- **Thông điệp cụ thể**: thường được biểu diễn bằng ngôn ngữ tự nhiên hoặc dưới dạng phương thức `method(parameters)`.
- **Số thứ tự giao tiếp**: thể hiện trình tự các thông điệp được gửi đi, được đánh theo định dạng phân cấp (1, 2, 2.1, ...). Phân cấp ở đây thể hiện sự gom nhóm các thông điệp (thông điệp cha-con)
- **Hướng giao tiếp**: thể hiện chiều gửi thông điệp, được vẽ bằng một mũi tên nhỏ nằm sát đường kết nối. Tùy vào [[sequence-communication-diagram#^e913c5|loại thông điệp]] sẽ có cách biểu diễn khác nhau. 
- **Các thông tin tùy chọn khác**: Tiền/Hậu điều kiện, giá trị trả về, ... 

> [!info] Lưu ý
> - Tất cả các thông tin trong cấu trúc quan hệ trên khi kết hợp với nhau sẽ được gọi là [Thông điệp](https://www.uml-diagrams.org/communication-diagrams.html#message) (khác với Thông diệp cụ thể)
> - Trong một số trường hợp, số thứ tự có thể gắn với tên của **luồng xử lý/thủ tục** (chính là cả cái biểu đồ giao tiếp). Nếu không, tất cả thông diệp trong biểu đồ phải được đánh số thứ tự giao tiếp
> - Thông điệp trong các luồng xử lý/thủ tục khác nhìn chung diễn ra **đồng thời**, trừ khi có sự phụ thuộc tường minh nào đó được mô tả. 

> [!challenge]- Thử thách
> Trong ca sử dụng "Đặt vé máy bay", Người dùng ↔ Ứng dụng đặt vé ↔ Hệ thống thanh toán ↔ Hãng hàng không. Thông điệp có thể là:
> 1. Người dùng gửi yêu cầu đặt vé.
> 2. Ứng dụng liên hệ hệ thống thanh toán.
> 3. Hệ thống thanh toán gửi xác nhận đến Hãng hàng không.
> 4. Kết quả trả về cho Người dùng.
>    
> Từ mô tả biểu đồ giao tiếp trên, hãy thử tự giải quyết các vấn đề sau và gửi lời giải vào <a href="#comment-box">hộp nhận xét</a> bài viết:
> - Xác định các đối tượng (nút) tham gia vào tương tác
> - Các loại thông điệp được dùng trong biểu đồ này là gì?
> - Vẽ biểu đồ này mà bạn cho là đúng (not easy)

## Mục đích của biểu đồ tương tác 🎯

### Mô hình hóa tương tác theo thời gian
Giúp làm rõ **trình tự các thông điệp** được gửi giữa các đối tượng tham gia tương tác. Cách làm:
1. Xác định tương tác đó ứng với khía cạnh động nào của hệ thống (bản thân hệ thống, hệ thống con, thao tác, lớp, kịch bản ca sử dụng, cộng tác, ...) 
2. Xác định và đặt các đối tượng tham gia tương tác vào biểu đồ theo thứ tự quan trọng giảm dần từ trái sang phải
3. Vẽ đường chu kỳ sống của từng đối tượng
	- Trong hầu hết trường hợp, các đối tượng sẽ tồn tại xuyên suốt quá trình tương tác (tức là không có đối tượng nào được tạo/hủy)
	- Với các đối tượng được tạo/hủy, đường này nên được sắp xếp phù hợp và chỉ rõ thời điểm tạo/hủy bởi các thông điệp được gán stereotype là `<<create>>` hay `<<delete>>`
4. Bắt đầu với thông điệp khởi tạo tương tác, tiếp đó là các thông điệp theo sau từ trên xuống dưới giữa các đường chu kỳ sống, chỉ rõ các thuộc tính thông diệp (danh sách tham số, điều kiện/ràng buộc, ...) và thêm [[unified-modeling-language#Phần tử chú thích|chú thích]] nếu cần làm rõ thêm tương tác
5. Xác định thời điểm ngừng tương tác giữa 2 đối tượng để vẽ thông điệp trả về và đặt thanh đặc tả thực thi lên đường chu kỳ sống giữa 2 thông điệp: gửi (bắt đầu tương tác) và nhận (kết thúc tương tác)

### Mô hình hóa tương tác theo tổ chức đối tượng
Giúp làm rõ **quan hệ cấu trúc** giữa các đối tượng tham gia tương tác Cách làm:
1. Xác định tương tác đó ứng với khía cạnh động nào của hệ thống (bản thân hệ thống, hệ thống con, thao tác, lớp, kịch bản ca sử dụng, cộng tác, ...) 
2. Xác định và đặt các đối tượng tham gia tương tác vào biểu đồ như các nút của đồ thị (đối tượng quan trọng hơn sẽ nằm gần trung tâm)
3. Thiết lập thuộc tính khởi tạo cho từng đối tượng. Nếu giá trị thuộc tính, trạng thái và vai trò của nó thay đổi đáng kể trong quá trình tương tác thì ta giữ lại trên biểu đồ (còn lại lược bỏ để đơn giản hóa đồ thị).
4. Nối giữa các đối tượng có tương tác với nhau bằng một liên kết thể hiện kiểu quan hệ tương ứng (kết hợp, phụ thuộc, ...). Có thể thêm thêm stereotype để làm rõ quan hệ như `<<become>>`, `<<copy>>`, ...
5. Bắt đầu với thông điệp khởi tạo tương tác, tiếp đó là các thông điệp được gắn trên các liên kết phù hợp (bao gồm số thứ tự, hướng giao tiếp, các tùy chọn, ...).

> [!tip]- Thực tiễn tốt nhất
> - **Kết hợp linh hoạt** hai loại biểu đồ để mô hình hóa toàn diện
> - **Biểu đồ tuần tự** thường được dùng để biểu diễn các **kịch bản ca sử dụng**, phù hợp hơn với các tương tác đơn giản, chứa các luồng điều khiển rẽ nhánh.
> - **Biểu đồ giao tiếp** thường được dùng khi thiết kế chi tiết cho các **thủ tục**, phù hợp hơn với các tương tác phức tạp, chứa các luồng điều khiển đa luồng và tương tranh.

## Tổng kết 🎬

Biểu đồ tương tác là **cầu nối** giữa phân tích và thiết kế hệ thống. Nó cho chúng ta hình dung trực quan:
- Ai tham gia (đối tương).
- Họ nói chuyện với nhau ra sao (thông diệp).
- Thứ tự và mối quan hệ như thế nào (biểu đồ tuần tự và giao tiếp).

Nếu ví hệ thống phần mềm là một bộ phim 📽️ thì:
- **Biểu đồ tuần tự** giống như kịch bản chi tiết từng cảnh quay.
- **Biểu đồ giao tiếp** giống như sơ đồ quan hệ giữa các nhân vật trong phim.
