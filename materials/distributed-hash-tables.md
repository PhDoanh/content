---
date: 2025-03-19
draft: false
status: Done
title: Kiến Trúc và Ứng Dụng của Distributed Hash Tables Trong Mạng P2P
description: Tìm hiểu cách xây dựng Distributed Hash Tables (DHTs) – một cơ chế phân phối cơ sở dữ liệu (key, value) trên hàng triệu peer. Bài viết giải thích khái niệm, cách thiết kế overlay vòng tròn, quản lý peer churn và ứng dụng trong BitTorrent 🚀
author: PhDoanh
authorlink: https://github.com/PhDoanh
tags:
  - computer-networking
  - application-layer
  - web
  - p2p
  - hash-tables
aliases:
  - distributed hash tables
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
    src="images/distributed-hash-tables.png"
    alt="Distributed Hash Tables (DHTs): Kiến Trúc và Ứng Dụng Trong Mạng P2P  " 
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

---

Distributed Hash Tables (DHTs) là một trong những công nghệ cốt lõi giúp xây dựng cơ sở dữ liệu phân tán trong các mạng P2P. Thay vì lưu trữ toàn bộ dữ liệu trên một máy chủ trung tâm, DHT cho phép các cặp **(key, value)** được phân tán trên nhiều peer, giúp tăng khả năng mở rộng và độ tin cậy của hệ thống.

# Giới thiệu Distributed Hash Tables

Trong một hệ thống P2P, mỗi peer chỉ lưu trữ một phần nhỏ của tổng cơ sở dữ liệu. Khi một peer muốn tra cứu hoặc thêm mới một cặp key-value, hệ thống DHT sẽ định vị peer chịu trách nhiệm lưu trữ cặp đó.  

> [!info] Lưu ý
> DHT thường được sử dụng để xây dựng các dịch vụ như **distributed trackers** trong BitTorrent, nơi mà một torrent identifier được ánh xạ với danh sách IP của các peer.

**Cơ sở dữ liệu phân tán** dùng để lưu trữ và truy vấn các cặp (key, value) một cách phân tán trên hàng triệu peer.

> [!example]- Ví dụ
> - **Key:** "Led Zeppelin IV" - Tên của nội dung  
> - **Value:** `128.17.123.38` - Địa chỉ IP của peer chứa nội dung đó.

DHT sử dụng hàm băm (hash function) để chuyển đổi các key không phải số (như tên phim, số an sinh xã hội) thành số nguyên trong khoảng $[0, 2^n - 1]$; với $n$ là số bit dùng để biểu diễn định danh  

> [!example]- Ví dụ
> Nếu key ban đầu là "Led Zeppelin IV", hàm băm sẽ cho ra một số nguyên, từ đó DHT sử dụng số đó để định vị nơi lưu trữ dữ liệu

# Phân phối Key-Value trong DHT

Hệ thống DHT sử dụng một **hàm băm** để xác định vị trí lưu trữ của một **key** trên mạng P2P. Quá trình này gồm các bước:

1. **Băm key**: Một key (ví dụ: tên file, ID tài liệu) được chuyển đổi thành một số nguyên bằng một **hàm băm** qua các thuật toán như: SHA-1, SHA-256, ... Số nguyên này xác định vị trí của key trong **không gian địa chỉ** của DHT.

2. **Xác định peer chịu trách nhiệm lưu trữ**: Mỗi peer trong hệ thống cũng có một ID duy nhất, được gán bằng cùng một hàm băm. Một key sẽ được lưu trữ tại peer có **ID gần nhất nhưng lớn hơn hoặc bằng key** (gọi là **"closest successor"**).

> [!example]- Ví dụ
> Giả sử ta có một hệ thống DHT với 6 peer, mỗi peer có một **ID** trong khoảng $[0,~15]$ (với $n = 4$, tương đương $2^4=16$ không gian địa chỉ tính từ 0 đến 15):
> 
> | Peer | ID  |
> | ---- | --- |
> | P1   | 1   | 
> | P2   | 3   |
> | P3   | 6   |
> | P4   | 9   |
> | P5   | 12  |
> | P6   | 15  |
> 
> **Bước 1: Băm key để xác định nơi lưu trữ**
> Giả sử ta muốn lưu file "data.txt", ta băm chuỗi "data.txt" bằng hàm SHA-1: hash("data.txt") = 10
> 
> **Bước 2: Xác định peer nào lưu trữ giá trị của key = 10**
> - Nhìn vào danh sách ID của các peer: 1, 3, 6, 9, 12, 15.
> - Tìm peer có ID lớn nhất nhưng gần nhất với 10.
> - Peer 12 (P5) là closest successor, nên file "data.txt" sẽ được lưu trữ tại P5.
>   
> Khi một peer mới (P7) với ID = 5 muốn tìm file "data.txt":
> 1. **Băm key** `"data.txt"` được **ID = 10**.
> 2. DHT bắt đầu truy vấn:
> 	- P7 kiểm tra danh sách các peer mà nó biết, thấy không có ID nào là 10.
> 	- P7 gửi truy vấn đến một peer gần nhất mà nó biết có ID gần với 10 nhất, ví dụ: P3 (ID = 6).
> 	- P3 tiếp tục gửi truy vấn đến P4 (ID = 9).
> 	- P4 chuyển tiếp đến P5 (ID = 12), là nơi đang lưu file "data.txt".
> 3. P5 trả về dữ liệu cho P7.
>    
>  **Lưu ý**:
>  - Hệ thống DHT này được thiết kế dưới dạng vòng nên 1 peer (P7) chỉ có thể biết các peer trước (Peer có ID 4) và sau nó (Peer có ID 5 là P3)
>  - Nếu hệ thống có **shortcuts** (đường tắt), P7 có thể biết trước P5 mà không cần đi từng bước qua P3, P4, giúp giảm độ trễ truy vấn. Hệ thống này cho phép P7 có bảng định tuyến đầy đủ (bảng các peer liên kết với P7) 

