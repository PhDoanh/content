---
stage: Publish
title: "Behind this Site: Cách tôi tạo ra nó"
description: Hướng dẫn cách xây dựng trang blog cá nhân cho mọi đối tượng
permalink: ""
lang: vi
draft: false
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
Nếu bạn chưa có bài viết nào của riêng mình, hãy đọc "[[blogger-from-zero|Hành trình ghi lại dấu ấn cá nhân bằng Blog]]" để biết cách đặt bút cho những bài viết đầu tiên của bản thân. Việc chuẩn bị các bài viết là một tùy chọn, bạn có thể bắt đầu luôn với việc xây dựng website trước rồi sản xuất nội dung sau cũng được!

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
Mặc định, trang web do Quartz tạo ra thường được dùng với mục đích **"sổ tay cá nhân kỹ thuật số"**. Nó cũng có những tính năng SEO cơ bản, nhưng chưa đủ mạnh nếu bạn hướng tới một thương hiệu **cá nhân**. Để đạt được điều đó thì cần rất nhiều yếu tố, phần này sẽ hỗ trợ tối ưu trang blog qua yếu tố trải nghiệm người dùng (UX).

Bạn có thể tham khảo và tùy biến các tính năng dưới đây, đã và đang được áp dụng cho trang blog của mình!

