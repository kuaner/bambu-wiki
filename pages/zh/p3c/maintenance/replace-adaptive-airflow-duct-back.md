---
path: zh/p3c/maintenance/replace-adaptive-airflow-duct-back
title: "P3C 后自适应风道组件更换指南"
description: "本文介绍了如何更换 P3C 后自适应风道组件"
tags: []
created: 2026-11-24T14:06:06.225Z
updated: 2026-11-24T14:06:06.225Z
source: https://wiki.bambulab.com/zh/p3c/maintenance/replace-adaptive-airflow-duct-back
---

## 后自适应风道组件

简述：安装在打印机后侧的风道组件，并内置了散热风扇，为腔室提供定向气流。

![001.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-adaptive-airflow-duct-back/zh/001.png)

## 何时更换

- 风门切换失败
- 控制电路板烧坏或连接器损坏
- HMS 提示故障并经Bambulab技术支持确认需更换后自适应风道组件

## 所需工具和材料

- H2.0 内六角扳手
- 后自适应风道组件

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 移除后自适应风道组件

### 步骤 1. 移除背板

您可以参考WIKI[P3C 背板更换指南](replace-back-panel.md)，完成 6-pin 接口板/缓冲器和背板的移除。

![002.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-adaptive-airflow-duct-back/zh/002.png)

### 步骤 2. 移除后自适应风道组件

使用 H2.0 内六角扳手，移除后自适应风道组件的 3 颗螺丝；随后松出风道组件，并依次按压白色连接器端子解锁卡扣断开线缆，移除风道组件。

|  |  |
| --- | --- |
| 003.png | 004.png |

## 安装后自适应风道组件

### 步骤 1. 安装后自适应风道组件

连接线缆，随后将风道组件安装到左内衬上，并使用 H2.0 内六角扳手锁入 3 颗螺丝固定。

|  |  |
| --- | --- |
| 005.png | 006.png |

### 步骤 2. 安装背板

您可以参考WIKI：[P3C 背板更换指南](replace-back-panel.md)，完成 6-pin 接口板/缓冲器和背板的安装。

![007.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-adaptive-airflow-duct-back/zh/007.png)

## 功能验证

接通电源并开机，在屏幕上切换腔温模式，切换过程顺畅，无报错或异常提示。

## 所涉及到的螺丝（非必要）

更多关于螺丝相关内容介绍可参考 [Bambu Lab 常见螺钉](../../knowledge-sharing/common-screws.md)。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
