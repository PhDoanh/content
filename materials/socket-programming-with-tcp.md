---
date: 2025-03-22
draft: false
status: Doing
title: Lập trình ứng dụng mạng với TCP
description: "Khám phá cách thiết lập và vận hành kết nối TCP thông qua lập trình socket. Bài viết hướng dẫn chi tiết cách tạo kết nối, xử lý handshake và giao tiếp giữa client và server với ví dụ Python thực tế."
author: PhDoanh
authorlink: https://github.com/PhDoanh
tags:
  - computer-networking
  - application-layer
  - tcp
  - socket-programming
aliases:
  - socket programming with tcp
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
    src="images/socket-programming-with-tcp.png"
    alt="Lập trình ứng dụng mạng với TCP" 
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

Trong bài viết này, chúng ta sẽ cùng tìm hiểu về **socket programming với TCP** – một giao thức kết nối theo kiểu connection-oriented giúp đảm bảo dữ liệu được truyền một cách **tin cậy** giữa các ứng dụng. Qua đó, bạn sẽ hiểu được quá trình **handshake** ba bước, cách tạo socket cho client và server, cũng như xem qua các ví dụ mã nguồn minh họa bằng Python.

# Giới thiệu

**TCP (Transmission Control Protocol)** là một giao thức **đáng tin cậy** cho việc truyền tải dữ liệu. Trước khi dữ liệu được gửi đi, TCP yêu cầu thiết lập một kết nối giữa client và server thông qua quá trình **three-way handshake**. Điều này giúp đảm bảo rằng cả hai bên đều sẵn sàng giao tiếp và dữ liệu sẽ được chuyển đúng thứ tự.

> [!info] Lưu ý
> - **TCP** đảm bảo tất cả các byte được truyền đến nơi nhận và theo đúng thứ tự.  
> - **UDP** thì không như vậy; nó phù hợp với ứng dụng yêu cầu tốc độ cao nhưng không cần độ tin cậy tuyệt đối.

---

# Kết nối Connection-Oriented

Khi sử dụng TCP, trước khi trao đổi dữ liệu, client phải thực hiện các bước sau:

1. **Bắt tay ba bước:**  
	- **SYN:** Client gửi yêu cầu kết nối tới server.  
	- **SYN-ACK:** Server phản hồi đồng ý kết nối và gửi lại xác nhận.  
	- **ACK:** Client gửi xác nhận cuối cùng, kết nối được thiết lập.

2. **Tạo socket kết nối:**  
	- **Client socket:** Sử dụng `socket(AF_INET, SOCK_STREAM)` để tạo socket TCP.
	- **Server socket:** Server tạo một socket "chào đón" (welcoming socket) và gán một port cố định (ví dụ: `12000`) để lắng nghe kết nối.

