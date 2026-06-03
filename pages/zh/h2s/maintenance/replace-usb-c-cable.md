---
path: zh/h2s/maintenance/replace-usb-c-cable
title: "更换 H2S USB-C线缆"
description: "本文将详细为您介绍更换 H2S 工具头 USB-C 线缆的步骤以及注意事项。"
tags: []
created: 2025-08-26T06:16:14.417Z
updated: 2026-01-19T04:20:07.011Z
source: https://wiki.bambulab.com/zh/h2s/maintenance/replace-usb-c-cable
---

## USB-C 数据线

USB-C 数据线用于连接 TH 板和 AP 板。

**USB-C 数据线的备件包含以下：**

1. USB-C 数据线 \* 1

## 何时更换

- USB-C 数据线损坏；
- 经过 Bambu Lab 官方技术支持确认需要更换。

## 所需的工具和材料

- 新的 USB-C 数据线
- H2.0 内六角扳手
- H1.5 内六角扳手

## 螺丝清单：

- 螺丝 A: 部件冷却风扇背面（和后盖共锁）以及工具头后盖螺丝，共 3 颗：BT2x6.5
- 螺丝 B: 部件冷却风扇左右两侧螺丝，共 2 颗： BT2x5
- 螺丝 C: TH 板螺丝，共 2 颗：BT2x5
- 螺丝 D: AP板盖螺丝，共1颗：BT2.6x8，下图中未包含
- 螺丝 E: USB-C线扣螺丝，共1颗
- 螺丝F：缓冲器固定螺丝，BT3\*8,共4颗

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-usb-c-cable/image-13.png)

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。
>
> 如果您对本指南有任何疑问，[*请联系在线技术支持（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)，我们将及时回复并为您提供所需的帮助。

## 移除 USB-C 数据线

### 步骤 1：断开 USB-C数据线与TH 板的连接，并从拖链支架中抽出线缆

由于 USB-C 线连接在 TH 板的背面，因此您需要先将 TH 板正面的插头松开，将TH板翻面，然后才能将 USB-C 线从 TH 板上拔出。您可以参考这篇 Wiki 先移除 TH 板，再断开USB-C的连接。您仅需参考到 TH 板与 USB-C 线缆断开连接的步骤即可。

[更换H2S TH板](replace-th-board.md)

从拖链支架中抽出线缆  
![remove-usb.webp](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-usb-c-cable/remove-usb.webp)

### 步骤 2：移除 AP 板盖与料线整理盖

使用 H2.0 内六角扳手拧下 1 颗固定螺丝（BT2.6x8），然后从靠近前门的一侧取下 AP 板盖。

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-usb-c-cable/jonjbwoh4okkoxxm0j4cxsbtnng.png)

![remove-ap-cover.webp](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-usb-c-cable/remove-ap-cover.webp)

### 步骤 3：移除缓冲器

按压解锁料管支架上的气动接头，移除与打印机背面连接的 PTFE 管；

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-usb-c-cable/image.png)

推出气动接头，按压解锁缓冲器上的气动接头，移除打印机内部的PTFE管

![remove-ptfe-tube.webp](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-usb-c-cable/remove-ptfe-tube.webp)

使用 H2.0 内六角扳手移除四颗固定螺丝，松开缓冲器。

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-usb-c-cable/image-1.png)

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-usb-c-cable/image-2.png)

### 步骤4：松开拖链

按压工具头上方的气动接头，断开工具头上方的PTFE管，并从拖链中抽出

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-usb-c-cable/image-3.png)

![remove-ptfe-toolhead.webp](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-usb-c-cable/remove-ptfe-toolhead.webp)

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-usb-c-cable/image-4.png)

断开拖链与打印机框架的连接（以H2D机型操作为例，H2S操作方法完全一致）

![remove-cable-chain-from-frame.webp](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-usb-c-cable/remove-cable-chain-from-frame.webp)

