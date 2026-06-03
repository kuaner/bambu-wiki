---
path: zh/p1/maintenance/replace-xy-axis-assembly
title: "更换 P1P/P1S 的 XY 框架"
description: "P1 系列打印机的 XY 框架更换指南"
tags: []
created: 2025-01-24T12:06:19.825Z
updated: 2026-05-12T06:39:02.492Z
source: https://wiki.bambulab.com/zh/p1/maintenance/replace-xy-axis-assembly
---

## 适用打印机型号

P1P/P1S

## X/Y 框架组件

X/Y 框架组件是安装在打印机的顶部，用于让工具头完成在 X/Y 方向上运动。

|  |  |
| --- | --- |
| screenshot-20241224-165041.png | xy框架备件.jpg |

该组件更换难度较大，建议在更换前先仔细阅读本更换指南;  
该组件更换过程中所涉及的螺丝较多，建议提前准备一些小盒子，用于存放不同的螺丝。

## 何时使用

1. 惰轮异响/损坏
2. X/Y 框架弯曲，变形
3. Y 轴直线轴承损坏
4. Y 轴光杆损坏

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。
>
> 如果您对本指南有任何疑问，请[点击这里提交工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)，我们将及时回复并为您提供所需的帮助。

## 所需工具和材料

- 新的 X/Y 框架 - 请联系售后团队
- H2.0 内六角扳手
- H1.5 内六角扳手
- 3 - 4 小时

## 移除 X/Y 框架组件

### 步骤 1：移除屏幕/前面盖

1. **移除屏幕**

按压屏幕下方的扣位，解除锁定，然后向右推动屏幕，使屏幕松脱；然后断开屏幕的连接线（屏幕连接线可留在 AP 板上，同 AP 板一起取下）：

|  |  |
| --- | --- |
|  |  |

您可以参阅下面这篇 Wiki 来了解更换 P1P/P1S 的屏幕的详细步骤：

[屏幕组件 | Bambu Lab Wiki](screen.md)

2. **移除前面盖**

由于后续拆装 P1S 的左右侧板均需先移除前面盖，您可以先将前面盖移除。

由于 Wifi 天线需要从横梁的小孔中穿出，您可以先移除 AP 板的四颗固定螺丝，将 AP 板从横梁中拉出并断开 Wifi 天线的连接线，

