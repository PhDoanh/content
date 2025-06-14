---
date: 2025-03-08
draft: true
status: Doing
title: Nguyên tắc trong các ứng dụng Mạng
description: "Bài viết này giải thích chi tiết nguyên tắc phát triển ứng dụng mạng theo hướng top‑down, từ kiến trúc ứng dụng đến giao tiếp giữa các tiến trình, cũng như các dịch vụ vận chuyển và giao thức ứng dụng. Hãy cùng khám phá cách thức xây dựng các ứng dụng mạng hiện đại qua các ví dụ thực tiễn! 🚀"
author: PhDoanh
authorlink: https://github.com/PhDoanh
tags:
  - internet
  - computer-network
  - application-layer
  - world-wide-web
aliases:
  - principles of network applications
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
    src="images/principles-of-network-applications.png"
    alt="Nguyên tắc trong các ứng dụng Mạng" 
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

Bài viết này giới thiệu cơ sở phát triển ứng dụng mạng – từ ý tưởng ban đầu đến việc triển khai phần mềm chạy trên các _end systems_ (thiết bị đầu cuối) để giao tiếp qua Internet. Khi phát triển ứng dụng mạng, bạn sẽ phải viết phần mềm bằng các ngôn ngữ như `C`, `Java` hay `Python` và chỉ chạy trên các thiết bị đầu cuối, không phải trên các router hay switch trong lõi mạng

> [!info] Lưu ý
> - Thiết kế ứng dụng mạng luôn tách biệt với kiến trúc mạng vật lý; bạn chỉ can thiệp vào lớp ứng dụng mà thôi!
> - Kiến trúc ứng dụng do nhà phát triển định hướng, khác biệt hoàn toàn so với kiến trúc mạng 5 lớp truyền thống (hoặc 7 lớp của OSI)

# 🏗️ Kiến trúc ứng dụng

Ứng dụng mạng được xây dựng dựa trên các mô hình kiến trúc chủ yếu sau:

## Client-Server
Kiến trúc **Client-Server** là một mô hình phổ biến trong mạng máy tính, trong đó **client (máy khách)** gửi yêu cầu dịch vụ và **server (máy chủ)** xử lý yêu cầu và trả về kết quả. Máy chủ thường có địa chỉ IP cố định và cung cấp tài nguyên hoặc dịch vụ cho nhiều máy khách khác nhau.

**Đặc điểm chính**:
- Máy khách (Client) khởi tạo yêu cầu và chờ phản hồi từ máy chủ.
- Máy chủ (Server) tiếp nhận và xử lý yêu cầu từ nhiều máy khách.
- Giao tiếp giữa Client và Server thường thông qua các **giao thức tầng ứng dụng** như HTTP, FTP, SMTP...

> [!example]- Ví dụ
> Khi bạn truy cập một trang web: **trình duyệt web (client)** gửi yêu cầu HTTP đến **máy chủ web (server)**, máy chủ xử lý yêu cầu và trả về mã HTML để hiển thị trang web. Trong quá trình này, máy chủ có thể truy vấn cơ sở dữ liệu để lấy thông tin, nhưng toàn bộ dữ liệu được gửi từ server chứ không phải từ các client khác.

**Ứng dụng**:
Kiến trúc này được sử dụng rộng rãi trong nhiều hệ thống và dịch vụ mạng:

- **Web & Internet:** Trình duyệt Web (Client) gửi yêu cầu HTTP đến máy chủ Web (Server) để lấy nội dung trang web. Ví dụ: **Google Chrome truy cập trang web từ máy chủ của Google**.

- **Thư điện tử (Email):** Email Client (Outlook, Gmail app) gửi và nhận email từ máy chủ qua SMTP, IMAP, hoặc POP3.

- **Cơ sở dữ liệu & Ứng dụng doanh nghiệp:** Ứng dụng quản lý bán hàng gửi truy vấn SQL đến máy chủ cơ sở dữ liệu (Database Server) như **MySQL, PostgreSQL** để lấy dữ liệu khách hàng.

