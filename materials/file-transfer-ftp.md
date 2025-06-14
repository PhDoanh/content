---
date: 2025-03-12
draft: false
status: Done
title: "File Transfer Protocol: Giao thức truyền tải tệp tin truyền thống và hiệu quả"
description: "Khám phá cơ chế hoạt động của FTP: từ việc thiết lập kết nối TCP song song (control và data) cho đến các lệnh FTP phổ biến. Bài viết này cũng so sánh FTP với HTTP và trình bày ưu, nhược điểm của FTP trong quản lý phiên làm việc."
author: PhDoanh
authorlink: https://github.com/PhDoanh
tags:
  - computer-networking
  - application-layer
  - web
  - http
  - file-transfer
  - ftp
aliases:
  - file transfer ftp
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
    src="images/file-transfer-ftp.png"
    alt="File Transfer Protocol: Giao thức truyền tải tệp tin truyền thống và hiệu quả" 
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

**FTP (File Transfer Protocol)** là một giao thức truyền tải tệp tin truyền thống, cho phép người dùng chuyển tệp tin giữa máy khách và máy chủ thông qua các kết nối TCP. Giao thức này không chỉ hỗ trợ quá trình chuyển tệp tin mà còn cho phép quản lý thư mục và thực hiện các lệnh điều khiển từ xa.

# Giới thiệu về FTP
**FTP (File Transfer Protocol)** là một giao thức mạng được sử dụng để truyền tải tệp tin giữa các máy tính qua mạng TCP/IP. Nó hoạt động với hai kết nối TCP: một cho việc điều khiển và một cho việc truyền tải dữ liệu, cho phép người dùng tải lên, tải xuống và quản lý tệp tin từ xa một cách hiệu quả.

Trong quá trình kết nối FTP, người dùng phải cung cấp thông tin xác thực để có thể truy cập vào tài khoản từ xa. Cụ thể, khi người dùng kết nối đến máy chủ FTP, họ sẽ cần cung cấp **tên người dùng** (username) và **mật khẩu** (password). Các thông tin này được gửi qua kết nối điều khiển FTP (control connection) để xác thực người dùng trước khi có thể thực hiện các thao tác truyền tệp tin.

> [!info] Lưu ý
> **Thông tin xác thực** giúp đảm bảo rằng chỉ những người có quyền truy cập mới có thể thực hiện các thao tác như tải lên, tải xuống, hoặc quản lý các tệp tin trên máy chủ từ xa.

**Ứng dụng của FTP**:
- **Chuyển tệp tin**: FTP được sử dụng phổ biến để chuyển tệp tin giữa các máy tính hoặc giữa máy tính và máy chủ từ xa qua mạng.
- **Quản lý tệp tin từ xa**: Dùng để quản lý, sao chép, di chuyển hoặc xóa tệp tin trên máy chủ từ xa.
- **Dùng trong hosting web**: FTP là công cụ chính để upload và quản lý tệp tin trên các máy chủ web.
- **Chuyển tệp tin lớn**: Thường dùng cho việc truyền tải các tệp có kích thước lớn mà không bị giới hạn nhiều về kích thước như các công cụ email.

---

# Cơ chế hoạt động của FTP

## Thiết lập kết nối và xác thực

**Kết nối TCP:** Người dùng nhập hostname của máy chủ từ xa, từ đó **FTP client** trên máy cục bộ sẽ thiết lập một kết nối TCP đến **FTP server** trên máy chủ từ xa. Kết nối điều khiển sẽ được thiết lập trên **port 21**.

**Xác thực người dùng:** Sau khi kết nối, người dùng cung cấp **user identification** và **password** (gọi chung là thông tin xác thực) qua kết nối điều khiển dưới dạng các lệnh FTP.

## Các kết nối trong FTP

### Kết nối điều khiển (Control Connection)

**Chức năng:**  
- Dùng để gửi và nhận các lệnh điều khiển như xác thực, thay đổi thư mục, và các lệnh chuyển tệp tin.
- **Luôn được giữ mở** trong suốt phiên làm việc của người dùng.

