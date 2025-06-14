---
date: 2025-04-02
draft: true
status: Doing
title: "UDP: Giao thức truyền tải không kết nối"
description: ""
author: PhDoanh
authorlink: https://github.com/PhDoanh
tags:
  - computer-networking
  - transport-layer
  - udp
  - connectionless
aliases:
  - connectionless transport udp
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
    src="images/connectionless-transport-udp.png"
    alt="UDP: giao thức vận chuyển không kết nối" 
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

# Giới thiệu
**UDP (User Datagram Protocol)** là một giao thức truyền tải cơ bản, không kết nối (có nghĩa là nó không yêu cầu thiết lập kết nối trước khi gửi dữ liệu) và được sử dụng rộng rãi trong mạng máy tính. Nó được định nghĩa trong [RFC 768] và có chức năng gần như tối thiểu, chỉ cung cấp hai dịch vụ chính là **multiplexing/demultiplexing** và một chút kiểm tra lỗi. Thực chất, **UDP** không thêm gì nhiều vào giao thức IP mà hầu như chỉ giúp ứng dụng gửi dữ liệu đến đúng nơi.

![[Pasted image 20250406145015.png|center|500]]

## Cách UDP hoạt động 🤔
Khi bạn muốn sử dụng UDP để gửi một thông điệp, thông điệp đó sẽ được chuyển trực tiếp từ ứng dụng đến giao thức UDP, và UDP chỉ cần thêm một vài trường dữ liệu (như số cổng nguồn và đích) rồi truyền đến lớp mạng. Lớp mạng sẽ đóng gói dữ liệu này thành một gói IP và cố gắng gửi nó đến máy đích. Nếu gói tin đến nơi, UDP sẽ dùng số cổng đích để chuyển dữ liệu đến đúng **ứng dụng nhận** trên máy đích đó.

> [!note] Lưu ý
> - Không có quá trình bắt tay (handshaking) giữa hai đầu giao thức trước khi gửi dữ liệu. Điều này làm cho UDP có thể gửi ngay lập tức mà không cần bất kỳ sự xác nhận nào trước khi bắt đầu.
> - UDP được sử dụng trong các ứng dụng yêu cầu thời gian thực, chẳng hạn như gọi điện Internet hay video trực tuyến 🎥📞.

## Vì sao lại chọn UDP? 🧐
Chắc chắn bạn đang thắc mắc tại sao lại chọn UDP thay vì TCP, dù TCP có khả năng truyền tải đáng tin cậy hơn. Dưới đây là những lý do khiến UDP vẫn được sử dụng:

1. **Điều khiển ứng dụng linh hoạt** 🕹️
	UDP cho phép ứng dụng quyết định chính xác dữ liệu nào được gửi và khi nào gửi. Điều này rất quan trọng đối với các ứng dụng yêu cầu truyền tải thời gian thực, chẳng hạn như video streaming hay gọi điện thoại qua mạng. TCP có cơ chế điều khiển tắc nghẽn, khiến dữ liệu bị trì hoãn nếu mạng quá tải, điều này không phù hợp với các ứng dụng yêu cầu tốc độ gửi dữ liệu ổn định.

2. **Không cần thiết lập kết nối** ⏳
	TCP yêu cầu thiết lập kết nối qua ba bước bắt tay trước khi truyền dữ liệu. UDP không cần bước này, giúp giảm độ trễ và gửi dữ liệu ngay lập tức. Đây là lý do tại sao DNS (Hệ thống phân giải tên miền) sử dụng UDP thay vì TCP. Nếu DNS sử dụng TCP, nó sẽ mất nhiều thời gian hơn.

3. **Không lưu trữ trạng thái kết nối** 🗃️
	TCP cần lưu trữ trạng thái kết nối, bao gồm các thông tin như bộ đệm gửi/nhận và các tham số kiểm soát tắc nghẽn. Điều này tốn tài nguyên và giới hạn số lượng kết nối mà máy chủ có thể xử lý. UDP không cần lưu trữ trạng thái, giúp các máy chủ hỗ trợ nhiều kết nối hơn.

4. **Tiết kiệm băng thông** 📉
	Một gói TCP có tiêu tốn ít nhất 20 byte cho phần tiêu đề (header), trong khi UDP chỉ cần 8 byte. Điều này giúp UDP tiết kiệm băng thông khi truyền tải dữ liệu.

> [!example]- Ví dụ
> - DNS: Truy vấn tên miền, không cần kết nối trước.
> - Video trực tuyến: Các ứng dụng như video gọi điện và streaming thường sử dụng UDP vì khả năng giảm độ trễ và xử lý thời gian thực tốt hơn.
> - Các ứng dụng mạng như RIP (Routing Information Protocol) hay SNMP (Simple Network Management Protocol) cũng sử dụng UDP.

