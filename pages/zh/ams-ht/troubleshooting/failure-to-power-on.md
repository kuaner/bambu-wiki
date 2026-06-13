---
path: zh/ams-ht/troubleshooting/failure-to-power-on
title: "AMS HT 上电异常的故障排查指南"
description: "本文将介绍 AMS HT 无法通电工作时的故障排查方法。"
tags: ["ams ht"]
created: 2026-06-01T09:36:26.343Z
updated: 2026-06-10T06:58:50.237Z
source: https://wiki.bambulab.com/zh/ams-ht/troubleshooting/failure-to-power-on
---

## 故障描述

当设备连接上 AMS HT 后，无法在软件或打印机屏幕上查看到 AMS HT，且 AMS HT 的显示屏无法亮起，这说明 AMS HT 未能成功通电启动。

![1_1.jpg](https://wiki.bambulab.com/ams-ht/troubleshooting/failure-to-power-on/1_1.jpg)

## 工具

- H1.5/H2.0 内六角螺丝刀
- 万用表

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 排查步骤

### 使用备用线缆或另一个 AMS（如有）

如果您有备用的 6-pin 线缆，请用该线缆连接设备并观察 AMS 的运行状态。如果您有其他 AMS 设备，请将其连接到打印机观察该设备运行状态。

> 交替实验能够快速确定打印机、线缆、AMS 的工作状态。

### 检查打印机状态

断开 AMS HT 的 6-pin 线缆后，为打印机通电，观察打印机屏幕是否能够正常亮起。若打印机无法正常亮起，请参考排查电路故障。

### 检查线缆连接

检查线缆两头的 Pin 脚是否有灰尘、弯曲或出现损坏。如果 Pin 脚损坏，则需要更换线缆。

![6pin-openv2.png](https://wiki.bambulab.com/ams-2-pro/troubleshooting/ams-2-pro-failure-to-power-on/6pin-openv2.png)

拧松 AMS HT 底部的两个螺丝，并从前方向上拉起中框。

|  |  |
| --- | --- |
| 3.底壳螺丝.jpg =800x |  |

检查下图两个位置的线缆是否脱落，并尝试重新连接。

![](https://wiki.bambulab.com/ams-ht/disassembly-and-assembly/7%E7%A7%BB%E9%99%A4%E5%B0%BE%E9%83%A8%E7%BA%BF%E7%BC%86.jpg)

完成后复原 AMS HT，并连回打印机。开机检查 AMS HT 是否能够正常工作。若 AMS HT 依然故障，并且您有万用表能够测量，可继续后续排查。若没有万用表，请联系客户支持团队为您提供帮助。

### 检查 24V 输出

> 万用表的基础使用可查看[如何使用万用表检测电路是否正常](../../knowledge-sharing/multimeter.md)。

将 6-pin 线连接上打印机后通电开机，万用表切换到电压档后，测量 6-pin 线另一端的电压输出。

![pixpin_2026-06-02_11-10-15.jpg](https://wiki.bambulab.com/ams-ht/troubleshooting/failure-to-power-on/pixpin_2026-06-02_11-10-15.jpg)

> 注意：测量过程中两表笔请勿相互接触。

若此处能够测量到 24V 左右电压，请检查[24V 输入](https://wiki.bambulab.com/zh/staging/ams-ht/troubleshooting/failure-to-power-on#%E6%A3%80%E6%9F%A5-24v-%E8%BE%93%E5%85%A5)。

![1_3.jpg](https://wiki.bambulab.com/ams-ht/troubleshooting/failure-to-power-on/1_3.jpg)  
![1_4.jpg](https://wiki.bambulab.com/ams-ht/troubleshooting/failure-to-power-on/1_4.jpg)

若此处无法测量到 24V 左右电压，再测量缓冲器上的 6-pin 插口。

> 所有型号的缓冲器 6-pin 插头测量位置相同，以防松扣方向为基准确认引脚。

![pixpin_2026-06-02_11-59-09.jpg](https://wiki.bambulab.com/ams-ht/troubleshooting/failure-to-power-on/pixpin_2026-06-02_11-59-09.jpg)  
![1_10.jpg](https://wiki.bambulab.com/ams-ht/troubleshooting/failure-to-power-on/1_10.jpg)

- 有 24V 电压：6-pin 线缆存在故障，需更换线缆。
- 无 24V 电压：缓冲器存在故障，需更换缓冲器。

---

> 对于 X1/P1/A1 系列设备，还需用相同方式测量 4-pin 线和 4-pin 插口的 24V 输出，从而判断 [AMS 接口板](../../x1/maintenance/replace-ams-interface-board.md)或 4-pin 线缆是否正常。

|  |  |
| --- | --- |
| 1_7.jpg | 1_8.jpg |

### 检查 24V 输入

拧松 AMS HT 底部的两个螺丝，并从前方向上拉起中框。

|  |  |
| --- | --- |
| 3.底壳螺丝.jpg =800x |  |

调整理线扣位置，释放线缆。

![pixpin_2026-06-02_11-58-09.jpg](https://wiki.bambulab.com/ams-ht/troubleshooting/failure-to-power-on/pixpin_2026-06-02_11-58-09.jpg)

拔下 AMS HT 主板上的电源线接头。

![pixpin_2026-06-02_11-31-00.jpg](https://wiki.bambulab.com/ams-ht/troubleshooting/failure-to-power-on/pixpin_2026-06-02_11-31-00.jpg)

用 6-pin 线缆连接打印机和 AMS HT 后开机，使用万用表测量这两个引脚的电压。

![1_9.jpg](https://wiki.bambulab.com/ams-ht/troubleshooting/failure-to-power-on/1_9.jpg)

- 若此处能够测量出24V，则 AMS HT 主板存在故障，需要[更换 AMS HT 主板](../maintenance/disassembly-and-assembly-of-the-motherboard.md)。
- 若此处无法测量出24V，则 AMS HT 电源板存在故障，需要[更换 AMS HT 电源板](../maintenance/replace-power-board.md)。

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
