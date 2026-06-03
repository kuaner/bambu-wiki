---
path: zh/software/bambu-handy/troubleshoot/check-software-version
title: "检查 bambu handy 软件版本"
description: ""
tags: ["bambu handy"]
created: 2025-07-04T03:09:37.237Z
updated: 2025-07-25T08:55:04.999Z
source: https://wiki.bambulab.com/zh/software/bambu-handy/troubleshoot/check-software-version
---

了解应用程序的软件版本对于故障排查、确保与打印机固件的兼容性以及获取最新功能至关重要。本教程将为您提供在 Bambu Handy 应用中查看软件版本的操作步骤。

## 为什么需要了解版本号

您需要了解软件版本号，特别是在以下情况下：

1. **进行故障排查时：** 客服团队可能会要求提供应用版本号，以帮助诊断问题。
2. **打印机固件兼容性：** 如果遇到应用与 3D 打印机之间的连接或授权问题，可能是由于版本不兼容造成的。在更新了打印机固件后，请确保 Bambu Handy 应用也更新至最新版本，以保持兼容。
3. **获取新功能：** 新功能通常只在最新版本中提供。查看版本号可以帮助判断是否需要更新应用以启用这些功能。

## 所需准备

- **设备：** 运行 iOS（13.0 或更高版本）或 Android（6.0 或更高版本）的智能手机或平板。
- **Bambu Handy 应用：** 可通过 [官网](https://bambulab.cn/zh-cn/download/app) 或个人移动设备应用商店下载。
- **互联网连接：** 以便更新应用。
- **Bambu Lab 账户：** 您需要登录账户以获取完整设置权限。

## 如何查看版本号

### 第一步：打开 Bambu Handy 应用

在设备主屏幕或应用列表中找到应用图标并点击，请确保设备已连接互联网。如果您尚未设置账户，请参考 [Bambu Handy 快速入门指南](../../../studio-handy/handy/bambu-handy-quick-start.md)。

### 第二步：进入“我的”界面

打开应用后，点击底部导航栏右下角的人形图标 **我的**。  
![](https://wiki.bambulab.com/software/bambu-handy/check-software-version/%E6%88%91%E7%9A%84-portrait.png)

### 第三步：进入设置

在“我的”界面中，找到标有齿轮图标的 **设置** 项进入。  
![](https://wiki.bambulab.com/software/bambu-handy/check-software-version/%E8%AE%BE%E7%BD%AE-portrait.png)

### 第四步：查找软件版本

在设置菜单中，点击 **关于应用** 选项。该页面包含应用的详细信息。

![](https://wiki.bambulab.com/software/bambu-handy/check-software-version/%E5%85%B3%E4%BA%8E%E5%BA%94%E7%94%A8-portrait.png)

您将在 “Bambu Lab” 文本下方看到软件版本号，以“Version X.X.X”的格式显示。  
![](https://wiki.bambulab.com/software/bambu-handy/check-software-version/%E6%9C%80%E6%96%B0-portrait.png)

### 第五步：检查是否为最新版本

为了确保与打印机固件兼容、获取新功能以及修复漏洞，请确认您使用的是最新版应用。点击 **检查更新**。

![](https://wiki.bambulab.com/software/bambu-handy/check-software-version/%E6%A3%80%E6%9F%A5%E6%9B%B4%E6%96%B0-portrait.png)

如果有更新，您将收到下载更新版本提示。如果没有更新，您将看到提示 “**已是最新版本**”。  
![](https://wiki.bambulab.com/software/bambu-handy/check-software-version/%E5%B7%B2%E6%98%AF%E6%9C%80%E6%96%B0%E7%89%88%E6%9C%AC-portrait.png)

### 第六步：查看新功能

若想了解新版应用添加了哪些功能，在“关于应用”页面点击 **功能介绍**。  
![](https://wiki.bambulab.com/software/bambu-handy/check-software-version//%E5%8A%9F%E8%83%BD%E4%BB%8B%E7%BB%8D.jpg)

等待页面加载后，您将看到应用版本的更新说明，包含新增功能、改进内容和修复的问题。  
![](https://wiki.bambulab.com/software/bambu-handy/check-software-version/%E7%89%88%E6%9C%AC%E8%AF%B4%E6%98%8E-portrait.png)

## 故障排查

如果您无法更新应用或应用运行异常，可参考以下建议：

**1. 确保手机操作系统版本兼容：** 请确认您的手机操作系统满足 Bambu Handy 的最低要求，即 iPhone/iPad 为 **iOS 13.0 或更高版本**，安卓设备为 **Android 6.0 或更高版本**。您可通过以下路径查看操作系统版本：iOS：**设置 > 通用 > 关于本机 > 软件版本**；Android：**设置 > 关于手机 > Android 版本**。如果系统版本过旧，请前往 **设置 > 通用 > 软件更新（iOS）** 或 **设置 > 系统 > 系统更新（Android）** 进行升级。如设备不支持，请考虑使用新设备或通过 PC 上的 Bambu Studio 管理打印机。

**2. 重启应用：** 完全关闭应用后重新打开。

**3. 清除应用缓存与数据：** 有时缓存会引发问题。在 Android 设备中，前往 **设置 > 应用 > Bambu Handy > 存储 > 清除缓存**。若问题仍在，点击 **清除数据**（注意：操作后需重新登录）。iOS 不提供清除缓存选项，建议选择卸载应用（**设置 > 通用 > iPhone 存储空间 > Bambu Handy > 卸载应用**），然后重新安装。

**4. 重新安装应用：** 长按应用图标选择“删除应用”（iOS）或“卸载”（Android），之后重新下载并安装最新版。请注意需要重新登录账户。

## 结语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)，点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
