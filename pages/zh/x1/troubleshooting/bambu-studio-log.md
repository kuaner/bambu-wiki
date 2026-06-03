---
path: zh/x1/troubleshooting/bambu-studio-log
title: "导出Bambu PC 软件日志"
description: ""
tags: []
created: 2022-08-26T07:54:36.304Z
updated: 2025-10-13T01:59:11.625Z
source: https://wiki.bambulab.com/zh/x1/troubleshooting/bambu-studio-log
---

## 何时需要导出日志

如果您在使用Bambu Studio的时候遇到无法启动、闪退或者无法观看摄像机视频等问题，您可以参考本文中的方式导出Bambu Studio的log并发送给我们售后支持团队，我们会帮您分析log并提供解决方案。

## Bambu Studio

### Windows操作系统

1.打开Bambu studio，点击“文件”旁边的“∨”图标，再点击“帮助”——“打开配置文件夹”，在弹出的窗口中可以看到log文件夹。

![](https://wiki.bambulab.com/x1/manual/bambu-studio-log/%E6%89%93%E5%BC%80%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6%E5%A4%B9.jpg)

![](https://wiki.bambulab.com/x1/manual/bambu-studio-log/%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6%E5%A4%B9.jpg)

2.在log文件夹中可以看到所有的log文件。如下图所示，把对应时间段的log，全部以压缩文件的形式，发送至我们的[技术支持工单](https://bambulab.cn/zh-cn/my/support/tickets?from=5)。

![](https://wiki.bambulab.com/x1/manual/bambu-studio-log/log%E6%96%87%E4%BB%B6%E5%A4%B9.jpg)

注意：如果您找不到文件，请在文件浏览器的上方，点击“查看”，勾选“隐藏的项目”之后重试。

3.如果Bambu Studio遇到无法启动或者闪退的情况，无法通过上述方式打开配置文件夹，可以直接在资源管理器里输入路径：**C:\Users\用户名\AppData\Roaming\BambuStudio\log**，进入log所在文件夹，然后将其导出。

### Mac OS

1.Mac操作系统的步骤与windows类似，只是界面略有区别。进入“帮助”——“打开配置文件夹”，即可导出log文件。

![](https://wiki.bambulab.com/x1/manual/bambu-studio-log/mac%E6%89%93%E5%BC%80%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6%E5%A4%B9.jpg)

![](https://wiki.bambulab.com/x1/manual/bambu-studio-log/mac%E9%85%8D%E7%BD%AE%E6%96%87%E4%BB%B6%E5%A4%B9(en).jpg)

![](https://wiki.bambulab.com/x1/manual/bambu-studio-log/mac_log%E6%96%87%E4%BB%B6%E5%A4%B9.jpg)

2.如果由于某些原因Bambu studio无法启动，您可以在MAC OS里下通过以下路径直接访问日志文件夹: **/Users/user.name/Library/Appliction\_support/BambuLab/log**，这个路径与windows系统不同。

![](https://wiki.bambulab.com/x1/troubleshooting/bambu-studio-log/%E9%9A%90%E8%97%8F.png)

### Linux

在 Linux 系统上，您可以在 **Home/config/BambuStudio/log** 位置下载日志。

1. 打开 Bambu Studio，选择 "文件" → "帮助" → "打开配置文件夹"。

![](https://wiki.bambulab.com/x1/troubleshooting/bambu-studio-log/linux_1.png)

2. 打开 log 文件夹即可查看所有日志。

![](https://wiki.bambulab.com/x1/troubleshooting/bambu-studio-log/linux_2.png)

![](https://wiki.bambulab.com/x1/troubleshooting/bambu-studio-log/linux_3.jpeg)

## **Bambu Suite**

1. 打开Bambu Suite，点击“∨”图标，再点击“帮助”——“打开配置文件夹”，在弹出的窗口中可以看到log文件夹。  
   ![cn.png](https://wiki.bambulab.com/staging/new-screen/cn.png)
2. 在log文件夹中可以看到所有的log文件。如下图所示，将log文件全部打包压缩（zip）的形式，发送至我们的[技术支持工单](https://bambulab.cn/zh-cn/my/support/tickets?from=5)。  
   ![file.png](https://wiki.bambulab.com/software/bambu-suite/file.png)

> 注意：请将所有日志文件复制出来后再进行打包，或在关闭 Bambu Suite 软件后再进行打包。否则，软件可能会占用某些程序，导致日志信息缺失。

## **拓竹农场管家**

1. 打开农场管家客户端，点击“设置”，并进入“工单”页面。  
   ![农场log1.png](https://wiki.bambulab.com/software/bambu-farm-manager/%E5%86%9C%E5%9C%BAlog1.png)
2. 选择日志类型为“服务器日志”，点击“准备”。等待服务器日志已准备完成后，点击“下载到本地”。就可以将服务器日志保存到电脑中，发送至我们的[技术支持工单](https://bambulab.cn/zh-cn/my/support/tickets?from=5)。  
   ![农场log2.png](https://wiki.bambulab.com/software/bambu-farm-manager/%E5%86%9C%E5%9C%BAlog2.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南并未解决您的问题，[*请点击此处联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
