---
date: 2025-04-02
draft: true
status: Doing
title: "Giới thiệu về tầng giao vận và các dịch vụ của nó"
description: ""
author: PhDoanh
authorlink: https://github.com/PhDoanh
tags: 
  - computer-networking
  - transport-layer
  - services
aliases:
  - introduction and transport layer services
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
    src="images/introduction-and-transport-layer-services.png"
    alt="Giới thiệu về tầng giao vận và các dịch vụ của nó" 
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

# Giới thiệu về Transport Layer 🚀

Trong hệ thống mạng máy tính, **transport layer** đóng vai trò quan trọng trong việc cung cấp giao tiếp logic giữa các tiến trình ứng dụng chạy trên các host khác nhau. Điều này có nghĩa là, từ góc nhìn của ứng dụng, các host dường như được kết nối trực tiếp, mặc dù thực tế chúng có thể nằm ở những vị trí địa lý cách xa nhau, được liên kết qua hàng loạt router và nhiều loại liên kết khác nhau.

> [!info]- Lưu ý
> - **Giao tiếp logic**: Ứng dụng không cần quan tâm đến chi tiết đường truyền vật lý, mà chỉ tập trung vào việc gửi và nhận thông điệp.
> - Transport layer **được cài đặt trên các hệ thống cuối** (end systems), chứ không phải trên các router trong mạng.
> - Router chỉ xử lý các trường thông tin của **network layer** (ví dụ: địa chỉ IP) trong gói dữ liệu, mà không can thiệp vào các trường của **transport-layer segment**.

---

# Quy trình xử lý dữ liệu trong Transport Layer 🔄

Khi một ứng dụng gửi dữ liệu, transport layer sẽ thực hiện các bước sau:
1. **Nhận và phân mảnh thông điệp ứng dụng**
    - Ứng dụng tạo ra một thông điệp lớn.
    - Transport layer có thể chia nhỏ thông điệp này thành các đoạn nhỏ hơn nếu cần.
2. **Tạo và đính kèm header**
    - Mỗi đoạn nhỏ được gọi là `transport-layer segment`.
    - Transport layer thêm một **header** chứa các thông tin cần thiết (như số hiệu cổng, số thứ tự, v.v.) để đảm bảo dữ liệu được chuyển đến đúng đích.
3. **Chuyển giao cho Network Layer**
    - Các segment này được đóng gói vào trong một **datagram** ở network layer.
    - Các router trên đường truyền chỉ xử lý các trường thông tin của datagram (như địa chỉ IP) mà không "nhìn" vào thông tin bên trong segment.
4. **Nhận dữ liệu ở phía đích**
    - Ở hệ thống đích, network layer trích xuất các segment và chuyển giao cho transport layer.
    - Transport layer xử lý các segment nhận được và ghép lại để tái tạo thông điệp ban đầu, sau đó chuyển giao cho ứng dụng.

---

# Các giao thức Transport Layer chủ yếu 📡

Trên Internet, có ít nhất hai giao thức transport layer được sử dụng phổ biến:
- `TCP` (Transmission Control Protocol):
    - **Đảm bảo kết nối tin cậy**: Dữ liệu được truyền đi theo thứ tự và không bị mất.
    - **Kiểm soát lưu lượng**: Giúp điều chỉnh tốc độ truyền dữ liệu giữa các host.
- `UDP` (User Datagram Protocol):
    - **Không đảm bảo kết nối tin cậy**: Dữ liệu có thể đến không theo thứ tự hoặc bị mất.
    - **Phù hợp với các ứng dụng yêu cầu tốc độ cao**: Ví dụ như streaming video, chơi game trực tuyến, v.v.

> [!tip]- Mẹo
> - Sử dụng `TCP` khi bạn cần đảm bảo dữ liệu truyền đi phải chính xác và theo đúng thứ tự.
> - Sử dụng `UDP` cho các ứng dụng mà tốc độ truyền tải là ưu tiên hàng đầu, và mất mát dữ liệu không gây ảnh hưởng nghiêm trọng.

