---
date: 2025-03-13
draft: false
status: Done
title: Định dạng thông điệp trong Mail
description: "Bài viết này khám phá cấu trúc mail message theo tiêu chuẩn RFC 5322, từ cách định dạng header cho đến cách sử dụng telnet để gửi email. Tìm hiểu ngay những mẹo và lưu ý quan trọng!"
author: PhDoanh
authorlink: https://github.com/PhDoanh
tags:
  - computer-networking
  - application-layer
  - web
  - email
  - smtp
  - mail-formats
aliases:
  - mail message formats
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
    src="images/mail-message-formats.png"
    alt="Định dạng thông điệp trong Mail" 
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

Trong thời đại số hóa, email không chỉ là phương tiện truyền tải thông tin mà còn là sản phẩm của một **cấu trúc chuẩn** giúp đảm bảo độ chính xác và hiệu quả trong giao tiếp. Bài viết này sẽ giúp bạn hiểu rõ về cấu trúc của header trong email theo **RFC 5322**, cách phân tách header với nội dung chính (body), cũng như hướng dẫn cơ bản cách gửi email qua `telnet`. 📧✨

# Giới thiệu

Email được xây dựng dựa trên cấu trúc tương tự như một lá thư thông thường, trong đó phần **header** chứa các thông tin phụ trợ như địa chỉ người gửi, người nhận và chủ đề của thư. Những thông tin này giúp máy chủ và ứng dụng email xử lý thư một cách chính xác.

- **RFC 5322**: Tiêu chuẩn quy định định dạng và ý nghĩa của các dòng header.
- **SMTP**: Giao thức truyền tải email, khác với header email mặc dù có một số từ khóa chung.
- **Telnet**: Công cụ kết nối tới máy chủ email qua cổng `25` để thực hiện việc gửi thư.

---

# Cấu trúc của header email

Header email bao gồm nhiều dòng, mỗi dòng có định dạng `keyword: value` theo chuẩn **RFC 5322**, trong đó một số header là bắt buộc và một số là tùy chọn. Dưới đây là một số thành phần của header:

| Header                            | Ý nghĩa                                                                                              | Bắt buộc? |
| --------------------------------- | ---------------------------------------------------------------------------------------------------- | --------- |
| **From**                          | Địa chỉ email của người gửi. Giống như tên người gửi trên thư tay.                                   | Có        |
| **To**                            | Địa chỉ email của người nhận. Giống như người nhận thư.                                              | Có        |
| **Date**                          | Ngày giờ gửi email, giúp biết khi nào email được tạo ra.                                             | Có        | 
| **Subject**                       | Tiêu đề email, giúp người nhận biết nội dung chính mà không cần mở.                                  | Không     |
| **CC** (Carbon Copy)              | Gửi bản sao email cho nhiều người **(những người này đều thấy nhau)**.                               | Không     |
| **BCC** (Blind Carbon Copy)       | Gửi bản sao email nhưng **người trong BCC không thấy nhau**.                                         | Không     |
| **Reply-To**                      | Địa chỉ nhận phản hồi, dùng khi muốn trả lời email đến một địa chỉ khác thay vì "From".              | Không     |
| **Message-ID**                    | Mã định danh duy nhất cho mỗi email, giúp theo dõi email trong hệ thống.                             | Không     |
| **MIME-Version**                  | Xác định phiên bản MIME, cần thiết khi gửi email có **hình ảnh, tệp đính kèm, hoặc HTML**.           | Không     |
| **Content-Type**                  | Xác định loại nội dung email, có thể là **văn bản thuần túy, HTML hoặc có tệp đính kèm**.            | Không     |
| **DKIM-Signature**                | Chữ ký xác thực giúp **ngăn chặn email giả mạo**, xác minh email từ đúng nguồn.                      | Không     |
| **SPF (Sender Policy Framework)** | Kiểm tra xem email có được gửi từ **máy chủ hợp lệ** không (giúp chống spam).                        | Không     |
| **Received**                      | Lịch sử máy chủ đã chuyển tiếp email, giúp kiểm tra email đi qua đâu trước khi đến tay người nhận.   | Không     |
| **Return-Path**                   | Địa chỉ nhận phản hồi nếu email bị lỗi hoặc không gửi được.                                          | Không     |
| **Disposition-Notification-To**   | Yêu cầu gửi thông báo khi người nhận **đọc hoặc xử lý** email (tương tự như "đã xem" trên tin nhắn). | Không     |

> [!example]- Ví dụ
> ```txt
> From: alice@crepes.fr
> To: bob@hamburger.edu
> Subject: Searching for the meaning of life.
> 
> (body content)
> ```

> [!info] Lưu ý
> - Sau phần header, có một dòng trống (CRLF) để phân tách với nội dung chính (body) của email. Quá trình này có thể được hiện bằng cách 
> - Header của email không phải là các lệnh của giao thức **SMTP**. Dù chúng có chứa các từ khóa tương tự, nhưng chúng phục vụ mục đích khác nhau: header là một phần của thông điệp, còn SMTP là giao thức truyền tải.

