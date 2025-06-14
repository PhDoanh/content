---
date: 2025-03-12
draft: false
status: Done
title: "Định dạng thông điệp HTTP: Hiểu sâu về Request và Response"
description: Khám phá cấu trúc của thông điệp HTTP với phần giải thích chi tiết về HTTP Request Message và HTTP Response Message. Bài viết này cung cấp ví dụ minh họa, phân tích các header quan trọng và mẹo thực hành qua Telnet để bạn hiểu rõ hơn về giao thức HTTP. 🚀
author: PhDoanh
authorlink: https://github.com/PhDoanh
tags:
  - computer-networking
  - application-layer
  - web
  - http
  - http-message
aliases:
  - http message format
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
    src="images/http-message-format.png"
    alt="Định dạng thông điệp HTTP: Hiểu sâu về Request và Response" 
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

Trong các đặc tả **HTTP** như [RFC 1945](https://www.rfc-editor.org/rfc/rfc1945.txt) và [RFC 2616](https://www.rfc-editor.org/rfc/rfc2616.txt), định dạng của các thông điệp HTTP được chia thành hai loại chính: **HTTP Request Message** và **HTTP Response Message**. Bài viết này sẽ cùng bạn khám phá chi tiết về cấu trúc, các thành phần cũng như cách hoạt động của từng loại thông điệp.

# HTTP Request Message

**HTTP Request Message** là thông điệp do client gửi tới server để yêu cầu truy cập một đối tượng trên web. Thông điệp này được viết bằng văn bản ASCII, giúp con người dễ dàng đọc và hiểu. Dưới đây là một ví dụ điển hình:

```http
GET /somedir/page.html HTTP/1.1 
Host: [www.someschool.edu](http://www.someschool.edu) 
Connection: close 
User-agent: Mozilla/5.0 
Accept-language: fr
```

**Trong đó:**

**Request line**: Dòng đầu tiên của thông điệp, chứa 3 trường:
- **Phương thức (method)**: Ví dụ như **GET**, **POST**, **HEAD**, **PUT**, **DELETE**. Hầu hết các yêu cầu truy xuất trang web sử dụng phương thức **GET**.  
- **URL**: Đường dẫn đến đối tượng yêu cầu (ví dụ: `/somedir/page.html`).
- **Phiên bản HTTP**: Ví dụ **HTTP/1.1**.

**Header lines**: Các dòng sau dòng đầu chứa thông tin bổ sung:
- **Host**: Xác định tên máy chủ chứa đối tượng, rất cần thiết cho các bộ nhớ đệm proxy.
- **Connection**: Ví dụ `close` cho biết client yêu cầu server đóng kết nối sau khi gửi phản hồi.
- **User-agent**: Cho biết loại trình duyệt hoặc client gửi yêu cầu (ví dụ: **Mozilla/5.0**).
- **Accept-language**: Cho biết ngôn ngữ ưu tiên (ví dụ: `fr` cho tiếng Pháp).

**Entity body**: Phần thân của thông điệp. Với phương thức **GET**, phần này thường rỗng; nhưng với **POST**, nó chứa dữ liệu từ form do người dùng nhập.

## Các phương thức HTTP
**Phương thức HTTP** (HTTP Methods) là các phương thức mà client sử dụng để yêu cầu các hành động khác nhau từ máy chủ khi giao tiếp qua giao thức HTTP. Các phương thức phổ biến bao gồm `GET` (lấy tài nguyên), `POST` (gửi dữ liệu), `PUT` (cập nhật dữ liệu), và `DELETE` (xóa dữ liệu). Mỗi phương thức có mục đích và cách thức sử dụng riêng biệt trong việc tương tác với tài nguyên trên máy chủ.

Dưới đây là một số các phương thức HTTP phổ biến:
- **GET**: Dùng để yêu cầu truy xuất đối tượng.
- **POST**: Thường dùng khi người dùng nhập dữ liệu vào form, dữ liệu này sẽ được gửi trong phần entity body.
- **HEAD**: Tương tự như GET nhưng server không gửi phần thân của thông điệp, hữu ích cho mục đích kiểm tra.
- **PUT**: Dùng để tải một đối tượng nên server, thường áp dụng trong các công cụ xuất bản web.
- **DELETE**: Cho phép xóa đối tượng trên server.

> [!info] Lưu ý
> Dữ liệu trong form không nhất thiết luôn được gửi bằng phương thức **POST**; nhiều khi **GET** được sử dụng kèm theo dữ liệu dưới dạng tham số trong URL. Ví dụ: `www.somesite.com/animalsearch?monkeys&bananas`, tức là yêu cầu lấy dữ liệu động vật từ server với dữ liệu tải lên là `monkeys` và `bananas` 

---

# HTTP Response Message

**HTTP Response Message** là thông điệp do server gửi về client để phản hồi yêu cầu. Thông điệp này bao gồm 3 phần chính: status line, header lines và entity body. Một ví dụ về HTTP Response Message như sau:

```http
HTTP/1.1 200 OK 
Connection: close 
Date: Tue, 09 Aug 2011 15:44:04 GMT 
Server: Apache/2.2.3 (CentOS) 
Last-Modified: Tue, 09 Aug 2011 15:11:03 GMT 
Content-Length: 6821 
Content-Type: text/html 

(data data data data data ...)
```

**Trong đó:**

**Status line**: Dòng đầu của thông điệp chứa:
- **Phiên bản HTTP**: Ví dụ **HTTP/1.1**.
- **Mã trạng thái (status code)**: Ví dụ **200**.
- **Thông điệp trạng thái (status phrase)**: Ví dụ **OK**.

**Header lines**: Các dòng cung cấp thông tin chi tiết về phản hồi:
- **Connection**: Cho biết rằng server sẽ đóng kết nối sau khi gửi dữ liệu.
- **Date**: Thời gian và ngày giờ mà phản hồi được tạo và gửi.
- **Server**: Thông tin về phần mềm server (ví dụ: **Apache/2.2.3 (CentOS)**).
- **Last-Modified**: Thời điểm tạo hoặc chỉnh sửa gần đây nhất của đối tượng.
- **Content-Length**: Kích thước của đối tượng được gửi (tính bằng số byte).
- **Content-Type**: Loại nội dung của đối tượng (ví dụ: `text/html`).

**Entity body**: Phần chứa nội dung chính của đối tượng, chẳng hạn như mã HTML của trang web.

## Các mã trạng thái HTTP phổ biến
**Mã trạng thái HTTP** (HTTP Status Codes) là các mã số được máy chủ trả về trong các phản hồi HTTP để chỉ báo kết quả của yêu cầu mà trình duyệt hoặc client gửi đến. Những mã này cung cấp thông tin về việc yêu cầu có thành công hay không, nếu không, lỗi là gì và cần làm gì tiếp theo.

- **200 OK**: Yêu cầu thành công và thông tin được trả về.
- **301 Moved Permanently**: Đối tượng đã được chuyển đến URL mới; thông tin chuyển hướng được cung cấp trong header **Location**.
- **400 Bad Request**: Yêu cầu không hợp lệ do cú pháp sai.
- **404 Not Found**: Đối tượng yêu cầu không tồn tại trên server.
- **505 HTTP Version Not Supported**: Phiên bản HTTP được yêu cầu không được server hỗ trợ.

---

# Hướng dẫn thực hành với Telnet

Để xem trực tiếp **HTTP Response Message**, bạn có thể sử dụng công cụ **Telnet** theo các bước sau:

1. Mở cửa sổ dòng lệnh và kết nối tới server:
```sh
telnet cis.poly.edu 80
```

2. Gõ lệnh yêu cầu, ví dụ:
```sh
GET /~ross/ HTTP/1.1
Host: cis.poly.edu
```

3. Nhấn **Enter** hai lần để gửi yêu cầu.

> [!tip]- Mẹo
> Sử dụng **HEAD** thay vì **GET** nếu bạn chỉ muốn xem thông tin header mà không nhận dữ liệu đối tượng. Vì dữ liệu phần thân `Entity body` có thể rất khổng lồ!

Việc thực hành này giúp bạn **nhìn trực tiếp** vào cách mà HTTP request và response được hình thành và xử lý bởi server.

---

# Các câu hỏi thường gặp

> [!caution]- Nội dung đang hoàn thiện
> Quá trình xây dựng nội dung này có thể mất nhiều thời gian ⌛, nhưng bạn có thể thúc đẩy nó bằng cách tham gia [[article-collaboration-guide|cộng tác bài viết]] 🤝
> 
> **Rất mong sự thông cảm của các bạn 🙏**

---

# Tổng kết

Qua bài viết này, chúng ta đã cùng nhau khám phá:

- **HTTP Request Message**: Cấu trúc gồm request line, header lines và (nếu cần) entity body, kèm theo phân tích các phương thức như **GET**, **POST**, **HEAD**, **PUT** và **DELETE**.
- **HTTP Response Message**: Gồm status line, header lines và entity body, với các mã trạng thái quan trọng như **200 OK**, **404 Not Found**.
- Hướng dẫn thực hành đơn giản qua **Telnet** để xem trực tiếp các thông điệp HTTP.

Việc hiểu rõ định dạng của **thông điệp HTTP** không chỉ giúp bạn debug và tối ưu hóa ứng dụng web mà còn nắm bắt được cách thức giao tiếp cơ bản giữa **client** và **server**. Happy coding! 💻✨