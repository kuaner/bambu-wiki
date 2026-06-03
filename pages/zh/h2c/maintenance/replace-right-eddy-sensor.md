---
path: zh/h2c/maintenance/replace-right-eddy-sensor
title: "更换 H2C 右涡流线圈"
description: ""
tags: []
created: 2025-11-18T13:17:11.862Z
updated: 2025-11-18T13:17:13.023Z
source: https://wiki.bambulab.com/zh/h2c/maintenance/replace-right-eddy-sensor
---

## H2C 右涡流线圈

涡流线圈参与 Z 轴归零、热床调平及动态流量校准等关键工作流程，其完好性与安装精度直接决定设备的打印精度和整体运行稳定性。

![](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/replace-right-eddy-sensor/002.jpg)

**挤出机组件的备件包含如下：**

- 挤出机组件（含挤出电机） \* 1
- BT2.6x8 螺丝 \* 2
- M2.5x8 螺丝 \* 4

## 何时更换

- 挤出机损坏
- 挤出电机异常

## 工具和材料

- 新的挤出机组件
- H2.0 内六角螺丝刀
- 镊子
- 螺丝盒（非必要）

本更换流程涉及的螺丝数量较多，为避免螺丝丢失或混淆，建议提前准备螺丝收纳盒进行分类，便于后续取用。

![](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/replace-right-eddy-sensor/001.jpg)

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，**请关闭打印机电源并断开电源连接**，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。
>
> 如果您对本指南有任何疑问，请[点击提交服务工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)，我们将及时回复并为您提供所需的帮助。

## 移除旧的右涡流线圈

### 1. 移除工具头增强散热风扇

|  |  |
| --- | --- |
|  |  |

详细步骤可参考此 wiki：[更换工具头散热增强风扇](../../h2d-pro/maintenance/replace-toolhead-enhanced-cooling-fan.md)

### 2. 移除工具头上方的PTFE管

以对称的方式，按住黑色外圈，解锁挤出机上方的两个气动接头，释放PTFE管。

![](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/replace-right-eddy-sensor/028.png)

### 3. 移除左右热端

- 左喷嘴：取下左喷嘴的硅胶套，打开喷嘴组件的固定卡扣，即可取出左喷嘴组件。
- 右喷嘴：向右拉动喷嘴的拉柄完成解锁，取下右喷嘴组件。

|  |  |
| --- | --- |
|  |  |

### 4. 移除挤出机前盖导向组件

用手指从下方向上抵住黑色喷嘴连接件，同时轻轻按压左切刀的刀柄，使左切刀从切刀螺丝附近的开口槽中脱出。

![](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/replace-right-eddy-sensor/030.webp)

详细更换步骤可参考wiki：[H2C挤出机前导向更换指南](replace-dual-extruder-filament-guide.md)

### 5. 移除部件冷却风扇风道和风扇

|  |  |
| --- | --- |
|  |  |

详细步骤可参考这篇 Wiki 移除部件冷却风扇风道和风扇：[更换 H2D 部件冷却风扇](../../h2/maintenance/replace-part-cooling-fan.md)

### 6. 移除挤出机组件

![](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/replace-right-eddy-sensor/034.webp)

详细步骤可以参考此 wiki：[H2C 挤出机组件更换指南](replace-dual-extruder-unit.md)

### 7. 移除感应加热组件

![](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/replace-right-eddy-sensor/031.webp)

详细步骤可以参考此 wiki：[H2C 感应加热组件更换指南](replace-induction-heating-assembly.md)

> 侧边排线涂有背胶，移除侧板排线时需要特别小心避免扯断。
>
> ![12.png](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/belt-tension/889.png)

### 8. 移除挤出接口板

如图所示，拔掉挤出接口板上的 3 个 FPC 插头，使用 H1.5 内六角螺丝刀移除两颗固定螺丝(M1.6×4)，小心地取出挤出接口板。

|  |  |
| --- | --- |
|  |  |

### 9. 移除右涡流线圈

找到加热组件线缆接头，轻轻拔开接头完成分离，将线缆从线扣内拉出。

![](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/replace-right-eddy-sensor/024.webp)

由于喷嘴相机与涡流线圈线缆存在干涉，需先松开工具头相机；使用 H1.5 螺丝刀，拆卸相机固定螺丝，注意相机排线无需移除，仅需将相机轻轻移位以腾出操作空间；

|  |  |
| --- | --- |
|  |  |

撕掉贴在右涡流线圈接口上的胶带。

![](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/replace-right-eddy-sensor/027.webp)

捏住右涡流线圈连接线接头，沿接头所在平面方向向外推出。

|  |  |
| --- | --- |
|  |  |

使用 H1.5 内六角螺丝刀，拆卸右涡流线圈上两颗固定螺丝。（M1.6×4）

![](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/replace-right-eddy-sensor/006.png)

