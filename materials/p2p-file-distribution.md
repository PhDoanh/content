---
date: 2025-03-19
draft: false
status: Done
title: Phân phối dữ liệu trong kiến trúc Mạng ngang hàng
description: Tìm hiểu cách phân phối file qua kiến trúc P2P, so sánh với mô hình client-server và khám phá cách BitTorrent hoạt động. Bài viết giải thích chi tiết, kèm ví dụ thực tế và các công thức tính toán để bạn dễ dàng nắm bắt nội dung 🚀
author: PhDoanh
authorlink: https://github.com/PhDoanh
tags:
  - computer-networking
  - application-layer
  - web
  - file-transfer
  - p2p
aliases:
  - p2p file distribution
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
    src="images/p2p-file-distribution.png"
    alt="Phân phối dữ liệu trong kiến trúc Mạng ngang hàng" 
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

**Phân phối file** là một ứng dụng điển hình của kiến trúc **P2P (Peer-to-Peer)**, nơi các máy chủ không đơn thuần là nơi phát tán file mà còn được hỗ trợ bởi chính các **peer** tham gia chia sẻ. Điều này giúp giảm tải cho máy chủ và tiết kiệm băng thông. Trong bài viết này, chúng ta sẽ cùng nhau khám phá cách phân phối file qua P2P, so sánh với mô hình **client-server** và tìm hiểu cơ chế hoạt động của **BitTorrent** – giao thức P2P nổi tiếng.

# Giới thiệu

Trong mô hình **client-server truyền thống**, máy chủ phải gửi từng bản sao file cho mỗi người dùng, gây tắc nghẽn và tiêu tốn băng thông. Ngược lại, trong kiến trúc **P2P**, mỗi peer vừa nhận file vừa chia sẻ nó cho các peer khác. Nhờ đó, tải trọng được phân chia đều, giúp hệ thống **tự cân bằng** và mở rộng theo số lượng người dùng.

> [!info] Lưu ý
> - Trong kiến trúc mạng ngang hàng, máy chủ thường được gọi là **peer**
> - Mô hình P2P không chỉ giúp tiết kiệm tài nguyên mà còn cải thiện tốc độ phân phối file khi số lượng peer tăng lên.

---

# So sánh P2P với Client-Server

## Client-Server

**Quá trình phân phối:** Máy chủ gửi một bản sao file đến mỗi peer.
**Thời gian phân phối tối thiểu:**  
$$
D_{cs} \ge \max\left\{\frac{NF}{u_s}, \frac{F}{d_{\min}}\right\}
$$

**Trong đó:**  
- $D_{cs}$: Độ trễ phân phối của Client-Server
- $N$: số peer.
- $F$: kích thước file
- $u_s$: Tốc độ tải đi của máy chủ.  
- $d_{\min}$: Tốc độ tải về của peer chậm nhất.

**Hạn chế:** Thời gian phân phối tăng theo tỷ lệ tuyến tính với số lượng peer, gây ra hiện tượng nghẽn băng thông khi $N$ lớn.

> [!example]- Ví dụ
>
> Giả sử ta có các thông số sau:
> - Số lượng client: $N=10$
> - Kích thước file cần truyền: $F=1 \text{GB}$ (tương đương $8000 \text{Mb}$)
> - Băng thông upload của server: $u_s=5\text{Mbps}$
> - Băng thông upload của mỗi client: $u_i=1 \text{Mbps}$ (cho $i=1,\ldots, 10$)
> - Băng thông download tối thiểu của các client: $d_min⁡=2 \text{Mbps}$
> 
> Ta có:
> $$\frac{NF}{u_s}=\frac{10\times 8000}{5}=16000 s$$
> $$\frac{F}{d_{min}}=\frac{8000}{2}=4000 s$$
> 
> Vậy thời gian phân phối của mô hình client-server là:
> $$D_{cs} \ge \max\{16000,4000\}=16000 s$$

## Peer-To-Peer

- **Quá trình phân phối:** Máy chủ ban đầu chỉ gửi file một lần vào mạng. Sau đó, mỗi peer chia sẻ các phần file mình nhận được cho các peer khác.
- **Thời gian phân phối tối thiểu:**  

$$
D_{P2P} \ge \max\left\{\frac{F}{u_s}, \frac{F}{d_{\min}}, \frac{NF}{u_s + \sum_{i=1}^{N} u_i}\right\}
$$

