---
path: zh/h2/troubleshooting/failure-to-power-on-part1
title: "H2 系列打印机上电异常排查指南-上篇"
description: "本指南介绍了 H2 系列打印机开机后不上电的故障排除方法，指南的上篇旨在排查铁壳电源指示灯异常情况。"
tags: ["h2d"]
created: 2025-10-10T06:46:46.856Z
updated: 2026-03-11T07:16:17.072Z
source: https://wiki.bambulab.com/zh/h2/troubleshooting/failure-to-power-on-part1
---

> **注意**：本页面以 H2D 机器为例。**H2S 和 H2C 的维护步骤完全相同**。

## 何时使用？

1. 接通电源后，打印机屏幕无反应。
2. 同时，其他电子元件的指示灯也部分或全部异常，例如铁壳电源指示灯未亮、或热床下方的状态指示灯未亮。
3. 打印机主要主板，如AP板的指示灯同样未亮或灯语异常。

|  |  |
| --- | --- |
| 屏幕不能亮.jpg   屏幕不亮 | 电源板灯不亮.png   铁壳电源指示灯未亮 |

## 排查须知

正式排查前首先需要观察打印机各部位指示灯状态。通过观察打印机状态指示灯的颜色变化与闪烁方式，可以快速识别打印机当前所处的工作状态，如空闲、准备、执行任务或报错等。状态指示灯作为打印机的“视觉语言”，能够在无需查看屏幕的情况下，提供直观的状态反馈。

- 开关插座指示灯正常状态：常亮

