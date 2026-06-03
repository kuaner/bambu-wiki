---
path: zh/ams-2-pro/maintenance/replace-power-board
title: "更换 AMS 2 Pro 电源板"
description: "本文介绍了如何更换 AMS 2 Pro 电源板"
tags: []
created: 2025-03-25T01:29:37.045Z
updated: 2025-06-17T02:52:51.126Z
source: https://wiki.bambulab.com/zh/ams-2-pro/maintenance/replace-power-board
---

## 适用打印机型号

AMS 2 Pro（后文简写为AMS）

## AMS 2 Pro 电源板

AMS 电源板是一块安装在AMS后部的电路板，它负责接收打印机输出的直流电源，并将电源传输到 AMS 主板，同时也担负一定的通信转接功能。

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-power-board/image-14.png)

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-power-board/image-10.png)

## 何时使用

1. AMS 接口板的电源输出正常，bambu 总线电缆4pin/6pin的连接也正常，但AMS却不能正常启动；
2. AMS 电源板有明显烧坏的现象；
3. AMS 电源板上的连接器或元器件损坏。

## 所需工具和材料

- 新的 AMS 2 Pro 电源板
- H2.0 内六角扳手
- H1.5 内六角扳手
- 15 分钟

### 螺丝清单

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。
>
> 如果您对本指南有任何疑问，请[点击这里提交工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)，[点击此处联系在线技术支持 （服务时间 9:00-21:00）](https://support.bambulab.cn/cn/im)，我们将及时回复并为您提供所需的帮助。

在开始操作之前，请确认AMS已经从打印机上断开连接。

## 拆除电源板

### 步骤 1 - 拆下AMS背面的铁氟龙管

从AMS背面按压铁氟龙料管释放按钮，解锁接头，然后从AMS背面拉出铁氟龙管。

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-power-board/image-11.png)

### 步骤 2 - 抽出铁氟龙料管释放按钮

从下盖内部捏住卡扣自动弹开铁氟龙料管释放按钮后，从AMS的背面抽出铁氟龙料管释放按钮。

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-power-board/image.png)

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-power-board/image-1.png)

捏卡扣时，另一只手需要用从AMS的背面扶住铁氟龙料管释放按钮，以避免弹簧被弹出丢失。

### 步骤 3 - 取出AMS主框架组件

拆下中间2个料槽的从动支撑套筒组件以露出2个螺丝孔，取出轴承套时，小心两端的轴承，避免丢失。

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-power-board/image-9.png)

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-power-board/image-6.png)

移除固定AMS主框架上2颗螺丝A。

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-power-board/image-12.png)

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-power-board/image-13.png)

将主框架后部完全提起来， 竖立放置在AMS下盖上，**注意有电缆连接，请勿暴力操作**；抬起时，建议先抬主框架前部分，再往前推一推，为框架后部分让出空间。

竖放AMS主框架时需避开风门的电子部件，以防压坏。

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-power-board/image-8.png)

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-power-board/image-4.png)

解锁插头的卡扣，拔出AMS电源板上的信号连接线和电源连接线，整体抬出AMS主框架组件。

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-power-board/image-5.png)

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-power-board/image-7.png)

### 步骤 4 - 移除电源板

拔掉2个进风口模块插头，拧下3颗螺丝，取下电源板。

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-power-board/image-2.png)

## 安装电源板

### 步骤 1 - 安装电源板

将电源板对准 AMS 背面的插孔孔位后，往前推，将6pin插孔和螺丝的孔位对齐后，锁紧电源板的3 颗螺丝B，并插回2个进气口和出气口模块的风门插头。

**注意：电源板的背面有一个硅胶垫片，切勿忘记嵌入。**

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-power-board/image-3.png)

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-power-board/image-23.png)

### 步骤 2 - 安装主框架组件与从动支撑套筒组件

将AMS主框架组件装入AMS下盖，连接信号电缆和电源电缆连接到AMS电源板。

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-power-board/image-27.png)

![20250325-131650.jpg](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-power-board/20250325-131650.jpg)

将下盖组件舌位对准中框卡槽，然后插入安装。  
![screenshot-20250519-161423.png](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-heating-unit/screenshot-20250519-161423.png)

AMS主框架安装到位后，锁入2颗螺丝固定。

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-power-board/image-28.png)

安装中间2个从动支撑套筒组件，确保所有从动轴两端的轴承都按压到位。

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-power-board/image-22.png)

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-power-board/image-24.png)

### 步骤 3 - 安装铁氟龙料管释放按钮

按照如下方向，将铁氟龙料管释放按钮压回外壳中，将卡扣顺利卡入对应的卡槽中，并保持黑色硅胶外壳平整嵌入。

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-power-board/image-21.png)

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-power-board/image-29.png)

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-power-board/image-25.png)

### 步骤 4 - 连接铁氟龙管

检查确认铁氟龙管硅胶支架与五通组件的料孔对齐，并从AMS后部推入铁氟龙管。装完后，拉动铁氟龙管，确认铁氟龙管已固定。

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-power-board/image-20.png)

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-power-board/image-24.png)

## 设备校准

连接电源线，将 AMS 连接到打印机，打开电源，通过机器显示屏的操作，开始使用 AMS 上料，如果能完成上料动作并且整个上料过程没有出现错误提示，则更换成功。

否则，请检查所有连接，然后重试。如果问题仍然存在，请联系 Bambu Lab 服务团队寻求进一步帮助。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 为了确保您安全有效地进行操作，如果对指南中的任何步骤有疑虑或问题，请在开始操作前联系我们的客户服务团队，我们随时乐意为您解答疑问并提供支持。  
> [点击此处联系在线技术支持 （服务时间 9:00-21:00）](https://support.bambulab.cn/cn/im)
