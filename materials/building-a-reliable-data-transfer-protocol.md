---
date: 2025-04-02
draft: true
status: Doing
title: Xây dựng một giao thức truyền dữ liệu đáng tin cậy
description: ""
author: PhDoanh
authorlink: https://github.com/PhDoanh
tags:
  - computer-networking
  - transport-layer
  - tcp
  - reliable-data
  - dtp-principles
  - dtp-building
aliases:
  - principles of reliable data transfer
cssclasses:
  - img
  - btn
---
%% LƯU Ý 
- Định dạng tên file: "tên-bài-viết" (jp-typing-guide, ...) 
%%

%% banner
<figure style="text-align: center; margin: 20px auto;">
  <img 
    src="images/principles-of-reliable-data-transfer.png"
    alt="Các nguyên lý của Truyền dữ liệu tin cậy" 
    style="
      width: 90%;
      height: auto;
      display: block;
      margin: 0 auto;
      border-radius: 8px;
      box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    "
  >
  <figcaption style="
    font-style: italic;
    color: #666;
    margin-top: 10px;
    font-size: 1em;
    padding: 0 10px;
  ">
    <em>caption</em>
  </figcaption>
</figure>
 %%

Trong thế giới mạng máy tính, việc đảm bảo **dữ liệu đến nơi một cách chính xác và đầy đủ** là một trong những thách thức quan trọng nhất. Không chỉ xảy ra ở tầng vận chuyển (transport layer), mà nhu cầu truyền dữ liệu tin cậy còn xuất hiện ở tầng liên kết dữ liệu (link layer) và thậm chí là tầng ứng dụng.

🎯 Vấn đề truyền dữ liệu tin cậy (reliable data transfer - RDT) không chỉ là một tính năng, mà là **nền móng quan trọng hàng đầu** trong lĩnh vực mạng. Nếu phải xếp hạng “Top 10 vấn đề cốt lõi trong ngành mạng”, thì **đảm bảo truyền dữ liệu tin cậy** chắc chắn góp mặt!

# Dịch vụ mà RDT cung cấp

Một **kênh truyền tin cậy (reliable channel)** có nghĩa là:
- Không mất gói (no loss) 📦
- Không bị lỗi dữ liệu (no corruption) 🔧
- Nhận dữ liệu đúng thứ tự đã gửi (in-order delivery) 📑

Đây chính là những gì **TCP** (một thể hiện của RDT) cung cấp cho các ứng dụng trên Internet ngày nay.

> [!question]- TCP là gì?
> - Transmission Control Protocol – một giao thức tầng vận chuyển trong mô hình TCP/IP.
> - Cung cấp cơ chế truyền dữ liệu tin cậy, kiểm soát lỗi, và kiểm soát luồng.

---

# 🛠️ Làm thế nào để hiện thực hoá một giao thức RDT?

Câu hỏi lớn đặt ra: **Làm sao để xây dựng một giao thức truyền dữ liệu tin cậy**, trong khi tầng bên dưới (như IP) lại **có thể không tin cậy**?

**Thách thức thực tế**:
- Các tầng dưới như IP có thể mất gói, hư gói hoặc làm trễ gói.
- Nhưng tầng trên vẫn phải đảm bảo rằng dữ liệu **đến nơi đúng cách**.

Vì vậy, giao thức RDT cần **tự xử lý vấn đề** bằng cách:
- Phát hiện lỗi 🔍
- Gửi lại gói tin bị lỗi 🔁
- Quản lý thứ tự gói tin 📬

---

# 📌 Mô hình lập trình cơ bản của RDT

Hãy tưởng tượng bạn là người lập trình giao thức truyền dữ liệu tin cậy. Bạn cần xây dựng 2 phía: **gửi (sender)** và **nhận (receiver)**. Dưới đây là các hàm cơ bản trong mô hình:

**Phía gửi**: `rdt_send(data)` – Được gọi khi ứng dụng muốn gửi dữ liệu.
**Phía nhận**:
- `rdt_rcv(packet)` – Được gọi khi có gói tin đến từ phía gửi.
- `deliver_data(data)` – Đưa dữ liệu hợp lệ lên cho ứng dụng.

**Dưới tầng RDT**:
- `udt_send(packet)` – Gửi một gói tin qua kênh không tin cậy (unreliable data transfer).

> [!info] Lưu ý
> - `rdt_`: Viết tắt của Reliable Data Transfer
> - `udt_`: Viết tắt của Unreliable Data Transfer

---

# 🔄 Truyền dữ liệu một chiều nhưng giao tiếp hai chiều

