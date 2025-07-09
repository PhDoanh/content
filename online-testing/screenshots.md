---
stage: "Draft"
title: "Ảnh chụp màn hình"
description: ""
permalink: ""
lang: vi
draft: true
tags: 
  - tutorials
  - windows
  - tester
  - android
  - online-testing
  - utest
aliases:
  - 
cssclasses:
  - img
  - btn
socialDescription: ""
socialImage: ""
---

# Tổng quan
**Ảnh chụp màn hình** là hình ảnh về dữ liệu được hiển thị trên màn hình máy tính hoặc thiết bị di động

Đây là một trong những đính kèm thiết yếu mà một tester cần có trong báo cáo lỗi của họ

Trong bài viết này, bạn sẽ được học cách chụp và chỉnh sửa ảnh chụp màn hình trên nhiều nền tảng khác nhau

## Quy định về ảnh chụp
- **Có điểm nhấn**: Luôn đánh dấu đối tượng bug trong ảnh chụp một cách rõ ràng. Dùng ô vuông hoặc tròn có màu đỏ hoặc vàng để làm nổi bật bug đó
- **Định dạng JPG hoặc PNG**: Luôn nhớ lưu hoặc chuyển đổi ảnh chụp về 2 định dạng này
- **Không sử dụng công cụ vẽ tay**: Tránh dùng bút vẽ để tô nhắn đối tượng bug trong ảnh
- **Chụp toàn màn hình**: Không chụp một phần màn hình hoặc chỉ chứa bug. Đảm bảo ảnh chụp bao gồm thanh URL khi kiểm thử trình duyệt
- **Đóng hết tab không cần thiết**: Đảm bảo ẩn đi hoặc đóng tất cả các tab không liên quan tới quá trình kiểm thử. *Quy định này chỉ áp dụng với kiểm thử trình duyệt* 
- **Chụp theo hướng thẳng đứng**: Mọi ảnh chụp màn hình phải theo hướng nhìn tự nhiên (không bị nghiêng, xoay góc, ...)

> [!info] Lưu ý
> Không tải lên quá 2 ảnh chụp màn hình trong một báo cáo lỗi

|         ![[low-high screenshot.png\|center]]         |
|:----------------------------------------------------:|
| **tip**: Ảnh **JPG** phù hợp hơn khi dùng để chia sẻ |

# Windows
## Cách 1: Dùng công cụ tích hợp sẵn
![[windows screenshots 1.gif|center]]

Bạn có thể chụp toàn màn hình hiện tại bằng cách nhấn tổ hợp phím **Windows+PrtSc**. Sau đó chỉnh sửa ảnh chụp bằng phần mềm **Paint** hoặc **Snipping Tool**

Mặc định, ảnh chụp màn hình sẽ được lưu vào thư mục **Screenshots** đặt bên trong **Pictures** và cũng có thể lấy nó ra từ bảng nhớ tạm với tổ hợp phím **Ctrl+V** (ngay sau khi chụp) hoặc **Windows+V**

## Cách 2: ShareX
![[EtEkIzoeTf.gif|center]]