> [!caution] Cảnh báo
> Việc nhầm lẫn giữa header email và lệnh SMTP có thể dẫn đến lỗi trong quá trình gửi và xử lý email. Hãy đảm bảo rằng bạn luôn kiểm tra kỹ định dạng trước khi thực hiện giao dịch.

---

# Sử dụng Telnet để gửi email
`telnet` là công cụ hữu ích để kết nối trực tiếp đến máy chủ email và thử nghiệm quá trình gửi thư.

**Bước 1: Kết nối đến máy chủ SMTP**: Sử dụng lệnh `telnet` để kết nối tới máy chủ SMTP. Ở đây, chúng ta sử dụng địa chỉ giả định `server.example.com` và cổng `25`.

```sh
telnet server.example.com 25
```

```txt title="Đầu ra"
220 server.example.com ESMTP Postfix
```

**Bước 2: Giới thiệu với máy chủ qua lệnh `HELO`**: Gửi lệnh `HELO` kèm theo tên miền của bạn để máy chủ nhận biết danh tính của bạn. Lệnh này là bước bắt đầu cho phiên giao tiếp SMTP.

```sh
HELO mydomain.com
```

```txt title="Đầu ra"
250 server.example.com Hello mydomain.com, pleased to meet you
```

**Bước 3: Xác định địa chỉ người gửi với lệnh `MAIL FROM`**: Gửi lệnh `MAIL FROM` để thông báo địa chỉ email của người gửi. Địa chỉ này phải nằm trong định dạng `<user@example.com>`.

```sh
MAIL FROM:<alice@example.com>
```

```txt title="Đầu ra"
250 OK
```

**Bước 4: Xác định địa chỉ người nhận với lệnh `RCPT TO`**: Sử dụng lệnh `RCPT TO` để chỉ định địa chỉ email của người nhận. Tương tự, địa chỉ được đặt trong dấu `< >`.

```sh
RCPT TO:<bob@example.com>
```

```txt title="Đầu ra"
250 Accepted
```

**Bước 5: Bắt đầu nhập nội dung email với lệnh `DATA`**: Lệnh `DATA` báo cho máy chủ biết rằng bạn sẽ gửi nội dung email (bao gồm header và body). Máy chủ sẽ trả về thông báo yêu cầu bạn nhập dữ liệu, kết thúc bằng một dòng chứa chỉ dấu `.`.

```sh
DATA
```

```txt title="Đầu ra"
354 End data with <CR><LF>.<CR><LF>
```

**Bước 6: Nhập header và nội dung email**: Nhập các dòng header theo định dạng `keyword: value` (theo **RFC 5322/RFC 5323**) và sau đó là một dòng trống để phân cách với nội dung (body) của email.

```sh
From: alice@example.com
To: bob@example.com
Subject: Test email via Telnet
Date: Thu, 13 Mar 2025 10:00:00 +0700

Hello Bob,
This is a test email sent via Telnet command.
.
```

**Bước 7: Kết thúc phiên giao tiếp với lệnh `QUIT`**: Sau khi email đã được gửi, sử dụng lệnh `QUIT` để kết thúc phiên làm việc với máy chủ SMTP.

```sh
QUIT
```

```txt title="Đầu ra"
221 Bye
```

> [!tip]- Mẹo
> Trước khi gửi, hãy kiểm tra kỹ các thông tin như địa chỉ email và định dạng header để đảm bảo không có lỗi nào phát sinh trong quá trình gửi thư. 👍

---

# Các câu hỏi thường gặp

> [!caution]- Nội dung đang hoàn thiện
> Quá trình xây dựng nội dung này có thể mất nhiều thời gian ⌛, nhưng bạn có thể thúc đẩy nó bằng cách tham gia [[article-collaboration-guide|cộng tác bài viết]] 🤝
> 
> **Rất mong sự thông cảm của các bạn 🙏**

---

# Tổng kết

Qua bài viết này, chúng ta đã cùng nhau khám phá:

- **Giới thiệu** về cấu trúc email và vai trò của header.
- **Chi tiết cấu trúc** header email theo tiêu chuẩn **RFC 5322** với định dạng `keyword: value`.
- **Hướng dẫn sử dụng `telnet`** để gửi email, đảm bảo bạn nắm bắt được quy trình gửi thư chuẩn.

Việc hiểu và áp dụng đúng cấu trúc **mail message formats** không chỉ giúp bạn gửi email đúng chuẩn mà còn đảm bảo thông tin được xử lý một cách hiệu quả và an toàn. **Hãy luôn chú ý đến định dạng và các lưu ý quan trọng** để trải nghiệm gửi email mượt mà và chính xác! 🚀