Dù chúng ta đang xét **truyền dữ liệu một chiều** (từ sender đến receiver), nhưng thực tế cả hai bên **đều cần gửi gói tin cho nhau**.

- Phía nhận cần gửi **gói xác nhận (ACK)** trở lại cho phía gửi.
- Phía gửi có thể cần gửi lại gói tin nếu không nhận được ACK.

> [!example]- Ví dụ
> - Bạn gửi một tin nhắn qua Zalo.
> - Nếu người nhận đọc được, Zalo hiển thị dấu "đã nhận".
> - Nếu không, bạn có thể phải gửi lại – hệ thống sẽ tự làm điều đó cho bạn!

---

# 📦 RDT 1.0 - Giao thức trên Kênh truyền lý tưởng

Trong phần này, chúng ta sẽ khám phá **rdt1.0**, phiên bản đơn giản nhất của giao thức truyền dữ liệu tin cậy (_Reliable Data Transfer protocol_). Đây là bước đầu tiên để hiểu cách các thiết bị trong mạng máy tính giao tiếp **mà không lo mất mát hay lỗi dữ liệu**.

Với **rdt1.0**, ta đặt giả định rằng kênh truyền là **hoàn toàn đáng tin cậy**. Có nghĩa là:
- Không có bit nào bị lỗi trong quá trình truyền.
- Không có gói tin nào bị mất.
- Gói tin được truyền theo đúng thứ tự.

> [!info]- Tại sao lại có rdt1.0?
> - Để tạo nền tảng vững chắc trước khi bước vào các phiên bản phức tạp hơn.
> - Giúp ta hiểu được luồng xử lý cơ bản giữa bên gửi và bên nhận.

## 🧠 Mô hình máy trạng thái hữu hạn (FSM)

Giao thức được biểu diễn bằng **mô hình máy trạng thái hữu hạn** (_Finite-State Machine – FSM_) với:
- **Một FSM cho bên gửi** 📤
- **Một FSM cho bên nhận** 📥

Ở phiên bản rdt1.0, cả hai FSM **chỉ có đúng một trạng thái duy nhất**, vì không có gì sai sót xảy ra cả.

## 🚀 Cách hoạt động của rdt1.0

![[Pasted image 20250406154206.png|center|500]]

**Bên gửi (Sender)**:
- Nhận dữ liệu từ tầng ứng dụng thông qua sự kiện `rdt_send(data)`
- Tạo gói tin với hành động `make_pkt(data)`
- Gửi gói tin qua kênh truyền

**Bên nhận (Receiver):**
- Nhận gói tin từ kênh truyền qua sự kiện `rdt_rcv(packet)`
- Trích xuất dữ liệu từ gói tin bằng `extract(packet, data)`
- Gửi dữ liệu lên tầng ứng dụng thông qua `deliver_data(data)`

> [!info] Lưu ý
> - Dữ liệu chỉ **chảy một chiều** từ người gửi đến người nhận.
> - **Không cần xác nhận hay kiểm tra lỗi** – vì kênh là hoàn hảo!
> - **Không cần điều chỉnh tốc độ gửi**, vì ta giả định rằng người nhận luôn xử lý kịp

---

# 📡 RDT 2.0 - Truyền dữ liệu tin cậy qua kênh có lỗi bit

Trong thực tế, không phải gói tin nào khi được gửi đi cũng đến nơi một cách hoàn hảo. Bit lỗi có thể xảy ra do nhiễu, tín hiệu yếu hoặc các vấn đề vật lý trong quá trình truyền qua mạng. Nhưng thay vì từ bỏ, ta xây dựng các giao thức giúp _truyền dữ liệu tin cậy_ bất chấp những lỗi như thế. Một trong những bước tiến đầu tiên là **rdt2.0**.

Hãy tưởng tượng bạn đang đọc một đoạn tin nhắn dài cho bạn mình qua điện thoại. Sau mỗi câu, người đó sẽ trả lời:

- "OK" nếu họ nghe và ghi lại đúng.
- "Lặp lại câu đó đi" nếu câu bị nghe nhầm hay không rõ.

Đây chính là cơ chế **ACK (Acknowledgment)** và **NAK (Negative Acknowledgment)** trong mạng máy tính! Tức là:

- Người nói = Sender (bên gửi)
- Người ghi = Receiver (bên nhận)
- "OK" = ACK → Gửi thành công
- "Lặp lại đi" = NAK → Gửi lại

## 🧠 Ý tưởng chính của RDT 2.0

![[Pasted image 20250406160142.png|center|500]]

