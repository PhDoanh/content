---
date: 2025-03-18
draft: false
status: Done
title: Tổng quan về hoạt động của DNS
description: "Bài viết này cung cấp một cái nhìn tổng quan về cách thức hoạt động của DNS, từ quá trình chuyển đổi hostname sang địa chỉ IP đến kiến trúc phân cấp và cơ chế caching. Cùng khám phá chi tiết quy trình và những mẹo tối ưu hóa truy vấn DNS trên Internet!"
author: PhDoanh
authorlink: https://github.com/PhDoanh
tags:
  - computer-networking
  - application-layer
  - web
  - http
  - dns
  - services
  - working-principle
aliases:
  - overview of how dns works
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
    src="images/overview-of-how-dns-works.png"
    alt="Tổng quan về cách DNS hoạt động" 
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

**DNS (Domain Name System)** là một **hệ thống dịch vụ chuyển đổi tên miền** giúp chuyển đổi các tên máy chủ dễ nhớ (hostname) thành địa chỉ IP mà các thiết bị mạng sử dụng để giao tiếp. Mặc dù với góc nhìn của ứng dụng (như trình duyệt web hay mail client), DNS giống như một **hộp đen** đơn giản, nhưng bên trong lại là một hệ thống phức tạp với nhiều máy chủ và giao thức tương tác chặt chẽ.

# Giới thiệu về DNS

**DNS** hoạt động theo mô hình **client-server** với các bước chính như sau:
- Ứng dụng (trình duyệt web chẳng hạn) sẽ gọi tới hàm như `gethostbyname` trên hệ điều hành của máy tính người dùng để thực hiện việc chuyển đổi tên miền.
- **DNS client** trên máy người dùng gửi truy vấn dưới dạng các gói **UDP** đến cổng `53` của **DNS server**
- Sau một khoảng thời gian (từ vài mili giây đến vài giây), **DNS server** trả về kết quả ánh xạ hostname và IP.

> [!info] Lưu ý
> - Dù quy trình đối với ứng dụng chỉ là một truy vấn "đơn giản", nhưng phía sau là một cơ chế phức tạp gồm nhiều lớp máy chủ phân tán.
> - Hàm `gethostbyname` là một **hàm của hệ điều hành**, cụ thể hơn là một phần của thư viện mạng trong **giao diện lập trình Berkeley Sockets API**. Hàm này đã **bị lỗi thời** (deprecated) trong chuẩn **POSIX** và **Windows**, thay vào đó, các hệ điều hành hiện đại khuyến nghị sử dụng:
> - **`getaddrinfo`**: Chuyển hostname thành địa chỉ IPv4 hoặc IPv6.
> - **`getnameinfo`**: Chuyển địa chỉ IP thành hostname.

---

# Vấn đề của thiết kế tập trung

Một thiết kế đơn giản với **một máy chủ DNS trung tâm** sẽ gặp phải một số hạn chế:
- **Single point of failure:** Nếu máy chủ DNS bị sự cố, toàn bộ hệ thống có thể ngừng hoạt động.
- **Traffic volume:** Một máy chủ phải xử lý toàn bộ truy vấn của hàng tỷ máy chủ khác, dễ gây nghẽn mạng.
- **Kho dữ liệu tập trung:** Việc cập nhật và duy trì một cơ sở dữ liệu khổng lồ không khả thi khi số lượng host liên tục tăng.

Vì lý do này, DNS được thiết kế theo mô hình **phân tán** và **phân cấp**, giúp tối ưu hóa hiệu năng và độ tin cậy.

---

# Kiến trúc phân cấp của DNS
Khi một máy tính muốn truy cập một website (VD: `example.com`), nó phải **tra cứu địa chỉ IP** tương ứng thông qua hệ thống DNS. Quá trình này diễn ra qua nhiều loại **máy chủ DNS**, mỗi loại có một vai trò nhất định.

## Root DNS Servers
**Vai trò:**
- Đây là **cấp cao nhất** trong hệ thống phân cấp DNS.
- Quản lý danh sách các máy chủ **TLD DNS Servers**.
- Hiện nay có **13 cụm máy chủ gốc (A → M)**, mỗi cụm bao gồm **nhiều máy chủ phân tán khắp thế giới** để đảm bảo tính bảo mật và tốc độ phản hồi.

**Hoạt động:** Khi nhận được truy vấn (VD: `example.com`), Root DNS Server **không biết địa chỉ IP** của `example.com`, nhưng nó **hướng truy vấn đến máy chủ TLD** của `.com`.

## TLD DNS Servers
**Vai trò:**
- Chịu trách nhiệm quản lý **các tên miền cấp cao (TLDs)** như `.com`, `.org`, `.vn`, `.jp`.
- Mỗi **TLD** có một nhóm máy chủ DNS riêng, ví dụ:
    - `.com` do **Verisign** quản lý
    - `.vn` do **VNNIC** quản lý

**Hoạt động:** Nếu Root DNS Server trỏ đến **TLD của `.com`**, máy chủ này sẽ tiếp tục tra cứu và trả về địa chỉ của **Authoritative DNS Server** cho `example.com`.