**Ưu điểm của cách phân phối này**:
- **Tính mở rộng:** Mỗi peer chỉ cần biết thông tin của một số ít peer lân cận.
- **Giảm tải:** Không yêu cầu mỗi peer phải lưu trữ thông tin của toàn bộ hệ thống.

# Thiết kế sơ đồ mạng logic dạng vòng tròn

**Cấu trúc mô hình overlay:** Các peer được sắp xếp thành một vòng tròn (circular overlay), với mỗi peer chỉ biết thông tin của **người kế tiếp** và **người đứng trước**.

> [!example]- Ví dụ
> - Với 8 peer có định danh: 1, 3, 4, 5, 8, 10, 12, 15.
> - Một peer (ví dụ peer 3) khi cần tìm peer chịu trách nhiệm cho key 11 sẽ gửi thông điệp đi theo chiều kim đồng hồ cho đến khi thông điệp tới peer 12, xác định rằng peer 12 là người "gần nhất" với key 11. Điều này yêu cầu peer gửi truy vấn tới peer trước nó hoặc sau nó miễn là ID gần với key nhất 
  
**Giải pháp mở rộng - Thêm "shortcuts"**
- **Shortcuts:** Mỗi peer có thể lưu thêm thông tin của một số peer xa hơn trong vòng tròn. Giúp **rút ngắn số lượng thông điệp** cần chuyển tiếp để định vị một key.
- **Lợi ích:** Đưa số lượng thông điệp trung bình về mức $O(\log N)$ thay vì $O(N)$ trong mô hình vòng tròn cơ bản.

---

# Quản lý Peer Churn trong DHT
**Peer churn** xảy ra khi các peer tham gia hoặc rời khỏi hệ thống một cách bất thường, khiến cho DHT phải cập nhật thông tin kịp thời để duy trì tính nhất quán của hệ thống qua các giải pháp sau:

- **Theo dõi liên tục:** Mỗi peer theo dõi **người kế tiếp** (successor) và **người đứng trước** (predecessor). Đôi khi, lưu thêm thông tin của **người kế tiếp thứ hai** để dự phòng.

- **Cơ chế cập nhật:** Khi một peer không phản hồi (ví dụ, peer 5 rời khỏi), các peer lân cận sẽ cập nhật thông tin của mình để kết nối với peer mới. Quá trình này giúp duy trì **overlay network** ổn định trong trường hợp có peer churn.

---

# Ứng dụng DHT trong BitTorrent

- **BitTorrent sử dụng DHT (ví dụ: Kademlia DHT)** để tạo ra một distributed tracker.
- **Quy trình:**  
	- Một torrent identifier được băm thành một key.
	- DHT ánh xạ key đó tới danh sách IP của các peer đang chia sẻ torrent.
	- Một peer mới có thể truy vấn DHT để tìm ra các peer chứa file cần tải.

> [!info] Lưu ý
> Việc sử dụng DHT trong BitTorrent giúp loại bỏ sự phụ thuộc vào các tracker tập trung, tăng tính **phi tập trung** và **độ tin cậy** của hệ thống.

---

# Các câu hỏi thường gặp

> [!caution]- Nội dung đang hoàn thiện
> Quá trình xây dựng nội dung này có thể mất nhiều thời gian ⌛, nhưng bạn có thể thúc đẩy nó bằng cách tham gia [[article-collaboration-guide|cộng tác bài viết]] 🤝
> 
> **Rất mong sự thông cảm của các bạn 🙏**

---

# Tổng kết

Qua bài viết này, chúng ta đã tìm hiểu:
- **Distributed Hash Tables (DHTs)** là cơ chế phân phối dữ liệu (key, value) trên mạng P2P, sử dụng hàm băm để chuyển key thành số nguyên.
- **Quy tắc phân phối "closest successor"** giúp định vị peer chịu trách nhiệm lưu trữ một key.
- **Overlay mạng dạng vòng tròn** giúp giảm lượng thông tin mỗi peer phải lưu trữ, và **shortcuts** cải thiện hiệu năng định tuyến.
- **Quản lý Peer Churn** thông qua việc theo dõi thông tin của các peer lân cận, đảm bảo hệ thống luôn ổn định.
- **Ứng dụng thực tế:** BitTorrent sử dụng DHT để quản lý torrent một cách phân tán, giảm phụ thuộc vào tracker tập trung.

Nhờ vào DHT, các hệ thống P2P có thể **mở rộng linh hoạt** và **phân phối dữ liệu hiệu quả** ngay cả khi có hàng triệu peer tham gia. Nếu bạn muốn tìm hiểu sâu hơn, hãy tham khảo các bài viết và nghiên cứu về [Kademlia DHT](https://en.wikipedia.org/wiki/Kademlia) hoặc [Chord](https://en.wikipedia.org/wiki/Chord_(protocol)) để biết thêm chi tiết 🚀.
