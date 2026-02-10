---
title: Biểu đồ lớp và đối tượng
description:
publish: true
updated: 2026-02-10
tags:
  - analysis-and-design
  - modeling-language
  - class-diagram
  - object-diagram
  - static-view
socialDescription:
socialImage:
permalink:
lang: vi
aliases:
cssclasses:
  - img
---
## Tổng quan về khung nhìn tĩnh 🔭
**Khung nhìn tĩnh** là nền tảng cơ bản của UML, nó chứa đựng các phần tử định nghĩa nên những đối tượng **tồn tại** trong hệ thống thông qua các đặc điểm nhận dạng gồm **dữ liệu và hành vi**, nhưng **không phản ánh chi tiết về hành vi động** như cách mà [[sequence-communication-diagram|biểu đồ tương tác]] (biểu diễn của khung nhìn động) thực hiện.

> [!example]- Ví dụ
> Hệ thống quản lý đăng ký học tồn tại một đối tượng là **sinh viên** được nhận diện qua các đặc điểm về:
> - **Dữ liệu**: họ tên, lớp khóa học, mã định danh, ...
> - **Hành vi**: đăng ký khóa học, hủy đăng ký, thanh toán phí học, ...
> 
> 👆 Những thông tin trên sẽ được khung nhìn tĩnh sử dụng và biểu diễn thông qua các biểu đồ tương ứng mà không quan tâm cách các hành vi thực sự được triển khai ra sao.  

