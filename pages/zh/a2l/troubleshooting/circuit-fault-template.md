---
path: zh/a2l/troubleshooting/circuit-fault-template
title: "电路故障排查-A2L"
description: "当设备正常通电后却无法开机工作时，请参考本文进行排查。"
tags: []
created: 2026-06-01T13:05:14.134Z
updated: 2026-06-01T13:14:21.434Z
source: https://wiki.bambulab.com/zh/a2l/troubleshooting/circuit-fault-template
---

## 何时使用

1.设备通电后电源开关指示灯无法亮起  
2.电源开关指示灯正常亮起，但屏幕无法亮起，且软件无法显示设备或显示打印机离线。

## 排查须知

正式排查前首先需要了解主板灯语，从而大致确认主板目前状态。

### 所需工具

- 内六角扳手
- 十字螺丝刀
- 万用表（可选）

### 安全提示

> 排查时需要观察打印机各部位指示灯状态。通过观察打印机状态指示灯的闪烁方式，可以快速识别打印机当前所处的工作状态，能够在无需查看屏幕的情况下，提供直观的状态反馈。排查过程中，主板是否正常的判断依据是灯语是否属于正常状态。

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路> 短路从而引起额外的电子设备损坏和安全隐患。  
> 观察灯语时主板上的元器件会裸露在外，请勿直接触碰元器件或带电拔插任意接头。

## 现象一：电源开关指示灯无法亮起

市电接入设备并按下开关后，电源开关的白色指示灯将自动亮起。如果开关的白色指示灯无法点亮，说明电源线故障或电源开关存在故障。

