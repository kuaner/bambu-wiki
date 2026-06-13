---
path: zh/x2d/troubleshooting/led-fill-light-troubleshooting-guide
title: "P2S/X2D LED 补光灯故障排查指南"
description: "本文将介绍 LED 补光灯无法点亮后的故障排查方法。"
tags: ["p2s", "x2d"]
created: 2026-06-01T09:36:28.413Z
updated: 2026-06-10T03:28:35.390Z
source: https://wiki.bambulab.com/zh/x2d/troubleshooting/led-fill-light-troubleshooting-guide
---

## 故障描述

P2S 和 X2D 的打印机仓内有两条 LED 补光灯，分别位于 AP 板盖和前面盖上。当某一补光灯无法工作，或两条补光灯都无法工作时，可参考本文进行故障排查。

|  |  |
| --- | --- |
|  | pixpin_2026-06-01_14-59-12.jpg |

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 排查步骤

### 情况一：前补光灯故障

首先轻轻撬开 AP 盖板。

![1.jpg](https://wiki.bambulab.com/x2d/troubleshooting/led-fill-light-troubleshooting-guide/1.jpg)

找到 AP 板上的补光灯插头。

![pixpin_2026-06-01_19-45-40.jpg](https://wiki.bambulab.com/x2d/troubleshooting/led-fill-light-troubleshooting-guide/pixpin_2026-06-01_19-45-40.jpg)

对调安装前补光灯和侧补光灯的线缆插头。

> 按下插头顶部的防松卡扣后，即可拔下插头。

![pixpin_2026-06-02_10-50-42.jpg](https://wiki.bambulab.com/x2d/troubleshooting/led-fill-light-troubleshooting-guide/pixpin_2026-06-02_10-50-42.jpg)

重新开机后观察前补光灯是否正常亮起。

- 前补光灯正常亮起，侧补光灯无法亮起：前补光灯功能正常，但 AP 主板或主板上插座故障，需更换 AP 板。

  P2S: [更换 P2S AP 板](../../p2s/maintenance/replace-ap-board.md)  
  X2D：[更换 X2D AP 板](../maintenance/replace-ap-board.md)
- 侧补光灯正常亮起，前补光灯无法亮起：AP 主板上的插座正常，但前补光灯存在故障，需[更换前补光灯](../../p2s/maintenance/replace-led-light-front.md)。

### 情况二：侧补光灯故障

首先轻轻撬开 AP 盖板。

![1.jpg](https://wiki.bambulab.com/x2d/troubleshooting/led-fill-light-troubleshooting-guide/1.jpg)

找到 AP 板上的补光灯插头。

![pixpin_2026-06-01_19-45-40.jpg](https://wiki.bambulab.com/x2d/troubleshooting/led-fill-light-troubleshooting-guide/pixpin_2026-06-01_19-45-40.jpg)

对调安装前补光灯和侧补光灯的线缆插头。

> 按下插头顶部的防松卡扣后，即可拔下插头。

![pixpin_2026-06-02_10-50-42.jpg](https://wiki.bambulab.com/x2d/troubleshooting/led-fill-light-troubleshooting-guide/pixpin_2026-06-02_10-50-42.jpg)

重新开机后观察侧补光灯是否正常亮起。

- 侧补光灯正常亮起，前补光灯无法亮起：侧补光灯功能正常，但 AP 主板或主板上插座故障，需更换 AP 板。  
  P2S: [更换 P2S AP 板](../../p2s/maintenance/replace-ap-board.md)  
  X2D：[更换 X2D AP 板](../maintenance/replace-ap-board.md)
- 前补光灯正常亮起，侧补光灯无法亮起：AP 主板上的插座正常，但侧补光灯存在故障，需[更换侧补光灯](../../p2s/maintenance/replace-ap-board-cover-and-led-light-left.md)。

### 情况三：两条补光灯故障

检查两条补光灯的插头是否受损。

|  |  |
| --- | --- |
| 3.jpg | 4.jpg |

检查主板上的插座是否受损。

![5.jpg](https://wiki.bambulab.com/x2d/troubleshooting/led-fill-light-troubleshooting-guide/5.jpg)

重新安装补光灯插头。

![2.jpg](https://wiki.bambulab.com/x2d/troubleshooting/led-fill-light-troubleshooting-guide/2.jpg)

开机通过屏幕控制补光灯工作。

![7.jpg](https://wiki.bambulab.com/x2d/troubleshooting/led-fill-light-troubleshooting-guide/7.jpg)

若两补光灯无法点亮，建议更换 AP 主板。

P2S: [更换 P2S AP 板](../../p2s/maintenance/replace-ap-board.md)  
X2D：[更换 X2D AP 板](../maintenance/replace-ap-board.md)

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
