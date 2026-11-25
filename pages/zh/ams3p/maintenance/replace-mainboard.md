---
path: zh/ams3p/maintenance/replace-mainboard
title: "P3C AMS 主板更换指南"
description: "本文介绍了如何更换 P3C AMS 主板"
tags: []
created: 2026-11-24T14:09:00.419Z
updated: 2026-11-24T14:09:00.419Z
source: https://wiki.bambulab.com/zh/ams3p/maintenance/replace-mainboard
---

## AMS 主板

简述：AMS主板是 AMS 的核心电路板，它提供了一系列连接器，通过这些连接器和连接电缆将各种功能组件连接起来。

![001.png](https://public-cdn.bblmw.com/wiki/new/ams3p/maintenance/replace-mainboard/zh/001.png)

## 何时更换

当出现 AMS 主板板件电压异常、元器件异常发热或烧坏、模块间的通信异常、连接器损坏、不可恢复的固件升级失败等故障时，可能需要更换 AMS 主板。

## 所需工具和材料

- H1.5 内六角扳手
- H2.0 内六角扳手
- AMS 主板

## 安全提示

> 重要提醒 ！
>
> 在对 AMS 及其内部电子设备进行任何维护工作之前，请关闭 AMS 及打印机电源，并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 拆装过程中请避免暴力操作，防止造成零部件或连接结构的二次损伤。
>
> 断开插头前，建议拍照记录各插头的连接位置，便于后续按正确顺序恢复连接。

## 版本提示

由于设计变更，AMS 主板下方的线缆线扣存在两种版本，二者仅线缆线扣位置不同，不影响拆装方式。

![002.png](https://public-cdn.bblmw.com/wiki/new/ams3p/maintenance/replace-mainboard/zh/002.png)

## 移除AMS 主板

### 步骤 1. 移除 AMS 舱体

您可以参考WIKI [AMS 3P 舱体拆装指南](../../p3c/maintenance/replace-chamber.md)，对 AMS 舱体进行移除。

> 注意：在移除或安装 AMS 舱体前，请先执行退料操作，并取出舱内的所有料盘。若未退料，残留的耗材可能在
>
> 安装时被夹断或卡住，导致后续进退料困难；同时，料盘的自重也会增加操作难度。
>
> |  |  |
> | --- | --- |
> | 003.png | 004.png |

### 步骤 2. 移除 AMS 主板装饰盖

使用 H1.5 内六角扳手，移除 AMS 主板装饰盖的 4 颗螺丝，随后取下装饰盖。

![005.png](https://public-cdn.bblmw.com/wiki/new/ams3p/maintenance/replace-mainboard/zh/005.png)

### 步骤 3. 移除 AMS 主板

逐一断开 AMS 主板连接器，并使用 H1.5 内六角螺丝移除 2 颗螺丝，取下 AMS 主板。

![006.png](https://public-cdn.bblmw.com/wiki/new/ams3p/maintenance/replace-mainboard/zh/006.png)

## 安装AMS 主板

### 步骤 1. 安装 AMS 主板

将 AMS 主板对准图示位置的定位销安装到位，并使用 H1.5 内六角扳手固定 2 颗螺丝，随后将连接器插入AMS 主板上的连接器座。

![007.png](https://public-cdn.bblmw.com/wiki/new/ams3p/maintenance/replace-mainboard/zh/007.png)

AMS 主板线缆说明如下：

![008.png](https://public-cdn.bblmw.com/wiki/new/ams3p/maintenance/replace-mainboard/zh/008.png)

### 步骤 2. 装回 AMS 主板装饰盖；

将 AMS 主板装饰盖对齐图示的耗材直通口装入，并使用 H1.5 内六角扳手锁紧装饰盖 4 颗螺丝。

|  |  |
| --- | --- |
| 009.png | 010.png |

### 步骤 3. 装回AMS舱体

您可以参考WIKI：[AMS 舱体拆装指南](../../p3c/maintenance/replace-chamber.md)，对 AMS 舱体进行移除。

## 功能验证

连接电源线，将 AMS 连接到打印机，打开电源，通过机器屏幕的操作，AMS 能完成上料动作并且整个上料过程无错误提示。

## 所涉及到的螺丝（非必要）

更多关于螺丝相关内容介绍可参考 [Bambu Lab 常见螺钉](../../knowledge-sharing/common-screws.md)。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
