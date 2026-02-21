---
title: Xây dựng trang blog mà bạn có toàn quyền kiểm soát
description: Khám phá cách bạn có thể tự build một web blog 0 đồng dựa trên cách trang web này ra đời
permalink: ""
lang: vi
publish: true
tags:
  - explorable
  - Intermediate
aliases:
cssclasses:
  - img
socialDescription: ""
socialImage: ""
updated: 2026-02-21
---

Trang blog này là một sản phẩm được tạo ra với sự hỗ trợ của trình tạo web tĩnh tên là [Quartz](https://quartz.jzhao.xyz/), nó giúp chuyển đổi nội dung các file [Markdown](https://www.markdownguide.org/getting-started/) thành các tệp mã nguồn mà trình duyệt hiểu để hiển thị trên Internet! 

Bài viết này sẽ chỉ bạn cách tùy chỉnh thêm các tính năng mà trang web mặc định do Quartz tạo ra không có, để có thể giúp tối ưu những yếu tố mà một trang blog thực thụ phải có (SEO, CTA, UX, ...)

## Bước đầu tiên 👣
Nếu bạn chưa có bài viết nào của riêng mình, hãy đọc "[[blogger-from-zero|Hành trình ghi lại dấu ấn cá nhân bằng Blog]]" để biết cách đặt bút cho những bài viết đầu tiên của bản thân. Việc chuẩn bị các bài viết là một tùy chọn, bạn có thể bắt đầu luôn với việc xây dựng website trước rồi sản xuất nội dung sau cũng được!

Tài liệu Quartz đã nói rất kỹ các bước tạo rồi, nên mình chỉ nhắc lại và rút gọn một số bước chưa cần thiết đi thôi

### Cài đặt các phụ thuộc 
Quartz yêu cầu một số tài nguyên mà nó phụ thuộc vào để hoạt động, bạn cần cài:
- [Node.js](https://nodejs.org/en/download) phiên bản 22+ (tải xuống trình cài đặt là cách thân thiện nhất) 
- **npm** phiên bản 10.9.2 (sẽ được đi kèm khi cài Node.js)
- [Git](https://git-scm.com/downloads) và [Github](https://github.com/) (Github chỉ cần tạo tài khoản là đủ)

Mở terminal của bạn ra và **nhập từng dòng lệnh** sau để hoàn tất quá trình cài đặt:
```sh
git clone https://github.com/jackyzha0/quartz.git
cd quartz
npm i
npx quartz create
```

> [!info] Lưu ý
> Bạn sẽ được nhắc cấu hình trang web khi chạy lệnh `npx quartz create`, nhấn **Enter** để áp dụng cấu hình **mặc định** hoặc chọn cấu hình mong muốn nếu bạn hiểu mình đang làm gì!

### Xây dựng website trên máy cục bộ 
Đã đến lúc bạn vận hành nhà máy Quartz để sản xuất ra trang web của mình! Tiếp tục ở terminal của bạn, gõ lệnh `npx quartz build --serve` để kích hoạt quá trình xây dựng.

Sẽ mất một lúc để bạn nhìn thấy dòng `http://localhost:8080/`. Đó chính là địa chỉ trang web của bạn nhưng đang hoạt động trên **mạng cục bộ chứ không phải mạng Internet**. Dán nó vào trình duyệt yêu thích của bạn và xem kết quả.

### Lưu trữ website lên Internet
Nếu bây giờ bạn mở máy khác ra, truy cập vào địa chỉ `http://localhost:8080/` thì sẽ không thấy trang web của bạn đâu. Đó là lúc bạn cần công khai website lên Internet để ai cũng có thể truy cập! Hãy làm theo các bước sau:

1. Trên Github, nhấn nút *"New"* để tạo một kho chứa mới (kho lưu trữ trang web của bạn trên Internet). 
2. Điền tên (Repository name) rồi nhấn nút *"Create repository"* ở cuối trang để hoàn tất quá trình tạo. Bạn sẽ được chuyển hướng vào bên trong kho chứa, hãy sao chép địa chỉ của kho chứa này 

![[build-your-own-blog-site-0.png|center]]

3. Quay trở lại terminal trước đó, gõ lệnh `git remote set-url origin REMOTE-URL` với `REMOTE-URL` là địa chỉ của kho chứa vừa tạo (có thể cần Cmd/Ctrl+C trước để trở về dấu nhắc lệnh bình thường) 
4. Đẩy trang web của bạn lên kho chứa Github bằng lệnh `npx quartz sync --no-pull` (Bạn có thể cần tải lại trình duyệt để thấy dữ liệu trang web xuất hiện trong kho chứa Github của mình)
5. Chuyển sang tab *"Settings"* và nhấp vào *"Pages"* trong mục *"Code and automation"* của thanh menu bên
6. Ngay dưới mục *"Source"*, chọn *"Github Actions"*
7. Chuyển về tab *"Code"* và nhấn vào *"Add file > Create new file"* để tạo file mới tên `.github/workflows/deploy.yml` với nội dung sau: 

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

8. Nhấn nút *"Commit changes"* để lưu các thay đổi
9. Thực hiện lại **bước 5** để lấy địa chỉ trang web (Có thể cần chờ một lúc để nhìn thấy địa chỉ)

Lúc này trang web của bạn đã trực tuyến trên Internet tại địa chỉ dạng `https://<user-name>.github.io/<repo-name>/`, bạn có thể truy cập nó bằng trình duyệt trên bất kỳ thiết bị nào!

> [!info] Lưu ý
> Xem tài liệu [Quartz](https://quartz.jzhao.xyz/) để biết cách tùy chỉnh đầy đủ trang web của bạn (bố cục, hành vi, tính năng, ...)

## Mở rộng tính năng 🔓
Mặc định, trang web do Quartz tạo ra thường được dùng với mục đích *"sổ tay cá nhân kỹ thuật số"*. Nó cũng có những tính năng SEO cơ bản, nhưng chưa đủ mạnh nếu bạn hướng tới một thương hiệu cá nhân. Để đạt được điều đó thì cần rất nhiều yếu tố, phần này sẽ hỗ trợ tối ưu trang blog qua yếu tố trải nghiệm người dùng (UX).

Bạn có thể tham khảo và tùy biến các tính năng dưới đây, đã và đang được áp dụng cho trang blog hiện tại!

> [!info]- Tính năng ẩn của Quartz
> Quartz cũng hỗ trợ một số tính năng mở rộng nhưng không được áp dụng mặc định để hiện thị lên trang web, nên bạn phải tự bật nó theo hướng dẫn của họ:
> - [Nhận xét bài viết](https://quartz.jzhao.xyz/features/comments)
> - [Các bài viết gần đây](https://quartz.jzhao.xyz/features/recent-notes)

### Chia sẻ bài viết
Sẽ rất bất tiện khi người dùng phải copy link bài viết từ thanh tìm kiếm của trình duyệt. Nên tính năng này cho phép chia sẻ bài viết tới **các nền tảng cụ thể** (Facebook, Linkedin, Reddit, Twitter/X, Instagram) và hỗ trợ nút **Copy thân thiện hơn**.

#### Cài đặt tính năng
1. Tạo các file sau ở đúng vị trí trong kho chứa Github của bạn:
	- [`quartz/components/MediaShare.tsx`](https://github.com/PhDoanh/blog/blob/v4/quartz/components/MediaShare.tsx)
	- [`quartz/components/styles/mediaShare.scss`](https://github.com/PhDoanh/blog/blob/v4/quartz/components/styles/mediaShare.scss)
	- [`quartz/components/scripts/mediaShare.inline.ts`](https://github.com/PhDoanh/blog/blob/v4/quartz/components/scripts/mediaShare.inline.ts)

2. Thêm 2 dòng sau vào [`quartz/components/index.ts`](https://github.com/PhDoanh/blog/blob/v4/quartz/components/index.ts) 

```ts {2,6}
// other imports
import MediaShare from "./MediaShare"

export {
	// other exports
	MediaShare,
}
```

3. Bật tính năng này bằng cách thêm đoạn mã sau vào [`quartz.layout.ts`](https://github.com/PhDoanh/blog/blob/v4/quartz.layout.ts) với cấu hình tùy chọn mà bạn muốn. Ví dụ:

```ts
Component.MediaShare({
	// support "facebook", "linkedin", "reddit", "twitter", "ínstagram"
	platforms: ["facebook", "instagram", "twiter"],
	copyButton: true,
}),
```

#### Tùy biến tính năng
- Component: `quartz/components/MediaShare.tsx`
- Style: `quartz/components/styles/mediaShare.scss`
- Script: `quartz/components/scripts/mediaShare.inline.ts`
- Vô hiệu hóa: Xóa tất cả những nơi sử dụng `Component.MediaShare()` trong `quartz.layout.ts`
- Tùy chỉnh ngôn ngữ hiển thị: tham khảo [`quartz/i18n/locales/definition.ts`](https://github.com/PhDoanh/blog/blob/v4/quartz/i18n/locales/definition.ts) và [`quartz/i18n/locales/en-US.ts`](https://github.com/PhDoanh/blog/blob/v4/quartz/i18n/locales/en-US.ts)

### Chỉnh sửa bài viết
Về lý thuyết thì bạn đang tạo ra trang blog cá nhân, tức chỉ mình bạn là người có quyền thao tác với mọi bài viết trong blog. Nhưng nếu muốn **blog mở có kiểm soát**, tức là chỉ cho phép cộng tác trên các bài viết của bạn, hoặc ít nhất là được sự đồng ý từ bạn để tạo bài viết mới theo đúng giá trị blog bạn truyền tải. Thì tính năng này là dành cho bạn!

> [!warning] Blog dành cho cộng đồng
> Mình không khuyến khích mở hoàn toàn trang blog của bạn cho mọi người mà không có kiểm soát, vì nó sẽ làm mất đi **bản chất của blog cá nhân** và hạ tầng chứa **trang web tĩnh** trên Internet sẽ không đủ sức chịu đựng do blog cộng đồng phù hợp hơn với trang [web động](https://gleads.vn/vi/blog/web-tinh-va-web-dong)!   

#### Cài đặt tính năng
1. Tạo các file sau ở đúng vị trí trong kho chứa Github của bạn:
	- [`quartz/components/EditThisPage.tsx`](https://github.com/PhDoanh/blog/blob/dev/quartz/components/EditThisPage.tsx)
	- [`content/admin/index.htm`](https://github.com/PhDoanh/content/blob/main/admin/index.htm)
	- [`content/admin/config.yml`](https://github.com/PhDoanh/content/blob/main/admin/config.yml)

2. Dựa vào tài liệu [CDN Hosting - Static CMS](https://staticcms.org/docs/docs/overview/cdn-hosting/), sửa lại file `config.yml` theo nhu cầu thiết lập của bạn và cấu trúc nội dung mà blog tổ chức.

3. Thêm 2 dòng sau vào [`quartz/components/index.ts`](https://github.com/PhDoanh/blog/blob/v4/quartz/components/index.ts) 

```ts {2,6}
// other imports
import EditThisPage from "./EditThisPage"

export {
	// other exports
	EditThisPage,
}
```

3. Bật tính năng này bằng cách thêm `Component.EditThisPage()` vào [`quartz.layout.ts`](https://github.com/PhDoanh/blog/blob/v4/quartz.layout.ts).

> [!info] Lưu ý
> Đối với cấu hình (`config.yml`) lấy [Github làm backend](https://staticcms.org/docs/docs/backends/github/),  bạn cần một máy chủ xác thực trung gian để người khác có thể truy cập vào hệ thống quản lý bài viết (CMS) thông qua tài khoản Github của họ.

#### Tùy biến tính năng
- Component + Style (không có Script): `quartz/components/MediaShare.tsx`
- Vô hiệu hóa: Xóa tất cả những nơi sử dụng `Component.EditThisPage()` trong `quartz.layout.ts`
- Tùy chỉnh ngôn ngữ hiển thị: tham khảo [`quartz/i18n/locales/definition.ts`](https://github.com/PhDoanh/blog/blob/v4/quartz/i18n/locales/definition.ts) và [`quartz/i18n/locales/en-US.ts`](https://github.com/PhDoanh/blog/blob/v4/quartz/i18n/locales/en-US.ts)

### Danh sách cộng tác viên
Trong hệ thống blog có nhiều người tham gia cộng tác, việc ghi danh các cộng tác viên giúp bài viết tăng độ uy tín và tôn trọng quyền sáng tạo nội dung của các tác giả, người đọc có thể xem nhanh hồ sơ cá nhân và theo dõi các hoạt động của họ trên Github nếu muốn. Thậm chí là biết được lịch sử từng thay đổi của bài viết qua biểu tượng <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-file-clock-icon lucide-file-clock"><path d="M16 22h2a2 2 0 0 0 2-2V8a2.4 2.4 0 0 0-.706-1.706l-3.588-3.588A2.4 2.4 0 0 0 14 2H6a2 2 0 0 0-2 2v2.85"/><path d="M14 2v5a1 1 0 0 0 1 1h5"/><path d="M8 14v2.2l1.6 1"/><circle cx="8" cy="16" r="6"/></svg>

#### Cài đặt tính năng
1. Tạo các file sau ở đúng vị trí trong kho chứa Github của bạn:
	- [`quartz/components/GitHubContributors.tsx`](https://github.com/PhDoanh/blog/blob/v4/quartz/components/GitHubContributors.tsx)
	- [`quartz/components/styles/githubContributors.scss`](https://github.com/PhDoanh/blog/blob/v4/quartz/components/styles/githubContributors.scss)
	- [`quartz/components/scripts/githubContributors.inline.ts`](https://github.com/PhDoanh/blog/blob/v4/quartz/components/scripts/githubContributors.inline.ts)

2. Thêm 2 dòng sau vào [`quartz/components/index.ts`](https://github.com/PhDoanh/blog/blob/v4/quartz/components/index.ts) 

```ts {2,6}
// other imports
import GitHubContributors from "./GitHubContributors"

export {
	// other exports
	GitHubContributors,
}
```

3. Bật tính năng này bằng cách thêm đoạn mã sau vào [`quartz.layout.ts`](https://github.com/PhDoanh/blog/blob/v4/quartz.layout.ts) với cấu hình tùy chọn mà bạn muốn. Ví dụ:

```ts
Component.GitHubContributors({
      owner: "PhDoanh", // your username of Github Account
      repo: "demo", // your repository name of blog site
      title: "Co-Authors", // Title for the contributors section, default: "Contributors"
      limit: 20, // Maximum number of contributors to display, default: 10
})
```

#### Tùy biến tính năng
- Component: `quartz/components/GitHubContributors.tsx`
- Style: `quartz/components/styles/githubContributors.scss`
- Script: `quartz/components/scripts/githubContributors.inline.ts`
- Vô hiệu hóa: Xóa tất cả những nơi sử dụng `Component.GitHubContributors()` trong `quartz.layout.ts`
- Tùy chỉnh ngôn ngữ hiển thị: tham khảo [`quartz/i18n/locales/definition.ts`](https://github.com/PhDoanh/blog/blob/v4/quartz/i18n/locales/definition.ts) và [`quartz/i18n/locales/en-US.ts`](https://github.com/PhDoanh/blog/blob/v4/quartz/i18n/locales/en-US.ts)

### Cuộn lên đầu trang
Đối với hầu hết thiết bị di động, bạn buộc phải cuộn trang bằng cách vuốt lên/xuống màn hình. Điều này đôi khi khiến người dùng khó chịu khi họ muốn cuộn lên đầu trang mà bài viết thì lại quá dài. Giải pháp là sử dụng một nút điều hướng sẵn sàng ngay khi họ có ý định cuộn lên đầu trang.

#### Cài đặt tính năng
1. Tạo các file sau ở đúng vị trí trong kho chứa Github của bạn:
	- [`quartz/components/BackToTop.tsx`](https://github.com/PhDoanh/blog/blob/dev/quartz/components/BackToTop.tsx)

2. Thêm 2 dòng sau vào [`quartz/components/index.ts`](https://github.com/PhDoanh/blog/blob/v4/quartz/components/index.ts) 

```ts {2,6}
// các import khác
import BackToTop from "./BackToTop"

export {
	// các export khác
	BackToTop,
}
```

3. Bật tính năng này bằng cách thêm `Component.BackToTop()` vào `afterBody` của [`quartz.layout.ts`](https://github.com/PhDoanh/blog/blob/v4/quartz.layout.ts).

#### Tùy biến tính năng
- Component + Style + Script: `quartz/components/MediaShare.tsx`
- Vô hiệu hóa: Xóa tất cả những nơi sử dụng `Component.BackToTop()` trong `quartz.layout.ts`

## Lời kết 🎉
Toàn bộ bài viết đã gói gọn quá trình hiện thực hóa ý tưởng xây dựng trang blog chỉ từ **0 đồng!** Trên thực tế, website cần rất nhiều yếu tố để vận hành. Do đó cũng phát sinh rất nhiều chi phí đi kèm. Mà cái gì miễn phí thì cũng có nhược điểm của riêng nó, nhưng ít nhất nó đủ để đáp ứng yêu cầu của một trang blog cá nhân dùng đến suốt đời!
