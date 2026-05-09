---
title: Tôi chọn tool như thế nào để biến Obsidian Vault thành Web Blog
description: Đây là hành trình loại trừ lựa chọn, nhật ký thất bại khi phát triển tính năng, và bài học về việc chọn tool theo chiến lược dài hạn.
permalink: ""
lang: vi
publish: false
updated: 2026-05-09
tags:
  - explorable
  - Intermediate
  - web-development
  - obsidian
  - static-site-generator
aliases:
  - 
cssclasses:
socialDescription: Tôi đã chọn Quartz không phải vì nó mạnh nhất, mà vì tôi có thể grow cùng nó.
socialImage: ""
---
## Điểm xuất phát 🌱

Mọi thứ bắt đầu từ một vault Obsidian cá nhân, nơi tôi lưu trữ toàn bộ ghi chú học tập theo dạng file Markdown trên máy cục bộ. Theo thời gian, nhu cầu chia sẻ kiến thức ra ngoài ngày một tăng: tôi muốn những ghi chú đó có thể tiếp cận được với người khác, không chỉ nằm yên trên ổ cứng của mình.

Bài toán lúc đó rất rõ: **biến Obsidian vault thành web blog**. Nhưng ẩn sau đó là hai ràng buộc cứng mà tôi không thể thỏa hiệp: chi phí phải là 0 đồng, và tôi phải có toàn quyền kiểm soát cả code lẫn kiến trúc (vì lúc đó tôi đang học phát triển web, đây là cơ hội thực chiến không thể bỏ qua).

## Hành trình loại trừ 🔍

