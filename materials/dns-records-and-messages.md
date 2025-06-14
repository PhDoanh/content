---
date: 2025-03-19
draft: false
status: Done
title: Khám phá hệ thống DNS qua các bản ghi và thông điệp của nó
description: Bài viết này giải thích chi tiết về các loại bản ghi DNS như A, NS, CNAME, MX và cấu trúc của thông điệp DNS. Tìm hiểu cách các máy chủ DNS lưu trữ, truyền tải thông tin và cách thức hoạt động của chúng qua các ví dụ cụ thể 🚀
author: PhDoanh
authorlink: https://github.com/PhDoanh
tags:
  - computer-networking
  - application-layer
  - web
  - http
  - dns
  - services
  - dns-records
  - dns-messages
aliases:
  - dns records and messages
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
    src="images/dns-records-and-messages.png"
    alt="Các bản ghi và thông điệp trong DNS" 
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

Hệ thống **DNS (Domain Name System)** được ví như là "danh bạ" của Internet, chịu trách nhiệm chuyển đổi tên miền dễ nhớ thành địa chỉ IP mà máy tính có thể hiểu. Bài viết này sẽ cung cấp cái nhìn toàn diện về **DNS Records** – các bản ghi lưu trữ thông tin, cũng như cấu trúc của **DNS Messages** – các thông điệp được trao đổi giữa các máy chủ DNS.

# Các bản ghi DNS

**DNS Records** là các **resource records (RRs)** được lưu trữ trên các máy chủ DNS để cung cấp thông tin cần thiết cho quá trình chuyển đổi tên miền. Một resource record thường là một bộ bốn phần tử: **(Name, Value, Type, TTL)**. Cụ thể:

- **Name:** Tên miền hoặc hostname của đối tượng được ghi nhận.

- **Value:** Giá trị tương ứng, thường là địa chỉ IP (đối với bản ghi A), hostname của máy chủ (bản ghi NS/MX) hoặc tên chính thức (đối với bản ghi CNAME).

- **Type:** Xác định loại bản ghi. Các loại **phổ biến** bao gồm:
	- **Type A:** Cung cấp ánh xạ từ hostname sang địa chỉ IP. Giúp chuyển đổi tên miền thành địa chỉ IP thực tế của máy chủ. **Ví dụ**: `(relay1.bar.foo.com, 145.37.93.126, A)`
	- **Type NS:** Xác định máy chủ DNS có thẩm quyền cho một domain. Nếu một máy chủ không có thẩm quyền cho hostname cụ thể, nó sẽ lưu trữ bản ghi NS của domain liên quan và kèm theo một bản ghi A để cung cấp địa chỉ IP của máy chủ DNS có thẩm quyền đó. **Ví dụ**: `(foo.com, dns.foo.com, NS)`
	- **Type CNAME:** Định nghĩa tên bí danh, cho biết tên chính thức của một hostname. Sử dụng CNAME để cho phép một hostname có nhiều bí danh. **Ví dụ**: `(foo.com, relay1.bar.foo.com, CNAME)`
	- **Type MX:** Chỉ định máy chủ thư điện tử cho domain, cho phép có bí danh cho máy chủ mail. MX giúp phân chia nhiệm vụ giữa các máy chủ cho các dịch vụ khác nhau như email và web. **Ví dụ**: `(foo.com, mail.bar.foo.com, MX)`

- **TTL (Time To Live):** Thời gian (tính bằng giây) mà bản ghi được lưu trong bộ nhớ đệm.  

> [!info] Lưu ý
> TTL giúp xác định khi nào một bản ghi nên bị xóa khỏi cache; ví dụ, TTL = **3600 giây** có nghĩa là bản ghi sẽ có hiệu lực trong 1 giờ.

---

# Cấu trúc thông điệp DNS

**DNS** sử dụng hai loại thông điệp chính: **query** và **reply**. Cả hai loại thông điệp này đều có cùng một cấu trúc cơ bản, giúp đảm bảo rằng thông tin được trao đổi một cách nhất quán:

**Header Section**:
- **Kích thước:** 12 bytes đầu tiên của thông điệp.
- **Identifier (16-bit):** Định danh duy nhất của truy vấn / phản hồi, giúp phân biệt và so khớp lẫn nhau.
- **Flags:**  
	- **Query/Reply Flag:** Xác định thông điệp là truy vấn (0) hay phản hồi (1).  
	- **Authoritative Flag:** Được đặt trong thông điệp phản hồi khi máy chủ DNS có thẩm quyền cho tên được hỏi.
	- **Recursion-Desired Flag:** Được thiết lập khi client yêu cầu máy chủ thực hiện đệ quy nếu không có bản ghi.
	- **Recursion Available Flag:** Cho biết máy chủ có hỗ trợ đệ quy hay không.
- **Các trường số lượng:** Chỉ định số lượng mục trong các phần: Questions, Answer RRs, Authority RRs, Additional RRs.

