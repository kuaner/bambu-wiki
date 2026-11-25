---
path: zh/p3c/maintenance/replace-adaptive-airflow-fan-back
title: "P3C 后自适应风扇更换指南"
description: "本文介绍了如何更换 P3C 后自适应风扇"
tags: []
created: 2026-11-24T14:06:12.520Z
updated: 2026-11-24T14:06:12.520Z
source: https://wiki.bambulab.com/zh/p3c/maintenance/replace-adaptive-airflow-fan-back
---

## 后自适应风扇

简述：安装在左内衬后方，为腔室提供气流动力。单品包含风扇本体与外罩。

![001.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-adaptive-airflow-fan-back/zh/001.png)

## 何时更换

- 风扇外壳物理损坏；
- HMS 提示故障并经 Bambulab 技术支持确认需要更换的。

## 所需工具和材料

- H2.0 内六角扳手
- 后自适应风扇

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 移除后自适应风扇

### 步骤 1. 移除背板

您可以参考WIKI[P3C 背板更换指南](replace-back-panel.md)，完成 6-pin 接口板/缓冲器和背板的移除。

![002.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-adaptive-airflow-fan-back/zh/002.png)

### 步骤 2. 移除后自适应风道组件

您可以参考Wiki: [P3C 后自适应风道组件更换指南](replace-adaptive-airflow-duct-back.md)，完成后自适应风道组件的移除。

![003.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-adaptive-airflow-fan-back/zh/003.png)

### 步骤 3. 移除自适应风扇

使用 H2.0 内六角扳手，移除左侧板后方 3 颗螺丝和左侧板底部的 2 颗螺丝；

|  |  |
| --- | --- |
| 004.png | 005.png |

风扇外罩共有 4 颗螺丝固定，先移除风扇左侧 1、2 号共 2 颗螺丝，将内六角扳手伸入图示打印机金属框架上的预留孔中移除 3 号螺丝；

|  |  |
| --- | --- |
| 006.png | 007.png |

小幅度扳动左侧板，露出 4 号螺丝预留孔，按图示操作使用内六角扳手移除 4 号螺丝后取下自适应风扇；

|  |  |
| --- | --- |
| 008.png | 009.png |

## 安装后自适应风扇

### 步骤 1. 安装自适应风扇

将自适应风扇对齐螺丝孔安装到左内衬上，使用 H2.0 内六角扳手锁入 1、2 号 2 颗螺丝固定；

|  |  |
| --- | --- |
| 010.png | 011.png |

随后将扳手穿过螺丝预留孔，依次锁紧 3 、4 号螺丝；

|  |  |
| --- | --- |
| 012.png | 013.png |

使用 H2.0 内六角扳手，锁入左侧板后方 3 颗螺丝和左侧板底部的 2 颗螺丝。

|  |  |
| --- | --- |
| 014.png | 015.png |

### 步骤 2. 安装后自适应风道组件

您可以参考Wiki: [P3C 后自适应风道组件更换指南](replace-adaptive-airflow-duct-back.md)，完成后自适应风道组件的安装。

![016.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-adaptive-airflow-fan-back/zh/016.png)

### 步骤 3. 安装背板

您可以参考WIKI[P3C 背板更换指南](replace-back-panel.md)，完成 6-pin 接口板/缓冲器和背板的安装。

![017.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-adaptive-airflow-fan-back/zh/017.png)

## 功能验证

接通电源并开机，在屏幕上开启后自适应风扇，无报错或异常提示。

![018.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-adaptive-airflow-fan-back/zh/018.png)

## 所涉及到的螺丝（非必要）

更多关于螺丝相关内容介绍可参考 [Bambu Lab 常见螺钉](../../knowledge-sharing/common-screws.md)。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
