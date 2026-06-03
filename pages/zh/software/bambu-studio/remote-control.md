---
path: zh/software/bambu-studio/remote-control
title: "远程控制和监控打印机"
description: ""
tags: []
created: 2023-03-14T13:35:46.648Z
updated: 2026-03-03T07:57:27.498Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/remote-control
---

Bambu Studio 支持通过网络（WAN/LAN）对打印机进行全方位的远程控制和监控。主要功能包括：

## 功能介绍

**远程打印**：通过 Wi-Fi 将打印任务发送到已连接的打印机。

**打印作业监控**：显示当前打印作业的进度，可启动、停止或暂停当前打印作业。

**摄像头实时画面**：查看摄像头实时画面，直观监控打印机状态。

**打印机控制**：控制热床温度、喷嘴温度、打印速度、风扇开关，移动打印头（XYZE），校准打印机并调整 AMS 设置。

**设备固件更新**：通过网络更新打印机和 AMS 的固件。

**两种网络模式**：可在自动模式（根据需要使用 WAN 和 LAN）和仅局域网模式之间切换。

## 准备工作

### 安装网络插件

Bambu Network Plugin 是 Bambu Studio 远程控制和监控功能的必要插件。如果未安装，将无法通过网络发送打印作业，且“设备”页面不可用。

若尝试在未绑定打印机的情况下选择“设备”标签页，会提示您安装所需插件。