![](https://wiki.bambulab.com/p1/maintenance/wifi-antenna/1_connector_4_screws.jpg)

然后移除前面盖的固定螺丝，将 Wifi 天线和前面盖一起移除：

|  |  |  |
| --- | --- | --- |
|  |  | 前面盖和wifi天线.jpg |

**注：可以不用将 Wifi 天线从前面盖中取下，直接和前面盖一起拆下即可。**

您可以参阅下面的 Wiki 来了解更换 P1P/P1S 的前面盖的详细步骤：

[P1P 前面盖 | Bambu Lab Wiki](front-cover.md)

[P1S 前面盖 | Bambu Lab Wiki](p1s-front-cover.md)

### 步骤 2：移除左/右侧板、背板和玻璃前门

**由于 P1P 没有左/右侧板和玻璃前门，如果您的 P1P 没有安装[升级套件](../manual/p1p-to-p1s.md)，您仅需参考后续更换背板的步骤。**

1. **移除 P1S 的玻璃前门**

您可以使用 H2.0 内六角扳手移除四颗玻璃前门固定螺丝：

|  |  |
| --- | --- |
|  |  |

您可以参阅下面这篇 Wiki 来了解更换 P1S 的玻璃前门的详细步骤：

[更换前玻璃门 | Bambu Lab Wiki](../../x1/maintenance/replace-the-front-door.md)

2. **移除 P1P/P1S 的背板**

您可以参阅下面的篇 Wiki 来查看移除 P1P/P1S 背板的详细步骤：

- [更换 P1S 的背板 | Bambu Lab Wiki](p1s-rear-panel.md)
- [更换 P1P 的背板 | Bambu Lab Wiki](rear-panel.md)

3. **移除 P1S 的右侧板**

您可以参阅下面的这篇 Wiki 来查看移除 P1S 右侧板的详细步骤：

[更换P1系列塑胶右侧板 | Bambu Lab Wiki](p1s-right-panel.md)

4. **移除 P1S 的左侧板**

您可以参阅下面的这篇 Wiki 来查看移除 P1S 左侧板的详细步骤：

[更换 P1 系列塑胶左侧板 | Bambu Lab Wiki](p1s-left-panel.md)

### 步骤 3：移除 TH 板/挤出机/热端

1. **移除热端和挤出机**

您可以将热端和挤出机一起移除。向下按压气动接头，移除 PTFE 管，并从挤出接口板上断开连接线；使用 H1.5 内六角扳手拧松切刀固定螺丝，使切刀可以自然下垂，然后使用 H2.0 内六角扳手移除三颗挤出机固定螺丝：

|  |  |  |
| --- | --- | --- |
| 热端挤出机固定螺丝和连接线.jpg |  | 移除挤出机和热端.jpg |

您可以参阅下面的 Wiki 来查看移除 P1P/P1S 的热端和挤出机的详细步骤：

[更换热端组件 | Bambu Lab Wiki](complete-hot-end-assembly.md)

[更换挤出机 | Bambu Lab Wiki](extruder-unit.md)

2. **移除工具头中盖和后盖**

使用 H1.5 内六角扳手移除工具头后盖和中盖上的八颗螺丝：

|  |  |
| --- | --- |
|  |  |

将工具头后盖与工具头中盖分离，移除工具头后盖；然后移除工具头中盖，注意不要被切刀划伤。

|  |  |
| --- | --- |
|  |  |

3. **移除 TH 板组件**

为便于后续安装，无需将 TH 板/挤出接口板和 FPC 排线断开连接，可以一起从工具头上移除。

使用 H1.5 内六角扳手移除 2 颗挤出接口板固定螺丝；断开挤出电机连接线，用 H1.5 内六角扳手移除三颗 TH 板固定螺丝，翻转 TH 板，在 TH 板的另一面移除工具头连接线；然后将 TH 板组件从工具头上取下：

|  |  |  |  |
| --- | --- | --- | --- |
|  |  |  | th_板组件.jpg |

您可以参考下面的这篇 Wiki 将 P1P/P1S 工具头上的部件移除：

[更换P1系列工具头电路板 | Bambu Lab Wiki](pcb-boards-on-toolhead.md)

### 步骤 4：移除 AP 板/屏幕/线缆

1. **移除 AP 板**

断开 MC-AP 线、LED 灯连接线和摄像头连接线，同时取出 SD 卡，将 AP 板移除。

**注：AP 板固定螺丝在移除前面盖时已移除**

|  |  |
| --- | --- |
| ap板连接线-1.jpg | ap_板连接线-2.jpg |

您可以参阅下面这篇 Wiki 来了解更换 P1P/P1S 的 AP 板的详细步骤：

[更换AP主板 | Bambu Lab Wiki](ap-board.md)

2. **移除 MC-AP 线缆**

由于在移除 AP 板的时候，已经从 AP 板上断开了 MC-AP 线缆，因此这里仅需将线缆从 X/Y 框架上移除 MC-AP 线缆，您可以撕掉固定胶布，将电缆从线槽中松出，移除 MC-AP 电缆。

注：这里可以不需要从 MC 板上断开 MC-AP 线缆的连接，您可以将线缆从线槽中抽出即可。

|  |  |
| --- | --- |
|  |  |

您可以参阅下面这篇 Wiki 来了解更换 P1P/P1S 的 MC-AP 线缆的详细步骤：

- [MC-AP 连接电缆 | Bambu Lab Wiki](mc-ap-cable.md)

3. **移除工具头线缆**

由于在移除 TH 板的时候，已经从 TH 板上断开了工具头线缆，您可以从 MC 板上断开工具头线缆的连接，然后将工具头线缆移除。

注：由于工具头线缆在 TH 板一端有硅胶套，这一端无法从线槽中取出，因此需要从 MC 板上断开连接，然后将工具头线缆从线槽中取出。

|  |  |
| --- | --- |
|  |  |

您可以参阅下面这篇 Wiki 来了解更换 P1P/P1S 的工具头线缆的详细步骤：

- [工具头数据线 | Bambu Lab Wiki](toolhead-cable.md)

4. **取出 LED 灯线缆和摄像头排线**

将 LED 灯线缆从 X/Y 框的小孔中取出，然后将摄像头排线撕下：

|  |  |
| --- | --- |
| 撕开摄像头排线.jpg | led_灯连接线.jpg |

5. **移除拖链**

如果没有拖链则可忽略该步骤。

您可以将 PTFE 管和拖链一起移除。您可以参阅下面这篇 Wiki 来了解更换 P1P/P1S 的拖链的详细步骤：

[更换拖链组件（P1 系列）| Bambu Lab Wiki](cable-chain.md)

### 步骤 5：移除 X/Y 张紧器/电机

1. **移除 X/Y 张紧器**

用 H2.0 内六角扳手移除两颗螺丝，移除张紧器固定支架和弹簧。

|  |  |
| --- | --- |
|  |  |

然后使用 H2.0 内六角扳手移除两颗螺丝和限位支架，松出张紧器。

|  |  |
| --- | --- |
|  |  |

2. **移除 X/Y 电机**

为了便于后续的安装，这里仅需将 X/Y 电机从打印机上拆下，将电机放在内衬上，无需将电机的连接线从 MC 板上断开。

![挂电机.jpg](https://wiki.bambulab.com/x1/maintenance/replace-xy-axis-assembly/%E6%8C%82%E7%94%B5%E6%9C%BA.jpg)

您可以参阅下面这篇 Wiki 来了解更换 P1P/P1S 的 X/Y 电机的详细步骤，安装在 X/Y 框架上的两个电机均需移除：

[XY电机 | Bambu Lab Wiki](xy-motor.md)

### 步骤 6：移除 X/Y 框架

**移除固定螺丝：**

X/Y 框架共使用 3 种规格的螺丝与四个立柱固定，**圆圈标记的均为同一种规格，方框标记的螺丝也均是同种规格**。四个立柱分别为左前，右前，左后，右后。

![立柱说明.jpg](https://wiki.bambulab.com/x1/maintenance/replace-xy-axis-assembly/x1c/%E7%AB%8B%E6%9F%B1%E8%AF%B4%E6%98%8E.jpg)

1. **移除左前立柱的固定螺丝：**

使用 H2.0 移除四颗圆圈标记的螺丝，再使用 H2.0 内六角扳手移除三颗方框标记的螺丝；

![左前立柱.jpg](https://wiki.bambulab.com/x1/maintenance/replace-xy-axis-assembly/%E5%B7%A6%E5%89%8D%E7%AB%8B%E6%9F%B1.jpg)

2. **移除右前立柱的固定螺丝：**

使用 H2.0 移除四颗圆圈标记的螺丝，再使用 H2.0 内六角扳手移除两颗方框标记的螺丝；

![右前立柱.jpg](https://wiki.bambulab.com/x1/maintenance/replace-xy-axis-assembly/%E5%8F%B3%E5%89%8D%E7%AB%8B%E6%9F%B1%E8%9E%BA%E4%B8%9D-%E6%96%B0.jpg)

3. **移除左后立柱的固定螺丝：**

使用 H2.0 移除四颗圆圈标记的螺丝，再使用 H2.0 内六角扳手移除三颗方框标记的螺丝，使用 H1.5 内六角扳手移除箭头标记的一颗银色螺丝；

![右后立柱.jpg](https://wiki.bambulab.com/x1/maintenance/replace-xy-axis-assembly/%E5%8F%B3%E5%90%8E%E7%AB%8B%E6%9F%B1.jpg)

4. **移除右后立柱的固定螺丝：**

使用 H2.0 移除六颗圆圈标记的螺丝，再使用 H2.0 内六角扳手移除两颗方框标记的螺丝，使用 H1.5 内六角扳手移除箭头标记的一颗银色螺丝；

![左后立柱.jpg](https://wiki.bambulab.com/x1/maintenance/replace-xy-axis-assembly/%E5%B7%A6%E5%90%8E%E7%AB%8B%E6%9F%B1.jpg)

如果您的打印机是 P1S，下图所示的这两螺丝在移除背板和侧板时已经移除。

![p1s螺丝移除.jpg](https://wiki.bambulab.com/x1/maintenance/replace-xy-axis-assembly/x1c/p1s%E8%9E%BA%E4%B8%9D%E7%A7%BB%E9%99%A4.jpg)

**移除上框架**

需要向外掰开立柱（您可以使用 H2.0 内六角扳手来撬开），解锁框架与立柱之间的插销；

> 需要将四个立柱均往外掰开/桥靠。

|  |  |
| --- | --- |
| 撬开框架.jpg | 框架已撬开.jpg |

然后将 X/Y 框架往上提起，从而取出 X/Y 框架。

|  |  |
| --- | --- |
| 取出和安装框架.jpg | 取出后.jpg |

## 安装 X/Y 框架组件

### 步骤 1：安装 X/Y 框架

将新的 X/Y 框架对准四个立柱，然后将 X/Y 框架按入打印机中，将 X/Y 框架的凸起对准立柱上的小孔，确保安装到位。 X/Y 框带有电机架的一面为背面，带有屏幕安装孔位的为正面，如下图所示：

|  |  |  |
| --- | --- | --- |
| xy框架备件.jpg | 取出和安装框架.jpg | 立柱说明.jpg |

注：

1. 左前立柱靠左侧的定位孔需将摄像头排线再往下撕开一点即可看到。
2. 将 X/Y 框架装好后请检查皮带是否可以正常移动，如果卡在 X/Y 框架与立柱之间，请及时调整。

| 左前立柱 | 右前立柱 | 左后立柱 | 右后立柱 |
| --- | --- | --- | --- |
| 左前立柱定位.jpg | 右前立柱定位.jpg | 右后立柱定位.jpg | 左后立柱定位.jpg |

依次拧紧左前，右前，左后，右后的固定螺丝（注意区分圆圈标记，方块标记以及银色的螺丝）

| 左前立柱 | 右前立柱 | 左后立柱 | 右后立柱 |
| --- | --- | --- | --- |
| 左前立柱.jpg | 右前立柱.jpg | 右后立柱.jpg | x1c右后立柱.jpg |

如果您的打印机是 P1P，需要拧紧这两颗螺丝。

![p1s螺丝移除.jpg](https://wiki.bambulab.com/x1/maintenance/replace-xy-axis-assembly/x1c/p1s%E8%9E%BA%E4%B8%9D%E7%A7%BB%E9%99%A4.jpg)

### 步骤 2：安装 X/Y 电机/张紧器

1. **安装 X/Y 电机**

您可以将放置在内衬上的 X/Y 电机重新安装到电机支架上，并将 X/Y 皮带装到 X/Y 电机主动轮上，然后使用 H2.0 内六角扳手拧紧固定电机的四颗螺丝。

> 需将后面的两颗螺丝穿过上横梁孔位，再放到内六角扳手上，通扳手将螺丝送到位。

|  |  |  |
| --- | --- | --- |
|  |  |  |

您可以参阅下面这篇 Wiki 来了解更换的 X/Y 电机的详细步骤：

[更换 XY 电机 - P1P/P1S | Bambu Lab Wiki](xy-motor.md)

[更换 XY 电机 - X1C/X1E | Bambu Lab Wiki](../../x1/maintenance/replace-the-xy-motor.md)

2. **安装 X/Y 张紧器**

将 X/Y 张紧器安装到位，装上两个限位支架并分别拧入螺丝进行预固定，不需要拧紧。

![](https://wiki.bambulab.com/p1/maintenance/xy-idler-pulley/install_the_tensioner.jpg)

将弹簧和固定支架安装到位，使用 H2.0 内六角扳手拧紧两颗固定螺丝。

|  |  |
| --- | --- |
|  |  |

3. **张紧 X/Y 皮带**

使用 H2.0 内六角扳手拧松另一个 X/Y 张紧器的两颗螺丝，双手握住工具头两端的滑车前后移动数次，然后紧靠后部停住。使用 H2.0 内六角扳手拧紧两边 X/Y 张紧器上的 4 颗螺丝。

|  |  |
| --- | --- |
|  |  |

您可以参阅下面这篇 Wiki 来了解皮带张紧的详细步骤：

[皮带张紧 | Bambu Lab Wiki](../../x1/maintenance/belt-tension.md)

### 步骤 3：安装前面盖

由于 Wifi 天线和前面盖一起拆下，在安装前面盖的时候需要先将 Wifi 天线从 X/Y 框架上的小孔中穿过：

> X/Y 框架上有两个小孔，需从靠右侧（面对打印机）的小孔中将 Wifi 天线穿过。

![安装前面盖和_wifi_天线.jpg](https://wiki.bambulab.com/x1/maintenance/replace-xy-axis-assembly/%E5%AE%89%E8%A3%85%E5%89%8D%E9%9D%A2%E7%9B%96%E5%92%8C_wifi_%E5%A4%A9%E7%BA%BF.jpg)

然后将前面盖对准 X/Y 框架，并使用 H2.0 内六角扳手拧紧外侧的两颗固定螺丝和内侧的一颗固定螺丝（外侧和内侧的螺丝规格不同，注意区分）。

![](https://wiki.bambulab.com/p1/maintenance/front-cover/3_screws_for_front_panel_cover.jpg)

您可以参阅下面的 Wiki 来了解更换 P1P/P1S 的前面盖的详细步骤：

[P1P 前面盖 | Bambu Lab Wiki](front-cover.md)

[P1S 前面盖 | Bambu Lab Wiki](p1s-front-cover.md)

### 步骤 4：安装 AP 板/屏幕/MC-AP 线缆

1. **安装 MC-AP 线缆和 AP 板**

- **MC-AP 线缆：**

将 MC-AP 线缆穿过 X/Y 框架上的线孔，并将 MC-AP 线缆压入线槽中，然后将 MC-AP 线缆的另外一端与 AP 板连接。

注：MC-AP 线缆的另外一端未与 MC 板断开连接。

|  |  |
| --- | --- |
|  |  |
| 穿过线孔并压入线槽 | 与 AP 板连接 |

- **AP 板：**

根据 SD 卡槽的缺口位置，将 AP 板安装到 X/Y 框架上，然后使用 H2.0 内六角扳手拧紧四颗螺丝，并将 Wifi 天线与 AP 板连接：

> 注意避让 Wifi 天线！

|  |  |
| --- | --- |
|  |  |

您可以参阅下面这篇 Wiki 来了解更换 P1P/P1S 的 MC-AP 线缆和 AP 板的详细步骤：

- [MC-AP 连接电缆 | Bambu Lab Wiki](mc-ap-cable.md)
- [更换AP主板 | Bambu Lab Wiki](ap-board.md)

2. **安装屏幕**

将屏幕与屏幕连接线连接，然后将屏幕通过卡扣固定在前面盖上：

|  |  |
| --- | --- |
|  |  |

您可以参阅下面这篇 Wiki 来了解更换 P1P/P1S 的屏幕的详细步骤，

- [屏幕组件 | Bambu Lab Wiki](screen.md)
- [更换屏幕排线 - P1 | Bambu Lab Wiki](screen-connector-cable.md)

### 步骤 5：安装 TH 板/挤出机/热端/工具头线缆

1. **安装工具头线缆**

将工具头线缆的两端分别穿过线孔，并将线压入线槽内，然后将工具头线缆与 MC 板连接：

> 由于 TH 板暂未安装，工具头线缆的另外一端在下一步与 TH 板连接。

|  |  |  |
| --- | --- | --- |
|  |  |  |

您可以参阅下面这篇 Wiki 来了解更换 P1P/P1S 工具头数据线的详细步骤，

- [工具头数据线 | Bambu Lab Wiki](toolhead-cable.md)

2. **安装 TH 板组件**

由于 FPC 排线与 TH 板和挤出接口板连接，可以先将 FPC 排线卡入线槽中。然后连接工具头线缆，然后将电机接口朝外，将 TH 板安装到工具头滑车后盖上，然后将电机与 TH 板连接，并使用 H1.5 内六角扳手拧紧三颗固定螺丝和挤出接口板的两颗固定螺丝：

|  |  |  |  |
| --- | --- | --- | --- |
| 安装_th_板.jpg |  |  |  |

您可以参阅下面这篇 Wiki 来了解更换 P1P/P1S TH 板的详细步骤：

[更换P1系列工具头电路板 | Bambu Lab Wiki](pcb-boards-on-toolhead.md)

3. **安装工具头中盖/后盖**

根据圆形线孔的位置，确认安装方向，将工具头中盖安装到位。然后将工具头后盖安装到工具头上，注意上方有卡扣。 确认工具头后盖与中盖扣合到位后，依次使用 H1.5 内六角扳手拧紧八颗螺丝。

|  |  |  |  |
| --- | --- | --- | --- |
|  |  |  |  |

您可以参阅下面这篇 Wiki 来了解更换 P1P/P1S 工具头中盖/后盖的详细步骤：

- [更换工具头后盖和中框 | Bambu Lab Wiki](toolhead-housing.md)

4. **安装挤出机/热端/工具头前盖**

将挤出机和热端安装到工具头上，使用 H2.0 内六角扳手拧紧三颗螺丝；然后将 PTFE 管接入到挤出机，将连接线与挤出接口板连接，最后使用 H1.5 内六角扳手拧紧切刀螺丝。

|  |  |
| --- | --- |
|  | 热端挤出机固定螺丝和连接线.jpg |

最后将工具头前盖线缆连接到接口板上，合上前盖。

|  |  |
| --- | --- |
|  |  |

您可以参阅下面这篇 Wiki 来了解更换 P1P/P1S 的挤出机和热端的详细步骤，

[更换挤出机 | Bambu Lab Wiki](extruder-unit.md)

[更换热端组件 | Bambu Lab Wiki](complete-hot-end-assembly.md)

### 步骤 6：安装左/右侧板、背板和玻璃前门

**由于 P1P 未包含左右侧板和玻璃前门，您只需安装背板即可。**

1. **安装 P1S 的右侧板**

[更换P1系列塑胶右侧板 | Bambu Lab Wiki](p1s-right-panel.md)

2. **安装 P1S 的左侧板**

[更换 P1 系列塑胶左侧板 | Bambu Lab Wiki](p1s-left-panel.md)

3. **安装 P1P/P1S 的背板**

您可以参阅下面的这篇 Wiki 来了解如何更换 P1P 的背板：

[更换P1P 的背板 | Bambu Lab Wiki](rear-panel.md)

您可以参阅下面的这篇 Wiki 来了解如何更换 P1S 的背板：

[更换P1S 的背板 | Bambu Lab Wiki](p1s-rear-panel.md)

4. **安装 P1S 的玻璃前门**

[更换前玻璃门 | Bambu Lab Wiki](../../x1/maintenance/replace-the-front-door.md)

## 设备校准

连接电源，启动打印机，运行设备校准流程，如果校准过程顺利通过，说明操作成功。

![](https://wiki.bambulab.com/p1/maintenance/boards-on-toolhead/calibration2.jpg)

如果有异常，请按照操作步骤排查组装是否有问题，排除后，再次运行设备自检。如果问题仍然存在，请联系 Bambu Lab 服务团队寻求进一步的帮助。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南并未解决您的问题，[*请点击此处联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