Giao thức **rdt2.0** được thiết kế để xử lý tình huống gói tin bị lỗi bit trong quá trình truyền. Về cơ bản, nó cần 3 thành phần quan trọng:

1. 🧪 **Phát hiện lỗi (Error Detection)**
- Dùng kỹ thuật như **checksum** để kiểm tra xem gói tin có bị lỗi hay không.
- Nếu checksum không khớp → báo lỗi.

> [!info]- Lưu ý
> - UDP cũng dùng checksum để kiểm tra lỗi, nhưng không đảm bảo tin cậy như rdt2.0.
> - Lúc gửi, phải thêm một vài bit dư vào gói để tính toán checksum.

2. 📨 **Phản hồi từ phía người nhận (Receiver Feedback)**
- Gửi lại thông báo **ACK** nếu nhận đúng.
- Gửi lại thông báo **NAK** nếu gói tin bị lỗi.

> [!tip]- Mẹo 
> - ACK = "Ngon lành"
> - NAK = "Hư rồi, gửi lại đi!"

3. 🔁 **Gửi lại khi cần thiết (Retransmission)**
- Nếu nhận được NAK → Gửi lại gói tin vừa rồi.
- Nếu nhận được ACK → Gửi gói tiếp theo.

> [!info] Lưu ý
> RDT 2.0 là dạng giao thức **dừng-và-chờ**: Sau khi gửi một gói, sender sẽ _ngồi đợi_ đến khi nhận được ACK hoặc NAK mới tiếp tục gửi tiếp. Trong lúc đang đợi ACK/NAK, bên gửi **không** gửi thêm dữ liệu mới!

## Nếu gói ACK hoặc NAK bị lỗi thì sao?

Đây là điểm yếu **chết người** của rdt2.0:  Nếu gói ACK hoặc NAK bị lỗi bit, sender **không biết** là gói trước đã được nhận đúng hay chưa!

**🛠️ Các cách xử lý lỗi phản hồi**

**Cách 1: Hỏi lại**
- Sender gửi gói kiểu "Bạn vừa nói gì?"
- Nhưng nếu cả gói hỏi lại cũng bị lỗi thì lặp vô hạn 😵

**Cách 2: Sửa lỗi luôn tại chỗ**
- Dùng kỹ thuật mạnh hơn checksum, như mã sửa lỗi (error-correcting code).
- Phức tạp nhưng khá hiệu quả nếu **chỉ có lỗi bit chứ không mất gói**.

**Cách 3: Gửi lại khi nghi ngờ**
- Nếu phản hồi bị lỗi → Gửi lại luôn gói trước đó
- Nhưng sẽ gây **trùng lặp gói**.

**Giải pháp chuẩn**: Đánh số gói tin (Sequence Number)
Giải quyết chuyện trùng lặp bằng cách **đánh số từng gói tin** (vd: 0, 1, 0, 1,... theo kiểu modulo-2).

Bên nhận chỉ cần:
- Nhớ số thứ tự gói cuối đã nhận đúng.
- So với gói mới nhận → Nếu trùng thì là **bản sao**, bỏ qua.
- Nếu khác → Là gói **mới**, xử lý tiếp.

> [!info]- Lưu ý
> - Sequence number chỉ cần 1 bit (0 hoặc 1) là đủ với giao thức stop-and-wait.
> - Các giao thức thực tế như TCP cũng dùng kỹ thuật tương tự, nhưng mạnh hơn nhiều!

## ✨ Điểm mới nổi bật ở RDT 2.1

![[Pasted image 20250406161650.png|center|500]]

![[Pasted image 20250406161705.png|center|500]]

Để giải quyết triệt để vấn đề **nhận nhầm gói tin cũ là gói mới**, rdt2.1 bổ sung thêm một cơ chế rất đơn giản mà hiệu quả: **số thứ tự gói tin (sequence number)**.

- Mỗi gói tin được gán một số thứ tự: `0` hoặc `1`.
- Bên gửi và bên nhận đều cần **nhớ** số thứ tự này để phân biệt gói tin mới và gói gửi lại.
- FSM (Finite State Machine – máy trạng thái hữu hạn) của cả **sender** và **receiver** giờ đây **có gấp đôi số trạng thái**, vì mỗi trạng thái phải lưu kèm thêm thông tin về `seq=0` hay `seq=1`.

> [!question]- Vì sao chỉ cần 0 và 1?
> - Giao thức chỉ cần phân biệt **gói hiện tại và gói trước đó**, nên chỉ cần **hai giá trị** là đủ.
> - Sau mỗi lần gửi thành công, số thứ tự **luân phiên đổi giữa 0 và 1** (gọi là "bit chẵn lẻ").

