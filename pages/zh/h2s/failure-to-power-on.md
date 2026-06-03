---
path: zh/h2s/failure-to-power-on
title: "H2S 打印机上电异常排查指南"
description: "本文将引导您完成 H2S 设备在开机后无法正常工作的故障排查流程。"
tags: ["h2s"]
created: 2026-02-25T03:38:15.389Z
updated: 2026-03-11T07:09:45.310Z
source: https://wiki.bambulab.com/zh/h2s/failure-to-power-on
---

## 何时使用

1. H2S 设备上电后，打印机显示屏无任何响应；整机电子元器件指示灯呈现局部或全部异常状态：热床下方状态指示灯未点亮，AP 板指示灯未点亮或灯语异常；仅铁壳电源模块指示灯可闪烁或常亮。
2. 按 [H2 系列打印机上电异常排查指南-上篇](../h2/troubleshooting/failure-to-power-on-part1.md) 排查流程逐项核验，已排除前述故障情形，但设备无法工作的故障现象依旧存在。

|  |  |
| --- | --- |
| 屏幕不能亮.jpg   屏幕 | 电源板灯.png  铁壳电源指示灯 |
| ap2.jpg  AP 板指示灯 | image13.png  热床状态指示灯 |

## 灯语状态

**先观察 AP 板和 TH 板指示灯**，如果这两块主板的指示灯同时异常，那么就从 MC 板开始检查。  
如果 TH 板和 AP 板某一个正常，那么 MC 板就是正常的，排查另一模块即可。

### AP 板灯语状态

使用 H2.0 内六角扳手拧下 1 颗固定螺丝（BT2.6x8），然后从靠近前门的一侧取下 AP 板盖，观察 AP 板指示灯。

|  |  |  |
| --- | --- | --- |
|  |  |  |

**快速闪烁（左）、常亮（右）**

