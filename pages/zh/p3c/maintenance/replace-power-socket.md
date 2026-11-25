---
path: zh/p3c/maintenance/replace-power-socket
title: "P3C 电源开关插座更换指南"
description: "本文介绍了如何更换 P3C 电源开关插座"
tags: []
created: 2026-11-24T14:06:13.425Z
updated: 2026-11-24T14:06:13.425Z
source: https://wiki.bambulab.com/zh/p3c/maintenance/replace-power-socket
---

## 电源开关插座

简述：电源开关插座是安装在打印机背面的电源线插座，是外部电源在打印机上的接入口，它包含一个电源线插座、一个控制打印机电源的开关以及一些线缆。

![001.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-power-socket/zh/001.png)

## 何时更换

- 电源指示灯不能正常亮起
- 电源开关插座有烧坏的痕迹
- 开关结构件损坏

## 所需工具和材料

- H2.0 内六角扳手
- 十字螺丝刀
- 电源开关插座

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 移除电源开关插座

### 步骤 1. 移除背板与废料滑梯

您可以参考WIKI：[P3C 废料滑梯更换指南](replace-purge-chute.md)，完成背板与废料滑梯的移除。

![002.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-power-socket/zh/002.png)

### 步骤 2. 断开线缆

使用十字螺丝刀，拧松图示 AC 板、电源上的 5 颗压线螺丝，并断开线缆。

|  |  |
| --- | --- |
| 003.png | 004.png |

### 步骤 3. 移除电源开关插座

使用 H2.0 内六角扳手移除图示电源开关插座底部与内衬连接的 2 颗螺丝，随后移除后立柱上的地线固定螺丝；

|  |  |
| --- | --- |
| 005.png | 006.png |

将线缆从内衬上的理线扣中松出，移除电源开关插座。

|  |  |
| --- | --- |
| 007.png | 008.png |

## 安装电源开关插座

### 步骤 1. 安装电源开关插座

将电源开关插座安装到内衬，使用 H2.0 内六角螺丝锁入电源开关插座的 2 颗螺丝固定，随后再锁入 1 颗螺丝将地线固定在后立柱上。

|  |  |
| --- | --- |
| 009.png | 010.png |

### 步骤 2. 连接线缆

逐一将 5 根线缆的 U 型端子卡入对应的压线螺丝方形金属片下方，使用十字螺丝刀拧紧压线螺丝使线缆固定到位，并盖上 AC 板电源线保护盖。

|  |  |
| --- | --- |
| 011.webp | 012.png |

将电源开关插座的线缆理顺并卡入理线扣中。

![013.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-power-socket/zh/013.png)

> 拆装提示：MC 板 “V-” 极通过一根黑色线缆与电源模块接地端相连。安装时，需将该黑线与黄绿色地线的 U 型端子叠放，一并锁入电源模块接地极的压线螺丝中。

![014.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-power-socket/zh/014.png)

### 步骤 3. 安装废料滑梯与背板

您可以参考WIKI：[P3C 废料滑梯更换指南](replace-purge-chute.md)，完成废料滑梯、背板及其余配件的安装。

![015.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-power-socket/zh/015.png)

## 功能验证

连接电源并打开打印机，操作设备校准流程，能够顺利完成校准。

## 所涉及到的螺丝（非必要）

更多关于螺丝相关内容介绍可参考 [Bambu Lab 常见螺钉](../../knowledge-sharing/common-screws.md)。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
