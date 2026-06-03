---
path: zh/h2d/troubleshooting/h2/failure-to-power-on-part2
title: "H2 系列打印机上电异常排查指南-下篇"
description: "本指南将引导您完成打印机开机后无法正常工作的故障排查。"
tags: ["h2c", "h2d"]
created: 2026-01-19T04:29:09.727Z
updated: 2026-03-05T06:32:52.468Z
source: https://wiki.bambulab.com/zh/h2d/troubleshooting/h2/failure-to-power-on-part2
---

## 何时使用？

1. 设备上电后，打印机显示屏无任何响应；整机电子元器件指示灯呈现局部或全部异常状态：热床下方状态指示灯未点亮，AP 板指示灯未点亮或灯语异常；仅铁壳电源模块指示灯可闪烁或常亮。
2. 按 [H2 系列打印机上电异常排查指南-上篇](../../../h2/troubleshooting/failure-to-power-on-part1.md) 排查流程逐项核验，已排除前述故障情形，但设备无法工作的故障现象依旧存在。

|  |  |
| --- | --- |
| 屏幕不能亮.jpg   屏幕 | 电源板灯.png  铁壳电源指示灯 |
| image12.png  AP 板指示灯 | image13.png  热床状态指示灯 |

## 排查须知

> 排查时需要观察打印机各部位指示灯状态。通过观察打印机状态指示灯的闪烁方式，可以快速识别打印机当前所处的工作状态，能够在无需查看屏幕的情况下，提供直观的状态反馈。排查过程中，主板是否正常的判断依据是灯语是否属于正常状态。

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路> 短路从而引起额外的电子设备损坏和安全隐患。  
> 观察灯语时主板上的元器件会裸露在外，请勿直接触碰元器件或带电拔插任意接头。

## 所需工具和材料

- H1.5 内六角螺丝刀
- H2.0 内六角螺丝刀

## H2D/H2C 排查流程

![流程图.png](https://wiki.bambulab.com/h2/maintenance/failure-to-power-on/%E6%B5%81%E7%A8%8B%E5%9B%BE.png)

## H2D/H2C 排查步骤

### 步骤 1：确定 MC 板状态

AP 板、 TH 板的 24V 电源需要通过 MC 板中转，当 MC 板出现异常时，将会导致打印机完全无法工作。而 MC 板的异常原因可能会是 AP 板或 TH 板存在短路，以及 MC 板本身故障，因此步骤 1 需要确定 MC 板的工作状态。

#### 1. 拆下背板

参阅 [移除背板](../../../h2/maintenance/replace-rear-panel.md)，[拆下废料槽](../../../h2/maintenance/replace-purge-chute.md) 预先拆除部分组件后，观察 MC 板指示灯状态。

#### 2.灯语状态

MC 板指示灯**常亮（左上）**、**慢速闪烁（左下）**、**快速闪烁（右）**

<https://public-cdn.bblmw.com/wiki/H2D/MC.mp4>

#### 3. 操作过程

1. MC 板指示灯正常：  
   MC 板指示灯正常的情况下，设备无法工作的原因则在 **AP 板模块**或 **TH 板模块**，请根据 AP 板和 TH 板对应的灯语状态，跳转到步骤 2 或步骤 3 进行排查。
2. MC 板指示灯异常或不亮：  
   先关闭打印机电源，然后根据下图断开 MC-AP 的**电源线**（序号 4）、**信号线**（序号 10），以及 MC-TH 的**电源线**（序号 3）、**信号线**（序号 2）。完成后开机再次观察 MC 板指示灯是否恢复正常。

|  |
| --- |
|  |

- 情况1：MC 板恢复正常  
  说明 MC 板本身并无故障，而异常原因由 AP 板和 TH 板引起。请关闭电源，先安装 **MC-AP 的电源线**（序号 4）、**信号线**（序号 10）并开机观察 MC 灯语，再安装 **MC-TH 的电源线**（序号 3）、**信号线**（序号 2）并开机观察 MC 板。

  1. 如果安装 MC-AP 出现异常，请跳转到步骤 2 进行排查。
  2. 如果安装 MC-TH 出现异常，请跳转到步骤 3 进行排查。
- 情况2：MC 板依旧异常  
  说明 MC 板的外接组件可能故障，或 MC 板本身存在故障，请关机后拔下 MC 板上的**所有插头**， 开机观察 MC 板指示灯。  
  1.如果 MC 板恢复正常，请您关机后逐个安装组件插头，并逐次开机观察灯语是否再次异常，来确定造成影响的组件；  
  2.如果 MC 板依旧异常，则为 MC 板本身故障。

### 步骤 2：确定 AP 板状态

#### 1. 拆卸 AP 板盖

使用 H2.0 内六角扳手拧下 1 颗固定螺丝（BT2.6x8），然后从靠近前门的一侧取下 AP 板盖，观察 AP 板指示灯。

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-ap-board/image-6.png)

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-ap-board/image-8.png)

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-ap-board/image-5.png)

#### 2. 灯语状态

AP 板指示灯快速闪烁（左）、常亮（右）  
<https://public-cdn.bblmw.com/wiki/H2D/AP.mp4>

您也可以不拆除 AP 板盖，在特定的角度透过 AP 板盖的散热孔来观察指示灯。

<https://public-cdn.bblmw.com/wiki/H2D/AP-1.mp4>

#### 3. 操作过程

关闭打印机电源，根据[更换 H2D AP 板](../../../h2/maintenance/replace-ap-board.md)指南断开 **AP 板的所有线缆**，保留**信号线**（序号 5）、**电源线**（序号 6）。完成后开机再次观察 AP 板和 MC 板指示灯。

![image11.png](https://wiki.bambulab.com/h2/troubleshooting/toolhead-module-troubleshooting-for-h2/image11.png)

- 情况1：AP 板恢复正常  
  说明 AP 板本身并无故障，异常原因由其他模块引起，请关机后逐个安装每个插头，并且逐次开机观察灯语是否再次异常来确定具体的异常组件。
- 情况2：AP 和 MC 板依旧异常  
  说明 AP 板或 MC-AP 线缆存在异常。关机后**断开 AP 板的信号线**（序号 5）以及**电源线**（序号 6），重新开机观察 AP 板指示灯。

  1. 如果 MC 板恢复正常则需要更换 AP 板；
  2. 如果 MC 板依旧异常则需要更换 MC-AP 电源线以及信号线。

### 步骤 3：确定 TH 板状态

通过步骤 1 的详细排查，打印机的故障已经能够定位在 TH 板组件上。因为 TH 板排查流程的篇幅较多，为了更好地进行故障排查，请您跳转到 [H2D/H2C 工具头模块故障排查](../../toolhead-module-troubleshooting-for-h2d.md)。

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
