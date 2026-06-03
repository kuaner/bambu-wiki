---
path: zh/ams-2-pro/maintenance/replace-internal-hub-unit
title: "更换 AMS 2 Pro 五通组件和内部五通组件马达"
description: "本文介绍了如何更换 AMS 2 Pro 五通组件和内部五通组件马达"
tags: []
created: 2025-03-25T01:36:59.898Z
updated: 2026-05-21T02:39:11.564Z
source: https://wiki.bambulab.com/zh/ams-2-pro/maintenance/replace-internal-hub-unit
---

## AMS 2 Pro 五通组件

AMS 2 Pro 五通组件是送料（4进1出）装置，根据当前选用的材料位置，开通对应的进料口，并辅助将耗材丝输送至打印机，同时也具有辅助将已送至打印机的耗材丝拉回 AMS 2 Pro 的功能。

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-internal-hub-unit/image-14.png)

## AMS 2 Pro 内部五通组件马达

AMS 2 Pro 内部五通组件马达用于为 AMS 2 Pro 五通组件的运行提供动力。

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-internal-hub-unit/image-13.png)

AMS HT 的上下料电机与其型号一致，如您需要为 AMS HT 更换上下料电机，可参考[该Wiki](../../amsht/maintenance/replace-feeder-unit.md)

## 何时使用

- 所有 PTFE 料管检查正常且连接良好，但打印材料仍经常性卡在 AMS 2 Pro 五通组件中。
- 经过售后技术支持的判断，确认是AMS五通组件的故障。

## 所需工具和材料

- 新的 AMS 2 Pro 五通组件
- H2.0 内六角扳手
- 约 20 分钟

### 螺丝清单

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。
>
> 如果您对本指南有任何疑问，请[点击这里提交工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)，[点击此处联系在线技术支持 （服务时间 9:00-21:00）](https://support.bambulab.cn/cn/im)，我们将及时回复并为您提供所需的帮助。

在开始操作之前，请确认 AMS 2 Pro 已经从打印上断开连接。

## 拆除五通组件及电机

### 步骤 1 - 拆下 AMS 2 Pro 背面的 PTFE 料管

从 AMS 2 Pro 背面按压料管释放按钮，解锁接头，然后拉出 PTFE 料管。

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-internal-hub-unit/image.png)

### 步骤 2 - 抽出料管释放按钮

从下盖内部捏住图示卡扣自动弹开料管释放按钮后，从 AMS 2 Pro 的背面将其抽出。

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-internal-hub-unit/image-1.png)

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-internal-hub-unit/image-2.png)

> 捏卡扣时，另一只手需要用从 AMS 2 Pro 的背面扶住料管释放按钮，以避免弹簧被弹出丢失。

### 步骤 3 - 取出 AMS 2 Pro 主框架组件

拆下中间 2 个料槽的从动支撑套筒组件以露出 2 个螺丝孔，取出轴承套时，小心保存避免丢失。

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-internal-hub-unit/image-7.png)

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-internal-hub-unit/image-9.png)

移除固定 AMS 2 Pro 主框架上的 2 颗螺丝。

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-internal-hub-unit/image-12.png)

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-internal-hub-unit/image-11.png)

将主框架后部完全提起来， 竖立放置在 AMS 2 Pro 下盖上，**注意此时仍有电缆连接，请勿暴力操作**。抬起时，建议先抬主框架前部分，再往前推一推，为框架后部分腾出空间。

> 竖放 AMS 2 Pro 主框架时需避开风门的电子部件，以防压坏。

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-internal-hub-unit/image-6.png)

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-internal-hub-unit/image-4.png)

解锁插头的卡扣，拔出 AMS 2 Pro 电源板上的信号连接线和电源连接线，整体抬出主框架组件。

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-internal-hub-unit/image-5.png)

> ℹ️**注意:** 拔连接线时需要按紧插头的卡扣，卡扣位置如下图所示。  
> ![tabs.png](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-internal-hub-unit/tabs.png)

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-internal-hub-unit/image-8.png)

### 步骤 4 **- 断开 4 条 PTFE 管**

依次按下快速接头上的按钮，解锁连接并断开 4 条PTFE 管。

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-internal-hub-unit/image-10.png)

### 步骤 5 - 移除五通组件

