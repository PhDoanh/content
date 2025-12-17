---
stage: Publish
draft: false
title: OCL - Ngôn ngữ ràng buộc cho mô hình hướng đối tượng
description:
tags:
  - analysis-and-design
  - modeling-language
  - constraint-language
  - overview
socialDescription:
socialImage:
permalink:
lang:
aliases:
cssclasses:
---
## Giới thiệu về OCL 🔍

Khi phân tích & thiết kế hệ thống hướng đối tượng, chúng ta dùng rất nhiều biểu đồ UML như lớp, ca sử dụng, hoạt động… Nhưng có vài vấn đề:
- Biểu đồ UML thường **chỉ mô tả cấu trúc hoặc hành vi** ở mức khái quát, nhưng **không đủ chi tiết** để diễn tả tất cả các quy tắc nghiệp vụ (business rules).
- Nếu ghi các ràng buộc nghiệp vụ bằng **ngôn ngữ tự nhiên**, rất dễ **mơ hồ**, khó kiểm tra và có thể hiểu sai.

Do đó, OCL ra đời để giúp giảm sự mơ hồ, tăng tính chính xác của mô hình - rất hữu ích trong phân tích, thiết kế và sau này là thực thi hoặc tự động hóa.

Theo Wikipedia, [OCL](https://en.wikipedia.org/wiki/Object_Constraint_Language) là một **ngôn ngữ biểu thức** (expression language) dùng để mô tả các **ràng buộc**[^1] trên các mô hình hướng đối tượng - đặc biệt là với [[unified-modeling-language|UML]] (Unified Modeling Language). Nó có một số đặc điểm sau:

- **Ngôn ngữ biểu thức**: Mỗi biểu thức OCL khi đánh giá sẽ trả về một giá trị mà **không làm thay đổi trạng thái** hệ thống
- **Ngôn ngữ mô hình hóa**: OCL chủ yếu dùng để mô tả mô hình, không dùng để viết logic chương trình phức tạp như loop, thay đổi trạng thái, gọi hàm kích hoạt quá trình.
- **Ngôn ngữ hình thức**: Có ngữ pháp, kiểu dữ liệu rõ ràng, có thể dùng cho việc kiểm tra tính đúng đắn của mô hình.
- **Phụ thuộc vào ngữ cảnh**: Mỗi biểu thức OCL phải xác định rõ `context` (ví dụ lớp nào, phương thức nào) để biết "self" là gì, các thuộc tính nào khả dụng.

> [!info] Lưu ý
> OCL được chuẩn hóa bởi [Object Management Group](https://www.omg.org) (OMG), phiên bản cập nhật gần nhất là [OCL 2.4](https://www.omg.org/spec/OCL/2.4/PDF). 

## Các thành phần cơ bản của OCL 🧩

### Kiểu dữ liệu

OCL có các **kiểu nguyên thủy** (atomic types) như `Integer`, `Real`, `String`, `Boolean`. Nó cũng hỗ trợ các kiểu do người dùng định nghĩa (user-defined types) như class types, enumeration types. Ngoài ra, các **kiểu tập hợp/phức hợp** (template/collection types) như `Set(T)`, `Bag(T)`, `Sequence(T)`, `OrderedSet(T)` và kiểu `Tuple(part1:T1, part2:T2, …)` được dùng để lưu trữ nhiều giá trị trong cùng một đối tượng

Ví dụ:
```ocl
-- kiểu nguyên thủy
context Person inv: self.age >= 0

-- kiểu tập hợp
context CarGroup inv:
  self.cars->size() > 0 and
  self.cars->forAll(c | c.year > 2000)
```

Vai trò: xác định kiểu của biểu thức OCL, đảm bảo tính **typed** (kiểu dữ liệu rõ ràng) trong OCL. 

### Ngữ cảnh và từ khóa `self`

Mỗi biểu thức OCL phải bắt đầu với từ khóa `context` để xác định "ngữ cảnh" mà biểu thức áp dụng - thường là một lớp, một interface hoặc một operation.

Từ khóa `self` đại diện cho **thể hiện hiện tại** (current instance) trong ngữ cảnh đó (giống như `this` trong các ngôn ngữ lập trình).

Ví dụ:
```ocl
context Account
inv: self.balance >= 0
```

Vai trò: xác định rõ "đối tượng nào" đang bị ràng buộc, giúp biểu thức rõ ràng và chính xác.

### Các ràng buộc

OCL hỗ trợ nhiều loại ràng buộc chính trong mô hình hướng đối tượng:
- **Invariant (inv)**: Ràng buộc bất biến - phải luôn đúng cho tất cả các thể hiện của lớp hoặc type trong mọi thời điểm. Ví dụ: `context Person inv: self.age >= 0`

- **Pre-condition (pre)**: Ràng buộc **trước** khi một operation được gọi - điều kiện bắt buộc khi bắt đầu thực thi. Ví dụ: `context Account::withdraw(amount: Real) pre: amount > 0 and self.balance >= amount`

- **Post-condition (post)**: Ràng buộc **sau** khi một operation kết thúc - điều kiện bắt buộc sau khi hoàn thành. Ví dụ: `context Account::withdraw(amount: Real) post: self.balance = self.balance@pre - amount`

- **Initial (init) & Derived (derive)**: 
	- `init` dùng để xác định giá trị khởi tạo của một thuộc tính khi đối tượng được tạo. Ví dụ: `context Customer::premium:Boolean init: false`
    - `derive` dùng để xác định thuộc tính phái sinh (derived attribute) - giá trị được tính từ các thuộc tính khác. Ví dụ: `context Order::totalPrice:Real derive: self.orderLines->collect(ol | ol.linePrice)->sum()`

- **Guard**: Ràng buộc dùng trong biểu đồ trạng thái (state-machines) hoặc chuyển trạng thái (yêu cầu trước khi chuyển trạng thái)

### Truy cập dẫn xuất và thao tác trên tập hợp

- OCL cho phép dẫn xuất giá trị qua các liên kết trong mô hình UML. Ví dụ: `self.orders`, `self.department.manager`… 

- Khi liên kết có multiplicity > 1, OCL sẽ trả về một tập hợp (collection) thay vì một giá trị đơn lẻ. Các thao tác tập hợp (collection operations) rất quan trọng. Ví dụ: 

```
context Company 
inv: self.employees->size() >= 1  

context Person 
inv: self.parents->forAll(p | p.age > self.age)
```

Vai trò: hỗ trợ diễn đạt các điều kiện liên quan đến nhiều đối tượng hoặc tập hợp đối tượng trong mô hình - rất hữu ích khi biểu đồ UML đơn giản không đủ diễn đạt các ràng buộc phức tạp.

### Biểu thức & toán tử

- OCL là **ngôn ngữ biểu thức** (expression language) - nghĩa là bạn viết biểu thức trả về giá trị (Boolean, Integer, Set, …) chứ không viết các lệnh làm thay đổi trạng thái hệ thống
- Các toán tử cơ bản:
    - Trên kiểu số: `+`, `-`, `*`, `/`, `div`, `mod` … 
    - So sánh: `=`, `<>`, `<`, `>`, `<=`, `>=`. 
    - Logic: `and`, `or`, `not`, `implies`.

Ví dụ:
```ocl
context Flight 
inv: self.duration <= 4 and self.maxNrPassengers <= 1000
```

Vai trò: cấu thành *"nội dung"* của ràng buộc và kiểm tra logic nghiệp vụ, biểu thức phải dễ hiểu, đúng kiểu, và không gây thay đổi hệ thống.

## Vai trò của OCL trong phân tích, thiết kế hướng đối tượng 🏗️

Khi bạn đang thực hiện các bước như phân tích ca sử dụng, thiết kế lớp, phân tích kiến trúc… OCL có thể hỗ trợ như sau:

- Trong **phân tích nghiệp vụ**: khi bạn xác định các quy tắc nghiệp vụ (business rules) mà biểu đồ UML không thể biểu diễn rõ bằng hình vẽ, bạn dùng OCL để viết rõ hơn.

- Trong **mô hình hóa lớp**: sử dụng OCL để viết invariant cho lớp (ví dụ: số lượng tối đa - tối thiểu, logic nghiệp vụ giữa các thuộc tính) → giúp bảo đảm mô hình đúng đắn theo nghiệp vụ.

- Trong **thiết kế chi tiết / thực thi**: OCL giúp liên kết thiết kế với code generation hoặc kiểm thử tự động - các ràng buộc có thể được chuyển thành kiểm tra (assertion) hoặc code.

- Trong **kiểm tra chất lượng mô hình**: OCL dùng để xác định well-formedness rules (luật định hình đúng) cho mô hình UML hoặc meta-model.

> [!info] Lưu ý khi dùng OCL
> - **Không thay thế logic chương trình**: OCL không phải để viết thay thế code, không có vòng lặp (loop) hay thay đổi trạng thái
> - **Xác định đúng context**: Khi bạn viết OCL, hãy ghi rõ `context` để xác định rõ nơi ràng buộc gắn vào.
> - **Kiểu dữ liệu đúng & navigation hợp lệ**: Ví dụ `self.attribute->size()` chỉ đúng nếu `attribute` là tập hợp; nếu là đơn giá trị thì dùng `self.attribute`.
> - **Tránh viết quá phức tạp**: OCL rất mạnh nhưng nếu quá rắc rối sẽ khó kiểm tra và bảo trì nên hãy viết rõ, đơn giản, dễ đọc
> - **Kiểm thử & công cụ hỗ trợ**: Có nhiều công cụ hỗ trợ OCL như Eclipse OCL (dành cho môi trường EMF/UML) để parse và đánh giá OCL.
> - **Thiết kế tốt từ đầu**: Việc sử dụng OCL từ sớm (giai đoạn phân tích) giúp đưa các ràng buộc nghiệp vụ vào mô hình, tránh việc *"quên"* hoặc viết sai sau này khi phân tích/thiết kế muộn.

## Tổng kết 🔥

**OCL = ngôn ngữ ràng buộc cho mô hình hướng đối tượng**. Nó giúp bạn từ mô hình UML hình ảnh chuyển sang mô hình có **độ chính xác cao hơn**, rõ ràng hơn và dễ kiểm tra hơn.  

Trong quá trình **phân tích & thiết kế hướng đối tượng**, OCL là một trong những *"công cụ ngôn ngữ"* không thể bỏ qua nếu bạn muốn mô hình của mình không chỉ là *"hình vẽ đẹp"* mà còn phải *"chi tiết và chính xác đến chuyên nghiệp"*.



[^1]: **Ràng buộc (constraint)** là quy tắc hoặc điều kiện hạn chế một hoặc nhiều giá trị trong một phần của mô hình hoặc hệ thống hướng đối tượng; nó đảm bảo mô hình vận hành đúng theo nghiệp vụ và không vi phạm các luật định nghĩa trước.
