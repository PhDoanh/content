---
date: <% tp.file.creation_date("YYYY-MM-DD") %>
draft: true
status: Not started
title: "<% tp.file.title.split("_")[0] %>. <% tp.file.cursor(1) %>"
description: "<% tp.file.cursor(2) %>"
author: PhDoanh
authorlink: https://github.com/PhDoanh
tags:
  - japanese
  - grammar
  - language
  - <% tp.file.cursor(3) %>
aliases:
  - <% tp.file.title.split("_")[1].split("-").join(" ") %>
cssclasses: 
  - img
  - btn
---
%% LƯU Ý 
- Định dạng tên file: "tên-bài-viết" (jp-typing-guide, ...) 
%%

%% banner
<figure style="text-align: center; margin: 20px auto;">
  <img 
    src="images/<% tp.file.title %>.png"
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
    <em>Cấu trúc ngữ pháp đầy đủ</em>
  </figcaption>
</figure>
%%

# ✨ Ứng dụng
## {trường hợp dùng} 
%% mô tả %%

**Cấu trúc:**

**Ví dụ:**

> [!content]- {bản gốc}
> {bản dịch}

---

# 🔓 Mở rộng ngữ pháp   
## {trường hợp dùng}  
%% mô tả %%

**Cấu trúc:**

**Ví dụ:**

> [!content]- {bản gốc}
> {bản dịch}

---

# 👀 Mẹo & Lưu ý
> [!tip] Mẹo học và thi
> 

> [!caution] Lưu ý quan trọng
> 

> [!info] Ngữ pháp tương tự
> 

---

# 🔥Tổng kết
{tóm tắt, nhận xét}

> [!advices] Lời khuyên
> 