> [!tip]- Mẹo
> Sử dụng [tài liệu Python socket](https://docs.python.org/3/library/socket.html) để hiểu sâu hơn về các hàm và tham số liên quan.

---

# Giao tiếp giữa client và server

Sau khi kết nối được thiết lập, TCP cho phép:
- **Client gửi dữ liệu:** Dữ liệu được "drop" trực tiếp vào kết nối TCP qua socket, không cần gắn địa chỉ đích như UDP.
- **Server xử lý và phản hồi:** Server nhận dữ liệu qua socket riêng được tạo ra sau khi client "gõ cửa" và xử lý nó (ví dụ: chuyển thành chữ in hoa), cuối cùng là gửi lại phản hồi.

> [!caution] Cảnh báo
> Việc đóng socket đúng cách sau khi giao tiếp xong là rất quan trọng để giải phóng tài nguyên và tránh lỗi kết nối.

Ví dụ dưới đây minh họa cách client thiết lập kết nối TCP, gửi dữ liệu và nhận phản hồi từ server:

```python title="TCPClient.py" {}
from socket import *

serverName = 'servername'  # Thay bằng địa chỉ IP hoặc hostname của server
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)

# Thiết lập kết nối TCP đến server
clientSocket.connect((serverName, serverPort))

# Nhập dữ liệu từ bàn phím
sentence = raw_input('Input lowercase sentence: ')

# Gửi dữ liệu tới server thông qua kết nối TCP
clientSocket.send(sentence)

# Nhận dữ liệu từ server (dữ liệu đã được xử lý, ví dụ: chuyển thành chữ in hoa)
modifiedSentence = clientSocket.recv(1024)
print 'From Server:', modifiedSentence

# Đóng kết nối sau khi giao tiếp xong
clientSocket.close()
```

> [!explain]- Giải thích
> - Sử dụng `AF_INET` để chỉ định IPv4 và `SOCK_STREAM` để tạo socket TCP.
> - Hàm `connect()` thực hiện quá trình handshake, thiết lập kết nối giữa client và server.

**Server** sẽ tạo một socket "chào đón", lắng nghe và chấp nhận kết nối từ client, sau đó xử lý dữ liệu và gửi phản hồi:

```python title="TCPServer.py" {}
from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)

# Gán port cho socket của server để nhận kết nối
serverSocket.bind(('', serverPort))

# Lắng nghe kết nối từ client (số lượng kết nối tối đa trong hàng đợi là 1)
serverSocket.listen(1)
print 'The server is ready to receive'

while True:
    # Chấp nhận kết nối từ client, tạo một socket mới dành riêng cho kết nối đó
    connectionSocket, addr = serverSocket.accept()
    
    # Nhận dữ liệu từ client
    sentence = connectionSocket.recv(1024)
    
    # Xử lý dữ liệu: chuyển đổi chuỗi thành chữ in hoa
    capitalizedSentence = sentence.upper()
    
    # Gửi phản hồi về client
    connectionSocket.send(capitalizedSentence)
    
    # Đóng socket kết nối sau khi giao tiếp xong
    connectionSocket.close()
```

> [!explain]- Giải thích
> - `bind()` gán một port cố định cho server, giúp client biết nơi để kết nối.
> - `listen()` tạo socket chào đón, cho phép server lắng nghe nhiều kết nối liên tiếp.
> - `accept()` tạo ra một socket mới (connection socket) dành riêng cho từng kết nối, đảm bảo quá trình giao tiếp độc lập giữa client và server.

> [!tip]- Mẹo
> - **Đóng socket:** Luôn đóng socket sau khi giao tiếp xong để tránh rò rỉ tài nguyên.
> - **Timeout và kiểm tra lỗi:** Thiết lập timeout cho socket và xử lý lỗi thích hợp giúp tăng tính ổn định cho ứng dụng.

---

# Các câu hỏi thường gặp

> [!caution]- Nội dung đang hoàn thiện
> Quá trình xây dựng nội dung này có thể mất nhiều thời gian ⌛, nhưng bạn có thể thúc đẩy nó bằng cách tham gia [[article-collaboration-guide|cộng tác bài viết]] 🤝
> 
> **Rất mong sự thông cảm của các bạn 🙏**

---

# Tổng kết

Bài viết đã tóm tắt lại những kiến thức cơ bản về **socket programming với TCP** bao gồm:
- **Quá trình handshake:** Thiết lập kết nối giữa client và server qua **three-way handshake**.
- **Thiết lập socket:** Sự khác biệt giữa socket TCP và UDP, cùng với ví dụ mã nguồn cụ thể.
- **Giao tiếp tin cậy:** Cách TCP đảm bảo dữ liệu được truyền đi **đầy đủ** và **đúng thứ tự**.

Hy vọng rằng với bài viết này, bạn đã nắm được cơ bản về **TCP socket programming** và có thể áp dụng vào các dự án của mình. Đừng quên truy cập [tài liệu Python socket](https://docs.python.org/3/library/socket.html) để cập nhật thêm các kỹ thuật nâng cao và mẹo tối ưu khi phát triển ứng dụng mạng. Chúc bạn thành công! 🎉
