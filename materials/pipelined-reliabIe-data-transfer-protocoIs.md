---
date: 2025-04-06
draft: true
status: Doing
title: Tăng tốc RDT 3.0 với kỹ thuật Pipelining
description: ""
author: PhDoanh
authorlink: https://github.com/PhDoanh
tags:
  - computer-networking
  - transport-layer
  - rdt
  - reliable-data
  - dtp-principles
  - pipelined
aliases:
  - pipelined reliabIe data transfer protocoIs
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
    src="images/pipelined-reliabIe-data-transfer-protocoIs.png"
    alt="Tăng Tốc RDT 3.0 Với Kỹ Thuật Pipelining" 
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

Trong phần trước, chúng ta đã tìm hiểu về **rdt3.0** – một giao thức truyền tin cậy trong mạng máy tính. Dù đảm bảo tính đúng đắn, nhưng rdt3.0 lại có một **vấn đề nghiêm trọng về hiệu suất**. Hãy cùng phân tích lý do và cách khắc phục vấn đề này!

# 😵 Tại sao RDT 3.0 lại chậm?
**RDT 3.0** sử dụng phương pháp truyền **"stop-and-wait"**, tức là: 📦 Gửi 1 gói → 🕒 Đợi ACK (phản hồi) → 📦 Gửi tiếp

Hãy tưởng tượng hai máy tính, một ở bờ Tây và một ở bờ Đông nước Mỹ, kết nối qua đường truyền tốc độ **1 Gbps**. Gói tin có kích thước **1,000 byte (8,000 bit)**.

**Thời gian truyền gói tin**:
$$
d_{trans} = \frac{L}{R} = \frac{8000~\text{bits/packet}}{10^9~\text{bit/sec}} = 8~microseconds
$$

- Độ trễ vòng (RTT): ~ **30 ms**

Khi gửi 1 gói:
- 👨‍💻 Gửi mất 8 micro giây
- 🧳 Truyền qua mạng mất 15 ms
- 📬 Nhận ACK quay về mất thêm 15 ms

⏱ **Tổng thời gian để gửi xong 1 gói là 30.008 ms**, nhưng trong đó, chỉ **8 micro giây là đang thực sự truyền**.

**Tính toán hiệu suất**:
$$
U_{sender} = \frac{L/R}{RTT + L/R} = 0.00027
$$

Hiệu suất chỉ đạt **267 kbps** (chỉ **0.027%** thời gian là có truyền dữ liệu thật), dù băng thông thực tế là **1 Gbps** 🤯

> [!caution]- Cảnh báo
> Bạn có thể bỏ hàng tỷ đồng đầu tư đường truyền tốc độ cao, nhưng nếu dùng rdt3.0, bạn chỉ khai thác được **một phần rất nhỏ** sức mạnh đó!

---

# 🚀 Giải pháp Pipelining - Truyền như dòng nước chảy

![[Pasted image 20250407143055.png|center|500]]

Thay vì gửi rồi đợi, chúng ta **gửi liên tiếp nhiều gói tin** trước khi đợi phản hồi. Kỹ thuật này gọi là **pipelining** – giống như một đường ống mà trong đó các gói tin liên tục di chuyển.

Ví dụ, nếu cho phép gửi **3 gói trước khi chờ ACK**, hiệu suất sẽ **tăng gấp 3 lần**.

> [!example]- Ví dụ
> Hãy tưởng tượng băng chuyền sushi 🍣: từng đĩa (gói tin) liên tục di chuyển tới người ăn (người nhận), không phải chờ ăn xong một đĩa mới được lấy cái tiếp theo.

Việc cho phép nhiều gói cùng lúc đồng nghĩa với **nhiều thứ phải quản lý hơn**. Những thay đổi cần có khi dùng pipelining
- **Phạm vi số thứ tự (sequence number)** phải rộng hơn → mỗi gói trong luồng đều cần số thứ tự riêng
- **Buffer (bộ đệm)** ở cả hai phía cần mở rộng → để lưu các gói đã gửi (chưa được xác nhận) hoặc đã nhận (chưa đúng thứ tự)
- Cách xử lý **gói mất mát, trễ, lỗi** cần cải tiến để xử lý nhiều gói đồng thời

---

# ⚙️ Xử lý lỗi trong pipelining

1. **Go-Back-N (GBN) – Quay lại từ đầu**
- Nếu một gói lỗi, **tất cả gói sau đó cũng bị gửi lại**, kể cả khi chúng đúng.
- GBN Có thể gây **lãng phí băng thông** khi chỉ 1 gói lỗi nhưng nhiều gói khác vẫn phải truyền lại.

2. **Selective Repeat (SR) – Lọc lại từng gói**
- Chỉ gửi lại **những gói lỗi**.
- Cần **nhiều bộ nhớ hơn** và xử lý phức tạp hơn, nhưng hiệu quả cao hơn.

---

# Các câu hỏi thường gặp

> [!caution]- Nội dung đang hoàn thiện
> Quá trình xây dựng nội dung này có thể mất nhiều thời gian ⌛, nhưng bạn có thể thúc đẩy nó bằng cách tham gia [[article-collaboration-guide|cộng tác bài viết]] 🤝
> 
> **Rất mong sự thông cảm của các bạn 🙏**

---

# 📌 Tổng kết
- **rdt3.0** tuy đúng chức năng nhưng quá **thiếu hiệu quả** trong thực tế.
- **Pipelining** là giải pháp mạnh mẽ để tận dụng hết tốc độ của mạng hiện đại.
- Sử dụng **GBN** hay **SR** tùy thuộc vào nhu cầu hiệu năng vs độ phức tạp của hệ thống.

Tóm lại, Stop-and-wait = đơn giản nhưng chậm ⏳. Còn Pipelining = nhanh và hiệu quả, nhưng cần quản lý tốt hơn ⚙️
