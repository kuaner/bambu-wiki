---
path: zh/r1/maintenance/xy-axis
title: "R1 导轨维护指南"
description: "本文将介绍如何维护 R1 的 X 轴和 Z 轴。"
tags: []
created: 2026-09-22T12:47:01.488Z
updated: 2026-09-22T13:11:10.019Z
source: https://wiki.bambulab.com/zh/r1/maintenance/xy-axis
---

## 介绍

激光加工过程中产生的烟雾或粉尘通常无法立刻排出，会短暂接触 X 轴和 Z 轴，因此定期润滑 X/Z 导轨将减少导轨的机械磨损，保证切割精度。表面的润滑油膜也能够防止生锈，并降低电机负载，从而延长设备使用寿命。

## 维护周期

- 可通过屏幕上的维护页面查看设备健康度。对于 X 轴，设备会根据加工时间和 X 轴的行驶距离进行综合计算，并在达到特定条件时弹窗提醒，建议用户及时进行维护；
- 使用 100 小时后，对 X 轴进行一次维护；
- 使用 200 小时后，对 Z 轴进行一次维护；

## 安全提示

> 在对激光切割机及其电子设备（包括工具头线缆）进行任何维护前，请先关闭设备电源并断开电源连接，以防屏幕误触或电路短路造成额外的设备损坏与安全隐患。维护或排查故障前，请确认相关部件已冷却。

## 需要使用的工具

- 清洁湿巾
- 润滑脂

![001.png](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/xy-axis/zh/001.png)

- 润滑油

![002.png](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/xy-axis/zh/002.png)

## 维护步骤

### X 轴

关机后使用干净的清洁湿巾擦拭 X 轴，擦拭一次后换干净的一面继续擦拭。

|  |  |
| --- | --- |
| 003.png | 004.png |

当湿巾擦拭面不再能够擦出黄色污渍后，擦拭同步带。

![005.png](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/xy-axis/zh/005.png)

按住工具头擦拭同步带，完成后开始润滑。

![006.png](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/xy-axis/zh/006.png)

在 X 轴上涂抹足够的**润滑脂。**

![007.png](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/xy-axis/zh/007.png)

完成后，左右拉动工具头，确保润滑脂遍布 X 轴。

![008.webp](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/xy-axis/zh/008.webp)

使用纸巾小心擦除多余的润滑脂。

![009.webp](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/xy-axis/zh/009.webp)

### Z 轴初步维护

使用 H1.5 内六角螺丝刀拆卸图示两颗螺丝。

|  |  |
| --- | --- |
| 010.jpg | 011.jpg |

取下工具头前盖。

![012.webp](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/xy-axis/zh/012.webp)

从上往下，向内部滴入 2-3 滴润滑油。

![013.png](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/xy-axis/zh/013.png)

再回到下方，滴上 1-2 滴润滑油

![014.png](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/xy-axis/zh/014.png)

上下推拉聚焦镜部分，确保导轨得到充分润滑。

![015.webp](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/xy-axis/zh/015.webp)

### Z 轴深度维护

若观察到导轨附近有明显黄色污渍，可进行深度维护。

请先参考[TH 板更换指南](replace-th-board.md)提前拆除部分零件。

使用新的清洁湿巾擦拭导轨。

|  |  |
| --- | --- |
| 016.png | 017.png |

在左右两侧重新补充**润滑油。**

|  |  |
| --- | --- |
| 018.png | 019.png |

上下推动，确保导轨被重复润滑。

![020.png](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/xy-axis/zh/020.png)

完成后，参考[TH 板更换指南](replace-th-board.md)装回所有零件。

### 校准

在屏幕的设置-校准中开启“振动补偿校准”，等待完成。

![021.png](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/xy-axis/zh/021.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
