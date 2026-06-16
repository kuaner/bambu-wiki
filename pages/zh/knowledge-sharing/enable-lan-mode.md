---
path: zh/knowledge-sharing/enable-lan-mode
title: "如何在Bambu Lab打印机上使用局域网模式"
description: "有关在 Bambu Lab 打印机上使用局域网模式的指南"
tags: []
created: 2023-08-30T06:27:06.873Z
updated: 2026-06-02T02:27:59.647Z
source: https://wiki.bambulab.com/zh/knowledge-sharing/enable-lan-mode
---

## 什么是局域网模式？

Bambu Lab 具备局域网模式功能，允许打印机在局域网内工作，并与 Bambu Studio 进行通信，以发送文件、监控打印进度和查看视频，而无需访问任何云网络。如果您需要打印高度机密的模型，并希望保持私密性和安全性，此功能将非常有用。请注意，**打印机和计算机必须连接在同一个网络中。**

启用 LAN 模式后，以下功能将不可用：

- 无法在本地网络之外远程启动打印
- 无法使用 Bambu Handy
- 无法使用打印历史功能

关于[炒面检测](Spaghetti_detection.md)：

X1 系列打印机的处理器芯片支持炒面检测。该系统采用机器学习算法，并且所有的数据处理都在本地完成。当打印机处于局域网模式时，它的运行方式类似于没有连接互联网，使用打印机的芯片来处理此功能。

如果打印机没有连接到云端，并且未启用用户改进选项，打印机仅依赖于最新固件中的信息进行故障检测，与云连接的体验相比可能较为陈旧，因为炒面检测的算法可能不是最新的。所以，我们建议定期更新固件，以获取最新的其他改进。

## 使用访问码连接打印机

### H2 系列/ P2S / X 系列打印机

#### 步骤一：在打印机端启用“仅局域网”模式

- 在设置里，点击 **设置 > 仅局域网**，进入“仅局域网”页面。