rdt2.1 cho phép người nhận gửi **ACK** (acknowledgment) hoặc **NAK** (negative acknowledgment):
- Nếu gói tin bị lỗi ➜ Gửi **NAK** để yêu cầu gửi lại.
- Nếu nhận đúng ➜ Gửi **ACK** tương ứng với số thứ tự của gói tin.

> [!example]- Ví dụ đơn giản
> - Bên gửi gửi gói tin số `0`.
> - Bên nhận kiểm tra thấy hợp lệ ➜ gửi ACK cho `0`.
> - Nếu gói đó bị lỗi ➜ gửi NAK và chờ gửi lại gói số `0`.

Mỗi hành động gửi – nhận giờ đây phải đi kèm với việc **kiểm tra hoặc sử dụng số thứ tự**:
- Bên gửi phải **kiểm tra số thứ tự của ACK nhận về** có đúng với gói tin đang chờ xác nhận không.
- Bên nhận phải **bao gồm số thứ tự trong ACK hoặc NAK gửi đi**, để bên gửi hiểu được phản hồi.

> [!caution]- Cảnh báo
> - Nếu không gắn `seq_num` trong ACK/NAK, người gửi không thể biết ACK đó là cho gói nào.
> - Điều này cực kỳ quan trọng khi các gói tin bị gửi lại.

**Cầu nối đến RDT 2.2 - NAK-free Protocol**
rdt2.1 hoạt động tốt, nhưng **việc dùng NAK vẫn hơi "rườm rà"**. Vậy nên trong **rdt2.2**, ta **loại bỏ hẳn NAK** bằng mẹo sau:

Không cần NAK nữa, chỉ cần gửi lại ACK cũ!
- Khi nhận nhầm hoặc gói lỗi ➜ **gửi lại ACK của gói trước đó**.
- Bên gửi nhận **hai ACK giống nhau liên tiếp** ➜ biết rằng gói bị lỗi.

---

# RDT 3.0 – Truyền dữ liệu "siêu đáng tin" qua kênh mất mát và lỗi bit

Ở phần trước, ta đã biết cách xử lý khi **dữ liệu bị lỗi bit** nhờ vào kỹ thuật như **checksum**, **ACK/NAK** và **sequence number** trong rdt2.2. Nhưng nếu **gói tin (packet) bị mất hoàn toàn** trên đường truyền thì sao? 😱  

Chào mừng bạn đến với **rdt3.0** – phiên bản nâng cấp giúp đảm bảo dữ liệu **vẫn về đích an toàn** kể cả khi bị rớt giữa đường!

## 💥 Vấn đề và Giải pháp Mất gói tin

Trong thế giới thật (và Internet hiện nay), gói tin không chỉ bị lỗi mà còn **có thể biến mất hoàn toàn** – có thể do router nghẽn, mất tín hiệu, hoặc một lý do "từ trên trời rơi xuống" nào đó. Giao thức rdt3.0 cần phải giải quyết **2 việc quan trọng**:

1. Làm sao **phát hiện** được gói tin (hoặc ACK) bị mất?
2. Và nếu mất thật, thì **làm gì để khôi phục**?

**Cách giải quyết**: Đặt _Timer_ và **tái gửi**

Giả sử sender (bên gửi) đã gửi một gói tin:
- Nếu gói tin đó **hoặc** gói ACK từ phía receiver gửi về bị mất => sender sẽ **không nhận được phản hồi nào cả** 😐
- Lúc này, sender cần phải **chờ một khoảng thời gian**. Nếu chờ mãi mà không thấy ACK, thì đoán rằng "chắc là mất rồi" => **gửi lại!**

**Nhưng chờ bao lâu là đủ?**
Đây mới là phần **hack não**:
- Chờ quá ngắn ➡️ có thể gói tin vẫn đang đến nhưng mình đã gửi lại rồi => gây **trùng lặp**
- Chờ quá lâu ➡️ **hiệu suất tệ** vì phải đợi rất lâu mới xử lý lỗi

Vậy nên, giao thức rdt3.0 chọn cách **"đoán hợp lý"** một khoảng thời gian gọi là **timeout interval** ⏲️, tức là giá trị của timeout interval thay đổi dựa vào điều kiện mạng hiện tại như độ trễ, tải mạng, jitter... 
Nếu sau thời gian đó vẫn chưa nhận được ACK, sender sẽ **kích hoạt timer interrupt** và gửi lại gói tin.

