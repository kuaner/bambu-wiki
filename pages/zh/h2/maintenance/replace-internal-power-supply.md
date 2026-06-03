---
path: zh/h2/maintenance/replace-internal-power-supply
title: "更换 H2 系列电源"
description: "本文介绍了如何更换 H2 系列电源"
tags: []
created: 2025-03-27T10:50:35.183Z
updated: 2026-03-13T03:15:39.643Z
source: https://wiki.bambulab.com/zh/h2/maintenance/replace-internal-power-supply
---

## 电源

H2D 打印机的电源模块是一个输入电压为 AC 100-240V，输出电压为 DC 24V 的电源转换器，它为除加热床以外的整个打印机供电。

![](https://wiki.bambulab.com/h2/maintenance/replace-internal-power-supply/img_v3_02k0_f7a30b88-4174-452f-a746-68c75962fd7g.jpg)

**电源备件包含以下：**

1. 电源\*1
2. BTW3x6 螺丝 - 用于固定电源\*2

## 何时更换

当您确定电源模块的输出电压不正常，或者电源模块板上的元器件有明显的烧坏现象时，可能需要更电源模块。

## 所需的工具和材料

1. 新的电源
2. H2.0 内六角扳手
3. 十字螺丝刀

**更换 H2D 电源所涉及的螺丝规格及数量（建议妥善保管拆下的螺丝，避免丢失）：**

| **螺丝规格** | **螺丝图片** | **用途** | **位置示意图** |  | **螺丝数量** |
| --- | --- | --- | --- | --- | --- |
| BT3x8 |  | 用于固定背板（绿色方框标记） |  |  | 12 |
| ST3x8 |  | 用于固定背板（红色圆圈标记） |  |  | 11 |
| ST3x12 |  | 用于固定料盘支架底座（黄色方框标记） |  |  | 2 |
| BTW3x6 |  | 用于固定电源 |  |  | 2 |

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。
>
> 如果您对本指南有任何疑问，[*请联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)，我们将及时回复并为您提供所需的帮助。

## 移除电源

### 步骤 1：移除背板

您可以参考这篇 Wiki 来移除打印机背板。

[更换 H2D 背板](replace-rear-panel.md)

### 步骤 2：断开电源线缆

向上扣开透明的保护壳后，使用十字螺丝刀拧松电源上的连接线固定螺丝（可以不用完全移除，拧松即可），然后将线缆向下取出。

![](https://wiki.bambulab.com/h2/maintenance/replace-internal-power-supply/image-4.png)

> ℹ️ **注意：** 部分 H2 系列打印机的黑色导线与黄绿导线压接在一起，连接到电源供应器的 (-V) 端子。  
> 其他版本则仅使用单根黑色导线连接到 (-V) 端子。两种接线配置的工作方式相同，且由于两根导线在同一压接处，拆解步骤也一致。
>
> ![gnd_wire.png](https://wiki.bambulab.com/h2/maintenance/replace-internal-power-supply/gnd_wire_zh.jpg)

### 步骤 3：移除电源

使用 H2.0 内六角扳手移除两颗固定螺丝（BTW3x6），然后从左侧（移除螺丝这一侧）向上掰开打印机电源，然后取出。

> 这一步需要稍微用力取出电源，先将左侧取出后即可完全取出电源。

![](https://wiki.bambulab.com/h2/maintenance/replace-internal-power-supply/image-5.png)

![del-power.webp](https://wiki.bambulab.com/h2/maintenance/replace-internal-power-supply/del-power.webp)

## 安装电源

### 步骤 1：放入电源模块

#### 方法一：

向右侧用力挤压内衬，

![push.jpeg](https://wiki.bambulab.com/h2/maintenance/replace-internal-power-supply/push.jpeg)

当内衬轻微变形，电源模块将卡在特定位置，

![specialspace.png](https://wiki.bambulab.com/h2/maintenance/replace-internal-power-supply/specialspace.png)

再小心拍入电源模块，

![hit.jpeg](https://wiki.bambulab.com/h2/maintenance/replace-internal-power-supply/hit.jpeg)

最后使用 H2.0 内六角扳手拧紧两颗固定螺丝（BTW3x6）。

![](https://wiki.bambulab.com/h2/maintenance/replace-internal-power-supply/image-9.png)

此方法需要一点力气和技巧，如果打印机需要运输，推荐此方法确保电源模块固定牢靠。

下面是完整动图。

![powerbirdview.webp](https://wiki.bambulab.com/h2/maintenance/replace-internal-power-supply/powerbirdview.webp)

#### 方法二：

> 如果您觉得方法一操作困难，您可以选择方法二。

先剪断内衬右下卡扣，再将电源模块的右侧放入内衬的卡扣下面，然后将左侧用力按入内衬中，最后使用 H2.0 内六角扳手拧紧两颗固定螺丝（BTW3x6）。

![power_supply_buckle.jpg](https://wiki.bambulab.com/h2/maintenance/replace-internal-power-supply/power_supply_buckle.jpg)

![](https://wiki.bambulab.com/h2/maintenance/replace-internal-power-supply/2-improve.webp)

![](https://wiki.bambulab.com/h2/maintenance/replace-internal-power-supply/image-9.png)

### 步骤 2：连接电源线缆

将线缆参考下图依次接入电源，然后使用十字螺丝刀拧紧螺丝，最后将透明保护壳扣紧。

线缆的颜色从左往右依次为：

1. 红色
2. 黄黑
3. 黄色（两根黄色的线缆均接在这里）
4. 蓝色
5. 棕色

![](https://wiki.bambulab.com/h2/maintenance/replace-internal-power-supply/image-10.png)

> ℹ️ **注意：** 部分 H2 系列打印机的黑色导线与黄绿导线压接在一起，连接到电源供应器的 (-V) 端子。  
> 其他版本则仅使用单根黑色导线连接到 (-V) 端子。两种接线配置的工作方式相同，且由于两根导线在同一压接处，拆解步骤也一致。
>
> ![gnd_wire.png](https://wiki.bambulab.com/h2/maintenance/replace-internal-power-supply/gnd_wire_zh.jpg)

### 步骤 3：安装背板

您可以参考这篇 Wiki 来安装打印机背板。

[更换 H2D 背板](replace-rear-panel.md)

## 如何验证成功

连接电源线并打开电源。在屏幕上点击运行设备自检。如果自检完成后没有错误提示，则替换完成并成功。

否则，请检查所有连接，然后重试。如果问题仍然存在，请联系 Bambu Lab 服务团队寻求进一步的帮助。

## 结束语

> 我们希望这份指南为您提供了有效的信息，并真实地帮助了您。
>
> 如果您对本文中描述的过程有任何疑虑或疑问，您可以在开始操作前联系我们的客户服务团队。 我们随时准备为您提供帮助并回答您的任何问题。
>
> [点击此处联系在线技术支持 （服务时间 9:00-21:00）](https://support.bambulab.cn/cn/im)