![](https://public-cdn.bblmw.com/wiki/new/a2l/troubleshooting/circuit-fault-template/1.jpg)

### 步骤一：电源线故障

打印机的电源线使用标准插头，请使用同一类型的电源线通电测试。开机观察白色指示灯是否亮起。若指示灯恢复正常，则说明电源线故障，需要更换新电源线。

### 步骤二：保险丝熔断或开关故障

开关内部装有保险丝，您可以使用镊子撬出保险丝安装座。由于部分保险丝外壳不透明，无法直接观察熔丝状态，可借助万用表或其他方式进行检测。

![](https://public-cdn.bblmw.com/wiki/new/a2l/troubleshooting/circuit-fault-template/2.png)

**方法一：**

将万用表拨至蜂鸣档（或电阻档），表笔分别接触保险丝两端的金属帽：若有**蜂鸣声**或**电阻值接近 0 Ω**，表示**保险丝正常**；若无蜂鸣声、显示“OL”（开路）或电阻值很大，则说明保险丝已熔断，需要更换新的开关插座。您可以参考 [如何使用万用表检测电路是否正常](../../knowledge-sharing/multimeter.md)了解万用表的基本使用方式。

**方法二：**

如果您的手机支持**多点触碰**，那么屏幕类型为“电容屏”。您就可以用手指捏住保险丝的一端，使用另一端触碰手机屏幕，观察屏幕是否能够被点击。如果可以的话那么保险丝就是正常的。

![3.webp](https://public-cdn.bblmw.com/wiki/new/a2l/troubleshooting/circuit-fault-template/3.webp)

## 现象二：电源开关指示灯亮起

电源开关指示灯能够亮起，说明故障位于设备内部。

### 检查电源模块

**电源模块指示灯正常状态**

小心地将打印机倾斜放置后，从底部观察屏幕对面方向的散热孔，在一定角度下可以观察到绿色 LED 灯，常亮说明电源模块工作正常。

![powersupply.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/troubleshooting/circuit-fault-template/powersupply.jpg)

观察电源模块指示灯是否常亮，若指示灯熄灭或闪烁，请关机后参考[更换电源模块](https://wiki.bambulab.com/zh/a2l/maintenance/replace-power-supply)断开电源模块上的 24V 输出线缆，再开机观察电源模块的指示灯。

- 若指示灯恢复常亮，说明电源模块能够正常输出 24V，此时打印机无法工作的故障可能在主板或 TH 板上，请进行后续排查；
- 若指示灯闪烁或熄灭，则需要[更换电源模块](https://wiki.bambulab.com/zh/a2l/maintenance/replace-power-supply)。

![dy114.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-y-axis-linear-guide-assembly/dy114.jpg)

### 排查主板

#### 流程图

flowchart TD
%% ==================== Nodes ====================
A[开机] --> B{指示灯恢复正常?}
B -- 恢复正常 --> C[故障在 TH 板/转接板] --> D[继续排查]
B -- 异常 --> E[关机并拔除线缆&取出 SD 卡]
E --> G[重新上电] --> H{指示灯仍异常?}
H -- 异常 --> I[更换主板] --> J[结束]
H -- 正常 --> K[逐个装回拔下的插件 + SD 卡]
K --> L[每装回一个组件后<br>开机检查灯状态] --> M{出现异常的插件是?}
M -- 是 --> N[更换对应插件] --> J
%% ==================== Styles ====================
%% Decision nodes – light yellow
classDef decision fill:#FFF9C4,stroke:#333,stroke-width:2px;
%% Process nodes – light blue
classDef process fill:#BBDEFB,stroke:#333,stroke-width:2px;
class B,H,M decision;
class A,C,D,E,G,I,J,K,L,N process;

#### 排查步骤

**通信状态灯正常状态**

从底部观察屏幕附近的散热孔，绿色和白色的 LED 灯为通信状态灯。白灯常亮说明主板发送数据正常，绿灯常亮说明 TH 板发送数据成功被主板接收。

![mcmodel.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/troubleshooting/circuit-fault-template/mcmodel.jpg)  
![mcmodel2.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/troubleshooting/circuit-fault-template/mcmodel2.jpg)

> 拆卸底盖后右侧的 LED 灯为 通信状态灯。  
> ![mcmodel3.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/troubleshooting/circuit-fault-template/mcmodel3.jpg)

**主板工作指示灯正常状态**

观察主板需拆卸前底盖，可参考[A2L 更换底盖](https://wiki.bambulab.com/zh/a2l/maintenance/replace-bottom-cover)预先拆除。

主板上的两个绿色 LED 灯分别为间隔 1s 闪烁和间隔 5s 闪烁，其中间隔 5s 闪烁的 LED 灯亮起时间很短，请仔细观察。

![ap2.webp](https://public-cdn.bblmw.com/wiki/new/a2l/troubleshooting/circuit-fault-template/ap2.webp)

若主板上的工作指示灯出现异常，请先关机后使用 H1.5 内六角螺丝刀拆下图示两颗螺丝，拔除工具头线缆。

![dz005.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-bottom-cover/dz005.jpg)  
![dz006.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-bottom-cover/dz006.jpg)

然后开机观察主板的工作指示灯是否恢复正常。

**工作指示灯恢复正常**

说明故障在 TH 板或转接板上，请进行后续排查。

**工作指示灯依然异常**

故障在主板上。关机后再将其余线缆拔下并取出 SD 卡，其中 1、2 端子需按下锁扣拔出，3、4 号端子可以直接拔出，5 号需要撬开黑色压块后取出线缆。

![ap001.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-mainboard/ap001.jpg)  
![sdcard.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/troubleshooting/circuit-fault-template/sdcard.jpg)

| **序号** | **连接对象** | **序号** | **连接对象** |
| --- | --- | --- | --- |
| 1 | 4/6 Pin 接口板 | 4 | Y 电机 |
| 2 | AC 板 | 5 | 屏幕组件 |
| 3 | Z 电机 |  |  |

完成后开机观察主板指示灯是否恢复正常。

- 若依然异常，则需要更换新的主板。
- 若恢复正常，则逐次逐个装回拔下的插头以及 SD 卡，开机观察安装哪个插头后灯语变为异常，并更换该组件。

### 排查转接板和 TH 板

**TH 板指示灯正常状态**

请先参考 [A2L 更换电源模块](https://wiki.bambulab.com/zh/a2l/maintenance/replace-toolhead-rear-housing) 取下工具头后盖。

左侧的白色和绿色 LED 灯为通信状态灯，常亮为通信正常。右侧的绿色 LED 灯为工作指示灯，闪烁代表工作正常。

![thboard.webp](https://public-cdn.bblmw.com/wiki/new/a2l/troubleshooting/circuit-fault-template/thboard.webp)

**转接板指示灯正常状态**

X 轴上的转接板也承担 MC-TH 通信功能，可取下前盖观察灯语，白色和绿色 LED 常亮为通信正常。

![connectorboard.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/troubleshooting/circuit-fault-template/connectorboard.jpg)  
![connectorboard2.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/troubleshooting/circuit-fault-template/connectorboard2.jpg)

> 主板和 TH 的通信中，1/2/3 白灯代表主板发射数据链路，4/5/6 绿灯代表 TH 板发射数据链路。  
> ![ledstatus.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/troubleshooting/circuit-fault-template/ledstatus.jpg)

#### 主板-转接板通讯存在异常

情况一：2 号转接板白灯异常；  
情况二：6 号主板绿灯异常，5 号转接板绿灯正常。

请参考[A2L 更换工具头线缆](https://wiki.bambulab.com/zh/a2l/maintenance/replace-toolhead-cable)重新安装工具头线缆（底座端）。若故障依旧，可能需要更换通讯线缆或转接板。

#### 转接板- TH 板通讯存在异常

情况三：3 号 TH 板白灯异常，2 号转接板白灯正常；  
情况四：5 号 转接板绿灯异常，4号 TH 板灯正常。

请参考[A2L 更换工具头线缆](https://wiki.bambulab.com/zh/a2l/maintenance/replace-toolhead-cable)重新安装工具头线缆（工具头端）。若故障依旧，可能需要更换通讯线缆或转接板。

#### TH 板模块存在故障

情况五：4 号 TH 板绿灯异常，或 TH 板**工作指示灯**异常。

请参考[A2L 更换TH板](https://wiki.bambulab.com/zh/a2l/maintenance/replace-th-board)断开工具头主板上的插头，仅保留工具头线缆。

![th009.jpg](https://public-cdn.bblmw.com/wiki/new/a2l/replace-th-board/th009.jpg)

| **序号** | **连接对象** | **序号** | **连接对象** |
| --- | --- | --- | --- |
| 1 | 涡流线圈 | 4 | 热端加热组件 |
| 2 | 热端风扇 | 5 | 进料霍尔板 |
| 3 | 部件风扇 | 6 | A3508挤出电机 |

然后开机观察异常灯是否恢复正常。

1. 依旧异常，需要更换 TH 板或通信线缆。
2. 恢复正常，逐次逐个装回拔下的插头，开机观察安装哪个插头后灯语变为异常，并更换该组件。

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的客户支持团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
