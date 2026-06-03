---
path: zh/bambu-studio/troubleshoot/win-crash-when-slicing
title: "Windows系统切片崩溃故障排查"
description: ""
tags: []
created: 2024-07-05T09:28:47.936Z
updated: 2025-07-21T12:46:46.603Z
source: https://wiki.bambulab.com/zh/bambu-studio/troubleshoot/win-crash-when-slicing
---

## 问题现象

使用 Windows 系统时，在 Bambu Studio 中通过点击“切片单盘”、“切片所有盘”、切换到“预览”页面，对 .3mf 文件进行切片，切片过程中 Bambu Studio 可能会崩溃或者闪退。

## GPU 线程优化异常

如果您的电脑使用的是 NVIDIA 的 GPU 其中的多线程优化可能会导致 Bambu Studio 切片过程出现崩溃，您可以通过以下方法将其关闭。

在 NVIDIA 控制面板中，进入“**3D 设置 → 管理 3D 设置 → 程序设置**”，将 Bambu Studio 添加到程序列表。找到名为“**线程优化**”的设置并将其**关**。

![zh.jpg](https://wiki.bambulab.com/software/bambu-studio/zh.jpg)

> 如果您在电脑中并没有找到 NVIDIA 控制面板，可以通过此微软应用商店下载安装[NVIDIA 控制面板。](https://apps.microsoft.com/detail/9nf8h0h7wmlt?hl=zh-TW&gl=TW) 或者通过 [NVIDIA 官方网站](https://www.nvidia.cn/drivers/lookup/)更新最新版本驱动。

## CPU 不能稳定支持超线程

该问题很可能是超频 CPU 不能稳定支持多线程导致的，可以参考以下面的方法解决。

### 方法一

步骤 1. 按 Ctrl + Shift + Escape 打开任务管理器。

步骤 2. 点击“详细信息”页签。

![](https://wiki.bambulab.com/bambu-studio/troubleshoot/win-crash-when-slicing/%E4%BB%BB%E5%8A%A1%E7%AE%A1%E7%90%86%E5%99%A8%E8%AF%A6%E7%BB%86%E4%BF%A1%E6%81%AF.png)

步骤 3.找到 bambu-studio.exe，右键选择“设置相关性”。

![](https://wiki.bambulab.com/bambu-studio/troubleshoot/win-crash-when-slicing/%E8%AE%BE%E7%BD%AE%E7%9B%B8%E5%85%B3%E6%80%A7.png)

步骤 4. 在弹出的“处理器相关性”窗口中，取消选择“所有处理器”，仅选择一部分CPU即可。例如选择 CPU 0 到 CPU 3，或者 CPU 0 到 CPU 7。

![](https://wiki.bambulab.com/bambu-studio/troubleshoot/win-crash-when-slicing/%E5%A4%84%E7%90%86%E5%99%A8%E7%9B%B8%E5%85%B3%E6%80%A7.png)

步骤 5. 点击“确定”。再次尝试在 Bambu Studio 中切片，观察是否还会出现崩溃或闪退。

### 方法二（适用于英特尔处理器）

步骤 1. 下载并安装“Intel extreme tuning utility”。

步骤 2. 选择“Advanced Tuning > Benchmarking”。

步骤 3. 将“Performance Active-Core Tuning”下的所有选项设置为“54x”，然后点击“应用”。

![](https://wiki.bambulab.com/bambu-studio/troubleshoot/win-crash-when-slicing/%E6%94%B9%E4%B8%BA54.png)

步骤 4. 再次尝试在 Bambu Studio 中切片，观察是否还会出现崩溃或闪退。

## 结束语

> 我们希望这份指南为您提供了有效的信息，并真实地帮助了您。  
> 如果您对本文中描述的过程有任何疑虑或疑问，您可以在开始操作前联系我们的客户服务团队。 我们随时准备为您提供帮助并回答您的任何问题。  
> [点击这里提交服务工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)
