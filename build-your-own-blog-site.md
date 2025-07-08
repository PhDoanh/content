---
stage: "Idea"
title: "Behind this Site: Cách tôi tạo ra nó"
description: "Hướng dẫn cách xây dựng trang blog cá nhân cho mọi đối tượng"
permalink: ""
lang: vi
draft: false
tags: 
  - explorable
aliases:
  - 
cssclasses:
  - img
  - btn
socialDescription: ""
socialImage: ""
---

Trang blog này là một sản phẩm được tạo ra với sự hỗ trợ của trình tạo trang web tĩnh tên là Quartz, nó giúp chuyển đổi nội dung các file Markdown thành các tệp mã nguồn mà trình duyệt hiểu (HTML, CSS, JS, ...). Để từ đó có thể hiển thị trên Internet! 

Bài viết này sẽ chỉ bạn cách tùy chỉnh thêm các tính năng mà trang web mặc định do Quartz tạo ra không có, để có thể giúp tối ưu những yếu tố mà một trang blog thực thụ phải có (SEO, CTA, UX, ...). Đừng lo lắng nếu bạn không chuyên về công nghệ, mọi thắc mắc đều có thể liên hệ với mình để giải quyết!

# Bước đi đầu tiên
Nếu bạn chưa có bài viết nào của riêng mình, hãy đọc "..." để biết cách xây dựng hệ thống quản lý nội dung blog CMS. Việc chuẩn bị CMS là một tùy chọn, bạn có thể bắt đầu luôn với việc xây dựng website trước rồi sản xuất nội dung sau cũng được!

Tài liệu Quartz đã nói rất kỹ các bước tạo rồi, nên mình chỉ nhắc lại và rút gọn một số bước chưa cần thiết đi thôi

## Cài đặt các phụ thuộc
Quartz yêu cầu một số tài nguyên mà nó phụ thuộc vào để hoạt động, bạn cần cài:
- Node.js phiên bản 22+
- npm phiên bản 10.9.2
- Git
- Github

Chạy thêm lệnh sau để hoàn tất quá trình cài đặt:
```bash
git clone https://github.com/jackyzha0/quartz.git
cd quartz
npm i
npx quartz create
```

## Xây dựng website trên máy cục bộ 


## Lưu trữ website lên Internet



# Mở rộng tính năng

## Chia sẻ bài viết

## Chỉnh sửa bài viết

## Nhận xét bài viết

## Lưu bài viết ngoại tuyến

## Các bài viết gần đây

## Danh sách các cộng tác viên


# Kết nối tới hệ thống CMS
Trước đó mình có nói CMS là một tùy chọn, nhưng khi đã có website rồi thì CMS là một lựa chọn bắt buộc, vì website mà không chứa nội dung gì thì cũng như cái "nhà hoang không người ở", kể cả nếu bạn chỉ viết các file Markdown rồi ném chúng vào thư mục mà Quartz nhìn vào đó để tạo thì hãy thử nghĩ xem sẽ thế nào nếu nội dung của bạn ngày một lớn (thậm chí là khổng lồ)?

Phần này là hướng dẫn kết nối, nên bạn phải có CMS của riêng mình trước!

# Lời kết