## Authoritative DNS Servers
**Vai trò:**
- Đây là máy chủ **quyết định chính xác IP của website**.
- Mỗi tổ chức hoặc nhà cung cấp dịch vụ (như Google, Facebook) có một hoặc nhiều **Authoritative DNS Servers** để quản lý các tên miền của họ.

**Hoạt động:** Khi nhận truy vấn từ **TLD DNS Server**, máy chủ này sẽ **trả về IP thực sự** của `example.com`, ví dụ: `93.184.216.34`.

## Local DNS Servers
**Vai trò:**
- **Nằm gần người dùng**, thường được cung cấp bởi ISP hoặc doanh nghiệp.
- Lưu trữ bản ghi **tạm thời (cache)** để giảm thời gian truy vấn.

**Hoạt động:** Khi người dùng nhập `example.com`, trình duyệt trước tiên gửi yêu cầu tới **Local DNS Server**. Nếu Local DNS Server **đã có bản ghi trong cache**, nó sẽ trả về kết quả ngay lập tức mà không cần hỏi các máy chủ cấp cao hơn. Nếu **không có cache**, nó sẽ khởi động truy vấn qua Root DNS → TLD DNS → Authoritative DNS như trên.

> [!tip]- Mẹo
> Sử dụng máy chủ DNS địa phương giúp giảm thời gian truy vấn, vì máy chủ này thường nằm gần host về mặt địa lý.

---

# Quy trình truy vấn DNS

1. **Người dùng nhập** `example.com` vào trình duyệt.  

2. **Local DNS Server** kiểm tra cache:
	- Nếu có, trả về IP ngay lập tức.
	- Nếu không, gửi truy vấn lên **Root DNS Server**.  

3. **Root DNS Server** hướng dẫn truy vấn đến **TLD DNS Server** của `.com`.  

4. **TLD DNS Server** cung cấp địa chỉ của **Authoritative DNS Server** của `example.com`.  

5. **Authoritative DNS Server** trả về IP thực sự (`93.184.216.34`).  

6. **Local DNS Server** lưu trữ kết quả vào cache và gửi IP cho trình duyệt.  

7. Trình duyệt **kết nối trực tiếp** đến `93.184.216.34` để tải trang web.

> [!tip]- Mẹo
> Để giảm độ trễ, hãy đảm bảo sử dụng **`DNS caching`** tại cả phía máy khách và máy chủ địa phương.

---

# Các loại truy vấn trong DNS

Khi một máy khách (client) gửi yêu cầu tìm kiếm địa chỉ IP của một tên miền, quá trình này diễn ra thông qua **ba loại truy vấn chính**:

## Truy vấn đệ quy

**Cách hoạt động:**
- Client yêu cầu **Local DNS Server** tìm **địa chỉ IP chính xác** cho một tên miền.
- Nếu Local DNS Server không có kết quả trong cache, nó sẽ thay mặt client truy vấn lên các máy chủ DNS cấp cao hơn (Root DNS → TLD DNS → Authoritative DNS).
- Các máy chủ cấp cao hơn trả về kết quả cho các máy chủ cấp thấp theo chiều ngược lại
- Local DNS Server sau đó gửi kết quả cuối cùng về cho client.

> [!example]- Ví dụ
> 1. Người dùng nhập `example.com` vào trình duyệt.
> 2. **Local DNS Server** kiểm tra cache nhưng **không có kết quả**.
> 3. Local DNS Server thực hiện các truy vấn tiếp theo lên Root DNS → TLD DNS → Authoritative DNS. 
> 4. Nhận được IP (`93.184.216.34`), Local DNS Server lưu cache và trả về cho client.

**Đặc điểm:**  
- Tiết kiệm tài nguyên cho client (chỉ cần gửi một yêu cầu duy nhất).  
- Thường được thực hiện bởi **Local DNS Server**.

## Truy vấn đệ quy ngược

**Cách hoạt động:**
- Ngược lại với truy vấn đệ quy, loại này được sử dụng để **tìm tên miền từ địa chỉ IP**.
- Dựa vào **bản ghi PTR (Pointer Record)** trong hệ thống DNS để ánh xạ IP ngược lại thành hostname.

> [!example]- Ví dụ
> - Truy vấn IP `93.184.216.34` có thể trả về tên miền `example.com`.
> - Thường được sử dụng trong **chẩn đoán mạng và bảo mật**, như kiểm tra nguồn gốc email hoặc chặn địa chỉ IP đáng ngờ.

**Đặc điểm:**  
- Hỗ trợ kiểm tra và xác minh nguồn gốc của một địa chỉ IP.  
- Hay được sử dụng trong **máy chủ mail (Mail Servers) hoặc hệ thống bảo mật**.

## Truy vấn lặp

**Cách hoạt động:**
- Client tự mình truy vấn từng bước (Root → TLD → Authoritative) mà không nhờ Local DNS Server tìm kiếm toàn bộ như truy vấn đệ quy.
- Nếu DNS Server nhận được yêu cầu nhưng không có thông tin, nó sẽ trả về **địa chỉ của máy chủ DNS tiếp theo**, để client tự gửi truy vấn tiếp theo.

