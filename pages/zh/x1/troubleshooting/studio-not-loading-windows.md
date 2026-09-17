---
path: zh/x1/troubleshooting/studio-not-loading-windows
title: "Bambu Studio 在Windows上无法启动"
description: ""
tags: []
created: 2022-08-01T06:43:05.735Z
updated: 2026-08-28T08:23:23.408Z
source: https://wiki.bambulab.com/zh/x1/troubleshooting/studio-not-loading-windows
---

在某些情况下，Bambu Studio无法在Windows上顺利加载。这个问题可能是由于没有启用Windows媒体播放器功能造成的，而且它主要存在于Windows N版本。

下面是解决这个问题的方法。

## 导航到Windows Media Player支持页面

打开 [Windows Media Player support page](https://support.microsoft.com/zh-cn/windows/%E8%8E%B7%E5%8F%96-windows-media-player-81718e0d-cfce-25b1-aee3-94596b658287)

## 用Windows Media Player功能

要在Windows中启用Windows Media Player，请选择“**开始**”按钮，然后选择**设置**>**应用程序**>**应用程序和功能**>**管理可选功能**>**添加功能**

![](https://wiki.bambulab.com/x1/troubleshooting/studio-not-loading-windows/add_a_feature.png)

在下一个窗口中，查找**Windows媒体播放器**。选择它，单击“安装”，然后等待它被启用。

![](https://wiki.bambulab.com/x1/troubleshooting/studio-not-loading-windows/scr-20220726-ba5-2.png)

## **配置文件出错**

### **Bambu Studio GUl initialization failed 相关报错**

此故障可能是由于配置文件损坏导致的。

您可以通过下载并运行[此文件](https://wiki.bambulab.com/software/fix-bambu-studio.bat)快速解决此问题。它会自动备份旧的配置文件，并允许您启动 Bambu Studio。

![](https://wiki.bambulab.com/x1/troubleshooting/studio-not-loading-windows/error_image1.png)

![](https://wiki.bambulab.com/x1/troubleshooting/studio-not-loading-windows/error_image2.png)

请跳转至文件夹 **C:\Users\[user.name](http://user.name)\AppData\Roaming\BambuStudio**， 删除 **BambuStudio.conf** 和 **system** 文件后，再次打开 Bambu Studio。

![](https://wiki.bambulab.com/bambu-studio/trouble/output.png)

> 注意：找到 AppData 需要打开**隐藏的项目**。
>
> ![](https://wiki.bambulab.com/software/20251020-142628.jpg)

## 重启计算机

安装过程完成后，重新启动计算机，Bambu Studio 应该能够成功加载。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