**Question Section**:
**Nội dung:**  Chứa tên và loại của truy vấn.  

> [!example]- Ví dụ
> Tên được hỏi và loại yêu cầu, chẳng hạn như Type A để lấy địa chỉ IP.

**Answer Section:** Chứa các **resource records** trả lời cho truy vấn ban đầu. Một truy vấn có thể trả về nhiều bản ghi, đặc biệt khi một hostname có nhiều địa chỉ IP (ví dụ: các máy chủ Web dự phòng).

**Authority Section:** Liệt kê các bản ghi của các máy chủ có thẩm quyền cho tên được truy vấn.

**Additional Section:** Cung cấp các bản ghi hỗ trợ, ví dụ như bản ghi A cho máy chủ được liệt kê trong phần Authority.

> [!info] Lưu ý
> Việc hiểu rõ cấu trúc thông điệp DNS rất cần thiết cho việc chẩn đoán sự cố mạng và phân tích bảo mật, ví dụ như khi sử dụng công cụ **nslookup** để truy vấn thông tin DNS từ dòng lệnh.

---

# Ví dụ về truy vấn DNS

Trong quá trình truy vấn DNS, một host gửi một thông điệp **DNS query** đến máy chủ DNS và nhận lại một **DNS reply** chứa các **resource records (RRs)**. Dưới đây, chúng ta sẽ xem qua một ví dụ thực tế sử dụng công cụ dòng lệnh **dig** để minh họa quy trình này và giải thích các thành phần trong cấu trúc thông điệp.

Giả sử bạn muốn truy vấn thông tin về tên miền **example.com**. Bạn mở terminal và nhập lệnh:

```sh
dig example.com
```

Kết quả trả về có thể trông như sau:
```sh
; <<>> DiG 9.11.3-1ubuntu1.13-Ubuntu <<>> example.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 56024
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 2, ADDITIONAL: 3

;; QUESTION SECTION:
;example.com.                   IN      A

;; ANSWER SECTION:
example.com.            86400   IN      A       93.184.216.34

;; AUTHORITY SECTION:
example.com.            172800  IN      NS      a.iana-servers.net.
example.com.            172800  IN      NS      b.iana-servers.net.

;; ADDITIONAL SECTION:
a.iana-servers.net.     172800  IN      A       199.43.135.53
b.iana-servers.net.     172800  IN      A       199.43.133.53

;; Query time: 38 msec
;; SERVER: 127.0.0.53#53(127.0.0.53)
;; WHEN: Tue Aug 15 10:15:42 UTC 2023
;; MSG SIZE  rcvd: 157
```

**Header Section**:
- **ID:** `56024` – Mã số định danh duy nhất cho truy vấn, giúp ghép nối query và reply.
- **Opcode:** `QUERY` – Loại thao tác được thực hiện.
- **Status:** `NOERROR` – Trạng thái của truy vấn (NOERROR cho biết truy vấn thành công).
- **Flags:**
    - **qr:** Đánh dấu thông điệp là reply (query/reply flag).
    - **rd:** Recursion desired – Client yêu cầu thực hiện đệ quy nếu cần.
    - **ra:** Recursion available – Máy chủ hỗ trợ đệ quy.

**Question Section**:
- **Tên được truy vấn:** `example.com.`
- **Loại truy vấn:** `IN A` – Yêu cầu bản ghi loại A (tương ứng với ánh xạ hostname -> địa chỉ IP).

**Answer Section**:
- `example.com.` có **TTL** là `86400` giây (1 ngày).
- **Loại bản ghi:** `A` – Cung cấp địa chỉ IP cho tên miền.
- **Giá trị:** `93.184.216.34` – Địa chỉ IP của `example.com`.

**Authority Section**: Liệt kê các máy chủ có thẩm quyền (NS records) cho domain: `a.iana-servers.net.` và `b.iana-servers.net.` với TTL `172800` giây.

**Additional Section**: Các bản ghi bổ sung cung cấp thông tin hỗ trợ. Bản ghi A của `a.iana-servers.net.` và `b.iana-servers.net.` cho biết địa chỉ IP tương ứng, giúp client có thể truy vấn các máy chủ này nếu cần.

---

# Quy trình trao đổi thông điệp

1. **Gửi Query:** Client (host của bạn) gửi DNS query để yêu cầu một bản ghi A của `example.com`.

2. **Xử lý tại máy chủ DNS:** Máy chủ DNS nhận query, kiểm tra cache. Nếu có bản ghi hợp lệ trong cache, nó sử dụng chúng; nếu không, nó sẽ thực hiện truy vấn tiếp theo đến các máy chủ có thẩm quyền.