---

# Mối quan hệ giữa Transport Layer và Network Layer 📡

![[Pasted image 20250402161622.png|center|500]]

Trong hệ thống mạng máy tính, **transport layer** nằm ngay trên **network layer** trong mô hình giao thức. Hai tầng này đều cung cấp giao tiếp logic nhưng cho các đối tượng khác nhau:

- **Network layer**: Đảm bảo giao tiếp logic giữa các **host** (các máy tính hay thiết bị đầu cuối).
- **Transport layer**: Đảm bảo giao tiếp logic giữa các **tiến trình ứng dụng** chạy trên các host.

Để hiểu sự khác biệt này một cách sinh động, ta hãy xem xét một ví dụ minh họa với một phép ẩn dụ về hộ gia đình:

Hãy tưởng tượng có hai căn nhà, một ở Bờ Đông và một ở Bờ Tây. Mỗi căn nhà đều có một đại gia đình gồm 12 đứa trẻ (các tiến trình ứng dụng). Các đứa trẻ ở hai gia đình đều yêu thích việc gửi thư cho nhau:
- **Thư từ** đại diện cho **tin nhắn ứng dụng** được gửi đi.
- Mỗi bức thư được đóng gói riêng trong một phong bì, tương tự như **application message** được đóng gói thành các **segment** của transport layer.

Trong mỗi gia đình, có một đứa trẻ được giao nhiệm vụ thu gom và phân phối thư từ:
- Ở nhà Bờ Tây, đó là **Ann**.
- Ở nhà Bờ Đông, đó là **Bill**.

> [!example]- Ví dụ
> - **Ann và Bill**: Đại diện cho các giao thức transport layer, chịu trách nhiệm nhận và chuyển giao thư từ giữa các đứa trẻ (các tiến trình ứng dụng) trong cùng một căn nhà.
> - **Dịch vụ bưu điện**: Đại diện cho network layer, chịu trách nhiệm chuyển thư giữa các căn nhà (host) mà không quan tâm thư nội bộ trong từng gia đình.

Khi thư được gửi đi:

1. **Dịch vụ bưu điện (Network Layer)** chịu trách nhiệm chuyển thư từ nhà này sang nhà khác.
    - Các bưu tá chỉ quan tâm đến việc di chuyển các phong bì dựa vào địa chỉ (giống như các router xử lý thông tin địa chỉ IP).
2. **Ann và Bill (Transport Layer)** thực hiện công việc thu gom và phân phối thư trong nội bộ căn nhà.
    - Họ nhận thư từ bưu tá và sau đó phát cho từng đứa trẻ.
    - Với góc nhìn của các đứa trẻ, Ann và Bill chính là "dịch vụ thư tín" của gia đình.

> [!info]- Lưu ý
> - Transport layer chỉ thực hiện công việc trong nội bộ các **host** và không can thiệp vào quá trình chuyển thư của dịch vụ bưu điện.
> - Điều này giúp tách biệt rõ ràng nhiệm vụ giữa việc chuyển giao dữ liệu qua mạng (network layer) và việc xử lý dữ liệu giữa các tiến trình ứng dụng (transport layer).

---

# Tác động của Dịch vụ Mạng đến Transport Layer ⚙️

Cũng như cách mà Ann và Bill phụ thuộc vào dịch vụ bưu điện để chuyển thư giữa các căn nhà, thì các giao thức transport layer cũng bị ràng buộc bởi các đặc tính của giao thức network layer. Ví dụ:

- Nếu dịch vụ bưu điện không đảm bảo thời gian giao thư cụ thể (ví dụ, tối đa 3 ngày), thì Ann và Bill cũng không thể đảm bảo rằng các bức thư của các đứa trẻ sẽ được nhận trong thời gian quy định.
- Tương tự, nếu network layer không đảm bảo về độ trễ hay băng thông, thì transport layer cũng không thể cung cấp các đảm bảo về độ trễ hay băng thông cho tin nhắn ứng dụng.

