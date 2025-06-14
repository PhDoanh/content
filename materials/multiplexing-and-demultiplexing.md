---
date: 2025-04-02
draft: true
status: Doing
title: "Cơ chế ghép kênh và phân kênh trong tầng giao vận"
description: ""
author: PhDoanh
authorlink: https://github.com/PhDoanh
tags: 
  - computer-networking
  - transport-layer
  - multiplexing
  - demultiplexing
aliases:
  - multiplexing and demultiplexing
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
    src="images/multiplexing-and-demultiplexing.png"
    alt="Cơ chế ghép kênh và phân kênh trong tầng giao vận" 
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

# Giới thiệu 👀

Trong tầng **transport** của mô hình mạng, nhiệm vụ mở rộng dịch vụ giao tiếp từ **host-to-host** (máy chủ tới máy chủ) của tầng **mạng** thành dịch vụ giao tiếp **process-to-process** (tiến trình tới tiến trình) cho các ứng dụng đang chạy trên máy tính. Điều này cho phép nhiều ứng dụng hoạt động đồng thời mà không bị nhầm lẫn dữ liệu.

Khi một gói dữ liệu (segment) được chuyển từ tầng mạng tới máy tính đích, tầng **transport** sẽ nhận gói tin đó và phải chuyển tiếp dữ liệu đến đúng tiến trình ứng dụng thông qua một **socket**. Hãy tưởng tượng bạn đang sử dụng máy tính để tải trang web trong khi cùng lúc mở một phiên **FTP** và hai phiên **Telnet**. Trong trường hợp này, máy tính của bạn đang chạy bốn tiến trình ứng dụng khác nhau:
- Hai tiến trình **Telnet**
- Một tiến trình **FTP**
- Một tiến trình **HTTP**

Để đảm bảo dữ liệu đến đúng tiến trình, mỗi **socket** được gán một số hiệu cổng (**port**). Trong các giao thức như `UDP` và `TCP`, mỗi đoạn dữ liệu được thêm vào các trường số cổng nguồn và số cổng đích. Tầng **transport** sẽ kiểm tra số cổng đích để thực hiện quá trình **demultiplexing** – tức là chuyển dữ liệu đến đúng **socket** tương ứng. Ngược lại, quá trình **multiplexing** tại nguồn sẽ gom dữ liệu từ các tiến trình khác nhau, đóng gói chúng thành các đoạn dữ liệu với thông tin số cổng phù hợp rồi gửi xuống tầng mạng.

![[Pasted image 20250402163125.png|center|500]]

> [!info]- Lưu ý
> - Mỗi số cổng là một số nguyên 16-bit, có giá trị từ 0 đến 65535.
> - Các số cổng từ 0 đến 1023 được gọi là `well-known ports` và dành riêng cho các giao thức tiêu chuẩn như `HTTP` (port 80) và `FTP` (port 21).

Nhờ các cơ chế trên, khi một đoạn dữ liệu đến, tầng **transport** có thể dễ dàng xác định:
- **Socket** nào sẽ nhận dữ liệu dựa vào trường số cổng đích.
- Dữ liệu được chuyển tiếp đúng tiến trình mà không nhầm lẫn giữa các ứng dụng khác nhau.

> [!example]- Ví dụ
> - Một gói tin có số cổng đích là **80** sẽ được chuyển đến **socket** của tiến trình **HTTP**.
> - Nếu có nhiều tiến trình đang chạy cùng lúc, tầng **transport** sẽ dựa vào số cổng để phân loại và chuyển dữ liệu đến từng tiến trình tương ứng.

Các nguyên tắc về **multiplexing** và **demultiplexing** không chỉ áp dụng cho giao thức Internet mà còn là cơ chế chung cho các giao thức mạng khác, giúp duy trì sự phân chia rõ ràng giữa các dịch vụ và tiến trình xử lý dữ liệu.

> [!tip]- Mẹo
> - Khi lập trình, sử dụng các từ khóa như `UDP`, `TCP`, và `socket` để khai báo rõ ràng kiểu giao thức và quản lý số cổng.
> - Đảm bảo mỗi `socket` được gán một số cổng duy nhất để tránh xung đột khi nhiều tiến trình cùng giao tiếp.

