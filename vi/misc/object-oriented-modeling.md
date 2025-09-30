---
stage: Publish
draft: false
title: Mô hình hóa hướng đối tượng
description:
tags:
  - OOAD
  - OOM
  - object-oriented
  - models
socialDescription:
socialImage:
permalink:
lang: vi
aliases:
cssclasses:
---
Có bao giờ bạn tự hỏi: _Tại sao phần mềm ngày càng phức tạp mà con người vẫn kiểm soát được nó?_ 🤔 Câu trả lời nằm ở cách chúng ta “nhìn” vào vấn đề. Ngày xưa, lập trình viên thường tư duy theo kiểu **thủ tục** (procedural programming): viết ra từng hàm, từng chức năng, xếp nối với nhau. Nhưng càng đi sâu, cách này càng “đuối sức” khi hệ thống phình to.

👉 Và rồi, **hướng đối tượng (Object-Oriented Programming – OOP)** ra đời, mang theo một triết lý mới:

> _Đừng chỉ nhìn vào “công việc cần làm”, hãy nhìn vào “ai” thực hiện công việc đó._

Nói cách khác, thay vì xoay quanh _hàm_, ta xoay quanh _đối tượng_ – chính là những thực thể trong thế giới thực, với đặc điểm (thuộc tính) và hành vi (phương thức).

## Nguyên tắc cơ bản của hướng đối tượng 🌟

%% mermaid code for image %%

Đây chính là “tứ trụ” – 4 nguyên tắc vàng mà bạn sẽ gặp đi gặp lại trong mọi ngôn ngữ OOP:
1. **Trừu tượng hóa (Abstraction)** 🪄  
    Hãy tưởng tượng bạn mô tả một chiếc xe hơi. Bạn đâu cần liệt kê _từng con ốc_, chỉ cần biết xe có bánh, động cơ, vô-lăng… đủ để phân biệt với cái xe đạp. Đó là **trừu tượng hóa**: tập trung vào đặc điểm quan trọng, bỏ qua chi tiết vụn vặt.  
    → Trong code: bạn tạo ra lớp `Car` thay vì liệt kê chi tiết từng bộ phận vật lý.

2. **Đóng gói (Encapsulation)** 📦  
    Đối tượng giống như một “hộp kín”. Bạn có thể bấm nút khởi động xe, nhưng không cần (và cũng không nên) chọc vào hệ thống điện bên trong.  
    → Trong code: các thuộc tính `private` được che giấu, chỉ lộ ra qua `getter/setter`.

3. **Mô-đun hóa (Modularity)** 🧩  
    Hãy chia hệ thống thành nhiều phần độc lập, dễ thay đổi mà không làm hỏng toàn bộ. Giống như xây nhà bằng Lego – thay một khối không ảnh hưởng cả ngôi nhà.

4. **Phân cấp (Hierarchy)** 🌳  
    Đây là “gia phả” trong lập trình. Một lớp `Dog` có thể **kế thừa** từ `Animal`, và mọi con chó đều có “hành vi chung” của động vật, nhưng cũng có đặc điểm riêng (sủa, trung thành).

## Khái niệm cơ bản trong mô hình hướng đối tượng 🧱

Sau khi nắm nguyên tắc, ta đi vào "từ vựng" của thế giới OOP:
- **Đối tượng (Object)** 🟢: Thực thể cụ thể. Ví dụ: _Chiếc xe Toyota Camry màu đen của bạn_.

- **Lớp (Class)** 🏗: Khuôn mẫu để tạo đối tượng. Ví dụ: `Car` là lớp, từ đó sinh ra nhiều đối tượng Camry, Civic, Mercedes…

- **Kế thừa (Inheritance)** 👨‍👩‍👧: Cho phép lớp con dùng lại và mở rộng đặc tính lớp cha.

- **Đa hình (Polymorphism)** 🎭: Một hành động nhưng nhiều cách thể hiện. Ví dụ: cùng là phương thức `draw()`, nhưng với `Circle` thì vẽ hình tròn, với `Square` thì vẽ hình vuông.

> [!question] Vì sao phải mô hình hóa đối tượng?
> Thay vì ngập trong mớ hàm lộn xộn, ta có:
> - Mô hình trực quan hơn (gần với thế giới thực 🌍).
> - Dễ bảo trì, dễ mở rộng.
> - Giúp phần mềm sống khỏe trong nhiều năm, thay đổi mà không sụp đổ.

## Lời kết ✍️

Bài viết này giống như "bản khai sinh" của một phong cách tư duy mới trong lập trình. Nếu coi việc phát triển phần mềm là xây một thành phố, thì **mô hình hóa đối tượng chính là bản đồ quy hoạch** 🏙. Không có nó, mọi công trình sẽ sớm hỗn loạn.

👉 Ở bài viết sau, mình sẽ cùng bạn khám phá **UML** – ngôn ngữ chung để vẽ bản đồ đối tượng. Tin mình đi, nó giống như học đọc bản vẽ thiết kế nhà vậy, cực kỳ trực quan và thú vị!