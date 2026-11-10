---
path: zh/h3c/maintenance/replace-chamber-liner-back-left
title: "拓竹H3C 左后内衬更换指南"
description: "本文介绍了如何更换拓竹H3C 左后内衬"
tags: []
created: 2026-11-06T09:31:37.384Z
updated: 2026-11-10T09:14:10.635Z
source: https://wiki.bambulab.com/zh/h3c/maintenance/replace-chamber-liner-back-left
---

## 左后内衬

安装在打印机的左后侧，用于隔离打印区并为一些功能配件提供安装空间的塑料配件。

![001.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-chamber-liner-back-left/zh/001.jpg)

## 何时更换

左后内衬出现结构损坏或变形，影响其他配件的安装或干涉其他配件的运动。

## 工具和材料

- H2.0 内六角扳手
- H1.5 内六角扳手

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 拆装提示

> 1. 打印机侧板的拆装需要提前移除 AMS 3H，请参考 WIKI： [AMS 3H 拆除与安装指南](replace-ams3.md)，将 AMS 3H 从打印机上移除和重新安装，本指南的操作均在已移除 AMS 3H 的场景下进行。
> 2. 根据更换侧板的操作指南，在断电前，先将热床下降到底部。

## 移除左后内衬

### 第 1 步 移除左自适应风道组件

请参考 WIKI：[左辅助部件冷却风扇风道更换指南](replace-auxiliary-part-cooling-fan-duct-left.md) 的步骤，依次移除背板、玻璃前门、左侧板和左自适应风道组件（不需要拆下辅助部件冷却风扇）。

![002.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-chamber-liner-back-left/zh/002.jpg)

### 第 2 步 移除左后内衬上的配件

请参考 WIKI：[后自适应风道组件及后腔温组件更换指南](replace-adaptive-airflow-assembly-back.md)，移除后适应风道组件和后腔温组件，并将上面的线缆都移除到左后内衬外。

![003.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-chamber-liner-back-left/zh/003.jpg)

然后从腔体内拆下滤芯盖和空气滤芯。

![004.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-chamber-liner-back-left/zh/004.jpg)

### 第 3 步 移除左后内衬

用 H2.0 内六角扳手移除左后内衬底部的 3 颗固定螺丝（细牙螺丝），移除顶部的 3 颗固定螺丝（粗牙螺丝），侧面的 3 颗固定螺丝（细牙螺丝），然后先将顶部倒向前门方向，移除左后内衬。

|  |  |
| --- | --- |
| 005.jpg | 006.jpg |
| 007.jpg | 008.jpg |

## 安装左后内衬

### 第 1 步 安装左后内衬

从前往后将左后内衬放置到位，对齐螺丝孔，然后依次预锁入（即先不要直接锁紧）各位置的螺丝（顶部的 3 颗螺丝是粗牙螺丝），待 9颗螺丝都拧入后，再进行锁紧。

|  |  |
| --- | --- |
| 009.jpg | 010.jpg |
| 011.jpg | 012.jpg |

### 第 2 步 安装配件到左后内衬

请参考 WIKI：[后自适应风道组件及后腔温组件更换指南](replace-adaptive-airflow-assembly-back.md)，安装后腔温组件和后适应风道组件，并整理好线缆。

![013.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-chamber-liner-back-left/zh/013.jpg)

装回空气滤芯和滤芯盖。

![014.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-chamber-liner-back-left/zh/014.jpg)

### 第 3 步 安装左自适应风道组件、左侧板和背板

请参考 WIKI：[左辅助部件冷却风扇风道更换指南](replace-auxiliary-part-cooling-fan-duct-left.md) 的步骤，依次安装左自适应风道组件（不需要拆下辅助部件冷却风扇）、左侧板、玻璃前门和背板。

![015.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-chamber-liner-back-left/zh/015.jpg)

## 功能验证

1. 启动打印机并进入空调系统界面，切换到腔温模式；
2. 设置腔温为 60 ℃；
3. 确认加热器和风扇能正常开启。

![016.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-chamber-liner-back-left/zh/016.jpg)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
