---
path: zh/x1/troubleshooting/bambu-studio-crashes-when-watching-online-video
title: "用Bambu Studio观看在线视频时软件崩溃"
description: ""
tags: []
created: 2022-08-31T07:45:58.828Z
updated: 2024-05-28T10:32:25.087Z
source: https://wiki.bambulab.com/zh/x1/troubleshooting/bambu-studio-crashes-when-watching-online-video
---

## 现象

每次在Bambu Studio里连接摄像头观看视频时，软件都会崩溃卡死。

![](https://wiki.bambulab.com/x1/troubleshooting/bambu-studio-crash/bambu_studio卡死崩溃.png)

## 原因

目前Bambu Studio和多显卡的电脑兼容性还不是很好，所以有时会遇到这个问题，我们也在持续地优化软件中。

## 解决方案

可以在**Nvidia控制面板**中，将Bambu Studio的图形处理器设置为**集成图形**处理来临时解决这个问题。

需要通过Nvidia control panel进行以下操作，如果没有Nvidia控制面板，则需要先到nvidia官网下载并安装一下相关显卡的驱动：<https://www.nvidia.cn/Download/find.aspx>

1.打开nvdia设置：

![](https://wiki.bambulab.com/x1/troubleshooting/bambu-studio-crash/点击nvidia.png)

2.进入“管理3D设置”，通常这里可以看到首选图形处理器为“自动选择”。

![](https://wiki.bambulab.com/x1/troubleshooting/bambu-studio-crash/管理3d设置.png)

3.点击进入“程序设置”，在“选择要自定义的程序”里添加bambu studio，然后将首选图形处理器设置为“集成图形”并应用。

![](https://wiki.bambulab.com/x1/troubleshooting/bambu-studio-crash/bambu_studio设置为集成图形.png)

4.然后重新启动Bambu studio，这时候应该就可以正常连接摄像头观看视频了。若仍有问题，请创建工单联系售后团队。

## 结束语

> 我们希望这份指南为您提供了有效的信息，并真实地帮助了您。
>
> 如果您对本文中描述的过程有任何疑虑或疑问，您可以在开始操作前联系我们的客户服务团队。 我们随时准备为您提供帮助并回答您的任何问题。
>
> [点击这里提交服务工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)
