---
path: zh/h2/maintenance/replace-power-safety-key-unit
title: "更换 H2 系列电源安全钥匙组件"
description: "本文介绍了如何更换 H2 系列电源安全钥匙组件"
tags: []
created: 2025-03-28T04:31:09.311Z
updated: 2026-03-13T03:22:54.916Z
source: https://wiki.bambulab.com/zh/h2/maintenance/replace-power-safety-key-unit
---

## 电源安全钥匙组件

![安全钥匙抠图.jpg](https://wiki.bambulab.com/h2/maintenance/replace-power-safety-key-unit/%E5%AE%89%E5%85%A8%E9%92%A5%E5%8C%99%E6%8A%A0%E5%9B%BE.jpg)

> 部分安全钥匙组件没有地线，您在拆装时可省略接地线的步骤。两种版本的安全钥匙在核心安全功能上完全一致。

**电源安全钥匙组件的备件包含以下：**

1. 电源安全钥匙底座 \* 1
2. 电源安全钥匙 \* 1
3. 螺丝 - 用于固定电源安全钥匙底座 \* 2

## 何时更换

- 电源安全钥匙组件损坏

## 需要的工具和材料

- 新的电源安全钥匙组件
- H2.0 内六角扳手

**更换 H2D 电源安全钥匙组件所涉及的螺丝规格及数量（建议妥善保管拆下的螺丝，避免丢失）：**

| **螺丝规格** | **螺丝图片** | **位置** | **位置示意图** |  | **螺丝数量** |
| --- | --- | --- | --- | --- | --- |
| BT3x8 |  | 用于固定背板（绿色方框标记） |  |  | 12 |
|  |  | 用于固定废料滑梯 |  |  | 1 |
|  |  | 用于固定电源开关插座 |  |  | 1 |
| ST3x8 |  | 用于固定背板（红色圆圈标记） |  |  | 11 |
|  |  | 用于固定电源开关插座 |  |  | 1 |
| ST3x12 |  | 用于固定料盘支架底座（黄色方框标记） |  |  | 2 |
| BT2.3x7 |  | 用于固定电源安全钥匙底座 |  |  | 2 |

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。
>
> 如果您对本指南有任何疑问，请点击此处联系在线技术支持 （服务时间 9:00-21:00），我们将及时回复并为您提供所需的帮助。

## 移除电源安全钥匙组件

### 步骤 1：移除电源安全钥匙

将电源安全钥匙从打印机上拔下。

### 步骤 2：移除背板和废料滑梯

您可以参考这篇 Wiki 来移除打印机背板和废料滑梯：

[更换 H2D 废料滑梯](replace-purge-chute.md)

### 步骤 3：拆除地线

拧下图中的螺丝，释放开关组件的地线和安全钥匙组件地线。  
![安全钥匙地线.jpeg](https://wiki.bambulab.com/h2/maintenance/replace-power-safety-key-unit/%E5%AE%89%E5%85%A8%E9%92%A5%E5%8C%99%E5%9C%B0%E7%BA%BF.jpeg)

### 步骤 4：移除电源开关插座

由于线缆被挡在电源开关插座旁边，您仅需将电源开关插座取出即可，以便于移除线缆。

> 为便于后续的拆装，电源开关插座仅需取出，而无需将连接线断开。

使用 H2.0 内六角扳手移除两颗电源开关插座固定螺丝（固定在底座上：ST3x8，固定在右内衬上：BT3x8），然后将电源开关插座取出，并按下卡扣与电源安全钥匙底座断开连接；

![](https://wiki.bambulab.com/h2/maintenance/replace-power-safety-key-unit/image.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-power-safety-key-unit/img_v3_02k0_26f25a68-0d90-452c-894d-a9d79395889g.jpg)

![](https://wiki.bambulab.com/h2/maintenance/replace-power-safety-key-unit/image-2.png)

### 步骤 5：移除电源安全钥匙底座

1. 使用 H2.0 内六角扳手移除两颗固定螺丝，然后将电源安全钥匙底座取出，将贴在侧边的胶布撕开，将线缆取出；

![](https://wiki.bambulab.com/h2/maintenance/replace-power-safety-key-unit/image-10.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-power-safety-key-unit/image-9.png)

2. 将电源钥匙开关底座与 MC 板转接线断开连接（线缆颜色为黄绿白），将连接线依次从线槽中取出。

![](https://wiki.bambulab.com/h2/maintenance/replace-power-safety-key-unit/image-12.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-power-safety-key-unit/image-1.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-power-safety-key-unit/image-18.png)

## 安装电源安全钥匙组件

### 步骤 1：安装电源安全钥匙底座

1. 将电源安全钥匙底座连接线依次扣入线扣中，并分别与 MC 板转接线连接。

![](https://wiki.bambulab.com/h2/maintenance/replace-power-safety-key-unit/image-28.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-power-safety-key-unit/image-26.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-power-safety-key-unit/image-25.png)

2. 然后将电源安全钥匙底座对准螺丝孔位，使用 H2.0 内六角扳手拧紧两颗固定螺丝，并将线缆用原有的胶布贴在内衬上。

![](https://wiki.bambulab.com/h2/maintenance/replace-power-safety-key-unit/image-27.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-power-safety-key-unit/image-21.png)

### 步骤 2：安装电源开关插座

将电源开关插座与电源安全钥匙底座重新连接后，将电源开关斜着装入（左侧的螺丝孔应插入立柱的后面），并使用 H2.0 内六角扳手拧紧两颗固定螺丝（固定在底座上：ST3x8，固定在右内衬上：BT3x8）；

![](https://wiki.bambulab.com/h2/maintenance/replace-power-safety-key-unit/image-23.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-power-safety-key-unit/image-24.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-power-safety-key-unit/image-22.png)

### 步骤 3：安装地线

顺时针将螺丝轻轻拧在螺丝孔上，然后调整两根地线方向朝向上方，再将螺丝彻底拧紧。  
![安全钥匙地线.jpeg](https://wiki.bambulab.com/h2/maintenance/replace-power-safety-key-unit/%E5%AE%89%E5%85%A8%E9%92%A5%E5%8C%99%E5%9C%B0%E7%BA%BF.jpeg)

### 步骤 4：安装背板和废料滑梯

您可以参考这篇 Wiki 来安装打印机背板和废料滑梯

[更换 H2D 废料滑梯](replace-purge-chute.md)

### 步骤 5：安装电源安全钥匙

将电源安全钥匙插回打印机。

## 如何验证完成/成功

打开打印机电源，检查打印机是否可以正常上电。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 为了确保您安全有效地进行操作，如果对指南中的任何步骤有疑虑或问题，请在开始操作前联系我们的客户服务团队，我们随时乐意为您解答疑问并提供支持。  
> [点击此处联系在线技术支持 （服务时间 9:00-21:00）](https://support.bambulab.cn/cn/im)
