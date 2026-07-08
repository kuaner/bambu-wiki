---
path: zh/a1/maintenance/z-motor-replacement-guide
title: "更换 A1 Z 轴电机指南"
description: "更换 A1 打印机 Z 轴电机的操作步骤"
tags: ["a1"]
created: 2024-09-11T11:28:25.563Z
updated: 2026-06-25T03:02:17.567Z
source: https://wiki.bambulab.com/zh/a1/maintenance/z-motor-replacement-guide
---

## 适用打印机型号

A1

## Z 轴电机

Z 轴电机是安装在打印机底部，用于驱动工具头在 Z 轴方向上移动的步进电机。

## 何时使用

- Z 轴电机烧坏
- 经官方技术支持通过分析日志，确认是 Z 轴电机故障。

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。
>
> 如果您对本指南有任何疑问，请[点击此处联系在线技术支持 （服务时间 9:00-21:00）](hhttps://support.bambulab.cn/cn/im)，我们将及时回复并为您提供所需的帮助。

## 所需工具和材料

- 新的 Z 轴电机（购买链接：请联系售后）
- H2.0 内六角扳手
- 20 分钟

## 移除 Z 轴电机

### **步骤 1：移除 Y 轴上盖**

正放打印机，将 X 轴上移到顶部；

![](https://wiki.bambulab.com/a1/maintenance/replace-z-motor/a1zmotor_(7).jpg)

热床前移到底，移除 Y 轴上盖。

![](https://wiki.bambulab.com/a1/maintenance/replace-z-motor/a1zmotor_(8).jpg)  
![](https://wiki.bambulab.com/a1/maintenance/replace-z-motor/a1zmotor_(9).jpg)

### 步骤 2：拧松 Z 轴皮带张紧螺丝

用 H2.0 内六角扳手，将 Z 皮带张紧螺丝拧松一圈（**请勿完全松开**）。

> Z 轴皮带的张紧螺丝位于底座靠右侧立柱的位置，将热床前移后可以看到。

![](https://wiki.bambulab.com/a1/maintenance/replace-z-motor/a1zmotor_(10).jpg)

### **步骤 3：断开连接线**

向左放倒机器，注意保护好工具头，露出底部理线盒；

![](https://wiki.bambulab.com/a1/maintenance/printer/side_down1.jpg)

依次断开摄像头线、X 轴电机线、Z 轴电机线；拧松 1 颗银色螺丝，滑动线盒断开 USB 数据线；

![](https://wiki.bambulab.com/a1/maintenance/replace-z-motor/a1zmotor_(11).jpg)

使用螺丝刀撬开 Z 电机线缆盖板；

![new1.jpg](https://wiki.bambulab.com/a1/maintenance/replace-z-motor/new2.jpg)

取出线缆。

![new1.jpg](https://wiki.bambulab.com/a1/maintenance/replace-z-motor/new3.jpg)

### **步骤 4：移除底座**

将热床前移，用 H2.0 内六角扳手移除 10 颗螺丝；

![](https://wiki.bambulab.com/a1/maintenance/replace-z-motor/a1zmotor_(12).jpg)

然后将热床向后推到底，用 H2.0 内六角扳手移除 2 颗螺丝；

![](https://wiki.bambulab.com/a1/maintenance/replace-z-motor/a1zmotor_(13).jpg)

最后将底座的一侧抬起，然后移除整个底座。

![](https://wiki.bambulab.com/a1/maintenance/replace-z-motor/a1zmotor_(14).jpg)

### **步骤 5：移除 Z 轴底板**

用 H2.0 内六角扳手移除 8 颗锁立柱螺丝（左右各 4 颗），移除 7 颗锁底板螺丝（中部），移除金属底板。

![](https://wiki.bambulab.com/a1/maintenance/replace-z-motor/a1zmotor_(15).jpg)

> 底板内部突出的螺丝头较为尖锐，部分金属框架上可能存在毛刺。在拆装过程请小心操作，注意规避，或佩戴防割手套进行操作。

|  |  |  |
| --- | --- | --- |
|  |  |  |

### 步骤 6：移除 Z 轴电机

移除线材固定胶布；

> 建议将胶带的一角贴在桌上，后续安装可重复使用。

![](https://wiki.bambulab.com/a1/maintenance/z-axis/tapes_2.jpg)

使用刮刀撬除主动轮上的黑色胶水。

![](https://wiki.bambulab.com/a1/maintenance/replace-z-motor/a1zmotor_(18).jpg)

> 如果主动轮顶部由螺丝限位，只需拧下该螺丝。  
> ![](https://wiki.bambulab.com/a1/maintenance/replace-z-motor/a1zmotor_(16).jpg)

用 H2.0 内六角扳手移除 4 颗螺丝，取下主动轮和 Z 轴电机；

![](https://wiki.bambulab.com/a1/maintenance/z-axis/z_motor_screws.jpg)  
![](https://wiki.bambulab.com/a1/maintenance/z-axis/remove_z_motor.jpg)

## 安装 Z 轴电机

### **步骤 1：提升 X 轴**

将 X 轴提升到顶部位置，并将左右两侧都推到顶部，避免 X 轴偏斜。

![](https://wiki.bambulab.com/a1/maintenance/replace-z-motor/a1zmotor_(7).jpg)

### **步骤 2：安装 Z 轴电机**

将主动轮安装至新的 Z 轴电机上并绕过 Z 轴皮带，确保安装到位；

> 主动轮顶部可涂抹一些**铸工胶**限位。

|  |  |
| --- | --- |
|  |  |

锁入 4 颗螺丝，整理好电缆，用胶带贴附固定。

|  |  |  |
| --- | --- | --- |
|  |  |  |

### **步骤 3：安装 Z 轴底板**

安装底板螺丝。

![](https://wiki.bambulab.com/a1/maintenance/replace-z-motor/a1zmotor_(15).jpg)

### 步骤 4：安装底座

保持龙门架正立状态，将打印机底座安装到龙门架上，注意避让 Z 轴电机线缆；

![](https://wiki.bambulab.com/a1/maintenance/replace-z-motor/a1zmotor_(22).jpg)  
![](https://wiki.bambulab.com/a1/maintenance/replace-z-motor/a1zmotor_(23).jpg)

将热床前移到底，锁入 10 颗螺丝；将热床向后移到底，锁入 2 颗螺丝。

![](https://wiki.bambulab.com/a1/maintenance/replace-z-motor/a1zmotor_(4).jpg)  
![](https://wiki.bambulab.com/a1/maintenance/replace-z-motor/a1zmotor_(13).jpg)

### 步骤 5：连接线缆

向后放倒打印机，将 Z 轴电机线安装到理线盒上;

![new1.jpg](https://wiki.bambulab.com/a1/maintenance/replace-z-motor/new3.jpg)

将理线盒安装在底座上，沿槽位方向滑动理线盒，连接线缆并锁紧 1 颗银色螺丝;

![new1.jpg](https://wiki.bambulab.com/a1/maintenance/replace-z-motor/new1.jpg)

### 步骤 6：安装 Y 轴上盖

正放打印机，将热床前移到底，将 Y 轴上盖从热床底下穿过，并向前推到底，对齐卡扣，将 Y 轴上盖安装到位。

|  |  |
| --- | --- |
|  |  |

特别说明：如果热床没有前移到底，Y 轴上盖可能卡不对位置，这时可以手动扶正 Y 轴上盖，协助 Y 轴上盖的安装。

![](https://wiki.bambulab.com/a1/maintenance/replace-z-motor/a1zmotor_(6).jpg)

### 步骤 7：张紧 Z 皮带

1：打开打印机电源，进入打印机运动控制界面，执行一次回零。

![](https://wiki.bambulab.com/a1/maintenance/lead-screw-kit-replacement/screen4.png)

2：等待回零完成后，先后点击右侧的向上/方向键 1 次，使 X 轴沿 Z 轴方向上下分别移动 1 次。

> 向下移动 X 轴前，请确保喷嘴不会撞击到热床！

![](https://wiki.bambulab.com/a1/maintenance/lead-screw-kit-replacement/screen6.png)

3：用 H2.0 内六角扳手拧紧 2 颗张紧螺丝。

![](https://wiki.bambulab.com/a1/maintenance/replace-z-motor/a1zmotor_(10).jpg)

## 设备校准

在校准页面，仅选择振动补偿，点击开始。

请执行此步骤以确保打印机正常工作。

|  |  |
| --- | --- |
|  |  |

## 结束语

> 我们希望这份指南为您提供了有效的信息，并真实地帮助了您。
>
> 如果您对本文中描述的过程有任何疑虑或疑问，您可以在开始操作前联系我们的客户服务团队。 我们随时准备为您提供帮助并回答您的任何问题。
>
> [点击此处联系在线技术支持 （服务时间 9:00-21:00）](https://support.bambulab.cn/cn/im)
