---
path: zh/a1/troubleshooting/circuit-fault
title: "打印机电路故障排查 - A1"
description: "A1 电路相关故障排查方法"
tags: []
created: 2025-02-09T02:51:40.456Z
updated: 2026-05-27T09:02:14.615Z
source: https://wiki.bambulab.com/zh/a1/troubleshooting/circuit-fault
---

## 何时使用

当设备出现以下几种情况时，请参考本文内容进行故障排查。

- **接通电源后，打印机电源指示灯不亮；**
- **接通电源后，打印机电源指示灯正常，屏幕不亮，并且软件显示该设备离线；**

## 排查须知

在开始正式的故障排查之前首先需要了解主板指示灯、工具头指示灯、HMS指示灯、电源模块指示灯的状态情况。

### 正常状态：TH 板指示灯绿灯常亮

观察工具头指示灯需要打开工具头后盖。请拉住后盖底部，小心撬开。

<https://public-cdn.bblmw.com/wiki/video/A1M-TH.mp4>

### 正常状态：MC 指示灯绿灯每 5 秒闪烁一次

<https://public-cdn.bblmw.com/wiki/video/A1-MC.mp4>

### 正常状态：AP 指示灯绿灯每 1 秒闪烁一次

<https://public-cdn.bblmw.com/wiki/video/A1-AP.mp4>

### 正常状态：电源模块指示灯绿灯常亮

您需要先参考[更换电源模块](../maintenance/power-supply-replacement-guide.md)，拆下打印机底板，才能观察到电源模块指示灯。

