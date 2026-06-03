---
path: zh/x1/manual/introduction-to-bambu-studio
title: "Bambu Studio简介 "
description: ""
tags: []
created: 2022-07-29T07:11:38.875Z
updated: 2024-09-18T13:31:06.125Z
source: https://wiki.bambulab.com/zh/x1/manual/introduction-to-bambu-studio
---

如果您正在阅读本文，那您可能是刚收到自己全新 Bambu Lab X1 3D 打印机，并打算进行打印文件的切片。 为了方便您的使用，我们准备了这份快速指南，帮助您完成 Bambu Studio 的设置并完成您的第一个打印文件切片。

### 什么是 Bambu Studio?

Bambu Studio 是Bambu Lab开发的切片软件，它功能丰富且易于使用，包含了基于项目的流程、系统性优化的切片算法和易于操作的图形界面，期望为您带来流畅打印体验。

![](https://wiki.bambulab.com/x1/manual/intro-bambu-studio/bambu_studio_interface.png)

Bambu Studio 基于 Prusa Slicer开发，具有专为 X1 和 X1C  3D 打印机开发的自定义功能。

### 什么是 Bambu Handy?

Bambu Handy 是由 Bambu Lab 开发的移动应用程序，适用于 iOS 和 Android，可让您远程访问所有的拓竹打印机。

![](https://wiki.bambulab.com/x1/manual/intro-bambu-studio/bambu_handy_app_controls.jpeg)

Handy可对打印机的运动进行完全控制，针对 X1C，它还提供实时视频以检查和监控您正在打印的模型。

## 安装 Bambu Studio 及 Bambu Handy

Bambu Studio 切片软件将不断开发新补丁和新功能，为确保您安装到最新版本，请通过以下链接下载软件：[Bambu Studio](https://bambulab.com/zh/download)

下载文件后，您可以通过双击安装文件并按照如下指引完成设置步骤。

![](https://wiki.bambulab.com/x1/manual/intro-bambu-studio/install_bambu_studio_on_windows.png)

如果您使用的是 MacOS，只需打开 .dmg 文件，将 Bambu Studio 应用程序复制到 Mac 的 Applications 文件夹。

![](https://wiki.bambulab.com/x1/manual/intro-bambu-studio/install_bambu_studio_on_mac.png)

## Bambu Studio 初始配置

安装 Bambu Studio 后，您将看到一个快速设置指南，帮助您完成初始设置过程。

请单击“开始”。

![](https://wiki.bambulab.com/x1/manual/intro-bambu-studio/introduction_to_bambu_studio1.png)

在如下页面中，系统将要求您选择您所在的地区。请注意：这一步非常重要。它将确保您能够访问到离您所在位置最近的服务器，以便获得最佳性能和最低延迟。

![](https://wiki.bambulab.com/x1/manual/intro-bambu-studio/introduction_to_bambu_studio2.png)

您可以匿名向我们发送切片软件中与打印设置相关的数据， 这将有助于我们改善用户体验和打印性能。

![](https://wiki.bambulab.com/x1/manual/intro-bambu-studio/introduction_to_bambu_studio3.png)

在下一个页面中，系统会要求您选择打印机和喷嘴类型。 X1 出厂配备了 0.4mm 喷嘴，可以使用默认设置。如果您购买并使用了其他尺寸的喷嘴，您需要在该界面选择相应值以保证配置正确。

![](https://wiki.bambulab.com/x1/manual/intro-bambu-studio/introduction_to_bambu_studio4.png)

最后，系统会要求您选择计划使用的线材。 我们建议勾选所有线材类型，这些线材类型最后会呈现在切片软件中供您选择使用。

![](https://wiki.bambulab.com/x1/manual/intro-bambu-studio/introduction_to_bambu_studio5.png)

## 创建一个 Bambu 账户

想要使用打印机的所有网络功能，您可以通过 Bambu Studio 或 Bambu Handy 将打印机连接到网络并将其绑定到您的 Bambu Lab 帐户。

首先，打开 Bambu Studio，然后点击 **登陆/注册** 按钮。

![](https://wiki.bambulab.com/x1/manual/intro-bambu-studio/login-register_button.png)

接下来，点击**创建您的帐户** 按钮。

![](https://wiki.bambulab.com/x1/manual/intro-bambu-studio/create_your_bambu_lab_account.png)

在注册页面输入您的邮箱地址，然后点击“发送验证码”按钮。 几秒钟后，您将在邮件中收到一个 6 位数的验证码。

最后，设置一个保密性高的密码，然后点击 **提交**。

![](https://wiki.bambulab.com/x1/manual/intro-bambu-studio/bambu_lab_account_creation.png)

现在，您可以登录您的 Bambu Studio 和 Bambu Handy App了。

## 绑定打印机到您的 Bambu 账户

有了 Bambu 账号，您可以通过Bambu Handy 将打印机绑定到该账号。

请打开 Bambu Handy App，并登录您的帐户。

![](https://wiki.bambulab.com/x1/manual/intro-bambu-studio/open_bambu_handy_app.png)![](https://wiki.bambulab.com/x1/manual/intro-bambu-studio/touch_the_+_button_in_bambu_handy_to_add_a_printer.png)

在添加打印机页面会显示已经连接到同一网络WiFi 的打印机。 您可以从列表中选择添加，也可以通过扫描打印机触摸屏上的二维码进行添加。

![](https://wiki.bambulab.com/x1/manual/intro-bambu-studio/scanning_new_printers_in_bambu_handy.png)

选择其中一台打印机或扫描二维码后，您的打印机将显示在 Bambu Handy 和 Bambu Studio 中。

![](https://wiki.bambulab.com/x1/manual/intro-bambu-studio/bambu_handy_app.png)![](https://wiki.bambulab.com/x1/manual/intro-bambu-studio/bambu_slicer_printer_controls.png)

## 通过 Bambu Studio 进行切片

切片您的第一个模型，您只需要将文件拖放到 Bambu Studio 中，然后按照以下步骤操作：

![](https://wiki.bambulab.com/x1/manual/intro-bambu-studio/steps_for_slicing_the_files.png)

1. **选择打印机类型**（比如，X1C）。
2. **选择热床类型**（低温热床、工程材料热床或高温热床）。
3. **选择线材类型（** 线料类型请选择安装在 AMS 第一个插槽上的线料类型）。
4. **选择切片设置**。
5. **点击”切片“生成打印文件**。

模型切片后，您可以选择单击"打印"并将文件发送到打印机，或导出切片文件到 SD 卡，通过SD 卡进行打印。

![](https://wiki.bambulab.com/x1/manual/intro-bambu-studio/export_or_print_the_sliced_file.png)

单击“print”后，您可以选择要使用的打印机，以及要在打印前执行的校准类型。

![](https://wiki.bambulab.com/x1/manual/intro-bambu-studio/send_print_job_to_printer.png)

点击"Send”, Bambu Studio会向打印机发送文件，开始打印。