> [!caution]- Cảnh báo
> - Không nên nhầm lẫn giữa việc **giao tiếp giữa các host** (network layer) với **giao tiếp giữa các tiến trình ứng dụng** (transport layer).
> - Mỗi tầng có vai trò và giới hạn riêng, phụ thuộc lẫn nhau nhưng không trộn lẫn chức năng.

Dù cho network layer có thể không đảm bảo một số dịch vụ nhất định (như độ trễ hay bảo mật), transport layer vẫn có thể cung cấp một số dịch vụ bổ sung:

- **Chuyển giao dữ liệu tin cậy**: Transport layer có thể sử dụng các cơ chế như kiểm tra lỗi, đánh số thứ tự, và xác nhận nhận dữ liệu để đảm bảo dữ liệu không bị mất hoặc sai thứ tự, ngay cả khi network layer không tin cậy.
- **Bảo mật thông tin**: Transport layer có thể áp dụng mã hóa để đảm bảo rằng dữ liệu không bị đọc trộm, mặc dù network layer không đảm bảo tính bảo mật.

> [!suggest]- Gợi ý
> - Khi thiết kế ứng dụng, hãy cân nhắc lựa chọn giao thức transport phù hợp dựa trên dịch vụ mà network layer có thể cung cấp.
> - Ví dụ, nếu yêu cầu bảo mật cao, có thể áp dụng thêm lớp mã hóa ở transport layer.

---

# Hai Giao Thức Giao Vận: UDP và TCP ⚖️
Trong một mạng Internet hay nói chung là mạng TCP/IP, ứng dụng luôn có hai giao thức tầng Giao Vận để lựa chọn: `UDP` và `TCP`.

- **UDP (User Datagram Protocol)**
    - `UDP` cung cấp một dịch vụ giao tiếp kiểu _connectionless_ (không cần kết nối) cho ứng dụng.
    - Nó chỉ đảm bảo việc chuyển giao dữ liệu từ quá trình gửi đến quá trình nhận thông qua kiểm tra lỗi cơ bản (ví dụ: trường kiểm tra lỗi trong header).
    - Không có cơ chế đảm bảo dữ liệu đến đúng thứ tự hoặc được chuyển giao đầy đủ.

> [!info]- Lưu ý
> - `UDP` thích hợp cho các ứng dụng yêu cầu tốc độ cao và chấp nhận mất mát dữ liệu (ví dụ: streaming video, game trực tuyến).
> - Khi tạo _socket_ trong ứng dụng, lập trình viên sẽ chọn `UDP` nếu không cần bảo đảm độ tin cậy cao.

- **TCP (Transmission Control Protocol)**
    - `TCP` cung cấp một dịch vụ kiểu _connection-oriented_ (có kết nối) cho ứng dụng.
    - Nó sử dụng các kỹ thuật như số thứ tự, xác nhận nhận dữ liệu, bộ đếm thời gian, và điều khiển lưu lượng để đảm bảo dữ liệu được truyền đúng và đầy đủ từ quá trình gửi đến quá trình nhận.
    - `TCP` còn tích hợp cơ chế kiểm soát tắc nghẽn để không làm quá tải các liên kết và router trên đường truyền.

> [!tip]- Mẹo
> - Sử dụng `TCP` cho các ứng dụng đòi hỏi độ tin cậy cao như truyền tải tệp, gửi email, hoặc web browsing.
> - Các ứng dụng yêu cầu tốc độ ưu tiên có thể chọn `UDP` mặc dù rủi ro mất gói dữ liệu cao hơn.

---

# Cách Đặt Tên Gói Dữ Liệu Trong Internet 📦

Để đơn giản hoá thuật ngữ, trong bối cảnh Internet:
- Các gói dữ liệu ở tầng Giao Vận thường được gọi là **segment**.
- Còn gói dữ liệu ở tầng mạng thường được gọi là **datagram**.