**Trong đó:**  
- **Phần đầu**: Máy chủ phải gửi file ít nhất một lần $\frac{F}{u_s}$.  
- **Phần thứ hai**: Peer chậm nhất không thể nhận file nhanh hơn $\frac{F}{d_{\min}}$. 
- **Phần thứ ba**: Tổng băng thông tải đi của toàn hệ thống $u_s + \sum u_i$ giới hạn tốc độ gửi tổng số $N\times F$ bit.

**Ưu điểm:** Với P2P, thời gian phân phối không phụ thuộc tuyến tính vào số lượng peer; thậm chí, với số lượng peer lớn, thời gian có thể **đều đặn thấp hơn** rất nhiều so với client-server.

**P2P và Tính tự mở rộng**: Hệ thống P2P cho phép các peer vừa là người nhận vừa là người gửi, làm tăng **tổng băng thông tải đi** của hệ thống. Nhờ vậy, ngay cả khi số lượng peer tăng cao, thời gian phân phối file vẫn có thể duy trì ở mức chấp nhận được. 

> [!example]- Ví dụ
> Nếu áp dụng P2P cho các thông số của ví dụ trên, ta có:
> $$\frac{F}{u_s}=\frac{8000}{5}=1600 s$$
> $$\frac{F}{d_{min}}=4000 s$$
> $$\frac{NF}{u_s+\sum_{i=1}^{N}u_i}=\frac{10\times 8000}{15}~\text{≈}~5333 s$$
>
> Vậy thời gian phân phối của mô hình P2P là:
> $$D_{P2P} \ge \max\{1600,~4000,~5333\}=5333 s$$

---

# BitTorrent - Ví dụ tiêu biểu của P2P

**BitTorrent** là giao thức P2P phổ biến nhất hiện nay. Khi một file lớn cần phân phối, nó được chia thành các **chunk** (thường là 256 KB). Quá trình hoạt động của BitTorrent bao gồm các bước sau:

1. **Tracker:** Là một node trung tâm quản lý danh sách các peer trong torrent. Khi một peer mới (ví dụ: **Alice**) tham gia, tracker gửi cho Alice danh sách các peer khác (có thể là 50 peer) để kết nối.

2. **Kết nối và trao đổi:** Alice cố gắng thiết lập kết nối TCP với các peer được liệt kê, tạo thành danh sách các **neighboring peers**. Sau đó, Alice gửi yêu cầu để nhận danh sách các chunk mà các peer sở hữu.

BitTorrent sử dụng nhiều thuật toán để tối ưu hóa quá trình chia sẻ file trong mạng **P2P**. Dưới đây là những thuật toán chính kèm theo giải thích và ví dụ dễ hiểu.

## Rarest First - Ưu tiên mảnh file hiếm nhất

**Ý tưởng chính:** Khi tải xuống file, BitTorrent sẽ **ưu tiên tải các mảnh (pieces) hiếm nhất trước**. Một mảnh file **hiếm** là mảnh có ít peer sở hữu nó nhất.

> [!example]- Ví dụ
> Giả sử một file có **4 mảnh**:
> 
> |Mảnh file|Số peer có mảnh này|
> |---|---|
> |Mảnh 1|10 peer|
> |Mảnh 2|8 peer|
> |Mảnh 3|12 peer|
> |Mảnh 4|5 peer|
> 
> **BitTorrent sẽ ưu tiên tải Mảnh 4 trước**, vì nó là mảnh hiếm nhất.

**Lợi ích:**  
- Tránh tình trạng **một số mảnh file bị thiếu** làm chậm quá trình tải.  
- Đảm bảo tất cả các mảnh của file đều được phân tán tốt trên toàn mạng.  
- Tăng cơ hội **song song hóa** khi tải file.

## Tit-for-Tat - Có qua có lại

**Ý tưởng chính:** Một peer chỉ cho phép tải file nếu những peer khác cũng **chia sẻ lại** với nó. Nếu một peer không chia sẻ, các peer khác sẽ **chặn (choke)** nó.

> [!example]- Ví dụ
> Giả sử có 4 người A, B, C, D đang tải một bộ phim:
> - A chia sẻ file cho B.
> - B chia sẻ file cho C.
> - C chia sẻ file cho D.
> - Nhưng D **chỉ tải về mà không chia sẻ lại** (leeching).
>
> **BitTorrent sẽ chặn D lại (choke), ngăn D tiếp tục tải.**  
> **Những ai chia sẻ nhiều sẽ được ưu tiên tải nhanh hơn!**

