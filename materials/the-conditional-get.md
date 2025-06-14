---
date: 2025-03-12
draft: false
status: Done
title: Tối ưu băng thông với Conditional GET
description: Conditional GET là cơ chế của HTTP giúp cache kiểm tra xem bản sao đã lưu có còn hợp lệ không, từ đó tránh truyền tải lại dữ liệu không cần thiết. Bài viết này giải thích chi tiết cách hoạt động, ví dụ minh họa và lợi ích của Conditional GET trong việc tối ưu hiệu suất mạng. 🚀
author: PhDoanh
authorlink: https://github.com/PhDoanh
tags:
  - computer-networking
  - application-layer
  - web
  - http
  - conditional-get-method
aliases:
  - the conditional get
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
    src="images/the-conditional-get.png"
    alt="Tối Ưu Băng Thông với Conditional GET" 
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

Trong khi **Web Caching** giúp giảm thời gian phản hồi cho người dùng, nó cũng có thể gặp vấn đề với việc lưu trữ các đối tượng cũ (stale). **Conditional GET** là cơ chế cho phép cache xác minh rằng đối tượng của máy chủ vẫn còn cập nhật trước khi phục vụ lại cho client những nội dụng mà nó có, giúp tiết kiệm băng thông và giảm độ trễ.

# Giới thiệu về Conditional GET
**Conditional GET** là một yêu cầu được gửi từ **cache** (có thể là trình duyệt hoặc proxy cache) đến máy chủ để kiểm tra xem phiên bản đã lưu trữ của một đối tượng có còn hợp lệ hay không.

- Nếu đối tượng trên máy chủ **không thay đổi**, máy chủ trả về mã trạng thái **304 Not Modified**, giúp tiết kiệm băng thông vì không cần tải lại dữ liệu.

- Nếu đối tượng **đã thay đổi**, máy chủ trả về mã **200 OK** kèm theo nội dung mới, và cache sẽ cập nhật lại dữ liệu của mình.

**Yêu cầu của Conditional GET:**  
- Phải sử dụng phương thức `GET`.  
- Phải bao gồm header `If-Modified-Since:` với giá trị tương ứng từ header `Last-Modified:` mà máy chủ đã gửi. Tức là nếu lần sửa đổi đối tượng gần đây nhất của server không khớp với thời gian sửa đổi trên cache thì cache sẽ cập nhật lại dữ liệu của mình

---

# Cách hoạt động của Conditional GET

**Bước 1: Yêu cầu ban đầu từ Cache**  

- Cache (thay mặt browser) gửi đi yêu cầu:  
```http
GET /fruit/kiwi.gif HTTP/1.1
Host: www.exotiquecuisine.com
```

- Máy chủ phản hồi với đối tượng kèm header `Last-Modified:`  
```http {4}
HTTP/1.1 200 OK
Date: Sat, 8 Oct 2011 15:39:29
Server: Apache/1.3.0 (Unix)
Last-Modified: Wed, 7 Sep 2011 09:23:24
Content-Type: image/gif
(data ...)
```
  
- Cache lưu trữ đối tượng và ghi nhớ giá trị `Last-Modified: Wed, 7 Sep 2011 09:23:24`.

**Bước 2: Yêu cầu kiểm tra cập nhật từ Cache**  
- Khi có yêu cầu sau này, cache sẽ gửi yêu cầu Conditional GET:  
```http {3}
GET /fruit/kiwi.gif HTTP/1.1
Host: www.exotiquecuisine.com
If-Modified-Since: Wed, 7 Sep 2011 09:23:24
```

- Yêu cầu này thông báo với máy chủ rằng cache chỉ muốn nhận lại đối tượng nếu nó đã được thay đổi sau ngày được ghi nhận.

**Bước 3: Phản hồi từ máy chủ**
- Nếu đối tượng **không thay đổi**, máy chủ phản hồi:  
```http {1}
HTTP/1.1 304 Not Modified
Date: Sat, 15 Oct 2011 15:39:29
Server: Apache/1.3.0 (Unix)
(empty entity body)
```