断开拖链上的2个PTFE管卡扣

![remove-buckle.webp](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-usb-c-cable/remove-buckle.webp)

将USB-C线缆从拖链中抽出

![remove-cable-from-chain.webp](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-usb-c-cable/remove-cable-from-chain.webp)

### 步骤 4：断开 USB-C 数据线与AP板的连接

1. 从卡扣中抽出USB-C线缆

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-usb-c-cable/image-5.png)

- 拧下USB-C理线扣中的螺丝。

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-usb-c-cable/image-6.png)

- 从卡扣中抽出线缆，断开 USB-C 数据线；

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-usb-c-cable/image-7.png)

## 安装 USB-C 数据线

### 步骤 1：连接USB-C数据线到 AP 板

连接新的 USB-C 数据线时，请注意，插头表面有防晃动胶带，因此需要用点力气才能将其插入，直到感觉到无法再推动为止，这样才算插入到位。

> 注意：A 字这一头与 AP 板连接，并且 A 字朝外！

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-usb-c-cable/image-8.png)

![connect-USB-C.webp](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-usb-c-cable/connect-usb-c.webp)

然后将线缆依次卡入线扣中，锁入线扣固定螺丝。

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-usb-c-cable/image-9.png)

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-usb-c-cable/image-10.png)

### 步骤 2：安装拖链

1. 将 USB-C 数据线装入拖链中，开口方向朝外，前后拉扯线缆，留出合适的长度；

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-usb-c-cable/image-11.png)

![insert-cable-to-chain.webp](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-usb-c-cable/insert-cable-to-chain.webp)

连接拖链与打印机框架（以H2D机型操作为例，H2S操作方法完全一致）

![install-cable-chain.webp](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-usb-c-cable/install-cable-chain.webp)

装回拖链卡扣，分别在第11节和第18节处卡入拖链卡扣

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-usb-c-cable/image-12.png)

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-usb-c-cable/image-14.png)

![cable-chain-buckle.webp](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-usb-c-cable/cable-chain-buckle.webp)

穿入PTFE管，连接气动接头

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-usb-c-cable/image-15.png)

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-usb-c-cable/image-16.png)

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-usb-c-cable/image-17.png)

### 步骤 4：安装缓冲器

将USB-C线缆卡入框架中的凹槽内，对准孔位，装回缓冲器。

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-usb-c-cable/image-18.png)

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-usb-c-cable/image-19.png)

缓冲器对准螺丝孔位后，使用 H2.0 内六角扳手拧紧四颗固定螺丝（BT3×8），最后重新将两根 PTFE 管与缓冲器连接。

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-usb-c-cable/image-20.png)

### 步骤 5：安装 AP 板盖

先从靠近打印机背面的一侧扣回 AP 板盖，将箭头所示的两处均按压到位，右侧与缓冲器齐平，底部与护线盖齐平，然后使用 H2.0 内六角扳手拧紧一颗固定螺丝（BT2.6x8）。

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-usb-c-cable/image-21.png)

注意：安装 AP 板盖前，需检查线缆是否阻碍 PTFE 管路，避免影响后续 PTFE 管的安装。

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-usb-c-cable/yp5wbuiapogrzlx23ttcyngrn0e.png)

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-usb-c-cable/image-22.png)

### 步骤 3：连接USB-C数据线到TH板

将USB-C线缆卡入拖链支架中  
![install-usb.webp](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-usb-c-cable/install-usb.webp)

参考TH板安装教程，连接TH板端的USB-C线缆插头，并重新安装TH板

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-usb-c-cable/image-23.png)

[更换H2S TH板](replace-th-board.md)

## 如何验证成功

连接电源并打开打印机，发起打印无报错即可。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南未解决您的问题，[*请联系在线技术支持（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！

[replace-toolhead-with-x-axis-assembly.mp4](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-toolhead-with-x-axis-assembly.mp4)
