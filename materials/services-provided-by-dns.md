---
date: 2025-03-18
draft: false
status: Done
title: "Khám phá dịch vụ của DNS: Từ chuyển đổi tên máy chủ đến phân phối tải"
description: "Bài viết này cung cấp cái nhìn tổng quan về dịch vụ của DNS, từ việc chuyển đổi hostname thành địa chỉ IP cho đến phân phối tải và các tính năng alias quan trọng. Tìm hiểu ngay để nắm bắt cách hoạt động của một trong những thành phần cốt lõi của Internet!"
author: PhDoanh
authorlink: https://github.com/PhDoanh
tags:
  - computer-networking
  - application-layer
  - web
  - http
  - dns
  - services
aliases:
  - services provided by dns
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
    src="images/services-provided-by-dns.png"
    alt="Khám phá dịch vụ của DNS: Từ chuyển đổi tên máy chủ đến phân phối tải" 
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

**DNS (Domain Name System)** là một hệ thống **directory service** chuyển đổi các tên miền dễ nhớ thành địa chỉ IP mà máy tính và các thiết bị mạng sử dụng để giao tiếp. Trong bài viết này, chúng ta sẽ cùng tìm hiểu chi tiết về các dịch vụ chính mà DNS cung cấp, đồng thời mở rộng sang một số thông tin nâng cao liên quan.

# Giới thiệu về DNS

**DNS** là một hệ thống phân tán, được triển khai dưới dạng cơ sở dữ liệu phân cấp trên nhiều máy chủ DNS. Một số đặc điểm nổi bật của DNS bao gồm:

- **Phân tán**: Dữ liệu DNS được lưu trữ trên nhiều máy chủ, giúp cải thiện tính sẵn sàng và hiệu suất.

- **Đa chức năng**: Ngoài việc chuyển đổi tên thành địa chỉ IP, DNS còn hỗ trợ các tính năng khác như alias, phân phối tải, v.v.

- **Giao thức ứng dụng**: DNS sử dụng giao thức UDP (cũng có thể dùng TCP trong một số trường hợp) và chạy trên cổng `53`.

> [!info] Lưu ý
> Do tính chất phân tán, một truy vấn DNS có thể trải qua nhiều bước, dẫn đến một độ trễ nhất định. Việc caching tại các máy chủ DNS gần người dùng sẽ giúp giảm độ trễ này.

---

# Chuyển đổi tên máy chủ sang địa chỉ IP

Đây là chức năng cốt lõi của **DNS**. Khi một trình duyệt cần truy cập vào một URL như `www.example.com`, hệ thống sẽ:
1. **Trích xuất hostname** từ URL.
2. **Gửi truy vấn** đến máy chủ DNS.
3. **Nhận phản hồi** chứa địa chỉ IP tương ứng.

Quá trình truy vấn DNS bổ sung thêm một độ trễ nhất định vào thời gian phản hồi của ứng dụng Internet. Một công thức đơn giản để tính tổng thời gian chờ là:

$$
T_{total} = T_{DNS} + T_{TCP}
$$

Trong đó:
- $T_{DNS}$: Thời gian thực hiện truy vấn DNS.
- $T_{TCP}$: Thời gian thiết lập kết nối TCP sau khi có địa chỉ IP.

> [!tip]- Mẹo
>  Việc caching kết quả DNS tại máy khách hoặc máy chủ gần đó sẽ giảm đáng kể $T_{DNS}$.

---

# Bí danh cho máy chủ

**Host aliasing** cho phép một máy chủ có nhiều tên gọi khác nhau. Một hostname phức tạp có thể được liên kết với một hoặc nhiều alias dễ nhớ hơn. Ví dụ:
- **Canonical hostname (tên máy chủ chuẩn):** `relay1.west-coast.enterprise.com`
- **Alias names:** `enterprise.com`, `www.enterprise.com`, ...

Điều này giúp người dùng dễ dàng truy cập vào máy chủ mà không cần nhớ chính xác tên đầy đủ.

> [!important] Quan trọng 
> Việc sử dụng alias giúp cải thiện tính **mnemonic** và thân thiện với người dùng.

---

# Bí danh cho máy chủ Mail