1. Tải xuống và cài đặt phầm mềm ShareX tại [đây](https://www.getsharex.com/)

2. Mở **ShareX** lên và nhấp vào **After capture tasks**, sau đó:
	- Bỏ chọn tùy chọn **Upload image to host**
	- Chọn tùy chọn **Open Image in Editor**

3. Chụp toàn màn hình bằng 1 trong 2 cách:
	- Nhấp vào **Capture** và chọn **Full Screen**
	- Nhấn nút **PrtSc** trên bàn phím

4. Trình sửa ảnh sẽ tự động mở ra, dùng công cụ vẽ hình chữ nhật hoặc hình tròn để tô nhấn bug và nhấn **Enter** để lưu

Mặc định **ShareX** sẽ lưu các ảnh chụp màn hình trong thư mục **ShareX\\Screenshots** bên trong thư mục tài liệu **(Documents)**

> [!info] Lưu ý
> Đảm bảo tùy chọn **Upload image to host** đã được tắt trong phần mềm ShareX

## Cách 3: Xbox Game Bar
![[LXtpK6CL8D.gif|center]]

Làm theo các bước sau để bật tính năng **Xbox Game Bar**:
1. Nhấn tổ hợp phím **Windows+S** để mở thanh tìm kiếm và gõ "Xbox Game Bar"
2. Chọn **Enable Xbox Game Bar** từ kết quả và bật nó lên

Hoặc mở **Settings > Gaming > Xbox Game Bar** và bật công tắc kích hoạt

Các bước tiếp theo sẽ lưu ảnh chụp màn hình dưới dạng một file và loại trừ thanh tác vụ khỏi ảnh chụp:

1. Nhấn tổ hợp phím **Windows+G** để mở không gian Xbox Game Bar
2. Nhấp vào biểu tượng **Camera** để chụp màn hình hoặc có thể nhấn tổ hợp **Windows+Alt+PrtSc** để chụp trực tiếp mà không phải mở Xbox Game Bar
3. Một thông báo sẽ xuất hiện. Nhấp vào nó để xem ảnh vừa chụp
4. Nhấp vào **Open file location > Continue** để mở vị trí file ảnh
5. Đổi tên và di chuyển file đến vị trí mong muốn
6. Chỉnh sửa ảnh bằng phần mềm giống ở cách 1

# MacOS
%% gif/video về quy trình chụp trên Mac %%

Với người dùng Mac, công cụ chụp và chỉnh sửa ảnh có sẵn là quá đủ. Chỉ cần làm theo các bước sau:
1. Nhấn tổ hợp phím **Shift+Command+3** để chụp toàn màn hình
2. Ảnh sau khi chụp sẽ hiển thị ở góc màn hình, nhấp vào nó để chỉnh sửa
3. Chọn ô vuông hình chữ nhật hoặc hình tròn để tô nhấn bug
4. Nhấp vào **Done** để lưu lại

Mặc định, ảnh chụp màn hình sẽ được lưu vào **Desktop**

Tham khảo:
- [Take a screenshot on your Mac](https://support.apple.com/en-in/HT201361)
- [Annotate an image](https://support.apple.com/en-in/guide/preview/prvw1501/mac)

# Linux
%% gif/video về quy trình chụp trên Linux %%

Linux cung cấp vô vàn phần mềm bên ngoài để chụp và chỉnh sửa ảnh. Đây là tùy chọn được đề xuất bởi mình: [Flameshot](https://flameshot.org//)

Các bước sau sẽ cài đặt và sử dụng Flameshot:
1. Chạy lệnh `sudo apt-get update && sudo apt-get install flameshot` để cài đặt
2. Mở Flameshot lên như bao phần mềm khác
3. Bạn sẽ thấy biểu tượng của Flameshot trên thanh tác vụ, hãy nhấp vào nó
4. Dùng chuột để kéo thả toàn màn hình
5. Các công cụ khác sẽ hiển thị phía dưới, chọn ô vuông hình chữ nhật hoặc hình tròn
6. Vẽ hình đó bao quanh đối tượng cần tô nhấn
7. Lưu lại bằng cách nhấp vào nút **Save**

> [!info] Lưu ý
> Nếu gặp bất kì vấn đề cài đặt nào, bạn có thể xem tài liệu [này](https://flameshot.org//) để khắc phục

# Android
![[Screenrecording_20240826_082957-output.gif|center|300]]
## Chụp màn hình
1. Mở màn hình mà bạn muốn chụp lên

2. Tùy vào thiết bị đang sử dụng, thử một trong các cách dưới để chụp toàn màn hình:
	- Nhấn giữ phím nguồn và phím giảm âm lượng cùng lúc trong ít giây
	- Nhấn giữ phím nguồn trong ít giây và chạm vào Screenshot
	- Tra google nếu các cách trên không hoạt động 😅

3. Bạn có thể tìm thấy ảnh sau khi chụp trong ứng dụng thư viện ảnh của mình

## Chỉnh sửa ảnh
### Cách 1: Dùng ứng dụng chỉnh sửa ảnh
Thường ứng dụng thư viện ảnh của thiết bị sẽ có sẵn các tùy chọn tô nhấn. Nếu không có, bạn có thể thử đề xuất của mình: [iMarkup app](https://play.google.com/store/apps/details?id=com.winterso.markup.annotable&hl=en_IN)

1. Cài đặt ứng dụng từ cửa hàng Google Play và mở nó lên
2. Chạm vào giữa màn hình để nhập và chọn ảnh
3. Cho phép ứng dụng truy cập vào ảnh của bạn và chọn ảnh chụp màn hình
4. Chạm vào nút **Draw** từ thanh công cụ bên dưới
5. Vuốt sang trái để chọn ô hình chữ nhật hoặc hình tròn 
6. Vẽ ô đó quanh đối tượng cần tô nhấn và chạm vào nút ✔
7. Sau khi xong, chạm vào nút **Export** ở góc trên cùng bên phải
8. Chọn các tùy chọn hoặc để nguyên và nhấn **OK** để lưu về máy

### Cách 2: Dùng máy tính để chỉnh ảnh
1. Di chuyển ảnh chụp màn hình từ điện thoại sang máy tính, xem [cách thực hiện](https://support.google.com/android/answer/9064445)
2. Dùng bất kì phần mềm chỉnh ảnh nào phù hợp với nền tảng máy tính để tô nhấn

# iOS
%% gif/video về quy trình chụp và highlight trên ios %%

## Chụp màn hình
- Đối với iPhone đời cũ: Nhấn đồng thời nút home và nút nguồn bên cạnh điện thoại 
- Đối với iPhone đời mới: Nhấn nút nguồn và nút tăng âm lượng cùng lúc  

Quy trình trên được mô tả rõ ràng qua các bài viết sau: [iPhone](https://support.apple.com/en-us/HT200289), [iPad](https://support.apple.com/en-us/HT210781)

## Chỉnh sửa ảnh
### Cách 1: Dùng công cụ Markup tích hợp sẵn
1. Mở ứng dụng **Photos** và chọn ảnh chụp màn hình
2. Chạm vào nút **Edit** rồi đến nút ba chấm xuất hiện ở góc trên cùng bên phải
3. Chạm vào **Markup**
4. Chạm vào nút dấu cộng và chọn khung hình chữ nhật hoặc hình tròn
5. Vẽ quanh đối tượng cần tô nhấn và chọn màu đỏ hoặc vàng cho khung hình đó
6. Khi hoàn tất, chạm vào nút **Done** để lưu lại

### Cách 2: Dùng máy tính
1. Di chuyển ảnh chụp màn hình từ điện thoại sang máy tính của bạn, xem cách [làm](https://support.apple.com/en-in/HT201302)
2. Dùng bất kì phần mềm chỉnh ảnh nào phù hợp với nền tảng máy tính để tô nhấn

> [!info] Lưu ý
> Đảm bảo kết quả cuối cùng phù hợp với [[#Quy định về ảnh chụp|quy định]]