- Cache tiếp tục phục vụ đối tượng đã lưu cho browser, tránh việc truyền tải lại dữ liệu lớn.

> [!important] Quan trọng
> Nếu máy chủ trả về **304 Not Modified**, nó không kèm theo dữ liệu đối tượng, giúp giảm tải băng thông và cải thiện tốc độ phản hồi.

---

# Ưu nhược điểm của Conditional GET

> [!check] Ưu điểm
> - **Tiết kiệm băng thông:** Tránh việc truyền tải dữ liệu không cần thiết khi đối tượng chưa thay đổi.
> - **Giảm độ trễ:** Phục vụ nhanh hơn từ cache khi dữ liệu đã được xác nhận là hợp lệ.
> - **Tối ưu hiệu suất mạng:** Giảm tải cho máy chủ gốc và giúp hệ thống mạng hoạt động hiệu quả hơn.
> - **Cải thiện trải nghiệm người dùng:** Người dùng nhận được dữ liệu nhanh chóng mà không cần chờ đợi truyền tải dữ liệu lớn.

> [!missing] Nhược điểm
> - **Vẫn phải gửi request**: Dù không tải lại toàn bộ dữ liệu, trình duyệt hoặc proxy cache vẫn phải gửi một HTTP request đến server để kiểm tra tính cập nhật của tài nguyên. Điều này có thể gây **độ trễ không cần thiết** nếu server phản hồi chậm.
> - **Phụ thuộc vào cơ chế Last-Modified và ETag**: Server phải hỗ trợ **Last-Modified** hoặc **ETag** để Conditional GET hoạt động. Một số server không cung cấp thông tin này hoặc cung cấp không chính xác, dẫn đến cache hoạt động kém hiệu quả.
> - **Không xử lý tốt với dữ liệu động**: Đối với các trang web có nội dung thay đổi liên tục (ví dụ: trang tin tức, biểu đồ thời gian thực), **Conditional GET không giúp giảm tải nhiều**, vì hầu hết các yêu cầu vẫn phải tải lại nội dung mới.
> - **Khả năng cache không hiệu quả với dữ liệu lớn**: Nếu server không tối ưu việc kiểm tra **ETag** hoặc **Last-Modified**, thì Conditional GET có thể không giúp tiết kiệm đáng kể băng thông đối với các tệp lớn.

> [!suggest]- Giải pháp cho nhược điểm
> - Kết hợp **Cache-Control: max-age** để giảm số lượng request cần kiểm tra.
> - Tối ưu hóa **ETag** và **Last-Modified** trên server.
> - Đối với dữ liệu ít thay đổi, có thể sử dụng **cache chậm hơn** thay vì cache có Conditional GET.

---

# Các câu hỏi thường gặp

> [!caution]- Nội dung đang hoàn thiện
> Quá trình xây dựng nội dung này có thể mất nhiều thời gian ⌛, nhưng bạn có thể thúc đẩy nó bằng cách tham gia [[article-collaboration-guide|cộng tác bài viết]] 🤝
> 
> **Rất mong sự thông cảm của các bạn 🙏**

---

# Tổng kết

**Conditional GET** là một **cơ chế thông minh** trong HTTP giúp kiểm tra tính cập nhật của dữ liệu đã được cache, đảm bảo rằng người dùng luôn nhận được nội dung mới nhất khi cần, đồng thời tiết kiệm băng thông và giảm độ trễ.  
- **Quy trình hoạt động:** Từ yêu cầu ban đầu, lưu trữ `Last-Modified` đến việc gửi Conditional GET với header `If-Modified-Since`.  
- **Lợi ích:** Tiết kiệm băng thông, giảm tải cho máy chủ, và cải thiện trải nghiệm người dùng.  
- **Mẹo:** Luôn thiết lập chính sách caching hợp lý để tối ưu hóa quá trình kiểm tra và làm mới dữ liệu.

Happy caching! 💻✨
