---
path: zh/ams3/maintenance/replace-heating-unit
title: "AMS 3H 烘干组件更换指南"
description: ""
tags: []
created: 2026-11-03T13:28:07.265Z
updated: 2026-11-03T13:28:08.322Z
source: https://wiki.bambulab.com/zh/ams3/maintenance/replace-heating-unit
---

## AMS 3H 烘干组件

AMS 烘干组件是 AMS 内部烘干耗材的元件，由加热片，风扇，以及 NTC 温度传感器构成。

![001.jpeg](https://public-cdn.bblmw.com/wiki/new/ams3/maintenance/replace-heating-unit/zh/001.jpeg)

## 何时更换

- 耗材烘干功能异常，出现HMS报错提示需要更换该模块；
- 经技术支持团队判断故障后，确定该模块需要被更换。

## 工具和材料

- H2.0 内六角扳手
- H1.5 内六角扳手

## 安全提示

> 重要提醒 ！
>
> 在对 AMS 及其内部电子设备进行任何维护工作之前，请关闭 AMS 及打印机电源，并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 拆装过程中请避免暴力操作，防止造成零部件或连接结构的二次损伤。
>
> 断开插头前，建议拍照记录各插头的连接位置，便于后续按正确顺序恢复连接。

## 拆装提示

> 本指南是在将 AMS 3H 舱体从支架上移除后的情况操作的，请参考WIKI: [AMS 3H 舱体拆装指南](../../h3c/maintenance/replace-chamber.md)，完成将 AMS 舱体从AMS 支架上移除和安装的操作。

## 移除 AMS 烘干组件

### 第 1 步 移除AMS 3H 进/出气口组件

请参考 WIKI ：[AMS 3H 进/出气口组件更换指南](replace-air-inlet-unit.md)，移除 AMS 3H 进/出气口组件。

![002.jpeg](https://public-cdn.bblmw.com/wiki/new/ams3/maintenance/replace-heating-unit/zh/002.jpeg)

### 第 2 步 移除尾板盖，断开连接线缆

用手扳尾板盖，尾板盖移除。

|  |  |
| --- | --- |
| 003.jpeg | 004.jpeg |

移除 3 根供电线的保护胶套，用 H1.5 内六角扳手按压插头弹片进行解锁插头，断开 3 个快速连接插头。

|  |  |
| --- | --- |
| 005.jpeg | 006.jpeg |

按压插头的锁扣解锁连接器，将 3 根线缆从 AMS 主板上断开，并将线缆从理线卡扣上松出。

|  |  |
| --- | --- |
| 007.jpeg | 008.jpeg |

### 第 3 步 移除 AMS 烘干组件

用 H2.0 内六角扳手移除 6 颗螺丝，将 AMS 烘干组件从 AMS 中框上移除。

|  |  |
| --- | --- |
| 009.jpeg | 010.jpeg |

## 安装 AMS 烘干组件

### 第 1 步 安装烘干组件

先检查电源连接线，确认线缆与安装槽没有干涉，避免安装时压线。然后将烘干组件对齐安装槽安装到 AMS 中框，锁入 6 颗螺丝进行固定。

|  |  |
| --- | --- |
| 011.jpeg | 012.jpeg |

### 第 2 步 连接线缆，安装尾板盖

根据快速连接插头的尺寸匹配，连接 3 根电源线到 AC 板上，装回保护胶套。

|  |  |
| --- | --- |
| 013.jpeg | 014.jpeg |

将 3 根线缆连接到 AMS 主板对应的连接器上，并将线缆整理进线扣中。

![015.jpeg](https://public-cdn.bblmw.com/wiki/new/ams3/maintenance/replace-heating-unit/zh/015.jpeg)

对齐电源接头的位置，将尾板盖扣装到 AMS 上。

![016.jpeg](https://public-cdn.bblmw.com/wiki/new/ams3/maintenance/replace-heating-unit/zh/016.jpeg)

### 第 3 步 安装 AMS 3H 进/出气口组件

请参考 WIKI ：[AMS 3H 进/出气口组件更换指南](replace-air-inlet-unit.md)，安装 AMS 3H 进/出气口组件、AC 板盖和 AMS 主板装饰盖。

## 功能验证

配置好打印机，在屏幕上启动耗材烘干功能，无异常报错即可。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
