---
date: 2025-04-07
draft: true
status: Doing
title: Giao thức Selective Repeat (SR)
description: ""
author: PhDoanh
authorlink: https://github.com/PhDoanh
tags:
  - computer-networking
  - transport-layer
  - rdt
  - sr
aliases:
  - selective repeat
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
    src="images/selective-repeat.png"
    alt="Giao thức Selective Repeat (SR)" 
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

Trong thế giới mạng không đáng tin cậy – nơi mà gói tin có thể bị mất, bị trễ hoặc hỏng – việc đảm bảo **dữ liệu truyền đi một cách chính xác** là cực kỳ quan trọng. Sau khi đã học về các giao thức như **Stop-and-Wait** và **Go-Back-N (GBN)**, giờ là lúc giới thiệu một "cao thủ": **Selective Repeat (SR)** – người anh hùng giúp giảm thiểu việc truyền lại gói tin **không cần thiết**.

# 📦 Tại sao cần đến Selective Repeat?

Giao thức GBN giúp tăng hiệu suất so với Stop-and-Wait, nhưng lại có **một nhược điểm nghiêm trọng**: chỉ cần **1 gói lỗi**, nó sẽ **gửi lại toàn bộ các gói sau đó** trong cửa sổ trượt – dù chúng không sai!

![[Pasted image 20250407152525.png|center|500]]

> [!example]- Ví dụ đời thường
> Tưởng tượng bạn đang đọc chính tả, người chép viết sai một từ, và bạn phải đọc lại **1.000 từ vừa đọc** mặc dù chỉ sai một từ nhỏ. Chán không?

Giao thức **Selective Repeat** sinh ra để khắc phục nhược điểm này. Khi phát hiện lỗi, **chỉ gửi lại đúng gói bị mất hoặc hỏng**, không phải tất cả.

---

# 🔄 Cách hoạt động của Selective Repeat

![[Pasted image 20250407152556.png|center|500]]

**✉️ Phía người gửi (Sender)**:
1. **Nhận dữ liệu từ tầng trên** → nếu còn trong cửa sổ, gửi gói đi ngay.
2. **Sử dụng bộ đếm thời gian riêng cho từng gói tin** (mỗi gói có timer riêng).
3. **Khi nhận được ACK**, đánh dấu gói đó là đã nhận, và nếu là `send_base`, thì dịch cửa sổ trượt.

**📥 Phía người nhận (Receiver)**:
1. Khi nhận **gói nằm trong cửa sổ**:
    - Gửi ACK.
    - Nếu **lần đầu nhận**, thì buffer lại.
    - Nếu là `rcv_base`, kiểm tra các gói liền sau → gửi lên tầng trên và trượt cửa sổ.
2. Nếu nhận lại **gói cũ** (đã nhận trước đó), vẫn phải gửi lại ACK.
3. Nếu gói nằm **ngoài cửa sổ**, thì **bỏ qua**.

> [!info] Tái gửi ACK là điều bắt buộc 🔁
> Nếu người gửi không nhận được ACK cho `send_base`, họ sẽ không bao giờ trượt cửa sổ. ACK lại gói đã nhận giúp tránh tình trạng "kẹt cửa".

![[Pasted image 20250407152616.png|center|500]]

---

# 🔐 Câu chuyện số thứ tự giới hạn

![[Pasted image 20250407152942.png|center|500]]

Một vấn đề "hóc búa" xuất hiện khi **kích thước dãy số thứ tự bị giới hạn** (ví dụ 0–3) và cửa sổ trượt quá lớn.

> [!caution]- Cảnh báo vòng lặp nguy hiểm 🚨
> Nếu cửa sổ trượt quá nửa dãy số thứ tự, người nhận có thể **không phân biệt được** giữa một gói mới và một bản sao cũ. Điều này dẫn đến **nhầm lẫn dữ liệu nghiêm trọng**!

> [!tip]- Mẹo
> Đặt kích thước cửa sổ `N ≤ (kích thước không gian số thứ tự)/2` để tránh rắc rối.

---

# 🔄 So sánh nhanh: GBN vs. SR

| Tiêu chí         | Go-Back-N                                | Selective Repeat         |
| ---------------- | ---------------------------------------- | ------------------------ |
| Gửi lại khi lỗi  | Gửi lại tất cả sau gói lỗi               | Gửi lại đúng gói lỗi     |
| ACK              | Cumulative ACK (cho tất cả đến một điểm) | ACK riêng từng gói       |
| Buffer phía nhận | Không cần                                | Cần buffer để chờ đủ gói |
| Hiệu quả         | Thấp khi lỗi tăng                        | Cao hơn, ít lãng phí hơn |

---

# Các câu hỏi thường gặp

> [!caution]- Nội dung đang hoàn thiện
> Quá trình xây dựng nội dung này có thể mất nhiều thời gian ⌛, nhưng bạn có thể thúc đẩy nó bằng cách tham gia [[article-collaboration-guide|cộng tác bài viết]] 🤝
> 
> **Rất mong sự thông cảm của các bạn 🙏**

---

# 🎬 Kết luận

**Selective Repeat** là lựa chọn tối ưu trong môi trường mạng có tỷ lệ lỗi cao hoặc có băng thông lớn, giúp **giảm thiểu lãng phí và tăng hiệu suất truyền**.