> [!caution]- Cảnh báo
> - Nếu sender gửi lại trong khi gói ban đầu vẫn còn trên đường, receiver sẽ **nhận 2 lần**
> - Nhưng đừng lo! Nhờ có **sequence number** (0 và 1), receiver có thể **phát hiện và loại bỏ gói lặp** ✅

Giao thức này dùng các thành phần sau để đảm bảo truyền tin "không lỗi":
- ✅ **Checksum** để kiểm tra lỗi bit
- 🔢 **Sequence number** (luân phiên 0 và 1) để phát hiện gói trùng
- 📩 **ACK/NAK** để xác nhận thành công hoặc yêu cầu gửi lại
- ⏲️ **Timer** để tự động gửi lại nếu phản hồi bị trễ hoặc mất

![[Pasted image 20250406164417.png|center|500]]

> [!info] Lưu ý
> - Vì chỉ dùng 2 số luân phiên (0 và 1) nên rdt3.0 còn có tên là **Alternating Bit Protocol**
> - Đơn giản nhưng cực kỳ hiệu quả cho kênh có mất mát và lỗi bit

---

# Các câu hỏi thường gặp

> [!caution]- Nội dung đang hoàn thiện
> Quá trình xây dựng nội dung này có thể mất nhiều thời gian ⌛, nhưng bạn có thể thúc đẩy nó bằng cách tham gia [[article-collaboration-guide|cộng tác bài viết]] 🤝
> 
> **Rất mong sự thông cảm của các bạn 🙏**

---

# Tổng kết
​Trong lĩnh vực truyền dữ liệu tin cậy (Reliable Data Transfer - RDT), việc đảm bảo dữ liệu được truyền chính xác và đúng thứ tự qua các kênh truyền không đáng tin cậy là một thách thức quan trọng. Dưới đây là tổng kết về các nguyên lý và phiên bản chính của giao thức RDT:​

**1. RDT 1.0 - Truyền dữ liệu qua kênh lý tưởng**
Phiên bản này giả định kênh truyền hoàn hảo, không có lỗi bit, mất gói hay trễ gói. Trong môi trường này, việc truyền dữ liệu diễn ra suôn sẻ mà không cần cơ chế kiểm tra hay xử lý lỗi.​

**2. RDT 2.0 - Xử lý lỗi bit trong kênh truyền**
Khi kênh truyền có thể gây lỗi bit, RDT 2.0 được giới thiệu với các cơ chế:​
- **Phát hiện lỗi**: Sử dụng checksum để kiểm tra tính toàn vẹn của gói tin.​
- **Phản hồi từ bên nhận**: Gửi ACK (xác nhận) nếu gói tin đúng, NAK (phủ nhận) nếu gói tin lỗi.​
- **Gửi lại khi cần thiết**: Bên gửi sẽ gửi lại gói tin khi nhận được NAK từ bên nhận.​

**3. RDT 2.1 và RDT 2.2 - Cải tiến xử lý lỗi và tránh trùng lặp**
Để giải quyết vấn đề gói tin ACK/NAK bị lỗi và tránh trùng lặp gói tin:​
- **Đánh số thứ tự gói tin**: Mỗi gói tin được gán một số thứ tự (0 hoặc 1) để phân biệt và kiểm soát việc gửi lại.​
- **Loại bỏ NAK**: Trong RDT 2.2, NAK được loại bỏ bằng cách bên nhận gửi lại ACK của gói tin trước đó khi phát hiện lỗi, giúp bên gửi nhận biết và gửi lại gói tin tương ứng.​

**4. RDT 3.0 - Đối phó với mất gói tin và lỗi bit**
Trong thực tế, gói tin có thể bị mất hoàn toàn trên đường truyền. RDT 3.0 bổ sung:​
- **Bộ đếm thời gian (Timer)**: Bên gửi đặt một khoảng thời gian chờ (timeout). Nếu không nhận được ACK trong thời gian này, gói tin được coi là mất và sẽ được gửi lại.​
- **Xử lý gói tin trùng lặp**: Bên nhận sử dụng số thứ tự gói tin để phát hiện và loại bỏ các gói tin trùng lặp.​

**Tóm lại**, các phiên bản của giao thức RDT được phát triển tuần tự để giải quyết các vấn đề từ kênh truyền lý tưởng đến kênh truyền có lỗi bit và mất gói. Những cơ chế như checksum, ACK/NAK, số thứ tự gói tin và bộ đếm thời gian là nền tảng để đảm bảo truyền dữ liệu tin cậy trong môi trường mạng không hoàn hảo.