## UDP và sự thiếu kiểm soát tắc nghẽn 🚧

Một điểm yếu lớn của UDP là không có cơ chế kiểm soát tắc nghẽn. Điều này có thể dẫn đến việc quá tải mạng nếu quá nhiều ứng dụng sử dụng UDP mà không có biện pháp kiểm soát. Trong trường hợp này, những gói UDP sẽ bị mất đi và làm giảm hiệu quả hoạt động của các giao thức khác, chẳng hạn như TCP.

---

# Cấu trúc của UDP Segment

![[Pasted image 20250406151347.png|center|500]]

Cấu trúc của một UDP segment bao gồm một header (tiêu đề) và một data field (trường dữ liệu). Dưới đây là một số thông tin cơ bản về cấu trúc của UDP segment:

UDP header bao gồm 4 trường, mỗi trường dài 2 byte (16 bit). Các trường này là:
1. **Port nguồn (Source Port)**: Xác định cổng nguồn gửi dữ liệu.
2. **Port đích (Destination Port)**: Xác định cổng đích nhận dữ liệu.
3. **Length (Chiều dài)**: Chỉ rõ tổng chiều dài của UDP segment (bao gồm cả header và dữ liệu).
4. **Checksum (Kiểm tra lỗi)**: Dùng để kiểm tra xem dữ liệu có bị lỗi khi truyền tải hay không.

## Data Field - Trường Dữ Liệu
Trường dữ liệu chứa thông tin ứng dụng mà chúng ta muốn gửi đi. Ví dụ:
- **DNS**: Trường dữ liệu sẽ chứa thông điệp truy vấn (query) hoặc phản hồi (response).
- **Ứng dụng streaming âm thanh**: Trường dữ liệu sẽ chứa các mẫu âm thanh (audio samples).

Đây chính là phần quan trọng nhất trong UDP segment, vì nó chứa thông tin ứng dụng mà người dùng cần truyền đi.

> [!tip]- Mẹo
> - **Checksum** giúp hệ thống nhận biết nếu có lỗi trong quá trình truyền tải gói tin UDP.
> - Trong thực tế, **checksum** không chỉ tính toán trên UDP segment mà còn tính toán trên một vài trường trong header của IP (IP header). Tuy nhiên, bạn không cần phải lo lắng về chi tiết này ngay bây giờ, vì chúng ta sẽ tập trung vào các khái niệm cơ bản.
> - Mặc dù **checksum** là công cụ kiểm tra lỗi hiệu quả, nhưng nó không đảm bảo 100% dữ liệu không bị lỗi. Đôi khi, một số lỗi nhỏ vẫn có thể không được phát hiện.

## UDP Segment Size

Trường **Length** trong UDP header cũng giúp xác định kích thước của gói tin UDP. Kích thước này sẽ bao gồm cả phần header (8 byte) và phần dữ liệu ứng dụng. Vì vậy, khi nhận được một gói tin UDP, hệ thống sẽ biết chính xác số byte mà nó cần xử lý, từ đó đảm bảo tính toàn vẹn và chính xác trong việc truyền nhận dữ liệu.

---

# Kiểm tra lỗi trong UDP
UDP (User Datagram Protocol) là một giao thức kết nối không tin cậy, nghĩa là nó không đảm bảo dữ liệu được gửi đi sẽ đến đúng đích và không bị thay đổi. Để phát hiện lỗi trong quá trình truyền tải, UDP sử dụng **Checksum** - một phương pháp kiểm tra lỗi đơn giản nhưng hiệu quả.

Mặc dù nhiều giao thức ở tầng liên kết (như Ethernet) đã có cơ chế kiểm tra lỗi, nhưng không phải tất cả các liên kết giữa nguồn và đích đều hỗ trợ kiểm tra lỗi. Điều này có thể dẫn đến việc bị lỗi trong quá trình truyền tải, như khi dữ liệu đi qua bộ nhớ của một router. Chính vì vậy, UDP cần một cơ chế kiểm tra lỗi ở tầng vận chuyển để đảm bảo tính toàn vẹn của dữ liệu trên toàn bộ đường truyền từ nguồn đến đích. Đây là một ví dụ điển hình của **nguyên lý end-to-end** trong thiết kế hệ thống.