**Lợi ích:**  
- Ngăn chặn người **chỉ tải mà không chia sẻ (leechers)**.  
- Tạo ra một hệ thống công bằng, ai chia sẻ nhiều thì được tải nhanh hơn.  
- Tối ưu băng thông mà không cần máy chủ trung tâm.

## Endgame Mode - Tăng tốc tải xuống lúc cuối

**Ý tưởng chính:** Khi một peer chỉ còn **một số ít mảnh file chưa tải xong**, nó sẽ **gửi yêu cầu tải mảnh đó đến nhiều peer cùng lúc**. Ai gửi mảnh đó trước thì peer sẽ nhận, các yêu cầu khác bị hủy.

> [!example]- Ví dụ
> - Bạn đã tải **99%** bộ phim, chỉ còn **một mảnh cuối cùng**.
> - Thay vì đợi một peer gửi cho bạn, bạn **yêu cầu nhiều peer cùng lúc**.
> - Ai gửi trước thì bạn nhận, những người còn lại hủy bỏ yêu cầu.

**Lợi ích:**  
- Giúp **tải nhanh hơn** khi sắp hoàn thành.  
- Tránh tình trạng **chờ quá lâu** nếu một peer bị chậm.

## Selective Piece Downloading - Chọn mảnh tải xuống hợp lý

**Ý tưởng chính:** Một số ứng dụng BitTorrent cho phép chọn **mảnh file quan trọng để tải trước**.

> [!example]- Ví dụ
> - Bạn tải một bộ phim, nhưng muốn xem thử trước khi tải hết.
> - BitTorrent có thể **ưu tiên tải phần đầu của video** trước để bạn xem ngay.

**Lợi ích:**  
- Hữu ích cho những file lớn như video.  
- Người dùng có thể kiểm tra file trước khi tải hết.

## Super Seeding - Tối ưu cho seeders

**Ý tưởng chính:** Dùng cho **người chia sẻ file đầu tiên (seeder)**. Seeder sẽ **phát mỗi mảnh file chỉ một lần duy nhất** cho một peer. Sau đó, peer này phải **chia sẻ lại với các peer khác** trước khi nhận mảnh mới.

> [!example]- Ví dụ
> - Bạn muốn chia sẻ một file 1GB lần đầu tiên.
> - Thay vì gửi nhiều lần cùng một mảnh cho nhiều người, bạn sẽ **phát mỗi mảnh chỉ một lần**.
> - Những người nhận được sẽ **phải chia sẻ lại với người khác** để có thêm mảnh mới.

**Lợi ích:**  
- Giúp file **lan truyền nhanh hơn** trong mạng P2P.  
- Giảm tải cho **seeder**, tránh lãng phí băng thông.

---

# Các câu hỏi thường gặp

> [!caution]- Nội dung đang hoàn thiện
> Quá trình xây dựng nội dung này có thể mất nhiều thời gian ⌛, nhưng bạn có thể thúc đẩy nó bằng cách tham gia [[article-collaboration-guide|cộng tác bài viết]] 🤝
> 
> **Rất mong sự thông cảm của các bạn 🙏**

---

# Tổng kết 

Qua bài viết này, chúng ta đã cùng khám phá:
- **Mô hình client-server** và cách phân phối file bằng cách gửi từng bản sao từ máy chủ.
- **Kiến trúc P2P** với lợi thế chia sẻ tải và tự mở rộng, giúp giảm thời gian phân phối file.
- **BitTorrent** – một ví dụ điển hình của P2P, sử dụng các chiến lược như **rarest first**, **tit-for-tat**, ... để tối ưu quá trình trao đổi dữ liệu.

Nhờ vào kiến trúc P2P, việc phân phối file trở nên **nhanh chóng**, **hiệu quả** và **đáng tin cậy** ngay cả khi số lượng người dùng tăng cao. Nếu bạn muốn tìm hiểu thêm, hãy tham khảo các nghiên cứu và bài viết về [BitTorrent](https://en.wikipedia.org/wiki/BitTorrent) và [Peer-to-Peer](https://en.wikipedia.org/wiki/Peer-to-peer) để có cái nhìn sâu sắc hơn 🚀.
