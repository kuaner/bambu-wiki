---
path: zh/ams-2-pro/troubleshooting/failure-to-power-on
title: "AMS 2 Pro 上电异常"
description: "本指南介绍了 AMS 2 Pro 连接到打印机后无法开机的故障排除方法。"
tags: ["ams"]
created: 2025-10-11T09:59:37.745Z
updated: 2026-06-01T02:10:01.513Z
source: https://wiki.bambulab.com/zh/ams-2-pro/troubleshooting/failure-to-power-on
---

## 何时使用？

当打印机能够正常开机，但 AMS 2 Pro 无法通电开机，那么您可以参考本教程进行排障。

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 检查设备状态

### 1. 确认打印机是否正常运行

请先务必断开 AMS 与打印机的连接，然后开机观察打印机是否符合如下情况。

- 触摸屏亮起并响应。
- LED 指示灯正常亮起。
- 软件端正确绑定了设备。

如果打印机状态不符合上述现象，可搜索《打印机电路故障》，找到对应机型开始排查。若打印机能够正常开机，那么请连接 AMS 后再启动打印机电源。

### 2. 检查 AMS 状态

若 AMS 符合以下状态，则说明 AMS供电存在故障，请根据本文完成排查。

- 4 个槽位的指示灯都不亮。
- 打印机屏幕上不显示 AMS 设备。

