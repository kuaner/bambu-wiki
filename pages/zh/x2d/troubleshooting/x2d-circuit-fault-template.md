---
path: zh/x2d/troubleshooting/x2d-circuit-fault-template
title: "打印机电路故障排查-X2D"
description: "X2D 打印机开机后设备无法通电的故障排查方法"
tags: []
created: 2026-05-09T02:03:31.994Z
updated: 2026-05-18T02:08:54.066Z
source: https://wiki.bambulab.com/zh/x2d/troubleshooting/x2d-circuit-fault-template
---

## 何时使用

当设备开机后，开关的白色指示灯无法亮起时，或开关的白色指示灯正常亮起，但屏幕、补光灯均无法工作。

![powerswitch.jpg](https://wiki.bambulab.com/p2s/troubleshooting/p2s-circuit-fault-template/powerswitch.jpg)

## 所需工具

- 内六角扳手
- 十字螺丝刀
- 万用表（非必需）

## 排查须知

> 排查时需要观察打印机各部位指示灯状态。通过观察打印机状态指示灯的闪烁方式，可以快速识别打印机当前所处的工作状态，能够在无需查看屏幕的情况下，提供直观的状态反馈。排查过程中，主板是否正常的判断依据是灯语是否属于正常状态。

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路，从而引起额外的电子设备损坏和安全隐患。  
> 观察灯语时主板上的元器件会裸露在外，请勿直接触碰元器件或带电拔插任意接头。

## 现象一：开关熄灭

白色指示灯无法亮起的现象可能是因为**电源线故障**、**开关故障**或开关内**保险丝烧毁**导致的，这需要进行故障排除确定原因。

### 步骤一：电源线故障

打印机的电源线使用标准插头，请使用同一类型的电源线通电测试。开机观察白色指示灯是否亮起。若指示灯恢复正常，则说明电源线故障，需要更换新电源线。

### 步骤二：保险丝熔断或开关故障

开关内部装有保险丝，您可以使用镊子撬出保险丝安装座。由于部分保险丝外壳不透明，无法直接观察熔丝状态，可借助万用表或其他方式进行检测。

|  |  |
| --- | --- |

#### 方法一：

将万用表拨至蜂鸣档（或电阻档），表笔分别接触保险丝两端的金属帽：若有**蜂鸣声**或**电阻值接近 0 Ω**，表示**保险丝正常**；若无蜂鸣声、显示“OL”（开路）或电阻值很大，则说明保险丝已熔断，需要更换新的开关插座。您可以参考 [如何使用万用表检测电路是否正常](../../knowledge-sharing/multimeter.md)了解万用表的基本使用方式。

如果您没有万用表配合测量，可以使用方法二。

#### 方法二：

如果您的手机支持**多点触碰**，那么屏幕类型为“电容屏”。您就可以用手指捏住保险丝的一端，使用另一端触碰手机屏幕，观察屏幕是否能够被点击。如果可以的话那么保险丝就是正常的。

![12.webp](https://wiki.bambulab.com/p2s/troubleshooting/p2s-circuit-fault-template/12.webp)

若保险丝烧毁，则需要[更换新的开关插座](../../p2s/maintenance/replace-power-switch-assembly.md) ，并根据[该Wiki](../maintenance/replace-ac-board.md)检查 AC 板外观是否存在烧毁痕迹，供电线是否相互接触短路。

![acboard.jpg](https://wiki.bambulab.com/x2d/troubleshooting/x2d-circuit-fault-template/acboard.jpg)

## 现象二：开关亮起

白色指示灯正常亮起，说明保险丝、电源线、电源开关都正常，而设备无法工作，可能是电源模块故障或主板异常导致的，可参考灯语判断各模块工作状态。

### 1. 排查电源模块

参考 [更换 X2D 背板](../maintenance/replace-rear-panel.md) 预先拆下打印机背板，完成后插上电源线开机，观察电源模块的 LED 灯是否正常亮起。

- 如果 LED 熄灭，请关机后重新连接下图所示的供电线；重新开机后若 LED 依然无法亮起，则需要更换新的电源模块。以上步骤均可参考[更换电源模块](../../p2s/maintenance/replace-power-supply.md)；

![powersupply.jpg](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_power_supply/006_power_supply_cable.jpg)

- 如果 LED 常亮或闪烁，说明电源模块工作正常，请进行后续步骤。

### 2. 排查 MC 板模块

#### 指示灯状态

MC 板指示灯常亮（上）、慢速闪烁（下）。

请参考[更换 X2D 背板](../maintenance/replace-rear-panel.md)移除打印机背板，观察 MC 板指示灯。

![mc_light.webp](https://wiki.bambulab.com/general/bbl-indicator-led/mc_light.webp)

#### MC 板指示灯正常

请进一步检查 AP 板和 TH 板工作状态。

#### MC 板指示灯异常

请关机后断开 MC-AP 的**通信线**（序号 1）和**供电线**（序号 2），然后开机观察 MC 板指示灯是否依然异常。

- MC 板恢复正常：说明故障原因在 AP 板或 TH 板，请关机后安装 MC-AP 的**通信线**（序号 1）和**供电线**（序号 2），并进行后续排查。

![012_mc_board_connector.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/mc_board/012_mc_board_connector.png)

| 序号 | 接口说明 | 序号 | 接口说明 | 序号 | 接口说明 | 序号 | 接口说明 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | AP 板（通信） | 5 | 腔温 NTC | 9 | XY 电机（A） | 13 | 辅助挤出机（电机） |
| 2 | AP 板（供电） | 6 | 腔温加热组件 NTC | 10 | XY 电机（B） | 14 | Z 电机 |
| 3 | 自适应风道切换组件 | 7 | 腔温加热组件 | 11 | 电源 | 15 | AC 板 |
| 4 | 缓冲器 | 8 | 热床（信号线） | 12 | 辅助挤出机（通信） | 16 | MC 板风扇 |

- MC 板依旧异常：说明 MC 板本身存在故障，或者 MC 板上连接模块存在故障。请拔下所有插头，保留 MC 电源线（序号 11），重新开机观察 MC 板是否恢复正常。  
  若**恢复正常**，请关机后逐个安装拔下的插头，开机观察灯语是否再次异常，找到具体故障组件后更换该组件；  
  若**依旧故障**，则需要更换 MC 板，可参考[该Wiki](../maintenance/replace-mc-board-and-the-cooling-fan.md)。

> 对于 MC 板本身损坏的情况，若您能够使用万用表测量保险丝状态，可切换电阻档测量下图元器件的电阻值是否几乎为 0Ω。

|  |  |
| --- | --- |
| mc.jpg | resis.jpg |

若阻值很大，说明 MC 板的保险丝烧毁了。请打开 AP 盖板，检查 MC-AP 线缆的绝缘层是否被压破，并调整线缆避免与盖板卡扣相互挤压。

> 若您没有万用表，我们也建议您额外检查 MC-AP 线缆。

|  |  |
| --- | --- |
|  |  |
| cable.jpg | cable2.jpg |

### 3. 排查 AP 板模块

#### 指示灯状态

AP 板指示灯快速闪烁（左）、常亮（右）。

从靠近前门一侧打开 AP 板盖，断开左 LED 灯，观察 AP 板指示灯。

|  |  |
| --- | --- |
|  |  |

![ap_light.webp](https://wiki.bambulab.com/general/bbl-indicator-led/ap_light.webp)

#### AP 板指示灯正常

请进一步排查 TH 板工作状态。

#### AP 板指示灯异常

关机后参考[更换 X2D AP 板](../maintenance/replace-ap-board.md)断开 AP 板上的所有插头，保留 8 号和 9 号，然后开机观察 AP 板指示灯是否依然异常。

![ap_connectors_007.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/ap_board/014_ap_board_instruction.png)

| 序号 | 接口说明 | 序号 | 接口说明 | 序号 | 接口说明 | 序号 | 接口说明 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 屏幕排线 | 4 | 实况摄像头 | 7 | LED 补光灯-左 | 10 | USB-C 线 |
| 2 | Wi-Fi 天线 | 5 | U 盘接口组件 | 8 | MC 板（通信） |  |  |
| 3 | 开门检测开关 | 6 | LED 补光灯-前 | 9 | MC 板（供电） |  |  |

- AP 板恢复正常：说明故障原因在其他拔下的某个插头中。**先重新连接 10 号线缆并开机观察 MC/AP 指示灯**，若灯语异常，则进一步排查 TH 板模块。若此时开机后灯语正常，再关机逐次逐个安装其他组件的插头，并开机**观察灯语是否再次异常**，找到具体故障组件后更换该组件。
- AP 板依旧异常：可能是 MC-AP 线缆存在故障，需拔下 AP 板上的 8 号和 9 号插头，开机观察 MC 板是否恢复正常。若 MC 板依旧异常，则需要[更换 MC-AP 线缆](https://wiki.bambulab.com/zh/p2s/maintenance/replace-mc-ap-cable-pack-(2-in-1))；若恢复正常则需要更换 AP 板。

**MC 板指示灯正常状态**

MC 板指示灯常亮（上）、慢速闪烁（下）。

请参考[更换 X2D 背板](../maintenance/replace-rear-panel.md)移除打印机背板，观察 MC 板指示灯。

![mc_light.webp](https://wiki.bambulab.com/general/bbl-indicator-led/mc_light.webp)

### 4. 排查 TH 板模块

#### 指示灯状态

TH 板指示灯快速闪烁。

请参考[更换 X2D 工具头外壳](../maintenance/replace-toolhead-housing.md)来移除工具头后盖，观察 TH 板指示灯。

![th_light.webp](https://wiki.bambulab.com/general/bbl-indicator-led/th_light.webp)

#### 操作步骤

关机后断开下图所示的插头，然后开机观察 MC/AP 板指示灯是否依然异常。

![22_022.png](https://public-cdn.bblmw.com/wiki/new/x2d/maintenance/replace_th_board/003_disconnect_the_th_board_cable_connection.png)

| 序号 | 接口说明 | 序号 | 接口说明 | 序号 | 接口说明 |
| --- | --- | --- | --- | --- | --- |
| 1 | 热端加热组件接口板 | 4 | 工具头摄像头 | 7 | 左热端风扇线缆 |
| 2 | 工具头接口板 | 5 | 辅助热端风扇线缆 |  |  |
| 3 | 挤出电机 | 6 | 堵嘴组件 |  |  |

- MC/AP 板恢复正常：说明故障原因在其他拔下的某个插头中。关机后逐个安装其他组件的插头，并开机**观察灯语是否再次异常**，找到具体故障组件后更换该组件。
- MC/AP 板依旧异常：说明可能是工具头线缆存在故障，拔下 USB-C 线缆后开机观察 MC/AP 板指示灯，若灯语依旧异常，则需要 [更换 X2D 的 USB-C 数据线](../maintenance/replace-usb-c-cable.md)；若灯语恢复正常，则需要更换 TH 板。

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的客户支持团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