> [!example]- Ví dụ
> 1. **Client** gửi yêu cầu tìm `example.com` đến **Local DNS Server**.
> 2. **Local DNS Server** không có bản ghi, nhưng nó trả về địa chỉ của **Root DNS Server**.
> 3. Client gửi truy vấn lên Root DNS Server, và tiếp tục gửi lên TLD DNS Server nếu  Root DNS Server không có thông tin và cứ thế lặp lại với các cấp tiếp theo (Authoritative DNS Server)
> 4. Cuối cùng, client nhận được IP và truy cập vào website.

**Đặc điểm:**  
- Tiết kiệm tài nguyên máy chủ DNS trung gian.  
- Thường được sử dụng bởi **các máy chủ DNS cấp cao** thay vì client trực tiếp.

**So sánh ba loại truy vấn DNS**

| Loại truy vấn                              | Ai thực hiện?              | Quá trình tìm kiếm                           | Ưu điểm                             | Nhược điểm                      |
| ------------------------------------------ | -------------------------- | -------------------------------------------- | ----------------------------------- | ------------------------------- |
| **Truy vấn đệ quy (Recursive)**            | Local DNS Server           | Local DNS thực hiện truy vấn thay cho client | Nhanh, tiện lợi cho client          | Tốn tài nguyên Local DNS        |
| **Truy vấn đệ quy ngược (Reverse Lookup)** | Client hoặc máy chủ        | Tìm hostname từ địa chỉ IP (bản ghi PTR)     | Kiểm tra nguồn gốc IP, bảo mật cao  | Không phải tất cả IP đều có PTR |
| **Truy vấn lặp (Iterative)**               | Client hoặc DNS trung gian | Client tự truy vấn từng bước                 | Giảm tải cho máy chủ DNS trung gian | Chậm hơn nếu client tự truy vấn |

> [!info] Lưu ý
> Sự kết hợp giữa truy vấn đệ quy và lặp giúp tối ưu quá trình tìm kiếm mà không gây quá tải cho từng máy chủ riêng lẻ.

---

# Cơ chế DNS Caching

DNS caching là một **chiến lược tối ưu hóa quan trọng** trong hệ thống DNS:
- **Lưu trữ tạm thời:** Khi một máy chủ DNS nhận được phản hồi, nó lưu kết quả vào bộ nhớ cache để phục vụ các truy vấn sau.
- **Giảm số lượng truy vấn:** Nếu cùng một hostname được truy vấn lại, máy chủ có thể trả lời ngay từ cache mà không cần gửi thêm truy vấn lên hệ thống phân cấp.
- **Thời gian tồn tại (TTL):** Các bản ghi cache được giữ trong một khoảng thời gian nhất định (thường là khoảng 2 ngày) trước khi bị xoá.

Ví dụ về công thức tính thời gian truy vấn. Giả sử quá trình truy vấn DNS gồm nhiều bước, ta có thể ước tính tổng thời gian trễ bằng công thức:

$$
T_{total} = \sum_{i=1}^{N} T_i
$$

- $N$: Số lượng truy vấn DNS được thực hiện.
- $T_i$: Thời gian của truy vấn thứ `i`.

> [!tip]- Mẹo
> Cải thiện tốc độ truy vấn bằng cách tăng cường cơ chế caching, giảm thiểu số lượng truy vấn cần gửi lên hệ thống phân cấp.

---

# Các câu hỏi thường gặp

> [!caution]- Nội dung đang hoàn thiện
> Quá trình xây dựng nội dung này có thể mất nhiều thời gian ⌛, nhưng bạn có thể thúc đẩy nó bằng cách tham gia [[article-collaboration-guide|cộng tác bài viết]] 🤝
> 
> **Rất mong sự thông cảm của các bạn 🙏**

---

# Tổng kết 🔍

Trong bài viết này, chúng ta đã cùng nhau khám phá:
- **Cách thức hoạt động của DNS:** Từ việc chuyển đổi tên thành địa chỉ IP cho đến giao tiếp giữa các máy chủ.
- **Quy trình truy vấn DNS:** Sự khác biệt giữa truy vấn đệ quy và lặp, cùng với các vấn đề khi sử dụng mô hình tập trung.
- **Kiến trúc phân cấp của DNS:** Bao gồm các lớp máy chủ như root, TLD, authoritative và local.
- **Cơ chế caching:** Giúp tối ưu hóa hiệu năng bằng cách lưu trữ tạm thời các bản ghi DNS.

DNS không chỉ là một dịch vụ chuyển đổi tên đơn giản mà còn là **trụ cột của Internet**, đảm bảo kết nối hiệu quả, an toàn và ổn định giữa hàng tỷ thiết bị trên toàn cầu. Hy vọng bài viết đã giúp bạn hiểu rõ hơn về cơ chế hoạt động của DNS và những **mẹo tối ưu** để nâng cao hiệu suất truy vấn. 🚀
