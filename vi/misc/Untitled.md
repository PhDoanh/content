---
stage: Idea
draft: true
title: Hướng dẫn tạo trình cài đặt ứng dụng Windows bằng WiX v4
description:
tags:
socialDescription:
socialImage:
permalink:
lang: vi
aliases:
cssclasses:
  - img
---
[Create installers for windows apps using WiX v4 | by Kamran Asgarov | Medium](https://medium.com/%40tivole/create-installers-for-windows-apps-using-wix-v4-d1ec73554dbe)

## 1. Chuẩn bị & cấu trúc dự án

### 1.1 Thiết lập WiX v4

- Cài WiX Toolset v4 (theo hướng dẫn chính thức từ WiX / FireGiant).
    
- Thiết lập biến môi trường nếu cần (chẳng hạn `WIX` hoặc dùng MSBuild integration).
    
- Tạo giải pháp / solution (ví dụ: `MyAppInstaller.sln`) chứa ít nhất một dự án `.wixproj` và (nếu cần) dự án ứng dụng (WPF, Win32, service, tùy bạn).
    

### 1.2 Cấu trúc thư mục gợi ý

Ví dụ cấu trúc như sau:

```
/repo-root
  /MyApp               ← mã ứng dụng chính (WPF, WinForms, console, Win32, service…)
  /Installer
    Installer.wixproj
    /WxsIncludes
      Folders.wxs
      Components.wxs
      Shortcuts.wxs
      UI.wxs
      Upgrade.wxs
      CustomActions.wxs
    /CustomActionsBin
      (DLL hoặc EXE mã tùy chỉnh nếu có)
    build.cmd / build.ps1
README.md
```

- Chia các phần `.wxs` theo chức năng (folders, components, UI, upgrade, custom actions) để dễ quản lý khi dự án mở rộng (modular).
    
- Nếu bạn có custom action bằng C# / C++ / PowerShell, đặt trong `CustomActionsBin` và tham chiếu từ file `.wxs`.
    

Repo mẫu bạn gửi (`tivole/sample-wpf-app`) cũng theo cấu trúc tương tự (Folders.wxs, Components.wxs, Shortcuts.wxs). Mình sẽ mở rộng thêm UI và custom actions trong bản mẫu gốc.

---

## 2. Viết file WiX cơ bản (.wxs)

Đây là phần “cốt lõi” mà bài gốc cũng đã minh họa rất tốt — mình tóm tắt, sau đó bạn sẽ mở rộng từ đó.

Ví dụ file `Package.wxs`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<Wix xmlns="http://wixtoolset.org/schemas/v4/wxs">
  <Product Id="*" 
           UpgradeCode="PUT-GUID-HERE"
           Name="MyApp"
           Version="1.0.0.0"
           Manufacturer="YourCompany"
           Language="1033">
    <Package InstallerVersion="500" Compressed="yes" InstallScope="perMachine" />

    <MediaTemplate />

    <Feature Id="MainFeature" Title="MyApp Feature" Level="1">
      <ComponentGroupRef Id="MainComponents"/>
    </Feature>

    <UIRef Id="WixUI_Minimal"/>

  </Product>
</Wix>
```

- `UpgradeCode` giữ cố định qua các version để hỗ trợ nâng cấp.
    
- `ComponentGroupRef` nối với `Components.wxs` chứa các thành phần file / registry / shortcut.
    
- `UIRef` tham chiếu UI mặc định (có thể thay bằng UI tùy chỉnh).
    

Trong `Components.wxs`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<Wix xmlns="http://wixtoolset.org/schemas/v4/wxs">
  <Fragment>
    <DirectoryRef Id="INSTALLFOLDER">
      <Component Id="cmpMyExe" Guid="PUT-GUID-HERE">
        <File Source="$(var.MyApp.TargetPath)" KeyPath="yes"/>
        <Shortcut Id="desktopShortcut"
                  Directory="DesktopFolder"
                  Name="MyApp"
                  WorkingDirectory="INSTALLFOLDER"
                  Target="[INSTALLFOLDER]MyApp.exe" />
        <RemoveFolder Id="RemoveDesktopShortcut" On="uninstall" Directory="DesktopFolder" />
        <RegistryValue Root="HKLM" Key="Software\MyCompany\MyApp" Name="Installed" Type="integer" Value="1" KeyPath="yes"/>
      </Component>
    </DirectoryRef>

    <ComponentGroup Id="MainComponents">
      <ComponentRef Id="cmpMyExe"/>
    </ComponentGroup>
  </Fragment>
</Wix>
```

Trong `Folders.wxs`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<Wix xmlns="http://wixtoolset.org/schemas/v4/wxs">
  <Fragment>
    <Directory Id="TARGETDIR" Name="SourceDir">
      <Directory Id="ProgramFilesFolder">
        <Directory Id="INSTALLFOLDER" Name="MyApp" />
      </Directory>
      <Directory Id="DesktopFolder" />
    </Directory>
  </Fragment>
</Wix>
```

File `Shortcuts.wxs` (nếu bạn muốn tách riêng phần shortcut UI, StartMenu):

```xml
<?xml version="1.0" encoding="utf-8"?>
<Wix xmlns="http://wixtoolset.org/schemas/v4/wxs">
  <Fragment>
    <DirectoryRef Id="INSTALLFOLDER">
      <Component Id="cmpStartMenuShortcut" Guid="PUT-GUID-HERE">
        <Shortcut Id="startMenuShortcut"
                  Directory="ProgramMenuFolder"
                  Name="MyApp"
                  WorkingDirectory="INSTALLFOLDER"
                  Target="[INSTALLFOLDER]MyApp.exe" />
        <RemoveFolder Id="RemoveStartMenuFolder" Directory="ProgramMenuFolder" On="uninstall"/>
        <RegistryValue Root="HKLM" Key="Software\MyCompany\MyApp" Name="StartMenuInstalled" Type="integer" Value="1" KeyPath="yes"/>
      </Component>
    </DirectoryRef>
    <ComponentGroup Id="ShortcutComponents">
      <ComponentRef Id="cmpStartMenuShortcut"/>
    </ComponentGroup>
  </Fragment>
</Wix>
```

Khi build, các `.wxs` sẽ được “candle / light” để tạo thành `.msi`.

---

## 3. UI tùy chỉnh & dialog wizard, binding property

Bài gốc sử dụng UI mặc định (`WixUI_Minimal`), nghĩa là không nhiều tùy chọn nhập liệu từ người dùng. Mình sẽ mở rộng để bạn có thể:

- Cho người dùng chọn thư mục cài đặt
    
- Nhập thông tin cấu hình (ví dụ: tên user, option bật/tắt module)
    
- Liên kết những input đó (properties) vào component / action tương ứng
    
- Tùy chỉnh giao diện wizard nếu cần
    

### 3.1 Định nghĩa dialog wizard mới

Bạn có thể thêm file `UI.wxs` chứa UI tùy chỉnh:

```xml
<?xml version="1.0" encoding="utf-8"?>
<Wix xmlns="http://wixtoolset.org/schemas/v4/wxs"
     xmlns:ui="http://wixtoolset.org/schemas/v4/ui">
  <Fragment>
    <UI>
      <Dialog Id="CustomInstallDlg" Width="370" Height="270" Title="Cài đặt MyApp">
        <Control Id="Next" Type="PushButton" X="236" Y="243" Width="56" Height="17" Default="yes" Text="Next">
          <Publish Event="NewDialog" Value="VerifyReadyDlg">1</Publish>
        </Control>
        <Control Id="Cancel" Type="PushButton" X="304" Y="243" Width="56" Height="17" Text="Cancel">
          <Publish Event="SpawnDialog" Value="CancelDlg">1</Publish>
        </Control>
        <Control Id="InstallFolderLabel" Type="Text" X="20" Y="70" Width="290" Height="20" Text="Chọn thư mục cài đặt:"/>
        <Control Id="InstallFolder" Type="PathEdit" X="20" Y="90" Width="290" Height="18" Property="INSTALLFOLDER"/>
        <!-- Bạn có thể thêm nhiều control input khác, ví dụ checkbox, textbox để cấu hình module -->
      </Dialog>
    </UI>

    <UIRef Id="WixUI_Common"/>
    <Publish Dialog="WelcomeDlg" Control="Next" Event="NewDialog" Value="CustomInstallDlg">1</Publish>
  </Fragment>
</Wix>
```

- `INSTALLFOLDER` là **property** đại diện cho thư mục cài đặt — bạn bind `PathEdit` control với property này.
    
- Bạn có thể thêm các control dạng `Checkbox`, `Edit` để người dùng nhập thông tin hoặc bật/tắt tính năng, và gán property tương ứng.
    
- Trong các `.wxs` khác (component, feature) bạn có thể dùng condition dựa trên property để quyết định cài hay không.
    

### 3.2 Liên kết property với component / điều kiện

Ví dụ, bạn muốn cài thêm module phụ nếu người dùng chọn (property `INSTALL_MODULE_X = 1`):

Trong `Components.wxs`:

```xml
<Component Id="cmpModuleX" Guid="GUID-MODULE-X">
  <Condition>INSTALL_MODULE_X = "1"</Condition>
  <File Source="$(var.ModuleXPath)" KeyPath="yes" />
</Component>
```

Hoặc, bạn có thể trong `Feature`:

```xml
<Feature Id="FeatureModuleX" Title="Module X" Level="0">
  <Condition Level="1">INSTALL_MODULE_X = "1"</Condition>
  <ComponentRef Id="cmpModuleX" />
</Feature>
```

Khi người dùng tick checkbox trong wizard, property `INSTALL_MODULE_X` sẽ được thiết lập (ví dụ đoạn trong UI control `Publish` hoặc binding). Khi build MSI, nếu property = 1 thì component được cài, nếu = 0 thì bỏ qua.

### 3.3 Giao diện UI đẹp & đa bước

Bạn có thể kế thừa các UI chuẩn của WiX (WixUI_InstallDir, WixUI_FeatureTree, WixUI_Mondo, v.v.) rồi chèn dialog tùy chỉnh, hoặc viết hẳn UI riêng. Tuy nhiên, viết UI từ đầu là khá tốn công, nên thường bạn kế thừa + mở rộng.

> **Lưu ý:** UI trình bày (dialog) chỉ thực thi trong giai đoạn _UI sequence_. Trong _execute sequence_ (deferred), bạn không thể truy cập public properties (ngoại trừ thông qua `CustomActionData`). Do đó, nếu bạn có custom action cần biết giá trị input người dùng, bạn cần truyền dữ liệu qua `CustomActionData`.

Ví dụ trong custom action:

```xml
<CustomAction Id="DoSomething" Execute="deferred" Property="DoSomething" Value="MODULE_X=[INSTALL_MODULE_X]" />
<CustomAction Id="RollbackDoSomething" Execute="rollback" Property="RollbackDoSomething" Value="MODULE_X=[INSTALL_MODULE_X]" />
```

Trong C# (DTF):

```csharp
[CustomAction]
public static ActionResult DoSomething(Session session)
{
    string moduleX = session.CustomActionData["MODULE_X"];
    // code thực hiện nếu moduleX = 1
    return ActionResult.Success;
}
```

---

## 4. Cơ chế rollback & xử lý lỗi

Rollback là phần thường bị bỏ sót trong các hướng dẫn cơ bản nhưng rất quan trọng nếu quá trình cài đặt gặp lỗi (thiếu file, quyền, lỗi mạng, hủy cài). Nếu không có rollback, hệ thống có thể bị “một nửa cài”.

### 4.1 Nguyên tắc rollback trong WiX / MSI

- Các `deferred` custom action (những action thay đổi hệ thống) nên có tương ứng `rollback` action để đảo ngược nếu lỗi xảy ra. [O'Reilly Media+2Docs+2](https://www.oreilly.com/library/view/wix-3-6-a/9781782160427/ch05s04.html?utm_source=chatgpt.com)
    
- `rollback` custom action phải được định nghĩa _trước_ custom action mà nó rollback (theo thứ tự sequence). [Medium+2Packt+2](https://thehenrytsai.medium.com/uninstall-vs-rollback-custom-action-in-wix-beed702d45c1?utm_source=chatgpt.com)
    
- Chỉ những action nằm giữa `InstallInitialize` và `InstallFinalize` mới được rollback; sau `InstallFinalize` là quá muộn để rollback. [Stack Overflow+2Medium+2](https://stackoverflow.com/questions/22583822/wix-installer-rollback-custom-action-for-a-custom-action-sequenced-after-instal?utm_source=chatgpt.com)
    
- Khi custom action bị lỗi (return lỗi) hoặc người dùng hủy, hệ thống sẽ chạy rollback actions theo thứ tự ngược lại so với định nghĩa. [Packt+1](https://subscription.packtpub.com/book/cloud-and-networking/9781849513722/5/ch05lvl1sec36/rollback-custom-actions?utm_source=chatgpt.com)
    

### 4.2 Cách định nghĩa rollback + deferred custom actions

Ví dụ trong `CustomActions.wxs`:

```xml
<Fragment>
  <Binary Id="MyCA" SourceFile="CustomActionsBin\MyCA.dll" />

  <CustomAction Id="DoWork" BinaryKey="MyCA" DllEntry="DoWork" Execute="deferred" Return="check"/>
  <!-- Rollback action đặt trước -->
  <CustomAction Id="Rollback_DoWork" BinaryKey="MyCA" DllEntry="RollbackDoWork" Execute="rollback" Return="ignore"/>

  <InstallExecuteSequence>
    <!-- Đăng ký rollback trước, rồi action thực tế -->
    <Custom Action="Rollback_DoWork" Before="DoWork">NOT Installed</Custom>
    <Custom Action="DoWork" After="InstallFiles">INSTALL_MODULE_X = "1"</Custom>
  </InstallExecuteSequence>
</Fragment>
```

- `Rollback_DoWork` sẽ được ghi lại để chạy nếu lỗi xảy ra sau `DoWork`.
    
- `CustomActionData` có thể truyền dữ liệu vào cả hai action.
    
- Trong code C#, bạn viết hai hàm `DoWork` và `RollbackDoWork`.
    

Nếu `DoWork` gặp lỗi, `Rollback_DoWork` được thực thi để phục hồi. Lưu ý: rollback không thể thực thi nếu custom action nằm ngoài vùng cho phép.

### 4.3 Xử lý tình huống người hủy cài đặt

Khi người dùng nhấn “Cancel” trong wizard, hệ thống sẽ tự động bắt lỗi và khởi động rollback. Bạn không cần viết riêng cho nút Cancel; chỉ cần đảm bảo các action chính có rollback tương ứng.

### 4.4 Lỗi runtime trong custom action

- Nên ghi log (session.Log) chi tiết để dễ debug.
    
- Nếu custom action phát sinh exception không bắt, sẽ khiến MSI thất bại — bạn nên catch ngoại lệ và trả về lỗi có kiểm soát.
    
- Trong custom action, bạn nên kiểm tra giá trị property trước khi thực thi, nếu dữ liệu không hợp lệ thì dừng action và trả lỗi.
    

---

## 5. Hỗ trợ nâng cấp / patch / uninstall

Một installer tốt cần hỗ trợ việc **nâng cấp phiên bản mới** (major upgrade, minor upgrade) và **gỡ sạch** (uninstall clean). Mình sẽ hướng dẫn các bước cần thiết.

### 5.1 Thiết lập `UpgradeCode` & giữ nó cố định

`UpgradeCode` là định danh của dòng sản phẩm và phải giữ cố định giữa version để MSI nhận biết có thể nâng cấp. Nếu `UpgradeCode` thay đổi, hệ thống sẽ coi như sản phẩm khác hẳn.

### 5.2 Tạo phần nâng cấp (Major Upgrade)

Trong `Upgrade.wxs`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<Wix xmlns="http://wixtoolset.org/schemas/v4/wxs">
  <Fragment>
    <MajorUpgrade
      AllowSameVersionUpgrades="no"
      DowngradeErrorMessage="A newer version is already installed."
      Schedule="afterInstallInitialize"
      />
  </Fragment>
</Wix>
```

- `Schedule="afterInstallInitialize"` cho phép loại bỏ phiên bản cũ trước khi cài mới.
    
- Bạn có thể tùy chỉnh các phần điều kiện.
    
- Với major upgrade, các component mới / cũ được thay thế, bỏ dần file cũ nếu không còn dùng.
    

### 5.3 Minor Upgrade / Patch

Patch và minor upgrade phức tạp hơn, thường yêu cầu tạo `.msp` (patch) và định nghĩa transform. Bài viết này có thể đề cập sơ lược:

- Minor upgrade: thay đổi version major phần phụ, giữ cấu trúc component ổn định
    
- Patch (.msp): tạo bản vá nhỏ, bản gói chênh lệch
    
- cần dùng `Patch` element và `ComponentRules` cẩn trọng
    

Để bài viết không quá dài, bạn có thể đề cập như phần “nâng cao”: nếu cần patch/minor, nên tham khảo tài liệu WiX / Microsoft về patch. (Bài gốc không đề cập.)

### 5.4 Uninstall / Remove / Clean-up

- Các `Component` nên định nghĩa `RemoveFolder` và `RegistryValue` (KeyPath) để tự gỡ file và registry.
    
- Gắn điều kiện vào các shortcut, folder removal khi uninstall.
    
- Nếu custom action cần dọn dẹp (ví dụ, file tạm, log), bạn có thể tạo custom action khi uninstall (Execute = deferred/uninstall) để làm việc này.
    

---

## 6. Bảo mật & kiểm tra quyền / điều kiện hệ thống

Phần này rất quan trọng để installer khi chạy thực tế không bị lỗi do quyền, thiếu điều kiện.

### 6.1 Kiểm tra quyền Admin / quyền chạy

- Nếu installer cần thay đổi vùng hệ thống (ví dụ: ghi vào `Program Files`, HKLM registry, cài service…), bạn nên yêu cầu quyền admin.
    
- Trong file `.wxs`, bạn có thể đặt `Package` attribute:
    

```xml
<Package InstallPrivileges="elevated" InstallScope="perMachine" />
```

- Kết hợp với `ShieldIcon` trên dialog “Install” để biểu thị rằng hành động cần quyền cao.
    
- Bạn có thể kiểm tra và cảnh báo nếu user không chạy ở quyền admin (kiểm tra `Privileged` property).
    

### 6.2 Kiểm tra điều kiện hệ thống (OS version, runtime, phụ thuộc)

Bạn có thể sử dụng `Condition` element để kiểm tra các điều kiện trước khi cài:

```xml
<Condition Message="Ứng dụng này yêu cầu Windows 10 trở lên.">
  VersionNT >= 1000
</Condition>
```

Hoặc kiểm tra .NET runtime:

- Dùng `PropertyRef` và `Condition` (với WiX .NET extension) để đảm bảo runtime phù hợp.
    
- Hoặc tạo custom action trước khi install chính để kiểm tra (immediate mode) và abort nếu không thỏa.
    

### 6.3 Bảo vệ gói cài đặt / ký số (Signature / Code Signing)

- Ký số cho file MSI (và EXE bootstrapper nếu có) để Windows không cảnh báo SmartScreen / User Account Control (UAC).
    
- Trong quá trình build, bạn có thể dùng `SignTool` hoặc công cụ ký số tích hợp MSBuild.
    
- Ký số đảm bảo integrity và tăng niềm tin cho người dùng khi tải từ Internet.
    

### 6.4 Tránh “DLL Hijacking” / thư viện độc hại

- Khi gọi custom action hoặc thư viện bên ngoài, đảm bảo đường dẫn rõ ràng (không dùng thư mục hiện hành).
    
- Nếu có dùng `WixUtilExtension` hoặc extension khác, đảm bảo bạn kiểm tra variables, không để lỗ.
    

---

## 7. Kiểm thử đa môi trường

Một phần quan trọng để chắc rằng installer hoạt động ổn định trên môi trường thực tế:

### 7.1 Kiểm thử trên các phiên bản Windows

Thử trên: Windows 7 (nếu bạn vẫn hỗ trợ), Windows 10, Windows 11, Windows Server, phiên bản 32-bit & 64-bit.  
Kiểm xem installer:

- có yêu cầu quyền?
    
- có chạy được khi user không phải admin?
    
- có rơi lỗi khi máy chưa cài .NET runtime?
    
- uninstall có sạch?
    
- upgrade từ version cũ có đúng?
    
- rollback khi lỗi giữa chừng?
    

### 7.2 Kiểm thử các kịch bản đặc biệt

- Người dùng nhấn Cancel ở giữa cài đặt → rollback phải hoàn chỉnh
    
- Lỗi trong custom action → rollback đúng
    
- Máy đang chạy ứng dụng (file locked) → installer xử lý thế nào (thông báo, yêu cầu đóng app, reboot)
    
- Phân quyền thấp (user không admin)
    
- Mạng yếu (nếu installer tải file ngoài)
    
- Trường hợp cập nhật (nâng cấp)
    
- Patch nhỏ (nếu bạn hỗ trợ)
    
- Kiểm thử trên máy ảo / sandbox để kiểm tra không ảnh hưởng ngoài ý muốn
    

### 7.3 Logging & debug

- Tích hợp logging verbose (`msiexec /i MyApp.msi /l*v install.log`) để ghi lại chi tiết quá trình cài đặt
    
- Trong custom action, ghi log chi tiết (`session.Log(...)`) để dễ trace lỗi
    
- Cho phép người dùng bật chế độ debug / log thêm nếu cần
    

---

## 8. Mở rộng cho ứng dụng Win32, service, app không .NET

Bài gốc tập trung vào ứng dụng WPF (.NET). Dưới đây cách mở rộng sang các loại khác.

### 8.1 Ứng dụng Win32 truyền thống

- Thay `File Source="$(var.MyApp.TargetPath)"` bằng đường dẫn đến `.exe` hoặc `.dll` Win32
    
- Không cần .NET runtime — bạn không kiểm tra runtime .NET
    
- Shortcut, registry, component giống như ví dụ
    
- Nếu ứng dụng cần thư viện phụ (DLL), cài cùng thư mục
    
- Nếu ứng dụng có driver hoặc COM, bạn có thể dùng custom action để register / unregister
    

### 8.2 Ứng dụng dạng dịch vụ (Windows Service)

- Trong `.wxs`, sử dụng element `<ServiceInstall>` và `<ServiceControl>` (của `WixUtilExtension`) để định nghĩa cài, start, stop service.
    

Ví dụ:

```xml
<Component Id="ServiceComponent" Guid="PUT-GUID">
  <File Source="$(var.ServiceExePath)" KeyPath="yes" />
  <ServiceInstall Id="MyService"
                  Type="ownProcess"
                  Name="MyServiceName"
                  DisplayName="My Service"
                  Start="auto"
                  ErrorControl="normal" />
  <ServiceControl Id="MyServiceControl"
                  Stop="uninstall"
                  Remove="uninstall"
                  Name="MyServiceName"
                  Wait="yes" />
</Component>
```

- Kèm điều kiện quyền admin để cài service
    
- Trong custom action (nếu cần), bạn có thể config service recovery, account, dependencies.
    

### 8.3 Ứng dụng không dùng .NET (C/C++, Python, Rust…)

- Cách đóng gói bản thân giống như Win32
    
- Nếu ứng dụng cần runtime (ví dụ Python), bạn có thể gói runtime kèm hoặc yêu cầu người dùng cài Python trước (kiểm tra trong `Condition`)
    
- Nếu ứng dụng có script hoặc thư viện native, bạn có thể dùng custom action hoặc extension để xử lý cài đặt phụ
    

---

## 9. So sánh các phương pháp đóng gói phổ biến & lý do chọn WiX / MSI

|Phương pháp / công cụ|Ưu điểm|Nhược điểm|Khi nên dùng|
|---|---|---|---|
|**WiX / MSI (hướng dẫn trong bài này)**|Chuẩn Microsoft, quản lý nâng cấp/uninstall/patch tốt; hỗ trợ kiểm soát chi tiết, rollback; phù hợp cho môi trường doanh nghiệp|Học khá nhiều; viết UI / custom action phức tạp; đôi khi verbose|Khi bạn muốn tạo installer mạnh mẽ, dễ bảo trì, được sử dụng lâu dài|
|**Inno Setup**|Gọn nhẹ, dễ học, cộng đồng lớn|Hạn chế trong patching, không chuẩn MSI, khó tích hợp quản lý doanh nghiệp|Dự án nhỏ, ứng dụng nhẹ, không cần tính năng nâng cao|
|**NSIS**|Script mạnh, plugin đa dạng|Cần viết script, khó với người mới, quản lý upgrade phức tạp nếu dự án lớn|Khi bạn muốn trình cài đặt nhẹ, dễ tuỳ chỉnh UI, không cần MSI chuẩn|
|**MSIX / APPX**|Hiện đại, hỗ trợ cập nhật, bảo mật tốt, hỗ trợ Windows Store / sideload|Yêu cầu Windows 10+, có thể khó với các ứng dụng legacy; đôi khi cần port|Khi bạn bắt đầu mới, muốn dùng công nghệ mới, muốn cập nhật dễ dàng|
|**Công cụ thương mại (InstallShield, Advanced Installer, InstallAware, PACE, …)**|Giao diện dễ dùng, hỗ trợ nhiều tính năng, tích hợp CI/CD, hỗ trợ người dùng doanh nghiệp|Chi phí; đôi khi “đóng hộp” khiến bạn ít kiểm soát|Dự án lớn, công ty có ngân sách, cần UI đẹp, localization, báo cáo, phân phối chuyên nghiệp|

**Vì sao trong bài này mình chọn WiX / MSI làm trung tâm:**

- WiX / MSI là phương pháp “chuẩn” của hệ sinh thái Windows, khả năng mở rộng & tương thích cao
    
- Cho phép bạn kiểm soát chi tiết (component, registry, custom action, rollback, upgrade)
    
- Nếu bạn viết hướng dẫn cho dev hoặc dự án thực tế, kiến thức WiX có giá trị lâu dài
    
- Hơn nữa, bạn có thể kết hợp WiX + bootstrapper (Burn) hoặc gói MSI trong MSIX nếu muốn mở rộng
    

Trong bài viết này, mình hướng dẫn từ WiX v4 — phiên bản mới — để bạn có nền tảng hiện đại, dễ mở rộng.

---

## 10. Hướng dẫn sử dụng **repo mã mẫu** đi kèm

Mình sẽ dựng một repo mẫu hoàn chỉnh để bạn clone & thực hành ngay theo bài viết:

### Cấu trúc repo mẫu (ví dụ: `wix-installer-sample`)

```xml
wix-installer-sample/
  /App/                      ← mã ứng dụng (có thể là WPF / Win32 / service)
    App.sln
    App/
      App.csproj / App.exe / mã nguồn
  /Installer/
    Installer.wixproj
    /WxsIncludes/
      Folders.wxs
      Components.wxs
      Shortcuts.wxs
      UI.wxs
      Upgrade.wxs
      CustomActions.wxs
    /CustomActionsBin/
      MyCA.dll  (project source custom action)
    build.cmd
    build.ps1
  README.md
```

### Nội dung README mẫu (gợi ý)

```markdown
# Wix Installer Sample

## Mô tả
Repo này chứa mã mẫu cho bài hướng dẫn “Tạo Installer Windows bằng WiX v4” (phiên bản tiếng Việt).  
Ứng dụng demo có thể là WPF / console / Win32 / service (tùy bạn chọn).  
Installer hỗ trợ: UI wizard tùy chỉnh, input người dùng, rollback, upgrade/uninstall, kiểm tra quyền & điều kiện.

## Cách chạy

1. Mở solution `App.sln`, build ứng dụng → tạo file exe / dll  
2. Chuyển sang folder `Installer/`, chạy `build.cmd` hoặc `build.ps1`  
3. Kết quả là file `.msi` trong thư mục `bin\Release`  
4. Chạy installer để cài thử; thử uninstall, upgrade…  
5. Mở `install.log` để xem log chi tiết

## Mã custom action (nếu có)
`CustomActionsBin/MyCA.dll` chứa mã C# (DTF) dùng cho custom actions.  
Hãy xem file `CustomActions.wxs` để biết cách liên kết.

## Lưu ý khi sử dụng
- Bạn cần Visual Studio + WiX v4 + .NET SDK  
- Nếu bạn dùng custom action, hãy build nó trước khi chạy installer  
- Bạn có thể tùy chỉnh GUID, tên application, path, UI theo nhu cầu  
```

### Các file chi tiết mẫu

- **CustomActions.wxs**: định nghĩa các custom action + rollback + sequence
    
- **UI.wxs**: dialog wizard nhập thư mục / input
    
- **Upgrade.wxs**: major upgrade cấu hình
    
- **Components.wxs**: định nghĩa các component với điều kiện property
    
- **Folders.wxs**: cấu trúc thư mục
    
- **Shortcuts.wxs**: shortcut desktop / start menu
    
- **build.cmd / build.ps1**: script tự động build cả ứng dụng + installer (ví dụ gọi `msbuild App.sln /p:Configuration=Release` rồi `msbuild Installer.wixproj /p:Configuration=Release`)
    

Mình có thể gửi repo mẫu cụ thể (code đầy đủ) nếu bạn muốn — bạn muốn mình tạo repo GitHub mẫu rồi gửi link không?

---

## 11. Kết luận & lời khuyên thực tế

- Việc tạo installer **chuyên nghiệp** đòi hỏi không chỉ “đúng cú pháp WiX” mà còn **xử lý rollback, nâng cấp, UI tuỳ chỉnh, kiểm tra quyền, bảo mật, kiểm thử kỹ càng**.
    
- Bắt đầu từ mẫu đơn giản, làm cho nó chạy ổn, rồi mở rộng thêm từng phần (UI, custom actions, upgrade).
    
- Mỗi phần bạn thêm vào (ví dụ custom action, dialog wizard) nên có rollback tương ứng, và kiểm thử kỹ càng.
    
- Ghi log đầy đủ: khi người dùng cài, nó giúp bạn debug nếu gặp lỗi.
    
- Không bỏ qua phần **ký số** và **kiểm tra quyền** — nếu người dùng cuối gặp cảnh báo hoặc lỗi quyền, họ có thể bỏ ngang.
    
- Kiểm thử trong nhiều môi trường (phiên bản Windows, quyền user, hủy cài giữa chừng) để chắc rằng installer bạn viết bền vững.
    
- Cung cấp mã mẫu sạch, dễ clone & chạy để người đọc có thể “làm theo và thành công” — đó là cách bạn tăng khả năng **chuyển hóa** (người đọc áp dụng thực tế).

# hướng dẫn source code

Mình không thể tạo repo GitHub trực tiếp từ đây, nhưng mình có thể **hướng dẫn chi tiết** cách bạn xây dựng repo đó dựa trên mã mẫu và hướng dẫn đã được trình bày. Bạn có thể làm theo các bước sau để tạo và cấu hình repo trên GitHub của mình:

---

### 🛠️ **Cách tạo GitHub repo mẫu**

1. **Tạo GitHub Repo**:
    
    - Đăng nhập vào [GitHub](https://github.com/) và tạo một repository mới. Đặt tên cho repo, ví dụ `wix-installer-sample`.
        
2. **Clone mã nguồn từ ví dụ vào máy của bạn**:
    
    - Nếu bạn muốn repo mẫu giống như những gì mình hướng dẫn trong bài, bạn có thể tạo cấu trúc thư mục theo ví dụ:
        
    
 ```
 wix-installer-sample/
  /App/
    App.sln
    App/
      App.csproj / App.exe / mã nguồn
  /Installer/
    Installer.wixproj
    /WxsIncludes/
      Folders.wxs
      Components.wxs
      Shortcuts.wxs
      UI.wxs
      Upgrade.wxs
      CustomActions.wxs
    /CustomActionsBin/
      MyCA.dll  (project source custom action)
    build.cmd
    build.ps1
README.md
 ```
    
3. **Tạo các file mẫu**:
    
    - Tạo các file `.wxs` như `Folders.wxs`, `Components.wxs`, `Shortcuts.wxs`, v.v. để mô phỏng quá trình cài đặt mà mình đã giải thích trong bài.
        
    - Viết các đoạn mã `custom actions`, `rollback`, `upgrade` theo cấu trúc WiX và các ví dụ đã cung cấp.
        
    - Tạo file `build.cmd` hoặc `build.ps1` để tự động hóa quá trình build và chạy MSI.
        
4. **Đẩy lên GitHub**:
    
    - Sau khi đã chuẩn bị đầy đủ mã nguồn và các file cấu hình, bạn có thể **commit** và **push** mã lên repo GitHub của mình.
        
    - Cung cấp một `README.md` chi tiết để người dùng hiểu cách sử dụng repo và thực hành theo.
        
5. **Chia sẻ link repo**:
    
    - Sau khi hoàn thành, bạn có thể chia sẻ **link GitHub repo** của mình với người khác hoặc sử dụng repo này như một tài liệu học tập.