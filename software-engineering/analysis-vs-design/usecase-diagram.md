---
stage: Publish
draft: false
title: Biểu đồ ca sử dụng
description:
tags:
  - analysis-and-design
  - usecase-diagram
  - modeling-language
socialDescription:
socialImage:
permalink:
lang: vi
aliases:
cssclasses:
  - img
---
## Tổng quan 🔭

**Biểu đồ ca sử dụng** được dùng để mô hình hóa các **khía cạnh động** của hệ thống, tức là cách hệ thống vận hành trong thực tế. Nó cung cấp **khung nhìn từ bên ngoài**, cho thấy:

- Hệ thống sẽ được sử dụng như thế nào trong bối cảnh thực tế.
- Ai (tác nhân) sẽ tương tác với hệ thống.
- Họ tương tác thông qua những chức năng (ca sử dụng) nào.

👉 Biểu đồ ca sử dụng giúp trả lời câu hỏi *"Người dùng sẽ làm gì với hệ thống?"*

## Bên trong biểu đồ ca sử dụng 🔬

### Tác nhân
Đại diện cho **vai trò** của một người, thiết bị, hay bất kể đối tượng nào tương tác với hệ thống. Nó làm rõ các tương tác mà một tập đối tượng có thể có với hệ thống.  

Trong biểu đồ, [tác nhân](https://www.uml-diagrams.org/use-case-actor.html) được biểu diễn bởi hình người que (stick man) kèm tên vai trò bên dưới.

> [!example]- Ví dụ
> **Sinh viên** là vai trò của nhiều người theo học đại học, nên nó được coi là tác nhân đại diện cho họ để tương tác với các hệ thống nhà trường.

Một số đặc điểm của tác nhân:
- Cùng một tác nhân có thể đại diện cho nhiều đối tượng cụ thể khác nhau (như ví dụ trên)
- Một đối tượng cụ thể cũng có thể tham gia một hay nhiều tác nhân của hệ thống (một người trong trường vừa là sinh viên vừa là trợ giảng)
- Một tác nhân tham gia vào một hay nhiều ca sử dụng (sinh viên có thể học, thi, ...)
- Tác nhân tương tác với hệ thống bằng cách trao đổi các thông điệp (sinh viên nộp học phí vào hệ thống tài chính nhà trường, học phí ở đây chính là thông điệp)

### Ca sử dụng
Đại diện cho **một chức năng cụ thể** mà hệ thống cung cấp cho tác nhân. Nó mô tả **chuỗi các tương tác** (thông điệp) giữa hệ thống và tác nhân để đạt được một mục tiêu có ý nghĩa. Khi mô tả một ca sử dụng, cần nêu rõ:
- **Chuỗi kịch bản chính**: cách thông thường mà hệ thống làm việc với tác nhân
- **Các luồng thay thế**: những tình huống khác có thể xảy ra mà hệ thống xử lý được
- **Các điều kiện ngoại lệ**: những sự cố bất ngờ khiến hệ thống hoạt động không như mong đợi

Trong biểu đồ, [ca sử dụng](https://www.uml-diagrams.org/use-case.html) được biểu diễn bằng một hình elip kèm tên của nó bên trong 

> [!example]- Ví dụ
> **Một hệ thống chấm thi** có thể cung cấp các chức năng như: Đăng nhập, Quản lý bảng điểm, Chấm điểm, Tra cứu điểm, ... Đối với chức năng **Đăng nhập**, ta có thể mô tả nó như sau:
> - **Kịch bản chính**: nhập tên đăng nhập và mật khẩu → hệ thống kiểm tra thông tin → đúng thì cho phép truy cập.
> - **Luồng thay thế**: người dùng chọn đăng nhập bằng phương thức khác (Google, Microsoft, ...)
> - **Ngoại lệ**: Nhập sai mật khẩu quá 3 lần → hệ thống khóa tạm thời và yêu cầu đổi mật khẩu (không cho đăng nhập = không như mong đợi)

### Quan hệ trong biểu đồ ca sử dụng
Biểu đồ ca sử dụng không chỉ có tác nhân và ca sử dụng, mà còn thể hiện **các quan hệ** giữa chúng:
- [Giao tiếp](https://www.uml-diagrams.org/use-case-actor-association.html) (Association): đường nét liền nối giữa tác nhân và ca sử dụng (nếu là giao tiếp một chiều thì đường này có thêm mũi tên).
- [Bao gộp](https://www.uml-diagrams.org/use-case-include.html) (Include): một ca sử dụng luôn bao gồm hành vi của ca sử dụng khác, được biểu diễn bởi đường nét đứt với nhãn `<<include>>` và mũi tên hướng về ca được bao gộp
- [Mở rộng](https://www.uml-diagrams.org/use-case-extend.html) (Extend): một ca sử dụng có thể được mở rộng thêm hành vi bởi ca sử dụng khác, được biểu diễn bằng đường nét đứt với nhãn `<<extend>>` và mũi tên hướng với ca được mở rộng
- [Kế thừa](https://www.uml-diagrams.org/use-case.html#generalization) (Generalization): Khi các tác nhân/ca sử dụng có chung đặc điểm, chúng sẽ kế thừa từ một tác nhân/ca sử dụng nào đó mang đặc điểm chung đó, được biểu diễn bởi đương nét liền với mũi tên rỗng hướng về cái mang đặc điểm chung. 

> [!example]- Ví dụ
> Trong một hệ thống nhà hàng:
> - **Quan hệ giao tiếp**: khách hàng **gọi món**, bếp trưởng **nấu ăn**, nhân viên **giao món**.
> - **Quan hệ bao gộp**: **Gọi món** luôn bao gồm **chọn món từ menu**.
> - **Quan hệ mở rộng**: **Thanh toán** có thể mở rộng thêm hành vi **nhập mã giảm giá**.

👉 Nhờ các quan hệ này, biểu đồ ca sử dụng giúp **giảm trùng lặp** và **tổ chức lại chức năng** của hệ thống một cách hợp lý hơn.

## Mục đích của biểu đồ ca sử dụng 🎯
### Mô hình hóa khung cảnh hệ thống
Giúp xác định cái gì nằm trong và ngoài hệ thống (biên hệ thống). Cách làm:

1. Xác định các tác nhân tương tác với hệ thống: 
	- Nhóm tác nhân cần được hệ thống trợ giúp để làm việc.
	- Nhóm tác nhân cần thiết để hệ thống vận hành
	- Các hệ thống/phần cứng khác liên quan.
	- Các nhóm quản trị, bảo trì.
2. Tổ chức các tác nhân thành quan hệ **kế thừa** khi chúng có nhiều điểm tương đồng.
3. Dùng kiểu mở rộng (stereotype) để chú thích thêm cho tác nhân. Ví dụ: `<<external system>>`.
4. Lắp ghép các tác nhân với các ca sử dụng mà chúng tham gia.

> [!example]- Ví dụ
> Một hệ thống ATM có thể gồm các tác nhân (nằm ngoài hệ thống): **Khách hàng**, **Ngân hàng trung tâm**, **Bộ phận bảo trì**. Ca sử dụng (nằm trong hệ thống) có thể là: **Rút tiền**, **Xem số dư**, **Nạp tiền**, **Bảo trì ATM**.

### Mô hình hóa yêu cầu của hệ thống 
Giúp làm rõ **những gì** hệ thống sẽ làm mà không quan tâm chúng được thực hiện **ra sao**. Cách làm:

1. Xác định các tác nhân của hệ thống
2. Xem xét hành vi mà từng tác nhân yêu cầu
3. Xem xét cách hệ thống đáp ứng từng hành vi và chuyển các hành vi chung thành các ca sử dụng tương ứng
4. Tạo ra các ca sử dụng mới cung cấp hành vi chung cho các ca sử dụng khác bằng quan hệ bao gộp. Mở rộng các ca sử dụng với luồng thay thế bằng quan hệ mở rộng
5. Lặp ghép thành biểu đồ ca sử dụng
6. Thêm các chú thích cho ca sử dụng (nếu cần)

> [!example]- Ví dụ
> Trong ứng dụng thương mại điện tử, yêu cầu "Khách hàng có thể mua sản phẩm online" có thể triển khai thành các ca sử dụng: **Đăng nhập**, **Xem sản phẩm**, **Thêm vào giỏ hàng**, **Thanh toán**. Trong đó, ca sử dụng **Thanh toán** có thể **include** ca sử dụng **Xác thực giao dịch**.

> [!info] Lưu ý
> - Mỗi ca sử dụng chính là **một yêu cầu hệ thống về chức năng**.
> - Yêu cầu hệ thống có thể được diễn đạt theo nhiều cách khác nhau, từ diễn đạt mơ hồ trong các kiểu giao tiếp phi hình thức (gọi điện, nhắn tin, cafe, ...) cho đến diễn đạt chính xác cao trong các giao tiếp chính thức (hợp đồng, họp nhóm, ...) 

## Tóm lại 🔥
**Biểu đồ ca sử dụng** giúp ta nhìn hệ thống từ **bên ngoài vào**, mô tả cách hệ thống được sử dụng bởi các **tác nhân**. Thành phần chính của nó gồm tác nhân, ca sử dụng và quan hệ. Được dùng để xác định **khung cảnh hệ thống** và tổ chức các **yêu cầu chức năng** trong hệ thống.
