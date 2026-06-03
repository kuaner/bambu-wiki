---
path: zh/ams-ht/maintenance/disassembly-and-assembly-of-the-motherboard
title: "AMS HT 主板更换指南"
description: "本文将详细为您讲述 AMS HT 更换步骤和注意事项。"
tags: []
created: 2025-06-16T10:22:01.042Z
updated: 2025-06-23T02:59:16.295Z
source: https://wiki.bambulab.com/zh/ams-ht/maintenance/disassembly-and-assembly-of-the-motherboard
---

![](https://wiki.bambulab.com/ams-ht/disassembly-and-assembly/ams-ht-motherboard.png)

AMS HT 主板是 AMS HT 单元的核心部件，负责管理传感器、电机、烘干组件与打印机之间的通信。

## 所需工具与材料

在开始之前，请确保您已准备好以下物品：

- 内六角扳手： 用于拆卸螺丝。
- 螺丝收纳盒： 用于妥善整理和存放拆下的螺丝，以防丢失。
- 替换用 AMS HT 主板（如果需要更换）： 您可以在 Bambu Lab 官方商店 购买。

## 安全提示

> **重要提醒 ！**  
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。  
> 如果您对本指南有任何疑问，请[点击这里提交工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)，我们将及时回复并为您提供所需的帮助。

## 移除 AMS HT 主板

### 断开 AMS HT 单元并移除 PTFE 管

断开 AMS HT 6 pin 连接线和电源线。接下来，按下位于 AMS HT 背部的 PTFE 管释放按钮以解锁连接器，拔出 PTFE 管。

![](https://wiki.bambulab.com/ams-ht/motherboard/disconnect-the-tube.png)

### 移除 AMS HT 中框

使用H2.0内六角螺丝刀，移除底部的两颗螺丝（BT3x8），它们用于固定 AMS 外壳的下部。小心地将螺丝放在安全的地方，以便稍后重新组装时使用。

![](https://wiki.bambulab.com/ams-ht/motherboard/bottom-screws.png)

如下图所示，缓慢向上提起中框组件，请务必缓慢操作，内部有线缆连接。

|  |  |
| --- | --- |
|  |  |

断开屏幕连接器锁扣并拔下线缆

![](https://wiki.bambulab.com/ams-ht/motherboard/connector-latch.png)

断开通信和电源线缆

![](https://wiki.bambulab.com/ams-ht/motherboard/signal-and-power-cables.png)

按下卡扣然后拔出线缆接头。

![](https://wiki.bambulab.com/ams-ht/motherboard/removing-cables.png)

拔下电源插座到主板的线缆

![](https://wiki.bambulab.com/ams-ht/motherboard/power-sockeyt.png)

向下按压解锁卡扣以解锁固定线缆的卡扣。一旦卡扣松开，即可拔出连接器以断开线缆。

![](https://wiki.bambulab.com/ams-ht/motherboard/pressing-unclock-clatch.png)

避免使用过大的力气，以防损坏连接器插针或主板。

### 取出 AMS HT 主板

拧松三颗主板固定螺丝（BT2x5）。缓慢将主板从中框上推出。

|  |  |
| --- | --- |
|  |  |

如下图所示，断开主板右侧 4 根线缆。

![](https://wiki.bambulab.com/ams-ht/motherboard/disconnecting-cables.png)

接下来，断开底部的五根线缆。

![](https://wiki.bambulab.com/ams-ht/motherboard/removing-cables-at-the-bottom.png)

断开加热器线缆,首先需要拨开线缆接头的绝缘橡胶套。

![](https://wiki.bambulab.com/ams-ht/motherboard/disconnecting-heater-cable.png)

取下橡胶套后，找到并按下解锁卡扣以释放锁定机制。卡扣松开后，从插座中轻轻拔出线缆，注意不要直接拉扯电线。

![](https://wiki.bambulab.com/ams-ht/motherboard/pulling-out-cables.png)

移除线缆固定螺丝（BT3x5）。

![](https://wiki.bambulab.com/ams-ht/motherboard/taking-out-the-motherboard.png)

将主板和剩余线缆一起从中框上移除。

![](https://wiki.bambulab.com/ams-ht/motherboard/removing-the-motherboard.png)

我们已成功从AMS HT上拆下主板。以下是该部件的各个部分。

![](https://wiki.bambulab.com/ams-ht/motherboard/parts-of-the-motherboard.png)

|  |  |  |
| --- | --- | --- |
| 1. 退料回转电机 | 2. 开盖霍尔板 | 3. 里程轮板 |
| 4. 3520 内部助力电机 | 5. LCD 屏幕 | 6. 温湿度传感器 |
| 7. 烘干组件温度传感器 | 8. 主板电源线 | 9. 出料口霍尔板 |
| 10. RFID 线圈 | 11. 主板通讯线 | 12. 烘干组件涡流风扇 |
| 13. 主板 AC 电源输入 | 14. 烘干组件 AC 输入 |  |

在开始重新组装或更换主板之前，注意对主板进行检查：

- 检查烧毁的组件： 寻找变黑的区域、熔化的塑料或烧焦的电路痕迹。这些迹象可能表明存在短路或组件故障，可能会影响整体性能。
- 检查连接器是否损坏： 轻轻检查每个连接器是否有松动或物理破损。

## 安装 AMS HT 主板

> 在正式安装前，需要将旧主板上三根线缆拔出，安装至新的主板上。

如果下图所示，连接主板侧边线缆。

![](https://wiki.bambulab.com/ams-ht/motherboard/connecting-cables.png)

确保每根线缆都正确对齐并牢固地插入其连接器中，听到或感觉到轻微的“咔嗒”声，表示连接稳固。

接口对应如下：

1. 退料回转电机
2. 开盖霍尔板
3. 里程轮板
4. 3520内部助力电机

![](https://wiki.bambulab.com/ams-ht/motherboard/inserting-cables.png)

插入以上四根线缆后，接着按顺序连接另外五根线缆：

1. 温湿度传感器
2. 烘干组件温度传感器
3. 出料口霍尔板
4. RFID 线圈
5. 烘干组件涡流风扇

![](https://wiki.bambulab.com/ams-ht/motherboard/connecting-five-cables.png)

安装完成后可以，轻轻拉一下线缆，确保连接牢固。

![](https://wiki.bambulab.com/ams-ht/motherboard/tagging-cables.png)

将加热器线缆接头对准引脚并轻轻推入，直到听到或者感觉到“咔嗒”声，确保连接牢固。

连接后，将绝缘套安装回线缆接头上。

![](https://wiki.bambulab.com/ams-ht/motherboard/hearter-cable.png)

### 安装主板到中框组件

缓慢地将主板插入固定槽中。接下来锁紧三颗固定螺丝（BT2x5）。

![](https://wiki.bambulab.com/ams-ht/motherboard/inserting-the-motherboard.png)

> 避免过度拧紧，以防损坏电路板或滑丝。

接下来整理尾部中框线缆。先将4根较细的线缆放置在底部，再把较粗的主板通讯线压在这 4 根细线缆上方，之后安装固定片并锁紧螺丝（BT3x5）。

![](https://wiki.bambulab.com/ams-ht/motherboard/organizing-rear-cables.png)

![](https://wiki.bambulab.com/ams-ht/motherboard/screwing-to-hold-cables-in-place.png)

将 AMS HT 单元旋转180° 整理前部线缆。

![](https://wiki.bambulab.com/ams-ht/motherboard/organizing-front-cables.png)

如果下图所示将线缆整理至理线槽内。

![](https://wiki.bambulab.com/ams-ht/motherboard/front-cables.png)

### 安装中框组件

在此步骤我们需要连接上下料器至出料组件的特氟龙管。

![](https://wiki.bambulab.com/ams-ht/motherboard/connecting_the_ptfe_tube.png)

如下图所致连接 1、2 号位的线缆。其中1号位为主板通讯线（14pin），2号位为主板电源线（2pin）。

![](https://wiki.bambulab.com/ams-ht/motherboard/connecting-the-cables-remaining.png)

将电源插座线缆插接在主板上并安装好绝缘橡胶套。

![](https://wiki.bambulab.com/ams-ht/motherboard/connecting-power-socket-cable.png)

> 注意：此处连接不区分正负极。

连接 AMS HT 前端屏幕线缆，连接完成后需要注意将线缆卡入理线槽内。

![](https://wiki.bambulab.com/ams-ht/motherboard/connecting-front-screen-cable.png)

接下来，用手指轻轻钩住并固定凸出的线缆，将中框组件安装至下盖组件内。

![](https://wiki.bambulab.com/ams-ht/motherboard/holding-protruding-cables.png)

需要确保中框组件完全压入下壳组件且前后没有翘起的情况。

![](https://wiki.bambulab.com/ams-ht/motherboard/mountaing-the-frame.png)

安装底部两颗固定螺丝（BT3x8）。

![](https://wiki.bambulab.com/ams-ht/motherboard/securing-the-frame.png)

### 插入 AMS HT 背面特氟龙料管

最后将特氟龙管从 AMS TH 尾部推入。装完后，拉动特氟龙管，确认特氟龙管已固定。

![](https://wiki.bambulab.com/ams-ht/motherboard/installing_the_ptfe_tube.png)

## 功能验证

将电源线连接妥当，把 AMS HT 设备与打印机进行对接。接通电源后，通过操作打印机显示屏上的相应界面，依次启用 AMS HT 的烘干功能和上料功能。

若烘干功能可正常开启，且设备能按预设升温至目标温度，则判定烘干组件工作正常。

接下来，对上料功能展开测试。确认整个上料流程正常且未出现任何错误提示。若上述测试均顺利通过，则表明 AMS HT 主板更换操作成功完成。

否则，请检查所有内部线缆连接，然后重试。如果问题仍然存在，请联系 Bambu Lab 技术支持团队寻求进一步帮助。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南并未解决您的问题，[*请点击此处联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
