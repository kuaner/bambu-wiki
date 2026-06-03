---
path: zh/h2/maintenance/replace-power-socket
title: "更换 H2 系列电源开关插座"
description: "本文介绍了如何更换 H2 系列电源开关插座"
tags: []
created: 2025-03-25T03:46:43.514Z
updated: 2026-03-13T03:21:13.688Z
source: https://wiki.bambulab.com/zh/h2/maintenance/replace-power-socket
---

> **注意**：本页面以 H2D 机器为例。**H2S 和 H2C 的更换步骤完全相同**。

## 电源开关插座

电源开关组件是安装在 H2D 打印机背面左下角的一个模块。它包含一个电源线插座、一个控制打印机电源的开关以及用于连接打印机电源、交流电板和地线的电缆。

**电源开关的备件包含以下：**

1. 电源开关插座 \* 1
2. 螺丝 - 用于固定电源开关 \* 1
3. 螺丝 - 用于固定地线 \* 1

## 何时更换

- 开关损坏
- 连接线缆损坏
- 开关座接触不良

## 所需的工具和材料

- 新的电源开关插座
- H2.0 内六角扳手

**更换 H2D 电源开关插座所涉及的螺丝规格及数量（建议妥善保管拆下的螺丝，避免丢失）：**

| **螺丝规格** | **螺丝图片** | **用途** | **位置示意图** |  | **螺丝数量** |
| --- | --- | --- | --- | --- | --- |
| BT3x8 |  | 用于固定背板（绿色方框标记） |  |  | 12 |
|  |  | 用于固定废料滑梯 |  |  | 1 |
|  |  | 用于固定电源开关插座 |  |  | 1 |
|  |  | 用于固定 AC 板理线盖 |  |  | 1 |
| ST3x8 |  | 用于固定背板（红色圆圈标记） |  |  | 11 |
|  |  | 用于固定电源开关插座 |  |  | 1 |
| ST3x12 |  | 用于固定料盘支架底座（黄色方框标记） |  |  | 2 |
| BT3x12 |  | 用于固定线扣 |  |  | 2 |
| STW3x5 |  | 用于固定地线（红色圆圈标记） |  |  | 1 |

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。
>
> 如果您对本指南有任何疑问，[*请联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)，我们将及时回复并为您提供所需的帮助。

## 移除电源开关

### 步骤 1：移除背板\废料滑梯\AC 板理线盖

您可以参阅这篇 Wiki 来依次移除

1. 背板
2. 废料滑梯
3. AC 板理线盖

由于更换电源开关插座不涉及 AC 板的拆装，因此您可忽略更换 AC 板的步骤：

[更换 H2D AC 板/AC 板理线盖](replace-ac-board-for.md)

### 步骤 2：移除电源开关

1. 向上扣开电源线的保护盖，然后使用十字螺丝刀拧松拧松螺丝，将三根电源线向下抽出；

![](https://wiki.bambulab.com/h2/maintenance/replace-power-socket/image-9.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-power-socket/image-10.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-power-socket/image-11.png)

- 使用 H2.0 内六角扳手拧松两颗线缆卡扣固定螺丝（BT3x12），打开左内衬中的线缆卡扣，然后将电源开关线缆从线扣中取出；

![](https://wiki.bambulab.com/h2/maintenance/replace-power-socket/image-12.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-power-socket/image-13.png)

- 使用 H2.0 内六角扳手拧松两颗电源开关固定螺丝（红色方框：ST3x8；绿色圆圈：BT3x8），将电源开关斜着从内衬中抽出，然后按下卡扣与电源安全钥匙底座断开连接；

![](https://wiki.bambulab.com/h2/maintenance/replace-power-socket/image-14.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-power-socket/img_v3_02k0_26f25a68-0d90-452c-894d-a9d79395889g.jpg)

![](https://wiki.bambulab.com/h2/maintenance/replace-power-socket/image-15.png)

- 向上扣开电源下方的透明保护盖，使用十字螺丝刀拧松下图所示的三颗螺丝，将线缆向下抽出，并使用 H2.0 内六角扳手拧松一颗地线固定螺丝（STW3x5），最后将线缆从线扣中取出即可。

![](https://wiki.bambulab.com/h2/maintenance/replace-power-socket/image-16.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-power-socket/image-17.png)

## 安装电源开关

### 步骤 1：装回电源开关

1. 将电源开关插座与电源安全钥匙底座重新连接后，将电源开关斜着装入（左侧的螺丝孔应插入立柱的后面），并使用 H2.0 内六角扳手拧紧两颗固定螺丝（红色方框：ST3x8；绿色圆圈：BT3x8）；

![](https://wiki.bambulab.com/h2/maintenance/replace-power-socket/image-18.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-power-socket/image-19.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-power-socket/image-20.png)

- 参考整理线缆，将线缆卡入内衬的线扣中，然后将电源开关线缆与电源连接，用十字螺丝刀拧紧螺丝后扣紧保护盖，再使用 H2.0 内六角扳手拧紧一颗地线螺丝（STW3x5）；

![](https://wiki.bambulab.com/h2/maintenance/replace-power-socket/image-21.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-power-socket/image-22.png)

- 然后将电源开关线缆卡在线扣下方，并拧紧左内衬内侧线缆卡扣的两颗固定螺丝（BT3x12），最后与 AC 板连接，使用十字螺丝刀拧紧螺丝后扣紧保护盖。

![](https://wiki.bambulab.com/h2/maintenance/replace-power-socket/image-23.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-power-socket/image-24.png)

### 步骤 2：安装 AC 板理线盖\废料滑梯\背板

您可以参阅下面的这篇 Wiki 依次安装：

1. AC 板理线盖；
2. 废料滑梯；
3. 背板

[更换 H2D AC 板/AC 板理线盖](replace-ac-board-for.md)

## 如何验证完成/成功

打开打印机电源，检查打印机是否可以正常上电。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南未解决您的问题，[*请联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
