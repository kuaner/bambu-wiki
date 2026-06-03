---
path: zh/h2d/toolhead-module-troubleshooting-for-h2d
title: "H2D/H2C 工具头模块故障排查"
description: "本文将引导您排查 H2D 工具头模块的故障"
tags: ["h2d"]
created: 2026-02-12T07:24:41.584Z
updated: 2026-03-05T06:33:44.130Z
source: https://wiki.bambulab.com/zh/h2d/toolhead-module-troubleshooting-for-h2d
---

## 何时使用

1. 打印机的工具头前盖灯会显示此时用到的挤出机，如果**工具头前盖灯一直不亮**（意味着无法切换挤出机）或**工具头前盖灯反复闪，风扇反复开关**时，这说明工具头模块存在故障。以下是工具头前盖灯正常工作状态。

![output.webp](https://wiki.bambulab.com/h2/troubleshooting/toolhead-module-troubleshooting-for-h2/output.webp)

|  |  |
| --- | --- |
| 右挤出机 | 左挤出机 |

2. 当**热端温度均显示为 0，但热床和腔温正常**时；  
3. 通过 [H2 系列打印机上电异常排查指南-下篇](troubleshooting/h2/failure-to-power-on-part2.md) 排查完，确定是工具头模块导致了整机故障。

## 排查须知

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路> 短路从而引起额外的电子设备损坏和安全隐患。  
> 观察灯语时主板上的元器件会裸露在外，请勿直接触碰元器件或带电拔插任意接头。

> 排查时需要观察打印机各部位指示灯状态。通过观察打印机状态指示灯的闪烁方式，可以快速识别打印机当前所处的工作状态，能够在无需查看屏幕的情况下，提供直观的状态反馈。排查过程中，主板是否正常的判断依据是灯语是否属于正常状态。  
> H2D 挤出主板上的风扇和涡流线圈插头采用这种小型插头设计。**拔出插头时，请用手握住插头根部，垂直于 PCB 面方向用力抬起以解锁插头**。切勿在水平方向用力，以免损坏插头。

![插头.jpg](https://wiki.bambulab.com/h2/maintenance/laser-module-40w/%E6%8F%92%E5%A4%B4.jpg)

## 排查流程

![流程图th.png](https://wiki.bambulab.com/h2/troubleshooting/toolhead-module-troubleshooting-for-h2/%E6%B5%81%E7%A8%8B%E5%9B%BEth.png)

## TH 板灯语

请根据 [更换 H2D 部件冷却风扇](../h2/maintenance/replace-part-cooling-fan.md) 教程拆下部件冷却风扇组件后观察灯语，当 TH 板出现故障时，TH 板上三个并排的指示灯将异常闪烁或熄灭。该指南中 TH 板是否恢复正常都需要通过这 3 个指示灯来判断。  
**正常状态：TH 板指示灯常亮（上&中）、快速闪烁（下）**

[

](https://public-cdn.bblmw.com/wiki/H2D/TH1.mp4)

## 排障步骤

### 1. 重启设备

重启电源有时也能够消除工具头模块异常的故障，若故障依旧，请继续下一步。

> 若有 AMS，请连接 AMS 并检查打印机屏幕上是否能够显示 AMS 信息。若打印机无法识别 AMS，则是 电源模块或 MC 板存在异常，请根据 [H2 系列打印机上电异常排查指南-上篇](../h2/troubleshooting/failure-to-power-on-part1.md) 进行故障排查。

### 2. 检查 MC-TH 线缆

**拧松**图中标记的**一个螺丝**，拆开 AP 板盖。

![image1.png](https://wiki.bambulab.com/h2/troubleshooting/toolhead-module-troubleshooting-for-h2/image1.png)  
![image2.png](https://wiki.bambulab.com/h2/troubleshooting/toolhead-module-troubleshooting-for-h2/image2.png)  
**检查**位于板盖后侧的 **MC-TH 电源连接器**是否断开，**金属 pin 脚**是否脱出。

![image3.1.png](https://wiki.bambulab.com/h2/troubleshooting/toolhead-module-troubleshooting-for-h2/image3.1.png)  
![image4.1.jpeg](https://wiki.bambulab.com/h2/troubleshooting/toolhead-module-troubleshooting-for-h2/image4.1.jpeg)

### 3. 检查挤出接口板

1. 请根据 [更换 H2C TH 板](../h2c/maintenance/replace-th-board.md) 或 [更换 H2D TH 板](../h2/maintenance/replace-H2D-TH-board.md) 拆下挤出接口板上的 2、3、4、5号插头，**保留 1 号**。开机**检查 TH 板指示灯**是否正常亮起。若恢复正常，即为拆除的某个组件存在异常，请依次插回 2、3、4、5 号插头并开机确认灯语。当插回某个插头会导致灯语异常，则表明该组件需要被更换。
2. 若 TH 板指示灯工作依旧异常，请**断电**后拆除 **1 号插头**；再重启上电，观察3个绿灯是否恢复正常；若恢复正常，即为挤出接口板存在异常，需要更换新的挤出接口板。
3. 如果拆除 **1 号插头**后故障依旧，请进行下一步。

具体的线缆接头及连接对象如下所示：

H2C:

|  |  |
| --- | --- |
|  |  |

H2D:

|  |  |
| --- | --- |
|  |  |

> 3 号插头请参考下图方式拆卸，避免插头损坏造成其他故障，后续 TH 板的部分插头也需要这样拆卸。

![output.webp](https://wiki.bambulab.com/h2/maintenance/replace-h2d-th-board/output.webp)

### 4. 检查 TH 板

1. 请断电并拆除 TH 板上 **1 至 11 号插头**，再重启上电。若 3 个绿灯恢复正常，即为拆除的某个组件存在异常，请**依次插回**这些插头并开机确认灯语。当插回某个插头会导致灯语异常，则表明该组件需要被更换。
2. 若移除这些插头后，灯语仍然异常，则需要**更换 TH 板或 MC-TH 线缆**。  
   可参考[更换 H2C TH 板](../h2c/maintenance/replace-th-board.md) 、 [更换 H2D TH 板](../h2/maintenance/replace-H2D-TH-board.md) 或 [更换 H2D MC-TH 电源通讯转接线](../h2/maintenance/replace-toolhead-to-mc-board-cable.md) 进行更换。

具体的线缆接头及连接对象如下所示：

H2C:

|  |  |
| --- | --- |
|  |  |

H2D:

|  |  |
| --- | --- |
|  |  |

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