将右涡流线圈沿水平方向从工具头上方缓慢抽出，抽出过程中避免线圈线缆与周边部件摩擦或勾挂。

![](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/replace-right-eddy-sensor/023.webp)

## 安装新的右涡流线圈

### 1. 安装右涡流线圈

将新的右涡流线圈连接线穿过工具头上的预设小孔，然后将右涡流线圈对准螺丝孔位。

![](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/replace-right-eddy-sensor/035.webp)

将线缆卡入设备预设走线槽内，保证线缆没有挤压。

![](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/replace-right-eddy-sensor/014.png)

将右涡流线圈对准安装工位的螺丝孔位，调整线圈位置至完全贴合安装面，使用 H1.5 内六角螺丝刀安装两颗螺丝先预锁紧；

![](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/replace-right-eddy-sensor/007.png)

> 注意此步骤不用完全锁紧涡流线圈两颗螺丝，完成加热组件安装后，再锁紧涡流线圈两颗固定螺丝。

移动至工具头后方，将右涡流线圈线缆从喷嘴摄像头连接线下方穿过，卡入线扣内。

![](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/replace-right-eddy-sensor/029.webp)

安装涡流线圈接头，使接口金属面朝向外侧，沿水平方向平稳压入 TH 板接口，然后贴回防护胶带。

![](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/replace-right-eddy-sensor/022.webp)

对准加热组件线缆接头与接口，连接后轻轻拉扯线缆确认牢固。

![](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/replace-right-eddy-sensor/009.png)

如下图所示，将加入组件线缆卡入线扣内。

|  |  |
| --- | --- |
|  |  |

### 2. 安装挤出接口板

调整挤出接口板位置，将板上两个金色针脚对齐 TH 板对应的接口，沿垂直方向缓慢插入。

![](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/replace-right-eddy-sensor/021.png)

连接挤出接口板上的3个 FPC 插头，使用 H1.5 内六角螺丝刀锁紧两颗固定螺丝(M1.6×4)，完成安装挤出接口板。

|  |  |
| --- | --- |
|  |  |

### 3. 安装感应加热组件

安装加热组件顶部铺一张薄型 A4 纸条作为缓冲垫层，避免安装过程中加热组件与顶部涡流线圈发生刚性碰撞；

![](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/replace-induction-heating-assembly/028.webp)

确认位置后锁紧加热组件两颗固定螺丝。

![](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/replace-right-eddy-sensor/005.png)

详细步骤可以参考此 wiki：[H2C 感应加热组件更换指南](replace-induction-heating-assembly.md)

完成加热组件安装后，再锁紧右侧涡流线圈固定螺丝。

![](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/replace-right-eddy-sensor/007.png)

### 4. 安装挤出机组件

![](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/replace-right-eddy-sensor/020.webp)

详细步骤可以参考此 wiki：[H2C 挤出机组件更换指南](replace-dual-extruder-unit.md)

### 5. 安装部件冷却风扇风道出口

对准螺丝和定位孔，插入风道出口，确保定位销与孔位精准契合。使用 H1.5 内六角扳手锁紧两颗固定螺丝（M2\*5），固定好风道出口。

|  |  |
| --- | --- |
|  |  |

### 6. 安装挤出机前盖导向组件

![](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/replace-dual-extruder-unit/024.webp)

详细步骤可参考这篇 wiki 安装挤出机前盖导向组件：[H2C挤出机前导向更换指南](replace-dual-extruder-filament-guide.md)

### 7. 安装左右热端

**左喷嘴安装**：将左喷嘴组件放入对应装配位，扣紧固定卡扣，确保喷嘴无松动；同时装回左喷嘴的硅胶套。

|  |  |
| --- | --- |
|  |  |

**右喷嘴安装**：确认拉柄的拉出的状态，将右喷嘴组件对准装配位推入，按下拉柄完成锁定；之后轻轻晃动喷嘴，确认锁定到位、无松动迹象。

![](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/replace-induction-hotend-latch/007.webp)

详细安装步骤可参考wiki：[H2C 感应热端安装指南](replace-induction-hotend.md)

### 8. 安装工具头增强散热风扇

|  |  |
| --- | --- |
|  |  |

## 如何验证成功

连接电源并打开打印机，发起打印，检查是否可以完成打印。

## 螺丝清单

| **螺丝规格** | **用途** | **位置示意图** | **螺丝数量** |
| --- | --- | --- | --- |
| BT3x8 | 用于固定部件冷却风扇风道 |  | 4 |
| BT3x20 | 用于固定部件冷却风扇 |  | 2 |
| M2.5x7 | 用于固定挤出机前盖导向组件 |  | 3 |
| BT2.6x8 | 用于固定部件冷却风扇 |  | 2 |
| M2×5 | 固定部件冷却风扇风道出口 |  | 2 |
| M3×6 | 固定感应加热组件电源线 |  | 2 |
| M3x12 | 固定感应加热组件 |  | 2 |

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
