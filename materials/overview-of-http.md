---
date: 2025-03-12
draft: false
status: Done
title: "HTTP: Nền tảng vô hạn của Web"
description: Khám phá cách thức hoạt động của giao thức `HTTP` – nền tảng của Web hiện đại. Bài viết này cung cấp tổng quan, kiến trúc client-server, cách giao tiếp và các lưu ý quan trọng khi truyền tải dữ liệu qua Internet.
author: PhDoanh
authorlink: https://github.com/PhDoanh
tags:
  - computer-networking
  - application-layer
  - web
  - http
aliases:
  - overview of http
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
    src="images/overview-of-http.png"
    alt="HTTP: Nền tảng vô hạn của Web" 
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

**HTTP (HyperText Transfer Protocol)** là giao thức tầng ứng dụng được thiết kế cho việc truyền tải siêu văn bản trên Web. Được định nghĩa trong [RFC 1945](https://www.rfc-editor.org/rfc/rfc1945.txt) và [RFC 2616](https://www.rfc-editor.org/rfc/rfc2616.txt), **HTTP** đóng vai trò then chốt trong việc trao đổi dữ liệu giữa các chương trình **client** (như các trình duyệt web: `Internet Explorer`, `Firefox`, …) và **server** (ví dụ: `Apache`, `Microsoft IIS`, …). 🚀

# Giới thiệu về HTTP

`HTTP` cho phép một đối tượng – thường là một file như HTML, hình ảnh JPEG, video clip, … – được truy cập thông qua một URL duy nhất.  
**Một số điểm chính:**

- **Đối tượng**: File được lưu trữ trên server và có thể là văn bản, hình ảnh, video hoặc các ứng dụng nhỏ.

- **URL** gồm 2 thành phần chính:
	- **Hostname**: Tên miền của server (ví dụ: `www.someSchool.edu`).
	- **Path name**: Đường dẫn đến file (ví dụ: `/someDepartment/picture.gif`).

> [!info] Lưu ý
> Một trang web thường bao gồm một file HTML chính cùng với các đối tượng phụ (hình ảnh, CSS, JavaScript, …).

---

# Kiến trúc client-server của HTTP

`HTTP` được thực hiện thông qua hai chương trình:

- **Client**: Thường là trình duyệt web, thực hiện việc gửi yêu cầu (`HTTP request`) đến server.

- **Server**: Lưu trữ các đối tượng và phản hồi yêu cầu của client thông qua các thông điệp (`HTTP response`).

> [!example] Ví dụ
> Khi bạn click vào một liên kết, trình duyệt sẽ gửi yêu cầu đến server để lấy về file HTML và các đối tượng kèm theo trong liên kết đó

> [!tip] Mẹo
>  Sử dụng các công cụ như `curl` hoặc `Postman` để kiểm tra và debug các yêu cầu `HTTP` từ phía client.

---

# Cách thức hoạt động của HTTP

Quá trình giao tiếp `HTTP` dựa trên giao thức `TCP` để đảm bảo dữ liệu được truyền tải một cách **đáng tin cậy**.  

**Quy trình hoạt động:**

1. **Thiết lập kết nối:** Client khởi tạo kết nối `TCP` đến server thông qua giao diện socket.

2. **Gửi yêu cầu:** Sau khi kết nối được thiết lập, client gửi các thông điệp `HTTP request` chứa thông tin cần truy cập.

3. **Nhận phản hồi:** Server nhận yêu cầu, xử lý và gửi lại `HTTP response` chứa dữ liệu (đối tượng) về client.


> [!info] Lưu ý
> - Giao thức `TCP` đảm bảo mỗi thông điệp được gửi đi đều đến đích một cách đầy đủ và đúng thứ tự.  
> - Nếu có sự cố trong quá trình truyền tải, `TCP` sẽ chịu trách nhiệm xử lý lỗi và khôi phục dữ liệu.

---

# Tính không lưu trạng thái của HTTP

Một đặc điểm quan trọng của `HTTP` là tính **stateless** (không lưu trạng thái).  
Điều này có nghĩa là:

- Server không lưu trữ thông tin về trạng thái của client sau khi xử lý yêu cầu.

- Mỗi yêu cầu được xử lý độc lập, ngay cả khi cùng client yêu cầu cùng một đối tượng nhiều lần.

> [!important] Quan trọng
> Tính không lưu giúp server xử lý số lượng lớn yêu cầu từ nhiều client cùng lúc nhưng đồng thời cũng đòi hỏi các cơ chế bổ sung (như cookies, session) để duy trì trạng thái khi cần thiết.

---

# Các câu hỏi thường gặp

> [!caution]- Nội dung đang hoàn thiện
> Quá trình xây dựng nội dung này có thể mất nhiều thời gian ⌛, nhưng bạn có thể thúc đẩy nó bằng cách tham gia [[article-collaboration-guide|cộng tác bài viết]] 🤝
> 
> **Rất mong sự thông cảm của các bạn 🙏**

---

# Tổng kết

Qua bài viết này, chúng ta đã cùng nhau khám phá **tổng quan về `HTTP`** – giao thức chủ đạo của Web.  
- **HTTP** định nghĩa cách thức các **client** và **server** trao đổi thông tin thông qua các thông điệp được gửi qua kết nối `TCP`.  
- Kiến trúc **client-server** cho phép xử lý hàng triệu yêu cầu một cách độc lập, nhờ vào đặc tính **stateless** của giao thức.  
- Các công thức tính toán đơn giản giúp ta hiểu rõ hơn về số lượng đối tượng trong trang web và thời gian truyền tải dữ liệu.

> [!tip] Mẹo
> Để tối ưu hiệu suất của các ứng dụng web, hãy cân nhắc việc giảm số lượng đối tượng và tối ưu thời gian phản hồi của server.

Hy vọng bài viết đã cung cấp cho bạn **cái nhìn toàn diện** về `HTTP` và cách thức hoạt động của nó trong hệ sinh thái Web hiện đại. Happy coding! 💻✨