DNS cũng hỗ trợ alias cho các máy chủ email, cho phép địa chỉ email trở nên **mnemonic** hơn. Ví dụ:
- **Email address:** `bob@hotmail.com`, trong đó `hotmail.com` là hostname.
- **Canonical hostname của mail server:** Có thể là một tên phức tạp như `relay1.west-coast.hotmail.com`

**MX Record (Mail Exchanger Record)** là một loại bản ghi trong **DNS** giúp xác định **máy chủ thư (mail server)** chịu trách nhiệm xử lý email đến cho một tên miền cụ thể. Khi một email được gửi, hệ thống sẽ tra cứu MX Record để biết mail server nào sẽ nhận thư. Ví dụ:

```sh
example.com.   3600  IN  MX  10  mail.example.com.
example.com.   3600  IN  MX  20  backupmail.example.com.
...
```

Ở đây:
- **`example.com.`**: Tên miền đích nhận email.
- **`3600`**: TTL (Time To Live), khoảng thời gian bản ghi được cache.
- **`IN`**: Chỉ ra loại bản ghi thuộc Internet.
- **`MX`**: Loại bản ghi Mail Exchanger.
- **`10 mail.example.com.`**: Chỉ ra mail server chính với **ưu tiên 10**.
- **`20 backupmail.example.com.`**: Mail server dự phòng với **ưu tiên 20** (số càng lớn, mức độ ưu tiên càng thấp).

Thông qua **MX record**, DNS cho phép cấu hình nhiều máy chủ email (`mail.example.com.`, `backupmail.example.com.`, ...) cho cùng một alias (`example.com.`), giúp tăng tính sẵn sàng và cân bằng tải.

> [!info] Lưu ý
> - Trong thiết lập MX Record, **`example.com` không phải là mail server thực sự**, mà chỉ là domain được cấu hình để nhận email. Nó đóng vai trò như một **Mail Server Client (SMTP Client)** khi gửi email, nhưng khi nhận email, nó sẽ dựa vào MX Record để xác định **Mail Server thực sự** (SMTP Server) chịu trách nhiệm xử lý thư đến.
> - Việc cấu hình đúng `MX record` rất quan trọng để đảm bảo email được phân phối hiệu quả.

---

# Phân phối tải qua DNS

**DNS** không chỉ chuyển đổi tên mà còn đóng vai trò quan trọng trong việc **phân phối tải** cho các dịch vụ trực tuyến, đặc biệt là các trang web có lượng truy cập lớn như `cnn.com`. Cách thức hoạt động:

- Máy chủ DNS liên kết một hostname với **nhiều địa chỉ IP** của các máy chủ khác nhau.

- Khi truy vấn, máy chủ DNS sẽ **xoay vòng thứ tự** của các địa chỉ IP trong phản hồi.

- **Khách hàng** thường kết nối tới địa chỉ IP được liệt kê đầu tiên sau khi xoay vòng, từ đó phân phối tải đều giữa các máy chủ.

> [!example]- Ví dụ
> Nếu có 3 máy chủ với địa chỉ IP khác nhau, DNS sẽ luân phiên đưa mỗi IP lên đầu danh sách phản hồi, đảm bảo rằng không máy chủ nào bị quá tải.

> [!info] Lưu ý
> Để hỗ trợ DNS phân phối tải, một dịch vụ / ứng dụng sẽ được triển khai trên nhiều máy chủ.

---

# Các ứng dụng nâng cao của DNS