![](https://wiki.bambulab.com/knowledge-sharing/lan-mode/%E8%AE%BE%E7%BD%AE-.jpg)

![](https://wiki.bambulab.com/knowledge-sharing/lan-mode/%E4%BB%85%E5%B1%80%E5%9F%9F%E7%BD%91.jpg)

- 开启“仅局域网”模式。

![](https://wiki.bambulab.com/knowledge-sharing/lan-mode/lanmode.png)

- 根据需求选择是否开启局域网模式实况。

![](https://wiki.bambulab.com/knowledge-sharing/lan-mode/lanmode2.png)

- 如果开启开发者模式，第三方软件或设备可控制打印机，第三方软件可管理打印机任务并处理数据。

![开发者模式-.jpg](https://wiki.bambulab.com/knowledge-sharing/lan-mode/%E5%BC%80%E5%8F%91%E8%80%85%E6%A8%A1%E5%BC%8F-.jpg)

#### 步骤二：将处于局域网模式的打印机绑定到 Bambu Studio

- 打开“设备”页面下弹出的打印机列表，找到已切换为“仅局域网”模式的打印机，仅局域网模式下的打印机名称前面会有一个锁定图标，如下图所示；

> 注意：该过程可能需要 20-60 秒，极少数情况下耗时可能更长，请您耐心等待。若打印机长时间仍未显示，需检查打印机与 Bambu Studio 是否处于同一本地网络，且两者间通信未被拦截（该问题可能出现在部分访客网络环境中）。

![device.png](https://wiki.bambulab.com/knowledge-sharing/lan-mode/device.png)

- 输入打印机访问码并单击“确认”。

![访问码.png](https://wiki.bambulab.com/knowledge-sharing/lan-mode/%E8%AE%BF%E9%97%AE%E7%A0%81.png)

- 确认连接后，您就可以在局域网模式下使用打印机。

![连接成功.png](https://wiki.bambulab.com/knowledge-sharing/lan-mode/%E8%BF%9E%E6%8E%A5%E6%88%90%E5%8A%9F.png)

- 打开“局域网模式实况”，即可在 Bambu Studio中查看打印机实况画面。

![打开局域网模式实况.png](https://wiki.bambulab.com/knowledge-sharing/lan-mode/%E6%89%93%E5%BC%80%E5%B1%80%E5%9F%9F%E7%BD%91%E6%A8%A1%E5%BC%8F%E5%AE%9E%E5%86%B5.png)

> ***注意：***  
> *在 X1 系列打印机的局域网模式下发起打印时，为了避免网络信息安全相关问题，使用局域网时需配合 Micro SD卡使用；*
>
> 您需要在打印机触摸屏右侧插入 SD 卡后，方可成功从 Bambu Studio 发起新的打印任务。了解更多SD卡相关信息，请查看[通过Micro SD卡打印的常见问题](../general/micro-sd-faq.md)*。*

### P1P/P1S系列打印机

#### 步骤一：在打印机端启用局域网模式

- 设置→网络，可以找到“局域网模式”选项。

![](https://wiki.bambulab.com/knowledge-sharing/lan-mode/p_wangluo_cn.jpg)

- “局域网模式”选项默认设置为“关闭”状态。您可以在此处“打开”此选项。

![](https://wiki.bambulab.com/knowledge-sharing/lan-mode/p_lan_guanbi_cn.jpg)

- 选择“是”，进行确认选择。

![](https://wiki.bambulab.com/knowledge-sharing/lan-mode/p_lan_shi_cn.jpg)

- 当“局域网模型”选项变为“打开”时，表示局域网模式切换成功，并且请记下访问码。

![](https://wiki.bambulab.com/knowledge-sharing/lan-mode/p_lan_connect_successful_cn.jpg)

#### 步骤二：将处于局域网模式的打印机绑定到Bambu Studio

- 打开“设备”页面下弹出的打印机列表，找到已切换为“仅局域网”模式的打印机。   
  （仅局域网模式下的打印机名称前面会有一个锁定图标，如下图所示）
- 这可能需要 20 秒到 60 秒，在极少数情况下，可能需要更长的时间，请您耐心等待。   
  如果您的打印机仍然没有显示，请检查打印机和 Bambu Studio 是否在同一个本地网络中，以及它们之间的通信是否被阻挡。（这可能发生在某些访客用户网络上）

![](https://wiki.bambulab.com/knowledge-sharing/lan-mode/stdio_lan_list.jpg)

- 输入打印机访问码并单击“确认”。确认连接后，您就可以在局域网模式下使用打印机。

![](https://wiki.bambulab.com/knowledge-sharing/lan-mode/fangwenma_cn.jpg)

### A 系列打印机

#### 步骤一：在打印机端启用局域网模式

- 点击“设置”按钮，找到“局域网模式”。

![](https://wiki.bambulab.com/knowledge-sharing/lan-mode/a1%E8%AE%BE%E7%BD%AE1.png)

- 启用“局域网模式”。如果按钮变为绿色，则表示该功能启用成功。

![](https://wiki.bambulab.com/knowledge-sharing/lan-mode/%E5%90%AF%E7%94%A8%E5%B1%80%E5%9F%9F%E7%BD%91.png)

#### 步骤二：将处于局域网模式的打印机绑定到Bambu Studio

- 打开“设备”页面下弹出的打印机列表，找到已切换为“局域网”模式的打印机。   
  （仅局域网模式下的打印机名称前面会有一个锁定图标，如下图所示）
- 这可能需要 20 秒到 60 秒，在极少数情况下，可能需要更长的时间，请您耐心等待。   
  如果您的打印机仍然没有显示，请检查打印机和 Bambu Studio 是否在同一个本地网络中，以及它们之间的通信是否被阻挡。（这可能发生在某些访客用户网络上）

![](https://wiki.bambulab.com/knowledge-sharing/lan-mode/studio_lan1.jpg)

- 选择打印机，输入打印机访问码并单击“确认”。

![](https://wiki.bambulab.com/knowledge-sharing/lan-mode/%E8%BE%93%E5%85%A5%E8%AE%BF%E9%97%AE%E7%A0%81.jpg)

- 如果连接成功，您可以在“我的设备”列表中找到该打印机，并确认连接后，您就可以在局域网模式下使用打印机。

![](https://wiki.bambulab.com/knowledge-sharing/lan-mode/lan%E6%88%90%E5%8A%9F.jpg)

## 使用访问码+ IP 连接打印机

### 特殊网络环境（打印机与电脑分属不同 VLAN、网段不同）

- 在“仅局域网”页面中查看打印机 IP 和访问码；

![局域网模式.png](https://wiki.bambulab.com/knowledge-sharing/access-code/%E5%B1%80%E5%9F%9F%E7%BD%91%E6%A8%A1%E5%BC%8F.png)

- 在 Bambu Studio 中点击设备，点击“无打印机 > 通过访问码绑定”；

![access_code-.png](https://wiki.bambulab.com/knowledge-sharing/access-code/access_code-.png)

- 输入打印机 IP 和访问码并单击“连接”。

![连接.png](https://wiki.bambulab.com/knowledge-sharing/access-code/%E8%BF%9E%E6%8E%A5.png)

> **注意：** 出于隐私保护需求，Bambu Studio 不会存储用户的打印机 IP 信息。因此，采用 IP + 访问码进行绑定时，**每次重启 Studio 后都需要重新输入这两项信息完成绑定**；若仅通过访问码连接打印机，则可避免该问题。

## 结束语

> 我们希望这份指南为您提供了有效的信息，并真实地帮助了您。
>
> 如果您对本文中描述的过程有任何疑虑或疑问，您可以在开始操作前联系我们的客户服务团队。 我们随时准备为您提供帮助并回答您的任何问题。
>
> [点击这里提交服务工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)