> [!info]- Tính năng ẩn của Quartz
> Quartz hỗ trợ một số tính năng sau nhưng không được áp dụng mặc định để hiện thị nên trang web, nên bạn phải tự bật nó theo hướng dẫn của họ:
> - [Nhận xét bài viết](https://quartz.jzhao.xyz/features/comments)
> - [Các bài viết gần đây](https://quartz.jzhao.xyz/features/recent-notes)

## Chia sẻ bài viết - MediaShare
Sẽ rất bất tiện khi người dùng phải copy link bài viết từ thanh tìm kiếm của trình duyệt. Nên tính năng này cho phép chia sẻ bài viết tới **các nền tảng cụ thể** (Facebook, Reddit, ...) hoặc hỗ trợ nút **Copy thân thiện hơn**. Đặc biệt hiệu quả với những người không chuyên về công nghệ!

Để **cài đặt** tính năng này, chỉ cần **thêm** các file sau ở đúng vị trí trong kho chứa Github của bạn:

1. Định nghĩa cấu trúc tính năng: [`quartz/components/MediaShare.tsx`](https://github.com/PhDoanh/blog/blob/dev/quartz/components/MediaShare.tsx)

2. Trang trí giao diện tính năng: [`quartz/components/styles/mediaShare.scss`](https://github.com/PhDoanh/blog/blob/dev/quartz/components/styles/mediaShare.scss)

3. Xây dựng hành vi tính năng: [`quartz/components/scripts/mediaShare.inline.ts`](https://github.com/PhDoanh/blog/blob/dev/quartz/components/scripts/mediaShare.inline.ts)

Để **sử dụng**, làm theo hướng dẫn của Quartz tại [đây](https://quartz.jzhao.xyz/advanced/creating-components#using-a-component) với các cấu hình sau của tính năng:

```ts
interface MediaShareOptions {
	platforms: {
		facebook?: boolean // mặc định là true 
		linkedin?: boolean // mặc định là true
		reddit?: boolean // mặc định là true
		twitter?: boolean // mặc định là false
		instagram?: boolean // mặc định là false
	}
}
```

## Chỉnh sửa bài viết - EditThisPage
Về lý thuyết thì bạn đang tạo ra trang blog cá nhân, tức chỉ mình bạn là người có quyền thao tác với mọi bài viết trong blog. Nhưng nếu muốn **blog mở có kiểm soát**, tức là chỉ cho phép cộng tác trên các bài viết của bạn, hoặc ít nhất là được sự đồng ý từ bạn để tạo bài viết mới theo đúng giá trị blog bạn truyền tải. Thì tính năng này là dành cho bạn!

> [!warning] Blog dành cho cộng đồng
> Mình không khuyến khích mở hoàn toàn trang blog của bạn cho mọi người mà không có kiểm soát, tức là bất cứ ai có thể sử dụng trang blog như một nơi chứa các bài viết mà **chính họ là tác giả**. Vì nó sẽ làm mất đi **bản chất của blog cá nhân** và hạ tầng chứa **trang web tĩnh** trên Internet sẽ không đủ sức chịu đựng do blog cộng đồng phù hợp hơn với trang [web động](https://gleads.vn/vi/blog/web-tinh-va-web-dong)!   

Để cài đặt tính năng, bạn chỉ cần đặt các file sau vào đúng vị trí của kho chứa Github:

- [`quartz/components/Link.tsx`](https://github.com/PhDoanh/blog/blob/dev/quartz/components/Link.tsx)
- [`quartz/components/EditThisPage.tsx`](https://github.com/PhDoanh/blog/blob/dev/quartz/components/EditThisPage.tsx)

Để sử dụng, làm theo hướng dẫn của Quartz tại [đây](https://quartz.jzhao.xyz/advanced/creating-components#using-a-component)

## Danh sách các cộng tác viên - Contributors

> [!caution]- Nội dung đang hoàn thiện
> Quá trình xây dựng nội dung này có thể mất nhiều thời gian, nhưng bạn có thể thúc đẩy nó bằng cách tham gia [[article-contribution-guide|Hướng dẫn cộng tác bài viết]]
> 
> **Rất mong sự thông cảm của các bạn!**

## Cuộn lên đầu trang - BackToTop
Đối với hầu hết thiết bị di động, bạn buộc phải cuộn trang bằng cách vuốt lên/xuống màn hình. Điều này đôi khi khiến người dùng khó chịu khi họ muốn cuộn lên đầu trang mà bài viết thì lại dài quá. Giải pháp là sử dụng một nút điều hướng sẵn sàng ngay khi họ có ý định cuộn lên đầu trang.

Để cài đặt tính năng, bạn chỉ cần đặt các file sau vào đúng vị trí của kho chứa Github:
- [`quartz/components/BackToTop.tsx`](https://github.com/PhDoanh/blog/blob/dev/quartz/components/BackToTop.tsx)

Để sử dụng, làm theo hướng dẫn của Quartz tại [đây](https://quartz.jzhao.xyz/advanced/creating-components#using-a-component)

# Kết nối tới Headless CMS
**CMS** là phần mềm giúp bạn dễ dàng **tạo, quản lý và chỉnh sửa nội dung số** như văn bản, hình ảnh, video thông qua giao diện web mà không cần code nhiều. Nó tích hợp cả backend (nơi lưu trữ nội dung) và frontend (phần hiển thị nội dung) trong cùng một hệ thống. 

Trong khi **Headless CMS** chỉ chứa **phần quản lý nội dung (backend)**, **không có phần hiển thị (frontend)**. Nó lưu nội dung rồi cung cấp qua một phương tiện nào đó (thường là API) để frontend khác (web, app, …) tự lấy về mà hiển thị. Đây chính xác là hệ thống chúng ta sẽ làm việc cùng!

> [!question]- Tại sao cần hệ thống quản lý nội dung?
> Vì rất khó để quản lý lượng bài viết khổng lồ nếu bạn chỉ viết và ném các file Markdown vào thư mục [`content`](https://quartz.jzhao.xyz/authoring-content) (thư mục Quartz dùng để nhúng các bài viết vào trang blog) 

Có nhiều lựa chọn Headless CMS, hướng dẫn này sẽ dựa trên giải pháp mình đã chọn là [Obsidian](https://obsidian.md/). Nó đúng ra là một ứng dụng ghi chú kỹ thuật số như Notion, Apple Note, Evernote, ... Nhưng khả năng tùy biến (mã nguồn mở) cho phép nó vượt xa sự mong đợi của người dùng. Đó là lý do **Obsidian có thể trở thành một Headless CMS**!

Tham khảo "[[my-own-headless-cms|Cách mình quản lý lượng bài viết khổng lồ bằng Obsidian]]" để biết cách xây dựng hệ thống quản lý nội dung blog. Các bước sau đây sẽ chỉ hướng dẫn kết nối Headless CMS tới trang blog của bạn:

1. Tải xuống và cài đặt ứng dụng [Obsidian](https://obsidian.md/download)
2. Mở ứng dụng lên, chọn **"Open"** để mở một thư mục dưới dạng hầm chứa 
3. Trong File Explorer, tìm đến thư mục `quartz\content` (thư mục chứa dữ liệu bài viết) và chọn **"Select folder"**
4. Trong Obsidian, bấm vào biểu tượng <svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-settings-icon lucide-settings"><path d="M12.22 2h-.44a2 2 0 0 0-2 2v.18a2 2 0 0 1-1 1.73l-.43.25a2 2 0 0 1-2 0l-.15-.08a2 2 0 0 0-2.73.73l-.22.38a2 2 0 0 0 .73 2.73l.15.1a2 2 0 0 1 1 1.72v.51a2 2 0 0 1-1 1.74l-.15.09a2 2 0 0 0-.73 2.73l.22.38a2 2 0 0 0 2.73.73l.15-.08a2 2 0 0 1 2 0l.43.25a2 2 0 0 1 1 1.73V20a2 2 0 0 0 2 2h.44a2 2 0 0 0 2-2v-.18a2 2 0 0 1 1-1.73l.43-.25a2 2 0 0 1 2 0l.15.08a2 2 0 0 0 2.73-.73l.22-.39a2 2 0 0 0-.73-2.73l-.15-.08a2 2 0 0 1-1-1.74v-.5a2 2 0 0 1 1-1.74l.15-.09a2 2 0 0 0 .73-2.73l-.22-.38a2 2 0 0 0-2.73-.73l-.15.08a2 2 0 0 1-2 0l-.43-.25a2 2 0 0 1-1-1.73V4a2 2 0 0 0-2-2z"/><circle cx="12" cy="12" r="3"/></svg> (Cài đặt) ở bên dưới 
5. Chuyển sang tab **"Community plugins"** và bấm vào nút **"Turn on community plugins"** để sử dụng các tiện ích từ cộng đồng
6. Bấm vào **"Browse"** để tìm và cài đặt tiện ích **Git** 
7. Cuối cùng, kích hoạt tiện ích bằng nút **"Enable"** là xong!

> [!info] Tiện ích Obsidian Git
> Đây là tiện ích giúp bạn dễ dàng hơn trong việc **đồng bộ dữ liệu bài viết từ máy tính cục bộ lên kho chứa Github trên Internet** mà không phải thao tác bằng dòng lệnh! Tìm hiểu thêm tại [đây](https://github.com/Vinzent03/obsidian-git/blob/master/README.md)

# Lời kết
Toàn bộ bài viết đã gói gọn quá trình mình hiện thực hóa ý tưởng xây dựng trang blog chỉ từ **0 đồng!** Trên thực tế, website cần rất nhiều yếu tố để vận hành. Do đó cũng phát sinh rất nhiều chi phí đi kèm. Mà cái gì miễn phí thì cũng có nhược điểm của riêng nó, nhưng ít nhất nó đủ để đáp ứng yêu cầu của một trang blog cá nhân dùng đến suốt đời! 

Nếu bạn hứng thú với các nội dung như này, đừng quên để lại tín hiệu **like, share, comment** cho mình và người khác cùng biết nhé!
