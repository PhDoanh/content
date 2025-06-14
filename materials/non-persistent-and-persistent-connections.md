---
date: 2025-03-12
draft: false
status: Done
title: "Không duy trì và duy trì: Chiến lược kết nối HTTP nào hiệu quả hơn?"
description: Khám phá cách thức hoạt động của kết nối không duy trì và kết nối duy trì trong giao thức HTTP. Bài viết này giải thích chi tiết quy trình, ưu nhược điểm, cũng như tác động của từng loại kết nối đến hiệu suất truyền tải dữ liệu qua Internet. 🚀
author: PhDoanh
authorlink: https://github.com/PhDoanh
tags:
  - computer-networking
  - application-layer
  - web
  - http
  - http-connections
aliases:
  - non persistent and persistent connections
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
    src="images/non-persistent-and-persistent-connections.png"
    alt="Không duy trì và duy trì: Chiến lược kết nối HTTP nào hiệu quả hơn?" 
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

Trong nhiều ứng dụng Internet, client và server giao tiếp trong một khoảng thời gian dài qua một chuỗi các yêu cầu và phản hồi. Tùy thuộc vào ứng dụng, các yêu cầu này có thể được gửi liên tiếp, theo chu kỳ hoặc ngắt quãng. Một quyết định quan trọng của lập trình viên là nên sử dụng **kết nối không duy trì** (non-persistent) hay **kết nối duy trì** (persistent) để truyền tải các yêu cầu / phản hồi qua `TCP`.

# Non-persistent connections

^b5634e

**Kết nối không duy trì** là cách thức mà mỗi cặp yêu cầu - phản hồi `HTTP` được gửi qua một kết nối `TCP` riêng biệt. Điều này có nghĩa là sau khi server gửi xong phản hồi, kết nối sẽ bị đóng lại.  

## Quy trình truyền tải

**Bước 1:** Client khởi tạo một kết nối `TCP` đến server (ví dụ: `www.someSchool.edu` trên cổng 80).  
  
> [!info] Lưu ý
> Mỗi kết nối yêu cầu một socket riêng ở cả phía client và server.

**Bước 2:** Client gửi thông điệp `HTTP request` chứa đường dẫn (ví dụ: `/someDepartment/home.index`) đến server.
  
**Bước 3:** Server nhận yêu cầu, truy xuất đối tượng (file HTML) từ bộ nhớ hoặc đĩa, sau đó gửi lại thông điệp `HTTP response` chứa nội dung file.
  
**Bước 4:** Sau khi gửi xong phản hồi, server yêu cầu `TCP` đóng kết nối.  

> [!info] Lưu ý
> Mỗi đối tượng (HTML, JPEG, …) yêu cầu mở và đóng kết nối riêng, gây ra thêm chi phí về tài nguyên và độ trễ.

**Bước 5:** Client nhận phản hồi, đóng kết nối và tiến hành phân tích nội dung. Nếu file HTML chứa tham chiếu đến 10 ảnh JPEG, các bước trên sẽ được lặp lại cho từng ảnh.  Cụ thể, nếu một trang web có 11 đối tượng, sẽ có 11 kết nối `TCP` được tạo ra.

> [!check] Ưu điểm
> - Đơn giản trong thiết kế và triển khai.

> [!missing] Nhược điểm
> - **Chi phí cao** do phải thiết lập và đóng kết nối nhiều lần.
> - **Độ trễ lớn** vì mỗi đối tượng mất ít nhất 2 lần RTT (Round-Trip Time).

---

# Persistent connections

**Kết nối duy trì** cho phép client và server sử dụng **một kết nối `TCP` liên tục** cho nhiều giao dịch. Sau khi server gửi xong phản hồi, kết nối vẫn được mở để phục vụ các yêu cầu tiếp theo.

## Cách thức hoạt động

**Kết nối liên tục:**  
- Một kết nối `TCP` được mở và duy trì cho đến khi không còn hoạt động trong một khoảng thời gian xác định (timeout).  
- Toàn bộ trang web (HTML và các đối tượng đi kèm) có thể được truyền qua cùng một kết nối.