![安装网络插件.gif](https://wiki.bambulab.com/software/bambu-studio/remote-control/%E5%AE%89%E8%A3%85%E7%BD%91%E7%BB%9C%E6%8F%92%E4%BB%B6.gif)

### 注册/登录

要绑定打印机进行远程控制，首先需要在 Bambu Studio 首页使用“登录/注册”按钮。

![](https://wiki.bambulab.com/software/bambu-studio/remote-control/login-register_button.png)

### 绑定打印机

如果账户尚未绑定打印机，可按照[本文](../../../en/knowledge-sharing/printer-account-binding-guide.md)进行绑定。以下以 P1S 打印机为例。

在设置菜单中选择 **未登录**。

![未登录.jpg](https://wiki.bambulab.com/software/bambu-studio/remote-control/%E6%9C%AA%E7%99%BB%E5%BD%95.jpg)

确保所选区域正确。生成 PIN 码后，请记录下来。注意：务必使用自己打印机上显示的 PIN 码，而非示意图中的。

![pin码.jpg](https://wiki.bambulab.com/software/bambu-studio/remote-control/pin%E7%A0%81.jpg)

在 Bambu Studio 中选择“设备”标签页的 **无打印机**，再选择 **通过Pin码绑定** 并输入 PIN 码。

![pin连接.gif](https://wiki.bambulab.com/software/bambu-studio/remote-control/pin%E8%BF%9E%E6%8E%A5.gif)

返回打印机屏幕，显示 **绑定** 和 **拒绝** 选项。确认显示的用户名与 Bambu Studio 登录的用户名一致后，选择 **绑定**。

![](https://wiki.bambulab.com/bambu-studio/manual/pin-code/printer-bind-cn.png)

屏幕将显示账户已登录的确认信息。

![退出登录1.png](https://wiki.bambulab.com/software/bambu-studio/remote-control/%E9%80%80%E5%87%BA%E7%99%BB%E5%BD%951.png)

在 Bambu Studio 中关闭“通过Pin码绑定”窗口，再次选择 **无打印机**。此时刚绑定的打印机名称会显示，选择它，打印机即可连接。

![设备状态.gif](https://wiki.bambulab.com/software/bambu-studio/remote-control/%E8%AE%BE%E5%A4%87%E7%8A%B6%E6%80%81.gif)

同一账户可绑定多台打印机，绑定后均可在列表中选择。

## 主要功能介绍

### 远程打印

切片完成后，可使用 Bambu Studio 将文件无线发送到绑定的打印机。

注意：多色打印的设置与发送方法（AMS 安装情况下）请参考[多色打印](multi-color-printing.md)文章。

单色打印作业切片完成后，可在下拉列表中选择绑定的打印机并确认发送。

![切片打印.gif](https://wiki.bambulab.com/software/bambu-studio/remote-control/%E5%88%87%E7%89%87%E6%89%93%E5%8D%B0.gif)

### 打印作业控制

打印机运行时，可在底部查看进度。

![打印过程.gif](https://wiki.bambulab.com/software/bambu-studio/remote-control/%E6%89%93%E5%8D%B0%E8%BF%87%E7%A8%8B.gif)

可使用进度条旁的按钮暂停（或停止）并恢复打印作业。

![打印暂停.jpg](https://wiki.bambulab.com/software/bambu-studio/remote-control/%E6%89%93%E5%8D%B0%E6%9A%82%E5%81%9C.jpg)

### 摄像头实时画面

若摄像头未开启，可使用左下角按钮打开。打印机关闭、未连接 Wi-Fi 或下载打印文件时无法显示画面。

![视频打开.gif](https://wiki.bambulab.com/software/bambu-studio/remote-control/%E8%A7%86%E9%A2%91%E6%89%93%E5%BC%80.gif)

### 打印机控制

选择打印机后，可在“设备”页面右侧的控制面板操作以下功能：

![控制面板1.png](https://wiki.bambulab.com/software/bambu-studio/remote-control/%E6%8E%A7%E5%88%B6%E9%9D%A2%E6%9D%BF1.png)

1. X/Y/Z/E 移动
2. 喷嘴温度
3. 热床温度
4. 腔温（视打印机型号而定）
5. 风扇速度控制
6. 打印速度（打印中可调整）
7. 灯光

![调整.gif](https://wiki.bambulab.com/software/bambu-studio/remote-control/%E8%B0%83%E6%95%B4.gif)

点击 **打印选项** 可设置部分打印选项（可用选项依打印机型号而定）：

- **AI 打印监控**（仅 H2D/X1C 系列）— 当监测在打印过程中可能出现[“炒面”现象（耗材缠绕）](../../knowledge-sharing/Spaghetti_detection.md)或废料槽耗材堆积时，会暂停打印以防止问题发生。
- **首层检测**（仅 H2D/X1C 系列）— 打印机检查首层质量并提示异常
- **自动从丢步中恢复** — 当打印头运动受阻时，打印机会重新回零后继续打印

![打印选项.gif](https://wiki.bambulab.com/software/bambu-studio/remote-control/%E6%89%93%E5%8D%B0%E9%80%89%E9%A1%B9.gif)

点击 **校准** 可在非打印状态下启动打印机校准。

![校准.gif](https://wiki.bambulab.com/software/bambu-studio/remote-control/%E6%A0%A1%E5%87%86.gif)

若打印机安装 AMS，将显示 AMS 耗材信息，可手动添加非 RFID（非 Bambu Lab）耗材信息，进料/退料 AMS 耗材至喷嘴，并调整 AMS 设置。

![更改耗材信息.gif](https://wiki.bambulab.com/software/bambu-studio/remote-control/%E6%9B%B4%E6%94%B9%E8%80%97%E6%9D%90%E4%BF%A1%E6%81%AF.gif)

### 两种网络模式

Bambu Studio 支持两种网络模式：

**自动模式**：通过互联网和局域网与打印机通信，打印文件将上传至云端，由打印机从远程下载。同时支持通过 Bambu Handy 打印历史列表重新打印。所有信息和文件仅对发送打印任务的用户可见。默认情况下，打印文件会在第一次打印 90 天后自动删除。用户可通过 Bambu Handy App 的打印历史逐个删除，或在 App 设置中启用“隐私打印”自动删除所有新文件。

**仅局域网模式**：仅通过局域网与打印机通信，打印信息和文件不会上传至云端。适用于对打印内容高度保密的场景。  
了解更多：[如何在Bambu Lab打印机上使用局域网模式](../../knowledge-sharing/enable-lan-mode.md)

打印机默认处于自动模式，可在打印机“网络设置”中开启“仅局域网”选项。详细操作请参阅[如何在Bambu Lab打印机上使用局域网模式](../../knowledge-sharing/enable-lan-mode.md)。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)；点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
