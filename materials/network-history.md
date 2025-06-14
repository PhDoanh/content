---
date: 2025-02-13
draft: false
status: Doing
title: "Hành trình Mạng máy tính và Internet bước vào sử sách"
description: "Tìm hiểu về lịch sử phát triển của mạng máy tính và Internet, từ giai đoạn sơ khai với chuyển mạch gói cho đến sự bùng nổ trong kỷ nguyên số."
author: PhDoanh
authorlink: https://github.com/PhDoanh
tags: 
  - "computer-network"
  - internet
aliases:
  - "network history"
cssclasses:
  - img
  - btn
---
%% ĐỊNH DẠNG TÊN FILE: "tên-bài-viết" | VD: jp-typing-guide %%

%% <figure style="text-align: center; margin: 20px auto;">
  <img 
    src="images/network-history.png"
    alt="Hành trình Mạng máy tính và Internet bước vào sử sách" 
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
</figure> %%

# 🚼 Sự ra đời công nghệ chuyển mạch gói (1961 - 1972)

Vào đầu thập niên 1960, khi **mạng điện thoại** còn thống trị, các nhà khoa học đã nhận ra sự cần thiết phải liên kết các **máy tính** để phục vụ nhu cầu chia sẻ dữ liệu. Tuy nhiên, phương pháp **chuyển mạch kênh** trong mạng điện thoại không phù hợp với dữ liệu máy tính do tính chất "bùng nổ" (bursty) của lưu lượng truyền tải.

## Ý tưởng chuyển mạch gói 💡 

Ba nhóm nghiên cứu độc lập tại **MIT, Rand Institute và NPL (Anh Quốc)** đã phát triển ý tưởng **chuyển mạch gói**, một phương pháp truyền dữ liệu giúp tối ưu hóa băng thông bằng cách chia nhỏ thông tin thành từng gói nhỏ:

- **Leonard Kleinrock** (MIT) chứng minh sự hiệu quả của phương pháp này bằng lý thuyết hàng đợi.

- **Paul Baran** (Rand) nghiên cứu ứng dụng trong hệ thống quân sự.

- **Donald Davies và Roger Scantlebury** (NPL) phát triển ý tưởng tương tự.   

## Ngày ARPAnet chào đời 🚀

Dưới sự lãnh đạo của **J. C. R. Licklider** và **Lawrence Roberts**, **ARPAnet** ra đời năm 1969 với 4 nút mạng đầu tiên:

1. **UCLA (University of California, Los Angeles)**: nơi thực hiện kết nối ARPAnet đầu tiên vào năm 1969, đánh dấu sự khởi đầu của Internet.

2. **Stanford Research Institute (SRI)**: nơi phát triển giao thức liên mạng và thực hiện một trong những kết nối đầu tiên.
  
3. **UC Santa Barbara**: tham gia vào nghiên cứu về truyền dữ liệu và giao thức mạng.
   
4. **Đại học Utah**: đóng góp vào ARPAnet với nghiên cứu về đồ họa máy tính và truyền thông dữ liệu, giúp mở rộng ứng dụng của mạng máy tính.

> [!important] Sự kiện đánh dấu cột mốc
> Lần đăng nhập từ xa đầu tiên vào ARPAnet đã khiến hệ thống bị sập ngay sau khi nhập chữ "L" trong lệnh "LOGIN"!

---

# 🔏 Mạng riêng và sự xuất hiện của Internet (1972 - 1980)

Ban đầu, ARPAnet là một **mạng khép kín**, chỉ dành riêng cho những ai được kết nối trực tiếp. Tuy nhiên, nhiều mạng độc lập khác bắt đầu xuất hiện:

- **ALOHA** (Hawaii) sử dụng sóng vi ba

- **Packet Satellite** và **Packet Radio** của DARPA

- **Cyclades** (Pháp) với ý tưởng **định tuyến phi tập trung**

📢 **Khái niệm internetting** được đề xuất bởi **Vinton Cerf và Robert Kahn** (1974), mở đường cho sự liên kết giữa các mạng độc lập.

---

# 📈 Những ngày tháng phát triển Mạng máy tính (1980 - 1990)

Thập niên 1980 chứng kiến sự mở rộng mạnh mẽ của mạng máy tính với sự xuất hiện của nhiều mạng lớn:

- **BITNET** hỗ trợ email và chia sẻ tệp tin giữa các trường đại học.

- **CSNET** kết nối các nhà nghiên cứu không có quyền truy cập vào ARPAnet.

- **NSFNET** ra đời năm 1986, trở thành xương sống của Internet với tốc độ **1.5 Mbps** vào cuối thập kỷ.

> [!important] Ngày 1/1/1983
> - ARPAnet chính thức chuyển từ giao thức **NCP** sang **TCP/IP**, đánh dấu sự ra đời của Internet hiện đại!
> - **DNS (Domain Name System)** cũng được phát triển để đơn giản hóa việc định danh địa chỉ IP.

---

# 💥 Sự bùng nổ của Internet (1990s)

Những sự kiện quan trọng trong thập niên 1990 đã đưa Internet đến với công chúng:

- **1991:** NSFNET gỡ bỏ lệnh cấm sử dụng cho mục đích thương mại.

- **1993:** Trình duyệt **Mosaic** ra đời, mở đầu cho kỷ nguyên Web.
   
- **1995:** NSFNET bị ngừng hoạt động, các ISP tư nhân tiếp quản hạ tầng Internet.

💡 **Tim Berners-Lee** phát minh ra **World Wide Web** vào năm 1989, xây dựng trên nền tảng HTML, HTTP, trình duyệt và máy chủ Web. Đến cuối 1993, chỉ có khoảng 200 máy chủ Web, nhưng đến cuối thập niên, con số này đã vượt hàng triệu!

---

# 🚀 Kỷ nguyên mới: Internet trong thế kỷ 21

Internet không ngừng phát triển với các xu hướng mới:

- **Mạng xã hội**: Facebook, Twitter thay đổi cách con người tương tác.

- **Điện toán đám mây**: Amazon AWS, Google Cloud.

- **Kết nối không dây**: WiFi, 3G, 4G và IoT.

> [!caution] Vấn đề bảo mật
> Sự phát triển nhanh chóng cũng đi kèm với các mối đe dọa như **tấn công mạng, virus, lừa đảo trực tuyến**.

---

# 🎯 Tổng Kết

Internet đã trải qua một hành trình đầy biến động, từ những ngày đầu tiên với ARPAnet đến một hệ thống kết nối toàn cầu. Với sự phát triển không ngừng, **công nghệ mạng máy tính** tiếp tục thay đổi cuộc sống chúng ta từng ngày!