- **Truyền tệp & Lưu trữ đám mây:** FTP Client kết nối đến FTP Server để tải lên hoặc tải xuống tệp. Dịch vụ lưu trữ đám mây như **Google Drive, Dropbox** hoạt động theo mô hình Client-Server.

- **Trò chơi trực tuyến (Online Gaming):** Các tựa game như **Liên Minh Huyền Thoại (LoL), CS:GO** sử dụng máy chủ trung tâm để quản lý trận đấu, dữ liệu game và kết nối người chơi.

> [!check] Ưu điểm
> - **Dễ quản lý & bảo mật:** Máy chủ tập trung lưu trữ dữ liệu, giúp dễ kiểm soát và bảo vệ thông tin.  
> - **Hiệu suất cao:** Máy chủ có thể được thiết kế mạnh mẽ để xử lý nhiều yêu cầu đồng thời từ nhiều Client.  
> - **Sao lưu & cập nhật dễ dàng:** Chỉ cần cập nhật trên máy chủ, tất cả Client đều được hưởng lợi mà không cần cập nhật từng thiết bị.  
> - **Phù hợp với hệ thống lớn:** Mô hình này dễ mở rộng khi số lượng Client tăng lên, chỉ cần nâng cấp máy chủ hoặc thêm máy chủ mới.

> [!missing] Nhược điểm
> - **Phụ thuộc vào máy chủ:** Nếu máy chủ gặp sự cố, toàn bộ hệ thống có thể bị gián đoạn.  
> - **Chi phí cao:** Máy chủ cần phần cứng mạnh mẽ và bảo trì liên tục để đảm bảo hoạt động ổn định.  
> - **Tắc nghẽn mạng:** Nếu có quá nhiều Client kết nối đồng thời, máy chủ có thể bị quá tải, làm giảm hiệu suất.  
> - **Khả năng mở rộng hạn chế:** Khi lượng Client tăng quá nhanh, việc nâng cấp máy chủ hoặc cân bằng tải có thể trở nên phức tạp.

## Peer-to-Peer (P2P)    
Kiến trúc **Peer-to-Peer (P2P)** là một mô hình mạng **phi tập trung**, trong đó **các thiết bị (peers) có thể vừa đóng vai trò là client vừa là server**. Không giống như mô hình **Client-Server**, nơi dữ liệu và dịch vụ tập trung tại một máy chủ, mô hình **P2P cho phép các thiết bị trực tiếp trao đổi dữ liệu với nhau** mà không cần máy chủ trung tâm.

> [!example]- Ví dụ
> Khi hai máy tính chia sẻ tệp tin trực tiếp với nhau qua mạng LAN mà không cần thông qua một máy chủ trung gian, đó chính là một **hệ thống P2P đơn giản**.

**Ứng dụng:**
Mô hình **P2P được ứng dụng rộng rãi** trong nhiều lĩnh vực, đặc biệt là các hệ thống yêu cầu phân phối dữ liệu lớn hoặc cộng tác phi tập trung:

- **Chia sẻ tệp tin:** Hệ thống **BitTorrent** giúp người dùng tải và chia sẻ dữ liệu nhanh chóng mà không cần máy chủ trung tâm.

- **Tiền điện tử:** Hệ thống **Bitcoin** hoạt động trên mô hình P2P, nơi các nút mạng xác nhận giao dịch mà không cần ngân hàng trung gian.

- **Gọi điện và nhắn tin:** **Skype (phiên bản cũ)** từng sử dụng P2P để kết nối các cuộc gọi trực tiếp giữa người dùng mà không cần máy chủ trung gian.

- **Mạng lưu trữ phân tán:** **IPFS (InterPlanetary File System)** giúp phân phối và lưu trữ dữ liệu theo mô hình P2P, thay thế hệ thống tập trung truyền thống.

