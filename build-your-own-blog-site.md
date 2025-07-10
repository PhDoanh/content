---
stage: Draft
title: "Behind this Site: Cách tôi tạo ra nó"
description: Hướng dẫn cách xây dựng trang blog cá nhân cho mọi đối tượng
permalink: ""
lang: vi
draft: true
tags:
  - explorable
aliases: 
cssclasses:
  - img
  - btn
socialDescription: ""
socialImage: ""
---

Trang blog này là một sản phẩm được tạo ra với sự hỗ trợ của trình tạo trang web tĩnh tên là [Quartz](https://quartz.jzhao.xyz/), nó giúp chuyển đổi nội dung các file Markdown thành các tệp mã nguồn mà trình duyệt hiểu (HTML, CSS, JS, ...). Để từ đó có thể hiển thị trên Internet! 

Bài viết này sẽ chỉ bạn cách tùy chỉnh thêm các tính năng mà trang web mặc định do Quartz tạo ra không có, để có thể giúp tối ưu những yếu tố mà một trang blog thực thụ phải có (SEO, CTA, UX, ...). Đừng lo lắng nếu bạn không chuyên về công nghệ, vì hướng dẫn này được viết cho cả bạn mà, còn nếu vướng mắc thì có thể liên hệ với mình để giải quyết!

# Bước đi đầu tiên
Nếu bạn chưa có bài viết nào của riêng mình, hãy đọc "[[my-own-cms|Cách mình quản lý lượng bài viết khổng lồ bằng Obsidian]]" để biết cách xây dựng hệ thống quản lý nội dung blog CMS. Việc chuẩn bị CMS là một tùy chọn, bạn có thể bắt đầu luôn với việc xây dựng website trước rồi sản xuất nội dung sau cũng được!

Tài liệu Quartz đã nói rất kỹ các bước tạo rồi, nên mình chỉ nhắc lại và rút gọn một số bước chưa cần thiết đi thôi

## Cài đặt các phụ thuộc
Quartz yêu cầu một số tài nguyên mà nó phụ thuộc vào để hoạt động, bạn cần cài:
- [Node.js](https://nodejs.org/en/download) phiên bản 22+ (tải xuống trình cài đặt là cách thân thiện nhất) 
- **npm** phiên bản 10.9.2 (sẽ được đi kèm khi cài Node.js)
- [Git](https://git-scm.com/downloads) và [Github](https://github.com/) (chỉ cần tạo tài khoản là đủ)

Mở terminal của bạn ra và nhập từng dòng lệnh sau để hoàn tất quá trình cài đặt:
```bash
git clone https://github.com/jackyzha0/quartz.git
cd quartz
npm i
npx quartz create
```

## Xây dựng website trên máy cục bộ 
Đã đến lúc bạn vận hành nhà máy Quartz để sản xuất ra trang web của mình! Tiếp tục ở terminal của bạn, gõ lệnh `npx quartz build --serve` để kích hoạt quá trình xây dựng.

Sẽ mất một lúc để bạn nhìn thấy dòng `http://localhost:8080/`. Đó chính là địa chỉ trang web của bạn nhưng đang hoạt động trên **mạng cục bộ chứ không phải mạng Internet**. Nhấp vào đó để xem kết quả

Kết quả có dạng giống trang tài liệu Quartz đúng không? 

## Lưu trữ website lên Internet
Nếu bây giờ bạn mở máy khác ra, truy cập vào địa chỉ `http://localhost:8080/` thì sẽ không thấy trang web của bạn đâu. Đó là lúc bạn cần công khai website lên Internet để ai ai cũng có thể truy cập!

Bây giờ mở Github ra, nhấn nút "New" để tạo một kho chứa mới (kho lưu trữ trang web của bạn trên Internet). Điền tên (Repository name) rồi nhấn vào nút "Create repository" ở cuối trang để hoàn tất quá trình tạo. Bạn sẽ được chuyển hướng vào bên trong kho chứa, sao chép địa chỉ của kho chứa này 

Quay trở lại terminal trước đó, gõ lệnh `git remote set-url origin REMOTE-URL` với REMOTE-URL là địa chỉ của kho chứa vừa tạo. Tiếp đó, kết nối thư mục hiện tại tới kho chứa trên Internet bằng lệnh `npx quartz sync --no-pull`

Lúc này toàn bộ dữ liệu trang web đã được đồng bộ lên Internet. Nhưng vẫn chưa xong, bạn cần đăng ký nhà mạng để họ quảng bá nó tới tay người dùng

Một trong số những nhà mạng phổ biến và thân thiện là Github Pages 

> [!caution]- Nội dung đang hoàn thiện
> Quá trình xây dựng nội dung này có thể mất nhiều thời gian, nhưng bạn có thể thúc đẩy nó bằng cách tham gia [[cộng tác bài viết]]
> 
> **Rất mong sự thông cảm của các bạn!**

# Mở rộng tính năng

> [!caution]- Nội dung đang hoàn thiện
> Quá trình xây dựng nội dung này có thể mất nhiều thời gian, nhưng bạn có thể thúc đẩy nó bằng cách tham gia [[cộng tác bài viết]]
> 
> **Rất mong sự thông cảm của các bạn!**


## Chia sẻ bài viết

## Chỉnh sửa bài viết

## Nhận xét bài viết

## Lưu bài viết ngoại tuyến

## Các bài viết gần đây

## Danh sách các cộng tác viên


# Kết nối tới hệ thống CMS
Trước đó mình có nói CMS là một tùy chọn, nhưng khi đã có website rồi thì CMS là một lựa chọn bắt buộc, vì website mà không chứa nội dung gì thì cũng như cái "nhà hoang không người ở", kể cả nếu bạn chỉ viết các file Markdown rồi ném chúng vào thư mục mà Quartz nhìn vào đó để tạo thì hãy thử nghĩ xem sẽ thế nào nếu nội dung của bạn ngày một lớn (thậm chí là khổng lồ)?

Phần này là hướng dẫn kết nối, nên bạn phải có CMS của riêng mình trước!

> [!caution]- Nội dung đang hoàn thiện
> Quá trình xây dựng nội dung này có thể mất nhiều thời gian, nhưng bạn có thể thúc đẩy nó bằng cách tham gia [[cộng tác bài viết]]
> 
> **Rất mong sự thông cảm của các bạn!**

# Lời kết

> [!caution]- Nội dung đang hoàn thiện
> Quá trình xây dựng nội dung này có thể mất nhiều thời gian, nhưng bạn có thể thúc đẩy nó bằng cách tham gia [[cộng tác bài viết]]
> 
> **Rất mong sự thông cảm của các bạn!**