Cái đầu tiên xuất hiện trong đầu là [Obsidian Publish](https://obsidian.md/publish) - dịch vụ hosting chính thức của Obsidian, tích hợp liền mạch, setup trong vài phút. Nhưng nó bị loại ngay lập tức vì hai lý do: mất phí hàng tháng, và quan trọng hơn là khả năng tùy biến kiến trúc web bị giới hạn hoàn toàn trong hệ sinh thái của Obsidian. Với người đang muốn học và tự xây, đó là dead end.

Lựa chọn tiếp theo là [Obsidian Digital Garden](https://github.com/oleeskild/obsidian-digital-garden) - một community plugin tương thích tốt với Obsidian, open source, miễn phí. Nghe có vẻ phù hợp. Nhưng sau khi research kỹ (bao gồm quan sát dữ liệu trải nghiệm thực tế từ người dùng khác), tôi quyết định không đi theo hướng này với lý do: quy mô cộng đồng còn nhỏ và tính ổn định dài hạn của dự án chưa đủ để tôi tin tưởng đặt cược toàn bộ hạ tầng nội dung vào đó. Tôi cần một giải pháp bền vững, không phải một plugin mà việc bảo trì có thể bị bỏ quên bất cứ lúc nào.

Cuối cùng, tôi tìm thấy [Quartz 4](https://quartz.jzhao.xyz/) - Trình tạo web tĩnh được thiết kế đặc biệt để chuyển đổi Obsidian vault thành web. Khác với tiện ích digital garden ở trên, Quartz hoạt động theo mô hình "content folder": bạn trỏ nó vào một thư mục chứa file Markdown, và nó build ra website. Vault Obsidian của tôi chính là content folder đó.

Điều tôi không ngờ là Quartz còn linh hoạt hơn thế, kiến trúc của nó được viết để có thể scale lên: hỗ trợ Notion, Evernote, hoặc bất kỳ hệ thống note-taking nào sau này nếu cần. Đây là tín hiệu của một dự án được thiết kế có tầm nhìn, không phải giải quyết bài toán nhỏ trước mắt. Và dự đoán đó của tôi đã được xác nhận sau một thời gian thực sự dùng nó.

## Bắt đầu với Quartz ⚙️

Nếu bạn đã có vault Obsidian và muốn biến nó thành web blog, đây là quy trình cơ bản. Tài liệu chính thức của Quartz đã rất đầy đủ, phần này chỉ rút gọn các bước thiết yếu.

### Cài đặt các phụ thuộc

Quartz yêu cầu:
- [Node.js](https://nodejs.org/en/download) phiên bản 22+
- **npm** phiên bản 10.9.2 (đi kèm khi cài Node.js)
- [Git](https://git-scm.com/downloads) và tài khoản [Github](https://github.com/)

Mở terminal và chạy từng lệnh sau:

```sh
git clone https://github.com/jackyzha0/quartz.git
cd quartz
npm i
npx quartz create
```

> [!info] Lưu ý
> Khi chạy `npx quartz create`, bạn sẽ được nhắc cấu hình. Nhấn **Enter** để áp dụng mặc định, hoặc chọn theo nhu cầu nếu bạn biết mình đang làm gì.

### Build và xem kết quả cục bộ

Chạy lệnh sau để build và xem thử trên máy:

```sh
npx quartz build --serve
```

Truy cập `http://localhost:8080/` trên trình duyệt - đó là trang web của bạn đang chạy trên mạng cục bộ.

### Deploy lên Internet

1. Tạo repository mới trên Github
2. Sao chép địa chỉ repository vừa tạo
3. Trong terminal, chạy: `git remote set-url origin REMOTE-URL` (thay `REMOTE-URL` bằng địa chỉ vừa sao chép)
4. Push lên Github: `npx quartz sync --no-pull`
5. Vào **Settings → Pages → Source**, chọn **GitHub Actions**
6. Tạo file `.github/workflows/deploy.yml` với nội dung sau:

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

7. Commit và chờ một lúc - trang web sẽ trực tuyến tại `https://<username>.github.io/<repo-name>/`

> [!info] Lưu ý
> Xem [tài liệu Quartz](https://quartz.jzhao.xyz/) để tùy chỉnh đầy đủ bố cục, hành vi, và tính năng.

## Nhật ký thất bại về tính năng "Edit This Page" 🤦‍♂️

Đây là phần tôi muốn kể kỹ nhất, vì nó dạy tôi nhiều hơn bất kỳ bước setup nào.

**Version 1 - Github Editor link:** Ban đầu, tính năng "Edit This Page" chỉ là một hyperlink điều hướng thẳng đến Github Editor của repo lưu bài viết. Mục đích hoàn toàn cá nhân: phát hiện và sửa nhanh lỗi vặt (chính tả, thông tin lỗi thời, markdown syntax bị break) khi đang đọc bài trên web.

**Điểm gãy đầu tiên:** Sau một thời gian, tôi quan sát thấy độc giả đề xuất sửa đổi qua phần comment bài viết. Nhu cầu đóng góp từ bên ngoài là có thật. Và tôi nhận ra tiềm năng: nếu mở quyền chỉnh sửa trực tiếp, tính tương tác hai chiều sẽ tăng, hệ sinh thái bài viết sẽ phong phú hơn, kéo theo nhiều lợi ích khác (SEO, network, tốc độ giữ chân độc giả). Và version 1 rõ ràng có vấn đề: chỉ phù hợp với người đã có Github và quen với giao diện Github Editor - tức là loại trừ đa số độc giả.

**Version 2 - Static CMS:** Tôi rebuild tính năng này bằng [Static CMS](https://staticcms.org/) - hệ thống quản lý nội dung self-hosted với giao diện thân thiện hơn nhiều. Bất kỳ ai cũng có thể đóng góp mà không cần biết Github workflow.

**Conflict triết lý - điểm tôi phải dừng lại:** Nhưng đây là lúc tôi va vào một câu hỏi lớn hơn: *"Đây là blog cá nhân - mà lại mở quyền chỉnh sửa cho người ngoài?"* Ngoài ra, blog này chạy trên static hosting - nếu tốc độ tạo bài viết tăng không kiểm soát, server sẽ không chịu được. Chưa kể rủi ro bảo mật nếu bất kỳ ai cũng có thể truy cập CMS.

**Quyết định cuối cùng:** Giữ nguyên tính mở - nhưng **có kiểm soát**. Người ngoài chỉ được đóng góp trong phạm vi giá trị mà blog chỉ định, và mọi thay đổi đều phải qua bước phê duyệt của tôi trước khi xuất bản. Tôi hiện thực hóa điều này thông qua cấu hình của Static CMS, Github auth làm barrier có chủ đích, và [giấy phép sáng tạo nội dung đặc biệt](https://github.com/PhDoanh/content/blob/main/LICENSE.md) trên repo.

Kết quả là sự cân bằng giữa tính tương tác hai chiều và tính độc bản của một blog cá nhân!

## Mở rộng tính năng 🔓

Mặc định, Quartz được dùng như *sổ tay cá nhân kỹ thuật số*. Phần này liệt kê các tính năng tôi đã và đang áp dụng để tối ưu UX cho một blog thực thụ.

> [!info]- Tính năng ẩn của Quartz
> Quartz hỗ trợ một số tính năng mở rộng không được bật mặc định:
> - [Nhận xét bài viết](https://quartz.jzhao.xyz/features/comments)
> - [Các bài viết gần đây](https://quartz.jzhao.xyz/features/recent-notes)

### Chia sẻ bài viết

Cho phép chia sẻ đến các nền tảng cụ thể (Facebook, LinkedIn, Reddit, Twitter/X, Instagram) và nút Copy thân thiện hơn.

#### Cài đặt

1. Tạo các file sau trong repo:
	- [`quartz/components/MediaShare.tsx`](https://github.com/PhDoanh/blog/blob/v4/quartz/components/MediaShare.tsx)
	- [`quartz/components/styles/mediaShare.scss`](https://github.com/PhDoanh/blog/blob/v4/quartz/components/styles/mediaShare.scss)
	- [`quartz/components/scripts/mediaShare.inline.ts`](https://github.com/PhDoanh/blog/blob/v4/quartz/components/scripts/mediaShare.inline.ts)

2. Thêm vào [`quartz/components/index.ts`](https://github.com/PhDoanh/blog/blob/v4/quartz/components/index.ts):

```ts {2,6}
// other imports
import MediaShare from "./MediaShare"

export {
  // other exports
  MediaShare,
}
```

3. Kích hoạt trong [`quartz.layout.ts`](https://github.com/PhDoanh/blog/blob/v4/quartz.layout.ts):

```ts
Component.MediaShare({
  // support "facebook", "linkedin", "reddit", "twitter", "instagram"
  platforms: ["facebook", "instagram", "twitter"],
  copyButton: true,
}),
```

#### Tùy biến
- Component: `quartz/components/MediaShare.tsx`
- Style: `quartz/components/styles/mediaShare.scss`
- Script: `quartz/components/scripts/mediaShare.inline.ts`
- Vô hiệu hóa: Xóa tất cả `Component.MediaShare()` trong `quartz.layout.ts`
- Tùy chỉnh ngôn ngữ: tham khảo [`quartz/i18n/locales/`](https://github.com/PhDoanh/blog/blob/v4/quartz/i18n/locales/definition.ts)

### Chỉnh sửa bài viết (Edit This Page)

Tính năng đã được mô tả kỹ trong phần Nhật ký thất bại. Đây là cách cài đặt sau khi đã quyết định dùng Static CMS:

#### Cài đặt

1. Tạo các file sau:
	- [`quartz/components/EditThisPage.tsx`](https://github.com/PhDoanh/blog/blob/dev/quartz/components/EditThisPage.tsx)
	- [`content/admin/index.htm`](https://github.com/PhDoanh/content/blob/main/admin/index.htm)
	- [`content/admin/config.yml`](https://github.com/PhDoanh/content/blob/main/admin/config.yml)

2. Sửa `config.yml` theo [tài liệu CDN Hosting - Static CMS](https://staticcms.org/docs/docs/overview/cdn-hosting/) và cấu trúc nội dung blog của bạn.

3. Thêm vào `quartz/components/index.ts`:

```ts {2,6}
// other imports
import EditThisPage from "./EditThisPage"

export {
  // other exports
  EditThisPage,
}
```

4. Kích hoạt trong `quartz.layout.ts`: thêm `Component.EditThisPage()`

> [!info] Lưu ý
> Với cấu hình Github làm backend, bạn cần một máy chủ xác thực trung gian để người đóng góp đăng nhập qua Github. Đây là trade-off chấp nhận được - Github auth vừa là barrier bảo mật, vừa là filter chất lượng người đóng góp.

#### Tùy biến
- Component + Style: `quartz/components/EditThisPage.tsx`
- Vô hiệu hóa: Xóa tất cả `Component.EditThisPage()` trong `quartz.layout.ts`

### Danh sách cộng tác viên

Hiển thị danh sách cộng tác viên theo bài viết, kèm avatar Github và lịch sử thay đổi - tăng độ uy tín và tôn trọng quyền sáng tạo nội dung.

#### Cài đặt

1. Tạo các file sau:
	- [`quartz/components/GitHubContributors.tsx`](https://github.com/PhDoanh/blog/blob/v4/quartz/components/GitHubContributors.tsx)
	- [`quartz/components/styles/githubContributors.scss`](https://github.com/PhDoanh/blog/blob/v4/quartz/components/styles/githubContributors.scss)
	- [`quartz/components/scripts/githubContributors.inline.ts`](https://github.com/PhDoanh/blog/blob/v4/quartz/components/scripts/githubContributors.inline.ts)

2. Thêm vào `quartz/components/index.ts`:

```ts {2,6}
// other imports
import GitHubContributors from "./GitHubContributors"

export {
  // other exports
  GitHubContributors,
}
```

3. Bật trong `quartz.layout.ts`:

```ts
Component.GitHubContributors({
  owner: "PhDoanh",       // Github username
  repo: "demo",           // tên repo blog
  title: "Co-Authors",    // tiêu đề section, mặc định: "Contributors"
  limit: 20,              // số contributor tối đa hiển thị, mặc định: 10
})
```

#### Tùy biến
- Component: `quartz/components/GitHubContributors.tsx`
- Style: `quartz/components/styles/githubContributors.scss`
- Script: `quartz/components/scripts/githubContributors.inline.ts`
- Vô hiệu hóa: Xóa tất cả `Component.GitHubContributors()` trong `quartz.layout.ts`

### Cuộn lên đầu trang

Nút điều hướng nhanh lên đầu trang - đặc biệt hữu ích trên mobile với các bài viết dài.

#### Cài đặt

1. Tạo file [`quartz/components/BackToTop.tsx`](https://github.com/PhDoanh/blog/blob/dev/quartz/components/BackToTop.tsx)

2. Thêm vào `quartz/components/index.ts`:

```ts {2,6}
// các import khác
import BackToTop from "./BackToTop"

export {
  // các export khác
  BackToTop,
}
```

3. Thêm `Component.BackToTop()` vào `afterBody` của `quartz.layout.ts`

#### Tùy biến
- Component + Style + Script: `quartz/components/BackToTop.tsx`
- Vô hiệu hóa: Xóa tất cả `Component.BackToTop()` trong `quartz.layout.ts`

## Bài học 🧭

> Tool tốt nhất không phải tool mạnh nhất - mà là tool bạn có thể grow cùng nó theo thời gian.

Tôi không chọn Quartz vì feature list dài nhất. Tôi chọn nó vì kiến trúc của nó được thiết kế để không lock-in tôi vào bất kỳ quyết định nào hôm nay. Và mỗi lần tôi thêm một tính năng nhỏ (như Edit This Page), tôi lại va vào câu hỏi lớn hơn về triết lý thiết kế của chính mình.

Nếu bạn đang ở điểm xuất phát tương tự, câu hỏi quan trọng không phải *"tool này có tính năng X không?"* - mà là *"một năm nữa, tool này có còn phù hợp với hướng mình đang đi không?"*
