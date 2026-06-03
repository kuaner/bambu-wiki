---
path: zh/h2s/maintenance/replace-extruder-unit
title: "更换 H2S 挤出机组件"
description: ""
tags: []
created: 2025-08-26T06:10:34.480Z
updated: 2026-01-19T04:20:07.011Z
source: https://wiki.bambulab.com/zh/h2s/maintenance/replace-extruder-unit
---

## 重要提示

> 在移除挤出机组件时务必小心操作，以避免扯断FPC排线。

## 挤出机组件

![](https://wiki.bambulab.com/h2s/maintenance/replace-extruder-unit/replace.png)

涡流线圈安装在挤出机上，位于热端的上方，正确安装后，线圈与热端散热片的间隙>=0.15mm && <= 0.5mm。

**备件包含如下：**

1. 挤出机组件 \* 1
2. M2.5x5 \* 2
3. BT3x12 \* 2
4. BT2x6.5 \* 2

## 何时更换

- 挤出机组件损坏；
- 挤出电机损坏
- 经 Bambu Lab 官方技术支持确认需要更换挤出机组件。

## 工具和材料

H2S 挤出机组件（购买链接：京东；天猫）

- H1.5 六角扳手
- H2.0 六角扳手
- 30 分钟

## 本文拆装步骤中涉及的螺丝清单

- 螺丝A：挤出机组件上方2颗螺丝：BT3x12
- 螺丝B：挤出机组件下方2颗螺丝：M2.5x5
- 螺丝 C: 部件冷却风扇背面（和后盖共锁）以及工具头后盖螺丝，共 3 颗：BT2x6.5; 涡流线圈螺丝同尺寸，2颗，合计5颗。
- 螺丝 D: 部件冷却风扇左右两侧螺丝，共 2 颗： BT2x5
- 螺丝 E:TH 板螺丝，共 3 颗：BT2x5
- 螺丝 F: 热端风扇螺丝，共 2 颗：BT2x4

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-extruder-unit/scre-extruder.png)

> 重要提醒！  
> **在进行任何维护工作之前，务必关闭打印机的电源**，包括对打印机的电子元件和工具头电线进行维护。在打印机通电时进行此类操作可能会导致短路，从而损坏电子设备和造成安全隐患。  
> 在维护或故障排除过程中，您可能需要拆卸热端等部件，从而暴露电线和电子元件。如果它们在打印机仍处于通电状态时相互接触或与其他金属、电子元件接触，就可能发生短路。**这将损坏打印机的电子元件和造成其他问题**。  
> 因此，**在进行任何维护前，务必关闭打印机并断开电源**，以防止短路或损坏打印机的电子原件，从而确保维护工作安全有效地进行。如果您对本指南有任何疑问，请[点击这里提交工单](https://bambulab.com/zh/my/support/tickets?from=5)，我们将及时回复并提供帮助。

## 拆除挤出机组件

### 步骤1：松开部件冷却风扇

- 拧下部件冷却风扇的 3 颗螺丝，其中背面的 1 颗螺丝与工具头后盖共锁。

|  |  |
| --- | --- |

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-extruder-unit/replace-extruder-unit-4.png)

- 松开螺丝后，风扇会自然下垂。请勿拉扯风扇，以免损坏连接器！

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-extruder-unit/replace-extruder-unit-5.png)

### 步骤2：松开工具头后盖

- 移除工具头后盖上方的 2 颗螺丝，打开模块接口盖子；

|  |  |
| --- | --- |

- 打开接口盖子后，可将手指伸入，从内壁轻微用力，往后推工具头后盖。

|  |  |
| --- | --- |

### 步骤3：断开 TH 板上的连接器

- 依次断开TH板上的挤出电机插头，热端加热组件线缆和工具头摄像头插头

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-extruder-unit/replace-extruder-unit-10.png)

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-extruder-unit/replace-extruder-unit-11.webp)

- 拧下 TH 板上的 3 颗螺丝；

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-extruder-unit/replace-extruder-unit-13.png)

- 小心移动 TH 板（手指抵着散热片，防止散热片脱落），创造出断开进料霍尔板插头的操作空间后，断开插头。

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-extruder-unit/replace-extruder-unit-14.webp)

### 步骤4：移除热端

参考此教程移除热端（[点击此处跳转](replace-silicone-sock-and-hotend.md)）

### 步骤5：移除热端风扇和涡流线圈

- 请注意：这一步可以不断开热端风扇和涡流线圈在TH板上的插头，仅松开热端风扇和涡流线圈螺丝，以便抽出卡在挤出机组件上的线缆；
- 卸下热端风扇的 2 颗螺丝，移除热端风扇；

|  |  |
| --- | --- |

- 卸下涡流线圈的2颗螺丝，绕开箭头处的走线

|  |  |
| --- | --- |

### 步骤6：移除挤出机组件

> 由于挤出机组组件的FPC排线有胶带背面及90度弯曲，尤其是对于较细的进料霍尔组件排线，移除挤出机组件时必须格外小心，以避免撕裂排线。

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-extruder-unit/tape1.png)

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-extruder-unit/tape2.png)

沿着中框的相反方向拨开排线背胶与中框的粘连。

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-extruder-unit/detach_fpc_cable.webp)

移除图示的4颗挤出机螺丝

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-extruder-unit/replace-extruder-unit-19.png)