![](https://wiki.bambulab.com/a1/troubleshooting/circuit-fault/power_light1.jpg)

## 安全提示

> **重要提醒 ！**  
> 本篇故障排查指南存在较多接头的插拔，在对打印机及其电子设备（包括工具头线缆）进行任何维护或插拔接头工作之前，请关闭打印机电源并断开电源连接，以避免带电操作发生电路短路从而引起额外的电子设备损坏和安全隐患。**插拔完成后，再开启打印机电源并观察指示灯状态，此时只需观察指示灯状态，请勿直接触碰线缆插头。**  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。  
> 如果您对本指南有任何疑问，请[点击这里提交工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)，我们将及时回复并为您提供所需的帮助。

## 所需工具

- H2.0 内六角扳手
- H1.5 内六角扳手
- PH2 十字螺丝刀
- 镊子
- 万用表（非必须）

## 电源开关指示灯熄灭

市电接入设备并按下开关后，电源开关的白色指示灯将自动亮起。如果开关的白色指示灯无法点亮，说明电源线故障或电源开关存在故障。

![](https://wiki.bambulab.com/a1/troubleshooting/circuit-fault/20250209-102005.jpg)

### 步骤一：电源线故障

打印机的电源线使用标准插头，请使用同一类型的电源线通电测试。开机观察白色指示灯是否亮起。若指示灯恢复正常，则说明电源线故障，需要更换新电源线。

### 步骤二：保险丝熔断或开关故障

开关内部装有 250V 6A 保险丝，您可以使用镊子撬出保险丝安装座。由于部分保险丝外壳不透明，无法直接观察熔丝状态，可借助万用表或其他方式进行检测。

![](https://wiki.bambulab.com/x1/maintenance/replace-fuse/350px-gap.png)

如果您的手机支持**多点触碰**，那么屏幕类型为“电容屏”。您就可以用手指捏住保险丝的一端，使用另一端触碰手机屏幕，观察屏幕是否能够被点击。如果可以的话那么保险丝就是正常的。

![12.webp](https://wiki.bambulab.com/p2s/troubleshooting/p2s-circuit-fault-template/12.webp)

将万用表拨至蜂鸣档（或电阻档），表笔分别接触保险丝两端的金属帽：若有**蜂鸣声**或**电阻值接近 0 Ω**，表示**保险丝正常**；若无蜂鸣声、显示“OL”（开路）或电阻值很大，则说明保险丝已熔断，需要更换新的开关插座。您可以参考 [如何使用万用表检测电路是否正常](../../knowledge-sharing/multimeter.md)了解万用表的基本使用方式。

## 电源开关指示灯亮起

电源开关指示灯能够正常亮起，那么屏幕不亮，并且软件显示该设备离线的情况就和 AP(MC) 板模块、TH 板模块、电源模块故障或短路有关。

> **排查方式：** 如果在断开某个特定的连接器后，其余电路的指示灯恢复正常，则表明连接到该接口的模块存在故障。而断开某主板上所有连接器后，该主板的指示灯依然没有恢复正常，则说明该主板存在故障。

### AP/MC/TH 指示灯均熄灭

打印机主板的输入电压为 24V，由电源模块提供。如果电源模块输出/输入异常，将导致主板无法通电，从而引起所有的指示灯无法点亮。

1. 参考[更换电源模块](../maintenance/power-supply-replacement-guide.md)，拧松下图 #1 #2 螺丝取出主板供电线缆，重启后若指示灯存在异常，则需要**更换新的电源模块**。
2. 若移除主板供电线缆之后，电源指示灯恢复正常，说明电源模块没有故障，请**继续后续排查**。

|  |  |
| --- | --- |
|  |  |

### AP/MC/TH 指示灯均异常（AP/MC 板模块排查）

flowchart TD
B[先断开 TH 板上的 USB-C 插头] --> C[开机观察灯语]
C --> D{AP 或 MC 指示灯<br/>是否恢复正常?}
D -- 是 --> E[故障原因在 TH 板模块上<br>进一步排查 TH 板模块]
D -- 否 --> G[故障原因在 AP 或 MC 板模块上]
G --> H[参考更换主板教程<br/>移除主板上的所有模块插头及 SD 卡]
H --> I[开机观察指示灯]
I --> J{指示灯是否恢复正常?}
J -- 是 --> K[逐个安装每个模块的插头及 SD 卡]
K --> L{安装某个模块后<br/>指示灯是否变为异常?}
L -- 是 --> M[更换该模块]
L -- 否 --> N[继续逐个安装并确认]
J -- 否 --> O[更换主板]
classDef proc fill:#dae8fc,stroke:#6c8ebf,color:#000;
classDef decision fill:#fff2cc,stroke:#d6b656,color:#000;
class B,C,E,G,H,I,K,N,O,M,F,L proc;
class D,J,L decision;

如果您观察到 AP/MC 指示灯存在异常，请先断开 TH 板上的 USB-C 插头，再开机观察灯语。

![](https://wiki.bambulab.com/a1/maintenance/toolhead-board/remove_the_usb_c_cable_of_a1.jpeg)

1. 若AP(MC) 指示灯恢复正常，则故障原因在 TH 板模块上，请进一步排查 TH 板模块。
2. 若AP(MC) 指示灯依旧异常，则故障原因在 AP(MC) 板模块上。参考 [更换主板](../maintenance/mainboard-replacement-guide.md) 教程，移除主板上的所有模块插头**以及 SD 卡**，开机观察指示灯是否恢复正常：

   ![](https://wiki.bambulab.com/a1/troubleshooting/circuit-fault/mc_light_-_%E5%89%AF%E6%9C%AC.jpg)

   - 若恢复正常则**逐个安装每个模块的插头**以及安装 SD 卡，当安装某个模块后指示灯变为异常，则需要**更换该模块**；
   - 若依旧异常，则**需要更换主板**。

![mainboard.jpg](https://wiki.bambulab.com/a1/troubleshooting/circuit-fault/mainboard.jpg)

### 仅 TH 指示灯异常（TH 板模块排查）

flowchart TD
A[TH 板模块排查] --> B[先安装 TH 板上的 USB-C 插头<br/>注意 USB-C 数据线方向<br/>及背面对齐的小凹槽]
B --> D[断开 TH 板上其他模块连接]
D --> E[开机观察 TH 板指示灯]
E --> F{TH 板指示灯<br/>是否恢复正常?}
F -- 否 --> G[更换新的 TH 板]
F -- 是 --> H[逐个安装每个模块的插头并开机确认]
H --> I{连接某一模块后<br/>TH 板指示灯是否变为异常?}
I -- 是 --> J[更换该模块]
I -- 否 --> K[继续逐个安装并确认]
classDef proc fill:#dae8fc,stroke:#6c8ebf,color:#000;
classDef decision fill:#fff2cc,stroke:#d6b656,color:#000;
class A,B,C,D,E,G,H,J,K proc;
class F,I decision;

请先安装 TH 板上的 USB-C 插头，注意 USB-C 数据线的方向和背面对齐的小凹槽。

![](https://wiki.bambulab.com/a1m/replace-usb-c-cable/usb_cable_orientation.jpeg)

然后根据 [更换新的 TH 板](../maintenance/th-board-replacement-guide.md) 断开 TH 板上其他模块连接，再开机观察 TH 板指示灯是否恢复正常。

![](https://wiki.bambulab.com/a1m/replace-th-board/th_board_cables_on_a1.jpeg)

1.若 TH 板指示灯依然异常，则需要**更换新的 TH 板**。  
2.若 TH 板指示灯恢复正常，则逐个安装每个模块的插头并开启确认指示灯情况。当某一模块连接上 TH 板后，TH 板指示灯变为异常，则需要**更换该模块**。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南并未解决您的问题，[*请点击此处联系在线技术支持* （服务时间 9:00-21:00）](https://support.bambulab.cn/cn/im)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