拔出 3 颗螺丝，然后将抽出五通组件，断开电机电缆、霍尔电缆和里程测速电缆3个插头。

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-internal-hub-unit/image-3.png)

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-internal-hub-unit/image-28.png)

取下五通后，注意收好 2 根防震硅胶垫，防止遗失。

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-internal-hub-unit/image-24.png)

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-internal-hub-unit/image-29.png)

### **步骤 6 - 移除 AMS 2 Pro 内部五通组件电机**

移除 2 颗螺丝，然后取下内部五通组件电机。取出电机时，建议将挤出轮和轴承一并取出放好，防止丢失。

在设定备件物料时，该挤出轮和轴承已包含在挤出电机单品和五通组件中。

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-internal-hub-unit/image-22.png)

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-internal-hub-unit/image-27.png)

## 安装五通组件及电机

### 步骤 1 **- 安装 AMS 2 Pro 内部五通组件电机**

将挤出齿轮按照正确的平面方向，套在挤出电机上。

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-internal-hub-unit/image-17.png)

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-internal-hub-unit/image-21.png)

将轴承装回到五通组件的槽位中，再将挤出电机按照螺丝孔位，装回到五通组件上，拧入2颗螺丝。

安装挤出电机时，需要注意方向，确保电机插头方向朝上，指向主板。

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-internal-hub-unit/image-16.png)

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-internal-hub-unit/image-18.png)

### 步骤 2 **- 安装五通组件**

安装防震垫片，将垫片的凹槽对准五通的边。

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-internal-hub-unit/image-20.png)

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-internal-hub-unit/image-19.png)

装回五通时，另一只手可从反面拨开PTFE管，便于将五通卡到位，对准螺丝孔。安装时，需关注五通的防震硅胶条，防止遗漏。

拧入 3 颗螺丝后，插回电机电缆、霍尔电缆和里程测速电缆3个插头，并整理好线缆。

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-internal-hub-unit/image-25.png)

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-internal-hub-unit/image-15.png)

### 步骤 3 - 连接 4 根 PTFE 管

依次将 4 根 PTFE 管连接至五通组件。

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-internal-hub-unit/image-23.png)

### 步骤 4 - 安装主框架组件与从动支撑套筒组件

将 AMS 2 Pro 主框架组件装入AMS下盖，将信号电缆和电源电缆连接到 AMS 2 Pro 电源板。

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-internal-hub-unit/image-26.png)

![20250325-131650.jpg](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-power-board/20250325-131650.jpg)

将下盖组件舌位对准中框卡槽，然后插入安装。

![screenshot-20250519-161423.png](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-heating-unit/screenshot-20250519-161423.png)

AMS 2 Pro 主框架安装到位后，锁入 2 颗螺丝固定。

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-internal-hub-unit/image-42.png)

安装中间 2 个从动支撑套筒组件，确保所有从动轴两端的轴承被按压到位。

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-internal-hub-unit/image-40.png)

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-internal-hub-unit/image-41.png)

### 步骤 5 - 安装料管释放按钮

按照如下方向，将料管释放按钮压回外壳中，将卡扣顺利卡入对应卡槽，并保持黑色硅胶外壳平整嵌入。

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-internal-hub-unit/image-44.png)

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-internal-hub-unit/image-38.png)

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-internal-hub-unit/image-39.png)

### 步骤 6 - 连接铁氟龙料管

检查确认铁氟龙管管硅胶支架与五通组件的料孔对齐，并从 AMS 2 Pro 后部推入铁氟龙料管。装完后，拉动铁氟龙料管，确认铁氟龙管已固定。

|  |  |
| --- | --- |
|  |  |

## 设备校准

连接电源线，将 AMS 2 Pro 连接到打印机，打开电源，通过机器显示屏的操作，开始使用 AMS 2 Pro 上料，如果能完成上料动作并且整个上料过程没有出现错误提示，则更换成功。

否则，请检查所有连接，然后重试。如果问题仍然存在，请联系Bambu Lab服务团队寻求进一步帮助。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 为了确保您安全有效地进行操作，如果对指南中的任何步骤有疑虑或问题，请在开始操作前联系我们的客户服务团队，我们随时乐意为您解答疑问并提供支持。  
> [点击此处联系在线技术支持 （服务时间 9:00-21:00）](https://support.bambulab.cn/cn/im)
