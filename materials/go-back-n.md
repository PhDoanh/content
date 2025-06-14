---
date: 2025-04-07
draft: true
status: Doing
title: Giới thiệu về Giao thức Go-Back-N (GBN)
description: ""
author: PhDoanh
authorlink: https://github.com/PhDoanh
tags:
  - computer-networking
  - transport-layer
  - rdt
  - gbn
aliases:
  - go back n
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
    src="images/go-back-n.png"
    alt="Giới thiệu về Giao thức Go-Back-N (GBN)" 
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

Trong giao thức Go-Back-N (GBN), người gửi được phép truyền nhiều gói tin mà không cần chờ phản hồi (acknowledgment) cho mỗi gói, nhưng giới hạn số lượng gói chưa được xác nhận trong pipeline không vượt quá một giá trị tối đa, gọi là N. Hãy tưởng tượng như người gửi đang "đẩy" nhiều gói tin vào mạng, nhưng không thể gửi quá nhiều gói chưa được xác nhận cùng một lúc.

![[Pasted image 20250407145808.png|center|500]]

# Các dãy số hiệu trong GBN

![[Pasted image 20250407145910.png|center|500]]

Trong GBN, chúng ta có một số dãy số hiệu (sequence numbers) để phân biệt các gói tin. Cụ thể, các dãy số hiệu được chia thành các khoảng như sau:

1. **Dãy \[0, base-1\]**: Đây là các gói tin đã được gửi và nhận xác nhận (acknowledged).
2. **Dãy \[base, nextseqnum-1\]**: Các gói tin đã được gửi nhưng chưa có xác nhận.
3. **Dãy \[nextseqnum, base+N-1\]**: Các gói tin có thể gửi tiếp nếu có dữ liệu mới từ lớp trên.
4. **Dãy >= base+N**: Các số hiệu này không thể sử dụng cho đến khi một gói tin trong pipeline được xác nhận.

Điều này tạo thành một **cửa sổ trượt** có kích thước N, nơi người gửi có thể truyền gói mới ngay khi cửa sổ di chuyển về phía trước.

> [!question]- Tại sao giới hạn số lượng gói tin chưa xác nhận?
> - **Kiểm soát lưu lượng**: Giới hạn này giúp tránh việc truyền quá nhiều gói tin, gây tắc nghẽn mạng.
> - **Kiểm soát tắc nghẽn**: Như trong giao thức TCP, việc giới hạn số gói tin chưa xác nhận giúp điều chỉnh băng thông và giảm thiểu tình trạng tắc nghẽn.

# Cách hoạt động của GBN

![[Pasted image 20250407150137.png|center|500]]

**Bên người gửi**: GBN hoạt động theo ba sự kiện chính:
1. **Gửi dữ liệu từ lớp trên**: Khi lớp trên yêu cầu gửi dữ liệu (rdt_send), người gửi kiểm tra xem cửa sổ đã đầy chưa (N gói tin chưa xác nhận). Nếu chưa đầy, gói tin được gửi và các biến sẽ được cập nhật. Nếu cửa sổ đầy, dữ liệu sẽ được trả lại cho lớp trên.
2. **Nhận xác nhận (ACK)**: Khi nhận được ACK cho một gói tin, người gửi sẽ cập nhật trạng thái và di chuyển cửa sổ.
3. **Sự kiện timeout**: Nếu hết thời gian mà không nhận được ACK, người gửi sẽ gửi lại tất cả các gói chưa được xác nhận.

**Bên người nhận**: GBN sử dụng **xác nhận tổng hợp (cumulative acknowledgment)**. Người nhận sẽ:
- Chỉ xác nhận các gói tin đã nhận đúng thứ tự và không bỏ qua bất kỳ gói nào. Nếu một gói tin bị mất, tất cả các gói sau đó sẽ bị bỏ qua cho đến khi gói tin bị mất được nhận lại.
- Đơn giản là chỉ cần lưu trữ **sequence number của gói tin mong đợi** và gửi lại xác nhận cho gói tin đó.

> [!example]- Ví dụ về GBN
> - Giả sử cửa sổ có kích thước N = 4. Người gửi sẽ gửi gói 0, 1, 2, 3. Sau khi nhận được ACK 0 và ACK 1, người gửi sẽ gửi tiếp gói 4, 5.
> - Nếu gói tin số 2 bị mất, người nhận sẽ bỏ qua các gói tin 3, 4, 5 và chỉ gửi lại ACK của gói tin 1.

> [!caution]- Cảnh báo về việc mất gói tin
> Nếu một gói tin bị mất, tất cả các gói tin tiếp theo trong cửa sổ sẽ bị coi là "không hợp lệ" và sẽ bị bỏ qua. Điều này có thể dẫn đến việc phải truyền lại nhiều gói tin, gây lãng phí tài nguyên.

# Tại sao GBN lại hữu ích?

Giao thức GBN giúp đơn giản hóa việc quản lý các gói tin trong mạng không đáng tin cậy và hỗ trợ **phục hồi lỗi** bằng cách retransmit lại các gói tin mất mát. Tuy nhiên, có một số nhược điểm, chẳng hạn như việc **lãng phí băng thông** khi phải retransmit quá nhiều gói tin bị mất.

> [!tip]- Mẹo
> **GBN** thích hợp cho các mạng có tỷ lệ mất gói thấp hoặc khi có thể sử dụng lại các gói tin mất mà không gây quá nhiều lãng phí. Trong những tình huống khác, có thể xem xét các giao thức khác như Selective Repeat.

---

# Các câu hỏi thường gặp

> [!caution]- Nội dung đang hoàn thiện
> Quá trình xây dựng nội dung này có thể mất nhiều thời gian ⌛, nhưng bạn có thể thúc đẩy nó bằng cách tham gia [[article-collaboration-guide|cộng tác bài viết]] 🤝
> 
> **Rất mong sự thông cảm của các bạn 🙏**

---

# Kết luận
Giao thức Go-Back-N rất hữu ích trong việc cung cấp một giải pháp đơn giản và hiệu quả cho việc truyền tải dữ liệu đáng tin cậy, nhưng với một số hạn chế nhất định trong trường hợp mạng không ổn định.