![](https://wiki.bambulab.com/ams-2-pro/troubleshooting/ams-2-pro-failure-to-power-on/amd_2_pro_led.png)

### 排查步骤

### **1. 使用备用线缆或另一个 AMS （如有）**

如果您有备用的 6-pin 线缆，请用该线缆连接设备并观察 AMS 的运行状态。如果您有其他 AMS 设备，请将其连接到打印机观察该设备运行状态。

> 交替实验能够快速确定打印机、线缆、AMS 的工作状态。

### 2. Pin 脚检查

请检查 AMS 线缆两头的 Pin 脚是否有灰尘、是否弯曲或出现损坏。如果 Pin 脚损坏，则需要更换电缆。

![6pin-openv2.png](https://wiki.bambulab.com/ams-2-pro/troubleshooting/ams-2-pro-failure-to-power-on/6pin-openv2.png)

### 3. AMS 线缆检查

参考[更换 AMS 2 Pro 电源板](../maintenance/replace-power-board.md)中的步骤，先分离 AMS 中框和底座。

检查内部的电源线是否脱落，解锁插头的卡扣后尝试重新安装插头，再次开机观察是否恢复正常。

> 如果无法恢复正常，并且您没有万用表，请联系客户服务团队获取进一步的帮助。

![image4.png](https://wiki.bambulab.com/ams-2-pro/troubleshooting/ams2pro-communication-anomalies/image4.png)

### 4. 测试打印机输出

断开 AMS 2 Pro 背后的 6-pin 线后，给打印机通电（另一端仍连接在打印机或缓冲器上）。使用万用表的电压档，测量如下两个引脚。

![](https://wiki.bambulab.com/ams_power_on_failure/%E6%B5%8B6pin%E7%BA%BF%E7%94%B5%E5%8E%8B.png)

若 6-pin 线无法测出 24V 电压输出，则可能是 6-pin 线故障或缓冲器故障，建议同时更换。

> 对于 X1/P1 设备，还需从缓冲器上断开 4-pin 线缆，再开启打印机电源，测试 4-pin 线缆的电压。  
> 若 4-pin 有 24V 输出，则优先更换缓冲器和 6-pin 线；若 4-pin线没有输出，则优先更换 AMS 接口板和 4-pin 线.  
> ![](https://wiki.bambulab.com/ams_power_on_failure/%E6%B5%8B4pin%E7%BA%BF%E7%94%B5%E5%8E%8B.png)

### 5. 测试电源板

AMS 电源板是一块安装在 AMS 后部的电路板，它负责接收打印机输出的直流电源，并将电源传输到 AMS 主板，同时也担负一定的通信转接功能。

> ⚠️**注意!** 请勿用手或金属工具触碰电源板，否则会导致受伤或组件损坏。

检查电源板前，请先参考此 wiki [AMS 2 Pro 拆装指南](../maintenance/disassembly-and-assembly.md) 的步骤 1-3 进行拆机。

电源板露出后，断开顶部连接器。使用正极（红色）探针接触上 #1 处引脚，使用接地（黑色）探针接触 #2 处引脚或 #3 处引脚。

|  |  |
| --- | --- |
|  |  |

万用表读数均应为 24V，如下图所示。

![20251223-120940.jpg](https://wiki.bambulab.com/ams-2-pro/troubleshooting/ams-2-pro-failure-to-power-on/20251223-120940.jpg)

如果万用表读数不是 24V ，请参考此 wiki [更换 AMS 2 Pro 电源板](../maintenance/replace-power-board.md) 。如需购买电源板，请[点此购买](https://item.jd.com/10145041061042.html) 。

### 6. 检查主板

AMS 主板是 AMS 的核心电路板，它提供了一系列连接器，通过这些连接器和连接电缆将各种功能组件连接起来。

如果您在前面的步骤中断开了主板的连接，请将其重新连接到电源板。请小心地将内部 AMS 组件翻转过来，就可以看到主板。此步骤可以检验主板是否正常供电。

> ⚠️**注意!** 请勿用手或金属工具触碰电源板，否则会导致受伤或组件损坏。

![](https://wiki.bambulab.com/ams-2-pro/troubleshooting/ams-2-pro-failure-to-power-on/ams_2_pro_flipped_assembly.png)

使用万用表，使接地探头（黑色）触碰输入接地电源引脚（图示 1 处），将正极探头（红色）触碰输入 24V 引脚 (图示 2 处)。确保将万用表设置为测量直流电压，且量程合适。

![](https://wiki.bambulab.com/ams-2-pro/troubleshooting/ams-2-pro-failure-to-power-on/amd_2_pro_power_connector_marked.png)

**若万用表读数为 24V，则电压正确。** 请重新组装 AMS 2 Pro 并检查其运行状态。在某些情况下，只需拔插线缆，即可解决因接触不良导致的问题，从而恢复正常运行。如果 AMS 仍然无法运行，则可能主板有故障，需要更换。

#### 确认主板供电

**若万用表读数不是 24V，** 拔下主板上的所有连接器，除了连接电源板的两根线缆不要拔（下图 1 和 2 处的线缆）。打开 AMS 电源，并将其连接到打印机，再次用万用表测量电压是否为 24V。测量上图 1 处的电压是否为 24V。

![](https://wiki.bambulab.com/ams-2-pro/troubleshooting/ams-2-pro-failure-to-power-on/ams_2_pro_mainboard_disconnect_all.png)

如果**测量结果仍然不是 24V**，则优先更换电源板供电线。更换教程请参考：[AMS 2 Pro 线材包](../maintenance/ams-2-pro-cable-pack.md)。

![电源板供电线.png](https://wiki.bambulab.com/ams-2-pro/troubleshooting/ams-2-pro-failure-to-power-on/%E7%94%B5%E6%BA%90%E6%9D%BF%E4%BE%9B%E7%94%B5%E7%BA%BF.png)

如果更换电源板供电线后依然异常，则需主板。更换教程请参阅：[更换 AMS 2 Pro 主板](../maintenance/replace-mainboard.md)。如需购买电源板，请[点此购买](https://item.jd.com/10145040983383.html)。

如果**测量结果为 24V**，则表明某个上下料组件或五通组件存在问题。请逐个重新连接这些组件，并开机确认 AMS 通电状态，从而找到故障元件。

请参阅：

- [更换 AMS 2 Pro 上下料组件](../maintenance/replace-feeder-unit.md)
- [更换 AMS 2 Pro 五通组件和内部五通组件马达](../maintenance/replace-internal-hub-unit.md)

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