> [!check] Ưu điểm
> - **Không cần máy chủ trung tâm** → Giảm chi phí vận hành và không có điểm lỗi tập trung.  
> - **Khả năng mở rộng tốt** → Hệ thống có thể mở rộng **dễ dàng** khi có nhiều người tham gia.  
> - **Hiệu suất cao** → Khi có nhiều peers, tốc độ truyền tải dữ liệu có thể nhanh hơn nhờ **chia nhỏ dữ liệu và tải về từ nhiều nguồn khác nhau (ví dụ: BitTorrent)**.  
> - **Tính phân tán cao** → Dữ liệu và tài nguyên không bị giới hạn tại một vị trí, giúp hệ thống **chống chịu tốt hơn với lỗi hoặc tấn công mạng**.

> [!missing] Nhược điểm
> - **Khó kiểm soát và quản lý** → Vì không có máy chủ trung tâm, rất khó để kiểm soát nội dung và bảo mật hệ thống.  
> - **Bảo mật kém hơn** → Người dùng phải giao tiếp trực tiếp với nhiều thiết bị khác nhau, tăng nguy cơ bị **tấn công hoặc lây nhiễm mã độc**.  
> - **Tốc độ có thể không ổn định** → Nếu **có ít peers hoặc peers có tốc độ mạng yếu**, hiệu suất truyền tải dữ liệu có thể bị giảm.  
> - **Tiêu tốn nhiều tài nguyên thiết bị** → Mỗi peer có thể phải **xử lý và lưu trữ dữ liệu**, gây hao tốn CPU, bộ nhớ và băng thông.

---

# 📬 Giao tiếp giữa các tiến trình
Một **tiến trình (process)** là một chương trình đang chạy trên một thiết bị, có thể thực hiện các tác vụ khác nhau như xử lý dữ liệu, gửi yêu cầu mạng, hoặc tương tác với người dùng.

> [!info]- Lưu ý
> - Một tiến trình có thể tạo ra **nhiều luồng (threads)** để thực hiện các tác vụ đồng thời.
> - Nhiều tiến trình có thể chạy song song trên cùng một thiết bị.

Khi nhiều tiến trình chạy trên cùng một thiết bị, chúng có thể giao tiếp với nhau thông qua **các cơ chế giao tiếp liên tiến trình (Inter-Process Communication - IPC)** như: Bộ nhớ chung, Hàng đợi thông điệp, Sockets nội bộ, Đường ống dữ liệu, ... 

Khi các tiến trình chạy trên **các thiết bị khác nhau**, chúng phải giao tiếp **qua mạng**. Điều này được thực hiện thông qua **các giao thức truyền thông** như: TCP/UDP Socket, HTTP/HTTPS, REST API, WebSockets, ...

**Đối với Client-Server:** 
- **Tiến trình khách (Client Process)**
    - Chạy trên thiết bị của người dùng (end system).
    - **Khởi tạo kết nối** đến tiến trình server để yêu cầu dịch vụ.
    - Không cần địa chỉ IP cố định.
    - **Ví dụ:** Trình duyệt web của bạn gửi yêu cầu đến máy chủ web để tải trang web.

- **Tiến trình máy chủ (Server Process)**
    - Luôn hoạt động để **lắng nghe và xử lý yêu cầu** từ client.
    - Thường có địa chỉ IP cố định để client dễ dàng kết nối.
    - Có thể phục vụ nhiều client cùng lúc.
    - **Ví dụ:** Máy chủ web (Apache, Nginx) xử lý yêu cầu HTTP từ trình duyệt.

Giao tiếp giữa tiến trình và mạng được thực hiện thông qua **socket**, được xem như "cửa" kết nối của một tiến trình.

**Đối với P2P:**
- Mỗi peer có thể tạo tiến trình để gửi yêu cầu đến các peer khác (như một client).
- Đồng thời, nó cũng có tiến trình lắng nghe để phản hồi yêu cầu từ các peer khác (như một server)

---

# 📦 Dịch vụ vận chuyển sẵn có cho ứng dụng

