---
path: zh/h2s/maintenance/replace-eddy-sensor
title: "更换 H2S 涡流线圈"
description: ""
tags: []
created: 2025-08-26T06:15:59.569Z
updated: 2026-01-07T10:03:30.314Z
source: https://wiki.bambulab.com/zh/h2s/maintenance/replace-eddy-sensor
---

## 重要提醒

H2S挤出主板上的涡流线圈插头采用这种小型插头设计。**拔出插头时，请用手握住插头根部，垂直于PCB面方向用力抬起以解锁插头。** 切勿在水平方向用力，以免损坏插头。

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-eddy-sensor/replace-eddy-sensor-1.jpeg)

## 涡流线圈

涡流线圈安装在挤出机上，位于热端的上方，正确安装后，线圈与热端散热片的间隙>=0.15mm && <= 0.5mm。

**备件包含如下：**

1. 涡流线圈 \* 1
2. M2x6.5 螺丝 - 用于固定右涡流线圈 \* 2

## 何时更换

- 涡流线圈损坏；
- 经 Bambu Lab 官方技术支持确认需要更换涡流线圈。

## 工具和材料

H2S 涡流线圈（购买链接：京东；天猫）

- H1.5 六角扳手
- 25 分钟

## 螺丝清单

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-eddy-sensor/replace-eddy-sensor-2.png)

- 螺丝 A: 部件冷却风扇背面（和后盖共锁）以及工具头后盖螺丝，共 3 颗; 涡流线圈螺丝，共2颗：BT2x6.5；
- 螺丝B: 热端风扇螺丝，共 2 颗：BT2x4
- 螺丝 C: 部件冷却风扇左右两侧螺丝，共 2 颗： BT2x5

> 安全警告  
> **重要提醒！**  
> **在进行任何维护工作之前，务必关闭打印机的电源**，包括对打印机的电子元件和工具头电线进行维护。在打印机通电时进行此类操作可能会导致短路，从而损坏电子设备和造成安全隐患。  
> 在维护或故障排除过程中，您可能需要拆卸热端等部件，从而暴露电线和电子元件。如果它们在打印机仍处于通电状态时相互接触或与其他金属、电子元件接触，就可能发生短路。**这将损坏打印机的电子元件和造成其他问题。**  
> 因此，**在进行任何维护前，务必关闭打印机并断开电源**，以防止短路或损坏打印机的电子原件，从而确保维护工作安全有效地进行。如果您对本指南有任何疑问，请点击这里[提交工单](https://bambulab.com/zh/my/support/tickets?from=5)，我们将及时回复并提供帮助。

## 拆除涡流线圈

### 步骤1：松开部件冷却风扇

- 拧下部件冷却风扇的 3 颗螺丝，其中背面的 1 颗螺丝与工具头后盖共锁。

|  |  |
| --- | --- |

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-eddy-sensor/replace-eddy-sensor-5.png)

- 松开螺丝后，风扇会自然下垂。请勿拉扯风扇，以免损坏连接器！

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-eddy-sensor/replace-eddy-sensor-6.png)

### 步骤2：松开工具头后盖

- 移除工具头后盖上方的 2 颗螺丝，打开模块接口盖子；

|  |  |
| --- | --- |

- 打开接口盖子后，可将手指伸入，从内壁轻微用力，往后推工具头后盖。

|  |  |
| --- | --- |

### 步骤3：断开 TH 板上的涡流线圈连接器

- 撕开涡流线圈插头的醋酸胶布；

> 注意：安装时需要贴回此醋酸胶布，请妥善保管！

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-eddy-sensor/replace-eddy-sensor-11.png)

- 捏住插头根部，从垂直 PBC 板的方向施力，断开涡流线圈插头。

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-eddy-sensor/replace-eddy-sensor-12.png)

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-eddy-sensor/replace-eddy-sensor-13.webp)

### 步骤4：移除热端

参考此教程移除热端[点击此处跳转](replace-silicone-sock-and-hotend.md)

### 步骤5：移除热端风扇和涡流线圈

- 卸下热端风扇的 2 颗螺丝，移除热端风扇；
- 请注意：这一步可以不断开热端风扇在TH板上的插头，仅松开热端风扇螺丝，以便抽出2根线缆；

|  |  |
| --- | --- |

- 卸下涡流线圈的2颗螺丝，绕开箭头处的走线

|  |  |
| --- | --- |

- 依次从理线槽中取出热端风扇和涡流线圈线缆，取下旧的涡流线圈

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-eddy-sensor/replace-eddy-sensor-18.webp)

