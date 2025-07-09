---
stage: "Draft"
title: "Nhật ký thiết bị di động"
description: ""
permalink: ""
lang: vi
draft: true
tags: 
  - tutorials
  - tester
  - android
  - window
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

# Nhật ký thiết bị Android
Bạn có thể thu thập nhật ký android bằng máy tính Windows, MacOS, Linux, hay bất cứ nền tảng nào miễn là sử dụng **adb** hoặc **Android Studio** thay vì các ứng dụng như **Syslog** hoặc **CatLog**. 

**Trước khi thu thập, hãy đảm bảo**:
1. **USB Debugging** được bật trên điện thoại của bạn:
	- Trên điện thoại của bạn, mở ứng dụng Cài đặt lên
	- Tìm và chạm vào **Build number** 7 lần để kích hoạt **Công cụ nhà phát triển**
	- Bật tùy chọn **USB Debugging** lên
2. Điện thoại của bạn không được khóa, nên ở trạng thái đang hoạt động và kết nối với máy tính
3. Bạn có thể thấy một thông báo trên điện thoại yêu cầu cho phép kết nối, hãy chắc chắn bạn tích vào **Always allow from this computer** và chạm vào **Allow**

> [!info] Lưu ý
> Nếu bạn thấy một thông báo của **phần mềm quét virus** (antivirus) về **adb.exe**, thì hãy tắt phần mềm đó đi hoặc thêm **adb.exe** vào danh sách không theo dõi của phần mềm đó

