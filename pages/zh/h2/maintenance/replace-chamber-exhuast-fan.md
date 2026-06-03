---
path: zh/h2/maintenance/replace-chamber-exhuast-fan
title: "更换 H2 系列腔体外排风扇"
description: "本文介绍了如何更换 H2 系列腔体外排风扇"
tags: []
created: 2025-03-27T10:37:30.411Z
updated: 2026-03-13T03:13:20.545Z
source: https://wiki.bambulab.com/zh/h2/maintenance/replace-chamber-exhuast-fan
---

## 腔体外排风扇

腔体外排风扇是安装在打印机右内衬，活性炭滤芯的后面，用于将打印机内部的空气往外排出。

**腔体外排风扇的备件包含如下：**

1. 腔体外排风扇 \* 1
2. 自动排气格栅 \* 2
3. 软螺钉 \* 4

![腔体外排.jpg =300x](https://wiki.bambulab.com/h2/maintenance/screw-kit-h2d/%E8%85%94%E4%BD%93%E5%A4%96%E6%8E%92.jpg)

## 何时更换

- 腔体外排风扇发出异响
- 腔体外排风扇损坏

## 所需的工具和材料

1. 新的腔体外排风扇
2. H2.0 内六角扳手

**更换 H2D 腔体外排风扇所涉及的螺丝规格及数量（建议妥善保管拆下的螺丝，避免丢失）：**

| **螺丝规格** | **螺丝图片** | **用途** | **位置示意图** |  | **螺丝数量** |
| --- | --- | --- | --- | --- | --- |
| BT3x8 |  | 用于固定背板（绿色方框标记） |  |  | 12 |
|  |  | 用于固定废料滑梯 |  |  | 1 |
| ST3x8 |  | 用于固定背板（红色圆圈标记） |  |  | 11 |
| ST3x12 |  | 用于固定料盘支架底座（黄色方框标记） |  |  | 2 |

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。
>
> 如果您对本指南有任何疑问，[*请联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)，我们将及时回复并为您提供所需的帮助。

## 移除腔体外排风扇

### 步骤 1：移除背板和废料滑梯

您可以参阅这篇 Wiki 来移除打印机背板和废料滑梯：

[更换 H2D 废料滑梯](replace-purge-chute.md)

### 步骤 2：移除自动排气格栅

请小心移除自动排气格栅，如果有损坏可以使用备用自动排气格栅。您可以参考这篇 Wiki 来移除：

[更换 H2D 自动排气格栅](replace-active-chamber-exhaust.md)

### 步骤 3：移除活性炭滤芯盖和活性碳滤芯

由于后续需要从这一侧来固定软螺钉，因此您可以参考这篇 Wiki 来移除活性炭滤芯盖和活性炭滤芯：

[更换 H2D 活性碳滤芯盖/活性碳滤芯](replace-air-filter.md)

### 步骤 4：移除腔体外排风扇

1. 您可以先从 MC 板上断开腔体外排风扇的连接线，并将线缆从线扣中移除；

![](https://wiki.bambulab.com/h2/maintenance/replace-chamber-exhuast-fan/image-4.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-chamber-exhuast-fan/image-5.png)

2. 腔体外排风扇是通过软螺钉固定在右内衬上，您可以用力将风扇拔出。拔出后可以将留在内衬上的软螺钉取出。

![](https://wiki.bambulab.com/h2/maintenance/replace-chamber-exhuast-fan/img_v3_02k0_e8612b69-39b8-47ea-91d5-9163ffcc2b6g.jpg)

![](https://wiki.bambulab.com/h2/maintenance/replace-chamber-exhuast-fan/image-6.png)

> 软胶钉可能存在颜色不同的情况，不影响安装与功能。

## 安装腔体外排风扇

### 步骤 1：安装腔体外排风扇

1. 取出4个软螺钉，将其中一个的尾端剪断；

![stick1.jpeg](https://wiki.bambulab.com/h2/maintenance/replace-chamber-exhuast-fan/stick1.jpeg)

2. 将软螺钉预安装到腔体外排风扇的三个角落；

![install-stick.webp](https://wiki.bambulab.com/h2/maintenance/replace-chamber-exhuast-fan/install-stick.webp)  
![fan-with-stick.jpg](https://wiki.bambulab.com/h2/maintenance/replace-chamber-exhuast-fan/fan-with-stick.jpg)

3. 将裁剪过的软螺钉安装在内衬的左下角；

![install-stick-printer.webp](https://wiki.bambulab.com/h2/maintenance/replace-chamber-exhuast-fan/install-stick-printer.webp)

4. 检查线缆位置，避免风扇朝向错误；

![](https://wiki.bambulab.com/h2/maintenance/replace-chamber-exhuast-fan/image-7.png)

5. 然后将打印机上螺钉拉入腔体外排风扇中，拉动螺钉并向内推入风扇，确保螺钉卡主风扇；  
   ![sitick-leftdown.webp](https://wiki.bambulab.com/h2/maintenance/replace-chamber-exhuast-fan/sitick-leftdown.webp)
6. 您可以轻轻推动挡风板，以便拉出螺钉，再从侧面塞入固定孔。

> 如果你发现软钉头过短，不便操作，可以用镊子等工具辅助安装。  
> 先拉动右下角的软螺钉，将软螺钉卡入内衬的卡扣中，然后依次安装左下、右上和左上三个软螺钉。

|  |  |  |
| --- | --- | --- |
| 黄色软螺钉 | install-fan-leftup.webp | install-fan-rightdown.webp |
| 白色软螺钉 |  |  |

7. 将线缆从内衬上的缺口穿过，然后依次卡入线扣中，最后与 MC 板连接。

![](https://wiki.bambulab.com/h2/maintenance/replace-chamber-exhuast-fan/image-9.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-chamber-exhuast-fan/image-10.png)

### 步骤 2：安装废料滑梯和背板

您可以参阅下面的这篇 Wiki 来安装废料滑梯和背板：

[更换 H2D 废料滑梯](replace-purge-chute.md)

### 步骤 3：安装自动排气格栅

您可以参阅下面的这篇 Wiki 来安装自动排气格栅：

[更换 H2D 自动排气格栅](replace-active-chamber-exhaust.md)

### 步骤 4：安装活性碳滤芯盖和活性炭滤芯

您可以参阅下面的这篇 Wiki 来安装活性碳滤芯盖和活性炭滤芯：

[更换 H2D 活性碳滤芯盖/活性碳滤芯](replace-air-filter.md)

## 如何验证成功

连接电源并打开打印机，检查腔体外排风扇可以正常使用。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 为了确保您安全有效地进行操作，如果对指南中的任何步骤有疑虑或问题，请在开始操作前联系我们的客户服务团队，我们随时乐意为您解答疑问并提供支持。  
> [点击此处联系在线技术支持 （服务时间 9:00-21:00）](https://support.bambulab.cn/cn/im)
