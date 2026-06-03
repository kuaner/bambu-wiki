---
path: zh/p2s/maintenance/replace-hotend-heating-assembly-and-cooling-fan
title: "更换 P2S 热端加热组件/热端风扇"
description: "本文介绍如何更换 P2S 的热端加热组件和热端风扇"
tags: []
created: 2025-10-14T14:25:05.604Z
updated: 2026-04-14T01:03:10.134Z
source: https://wiki.bambulab.com/zh/p2s/maintenance/replace-hotend-heating-assembly-and-cooling-fan
---

## 热端加热组件/热端风扇

**热端加热组件**是安装在工具头上，负责将打印耗材（如PLA、ABS等）加热至熔融状态的配件。

配件包装内包含：

1. 热端加热组件 \* 1；
2. M2.5x5 螺丝 \* 3。  
   ![fah049.jpg](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/p2s-sku-pics/fah049.jpg)

**热端风扇**是冷却热端上部，防止耗材过早软化导致堵料的风扇。

配件包装内包含：

1. 热端风扇 \* 1；
2. 风道 \* 1；
3. BT2x5 螺丝 \* 3。

![faf021.jpg](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/p2s-sku-pics/faf021.jpg)

## 何时使用

- 热端加热功能异常，表明可能存在故障。
- 热端加热组件/热端冷却风扇电缆损坏，影响打印机运行。
- 由于操作不当或撞击导致热端加热组件/热端冷却风扇明显物理损坏，从而影响其功能。
- Bambu Lab 技术支持根据诊断结果建议更换热端加热组件或热端冷却风扇。

## 所需的工具和材料

- 新的热端加热组件/热端风扇
- H1.5 内六角扳手

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 移除热端加热组件/热端风扇

### 步骤 1：移除工具头外壳

请参考[更换工具头外壳](replace-toolhead-housing.md)，移除工具头的前盖和后盖。

![toolhead_housing_001.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/extruder_unit/toolhead_housing_001.png)

> 注：如果只需要移除热端加热组件，则无需拆下工具头中框。

### 步骤 2：移除热端硅胶套和热端

请参考[更换热端和热端硅胶套](replace-hotend-and-silicone-sock.md)，移除热端硅胶套与热端：  
![remove-sock.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-hotend-heating-assembly-and-cooling-fan/remove-sock.png)  
![remove-hotend.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-hotend-heating-assembly-and-cooling-fan/remove-hotend.png)

### 步骤 3：移除风道

使用 H1.5 内六角扳手移除两颗风道固定螺丝（BT2x5），取下风道。

|  |  |
| --- | --- |
|  |  |

### 步骤 4：移除热端风扇

依次撕下贴在 TH 板上的泡棉和胶布，然后断开热端加热组件、热端冷却风扇的连接，并将线缆从底部的线扣中取出。注意，断开热端风扇连接线时，要往垂直于连接器的方向拨起，请勿在连接器左右方向用力或摇晃，以免损坏连接器。

|  |  |
| --- | --- |
|  |  |

![_017.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-hotend-heating-assembly-and-cooling-fan/_017.png)

使用 H1.5 内六角扳手移除一颗风扇固定螺丝（BT2x5），然后向下滑动将风扇从安装槽里松出，取下热端风扇。

|  |  |
| --- | --- |
|  |  |

![005.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-hotend-heating-assembly-and-cooling-fan/005.png)

### 步骤 5：移除热端加热组件

使用 H2.0 内六角扳手移除三颗热端加热组件固定螺丝（M2.5x5），将热端加热组件线缆从线扣中取出，取下热端加热组件。

|  |  |
| --- | --- |
|  |  |

![0010.png](https://public-cdn.bblmw.com/wiki/new/0010.png)

## 安装热端加热组件/热端风扇

### 步骤 1：安装热端加热组件

将热端加热组件线缆从加热底座侧边穿出，然后安装到工具头上，使用 H2.0 内六角扳手拧紧三颗固定螺丝（M2.5x5），将线缆绕过风道的螺丝柱，并整理入线扣中。

> 请确认没有线缆被压在热端加热底座下面，否则可能导致**加热组件**或**涡流线圈**损坏。

|  |  |
| --- | --- |
|  |  |

![009.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-hotend-heating-assembly-and-cooling-fan/009.png)

将热端加热组件的线缆与 TH 板连接，并将胶布重新贴上。

![013.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-hotend-heating-assembly-and-cooling-fan/013.png)

### 步骤 2：安装热端风扇

将热端风扇线缆整理入工具头底部的线槽里，将热端风扇安装槽插入工具头上的凹槽中，往上滑动安装到位。

|  |  |
| --- | --- |
|  |  |

![上滑风扇.jpg](https://wiki.bambulab.com/p2s/maintenance/replace-hotend-heating-assembly-and-cooling-fan/%E4%B8%8A%E6%BB%91%E9%A3%8E%E6%89%87.jpg)

使用 H1.5 内六角扳手拧紧一颗螺丝（BT2x5），整理好线缆，然后将接头垂直于 TH 板的方向压入到连接器中，重新贴上泡棉和胶布。

|  |  |
| --- | --- |
|  |  |

|  |  |
| --- | --- |
|  |  |

### 步骤 3：安装风道

将风道安装到加热底座旁边，使用 H1.5 内六角扳手拧紧两颗固定螺丝（BT2x5）。

|  |  |
| --- | --- |
|  |  |

### 步骤 4：安装热端硅胶套和热端

请参考 [更换热端和热端硅胶套](replace-hotend-and-silicone-sock.md) 这篇WIKI，安装热端硅胶套与热端：

|  |  |
| --- | --- |
|  |  |

### 步骤 5：安装工具头外壳

请参考 [更换工具头外壳](replace-toolhead-housing.md) 的内容，安装好工具头外壳。

![close_front_cover_002.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/hotend-and-silicone-sock/close_front_cover_002.png)

## 如何验证成功

连接电源，打开打印机，将热端升温到100℃，确认温度能正常升温，且热端风扇能正常启动。

如果您遇到任何问题，请先回溯您的步骤并检查所有连接以重试。 如果问题仍然存在，请联系 Bambu Lab 服务团队寻求进一步帮助。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 为了确保您安全有效地进行操作，如果对指南中的任何步骤有疑虑或问题，请联系我们的客户服务团队，我们随时乐意为您解答疑问并提供支持。  
> [点击此处联系技术支持](https://support.bambulab.cn)
