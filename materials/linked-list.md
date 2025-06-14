---
date: 2025-02-16
draft: true
status: Not started
title: "<% tp.file.cursor(1) %>"
description: "<% tp.file.cursor(2) %>"
author: PhDoanh
authorlink: https://github.com/PhDoanh
tags: 
  - "<% tp.file.cursor(3) %>"
aliases:
  - "linked list"
cssclasses:
  - img
  - btn
---
%% ĐỊNH DẠNG TÊN FILE: "tên-bài-viết" | VD: jp-typing-guide %%

<figure style="text-align: center; margin: 20px auto;">
  <img 
    src="images/linked-list.png"
    alt="<% tp.file.cursor(1) %>" 
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

Có 3 loại danh sách liên kết: đơn, đôi và vòng

> [!info] Ứng dụng
> - **Quản lý bộ nhớ động**: Dùng trong hệ thống quản lý bộ nhớ heap.
> - **Xây dựng các cấu trúc dữ liệu khác**: Như **Stack**, **Queue**, **Graph**,... 
> - **Undo/Redo trong phần mềm**: Hỗ trợ quay lui/quay lại các thao tác.
> - **Hệ thống quản lý tệp**: Ứng dụng trong việc quản lý file block trên ổ đĩa.

> [!check] Ưu điểm
> - **Không giới hạn kích thước cố định**: Có thể mở rộng động mà không cần cấp phát trước.
> - **Thêm/Xóa nhanh**: Chỉ mất **O(1)** nếu có con trỏ đến vị trí cần thao tác.
> - **Không bị giới hạn về không gian địa chỉ**: Giúp tiết kiệm bộ nhớ trong nhiều trường hợp.

> [!missing] Nhược điểm
> - **Truy cập phần tử chậm**: Phải duyệt từng nút thay vì truy cập trực tiếp như mảng.
> - **Tốn bộ nhớ hơn mảng**: Do cần lưu trữ con trỏ cho mỗi phần tử. 
> - **Cần quản lý bộ nhớ thủ công**: Cần thao tác **delete** để tránh rò rỉ bộ nhớ.