如果后面的挤出机进料霍尔传感器电缆粘在塑料中框上，可以先移动电缆以将其与中框分离。如果顶部电机电缆干扰，可以使用塑料工具将其按下。

左右摇动挤出机，然后从前面拉出挤出机组件。

> 如果传感器的排线或电机电缆与中框有干涉，请用手指或塑料工具轻轻按下；不要用力拉扯。

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-extruder-unit/replace-extruder-unit-21.webp)

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-extruder-unit/remove-extruder.webp)

## 安装挤出机组件

### 步骤1：安装新的挤出机组件

- 如动图所示，折叠新的挤出机组件排线（也可以参考拆下来旧的挤出机组件折纹），撕开背胶保护膜

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-extruder-unit/replace-extruder-unit-22.webp)

- 进料霍尔排线在上，挤出电机排线在下，将挤出机组件穿入工具头中框中。

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-extruder-unit/replace-extruder-unit-23.png)

- 此处如有排线翘起来，需要用塑料工具将排线压平再继续往前推入，防止损坏排线。

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-extruder-unit/replace-extruder-unit-24.png)

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-extruder-unit/install-extruder.png)

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-extruder-unit/replace-extruder-unit-25.webp)

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-extruder-unit/install-extruder-v2.webp)

- 锁入挤出机组件的4颗螺丝

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-extruder-unit/replace-extruder-unit-26.png)

### 步骤2：安装涡流线圈和热端风扇

对准螺丝孔，两个结构件的弧形相互重合，锁入涡流线圈螺丝。锁螺丝时，请先预锁一颗，锁紧另一颗后再次拧紧第一颗螺丝，以保证涡流线圈装好后呈水平状态（重要）。

|  |  |
| --- | --- |

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-extruder-unit/replace-extruder-unit-29.webp)

- 校准涡流线圈安装位置（重要）：装回热端，将一张合适尺寸的A4纸对折，插入到热端和涡流线圈之间的间隙，来回抽拉时，能感受到一定的摩擦阻力，但是纸张仍然可以自由移动，这样的话，热端和涡流线圈大致间隙为0.2-0.3mm。

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-extruder-unit/replace-extruder-unit-30.webp)

- 将风扇带标签的一面朝向热端，对准螺丝孔位（参考下图红色和黄色圆圈）；

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-extruder-unit/replace-extruder-unit-31.png)

- 将风扇线缆折在图示凹槽内，安装风扇。

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-extruder-unit/replace-extruder-unit-32.png)

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-extruder-unit/replace-extruder-unit-33.webp)

- 锁紧固定风扇的两颗螺丝。

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-extruder-unit/replace-extruder-unit-34.png)

#### 步骤3：安装热端

参考此教程[安装热端](replace-silicone-sock-and-hotend.md)

步骤3：连接 TH 板上的连接器

- 连接挤出电机插头

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-extruder-unit/replace-extruder-unit-35.webp)

- 连接进料霍尔组件插头，往塑料中框按压排线，使其粘在中框上。

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-extruder-unit/replace-extruder-unit-36.webp)

- 对准TH板与工具头中框的螺丝孔，拧回TH板3颗螺丝。

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-extruder-unit/replace-extruder-unit-37.png)

- 插入工具头摄像头插头

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-extruder-unit/replace-extruder-unit-38.webp)

- 预对准风扇的螺丝孔位，将风扇线缆排在 TH 上，并向上拉动，将多余的线缆折叠，避免被风扇外壳或工具头后盖压破导致风扇异常。

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-extruder-unit/replace-extruder-unit-40.webp)

|  |  |
| --- | --- |

- 整理好线缆后，插入热端加热组件插头，并用热端加热组件插头和线缆压住部件冷却风扇线缆。

|  |  |
| --- | --- |

- 插入热端加热组件时，确保对准孔位，不要错排。

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-extruder-unit/replace-extruder-unit-45.png)

### 步骤4：安装工具头后盖

- 安装工具头后盖；

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-extruder-unit/replace-extruder-unit-46.png)

- 安装后，注意检查部件冷却风扇线缆是否位于专用的缺口处，避免被后盖边框挤压；

|  |  |
| --- | --- |

- 锁入 2 颗后盖固定螺丝。

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-extruder-unit/replace-extruder-unit-49.png)

### 步骤5：安装部件冷却风扇

- 对准螺丝孔，安装部件冷却风扇；卡入风扇时，注意不要压住风扇线缆。如果线缆过长，需退回至安装指南的步骤一，先折叠多余的线缆。

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-extruder-unit/replace-extruder-unit-50.png)

- 锁入3颗螺丝，固定部件冷却风扇。

|  |  |
| --- | --- |

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-extruder-unit/replace-extruder-unit-53.png)

## 功能验证

为确保一切正常，请打开打印机，进行进退料操作，如果一切正常，则代表更换顺利。

## 操作后的校准步骤

建议您在更换完挤出机组件后进行一次全面校准，以确保打印机顺畅运行。

此外，强烈建议在进行打印之前[清洗纹理PEI打印板](../../general/textured-PEI-plate-not-working-as-expected.md)，因为在更换挤出机组件的过程中，构建板可能会受到污染。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 为了确保您安全有效地进行操作，如果对指南中的任何步骤有疑虑或问题，请在开始操作前联系我们的客户服务团队。  
> 我们随时乐意为您解答疑问并提供支持。  
> [点击此处联系在线技术支持 （服务时间 9:00-21:00）](https://support.bambulab.cn/cn/im)