> [!caution]- Cảnh báo
> Không nên sử dụng các số cổng trong dải `well-known` (0-1023) cho các ứng dụng riêng, trừ khi cần tương tác với các giao thức tiêu chuẩn, để tránh gây ra sự cố giao tiếp hoặc vi phạm tiêu chuẩn.

---

# Ghép và phân kênh trong UDP 🚀
Khi lập trình với `UDP`, bạn có thể tạo một socket UDP trong Python bằng lệnh:
```python
clientSocket = socket(socket.AF_INET, socket.SOCK_DGRAM)
```

## Quá trình tự động gán số cổng
**Tự động gán số cổng**: Khi socket UDP được tạo ra, tầng transport sẽ tự động gán một số cổng thuộc khoảng từ 1024 đến 65535 (các số cổng chưa được sử dụng trên host).

**Gán số cổng cụ thể**: Nếu muốn, bạn có thể gán số cổng cụ thể cho socket bằng cách sử dụng phương thức `bind()` như sau:

```python
clientSocket.bind(('', 19157))
```

Điều này thường được sử dụng ở phía server cho các giao thức "well-known", trong khi phía client thường để hệ thống tự động chọn số cổng.

## Quá trình ghép và phân kênh
**Multiplexing (ghi gộp dữ liệu)**:
- Khi một tiến trình ở Host A, với số cổng UDP 19157, muốn gửi dữ liệu đến tiến trình ở Host B có số cổng 46428, tầng transport của Host A tạo ra một đoạn dữ liệu (segment) chứa:
    - Dữ liệu ứng dụng
    - Số cổng nguồn: 19157
    - Số cổng đích: 46428
    - Các trường khác (sẽ bàn ở phần sau)

- Sau đó, đoạn này được chuyển xuống tầng mạng, đóng gói trong một IP datagram và cố gắng chuyển đến Host B.

**Demultiplexing (tách dữ liệu)**:
- Khi Host B nhận được đoạn dữ liệu, tầng transport của Host B sẽ xem số cổng đích trong đoạn dữ liệu (46428) và chuyển dữ liệu đó đến socket tương ứng đã được gán số cổng 46428.

- Một socket UDP được định danh hoàn toàn bởi một cặp số (destination IP, destination port). Điều này có nghĩa là, nếu hai đoạn UDP có cùng số cổng đích thì dù nguồn IP hay nguồn port có khác nhau, chúng vẫn được chuyển đến cùng một tiến trình qua socket đó.

> [!info]- Lưu ý
> - Các số cổng là các số nguyên 16-bit, giá trị từ 0 đến 65535
> - Các số cổng từ 0 đến 1023 được gọi là `well-known ports` và dành riêng cho các giao thức tiêu chuẩn (ví dụ: `HTTP` sử dụng port 80, `FTP` sử dụng port 21). 😊

---

# Ghép và phân kênh trong TCP 🔐
Khác với UDP, khi sử dụng TCP, một socket được định danh bởi một **bộ 4 giá trị** (four-tuple): source IP, source port, destination IP, destination port

## Quá trình thiết lập kết nối và định danh socket TCP
**Khởi tạo kết nối**:
Ví dụ, ở phía client, bạn tạo socket TCP và thực hiện kết nối với server:

```python
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, 12000))
```

Tại server, một socket "chờ" (welcoming socket) lắng nghe kết nối trên số cổng 12000
Khi server nhận được yêu cầu kết nối, nó sẽ thực hiện lệnh:

```python
connectionSocket, addr = serverSocket.accept()
```

Ở đây, hệ thống tạo ra một socket mới được định danh bởi bốn giá trị: Số cổng nguồn và IP của client, Số cổng đích và IP của server

## Quá trình ghép và phân kênh

**Multiplexing**:
- Khi dữ liệu được gửi từ client đến server, hệ thống đóng gói thông tin gồm:
    - Số cổng nguồn (được client chọn)
    - Số cổng đích (server đã chỉ định, ví dụ 12000)
    - IP của client và server
- Tất cả các thông tin này giúp định danh chính xác kết nối.

**Demultiplexing**:
- Khi một TCP segment đến, hệ thống sẽ sử dụng toàn bộ thông tin của bộ 4 giá trị để xác định socket nhận dữ liệu.
- **Trường hợp đặc biệt**: Nếu hai TCP segment có cùng số cổng đích nhưng khác ở IP hoặc số cổng nguồn, chúng sẽ được chuyển đến các socket khác nhau vì bộ 4 giá trị là duy nhất.