Để biểu diễn khung nhìn tĩnh, UML cung cấp hai loại biểu đồ:
- [Biểu đồ lớp](https://www.uml-diagrams.org/class-diagrams-overview.html): được sử dụng phổ biến nhất do tính đa dụng và khả năng phản ảnh sát khung nhìn nhất, nó đại diện cho một tập các đối tượng có chung đặc điểm nhận dạng. *Ví dụ*: lớp số nguyên đại diện cho các số nguyên cụ thể (..., -1, 0, 1, ...), gồm dữ liệu như giá trị và hành vi như cộng, trừ, nhân, chia, ...
- [Biểu đồ đối tượng](https://www.uml-diagrams.org/class-diagrams-overview.html#object-diagram): biểu diễn ảnh chụp (snapshot) của hệ thống tại một thời điểm nhất định, chứa các đối tượng mang trong mình **giá trị nhận dạng cụ thể** như một ví dụ về hệ thống trong thực tế. *Ví dụ*: thay vì nói x có giá là một số nguyên như biểu đồ lớp thì ta nói x có giá trị bằng 5 tại thời điểm hiện tại. 

## Bên trong khung nhìn tĩnh 🔬

### Phân lớp
[Phân lớp](https://www.uml-diagrams.org/classifier.html) là việc **phân/chia** thành các **lớp/nhóm** để mô tả các đối tượng có **định danh, trạng thái, hành vi và quan hệ**. Các lớp/nhóm (loại phân lớp) đấy bao gồm: lớp, giao diện và kiểu dữ liệu. Ngoài ra còn có **phân lớp hành vi**, tức là chia theo những việc đối tượng có thể làm như: tương tác với hệ thống (tác nhân), cùng làm việc với nhau (cộng tác), ...   

### Lớp
[Lớp](https://www.uml-diagrams.org/class.html) đại diện cho một tập các đối tượng có **chung đặc điểm, hành vi và các quan hệ** với những đối tượng khác. Trong thế giới đời thực, đặc điểm (màu tóc chẳng hạn) được tái hiện bằng các giá trị cụ thể (màu nâu/đen chẳng hạn) gọi là **giá trị thuộc tính**. Còn hành vi (nhuộm tóc) được tái hiện bằng các thao tác cụ thể (chọn màu, thoa thuốc, xả tóc, ...) gọi là **thao tác đối tượng**. Vai trò của lớp là cung cấp các **khai báo thuộc tính** (gồm tên và [[class-object-diagram#Kiểu dữ liệu|kiểu dữ liệu]]) và các **khai báo thao tác** (gồm tên, các tham số và kiểu trả về) cho các đối tượng đó.

> [!example]- Ví dụ
> Lớp `Hair` cung cấp:
> - **Các khai báo thuộc tính**: `color: Color`, `length: Number`, `style: Text`, ...   
> - **Các khai báo thao tác**: `dyeHair(color: Color)`,  `cutHair(lengthToCut: Number) -> Number`, ...

Ngoài ra, trạng thái của một đối tượng được mô tả bởi **các thuộc tính và các liên kết** với đối tượng khác. Trong khi hành vi của đối tượng đó được mô tả bởi **các thao tác** mà hiện thực hóa của chúng là các **phương thức** của một lớp.  

> [!info] Lưu ý
> - **Thao tác**: mô tả hành vi ở mức mô hình (thiết kế). *Ví dụ*: lớp `Bicycle` có thao tác `changeGear(newValue)`, nghĩa là xe đạp có khả năng đổi số.
> - **Phương thức**: hiện thực hóa hành vi bằng mã nguồn (cài đặt). *Ví dụ*: Trong Java, phương thức `void changeGear(int newValue) { gear = newValue; }` chính là hiện thực hóa cho thao tác `changeGear`.

### Giao diện
[Giao diện](https://www.uml-diagrams.org/interface.html) là sự **mô tả vẻ ngoài** của các đối tượng bằng cách liệt kê các **mô tả thao tác** mà **không đề cập đến phần triển khai** bên trong chúng. Giao diện có thể được hiện thực hóa bởi một hay nhiều lớp. Những lớp này sẽ triển khai các thao tác dựa trên mô tả mà giao diện đã cung cấp.

> [!example]- Ví dụ
> Giao diện `IPaymentGateway` cung cấp các mô tả thao tác sau:
> - Xác thực giao dịch: `authorizePayment(amount: Number) -> Logic (success/fail)`
> - Thực hiện thanh toán: `capturePayment(amount: Number) -> Logic`:  
> - Hoàn tiền: `refundPayment(amount: Number) -> Logic`: 
> - Lấy trạng thái giao dịch`getTransactionStatus(transactionId: Text) -> Text`

### Kiểu dữ liệu
[Kiểu dữ liệu](https://www.uml-diagrams.org/data-type.html) là sự **mô tả các giá trị** đối tượng thực sự chứa trong đời thực như: số nguyên, số thực, văn bản, ký tự, ... Không có cách nào định danh được chúng vì một số vừa có thể là số nguyên, số thực hay văn bản, ... (số 5 chẳng hạn), nên chúng **không có thuộc tính** (thứ vốn để định danh) và thường được gọi là **kiểu dữ liệu nguyên thủy** trong kỹ thuật phần mềm. Dù vậy, chúng vẫn có thể có thao tác (như cộng trừ nhân chia giữa các số) và các thao tác này chỉ trả về giá trị mới chứ không sửa đổi giá trị của đối tượng tham gia thao tác.  

Mặt khác, những kiểu dữ liệu do người dùng **sáng tạo** ra (còn gọi là kiểu tự định nghĩa/kiểu dữ liệu có cấu trúc) sẽ mất đi tính nguyên thủy do chúng **chứa đựng các thuộc tính** (có thể bao gồm thuộc tính có kiểu dữ liệu nguyên thủy hoặc không). Điều này cho phép các thao tác trên đối tượng **có thể sửa đổi giá trị** của đối tượng tham gia. *Ví dụ*: Shiba là một giống chó nên có thể coi Chó là một kiểu dữ liệu gồm các thuộc tính màu, số chân, ... Trong khi Shiba hay bất kỳ cái tên nào khác như Husky, Chihuahua, ... là các giá trị xuất hiện trong đời thực của kiểu dữ liệu này.

> [!example]- Ví dụ
> Trong lập trình Java, dữ liệu có thể được chia thành:
> - **Kiểu nguyên thủy**: int (số nguyên), double (số thực), char (ký tự), boolean (đúng/sai), ...
> - **Kiểu tự định nghĩa**: Array (Mảng các phần tử), Point2D (tọa độ Đề-các), Date (ngày giờ), ...  

### Cấp độ ngữ nghĩa
Trong mô hình UML, các lớp có thể tồn tại ở nhiều cấp độ ngữ nghĩa khác nhau như:
- **Phân tích**: phản ánh các lớp ở mức độ **trừu tượng**, tái hiện một cách cơ bản về hệ thống để phản ánh **đủ logic cốt lõi mà bỏ qua các chi tiết cài đặt**. Lớp ở cấp độ này thường được trình bày bằng văn bản mô tả ý nghĩa các khái niệm. 
- **Thiết kế**: tái hiện các quyết định tổ chức **gom nhóm thông tin vào thao tác** vào một đơn vị cấu trúc rời rạc như lớp chẳng hạn. Lớp ở cấp độ này đã có khung thiết kế chứa đầy đủ thuộc tính và phương thức được biểu diễn trong biểu đồ lớp
- **Cài đặt**: các lớp ở cấp độ này có thể được **ánh xạ trực tiếp vào mã nguồn** của ngôn ngữ lập trình. Lớp ở cấp độ này chính là code cụ thể được viết ra dựa trên khung thiết kế trước đó.

### Quan hệ giữa các phân lớp

|                                 Quan hệ                                 | Mô tả                                                                                                                                                                                                                                     | Ký hiệu                                                                                                                                                  | Ví dụ                                                                                                                            |
| :---------------------------------------------------------------------: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
|        [Kết hợp](https://www.uml-diagrams.org/association.html)         | kiểu quan hệ cho biết một lớp **có liên quan** đến lớp khác và có thể chứa các **thuộc tính quan hệ** được đại diện bởi một lớp kết hợp. Nó còn có 2 dạng kết hợp đặc biệt là [[unified-modeling-language#^3cb783\|tập hợp và hợp thành]] | Đường nét liền nối giữa 2 lớp, có thể có nhãn, vai trò, bội số, ... Hình thoi rỗng được thêm ở đầu lớp toàn thể đối với tập hợp và đặc đối với hợp thành | Một `Student` có thể học nhiều `Subject`, một `Subject` có thể có nhiều `Student` → quan hệ kết hợp giữa `Student` và `Subject`  |
|    [Tổng quát hóa](https://www.uml-diagrams.org/generalization.html)    | kiểu quan hệ **khái quát** những **lớp cụ thể** (lớp con) thành một **lớp trừu tượng** (lớp cha), trong đó các đối tượng của lớp cụ thể có thể được thay thế bằng đối tượng của lớp trừu tượng                                            | Mũi tên rỗng, hướng từ lớp con đến lớp cha.                                                                                                              | Giống Kế thừa, nhưng ta hiểu là khái quát `Student` và `Teacher` thành `Human`                                                   |
| [Kế thừa](https://www.uml-diagrams.org/generalization.html#inheritance) | kiểu quan hệ **cha - con**, cho phép lớp con kết hợp thông tin của chính nó với thông tin được **kế thừa** từ lớp cha. Khi một lớp kế thừa từ nhiều lớp → đa kế thừa                                                                      | Giống Tổng quát hóa                                                                                                                                      | Lớp `Student` và `Teacher` đều có các thuộc tính chung từ lớp `Human` (tên, tuổi, địa chỉ) và có thể mở rộng thêm hành vi riêng. |
|     [Hiện thực hóa](https://www.uml-diagrams.org/realization.html)      | kiểu quan hệ **triển khai/thực thi hợp đồng** giữa phân lớp triển khai và phân lớp cung cấp hợp đồng, thường là giữa giao diện và thành phần thực thi hay giữa ca sử dụng và cộng tác hiện thực hóa chúng.                                | Đường nét đứt với mũi tên rỗng, từ phân lớp triển khai đến phân lớp cung cấp hợp đồng.                                                                   | Lớp `payByCard` và `payByCash` cài đặt các phương thức đã được mô tả trong giao diện `IPayment`                                  |
|        [Phụ thuộc](https://www.uml-diagrams.org/dependency.html)        | thể hiện rằng sự thay đổi của một phân lớp (phần tử độc lập) **có thể ảnh hưởng** đến phân lớp khác (phần tử phụ thuộc). Để phân biệt các loại phụ thuộc, ta dùng các nhãn stereotype như: access, use, call, send, ...                   | Mũi tên nét đứt từ phần tử phụ thuộc đến lớp phần tử độc lập                                                                                             | `SignupInterface` phụ thuộc `SignupSystem` vì các thay đổi trong hệ thống đăng ký có thể ảnh hưởng đến giao diện hiển thị        |

> [!info] Lưu ý
> Về mặt biểu diễn, quan hệ tổng quát hóa trùng với quan hệ kế thừa. Chúng khác nhau ở hướng xem xét quan hệ: kế thừa nhìn từ **trên xuống**, tổng quát hóa nhìn từ **dưới lên**. 

## Biểu đồ đối tượng 📷

**Biểu đồ đối tượng** là một **ảnh chụp tức thời** của biểu đồ lớp ở một trạng thái cụ thể. Nếu biểu đồ lớp mô tả *"những gì xảy ra theo lý thuyết"* thì biểu đồ đối tượng chính là *"những gì diễn ra trong thực tế"*, tức bao gồm các đối tượng với các giá trị cụ thể tại một thời điểm.

> [!example]- Ví dụ
> - Biểu đồ lớp có lớp `Student` gồm thuộc tính `name`, `age` và `id`
> - Biểu đồ đối tượng sẽ có: `student1: Student` gồm `name=Long`, `age=18`, `id=12345678`; `student2`, ... 

## Mục đích của biểu đồ lớp 🎯

### Mô hình hóa những thứ bên trong hệ thống
Là việc xác định các khái niệm, trừu tượng làm nên hệ thống và chỉ ra các phần không thuộc hệ thống. Cũng giống như việc viết một cuốn từ điển chuyên ngành để định nghĩa những thứ (như khái niệm, phương pháp, trách nhiệm, ...) bên trong chuyên ngành đó.

### Mô hình hóa các cộng tác đơn giản

Cách làm:
1. **Xác định cơ chế cần mô hình hóa**: Nghĩ xem hệ thống có những chức năng/hành vi nào, ví dụ: "Người dùng đăng nhập", "Sinh viên đăng ký môn học".
2. **Xác định các lớp và giao diện liên quan**: Tìm ra những đối tượng nào tham gia vào chức năng đó, ví dụ: `User`, `LoginForm`, `Database`. Nếu có giao diện thì liệt kê luôn, ví dụ: `IAuthenticatable`.
3. **Xác định quan hệ giữa chúng**: Vẽ mối liên kết để thể hiện lớp nào gọi lớp nào, lớp nào kế thừa lớp nào, lớp nào thực thi giao diện nào, ...
4. **Dùng kịch bản ca sử dụng để kiểm tra**: Giả sử một tình huống cụ thể, ví dụ: người dùng nhập mật khẩu sai → duyệt qua các đối tượng để xem chúng có đủ hành vi chưa, thiếu gì không.
5. **Phân bổ trách nhiệm cho lớp**: Gán cho mỗi lớp nhiệm vụ rõ ràng (ví dụ: `User` lưu thông tin, `LoginForm` kiểm tra dữ liệu nhập, `Database` xác thực. Bổ sung dần các thuộc tính và phương thức cần thiết.

### Mô hình hóa lược đồ cơ sở dữ liệu
[Lược đồ cơ sở dữ liệu](https://en.wikipedia.org/wiki/Database_schema) giống như **bản thiết kế** cho một cơ sở dữ liệu sẽ được xây dựng trong đời thực. Nó cho ta biết trong hệ thống sẽ có những bảng hoặc đối tượng nào, mỗi bảng có cột gì, và chúng liên kết với nhau ra sao.

Khi muốn lưu trữ thông tin lâu dài, ta có thể chọn dùng **cơ sở dữ liệu quan hệ** (dùng bảng, hàng, cột) hoặc **cơ sở dữ liệu hướng đối tượng** (dùng đối tượng và quan hệ giữa chúng).

Để mô tả những bản thiết kế này, ta có thể dùng **biểu đồ lớp UML**, vì nó cho phép biểu diễn các bảng, đối tượng, thuộc tính và mối quan hệ một cách trực quan.

## Tóm lại 🔥

Biểu đồ lớp là *trái tim vạn năng* của UML, giúp mô hình hóa phần *"xương sống"* của hệ thống. Nó cho ta thấy rõ những ai tham gia, quan hệ thế nào, tồn tại ra sao trong hệ thống.