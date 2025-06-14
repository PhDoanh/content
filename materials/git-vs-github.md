---
date: 2025-02-10
draft: true
status: Doing
title: Hiểu Git và Github trong 5 phút!
description: Git là một hệ thống quản lý phiên bản phân tán, giúp theo dõi và kiểm soát thay đổi trong mã nguồn một cách hiệu quả. GitHub là một nền tảng trực tuyến dựa trên Git, cho phép lưu trữ, chia sẻ và cộng tác trong dự án phần mềm.
author: PhDoanh
authorlink: https://github.com/PhDoanh
tags:
  - coding
  - git
  - github
  - dev-tools
  - version-control
aliases:
  - git vs github
  - Hiểu Git và Github trong 5 phút!
cssclasses:
  - img
  - btn
---
%% ĐỊNH DẠNG TÊN FILE: "tên-bài-viết" | VD: jp-typing-guide %%

%% <figure style="text-align: center; margin: 20px auto;">
  <img 
    src="images/git-vs-github.png"
    alt="Hiểu Git và Github trong 5 phút!" 
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

# Quản Lý Phiên Bản Mã Nguồn 📜

**Quản lý phiên bản mã nguồn** là một phương pháp giúp theo dõi và quản lý các thay đổi trong mã nguồn của dự án phần mềm. Dưới đây là những lý do tại sao việc quản lý phiên bản lại quan trọng:

- ✅ **Ghi lại thay đổi:** Theo dõi từng chỉnh sửa trên mã nguồn
- ✅ **Hỗ trợ làm việc nhóm:** Giúp các lập trình viên cộng tác hiệu quả
- ✅ **Lưu trữ lịch sử phát triển:** Cho phép quay lại phiên bản trước nếu có lỗi xảy ra
- ✅ **Giúp kiểm soát sự thay đổi:** Dễ dàng kiểm tra ai đã chỉnh sửa phần nào của dự án

💡 **Mẹo:** Nếu bạn làm việc trong một nhóm phát triển, hãy sử dụng công cụ quản lý phiên bản như **Git** hoặc **GitHub** để duy trì quy trình làm việc chuyên nghiệp!

---

# Git Là Gì? 🧑‍💻

**Git** là một hệ thống quản lý phiên bản phân tán, được tạo ra vào năm 2005 bởi **Linus Torvalds** để hỗ trợ phát triển **Linux Kernel**. Một số đặc điểm quan trọng của Git:

- 🏆 **Hiệu suất cao:** Hỗ trợ lưu trữ và truy xuất nhanh chóng
- 🔄 **Phân tán:** Mỗi lập trình viên có một bản sao đầy đủ của kho lưu trữ (repository)
- 🔍 **Theo dõi thay đổi:** Ghi lại toàn bộ lịch sử chỉnh sửa của dự án

🚀 **Lợi ích lớn nhất của Git là khả năng làm việc offline** – bạn có thể commit thay đổi cục bộ và sau đó đồng bộ khi có kết nối mạng.

---

# Một Số Khái Niệm Cơ Bản 🏗️

## Snapshots

Git sử dụng **snapshot** để lưu trạng thái của dự án tại một thời điểm cụ thể.

**Lợi ích của snapshot:**

- Giúp quay lại các phiên bản trước đó dễ dàng
- Hạn chế mất dữ liệu khi chỉnh sửa

💡 **Ví dụ:** Nếu bạn vô tình xóa một file quan trọng, Git có thể giúp bạn khôi phục lại!

## Commit

**Commit** là hành động lưu một snapshot của mã nguồn vào lịch sử Git.

- Một commit gồm:
    - Danh sách các thay đổi
    - Liên kết đến commit trước đó (_parent commit_)
    - Một mã hash duy nhất (hash code)

💡 **Mẹo:** Luôn sử dụng mô tả ngắn gọn nhưng rõ ràng khi commit để giúp đồng đội hiểu thay đổi của bạn!

## Repository (Repo)

Repo chứa toàn bộ mã nguồn và lịch sử thay đổi.

- Repo có thể lưu trên **máy cá nhân** hoặc **máy chủ từ xa (GitHub)**
- Khi tải repo về máy, ta gọi là **cloning**
- Khi lấy thay đổi mới nhất từ server, ta gọi là **pulling**
- Khi đẩy thay đổi từ máy lên server, ta gọi là **pushing**

## Branches

Branches (nhánh) cho phép bạn làm việc trên nhiều tính năng mà không ảnh hưởng đến nhánh chính.

- Nhánh chính trong Git thường gọi là **master** hoặc **main**
- Mỗi commit đều thuộc về một nhánh nào đó
- Có thể tạo nhiều nhánh để phát triển tính năng mới

💡 **Lưu ý:** Hãy luôn kiểm tra nhánh hiện tại bằng `git branch` trước khi thực hiện commit!

---

# GitHub Là Gì? 🌐

**GitHub** là một nền tảng lưu trữ mã nguồn trực tuyến, giúp lập trình viên quản lý và cộng tác trong dự án Git.

- 📡 **Lưu trữ mã nguồn trực tuyến**
- 👥 **Hỗ trợ làm việc nhóm**
- 🛠️ **Cung cấp công cụ quản lý dự án, báo lỗi**
- 🔎 **Dễ dàng theo dõi và kiểm tra lịch sử thay đổi**

🔗 [Truy cập GitHub tại đây](https://www.github.com/)

---

# Cài Đặt Git ⚙️

## Trên Linux

- Debian/Ubuntu: `sudo apt-get install git`
- Fedora: `sudo yum install git`

## Trên macOS

- Tải tại: [Git cho macOS](http://git-scm.com/download/mac)

## Trên Windows

- Tải tại: [Git cho Windows](http://git-scm.com/download/win)

💡 **Mẹo:** Sau khi cài đặt, kiểm tra phiên bản Git bằng lệnh `git --version`

---

# Các Lệnh Git Cơ Bản 🔥

## Tạo Git Repo Cục Bộ

```sh
git init
```

## Thêm File Vào Staging Area

```sh
git add filename
```

## Commit Thay Đổi

```sh
git commit -m "Mô tả thay đổi"
```

## Sao Chép Repo Về Máy

```sh
git clone [URL]
```

## Kiểm Tra Trạng Thái File

```sh
git status
```

## Xem Lịch Sử Commit

```sh
git log
```

💡 **Lưu ý:** Luôn kiểm tra trạng thái bằng `git status` trước khi commit!

---

# Tổng Kết

Git và GitHub là hai công cụ mạnh mẽ giúp quản lý mã nguồn hiệu quả. Trong bài viết này, chúng ta đã tìm hiểu:

- 📌 **Git** là gì và cách hoạt động của nó
- 📌 **Các khái niệm quan trọng** như commit, repo, branch
- 📌 **Cách cài đặt và sử dụng Git** trên các hệ điều hành
- 📌 **GitHub** và những lợi ích khi sử dụng nền tảng này

🚀 **Bắt đầu ngay:** Hãy thử tạo một repo trên GitHub và thực hành các lệnh Git để làm chủ công cụ này! 💪
