---
path: zh/p2s/p2s-circuit-fault-template
title: "打印机电路故障排查 - P2S"
description: "P2S 打印机开机后设备无法通电的故障排查方法"
tags: ["p2s"]
created: 2026-02-25T08:13:36.437Z
updated: 2026-07-02T09:06:03.013Z
source: https://wiki.bambulab.com/zh/p2s/p2s-circuit-fault-template
---

## 何时使用

当设备开机后，开关的白色指示灯无法亮起时，或开关的白色指示灯正常亮起，但屏幕、补光灯均无法工作。  
![powerswitch.jpg](https://wiki.bambulab.com/p2s/troubleshooting/p2s-circuit-fault-template/powerswitch.jpg)

## 排查须知

> 排查时需要观察打印机各部位指示灯状态。通过观察打印机状态指示灯的闪烁方式，可以快速识别打印机当前所处的工作状态，能够在无需查看屏幕的情况下，提供直观的状态反馈。排查过程中，主板是否正常的判断依据是灯语是否属于正常状态。

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路> 短路从而引起额外的电子设备损坏和安全隐患。  
> 观察灯语时主板上的元器件会裸露在外，请勿直接触碰元器件或带电拔插任意接头。

## 现象一：开关熄灭

白色指示灯无法亮起的现象可能是因为**电源线故障**、**开关故障**或开关内**保险丝烧毁**导致的，这需要进行故障排除确定原因。

### 步骤一：电源线故障

打印机的电源线使用标准插头，请使用同一类型的电源线通电测试。开机观察白色指示灯是否亮起。若指示灯恢复正常，则说明电源线故障，需要更换新电源线。

### 步骤二：保险丝熔断或开关故障

开关内部装有保险丝，您可以使用镊子撬出保险丝安装座。由于部分保险丝外壳不透明，无法直接观察熔丝状态，可借助万用表或其他方式进行检测。

|  |  |
| --- | --- |

如果您的手机支持**多点触碰**，那么屏幕类型为“电容屏”。您就可以用手指捏住保险丝的一端，使用另一端触碰手机屏幕，观察屏幕是否能够被点击。如果可以的话那么保险丝就是正常的。

![12.webp](https://wiki.bambulab.com/p2s/troubleshooting/p2s-circuit-fault-template/12.webp)

将万用表拨至蜂鸣档（或电阻档），表笔分别接触保险丝两端的金属帽：若有**蜂鸣声**或**电阻值接近 0 Ω**，表示**保险丝正常**；若无蜂鸣声、显示“OL”（开路）或电阻值很大，则说明保险丝已熔断，需要更换新的开关插座。您可以参考 [如何使用万用表检测电路是否正常](../knowledge-sharing/multimeter.md)了解万用表的基本使用方式。

如果您没有万用表配合测量，那么也可以直接更换开关，开关插座中内置了一个新的保险丝。请参考 [更换 P2S 电源开关插座](maintenance/replace-power-switch-assembly.md) 更换新的开关插座。

## 现象二：开关亮起

白色指示灯正常亮起，说明保险丝、电源线、电源开关都正常，而设备无法工作可能会是电源模块故障，或主板异常导致的设备无法工作，可参考灯语判断各模块工作状态。

### 灯语

#### TH 板正常状态

TH 板指示灯常亮（上&右下）、快速闪烁（左下）

参考[更换 P2S TH 板](maintenance/replace-th-boards-and-fpc-cable.md) ，取下**工具头后盖**，观察 TH 板指示灯状态。

![p2s_th.gif](https://wiki.bambulab.com/general/bbl-indicator-led/p2s_th.gif)

#### AP 板正常状态

AP 板指示灯快速闪烁（左）、常亮（右）

从靠近前门的一侧打开 AP 板盖，观察 AP 板指示灯。

![01_open_the_service_end_of_the_ap_board_cover_001.png](https://wiki.bambulab.com/knowledge-sharing/knowledge/01_open_the_service_end_of_the_ap_board_cover_001.png)

![p2s-ap.gif](https://wiki.bambulab.com/general/bbl-indicator-led/p2s-ap.gif)

#### MC 板正常状态

MC 板指示灯常亮（上）、慢速闪烁（下）

![指示灯2.webp](https://wiki.bambulab.com/p2s/%E6%8C%87%E7%A4%BA%E7%81%AF2.webp)

### 1. 排查电源模块

参考 [更换 P2S 背板](maintenance/replace-rear-panel.md) 预先拆下打印机背板，完成后插上电源线开机，观察电源模块的 LED 灯是否正常亮起。

![rear_panel_screws_010.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/rear_panel/rear_panel_screws_010.png)

[p2s-pw.mp4](https://wiki.bambulab.com/general/bbl-indicator-led/p2s-pw.mp4)

- 如果 LED 熄灭，请关机后重新连接电源模块和 AC 板的供电线；重新开机后若 LED 依然无法亮起，则需要更换新的电源模块，可参考[更换电源模块](maintenance/replace-power-supply.md)；  
  ![powersupply.jpg](https://wiki.bambulab.com/p2s/troubleshooting/p2s-circuit-fault-template/powersupply.jpg)
- 如果 LED 常亮或闪烁，说明电源模块工作正常，请进行后续步骤。

### 2. 排查 MC 板模块

#### 流程图

%%{init: {"flowchart": {"htmlLabels": true, "curve": "linear"}}}%%
flowchart TD
classDef proc fill:#dae8fc,stroke:#6c8ebf,color:#000;
classDef decision fill:#fff2cc,stroke:#d6b656,color:#000;
A{MC 板指示灯是否正常?}:::decision -- 是 --> B[进一步检查 AP 板和 TH 板工作状态]:::proc
A -- 否 --> C[关机后断开 2/3/10 线缆<br/>开机观察 MC 板指示灯是否依然异常]:::proc
C --> D{MC 板是否恢复正常?}:::decision
D -- 是 --> E[故障原因在 AP 板或 TH 板<br/>关机后逐个安装 MC-AP / MC-TH 线缆<br/>逐次开机确认与 AP 或 TH 相关<br/>再进行后续排查]:::proc
D -- 否 --> F[可能为 MC 板本身故障或连接模块故障<br/>关机后拔下 MC 板所有插头<br/>仅保留 9 电源线<br/>开机观察 MC 板是否恢复正常]:::proc
F --> G{MC 板是否恢复正常?}:::decision
G -- 否 --> H[更换 MC 板]:::proc
G -- 是 --> I[关机后逐个安装拔下的插头<br/>逐次开机定位引发故障的组件]:::proc

#### MC 板指示灯正常

请进一步检查 AP 板和 TH 板工作状态。

#### MC 板指示灯异常

请关机后断开 MC-AP 的**电源线**（序号 2）和**信号线**（序号 3）和**MC-TH 线缆**（序号 10），然后开机观察 MC 板指示灯是否依然异常。

- MC 板恢复正常：说明故障原因在 AP 板或 TH 板，请关机后逐个安装 MC-AP 的**电源线**（序号 2）和**信号线**（序号 3）和**MC-TH 线缆**（序号 10），开机确定故障与 AP 或 TH 相关，并进行后续排查。

![mc_board_connectors_027.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-mc-and-ac-boards/mc_board_connectors_028.png)

- MC 板依旧异常：说明 MC 板本身存在故障，或者 MC 板上连接模块存在故障。请拔下所有插头，保留 MC 电源线（序号 9），重新开机观察 MC 板是否恢复正常。若**依旧故障**，则需要更换 MC 板；若**恢复正常**，请关机后逐个安装拔下的插头，开机观察灯语是否再次异常，找到具体故障组件后更换该组件。

### 3. 排查 AP 板模块

#### 流程图

flowchart TD
A["检查 AP 板指示灯状态"] --> B{"AP 板指示灯是否正常？"}
B -->|正常| C["进一步检查 TH 板工作状态"]
B -->|异常| D["关机后断开 AP 板上的所有插头<br/>再开机观察 AP 和 MC 板指示灯"]
D --> E{"AP 和 MC 板指示灯是否恢复正常？"}
E -->|恢复正常| F["先重新连接 8 号和 9 号线缆<br/>开机观察灯语"]
F --> G{"此时灯语是否依然正常？"}
G -->|正常| H["AP 主板正常<br/>关机后逐个安装其他组件插头<br/>每装一个就开机观察灯语"]
H --> I{"灯语是否再次异常？"}
I -->|是| J["定位到具体故障组件<br/>更换该组件"]
I -->|否| K["全部组件连接完成<br/>状态正常"]
G -->|异常| L["AP 主板异常<br/>需要更换新的 AP 板"]
E -->|依旧异常| M["判定 MC-AP 线缆故障<br/>更换新的 MC-AP 线缆"]
%% 样式
classDef process fill:#D6ECFF,stroke:#4A90E2,stroke-width:1px,color:#000;
classDef decision fill:#fff2cc,stroke:#d6b656,color:#000;
class A,C,D,F,H,J,K,L,M process;
class B,E,G,I decision;

#### AP 板指示灯正常

请进一步检查 TH 板工作状态。

#### AP 板指示灯异常

关机后参考[更换 P2S AP 板](maintenance/replace-ap-board.md)断开 AP 板上的所有插头，然后开机观察 AP 和 MC 板指示灯是否依然异常。

![ap_connectors_007.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-ap-board/ap_connectors_007.png)

- AP 和 MC 板恢复正常：说明故障原因在 AP 板或其他拔下的某个插头中。**先重新连接 8 号和 9 号线缆**，若灯语异常，则 AP 主板存在故障，需要 [更换 AP 主板](maintenance/replace-ap-board.md)。若此时开机后灯语依然正常，则 AP 主板正常，再关机逐个安装其他组件的插头，并开机**观察灯语是否再次异常**，找到具体故障组件后更换该组件。
- AP 和 MC 板依旧异常：说明 MC-AP 线缆存在故障，需要[更换 MC-AP 线缆](https://wiki.bambulab.com/zh/p2s/maintenance/replace-mc-ap-cable-pack-(2-in-1))。

### 4. 排查 TH 板模块

#### 流程图

flowchart TD
A["断开 TH 板上的所有插头<br/>然后开机观察 MC 板指示灯是否依然异常"] --> B{"MC 板指示灯是否恢复正常？"}
B -->|恢复正常| C["先重新连接 6 号线缆并开机<br/>观察灯语"]
C --> D{"此时 TH 板灯语是否异常？"}
D -->|异常| E["TH 主板存在故障<br/>需要更换 TH 主板"]
D -->|正常| F["TH 主板正常<br/>关机后逐个安装其他组件插头<br/>每装一个就开机观察灯语"]
F --> G{"灯语是否再次异常？"}
G -->|是| H["定位到具体故障组件<br/>更换该组件"]
G -->|否| I["全部组件连接完成<br/>状态正常"]
B -->|依旧异常| J["工具头线缆故障<br/>需要更换工具头线缆"]
%% 样式
classDef process fill:#D6ECFF,stroke:#4A90E2,stroke-width:1px,color:#000;
classDef decision fill:#fff2cc,stroke:#d6b656,color:#000;
class A,C,E,F,H,I,J process;
class B,D,G decision;

#### 操作步骤

关机后断开 TH 板上的所有插头，然后开机观察 MC 板指示灯是否依然异常。

|  |  |
| --- | --- |
| 22_022.png | connector1.png |

- MC 板恢复正常：说明故障原因在 TH 板或其他拔下的某个插头中。**先重新连接 6 号线缆**并开机，若此时灯语异常，则 TH 主板存在故障，需要 [更换 TH 主板](maintenance/replace-th-boards-and-fpc-cable.md)。若此时开机后灯语依然正常，则 TH 主板正常，再关机逐个安装其他组件的插头，并开机**观察灯语是否再次异常**，找到具体故障组件后更换该组件。
- MC 板依旧异常：说明工具头线缆存在故障，需要 [更换工具头线缆](maintenance/replace-toolhead-cable.md)。

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的客户支持团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