![[Pasted image 20250402170038.png|center|500]]

> [!example]- Ví dụ
> ![[Pasted image 20250402165949.png|center|500]]
> - Giả sử Host C mở hai phiên HTTP đến server B với các số cổng nguồn khác nhau (ví dụ: 26145 và 7532).
> - Trong khi đó, Host A có thể mở một phiên HTTP với số cổng nguồn 26145 nhưng vì IP của Host A khác với Host C, nên các kết nối sẽ không bị nhầm lẫn. 🌐

> [!tip]- Mẹo nhỏ
> - Khi phát triển ứng dụng TCP, hãy chú ý đến việc kiểm tra toàn bộ bộ 4 giá trị khi thiết lập và quản lý các kết nối. Điều này giúp đảm bảo rằng dữ liệu được truyền đúng đích. 🚀

---

# Máy chủ Web và giao thức TCP 🖥️

Khi một host chạy một Web server, chẳng hạn như Apache, thì Web server đó thường lắng nghe tại **port 80**. Điều này có nghĩa là, tất cả các phân đoạn (segment) được gửi từ trình duyệt (hay các client khác) đến Web server đều có số cổng đích là 80. Các phân đoạn này có thể là các phân đoạn để thiết lập kết nối ban đầu hoặc các phân đoạn chứa thông điệp HTTP request.

## Cách Web Server Phân Biệt Các Kết Nối

**Phân biệt dựa trên source IP và source port**:  
Mặc dù tất cả các phân đoạn đến đều có số cổng đích 80, nhưng Web server phân biệt các kết nối từ các client khác nhau nhờ vào:
- Địa chỉ IP nguồn của client
- Số cổng nguồn của client

## Quá Trình Xử Lý Kết Nối

Truyền thống, một Web server sẽ tạo ra một tiến trình (process) mới cho mỗi kết nối. Mỗi tiến trình này có một **connection socket** riêng để nhận các HTTP request và gửi lại HTTP response. Tuy nhiên, thực tế hiện nay:

Các Web server hiệu năng cao thường sử dụng **một tiến trình duy nhất** và tạo ra **các thread** (luồng nhẹ) riêng cho từng kết nối thay vì tạo một tiến trình mới cho mỗi kết nối. Điều này giúp tiết kiệm tài nguyên hệ thống và tăng tốc độ xử lý. 🚀

Trong trường hợp:
- **HTTP persistent**: Client và server trao đổi các thông điệp HTTP qua **cùng một server socket** trong suốt phiên kết nối.
- **HTTP non-persistent**:
    - Mỗi yêu cầu/phản hồi HTTP được thực hiện qua một kết nối TCP riêng biệt, do đó sẽ tạo ra một socket mới cho mỗi giao dịch.
    - Việc tạo và đóng socket liên tục có thể ảnh hưởng tiêu cực đến hiệu năng của một Web server bận rộn, mặc dù có nhiều kỹ thuật trong hệ điều hành để giảm thiểu vấn đề này.

> [!caution]- Cảnh báo
> - Nếu sử dụng HTTP non-persistent, việc tạo và đóng kết nối liên tục có thể làm giảm hiệu năng của Web server, nhất là khi số lượng kết nối lớn.
> - Cần cân nhắc sử dụng HTTP persistent hoặc các kỹ thuật tối ưu khác để đảm bảo hiệu suất.

---

# Các câu hỏi thường gặp ❓

> [!caution]- Nội dung đang hoàn thiện
> Quá trình xây dựng nội dung này có thể mất nhiều thời gian ⌛, nhưng bạn có thể thúc đẩy nó bằng cách tham gia [[article-collaboration-guide|cộng tác bài viết]] 🤝
> 
> **Rất mong sự thông cảm của các bạn 🙏**

---

# Tổng kết 🎉

> [!caution]- Nội dung đang hoàn thiện
> Quá trình xây dựng nội dung này có thể mất nhiều thời gian ⌛, nhưng bạn có thể thúc đẩy nó bằng cách tham gia [[article-collaboration-guide|cộng tác bài viết]] 🤝
> 
> **Rất mong sự thông cảm của các bạn 🙏**

