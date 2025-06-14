---
date: 2025-02-14
draft: false
status: Doing
title: Các nghiên cứu điển hình trong kỹ nghệ phần mềm
description: Khám phá bốn loại hệ thống phần mềm được sử dụng làm nghiên cứu điển hình trong kỹ nghệ phần mềm. Mỗi loại mang đến những thách thức và bài học thực tiễn quan trọng.
author: PhDoanh
authorlink: https://github.com/PhDoanh
tags:
  - software-technology
  - development
  - sofware-engineer
aliases:
  - case studies
cssclasses:
  - img
  - btn
---
%% ĐỊNH DẠNG TÊN FILE: "tên-bài-viết" | VD: jp-typing-guide %%

%% <figure style="text-align: center; margin: 20px auto;">
  <img 
    src="images/case-studies.png"
    alt="Các nghiên cứu điển hình trong kỹ nghệ phần mềm" 
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

Trong kỹ nghệ phần mềm, không có một phương pháp duy nhất nào phù hợp với tất cả các loại hệ thống. **Việc lựa chọn phương pháp phát triển phụ thuộc vào loại hệ thống đang được xây dựng**. Do đó, để minh họa các nguyên tắc của kỹ nghệ phần mềm, chúng ta sẽ xem xét **bốn nghiên cứu điển hình khác nhau** liên quan đến bốn loại hệ thống phổ biến:

1. **Hệ thống nhúng** - Điều khiển thiết bị phần cứng.
2. **Hệ thống thông tin** - Quản lý cơ sở dữ liệu thông tin.
3. **Hệ thống thu thập dữ liệu cảm biến** - Lưu trữ và xử lý dữ liệu môi trường.
4. **Môi trường hỗ trợ học tập** - Cung cấp công cụ phục vụ giáo dục.

Mỗi hệ thống có **đặc thù riêng**, dẫn đến những yêu cầu và cách tiếp cận phát triển khác nhau.

# 💉 Hệ thống nhúng - Điều khiển bơm insulin

Hệ thống nhúng là **phần mềm được tích hợp trong thiết bị phần cứng**, chẳng hạn như bơm insulin dành cho người tiểu đường.

**Cách thức hoạt động**:🩸 Cảm biến đo lượng đường trong máu ⟶ 📡 Gửi dữ liệu đến bộ điều khiển ⟶ 💉 Tính toán liều insulin cần thiết ⟶ 🖥️ Điều khiển bơm cung cấp insulin.

**Thách thức & lưu ý**:
- **Yêu cầu độ chính xác cao**: Nếu hệ thống cấp quá nhiều insulin, bệnh nhân có thể rơi vào trạng thái hôn mê.
- **Tính an toàn quan trọng**: Hệ thống phải **luôn sẵn sàng hoạt động** và **đưa ra liều lượng chính xác**.

> [!example]- Ví dụ
> Một bệnh nhân cần tiêm 10 đơn vị insulin, bộ điều khiển sẽ gửi 10 xung tín hiệu đến bơm để thực hiện thao tác này.

---

# 🏥 Hệ thống thông tin - Quản lý bệnh án tâm thần

Hệ thống thông tin chủ yếu tập trung vào **lưu trữ và truy xuất dữ liệu**. Ví dụ, hệ thống quản lý bệnh án tâm thần giúp bác sĩ theo dõi hồ sơ bệnh nhân.

**Các tính năng quan trọng**:
- **Lưu trữ thông tin cá nhân và bệnh án**.
- **Theo dõi lịch hẹn và nhắc nhở bác sĩ** nếu bệnh nhân vắng mặt quá lâu.
- **Cảnh báo khi bệnh nhân có hành vi nguy hiểm**.

**Thách thức**:
- **Bảo mật dữ liệu**: Chỉ nhân viên y tế có quyền truy cập.
- **Đồng bộ dữ liệu**: Khi làm việc ngoại tuyến, dữ liệu cần được cập nhật khi kết nối trở lại.

> [!info] Lưu ý
> Nếu hệ thống gặp sự cố, bác sĩ có thể không tiếp cận được thông tin bệnh nhân kịp thời.

---

# 🌦️ Hệ thống thu thập dữ liệu cảm biến - Trạm khí tượng hoang dã

Hệ thống này sử dụng **cảm biến để thu thập dữ liệu môi trường** và gửi về trung tâm phân tích.

**Chức năng chính**: 🌦 Đo nhiệt độ, áp suất, lượng mưa ⟶ 🛰 Gửi dữ liệu qua vệ tinh ⟶ 📊 Phân tích xu hướng thời tiết.

**Thách thức**:
- **Hoạt động trong điều kiện khắc nghiệt**: Thiết bị phải **chịu được gió lớn, nhiệt độ thấp hoặc cao**.
- **Quản lý năng lượng**: Hệ thống sử dụng **pin mặt trời** để duy trì hoạt động lâu dài.

**Ứng dụng thực tế**: Dữ liệu từ các trạm này giúp dự đoán biến đổi khí hậu.

---

# 🎓 Môi trường hỗ trợ học tập - Hệ thống giáo dục số

Hệ thống giáo dục số giúp học sinh và giáo viên sử dụng các công cụ hỗ trợ học tập trực tuyến.

**Chức năng**: 📚 Cung cấp bài giảng trực tuyến ⟶ 📑 Quản lý bài tập và điểm số ⟶ 🗣 Hỗ trợ giao tiếp giữa giáo viên và học sinh.

**Thách thức**:
- **Tính linh hoạt**: Phải tương thích với nhiều thiết bị khác nhau.
- **Cấu trúc phân tán**: Hệ thống hoạt động trên nền tảng đám mây.

> [!example]- Ví dụ
> Các nền tảng như Google Classroom hay Moodle là những ứng dụng phổ biến.

---

# 🔥 Tổng kết

Mỗi hệ thống phần mềm có những đặc thù riêng đòi hỏi phương pháp phát triển khác nhau:

- **Hệ thống nhúng** cần độ chính xác cao và an toàn tuyệt đối.
- **Hệ thống thông tin** tập trung vào bảo mật và khả năng đồng bộ dữ liệu.
- **Hệ thống thu thập dữ liệu cảm biến** phải hoạt động trong môi trường khắc nghiệt.
- **Môi trường giáo dục số** yêu cầu tính linh hoạt và hỗ trợ đa thiết bị.

📌 **Bài học rút ra**: **Không có một quy trình phần mềm nào phù hợp với tất cả hệ thống. Kỹ sư phần mềm cần linh hoạt lựa chọn phương pháp thích hợp cho từng loại dự án.**
