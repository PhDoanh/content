---
stage: Idea
title: Hướng dẫn cộng tác bài viết
description: ""
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

Mặc dù đây là trang blog cá nhân, nhưng mình hoan nghênh sự đóng góp của các bạn để cải thiện chất lượng bài viết lẫn trải nghiệm trang web. Bạn sẽ nhận được quyền lợi tương xứng với mức độ đóng góp của mình. Hãy đọc qua hướng dẫn bên dưới để hiểu cách tham gia hiệu quả.


# Nội quy cộng đồng

Dự án này tuân theo [Code of Conduct](LINK-TO-CODE-OF-CONDUCT), mong bạn giữ thái độ tích cực, tôn trọng và hợp tác trong mọi tương tác. :contentReference[oaicite:1]{index=1}

---

## 3. Cách báo lỗi (Issue)

- Trước khi tạo issue, **search** xem vấn đề đã được báo chưa.
- Sử dụng **template** có cấu trúc: tiêu đề ngắn + mô tả + bước tái hiện + log + môi trường.
- Label: `bug` / `enhancement`.

---

## 4. Cách đóng góp mã (PR)

1. Mong bạn mở issue để bàn trước nếu thay đổi lớn :contentReference[oaicite:2]{index=2}  
2. Fork repo –> tạo branch riêng tên `feature/<mô-tả-ngắn>`  
3. Viết code + unit test + docs (nếu cần)  
4. Chạy toàn bộ test (`npm test` / `make test`, ...)  
5. Viết commit theo chuẩn **imperative**, 50 ký tự đầu – ví dụ “Fix typo in README” :contentReference[oaicite:3]{index=3}  
6. Tạo PR: mô tả mục đích + issue liên quan + còn cần làm gì.  
7. Chờ phản hồi từ reviewers. Sau khi được approve, PR sẽ được merge.

---

## 5. Hướng dẫn môi trường dev & test

- Clone repo  
- Cài dependencies: `npm install`  
- Cài công cụ dev: `npm install -g xyz`  
- Chạy dev server: `npm run dev`  
- Chạy test: `npm test` hoặc `make test`

---

## 6. Quy tắc commit & PR

- **Commit message**: present-tense, tối đa 50 ký tự ở dòng đầu, cách dòng trống rồi bổ sung chi tiết nếu cần :contentReference[oaicite:4]{index=4}  
- **PR nhỏ** ưu tiên; nếu lớn, có thể chia thành nhiều phần dễ review  
- Trong PR, link tới issue: `Fixes #123` giúp tự động close khi merge

---

## 7. Các dạng đóng góp khác

Ngoài code, bạn có thể:
- Viết tài liệu lên Wiki
- Thiết kế UI/UX
- Viết blog/tutorial
- Dịch ngôn ngữ
- Giúp quản lý issue, review code

---

## 8. Cảm ơn & Công nhận

Rất cảm ơn mọi đóng góp của bạn 🎉  
Tên bạn sẽ được thêm vào file [ACKNOWLEDGEMENTS.md] hoặc credits trong bản release.

---

## 🛠 Template bắt đầu nhanh

```markdown
### Mục đích PR
> Ví dụ: Sửa lỗi hiển thị nút “Submit” trên màn hình mobile

### Mô tả
- Thay đổi A
- Thay đổi B

### Issue liên quan
Closes #456

### Test plan
Vào view X rồi thử thao tác Y, kết quả như Z
📞 Nếu bạn cần giúp đỡ
Mở issue với label help wanted

Tham gia Slack/Discord/Email: LINK