## 安装涡流线圈

### 步骤1：安装新的涡流线圈和热端风扇

- 将涡流线圈线缆和热端风扇线缆依次卡入理线槽中

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-eddy-sensor/replace-eddy-sensor-19.webp)

请注意，从前往后看，线缆需要从箭头处理线柱的左边穿过（从前往后看）

|  |  |
| --- | --- |

- 对准螺丝孔，两个结构件的弧形相互重合，锁入涡流线圈螺丝。锁螺丝时，请先预锁一颗，锁紧另一颗后再次拧紧第一颗螺丝，以保证涡流线圈装好后呈水平状态（重要）。

|  |  |
| --- | --- |

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-eddy-sensor/replace-eddy-sensor-24.webp)

- 校准涡流线圈安装位置（重要）：装回热端，将一张合适尺寸的A4纸对折，插入到热端和涡流线圈之间的间隙，来回抽拉时，能感受到一定的摩擦阻力，但是纸张仍然可以自由移动，这样的话，热端和涡流线圈大致间隙为0.2-0.3mm。

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-eddy-sensor/replace-eddy-sensor-25.webp)

- 将风扇带标签的一面朝向热端，对准螺丝孔位（参考下图红色和黄色圆圈）；

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-eddy-sensor/replace-eddy-sensor-26.png)

- 将风扇线缆折在图示凹槽内，安装风扇。

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-eddy-sensor/replace-eddy-sensor-27.png)

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-eddy-sensor/replace-eddy-sensor-28.webp)

- 锁紧固定风扇的两颗螺丝。

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-eddy-sensor/replace-eddy-sensor-29.png)

### 步骤2：安装热端

参考此教程安装热端[点击此处跳转](replace-silicone-sock-and-hotend.md)

### 步骤3：连接 TH 板上的涡流线圈连接器

- 连接风扇线缆，将插头的插孔面朝 TH 板上的插座（插头金属焊点面朝机箱背面），对齐后下压插头，将多余线长压入TH板下方；

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-eddy-sensor/replace-eddy-sensor-30.png)

- 贴回醋酸胶布；

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-eddy-sensor/replace-eddy-sensor-31.png)

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-eddy-sensor/replace-eddy-sensor-32.webp)

- 预对准风扇的螺丝孔位，将风扇线缆排在 TH 上，并向上拉动，将多余的线缆折叠，避免被风扇外壳或工具头后盖压破导致风扇异常。

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-eddy-sensor/replace-eddy-sensor-33.webp)

|  |  |
| --- | --- |

- 整理好线缆后，插入热端加热组件插头，并用热端加热组件插头和线缆压住部件冷却风扇线缆。

|  |  |
| --- | --- |

> 插入热端加热组件时，确保对准孔位，不要错排。

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-eddy-sensor/replace-eddy-sensor-38.png)

### 步骤4：安装工具头后盖

- 安装工具头后盖；

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-eddy-sensor/replace-eddy-sensor-39.png)

- 安装后，注意检查部件冷却风扇线缆是否位于专用的缺口处，避免被后盖边框挤压；

|  |  |
| --- | --- |

- 锁入 2 颗后盖固定螺丝。

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-eddy-sensor/replace-eddy-sensor-42.png)

### 步骤5：安装部件冷却风扇

- 对准螺丝孔，安装部件冷却风扇；卡入风扇时，注意不要压住风扇线缆。

> 如果线缆过长，需退回至安装指南的步骤一，先折叠多余的线缆。

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-eddy-sensor/replace-eddy-sensor-43.png)

- 锁入3颗螺丝，固定部件冷却风扇。

|  |  |
| --- | --- |

|  |
| --- |

## 功能验证

为确保一切正常，请打开打印机，进行一次回零和调平操作，若无出现回零或调平失败报错，表示上方操作均正确。

## 操作后的校准步骤

建议您在更换完热端风扇后进行一次全面校准，以确保打印机顺畅运行。  
此外，强烈建议在进行打印之前[清洗纹理PEI打印板](../../general/textured-PEI-plate-not-working-as-expected.md)，因为在更换热端风扇的过程中，构建板可能会受到污染。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 为了确保您安全有效地进行操作，如果对指南中的任何步骤有疑虑或问题，请在开始操作前联系我们的客户服务团队。  
> 我们随时乐意为您解答疑问并提供支持。  
> [点击此处联系在线技术支持 （服务时间 9:00-21:00）](https://support.bambulab.cn/cn/questionType)
