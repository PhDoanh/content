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

Bài viết này sẽ chỉ bạn cách tùy chỉnh thêm các tính năng mà trang web mặc định do Quartz tạo ra không có, để có thể giúp tối ưu những yếu tố mà một trang blog thực thụ phải có (SEO, CTA, UX, ...). Đừng lo lắng nếu bạn không chuyên về công nghệ, vì hướng dẫn này được viết cho cả bạn, còn nếu vướng mắc thì có thể liên hệ với mình để giải quyết!

# Bước đi đầu tiên
Nếu bạn chưa có bài viết nào của riêng mình, hãy đọc "[[my-own-cms|Cách mình quản lý lượng bài viết khổng lồ bằng Obsidian]]" để biết cách xây dựng hệ thống quản lý nội dung blog CMS. Việc chuẩn bị CMS là một tùy chọn, bạn có thể bắt đầu luôn với việc xây dựng website trước rồi sản xuất nội dung sau cũng được! ^2423b0

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

> [!info] Lưu ý
> Bạn sẽ được nhắc cấu hình trang web khi chạy lệnh `npx quartz create`, nhấn **Enter** để áp dụng cấu hình **mặc định** hoặc chọn cấu hình mong muốn nếu bạn hiểu mình đang làm gì!

## Xây dựng website trên máy cục bộ 
Đã đến lúc bạn vận hành nhà máy Quartz để sản xuất ra trang web của mình! Tiếp tục ở terminal của bạn, gõ lệnh `npx quartz build --serve` để kích hoạt quá trình xây dựng.

Sẽ mất một lúc để bạn nhìn thấy dòng `http://localhost:8080/`. Đó chính là địa chỉ trang web của bạn nhưng đang hoạt động trên **mạng cục bộ chứ không phải mạng Internet**. Dán nó vào trình duyệt yêu thích của bạn và xem kết quả

## Lưu trữ website lên Internet
Nếu bây giờ bạn mở máy khác ra, truy cập vào địa chỉ `http://localhost:8080/` thì sẽ không thấy trang web của bạn đâu. Đó là lúc bạn cần công khai website lên Internet để ai ai cũng có thể truy cập! Hãy làm theo các bước sau:

1. Trên Github, nhấn nút **"New"** để tạo một kho chứa mới (kho lưu trữ trang web của bạn trên Internet). 
2. Điền tên (Repository name) rồi nhấn vào nút **"Create repository"** ở cuối trang để hoàn tất quá trình tạo. Bạn sẽ được chuyển hướng vào bên trong kho chứa, hãy sao chép địa chỉ của kho chứa này 

![[Pasted image 20250712213827.png|center]]

3. Quay trở lại terminal trước đó, gõ lệnh `git remote set-url origin REMOTE-URL` với **REMOTE-URL** là địa chỉ của kho chứa vừa tạo (có thể cần **Ctrl+C** trước để trở về dấu nhắc lệnh bình thường) 
4. Đẩy trang web của bạn lên kho chứa Github bằng lệnh `npx quartz sync --no-pull` (Bạn có thể cần tải lại trình duyệt để thấy dữ liệu trang web xuất hiện trong kho chứa Github của mình)
5. Chuyển sang tab **"Settings"** và nhấp vào **"Pages"** trong mục **Code and automation** của thanh menu bên
6. Ngay dưới mục **Source**, chọn **"Github Actions"**
7. Chuyển về tab "Code" và nhấn vào **"Add file > Create new file"** để tạo file mới tên `.github/workflows/deploy.yml` với nội dung sau: 

```yml
name: Deploy Quartz site to GitHub Pages
 
on:
  push:
    branches:
      - v4
 
permissions:
  contents: read
  pages: write
  id-token: write
 
concurrency:
  group: "pages"
  cancel-in-progress: false
 
jobs:
  build:
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0 # Fetch all history for git info
      - uses: actions/setup-node@v4
        with:
          node-version: 22
      - name: Install Dependencies
        run: npm ci
      - name: Build Quartz
        run: npx quartz build
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: public
 
  deploy:
    needs: build
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

8. Nhấn nút **"Commit changes"** để lưu các thay đổi
9. Thực hiện lại **bước 5** để lấy địa chỉ trang web (Có thể cần chờ một lúc để nhìn thấy địa chỉ)

Lúc này trang web của bạn đã trực tuyến trên Internet tại địa chỉ dạng `https://<user-name>.github.io/<repo-name>/`, bạn có thể truy cập nó bằng trình duyệt trên bất kỳ thiết bị nào!

> [!info] Lưu ý
> Xem tài liệu [Quartz](https://quartz.jzhao.xyz/) để biết cách tùy chỉnh đầy đủ trang web của bạn (bố cục, hành vi, tính năng, ...)

# Mở rộng tính năng
Mặc định, trang web do Quartz tạo ra thường được dùng với mục đích **"sổ tay cá nhân kỹ thuật số"**. Nó cũng có những tính năng SEO cơ bản, nhưng chưa đủ mạnh nếu bạn hướng tới một thương hiệu cá nhân. Bạn có thể tham khảo và tùy biến các tính năng dưới đây, đã và đang được áp dụng cho trang blog của mình!

## Chia sẻ bài viết

## Chỉnh sửa bài viết

## Nhận xét bài viết

## Lưu bài viết ngoại tuyến

## Các bài viết gần đây

## Danh sách các cộng tác viên


# Kết nối tới hệ thống CMS
Trước đó mình có nói CMS là một tùy chọn, nhưng khi đã có website rồi thì CMS là một lựa chọn bắt buộc, vì website mà không chứa nội dung gì thì cũng như cái *"nhà hoang không người ở"*, kể cả việc chỉ viết các file Markdown rồi ném chúng vào thư mục [`content`](https://quartz.jzhao.xyz/authoring-content) (thư mục Quartz dùng để nhúng các bài viết vào trang blog) thì cũng rất khó để quản lý khi lượng bài viết tăng lên ngày một nhiều!

Phần này là hướng dẫn kết nối, nên bạn phải có [[#^2423b0|CMS]] của riêng mình trước!



# Lời kết

> [!caution]- Nội dung đang hoàn thiện
> Quá trình xây dựng nội dung này có thể mất nhiều thời gian, nhưng bạn có thể thúc đẩy nó bằng cách tham gia [[cộng tác bài viết]]
> 
> **Rất mong sự thông cảm của các bạn!**