![ap.webp](https://wiki.bambulab.com/h2s/troubleshooting/failure-to-power-on/ap.webp)

您也可以不拆除 AP 板盖，在特定的角度透过 AP 板盖的散热孔来观察指示灯。

![ap-1.webp](https://wiki.bambulab.com/h2s/troubleshooting/failure-to-power-on/ap-1.webp)

### TH板灯语状态

参阅 [更换 H2S TH 板](maintenance/replace-th-board.md)的步骤一与步骤二，移除工具头后盖，观察 TH 板指示灯状态。

**快速闪烁**。

![th-1.webp](https://wiki.bambulab.com/h2s/troubleshooting/failure-to-power-on/th-1.webp)  
您也可以不拆除工具头后盖，通过打开工具头模块接口盖子，来观察 TH 板指示灯状态。

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-th-board/image-11.png)  
![th-2.webp](https://wiki.bambulab.com/h2s/troubleshooting/failure-to-power-on/th-2.webp)

### MC 板灯语状态

参考 [更换 H2D 废料滑梯](../h2/maintenance/replace-purge-chute.md) 拆除背板以及废料滑梯，开机观察 MC 板灯语情况。

**常亮（左上）、慢速闪烁（左下）、快速闪烁（右）**

本视频包含了开机后的初始化状态，故左下的指示灯有一小段常亮。  
![mc2.webp](https://wiki.bambulab.com/h2s/troubleshooting/failure-to-power-on/mc2.webp)

## H2S 排查步骤

### 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行故障排查或维护时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

### 步骤 1. MC 板模块故障排查

#### 流程图

%%{init: {"flowchart": {"htmlLabels": true, "curve": "linear"}, "themeVariables": {
"primaryColor": "#dae8fc","primaryBorderColor": "#6c8ebf",
"tertiaryColor": "#fff2cc","tertiaryBorderColor": "#d6b656"
}}}%%
graph TD
classDef proc fill:#dae8fc,stroke:#6c8ebf,color:#000;
classDef decision fill:#fff2cc,stroke:#d6b656,color:#000;
M0["MC 板异常 / 不亮"]:::proc
M1["关机<br/>断开：MC-AP 电源线、信号线<br/>断开：TH 电源线<br/>开机观察 MC 板指示灯"]:::proc
M2{"MC 板是否恢复正常？"}:::decision
M3["关机<br/>拔下 AP 板 XT30 接头 + Type-C 接头（TH 线缆）<br/>再安装 MC 板端的 MC-AP 电源线+ 信号线<br/>开机观察 MC 灯语"]:::proc
M4{"MC 板是否依旧异常？"}:::decision
TO\_AP["转 ：AP 板及其部件排查"]:::proc
TO\_TH["转 ：TH 板及其部件排查"]:::proc
M5["关机<br/>拔下 MC 板所有插头<br/>开机观察 MC 板指示灯"]:::proc
M6{"MC 板是否恢复正常？"}:::decision
M7["关机后逐个装回组件插头<br/>逐次开机定位异常组件"]:::proc
M8["更换 MC 板"]:::proc
M0 --> M1 --> M2
M2 -- "恢复正常" --> M3 --> M4
M4 -- "依旧异常" --> TO\_AP
M4 -- "恢复正常" --> TO\_TH
M2 -- "依旧异常" --> M5 --> M6
M6 -- "恢复正常" --> M7
M6 -- "依旧异常" --> M8

#### 操作步骤

MC 板灯语异常的前提下，关机拔下 **MC 板上** 3、4、10 号插头，重新开机观察 MC 板灯语是否恢复正常。

![MCboard](https://wiki.bambulab.com/h2/maintenance/replace-mc-board/image-11.png)

- 情况1：MC 板恢复正常  
  说明 MC 板本身并无故障，而异常原因由 AP 板和 TH 板引起。请关闭电源，拔下 **AP 板上**的 XT30 接头（序号 7）以及 USB-C 接头（序号 8）。再安装 **MC 板**的 MC-AP 电源线（序号 4）、信号线（序号 10）并开机观察 MC 灯语。  
  1. 如果 MC 板依旧异常，请跳转到 AP 板模块故障进行排查。  
  2. 如果 MC 板恢复正常，请跳转到 TH 板模块故障进行排查。

![APboard](https://wiki.bambulab.com/h2s/maintenance/image-8.png)

- 情况2：MC 板依旧异常  
  说明 MC 板的外接组件可能故障，或 MC 板本身存在故障。请关机后拔下 MC板 图中标记的所有插头，再开机观察 MC 板指示灯。  
  1.如果 MC 板恢复正常，请您关机后逐个安装组件插头，并逐次开机观察灯语是否异常来确定造成影响的组件；  
  2.如果 MC 板依旧异常，则为 MC 板本身故障，需要更换 MC 板，可参考[MC 板更换指南](maintenance/replace-mc-board.md)。

### 步骤 2. AP 板及其部件排查

%%{init: {"flowchart": {"htmlLabels": true, "curve": "linear"}, "themeVariables": {
"primaryColor": "#dae8fc","primaryBorderColor": "#6c8ebf",
"tertiaryColor": "#fff2cc","tertiaryBorderColor": "#d6b656"
}}}%%
graph TD
classDef proc fill:#dae8fc,stroke:#6c8ebf,color:#000;
classDef decision fill:#fff2cc,stroke:#d6b656,color:#000;
A0["AP 板存在故障"]:::proc
A1["关机<br/>断开 AP 板所有线缆<br/>保留：信号线+ 电源线<br/>开机观察 AP + MC 指示灯"]:::proc
A2{"AP + MC 是否恢复正常？"}:::decision
A3["关机后逐个装回每个插头（除 USB-C 线缆）<br/>逐次开机定位异常组件"]:::proc
A4["关机<br/>断开 AP 板：信号线+ 电源线<br/>重新开机观察 AP 板指示灯"]:::proc
A5{"MC 板是否恢复正常？"}:::decision
A6["更换 AP 板"]:::proc
A7["更换 MC-AP 电源线 + 信号线"]:::proc
A0 --> A1 --> A2
A2 -- "恢复正常" --> A3
A2 -- "依旧异常" --> A4 --> A5
A5 -- "恢复正常" --> A6
A5 -- "依旧异常" --> A7

关闭打印机电源，断开 AP 板的所有线缆，仅保留信号线（序号 5）、电源线（序号 6）。完成后开机再次观察 AP 板和 MC 板指示灯。

![](https://wiki.bambulab.com/h2s/maintenance/image-8.png)

#### 情况1：AP 和 MC 板恢复正常

说明 AP 板本身并无故障，异常原因由其他模块引起，请关机后逐个安装每个插头（USB-C 线缆无需安装验证），并且逐次开机观察灯语是否异常来确定具体的异常组件。

#### 情况2：AP 和 MC 板依旧异常

说明 AP 板或 MC-AP 线缆存在异常。关机后断开 AP 板的信号线（序号 5）以及电源线（序号 6），重新开机观察 AP 板指示灯。  
1. 如果 MC 板恢复正常则需要更换 AP 板，可参考[AP 板更换指南](maintenance/replace-ap-board.md)；  
2. 如果 MC 板依旧异常则需要更换 MC-AP 电源线以及信号线,可参考[MC-AP 线更换指南](../h2/maintenance/replace-mc-ap-cable.md)。

### 步骤 3. TH 板及其部件排查

%%{init: {"flowchart": {"htmlLabels": true, "curve": "linear"}, "themeVariables": {
"primaryColor": "#dae8fc","primaryBorderColor": "#6c8ebf",
"tertiaryColor": "#fff2cc","tertiaryBorderColor": "#d6b656"
}}}%%
graph TD
classDef proc fill:#dae8fc,stroke:#6c8ebf,color:#000;
classDef decision fill:#fff2cc,stroke:#d6b656,color:#000;
T0["TH 板存在故障<br/>（拔下 AP 板的 USB-C 后，AP + MC 恢复正常）"]:::proc
T1["拔下 TH 板上所有插头，仅保留USB-C 线缆<br/>开机观察 TH / AP / MC 指示灯"]:::proc
T2{"是否恢复正常？"}:::decision
T3["关机后逐个装回每个插头<br/>逐次开机定位异常组件"]:::proc
T4["关机<br/>断开 TH 板 USB-C 线缆<br/>重新开机观察指示灯"]:::proc
T5{"AP + MC 是否恢复正常？"}:::decision
T6["更换 TH 板"]:::proc
T7["更换 USB-C 线缆"]:::proc
T0 --> T1 --> T2
T2 -- "恢复正常" --> T3
T2 -- "依旧异常" --> T4 --> T5
T5 -- "恢复正常" --> T6
T5 -- "依旧异常" --> T7

当拔下 AP 板上的 USB-C 线缆后，AP 和 MC 板都能恢复正常，这说明 TH 板存在故障导致设备异常。  
请参考 [更换 H2S TH 板](https://wiki.bambulab.com/e/zh/h2s/maintenance/replace-th-board) 拔下图中标记的所有插头，再次开机观察 TH、AP 和 MC 的指示灯是否恢复正常。

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-th-board/image-2.png)

#### 情况1：恢复正常

说明 TH 板本身并无故障，异常原因由其他模块引起，请关机后逐个安装每个插头，并且逐次开机观察灯语是否异常来确定具体的异常组件并更换。

#### 情况2：依旧异常

说明 TH 板或 USB-C 线缆存在异常。关机后断开 TH 板的 USB-C 线缆，重新开机观察指示灯。  
![pull_usb-c.webp](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-th-board/pull_usb-c.webp)

1. 如果 AP 和 MC 板恢复正常则需要更换 TH 板，可参考[更换 H2S TH 板](maintenance/replace-th-board.md)。
2. 如果 AP 和 MC 板依旧异常则需要更换 USB-C 线缆，可参考[更换 H2S USB-C线缆](maintenance/replace-usb-c-cable.md)。

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
