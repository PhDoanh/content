---
date: 2025-02-12
draft: false
status: Doing
title: "Độ trễ, mất gói và thông lượng: Hiểu rõ hiệu suất mạng gói"
description: Bạn có biết rằng trong mạng chuyển mạch gói, dữ liệu có thể bị mất, bị trễ hoặc bị giới hạn về tốc độ truyền tải? Bài viết này sẽ giúp bạn hiểu rõ về độ trễ, mất gói, thông lượng, cũng như cách chúng ảnh hưởng đến hiệu suất mạng! 🚀
author: PhDoanh
authorlink: https://github.com/PhDoanh
tags:
  - computer-network
  - internet
aliases:
  - delay loss throughput
cssclasses:
  - img
  - btn
---
%% ĐỊNH DẠNG TÊN FILE: "tên-bài-viết" | VD: jp-typing-guide %%

%% <figure style="text-align: center; margin: 20px auto;">
  <img 
    src="images/delay-loss-throughput.png"
    alt="Độ trễ, mất gói và thông lượng: Hiểu rõ hiệu suất mạng gói" 
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
</figure> %%

Mạng Internet ngày nay hoạt động dựa trên cơ chế **chuyển mạch gói** (packet-switching), trong đó dữ liệu được chia nhỏ thành các gói tin và truyền từ nguồn đến đích qua nhiều thiết bị mạng. Tuy nhiên, không phải lúc nào quá trình truyền tải này cũng diễn ra **hoàn hảo**. Các yếu tố như **độ trễ** (delay), **mất gói** (packet loss) và **thông lượng** (throughput) ảnh hưởng rất nhiều đến hiệu suất của mạng.

# ⏳ Độ trễ trong mạng chuyển mạch gói

Độ trễ trong mạng là khoảng thời gian cần thiết để một gói tin di chuyển từ nguồn đến đích. Có nhiều loại độ trễ khác nhau ảnh hưởng đến tổng thời gian truyền của gói tin.

## Độ trễ xử lý (Processing Delay)

- Xảy ra tại mỗi nút mạng (router, switch, host).
- Gồm thời gian đọc tiêu đề gói tin, kiểm tra lỗi, và quyết định tuyến đường.

## Độ trễ xếp hàng (Queuing Delay)

- Gói tin phải **chờ** tại bộ đệm của thiết bị mạng trước khi được truyền đi.
- **Phụ thuộc vào mức độ tắc nghẽn của mạng**: nếu có nhiều gói tin đến cùng lúc, thời gian chờ sẽ tăng lên đáng kể.

## Độ trễ truyền tải (Transmission Delay)
Thời gian cần để **đưa toàn bộ gói tin vào đường truyền**:

$$
d_{trans}=\frac LR
$$

Trong đó:
- $L$ là kích thước gói tin (bit),
- $R$ là tốc độ truyền tải của liên kết (bits/second).

## Độ trễ lan truyền (Propagation Delay)
Thời gian để một bit **di chuyển từ nguồn đến đích** qua môi trường truyền (cáp quang, dây đồng, sóng vô tuyến...):

$$
d_{prop}=\frac ds
$$

Trong đó:
- $d$: khoảng cách giữa 2 thiết bị mạng
- $s$: tốc độ truyền tín hiệu trong môi trường đó


## Công thức tổng quát của độ trễ tại một nút mạng

$$
d_{nodal}=d_{proc}+d_{queue}+d_{trans}+d_{prop}
$$

Trong đó:
- $d_{proc}$: độ trễ xử lý
- $d_{queue}$: độ trễ xếp hàng (chờ đợi)
- $d_{trans}$: độ trễ truyền tải
- $d_{prop}$: độ trễ lan truyền

> [!example]- Ví dụ
> Giả sử bạn đang gửi một file từ **máy tính A** đến **máy chủ B** qua mạng có 3 nút trung gian. Nếu:
> - $d_{proc}=1ms$
> - $d_{queue}=5ms$
> - $d_{trans}=10ms$
> - $d_{prop}=20ms$
> - Số nút trung gian $N=3$
> 
> Khi đó, tổng độ trễ **end-to-end**:
> $$d_{end-to-end}=N(d_{prac}+d_{queue}+d_{trans}+d_{prop})=3(1+5+10+20)=108ms$$

