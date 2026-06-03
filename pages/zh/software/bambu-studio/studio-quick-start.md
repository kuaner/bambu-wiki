---
path: zh/software/bambu-studio/studio-quick-start
title: "Bambu Studio 快速上手教程"
description: "这篇文章简要介绍了Bambu Studio，并提供了一份指南，帮助您快速安装、设置、切片，并立即开始打印。"
tags: ["bambu studio"]
created: 2023-03-23T09:00:57.080Z
updated: 2026-05-08T12:03:14.777Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/studio-quick-start
---

## 什么是 Bambu Studio?

**Bambu Studio** 基于 Prusa Research 的 PrusaSlicer，而 PrusaSlicer 来源于 Alessandro Ranellucci 和 RepRap 社区的 Slic3r。Bambu Studio 是 Bambu Lab 开发的切片软件，具有专为拓竹 3D 打印机开发的自定义功能，包含了基于项目的流程、系统性优化的切片算法和易于操作的图形界面，期望为您带来流畅的打印体验。

![](https://wiki.bambulab.com/software/bambu-studio/quick-start/studio_cn.png)

## 系统要求

- Windows 10 或更高版本- Mac OS X v10.15 或更高版本
- Linux Ubuntu 20.02及以上/Fedora 36及以上(Linux 版本需要从 [github](https://github.com/bambulab/BambuStudio/releases)下载)
- Intel® Core 2 或 AMD Athlon® 64 处理器；2 GHz 或更快的处理器
- 支持 OpenGL 2.0 的系统
- 推荐 8GB RAM，至少 4GB- 2.0 GB 或更多可用硬盘空间

## 下载和安装

- 下载 [Bambu Studio](https://bambulab.com/en/download)
- 按照分步指南安装 Bambu Studio

## 安装向导

### 选择登录地区设置登录区域为 **“中国内地（大陆）”**

![](https://wiki.bambulab.com/software/bambu-studio/quick-start/%E7%99%BB%E5%BD%95%E5%8C%BA%E5%9F%9F-cn.jpeg)

### 打印机选择

选择您希望在切片操作菜单中显示的打印机或喷嘴选项，可选择任何或所有可用选项。

如果您在此阶段只选择一个喷嘴尺寸，可在稍后阶段通过切片器菜单调整这些选项。

![选择打印机-.png](https://wiki.bambulab.com/quick-start-guide/%E9%80%89%E6%8B%A9%E6%89%93%E5%8D%B0%E6%9C%BA-.png)

### 材料选择

选择您希望在材料预设列表中列出的材料，可选择尽可能多的材料。

![选材料.jpeg](https://wiki.bambulab.com/software/bambu-studio/quick-start/%E9%80%89%E6%9D%90%E6%96%99.jpeg)

### 安装 Bambu 网络插件

Bambu Network 插件提供网络功能，例如通过 WAN/LAN 打印、远程控制、用户数据同步。

插件安装需要 Internet 连接，并且将在安装向导后自动安装（如果启用）。

![安装网络插件.jpeg](https://wiki.bambulab.com/software/bambu-studio/quick-start/%E5%AE%89%E8%A3%85%E7%BD%91%E7%BB%9C%E6%8F%92%E4%BB%B6.jpeg)

## 首次打印

### 登录您的账户（可选，但强烈推荐）

**您需要安装 Bambu 网络插件才能登录**。 这是启用打印历史记录的必要步骤，它允许您在 Bambu Handy 应用程序中重新打印历史模型。

此外，您的用户设置将同步到 Bambu Cloud，从而在不同的 PC 设备之间共享信息。

![登录.png](https://wiki.bambulab.com/software/bambu-studio/quick-start/%E7%99%BB%E5%BD%95.png)

> 注意：由于打印机和 Studio 不能定时刷新调用接口，因此当用户修改昵称后，需要解绑打印机并重新绑定，Studio 也需要退出重新登录，才会展示最新的昵称。

> 注意：如果显示使用邮箱地址登录 Bambu Studio，可在屏幕左上角点击：**下拉箭头 > 偏好设置 > 登录区域 > 选择“中国内地（大陆）”**，即可使用手机号登录 Bambu Studio。  
> ![偏好设置.png](https://wiki.bambulab.com/software/bambu-studio/quick-start/%E5%81%8F%E5%A5%BD%E8%AE%BE%E7%BD%AE.png)  
> ![登录区域.png](https://wiki.bambulab.com/software/bambu-studio/quick-start/%E7%99%BB%E5%BD%95%E5%8C%BA%E5%9F%9F.png)

### 打印机绑定

在发起打印任务之前，首先您需要完成 Bambu Studio 和打印设备的绑定，这样才能进行设备状态的查看、任务的远程发起与控制。您可以通过 Bambu Handy 移动应用 或 Bambu Studio 桌面客户端 完成打印机的绑定操作。

1. [**Bambu Handy**](https://bambulab.cn/zh-cn/download/app)  
   打开 APP 找到底部标签栏中的“设备”，点击“绑定打印机”。  
   ![1280x1280.jpeg](https://wiki.bambulab.com/software/bambu-studio/quick-start/1280x1280.jpeg)  
   完成打印机的绑定后，在 Bambu Studio 登录相同账户，即可同步设备列表。推荐优先使用 Bambu Handy 绑定，支持所有 Bambu 系列打印机。
2. **Bambu Studio**  
   若选择通过 Bambu Studio 完成绑定操作。具体有两种方式可供选择：

- 通过 Pin code 进行绑定（仅限 P 系列 / A 系列）。
- 使用 IP 地址和访问码来绑定打印机（需要打印机在局域网模式下使用，适合数据隔离或无外网环境。）。

![1280x1280.png](https://wiki.bambulab.com/software/bambu-studio/quick-start/1280x1280.png)

> 绑定详细步骤您可以参考以下 wiki:
>
> 1. [Bambu Studio 中使用 Pin 码绑定打印机](../../bambu-studio/manual/pin-code.md)
> 2. [Bambu Lab 打印机上使用局域网模式](../../knowledge-sharing/enable-lan-mode.md)

### 创建新项目

点击主页**创建一个新项目**。

![创建新项目.jpeg](https://wiki.bambulab.com/software/bambu-studio/quick-start/%E5%88%9B%E5%BB%BA%E6%96%B0%E9%A1%B9%E7%9B%AE.jpeg)

### 添加模型

在预览窗格的顶部工具栏上，点击第一个图标**添加**，以导入模型；也可将文件夹中的模型文件拖入 Studio 中导入。支持的文件包括 .3mf .stl .stp .step .amf .obj 格式。

![添加模型.jpeg](https://wiki.bambulab.com/software/bambu-studio/quick-start/%E6%B7%BB%E5%8A%A0%E6%A8%A1%E5%9E%8B.jpeg)

### 选择打印机/耗材丝/工艺预设

在模型切片前，需要选择您想使用的打印机和耗材丝，并对打印模型进行相关设置。

1. 点击**打印机**选择框，在列表中选择要使用的机型及喷嘴尺寸
2. 点击**耗材丝**选择框，在列表中选择您要使用的耗材类型
3. 点击**工艺**选择框，在列表中选择模型的层高。**层高越小，打印时间越长。对于大多数用0.4 mm 喷嘴打印的模型来说，0.20 mm 的层高是合适的。**![准备.png](https://wiki.bambulab.com/software/bambu-studio/quick-start/%E5%87%86%E5%A4%87.png)

### 模型切片

- 设置完成后，点击屏幕右上角的**切片单盘**。

![切片单盘-cn.jpeg](https://wiki.bambulab.com/software/bambu-studio/quick-start/%E5%88%87%E7%89%87%E5%8D%95%E7%9B%98-cn.jpeg)

- 如模型文件包含多盘，可点击屏幕右上角的**切片所有盘**。

![切片所有盘-cn.png](https://wiki.bambulab.com/software/bambu-studio/quick-start/%E5%88%87%E7%89%87%E6%89%80%E6%9C%89%E7%9B%98-cn.png)

完成后，屏幕将显示 .3mf 文件模型切片后的外观，右侧直方图还将显示模型的颜色方案、耗材丝用量、打印时间等信息。

![预览信息.jpeg](https://wiki.bambulab.com/software/bambu-studio/quick-start/%E9%A2%84%E8%A7%88%E4%BF%A1%E6%81%AF.jpeg)

### 发送打印任务

#### 打印单盘

点击屏幕右上角的**打印单盘**，屏幕将弹出一个**发送打印任务**窗口。选择要发送的打印机，使用的耗材，以及打印机在打印开始前是否执行某些功能，如热床调平、流量校准等。选择完成后，点击**发送**，即可开始打印。  
![发送打印任务.png](https://wiki.bambulab.com/software/bambu-studio/quick-start/%E5%8F%91%E9%80%81%E6%89%93%E5%8D%B0%E4%BB%BB%E5%8A%A1.png)

##### 打印所有盘

请点击[多盘打印指南](../../studio-handy/multi-plate-printing.md)查看更多相关信息。

> 注意：您需要安装 Bambu 网络插件才能通过 WLAN 发送文件，且需确保 Bambu Studio 和打印机在同一个 LAN上。

#### 发送/发送所有盘

- 点击屏幕右上角**打印单盘**左侧的箭头，选择**发送**。

![发送单盘.jpeg](https://wiki.bambulab.com/software/bambu-studio/quick-start/%E5%8F%91%E9%80%81%E5%8D%95%E7%9B%98.jpeg)

- 如模型文件包含多盘，可点击屏幕右上角**打印单盘**左侧的箭头，选择**发送所有盘**。屏幕将弹出一个**发送到打印机的 SD 卡**窗口。选择要发送的打印机，即可将模型文件发送到该打印机的 SD 卡中，在打印机屏幕上开启打印（以 A1 系列为例）。

![发送所有盘.jpeg](https://wiki.bambulab.com/software/bambu-studio/quick-start/%E5%8F%91%E9%80%81%E6%89%80%E6%9C%89%E7%9B%98.jpeg)

> 注意： 需确保 Bambu Studio 和打印机在同一个 LAN 上。

#### 导出单盘/所有切片文件

- 将打印机 SD 卡从打印机中取出，并插入电脑中。点击屏幕右上角**打印单盘**左侧的箭头，选择**导出单盘切片文件**。

![导出单盘.jpeg](https://wiki.bambulab.com/software/bambu-studio/quick-start/%E5%AF%BC%E5%87%BA%E5%8D%95%E7%9B%98.jpeg)

- 如模型文件包含多盘，可点击屏幕右上角**打印单盘**左侧的箭头，选择**导出所有切片文件**。

![导出所有切片文件.jpeg](https://wiki.bambulab.com/software/bambu-studio/quick-start/%E5%AF%BC%E5%87%BA%E6%89%80%E6%9C%89%E5%88%87%E7%89%87%E6%96%87%E4%BB%B6.jpeg)

- 屏幕将弹出一个文件资源管理器窗口，选择 SD 卡，将文件保存至 SD 卡中。

![选择_sd_卡.jpeg](https://wiki.bambulab.com/software/bambu-studio/quick-start/%E9%80%89%E6%8B%A9_sd_%E5%8D%A1.jpeg)

保存后，取出 SD 卡并将其插入打印机中。点击打印机屏幕左侧菜单选项中的**主页**图标-**打印文件**，选择顶部菜单中的 **SD 卡**，点击刚刚导出的文件，即可开始打印。

![查看_sd_卡-cn.png](https://wiki.bambulab.com/software/bambu-studio/quick-start/%E6%9F%A5%E7%9C%8B_sd_%E5%8D%A1-cn.png)

> 各机型从 SD 卡开始打印的详情指南请参考：
>
> - [如何在 X1 系列 3D 打印机中使用 SD 卡进行打印](../../x1/manual/print-from-sd-card.md)
> - [如何在 P1 系列 3D 打印机中使用 SD 卡进行打印](../../p1/manual/how-to-print-from-sd-card.md)
> - [如何在 A1 系列 3D 打印机中使用 SD 卡进行打印](../../a1/manual/how-to-print-from-sd-card.md)

#### 发送到多设备

请点击[多设备管理](https://wiki.bambulab.com/zh/software/bambu-studio/multi-device-management#%E5%8F%91%E9%80%81%E4%B8%80%E4%B8%AA%E4%BB%BB%E5%8A%A1%E5%88%B0%E5%A4%9A%E4%B8%AA%E8%AE%BE%E5%A4%87)查看更多相关信息。

## 远程控制

选择 Studio 中的**设备**界面，可实时[远程控制和监视打印](remote-control.md)。如果您的打印机上安装了摄像头（X1C 标配），您还可以远程观看打印的实时画面。

> ***注意：您需要安装 Bambu 网络插件才能通过此过程访问机器***  
> ![远程控制.jpeg](https://wiki.bambulab.com/software/bambu-studio/quick-start/%E8%BF%9C%E7%A8%8B%E6%8E%A7%E5%88%B6.jpeg)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 我们希望能确保您安全有效地进行操作。如果您对本指南描述的过程有任何疑虑或问题，建议您在开始操作前联系我们友好的客户服务团队。  
> 我们随时准备为您解答疑问并提供帮助。[点击此处联系在线技术支持 （服务时间 9:00-21:00）](https://support.bambulab.cn/cn/im)