Ngoài các dịch vụ cơ bản đã đề cập, DNS còn được sử dụng trong nhiều ứng dụng nâng cao:
- **Content Distribution Networks (CDN):** Các công ty như **[Akamai](https://www.akamai.com/)** sử dụng DNS để định tuyến người dùng tới máy chủ CDN gần nhất. Khi người dùng truy cập một trang web sử dụng Akamai (ví dụ: **Netflix, Steam, Apple**), DNS sẽ giúp họ kết nối đến **máy chủ CDN gần nhất** để giảm độ trễ và tăng tốc độ tải trang.

> [!example]- Ví dụ
> - Khi bạn mở trang https://www.apple.com/, yêu cầu của bạn có thể được định tuyến đến một máy chủ CDN gần nhất, thay vì đến trực tiếp máy chủ chính của Apple.
> - Akamai sử dụng **Anycast DNS** để xác định vị trí của bạn và trả về IP của máy chủ CDN phù hợp nhất.
> - Nếu bạn ở Việt Nam, thay vì tải dữ liệu từ Mỹ, bạn sẽ được kết nối với một máy chủ Akamai ở Singapore hoặc Việt Nam.

- **Bảo mật:** DNSSEC (DNS Security Extensions) giúp bảo vệ người dùng khỏi các cuộc tấn công giả mạo DNS như **DNS Spoofing** hoặc **Man-in-the-Middle Attack**. DNSSEC sử dụng **chữ ký số** để đảm bảo rằng bản ghi DNS nhận được là chính xác và không bị thay đổi.

> [!example]- Ví dụ
> - Google Public DNS (**8.8.8.8**) hỗ trợ **DNSSEC**. Khi bạn truy vấn một trang web, Google DNS có thể kiểm tra tính toàn vẹn của bản ghi DNS trước khi trả về kết quả.
> - Nếu một hacker cố gắng giả mạo địa chỉ IP của ngân hàng (ví dụ: **vietcombank.com.vn**) để chuyển hướng bạn đến một trang lừa đảo, DNSSEC sẽ phát hiện ra sự giả mạo này và chặn kết nối.

- **Tối ưu hóa mạng:** Một số nhà cung cấp DNS, như **Cloudflare, Google Public DNS**, sử dụng **GeoDNS** để xác định vị trí của người dùng và trả về địa chỉ IP gần nhất, giúp tối ưu hóa hiệu suất mạng.

> [!example]- Ví dụ
> - Khi bạn tìm kiếm trên **Google.com**, hệ thống sẽ tự động định tuyến bạn đến một máy chủ gần nhất dựa trên vị trí của bạn.
> - Nếu bạn ở Việt Nam, Google sẽ không trả về máy chủ tại Mỹ, mà thay vào đó là một máy chủ **Google tại Singapore hoặc Hồng Kông** để cải thiện tốc độ tìm kiếm.
> - Netflix cũng áp dụng GeoDNS để hiển thị nội dung phù hợp với từng khu vực. Ví dụ, người dùng tại Mỹ sẽ thấy nhiều phim hơn so với người dùng tại Việt Nam.

> [!tip]- Mẹo
> Nếu bạn quản trị hệ thống, hãy cân nhắc triển khai `DNS caching` và `DNSSEC` để tăng cường hiệu năng và bảo mật.

---

# Các câu hỏi thường gặp

> [!caution]- Nội dung đang hoàn thiện
> Quá trình xây dựng nội dung này có thể mất nhiều thời gian ⌛, nhưng bạn có thể thúc đẩy nó bằng cách tham gia [[article-collaboration-guide|cộng tác bài viết]] 🤝
> 
> **Rất mong sự thông cảm của các bạn 🙏**

---

# Tổng kết

Trong bài viết này, chúng ta đã khám phá các **dịch vụ chính của DNS**:
- **Chuyển đổi tên máy chủ sang địa chỉ IP** là chức năng cốt lõi, giúp máy tính kết nối với nhau trên Internet.
- **Host aliasing** và **mail server aliasing** giúp cải thiện tính **mnemonic** của tên miền, từ đó nâng cao trải nghiệm người dùng.
- **Phân phối tải** qua DNS là một phương pháp hiệu quả để quản lý lưu lượng truy cập trên các trang web lớn.
- Ngoài ra, DNS còn hỗ trợ các ứng dụng nâng cao như CDN và bảo mật thông tin.

**DNS** thực sự là một thành phần không thể thiếu của Internet, không chỉ giúp dịch chuyển dữ liệu một cách nhanh chóng mà còn đảm bảo **hiệu suất**, **bảo mật**, và **tính khả dụng** của các dịch vụ mạng. Hy vọng rằng bài viết đã cung cấp cho bạn cái nhìn toàn diện và những **mẹo hữu ích** để hiểu sâu hơn về cơ chế hoạt động của DNS. 🚀