Ứng dụng sử dụng giao diện socket để gửi và nhận thông điệp qua các giao thức vận chuyển do Internet cung cấp.

**Yêu cầu của giao tiếp:**
- **Tính bảo đảm:** Đảm bảo dữ liệu không bị mất mát hoặc thay đổi (đặc biệt với giao thức `TCP`).
- **Tốc độ & Độ trễ:** Một số ứng dụng yêu cầu giao tiếp theo thời gian thực (ví dụ: VoIP, game online).

> [!tip]- Mẹo
> Lựa chọn giữa `TCP` và `UDP` dựa trên tính chất ứng dụng:
> - `TCP`: Hỗ trợ kết nối định hướng và đảm bảo độ tin cậy.
> - - `UDP`: Ưu tiên tốc độ và thích hợp cho ứng dụng chấp nhận mất mát dữ liệu

---

# 🌐 Dịch vụ vận chuyển được cung cấp bởi Internet

Các giao thức vận chuyển chính:

**TCP (Transmission Control Protocol):**
- **Kết nối định hướng:** Yêu cầu quá trình bắt tay (handshaking) trước khi truyền dữ liệu.
- **Bảo đảm dữ liệu:** Đảm bảo dữ liệu được chuyển giao đầy đủ, đúng thứ tự.
- **Ví dụ:** Giao thức HTTP cho truy cập web, FTP cho truyền tệp (xem ).

- **UDP (User Datagram Protocol):**
- **Không kết nối:** Không yêu cầu quá trình bắt tay, do đó giảm độ trễ.
- **Không đảm bảo:** Dữ liệu có thể mất mát, không đảm bảo thứ tự.
- **Ví dụ:** Ứng dụng truyền thông thời gian thực như streaming video và VoIP.

> [!info] Lưu ý
> Khi phát triển ứng dụng, hãy cân nhắc yêu cầu của dịch vụ (độ tin cậy, độ trễ) để lựa chọn giao thức phù hợp.

---

# 📡 Giao thức ứng dụng
**Giao thức ứng dụng** xác định cách thức định dạng, truyền tải thông điệp và cách xử lý phản hồi giữa các tiến trình.

> [!example]- Vi dụ
> - **HTTP:** Dùng cho Web.
> - **SMTP:** Dùng cho email.
> - **FTP:** Dùng cho truyền tệp.
> - **SIP/RTP:** Dùng cho VoIP và video conferencing

**Yếu tố quan trọng:**
- **Cú pháp:** Các trường dữ liệu và cách phân tách.
- **Ngữ nghĩa:** Ý nghĩa của thông điệp.
- **Quy tắc tương tác:** Thứ tự gửi và nhận thông điệp.

> [!important]- Quan trọng
> Việc tuân thủ chuẩn giao thức (được định nghĩa trong các RFC) là yếu tố cần thiết để đảm bảo tính tương thích giữa các hệ thống.

---

# 🎉 Tổng kết

Chúng ta đã cùng nhau khám phá các khía cạnh cốt lõi về **nguyên tắc ứng dụng mạng**:

- **Kiến trúc ứng dụng:** Xác định mô hình **client-server** và **peer-to-peer** – mỗi mô hình có ưu, nhược điểm riêng.
- **Giao tiếp tiến trình:** Thông qua **socket**, tiến trình gửi nhận thông điệp một cách hiệu quả.
- **Dịch vụ vận chuyển:** Lựa chọn giữa **TCP** và **UDP** dựa trên yêu cầu độ tin cậy và thời gian phản hồi.
- **Giao thức ứng dụng:** Xác định định dạng và quy tắc giao tiếp giữa các ứng dụng như HTTP, SMTP, FTP,…

Việc hiểu rõ các nguyên tắc này không chỉ giúp bạn xây dựng các ứng dụng mạng hiện đại mà còn tạo nền tảng vững chắc để nắm bắt các công nghệ và giao thức mới trong tương lai. Hãy bắt đầu thực hành và tự tạo ra những ứng dụng đột phá của riêng bạn! 🚀