**Pipelining:** Các yêu cầu có thể được gửi liên tiếp mà không cần đợi phản hồi của các yêu cầu trước đó.  Pipelining giúp rút ngắn thời gian chờ, cải thiện hiệu suất truyền tải.

> [!check] Ưu điểm
> - **Tiết kiệm tài nguyên**: Giảm số lượng kết nối `TCP` cần thiết.
> - **Giảm độ trễ:** Loại bỏ thời gian thiết lập kết nối lặp đi lặp lại.

> [!missing] Nhược điểm
> - Cần quản lý timeout và xử lý các vấn đề liên quan đến **sự ổn định của kết nối**.

---

# So sánh hiệu năng

**Thời gian phản hồi:**
Một cách tính ước tính (back-of-the-envelope) về thời gian phản hồi khi sử dụng **kết nối không duy trì** có thể được biểu diễn qua công thức:

$$
T_{\text{total}} = 2\times RTT + T_{\text{trans}}
$$

Trong đó:
- $RTT$: Thời gian round-trip (thời gian đi và về của một gói dữ liệu).
- $T_{\text{trans}}$: Thời gian truyền tải file (thời gian server truyền file qua kết nối).

> [!example]- Ví dụ
> Nếu $RTT = 100ms$ và $T_{\text{trans}} = 50ms$, ta có:  
> $$ T_{\text{total}} = 2 \times 100ms + 50ms = 250ms $$  
> Điều này cho thấy độ trễ của mỗi giao dịch có thể tăng đáng kể khi sử dụng kết nối không duy trì do đối tượng khác phải đợi đối tượng hiện tại tải xong $\rightarrow$ độ trễ hàng đợi 

Trong khi đó, **kết nối duy trì** giảm thiểu số lần phải thiết lập kết nối, giúp giảm tổng thời gian phản hồi cho cả trang web, đặc biệt khi có nhiều đối tượng cần tải.

**Tốc độ và tài nguyên:**  
- Với **non-persistent connections**, mỗi đối tượng cần mở một kết nối mới, dẫn đến việc sử dụng nhiều bộ nhớ và tài nguyên CPU trên server.  
- **Persistent connections** giảm bớt tải này, cho phép server phục vụ nhiều yêu cầu hơn trên cùng một kết nối.

**Đồng thời và pipelining:**  
- Các trình duyệt hiện đại có thể mở từ 5 đến 10 kết nối song song khi sử dụng non-persistent connections.  
- Với persistent connections, việc pipelining cho phép gửi các yêu cầu liên tiếp mà không cần chờ phản hồi, tăng tốc độ tải trang.

**Timeout và quản lý kết nối:**  
- Một điểm cần lưu ý là việc quản lý timeout trong persistent connections. Nếu kết nối bị giữ quá lâu mà không có hoạt động, server có thể đóng kết nối để giải phóng tài nguyên.

---

# Các câu hỏi thường gặp

> [!caution]- Nội dung đang hoàn thiện
> Quá trình xây dựng nội dung này có thể mất nhiều thời gian ⌛, nhưng bạn có thể thúc đẩy nó bằng cách tham gia [[article-collaboration-guide|cộng tác bài viết]] 🤝
> 
> **Rất mong sự thông cảm của các bạn 🙏**

---

# Tổng kết

Qua bài viết, chúng ta đã tìm hiểu:
- **Non-persistent connections**: Mỗi yêu cầu - phản hồi sử dụng một kết nối `TCP` riêng biệt, dẫn đến chi phí thiết lập kết nối cao và độ trễ tăng do phải mất 2 lần RTT cho mỗi giao dịch.
- **Persistent connections**: Cho phép sử dụng một kết nối duy trì cho nhiều giao dịch, giảm thiểu thời gian thiết lập kết nối và cải thiện hiệu năng thông qua **pipelining**.

Việc lựa chọn giữa hai phương pháp này phụ thuộc vào ứng dụng cụ thể và mục tiêu tối ưu hiệu suất. **Hiểu rõ sự khác biệt** giữa chúng sẽ giúp bạn thiết kế các ứng dụng web hiệu quả hơn. Happy coding! 💻✨