**Đặc điểm:**  
- Sử dụng cổng 21.
- Truyền tải thông tin dưới dạng lệnh (7-bit ASCII), dễ đọc và hiểu.

### Kết nối dữ liệu (Data Connection)

**Chức năng:**  
- Được sử dụng để truyền tải **tệp tin** giữa máy khách và máy chủ.
- Mỗi lần chuyển tệp tin, FTP sẽ thiết lập một kết nối dữ liệu mới.

**Đặc điểm:**
- Sử dụng cổng 20 (hoặc một cổng động khác tùy theo cấu hình).
- Là kết nối **[[non-persistent-and-persistent-connections#^b5634e|non-persistent]]**, nghĩa là sau khi chuyển xong tệp tin thì kết nối này sẽ bị đóng lại.

> [!caution] Cảnh báo
> Việc sử dụng hai kết nối song song (một cho điều khiển và một cho dữ liệu) yêu cầu FTP phải duy trì trạng thái của phiên làm việc, điều này làm cho FTP **stateful**. Do đó, số phiên làm việc mà FTP có thể duy trì cùng lúc bị giới hạn bởi khả năng lưu trữ trạng thái của máy chủ.

---

# So sánh FTP và HTTP

| Đặc điểm                   | HTTP                                                                                                                                       | FTP                                                                                                                                                                      |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Mục đích sử dụng**       | - Truyền tải dữ liệu siêu văn bản cho việc truy cập web  <br>- Hỗ trợ giao tiếp giữa client và server thông qua các lệnh như `GET`, `POST` | - Chuyển file giữa các hệ thống máy tính  <br>- Dùng để upload/download tập tin                                                                                          |
| **Cổng mặc định**          | - 80                                                                                                                                       | - 21 (kênh điều khiển)  <br>- 20 (kênh truyền dữ liệu)                                                                                                                   | 
| **Kiểu kết nối**           | - Không trạng thái (stateless): mỗi yêu cầu là độc lập và không lưu trữ thông tin phiên làm việc                                           | - Có trạng thái (stateful): phiên kết nối được duy trì giữa các lệnh truyền tải tập tin                                                                                  |
| **Phương thức truyền tải** | - Mô hình `request/response`: client gửi yêu cầu, server phản hồi  <br>- Hỗ trợ nhiều phương thức như `GET`, `POST`, `PUT`, `DELETE`       | - Sử dụng hai kênh riêng biệt:  <br>- **Command Channel**: gửi lệnh và nhận phản hồi (ví dụ: `LIST`, `RETR`, `STOR`)  <br>- **Data Channel**: truyền tải dữ liệu tập tin |
| **Bảo mật**                | - Bản chất không bảo mật  <br>- Có thể nâng cấp lên bảo mật qua HTTPS (sử dụng SSL/TLS)                                                    | - Bản chất không bảo mật  <br>- Có thể nâng cấp lên FTPS hoặc SFTP để tăng cường bảo mật                                                                                 |
| **Ứng dụng phổ biến**      | - Duyệt web  <br>- Giao tiếp API  <br>- Truyền tải dữ liệu web                                                                             | - Chuyển file giữa máy chủ và máy khách  <br>- Quản lý file trên máy chủ                                                                                                 |

> [!tip]- Mẹo
> Nếu bạn chỉ cần truyền tải các trang web hoặc dữ liệu có kích thước nhỏ, HTTP có thể là lựa chọn tối ưu nhờ tính chất [[overview-of-http#Tính không lưu trạng thái của HTTP|stateless]], giúp hệ thống mở rộng dễ dàng hơn.

---

# Các lệnh FTP và phản hồi của nó

Các lệnh FTP được gửi qua kết nối điều khiển ở định dạng 7-bit ASCII, kết thúc bằng CRLF (Carriage Return và Line Feed). Một số lệnh FTP phổ biến gồm:

- **USER username:** Gửi thông tin nhận dạng người dùng.
- **PASS password:** Gửi mật khẩu người dùng.
- **LIST:** Yêu cầu danh sách tệp tin trong thư mục hiện tại của máy chủ. (Danh sách được gửi qua kết nối dữ liệu mới)
- **RETR filename:** Tải tệp tin từ máy chủ về máy khách.
- **STOR filename:** Tải tệp tin từ máy khách lên máy chủ.

Các lệnh này được trả lời bằng các mã số ba chữ số, tương tự như cấu trúc của [[http-message-format#Các mã trạng thái HTTP phổ biến|HTTP status code]]. Một số ví dụ:

- **331:** Username OK, cần mật khẩu.
- **125:** Kết nối dữ liệu đã mở; quá trình chuyển tệp tin bắt đầu.
- **425:** Không thể mở kết nối dữ liệu.
- **452:** Lỗi khi ghi tệp tin.

> [!info] Lưu ý
> - **FTP bản chất là giao thức CLI** vì sử dụng tập lệnh ASCII 7-bit để giao tiếp. Tuy nhiên, **có thể dùng GUI** (như FileZilla, WinSCP) để tạo giao diện trực quan, giúp người dùng thao tác mà không cần nhập lệnh ASCII trực tiếp.
> - Việc hiểu rõ các lệnh FTP và mã phản hồi giúp quản trị viên hệ thống dễ dàng phát hiện lỗi và tối ưu hóa quá trình truyền tải tệp tin.

---

# Các câu hỏi thường gặp

> [!question]- FTP có còn được sử dụng phổ biến không?
> FTP là một **giao thức truyền thống** và hiện nay có nhiều công nghệ mới thay thế, nhưng nó vẫn được sử dụng trong một số trường hợp cụ thể.
>
> **Những hạn chế của FTP**:
> - **Không bảo mật**: FTP truyền dữ liệu dưới dạng **plain text** (không mã hóa), dễ bị tấn công `man-in-the-middle (MITM)`.
> - **Không hỗ trợ bảo mật mặc định**: Phải sử dụng **FTPS (FTP Secure)** hoặc **SFTP (SSH File Transfer Protocol)** để có mã hóa.
> - **Bị hạn chế trong một số hệ thống mới**: Các trình duyệt hiện đại **không còn hỗ trợ FTP** (Chrome, Firefox đã loại bỏ FTP).
>
> **Các công nghệ thay thế FTP**:
> - **SFTP (SSH File Transfer Protocol)**: Bảo mật tốt hơn, sử dụng SSH để mã hóa dữ liệu.
> - **FTPS (FTP Secure - FTP + SSL/TLS)**: Hỗ trợ bảo mật qua SSL/TLS nhưng vẫn giữ mô hình FTP.
> - **WebDAV (Web-based Distributed Authoring and Versioning)**: Hỗ trợ làm việc với file trực tiếp qua HTTP/HTTPS.
> - **Cloud Storage (Google Drive, OneDrive, Dropbox, AWS S3)**: Dễ sử dụng, có giao diện web, bảo mật cao hơn.
> - **Rsync (Remote Sync)**: Hiệu quả cho việc đồng bộ file giữa các máy chủ Linux.

---

# Tổng kết

**FTP** là một giao thức truyền tải tệp tin mạnh mẽ, cho phép chuyển tệp tin giữa máy khách và máy chủ từ xa thông qua hai kết nối TCP: **Control Connection** (dùng cho lệnh điều khiển) và **Data Connection** (dùng cho truyền tải tệp tin).

> [!check] Ưu điểm
> - Hỗ trợ truyền tải tệp tin lớn và nhiều tệp tin.
> - Cho phép quản lý thư mục và kiểm soát quá trình truyền tải.

> [!missing] Nhược điểm
> - Do tính chất stateful nên số phiên làm việc đồng thời bị hạn chế.
> - Cấu hình và quản lý phức tạp hơn so với các giao thức stateless như HTTP.

Việc so sánh giữa FTP và HTTP giúp bạn lựa chọn giao thức phù hợp với nhu cầu: FTP thích hợp cho truyền tải tệp tin, trong khi HTTP phù hợp với các ứng dụng web. Happy transferring! 💻✨