## Dùng ADB để kết nối và thu thập
Tìm hiểu về **adb** tại [đây]([Android Debug Bridge (adb)  |  Android Studio  |  Android Developers](https://developer.android.com/tools/adb))

### Gỡ lỗi không dây (chỉ Android 11+)
%% gif/video %%

Bạn có thể skip phần này và đọc các hướng dẫn kết nối có dây phía dưới nếu phiên bản Android thấp hơn 11. Đảm bảo các thiết bị kết nối cùng mạng WiFi và thực hiện các bước sau:

1. Tải xuống, giải nén và mở thư mục [platform-tools](https://developer.android.com/tools/releases/platform-tools) trên máy tính của bạn
2. Trên điện thoại, đi tới **Settings > Developers Settings**
3. Một cửa sổ thông báo sẽ hiện ra với yêu cầu gỡ lỗi không dây qua mạng, tích vào **Always allow on this network** và chạm vào **Allow**
4. Chạm vào **Pair device with pairing code**
5. Trên máy tính, gõ **cmd** tại đường dẫn thư mục platform-tools và nhấn **Enter**
6. Nhập địa chỉ IP, cổng, và mã kết nối được hiển thị trên thiết bị Android của bạn với lệnh: `adb pair <Địa chỉ IP>:<Cổng> <Mã kết nối>`
7. Xong rồi thì kết nối với máy tính bằng lệnh: `adb connect <Địa chỉ IP>:<Cổng mới>`
8. Bây giờ bạn đã sẵn sàng thể thu thập nhật ký mà không phải thông qua dây cáp USB
9. Xóa nhật ký cũ bằng lệnh `adb logcat -c`
10. Thực hiện các bước tái tạo lỗi trên thiết bị Android
11. Thu thập bằng lệnh `adb logcat -d -v time >log.txt` **hoặc** `adb logcat -v threadtime >log.txt` và nhấn **Ctrl+C** để dừng thu thập
12. Bạn sẽ thấy file **log.txt** trong thư mục hiện tại
13. Tải lên báo cáo là xong!

> [!info] Lưu ý
> - Để thấy **thông báo gỡ lỗi không dây** lần đầu, bạn nên chạm vào **Revoke USB debugging authorizations** để xóa tất cả các xác thực USB đã lưu trước đó và thực hiện lại các bước trên
> - Nếu dung lượng nhật ký lớn mà dự án giới hạn tài nguyên tải lên, hãy thử lại bằng cách đóng hết ứng dụng không liên quan và xóa nhật ký cũ bằng lệnh `adb logcat -c` 

> [!tip] Mẹo
> Dùng kết nối không dây sẽ ổn định hơn cách trên

### Windows
%% gif/video %%

1. Tải xuống **SDK Platform Tools** tại [đây](https://developer.android.com/studio/releases/platform-tools.html) trên máy tính của bạn
2. Giải nén và lưu nó vào ổ cứng thiết bị mà bạn muốn
3. Mở thư mục **platform-tools** lên và gõ `cmd` trong thanh địa chỉ đường dẫn rồi nhấn **Enter**
4. Xóa nhật ký cũ trước đó bằng lệnh: `adb logcat -c`
5. Thực hiện các bước tái tạo lỗi trên thiết bị của bạn
6. Sau khi tái tạo xong, gõ lệnh: `adb logcat -d -v time >.\log.txt` để thu thập
7. Bạn sẽ thấy file **log.txt** trong thư mục hiện tại
8. Tải nó lên báo cáo lỗi là xong

**Cách khác (khuyên dùng)**:
1. Thực hiện các bước từ 1 đến 4 ở trên
2. Gõ `adb logcat -v threadtime >.\log.txt` để bắt đầu thu thập
3. Thực hiện các bước tái tạo lỗi và bạn sẽ thấy nhật ký được tạo ngay trong thời gian thực, khác với cách trên 
4. Nhấn tổ hợp **Ctrl+C** để dừng thu thập
5. Bạn sẽ thấy file **log.txt** trong thư mục hiện tại
6. Tải lên báo cáo và đảm bảo file không có vấn đề khi nhấp vào

> [!info] Lưu ý
> - Nếu dung lượng nhật ký lớn mà dự án giới hạn tài nguyên tải lên, hãy thử lại bằng cách xóa nhật ký cũ bằng lệnh `adb logcat -c` và chỉ mở ứng dụng cần kiểm thử để tái tạo
> - Nếu gặp vấn đề khi thực thi các lệnh **adb**, chạy `adb kill-server` để dừng tiến trình đang chạy và làm lại các bước trên

### MacOS
%% gif/video %%

1. Tải xuống **SDK Platform Tools** tại [đây](https://developer.android.com/studio/releases/platform-tools.html) trên máy Mac của bạn
2. Giải nén và lưu nó vào ổ cứng thiết bị mà bạn muốn
3. Mở **Terminal** lên và gõ `cd` kèm 1 dấu cách theo sau
4. Kéo thả thư mục **platform-tools** vừa tải xuống vào cửa sổ terminal và nhấn **Enter**
5. Xóa nhật ký cũ trước đó bằng lệnh: `./adb logcat -c`
6. Thực hiện các bước tái tạo lỗi trên thiết bị của bạn
7. Sau khi tái tạo xong, gõ lệnh: `./adb logcat -d -v time >./log.txt` để thu thập
8. Bạn sẽ thấy file **log.txt** trong thư mục hiện tại
9. Tải nó lên báo cáo lỗi là xong

**Cách khác (khuyên dùng)**:
1. Thực hiện các bước từ 1 đến 4 ở trên
2. Gõ `./adb logcat -v threadtime >./log.txt` để bắt đầu thu thập
3. Thực hiện các bước tái tạo lỗi và bạn sẽ thấy nhật ký được tạo ngay trong thời gian thực, khác với cách trên 
4. Nhấn tổ hợp phím **Ctrl+C** để dừng thu thập
5. Bạn sẽ thấy file **log.txt** được tạo trong thư mục hiện tại
6. Tải nó lên báo cáo và đảm bảo file không có vấn đề khi nhấp vào

### Linux
%% gif/video %%

1. Mở **Terminal** lên và gõ lệnh sau tùy vào bản phân phối Linux của bạn
	- Bản **Debian (Ubuntu, Linux Mint, ...)**: `sudo apt-get install adb`
	- Bản **Fedora/SUSE**: `sudo yum install android-tools`
2. Cung cấp mật khẩu thiết bị và đợi đến khi cài xong
3. Xóa nhật ký cũ bằng lệnh: `adb logcat -c`
4. Thực hiện các bước tái tạo lỗi
5. Sau khi tái tạo xong, gõ lệnh: `./adb logcat -d -v time >./log.txt` để thu thập
6. Bạn sẽ thấy file **log.txt** trong thư mục hiện tại
7. Tải nó lên báo cáo lỗi là xong

**Cách khác (khuyên dùng)**:
1. Thực hiện các bước từ 1 đến 3 ở trên
2. Gõ `./adb logcat -v threadtime >./log.txt` để bắt đầu thu thập
3. Thực hiện các bước tái tạo lỗi và bạn sẽ thấy nhật ký được tạo ngay trong thời gian thực, khác với cách trên 
4. Nhấn tổ hợp phím **Ctrl+C** để dừng thu thập
5. Bạn sẽ thấy file **log.txt** được tạo trong thư mục hiện tại
6. Tải nó lên báo cáo và đảm bảo file không có vấn đề khi nhấp vào

> [!info] Lưu ý
> Bạn cũng có thể tải xuống **platform-tools** ở [đây](https://developer.android.com/studio/releases/platform-tools) và thực hiện các bước từ 2 đến 4 tương tự như Windows 

## Dùng Android Studio
%% link %%
Tìm hiểu về Android Studio tại [đây]()

### Gỡ lỗi không dây (chỉ Android 11+)
%% gif/video %%

Đảm bảo các thiết bị kết nối cùng mạng **WiFi** và thực hiện các bước sau:
1. Trên máy tính của bạn, tải xuống và cài đặt **Android Studio** tại [đây](https://developer.android.com/studio/) 
2. Trong phần **Setup Wizard**, nhấp vào **Next**
3. Đối với mảng testing, thay đổi cài đặt thành **Custom** để loại bỏ việc cài đặt các tệp không cần thiết và không liên quan
4. Bỏ tích tất cả các thành phần tùy chọn và nhấp vào **Next**
5. Trong màn hình chào mừng của **Android Studio**, nhấp vào **New Project** và chọn **Empty Activity**
6. Nhấp vào **Next > Finish** và không cần thay đổi thêm gì cả
8. Sau khi quá trình đồng bộ hoàn tất, nhấp vào danh sách thả **No Device**
9. Nhấp vào **Pair device using Wifi** và đi tới tab **Pair using the pairing code**
10. Giờ hãy đi tới **Settings > Developers options** trên điện thoại của bạn
11. Chạm vào **Wireless debugging** và bật nó lên
12. Chạm vào **Pair device with Pairing code** hoặc chạm vào **Pair device with QR code** để quét mã QR
13. Nhấp vào nút **Pair** bên cạnh đỉa chỉ IP xuất hiện khớp với IP của điện thoại trên Android Studio
14. Gõ mã kết nối và nhấp vào **Pair**
15. Khi kết nốt thành công, nhấp vào **Logcat** từ dưới màn hình và xóa các bộ lọc nếu nó tự động chọn lọc
16. Xóa nhật ký cũ bằng cách nhấp vào **biểu tượng thùng rác**
17. Giờ hãy thực hiện các bước tái tạo lỗi trên điện thoại 
18. Trên máy tính, nhấp vào nút **Pause** để dừng việc Android Studio tiếp tục ghi nhật ký
19. Nhấn **Ctrl+A** đẻ chọn tất cả nhật ký và chuột phải để chọn **Copy**
20. Mở bất kì trình soạn thảo văn bản nào và tạo file mới, dán nhật ký vừa sao chép và lưu lại với định dạng **.txt**

> [!info] Lưu ý
> Khi đã kết nối thành công lần đầu thì những lần sau Android Studio sẽ tự phát hiện và kết nối thiết bị của bạn để tạo nhật ký miễn là tùy chọn **wireless debugging** trên điện thoại được bật

### Gỡ lỗi có dây
%% gif/video %%

1. Tải xuống và cài đặt **Android Studio** tại [đây](https://developer.android.com/studio/)
2. Tải xong thì mở **Android Studio** lên
3. Trong phần **Setup Wizard**, nhấp vào **Next**
4. Thay đổi cài đặt thành **Custom** để loại bỏ việc cài đặt các tệp không cần thiết và không liên quan đến mảng testing
5. Bỏ tích tất cả các thành phần tùy chọn và nhấp vào **Next**
6. Bên trong màn hình chào mừng của **Android Studio**, nhấp vào **New Project** và chọn **Empty Activity**
7. Nhấp vào **Next > Finish** và không cần thay đổi thêm gì cả
8. Đợi đến khi quá trình đồng bộ hoàn tất và mở **Logcat** từ menu **View > Tool Windows > Logcat** hoặc nhấp trực tiếp vào nút **Logcat** nếu nó hiển thị ở dưới màn hình
9. Kết nối Android của bạn với máy tính
10. Trong cửa sổ **Logcat**, chọn thiết bị Android của bạn nếu nó không tự động chọn và xóa nhật ký cũ đi bằng cách nhấp vào **biểu tượng thùng rác**
11. Thực hiện các bước tái tạo lỗi trên điện thoại Android
12. Trên máy tính, nhấp vào nút **Pause** để dừng Android Studio từ việc ghi nhật ký
13. Nhấn **Ctrl+A** để chọn tất cả nhật ký được ghi và chuột phải vào đó để chọn **Copy**
14. Mở bất kì **trình sửa văn bản** nào và tạo file mới, dán nội dung đã sao chép rồi lưu lại với định dạng **.txt**

> [!info] Lưu ý
> Nếu dung lượng nhật ký lớn mà dự án giới hạn tài nguyên tải lên, hãy thử lại bằng cách đóng hết ứng dụng không liên quan và xóa nhật kỹ cũ bằng cách nhấp vô **biểu tượng thùng rác**, sau đó tái tạo lại lần nữa.

# Nhật ký thiết bị iOS
Có vô vàn phần mềm quản lý thiết bị iOS mà hỗ trợ nhật ký console, nhưng mình khuyên bạn nên dùng **iMazing** vì nó hoạt động trên cả Windows và MacOS. Còn Linux sẽ có phần mềm riêng biệt của nó

## iMazing (Windows hoặc MacOS)
%% gif/video %%

1. Mở trang này lên: https://imazing.com/download
2. Tải xuống phần mềm tương thích với hệ điều hành máy tính của bạn và cài đặt nó
3. Mở **iMazing** lên và kết nối máy tính với thiết bị iOS
4. Nhấp vào **Show Device Console** trong phần mềm
5. Xóa console cũ và bắt đầu tái tạo lỗi
6. Tái tạo xong rồi thì nhấp vào **Pause > Save** 
7. Lưu lại ở định dạng **.txt**
8. Tải lên báo cáo lỗi là xong

> [!warning] Thông tin quan trọng 
> Phần mềm này **miễn phí** với người dùng cá nhân và người liên quan tới ngành giáo dục nhưng **trả phí** cho tổ chức thương mại. Trường hợp dùng cá nhân có thể yêu cầu bạn mua một giấy phép sử dụng. **Mỗi người dùng có trách nhiệm tuân thủ các điều khoản và thực hiện nghĩa vụ mà thỏa thuận của giấy phép đưa ra!** 

> [!info] Lưu ý
> Ngoài **iMazing** ra, bạn có thể thử **3uTools** hoặc **iTools** nhưng chúng chỉ hỗ trợ cho thiết bị Windows. Và có thể thử phần mềm ngay dưới đây trên **Mac** nếu cái này không hoạt động với bạn

## Console (chỉ MacOS)
%% gif/video %%

1. Kết nối iOS của bạn với máy tính Mac qua mạng Internet
2. Trên máy tính, mở phần mềm **Console**
3. Chọn thiết bị iOS vừa kết nối
4. Đảm bảo bạn đang ở tab **All messages**, xóa nhật ký cũ bằng cách nhấp vào nút **Clear**
5. Thực hiện các bước tái tạo lỗi trên iOS
6. Nhấn tổ hợp phím **Command+A** để chọn tất cả nhật ký được ghi và nhấn **Command+C** để sao chép chúng
7. Mở trình soạn thảo văn bản như **TextEdit** lên, mở cài đặt của nó và thay đổi định dạng file thành **văn bản thô (.txt)**
8. Tạo mới file rồi dán nhật ký đã sao chép bằng cách nhấn **Command+V**
9. Lưu lại với định dạng **.txt** và tải lên báo cáo

## libimobiledevice (chỉ Linux)
%% gif/video %%

1. Tải xuống và cài đặt phần mềm [libimobiledevice](https://libimobiledevice.org/)
2. Dùng dây cáp **USB** để kết nối iOS với máy tính của bạn
3. Chuột phải vào thư mục **Desktop** và chọn **Open terminal here**
4. Trong cửa sổ terminal, gõ lệnh: `idevicesyslog | tee log.txt` để thu thập và ghi nhật ký vào file
5. Thực hiện các bước tái tạo lỗi trên iOS
6. Nhấn tổ hợp phím **Ctrl+C** để dừng thu thập, sau đó đóng terminal lại
7. Tìm file **log.txt** và tải lên báo cáo là xong

## Nhật ký "Crashed App"
Loại nhật ký này được yêu cầu khi một ứng dụng iOS bị tắt đột ngột với thông báo có mã lỗi đi kèm, nó giống như **màn hình xanh chết chóc trên Windows** và đươc xếp vào loại lỗi **nghiêm trọng nhất**. Không giống Android, nhật ký này trên iOS cần được thu thập theo cách riêng biệt 

Các nhà phát triển sẽ dùng nhật ký này để phân tích về vấn đề bị crash, và dựa trên nó để hiểu các vấn đề tồn đọng, tiềm ẩn trong ứng dụng

**Có 2 cách chính để thu thập loại nhật ký này**:
### Trực tiếp trên iPhone hoặc iPad
%% gif/video %%

1. Thực hiện các bước tái tạo lỗi bắt đầu từ hành động mở app
2. Mở ứng dụng **Settings** lên 
3. Chạm vào **Privacy**
4. Vuốt xuống dưới và chạm vào **Analytics & Improvements**
5. Chạm vào **Analytics Data**
6. Chạm vào **báo cáo** với tên ứng dụng bị crash cùng mốc thời gian (danh sách được sắp xếp theo bảng chữ cái)
7. Chia sẻ qua bất kì ứng dụng nào có sẵn (ví dụ: Gmail) rồi lại tải xuống từ đó
8. Tải lên nhật ký với định dạng **.ips** tới bài báo cáo của bạn

### iTunes (Windows hoặc MacOS dựa trên Catalina)
%% gif/video %%

1. Tải xuống, cài đặt và mở [iTunes](https://www.apple.com/itunes/download/) lên
2. Kết nối iOS tới máy tính qua dây cáp **USB** (Nếu quá trình đồng bộ không tự bắt đầu, bạn phải bắt đầu nó một cách thủ công)
3. Thực hiện các bước tái tạo lỗi bắt đầu từ hành động mở app
4. Đi tới thư mục **Reports** trên máy tính của bạn (Đảm bảo bật tùy chọn **show hidden items**) theo định dạng sau:
	- **MacOS X**: `~/Library/Logs/CrashReporter/MobileDevice/<tên thiết bị>`
	- **Windows**: `C:\Users\<tên người dùng>\AppData\Roaming\Apple Computer\Logs\CrashReporter\MobileDevice\<tên thiết bị>`
5. Tìm file **.log, .crash hoặc .ips** bao gồm tên ứng dụng bị crash và dấu thời gian
6. Tải lên báo cáo lỗi của bạn