> [!info]- Lưu ý
> - một số tài liệu cũng có thể gọi gói UDP là datagram, nhưng để tránh nhầm lẫn, chúng ta chỉ sử dụng từ **segment** cho cả TCP và UDP.
> - Việc thống nhất cách đặt tên giúp học sinh dễ hình dung sự khác biệt giữa các tầng trong mô hình TCP/IP.

---

# Vai Trò của Tầng Mạng (Network Layer) 📶

**IP (Internet Protocol)**:
- Là giao thức ở tầng mạng, IP cung cấp giao tiếp giữa các **host** (máy tính hay thiết bị đầu cuối) theo kiểu "best effort" – tức là cố gắng hết sức để giao dữ liệu nhưng **không đảm bảo** việc giao dữ liệu đúng thứ tự, đầy đủ hay không bị lỗi.
- Mỗi host có ít nhất một địa chỉ IP, được dùng để định danh khi giao tiếp trên Internet.

> [!caution]- Cảnh báo
> Vì IP là một dịch vụ không đảm bảo, nên các giao thức Giao Vận như `TCP` cần phải bổ sung cơ chế tin cậy để đảm bảo dữ liệu không bị mất hay sai thứ tự.

---

# Ghép kênh và Phân kênh 🔗

**Multiplexing:**
- Là quá trình mở rộng giao tiếp từ mức host-to-host (máy này đến máy khác) lên mức process-to-process (tiến trình này đến tiến trình khác).
- Khi một host gửi nhiều luồng dữ liệu từ các ứng dụng khác nhau, `UDP` và `TCP` sẽ gắn thêm thông tin (như số hiệu cổng) vào header của mỗi segment để phân biệt các tiến trình ứng dụng.

**Demultiplexing:** Là quá trình tại host nhận, giúp phân phối dữ liệu đến đúng tiến trình ứng dụng dựa trên thông tin trong header.

---

# Các câu hỏi thường gặp ❓

> [!caution]- Nội dung đang hoàn thiện
> Quá trình xây dựng nội dung này có thể mất nhiều thời gian ⌛, nhưng bạn có thể thúc đẩy nó bằng cách tham gia [[article-collaboration-guide|cộng tác bài viết]] 🤝
> 
> **Rất mong sự thông cảm của các bạn 🙏**

---

# Tổng kết 🎉

Qua bài viết này, chúng ta đã cùng nhau khám phá tầng giao vận của Internet với hai giao thức chính: **UDP** và **TCP**. Mỗi giao thức có những đặc điểm riêng phù hợp với từng loại ứng dụng:
- **UDP** 🚀 – Giao thức **không kết nối** và **không đảm bảo tin cậy**, thích hợp cho các ứng dụng yêu cầu tốc độ cao như **truyền phát video, trò chơi trực tuyến** hoặc **giao tiếp thời gian thực**.
- **TCP** 🔒 – Giao thức **có kết nối** và **đảm bảo độ tin cậy**, sử dụng các cơ chế như kiểm soát lỗi, xác nhận, và kiểm soát tắc nghẽn, thích hợp cho các ứng dụng quan trọng như **truyền tệp, gửi email, duyệt web**.

Ngoài ra, chúng ta cũng tìm hiểu về vai trò của tầng mạng **IP**, nơi chịu trách nhiệm chuyển dữ liệu giữa các thiết bị nhưng **không đảm bảo độ tin cậy**. Để dữ liệu có thể được gửi đến đúng tiến trình ứng dụng, tầng vận chuyển sử dụng các cơ chế **multiplexing** và **demultiplexing** để phân phối dữ liệu một cách chính xác.

Hy vọng qua bài viết này, bạn đã có cái nhìn rõ ràng hơn về tầng vận chuyển của Internet. Hãy tiếp tục khám phá các chủ đề về **giao thức mạng** để hiểu sâu hơn về cách Internet vận hành! 🌍🔥