![开关灯.png](https://wiki.bambulab.com/h2/maintenance/failure-to-power-on/%E5%BC%80%E5%85%B3%E7%81%AF.png)

- 铁壳电源指示灯正常状态：常亮

![电源板灯.png](https://wiki.bambulab.com/h2/maintenance/failure-to-power-on/%E7%94%B5%E6%BA%90%E6%9D%BF%E7%81%AF.png)

- 热床下方打印机状态指示灯正常状态：UI上打开指示灯后，常亮或闪烁

![闲置.webp](https://wiki.bambulab.com/h2/manual/status-indicator-light-meanings/%E9%97%B2%E7%BD%AE.webp)

- AP 板指示灯正常状态：左侧灯快速闪烁、右侧灯常亮

![board-location.png](https://wiki.bambulab.com/h2/maintenance/failure-to-power-on/board-location.png)  
<https://public-cdn.bblmw.com/wiki/H2D/AP-1.mp4>

> **请注意区分以下两种情况：**
>
> 1. 打印机可以开机但主电路未上电：几乎所有电子元件均无供电，此类情况适用于本文的排查建议。
> 2. 开机后仅屏幕无显示：仅屏幕背光不亮，其他电子元件指示灯正常（如前述）。此时通常只需更换屏幕、AP 板，或检查并重新连接屏幕与 AP 板之间的排线。该情况不适用下文的故障排查流程，建议参考 [屏幕拆装教程](../maintenance/replace-touchscreen.md) 重新插拔屏幕插头。

## 故障原因

铁壳电源的作用是将交流电（AC）转换为 24V 直流电（DC）。后级电路，如 MC 板、AP 板、TH 板等，均依赖铁壳电源提供的 24V 电压才能正常上电并启动。

![铁壳电源电路图中文.png](https://wiki.bambulab.com/h2/maintenance/failure-to-power-on/%E9%93%81%E5%A3%B3%E7%94%B5%E6%BA%90%E7%94%B5%E8%B7%AF%E5%9B%BE%E4%B8%AD%E6%96%87.png)

H2 系列打印机开机后不上电最有可能的原因之一，是铁壳电源的 24V 输出功能异常。 造成该异常的原因通常有以下两种：

### 1. 铁壳电源的 AC 交流电源输入异常

安全钥匙与急停开关安装在铁壳电源的输入端，用于控制铁壳电源是否接入交流电（AC）。

如果安全钥匙或急停开关的插头未正确插入、出现松动、或急停按钮被误按下，或安全钥匙组件链路异常（前三种情况较为常见，后一种情况极为少见），都会导致铁壳电源模组无法获得 AC 交流电输入，从而无法输出 24V 直流电压。

### 2. 铁壳电源模组本体异常

铁壳电源模组的 AC 交流电源输入正常的情况下，由于铁壳电源模组本体出现故障，也会导致 24V 电源输出异常。

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行故障排查或维护时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 所需的工具

- H 2.0内六角螺丝刀和十字螺丝刀
- 镊子

请确保在使用这些工具时采取适当的安全措施，并遵循以下操作建议：

- 在进行任何插头拔插之前，请确保打印机已经断开电源，并且电源线已拔出插座。
- 请使用正确尺寸的内六角扳手进行拆卸和安装操作，以避免损坏螺丝或工具。
- 使用镊子时，请小心操作，避免损坏或弯曲零件。

## 排查步骤

本排查指南旨在判断铁壳电源模组的 AC 输入是否正常。

> 若铁壳电源指示灯常亮，则表示铁壳电源 24V 输出正常，可跳过此指南的步骤，直接根据《H2 系列打印机上电异常排查指南-下篇》（建设中，敬请期待），以排查主板及其级联电路中的故障部件。

![diagram_排查指南.png](https://wiki.bambulab.com/h2/maintenance/failure-to-power-on/diagram_%E6%8E%92%E6%9F%A5%E6%8C%87%E5%8D%97.png)

### 1. 检查电源线是否破损

先将电源线从插座上拔下，检查整条线缆外部绝缘层是否完整。如果存在受压破损的情况，请停止使用该线缆并更换。  
![power-cable.jpeg](https://wiki.bambulab.com/h2/maintenance/failure-to-power-on/power-cable.jpeg)

### 2. 检查电源插座是否松动

确保电源线完全插入电源插座，没有明显的松动。另外，请检查所使用的电源线是否为打印机原装电源线。  
![power-cable-h2.png](https://wiki.bambulab.com/h2/maintenance/failure-to-power-on/power-cable-h2.png)

### 3. 检查安全钥匙或是否松动

建议重新插拔安全钥匙，确保插到底，推不动为止。

![安全钥匙.png](https://wiki.bambulab.com/h2/maintenance/failure-to-power-on/%E5%AE%89%E5%85%A8%E9%92%A5%E5%8C%99.png)

### 4.（若安装了急停钥匙）检查急停按键线缆是否松动

![](https://wiki.bambulab.com/h2/laser/image-94.png)

### 5.（若安装了急停钥匙）检查是否安装安全钥匙或急停按键是否被误按下

检查急停按钮上的钥匙孔是否插入了安全钥匙，如没有，请插入安全钥匙。请注意，急停按钮线缆插头和安全钥匙与插孔是具有方向性的。  
![](https://wiki.bambulab.com/h2/troubleshooting/hmscode/0500-0400-0001-0051/image-3_cn.png)

检查急停按键是否被误按下。若被按下，您可以参考下图方法顺时针旋转并向上拔出以解锁急停按键。

![急停按键.webp](https://wiki.bambulab.com/h2/maintenance/failure-to-power-on/%E6%80%A5%E5%81%9C%E6%8C%89%E9%94%AE.webp)

### 6. 检查安全钥匙组件是否异常

若确认安全钥匙和急停按键安装均正确，但铁壳电源指示灯仍然不亮，请进行以下排查:

1. 拆开打印机背板。请参考此 wiki [更换 H2 系列打印机背板](../maintenance/replace-rear-panel.md) 。
2. 根据此 wiki [更换 H2D 电源安全钥匙组件](../maintenance/replace-power-safety-key-unit.md) 的步骤1-3步，检查安全钥匙组件是否异常，若有线缆脱 pin 或明显异常，则需要根据所述指南更换安全钥匙组件。
3. 如果安全钥匙组件未发现明显异常，请继续下一步排查。

|  |  |
| --- | --- |
| 安全钥匙组件1.png | 安全钥匙组件2.png |

### 7. 断开 24V 直流输出电源

如果安全钥匙组件未发现明显异常，可继续向上扣开透明保护壳。使用十字螺丝刀，拧松下图红色标记所示电源连接线的固定螺丝。**注意：这2颗螺丝无需完全取下螺丝，拧松即可，** 然后将螺丝下方固定的线缆向下拔出，以断开 24V 直流输出。

![断开_24v_直流输出电源.png](https://wiki.bambulab.com/h2/maintenance/failure-to-power-on/%E6%96%AD%E5%BC%80_24v_%E7%9B%B4%E6%B5%81%E8%BE%93%E5%87%BA%E7%94%B5%E6%BA%90.png)

随后重新开机，检查指示灯状态是否恢复正常：

- 若指示灯仍异常，则需更换铁壳电源模组。请参阅此 wiki ：[更换 H2D 电源](../maintenance/replace-internal-power-supply.md)。
- 若指示灯恢复正常，请参照[《H2 系列打印机上电异常排查指南-下篇》](../../h2d/troubleshooting/h2/failure-to-power-on-part2.md)进行后续排查，H2S设备请参考[《H2S 打印机上电异常排查指南》](../../h2s/failure-to-power-on.md)。

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
