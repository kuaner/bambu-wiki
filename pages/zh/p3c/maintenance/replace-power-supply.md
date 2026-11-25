---
path: zh/p3c/maintenance/replace-power-supply
title: "P3C 电源更换指南"
description: "本文介绍了如何更换 P3C 电源"
tags: []
created: 2026-11-24T14:06:12.321Z
updated: 2026-11-24T14:06:12.321Z
source: https://wiki.bambulab.com/zh/p3c/maintenance/replace-power-supply
---

## 电源

简述：打印机的电源是一个输入电压为 AC 100-240V 的交流电，转换为输出电压为 DC 24V 的直流电源的装置，它能为除热床以外的整台打印机提供稳定、干净且符合要求的直流电源。

![001.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-power-supply/zh/001.png)

电源连接端子示意图如下，请根据电源上的标识和线缆颜色来连接。

![002.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-power-supply/zh/002.png)

| 序号 | 端子用途 | 线材颜色 | 序号 | 用途 | 线材颜色 |
| --- | --- | --- | --- | --- | --- |
| 1 | 直流正极输出 | 白色 | 4 | 高压零线输入 | 蓝色 |
| 2 | 直流负极输出 | 白黑色 | 5 | 高压火线输入 | 棕色 |
| 3 | 共用地线 | 黑色（直流）/黄绿色（交流） |  |  |  |

## 何时更换

1. 电源出现明显的物理损坏，如连接器损坏、元器件脱落或烧坏；
2. 经 Bambu Lab 技术支持确认需更换电源。

## 所需工具和材料

- H2.0 内六角扳手
- 十字螺丝刀
- 电源

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 移除电源

### 步骤 1. 移除背板

您可以参考WIKI：[P3C 背板更换指南](replace-back-panel.md) ，完成 6-pin 接口板/缓冲器和背板的移除。

![003.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-power-supply/zh/003.png)

### 步骤 2. 松开电源开关插座

使用 H2.0 内六角扳手移除图示电源开关插座底部与内衬连接的 2 颗螺丝，随后移除后立柱上的地线的 1 颗螺丝；

|  |  |
| --- | --- |
| 004.png | 005.png |

将电源开关插座从内衬上取下。

![006.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-power-supply/zh/006.png)

### 步骤 3. 断开线缆

使用十字螺丝刀拧松电源压线螺丝，断开连接线缆；

|  |  |
| --- | --- |
| 007.png | 008.png |

### 步骤 4. 移除电源

使用 H2.0 内六角扳手移除电源 2 颗螺丝，取下电源。

|  |  |  |
| --- | --- | --- |
| 009.png | 010.png | 011.png |

## 安装电源

### 步骤 1. 安装电源

将电源安装到内衬上，使用 H2.0 内六角扳手锁入 2 颗螺丝固定。

|  |  |
| --- | --- |
| 012.png | 013.png |

### 步骤 2. 连接线缆

请按照下方的连接器说明，将线缆 U 型端子依次插入对应的电源接口，并用十字螺丝刀将压线螺丝拧紧。在使用螺丝刀拧紧螺丝的时候可以用手扶住线缆，避免线缆松脱。

![014.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-power-supply/zh/014.png)

| 序号 | 端子用途 | 线材颜色 | 序号 | 用途 | 线材颜色 |
| --- | --- | --- | --- | --- | --- |
| 1 | 直流正极输出 | 白色 | 4 | 高压零线输入 | 蓝色 |
| 2 | 直流负极输出 | 白黑色 | 5 | 高压火线输入 | 棕色 |
| 3 | 共用地线 | 黑色（直流）/黄绿色（交流） |  |  |  |

### 步骤 3. 安装电源开关插座

将电源开关插座装回内衬，并使用 H2.0 内六角扳手锁入 2 颗固定螺丝与 1 颗立柱地线螺丝；

|  |  |
| --- | --- |
| 015.png | 016.png |

### 步骤 4. 安装背板

您可以参考WIKI：[P3C 背板更换指南](replace-back-panel.md) ，完成背板和其他配件的安装。

![017.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-power-supply/zh/017.png)

## 功能验证

连接电源，打开打印机并执行设备校准操作，校准通过则更换成功。

## 所涉及到的螺丝（非必要）

更多关于螺丝相关内容介绍可参考 [Bambu Lab 常见螺钉](../../knowledge-sharing/common-screws.md)。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