## Cách tính toán Checksum trong UDP 🧮
**Checksum** trong UDP được tính bằng cách thực hiện phép cộng tất cả các từ 16-bit trong gói tin, và sau đó thực hiện phép bổ sung bù (1's complement) với kết quả cuối cùng.

Giả sử ta cộng ba từ 16-bit sau:
```
0110011001100000 (port nguồn)
0101010101010101 (port đích)
1000111100001100 (trường length)
----------------
0100101011000000
```

Lúc này, kết quả của phép cộng có **tràn số** (kết quả dư ra 1 bit thứ 17), và phần tràn này cần được "quấn lại" vào kết quả (cộng chính kết quả với bit dư). Sau khi quấn lại, ta có:

```
0100101011000001
```

**Thực hiện phép bổ sung bù (1’s complement)**: Chúng ta đổi tất cả các bit 0 thành 1, và các bit 1 thành 0:
```
1011010100111110 (checksum)
```

Đây chính là **checksum** của gói tin UDP!

## Kiểm tra lỗi ở phía người nhận 📡

Khi gói tin UDP đến người nhận, tất cả các từ 16-bit trong gói tin, bao gồm cả **checksum**, sẽ được cộng lại. Nếu không có lỗi, tổng của các từ 16-bit này sẽ bằng `1111111111111111`. Nếu một trong các bit là 0, thì chắc chắn đã có lỗi xảy ra trong quá trình truyền tải.

> [!info] Lưu ý
> - UDP không có cơ chế để sửa chữa lỗi mà chỉ phát hiện lỗi.
> - Nếu có lỗi, một số triển khai UDP sẽ loại bỏ gói tin bị lỗi, trong khi những triển khai khác có thể chuyển tiếp gói tin lỗi tới ứng dụng với cảnh báo.

---

# Các câu hỏi thường gặp

> [!question]- Làm thế nào để đảm bảo độ tin cậy khi dùng UDP? 
> Mặc dù UDP không đảm bảo độ tin cậy, các nhà phát triển có thể xây dựng cơ chế kiểm tra độ tin cậy trong ứng dụng của mình. Điều này có thể bao gồm việc thêm các cơ chế xác nhận và truyền lại gói tin khi cần thiết. Tuy nhiên, đây là một nhiệm vụ không hề đơn giản và có thể gây khó khăn trong quá trình phát triển ứng dụng.

> [!question]- Tại sao UDP không sửa lỗi mà chỉ phát hiện? 
> Một điểm cần lưu ý là, mặc dù UDP có khả năng phát hiện lỗi, nhưng nó không có cơ chế sửa chữa lỗi như trong TCP. Điều này giúp UDP giữ được tính đơn giản và nhanh chóng, phù hợp với những ứng dụng không yêu cầu độ tin cậy cao như truyền tải video trực tiếp hay chơi game trực tuyến.

---

# Tổng kết

**UDP (User Datagram Protocol)** là một giao thức truyền tải đơn giản, nhanh và không kết nối. Nó không đảm bảo dữ liệu đến đúng nơi hay đúng thứ tự, nhưng đổi lại mang lại tốc độ và độ trễ thấp, phù hợp cho các ứng dụng thời gian thực như gọi điện, video streaming, DNS hay các giao thức quản lý mạng.

**Những điểm nổi bật**:
- **Không cần thiết lập kết nối** trước khi truyền dữ liệu ⇒ giúp giảm độ trễ.
- **Không lưu trạng thái phiên** ⇒ tiết kiệm tài nguyên hệ thống, hỗ trợ nhiều client hơn.
- **Không kiểm soát tắc nghẽn** ⇒ ứng dụng phải tự đảm bảo không làm quá tải mạng.
- **Tiêu đề nhỏ gọn (8 byte)** ⇒ tiết kiệm băng thông.
- **Có checksum** để phát hiện lỗi ⇒ đảm bảo dữ liệu không bị hỏng trên đường đi.

**Checksum – vũ khí nhỏ mà có võ**:
- Dùng phép **cộng tất cả các từ 16-bit**, sau đó lấy **bù 1** để tạo ra checksum.
- Nếu phép cộng bị **tràn 17-bit**, bit dư sẽ được **quấn lại (wrap around)** vào kết quả.
- Ở phía nhận, nếu **tổng tất cả các từ (kể cả checksum)** là toàn 1 (`0xFFFF`), thì gói tin được xem là **không lỗi**.

UDP không hoàn hảo, nhưng cực kỳ hữu ích trong những ngữ cảnh cần **tốc độ**, **tối giản**, và **kiểm soát ở ứng dụng**. Hiểu rõ đặc điểm và cơ chế kiểm tra lỗi của UDP giúp bạn chọn đúng công cụ cho đúng công việc – một kỹ năng quan trọng với bất kỳ kỹ sư mạng hay lập trình viên hệ thống nào.