---

# 🚨 Mất gói trong mạng

Đây là các nguyên nhân khiến gói tin bị mất:
- **Bộ đệm của router bị đầy** → Gói tin bị loại bỏ.
- **Lỗi tín hiệu** → Bit trong gói tin bị lỗi, gói tin bị hủy.
- **Xung đột mạng** (congestion) khiến một số gói không đến được đích.

> [!danger] Hậu quả nếu mất gói
> - Giảm hiệu suất ứng dụng mạng (video call bị giật, game online lag...).
> - Tăng thời gian chờ vì gói tin cần được **gửi lại**.
> - Gây ra hiện tượng **timeout** trong giao thức truyền tải dữ liệu như TCP.

> [!check] Giải pháp cải thiện
> - **Tăng dung lượng bộ đệm trên router**  
> - **Sử dụng thuật toán điều khiển tắc nghẽn (Congestion Control) như TCP Reno**  
> - **Sử dụng giao thức UDP cho ứng dụng thời gian thực (VoIP, livestream, game online)**

---

# 📡 Thông lượng trong mạng

Thông lượng (throughput) là **tốc độ dữ liệu thực tế** được truyền từ nguồn đến đích trong một khoảng thời gian.

## Các yếu tố ảnh hưởng đến thông lượng 

- **Băng thông khả dụng** của mạng.
- **Tắc nghẽn mạng**: Khi quá nhiều gói tin đi qua cùng một liên kết, thông lượng có thể giảm đáng kể.
- **Kiến trúc mạng**: Số lượng router, kiểu kết nối (có dây hay không dây), giao thức sử dụng...

## Công thức tính thông lượng

$$
\text{Throughput}=\frac{F}{T}
$$

Trong đó:
- $F$ là tổng số bit được truyền,
- $T$ là tổng thời gian truyền tải.

> [!example]- Ví dụ
> Nếu bạn tải một file 1 GB (8 × 10⁹ bits) trong 10 giây:
> $$\text{Throughput}=\frac{8\times10^9}{10}=800\mathrm{Mbps}$$

> [!info] Lưu ý
> Nếu mạng bị tắc nghẽn, thông lượng thực tế có thể **thấp hơn rất nhiều** so với giá trị danh nghĩa.

---

# ❓ Câu hỏi thường gặp


> [!question]- Băng thông có phải thông lượng không?
> Không! **Băng thông (Bandwidth)** và **thông lượng (Throughput)** là hai khái niệm khác nhau trong mạng máy tính, dù chúng có liên quan.
> - **Băng thông (B)** là **tốc độ tối đa lý thuyết** mà một kết nối có thể đạt được, đo bằng bps (**bit per second**). Nó giống như **kích thước đường cao tốc** – càng rộng, càng có thể chứa nhiều xe.
> - **Thông lượng (T)** là **tốc độ thực tế** mà dữ liệu truyền qua mạng trong một khoảng thời gian nhất định. Nó bị ảnh hưởng bởi tắc nghẽn mạng, mất gói, độ trễ, v.v.
> 
> Băng thông là giới hạn trên, còn thông lượng thể hiện tốc độ truyền dữ liệu thực tế!


---

# 🔥 Tổng kết
- **Độ trễ mạng** gồm nhiều thành phần: xử lý, xếp hàng, truyền tải và lan truyền.
- **Mất gói** thường xảy ra do tắc nghẽn hoặc lỗi tín hiệu, ảnh hưởng lớn đến hiệu suất mạng.
- **Thông lượng** là tốc độ dữ liệu thực tế, bị ảnh hưởng bởi băng thông và tình trạng tắc nghẽn.

📢 **Bạn đã bao giờ gặp vấn đề về tốc độ mạng hoặc mất kết nối chưa? Hãy chia sẻ trải nghiệm của bạn dưới phần bình luận nhé!** 👇
