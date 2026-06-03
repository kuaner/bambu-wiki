---
path: zh/a1-mini/maintenance/heatbed-replacement-guide
title: "A1 mini 热床更换指引"
description: "本指南详细介绍了如何卸下和安装A1 mini的热床。"
tags: []
created: 2024-03-06T09:43:31.998Z
updated: 2026-04-23T01:50:01.278Z
source: https://wiki.bambulab.com/zh/a1-mini/maintenance/heatbed-replacement-guide
---

![](https://wiki.bambulab.com/a1m/replace-heatbed/a1_mini_heatbed_unit.jpg)

## 何时使用?

A1 mini 热床引起的常见问题：

- 热床不加热
- 热床表面损坏
- 联系拓竹技术支持后建议更换

## 工具

- A1 mini的新热床
- H2.0 内六角扳手
- 15分钟时间

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，**请关闭打印机电源并断开电源连接**，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。
>
> 如果您对本指南有任何疑问，请[点击提交服务工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)，我们将及时回复并为您提供所需的帮助。

## 拆除

### 1. 移除热床上方的打印板

![](https://wiki.bambulab.com/a1m/replace-heatbed/remove_the_textured_pei_plate.jpg)

### 2. 移除热床螺丝

移除热床上的三颗松紧螺丝。请注意，热床右上角的位置没有螺丝的。

![](https://wiki.bambulab.com/a1m/replace-heatbed/heatbed_locking_screws.jpeg)

然后移除四颗图示的热床螺钉。

![](https://wiki.bambulab.com/a1m/replace-heatbed/remove_the_four_heatbed_screws.jpeg)

### 3. 移除打印机底部的外壳

请将打印机侧放，使得Z轴支柱朝向桌面，并拧下下图所示的16颗螺丝。

请注意，第15号和第16号螺丝是不同的，请记住它们，以便在重新安装底部外壳时使用。

![](https://wiki.bambulab.com/a1m/replace-mc-board-fan/remove_bottom_cover_screws_for_a1_mini.jpeg)

卸下螺丝后，轻轻撬出外壳。可以从右上方开始，绕着外壳边缘轻轻转动，直到外壳松动。

### 4. 取下塑料电线盖

请小心拧下固定塑料电线盖的三颗螺丝。请注意，第 3 号螺丝位于侧面。

![](https://wiki.bambulab.com/a1m/power-supply/remove_the_plastic_wire_cover.jpeg)

### 5. 断开热床线

您现在可以拆下热床线。  
连接器处有一个安全扣，起固定作用，因此在移除电线时需要推动小金属夹子。

![](https://wiki.bambulab.com/a1m/replace-heatbed/remove_the_heatbed_cables.jpeg)

这张图展示了更多细节：

![](https://wiki.bambulab.com/a1m/replace-heatbed/secure_latch_on_wire.jpeg)

### 6. 从打印机上移除热床线

移除固定支架的螺丝，然后移除热床线。

![](https://wiki.bambulab.com/a1m/replace-heatbed/unscrew_the_cable_.jpeg)

现在您可以移除热床了。

## 安装

### 1. 将热床线连接到打印机上

小心地将电缆安装在支架上，然后适度拧紧螺钉，注意不要过紧。  
请注意电线安装的方向如下图所示。

![](https://wiki.bambulab.com/a1m/replace-heatbed/install_the_new_heatbed_cable.jpeg)

### 2. 重新连接热床线

重新连接热敏电阻线，然后仔细地将红色和黑色电线连接到主板上。

**不要忘记将橡胶绝缘套推到热床线连接器上。**

![](https://wiki.bambulab.com/a1m/replace-heatbed/re-connect_the_heatbed_wires.jpeg)

### 3. 安装固定塑料线盖的螺丝

请按照图像中所示的方式，安装热床线和电源线，然后使用三颗螺丝将塑料电线盖固定。**请避免过度拧紧，以免造成滑丝。**

![](https://wiki.bambulab.com/a1m/power-supply/remove_the_plastic_wire_cover.jpeg)

### 4. 整理线缆

在重新安装底部外壳之前，请确保主板上的线缆位置都安装正确。

![](https://wiki.bambulab.com/a1m/replace-usb-c-cable/a1_mini_board_and_wire_managemet.jpg)

### 5. 安装底部外壳

将底部外壳安装回打印机中。请先拧紧螺丝15和16，然后继续安装其他剩余的螺丝，**请避免过度拧紧，以免造成滑丝。**

![](https://wiki.bambulab.com/a1m/replace-mc-board-fan/remove_bottom_cover_screws_for_a1_mini.jpeg)

### 6.安装热床和螺丝

请将热床安装回原位，并使用图中所示的四颗螺丝进行安装。在安装螺丝之前，请确保热床线没有任何缠绕，以避免需要再次拆卸。

![](https://wiki.bambulab.com/a1m/replace-heatbed/remove_the_four_heatbed_screws.jpeg)

将螺丝拧紧至与热床底座齐平。

![](https://wiki.bambulab.com/a1m/replace-heatbed/heatbed_screw.png)

## 功能检查

为确保正常运作，请打开打印机并检查加热床温度是否正确显示，并确认加热功能正常工作。

## 设备校准

请参考Wiki [A1 mini 热床手动调平](manual-bed-tramming.md)进行调平，然后对打印机进行校准操作。这一步骤对于确保打印平面的平整度非常重要。

## 可能出现的问题和解决方案

如果在安装新的热床过程中遇到问题，请参考以下列出的潜在问题和解决方案：:

### 热床温度未显示或显示为0℃

请检查安装步骤2. 重新连接热床线部分，确认绿色和白色线缆连接器已完全插入主板。

### 热床无法加热

请检查安装步骤2. 重新连接热床线部分，确认红色和黑色线缆连接器已完全插入主板。

### 首层打印不连续/首层打印有问题

开始打印之前，请确认热端加热组件的螺丝已拧紧，并且开启了“打印板调平”功能。

请参考Wiki[A1系列打印首层打印质量问题及对应方案——首层偏低](../troubleshooting/print-issues-troubleshooting.md)获取更多信息。

## 结束语

> 我们希望这份指南为您提供了有效的信息，并真实地帮助了您。
>
> 如果您对本文中描述的过程有任何疑虑或疑问，您可以在开始操作前联系我们的客户服务团队。 我们随时准备为您提供帮助并回答您的任何问题。
>
> [点击这里提交服务工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)