3. **Nhận Reply:**
	- Máy chủ DNS trả về một thông điệp DNS reply với các thành phần:
        - **Header:** Xác định thông điệp reply với ID khớp với query.
        - **Question:** Xác nhận lại tên và loại truy vấn.
        - **Answer:** Chứa các resource records đáp ứng truy vấn.
        - **Authority & Additional Sections:** Cung cấp thông tin về máy chủ có thẩm quyền và các bản ghi hỗ trợ.

4. **Hiển thị kết quả:** Công cụ **dig** hiển thị kết quả trên terminal, giúp người dùng hiểu rõ các thành phần trong thông điệp DNS.

> [!tip]- Mẹo
> - Dùng lệnh `dig +short example.com` để có kết quả ngắn gọn chỉ hiển thị địa chỉ IP.
> - Dùng `nslookup example.com` cũng là một cách tiện lợi khác để truy vấn DNS.

---

# Chèn bản ghi vào Cơ sở dữ liệu DNS

Trong hệ thống DNS, **bản ghi** giống như danh bạ điện thoại, giúp ánh xạ **tên miền** (vd: `example.com`) thành **địa chỉ IP**. Khi bạn muốn thêm hoặc thay đổi thông tin này, bạn cần **chèn bản ghi vào hệ thống DNS**.

**Các loại bản ghi DNS phổ biến**:
- **A**: Chuyển tên miền thành địa chỉ IPv4 (vd: `example.com` → `192.168.1.100`).
- **AAAA**: Chuyển tên miền thành IPv6.
- **CNAME**: Bí danh (vd: `blog.example.com` trỏ về `www.example.com`).
- **MX**: Chỉ định máy chủ email.
- **TXT**: Lưu thông tin văn bản (vd: xác thực email).

## Cách chèn bản ghi DNS

### Sửa trực tiếp tệp cấu hình (Dành cho server tự quản lý)

1. Mở tệp **cấu hình DNS** (`/etc/bind/zones/db.example.com`).

2. Thêm bản ghi, ví dụ ánh xạ `example.com` sang IP:
```txt
example.com.   IN  A   192.168.1.100
www            IN  A   192.168.1.100
```

3. **Lưu tệp** và **khởi động lại DNS** bằng lệnh:
```sh
sudo systemctl restart bind9
```

### Dùng lệnh `nsupdate` (Dành cho Dynamic DNS)

Gõ lệnh sau để thêm bản ghi A:

```sh
nsupdate
> server 192.168.1.1
> update add dev.example.com. 3600 IN A 192.168.1.200
> send
> quit
```

### Dùng giao diện web (Dễ nhất)

Nếu dùng **Cloudflare, Google Domains, AWS Route 53**, làm như sau:

1. Vào trang **quản lý DNS**.
2. Chọn **Thêm bản ghi**.
3. Nhập **loại bản ghi (A, CNAME, MX, v.v.)** và **địa chỉ IP**.
4. **Lưu lại** và chờ DNS cập nhật.

## Kiểm tra sau khi chèn bản ghi

**Kiểm tra bản ghi A:**
```sh
dig example.com A
```

**Kiểm tra bản ghi CNAME:**
```sh
dig blog.example.com CNAME
```

Nếu thấy kết quả đúng với bản ghi bạn thêm, có nghĩa là DNS đã cập nhật thành công.

---

# Các câu hỏi thường gặp

> [!caution]- Nội dung đang hoàn thiện
> Quá trình xây dựng nội dung này có thể mất nhiều thời gian ⌛, nhưng bạn có thể thúc đẩy nó bằng cách tham gia [[article-collaboration-guide|cộng tác bài viết]] 🤝
> 
> **Rất mong sự thông cảm của các bạn 🙏**

---

# Tổng kết

Qua bài viết này, chúng ta đã tìm hiểu về:
- **DNS Records:** Các bản ghi như **A, NS, CNAME, MX** được sử dụng để lưu trữ thông tin chuyển đổi tên miền, với mỗi bản ghi có 4 trường: **Name, Value, Type, TTL**.
- **DNS Messages:** Cấu trúc thông điệp DNS bao gồm **Header, Question, Answer, Authority, Additional Sections** giúp trao đổi thông tin một cách nhất quán giữa các máy chủ.
- **Ứng dụng thực tế:** Từ việc gửi truy vấn với **nslookup** cho đến quá trình chèn bản ghi khi đăng ký tên miền, tất cả đều minh họa cho cách thức hoạt động của hệ thống DNS.

Việc nắm rõ các khái niệm trên sẽ giúp bạn **hiểu rõ hơn về cơ chế hoạt động của DNS** và hỗ trợ trong việc chẩn đoán, bảo mật cũng như tối ưu hóa hệ thống mạng của mình. Nếu bạn muốn tìm hiểu thêm, hãy tham khảo [RFC 1034](https://tools.ietf.org/html/rfc1034) và [RFC 1035](https://tools.ietf.org/html/rfc1035) để có kiến thức chuyên sâu hơn về DNS. 🚀
