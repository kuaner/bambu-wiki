---
path: zh/h2c/maintenance/replace-dual-extruder-unit
title: "更换 H2C 挤出机组件"
description: "本文将详细为您介绍更换 H2C 挤出机组件的详细步骤和注意事项。"
tags: []
created: 2025-11-18T13:16:53.334Z
updated: 2025-12-09T09:25:28.699Z
source: https://wiki.bambulab.com/zh/h2c/maintenance/replace-dual-extruder-unit
---

## 挤出机组件

挤出机负责从线轴中拉出耗材，并将其送入热端。耗材在热端加热熔化后，通过喷嘴挤出，生成打印模型。

![](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/replace-dual-extruder-unit/003.jpg)

**挤出机组件的备件包含如下：**

1. 挤出机组件（含挤出电机） \* 1
2. BT2.6x8 螺丝 \* 2
3. M2.5x8 螺丝 \* 4

## 何时更换

1. 挤出机损坏
2. 挤出电机异常

## 工具和材料

1. 新的挤出机组件
2. H2.0 内六角扳手
3. 镊子

## 视频指南

## 移除旧的挤出机组件

### 1. 移除工具头增强散热风扇

|  |  |
| --- | --- |
|  |  |

详细步骤可参考 wiki 移除：[更换工具头散热增强风扇](../../h2d-pro/maintenance/replace-toolhead-enhanced-cooling-fan.md)

### 2. 移除工具头上方的PTFE管

以对称的方式，按住黑色外圈，解锁挤出机上方的两个气动接头，释放PTFE管。

![](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/replace-dual-extruder-unit/035.png)

### 3. 移除左右热端

- 左喷嘴：取下左喷嘴的硅胶套，打开喷嘴组件的固定卡扣，即可取出左喷嘴组件。
- 右喷嘴：向右拉动喷嘴的拉柄完成解锁，取下右喷嘴组件。

|  |  |
| --- | --- |
|  |  |

### 4. 移除挤出机前盖导向组件

用手指从下方向上抵住黑色喷嘴连接件，同时轻轻按压左切刀的刀柄，使左切刀从切刀螺丝附近的开口槽中脱出。

![](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/replace-dual-extruder-unit/036.webp)

详细更换步骤可参考wiki：[H2C挤出机前导向更换指南](replace-dual-extruder-filament-guide.md)

### 5. 移除部件冷却风扇风道和风扇

|  |  |
| --- | --- |
|  |  |

详细步骤可参考这篇 Wiki 移除部件冷却风扇风道和风扇：[更换 H2D 部件冷却风扇](../../h2/maintenance/replace-part-cooling-fan.md)

### 6. 移除挤出机组件

先解开**②切换电机连接线**的卡扣，断开切换电机连接线。用手指扶住切换电机连接线，再解开**①挤出电机连接线**的卡扣，并断开挤出电机连接线。

|  |  |
| --- | --- |
|  |  |

使用 H2.0 内六角扳手移除六颗固定螺丝（最上方的两颗螺丝:BT2.6x8 \* 2，剩余的四颗螺丝:M2.5x8 \* 2），拧出前盖导向底部的两颗螺丝时，先按住切刀，再拧出螺丝。

![](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/replace-dual-extruder-unit/002.jpg)

> 由于前盖导向底部的两颗螺丝位置比较深，将螺丝完全拧松后可能会掉落在切刀和前盖导向附近。若发生这种情况，可以拆除挤出机组件后，轻轻摇晃挤出机组件将这2颗被别住的螺丝取出即可。

取出挤出机组件时，可以用镊子从工具头上方的缝隙中将内部的连接线压平，防止连接线弯曲而无法取出挤出机组件。

|  |  |
| --- | --- |
|  |  |

抓住左右两侧切刀缓慢向外拉出挤出机单元。

> 注意：挤出机单元背后有霍尔排线拉出时不可用力过猛，否则可能会导致排线断裂。

![](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/replace-dual-extruder-unit/039.webp)

最后解开挤出霍尔连接线的卡扣，断开挤出霍尔连接线，移除挤出机组件。

![](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/replace-dual-extruder-unit/032.webp)

## 安装新的挤出机组件

### 1. 安装挤出机组件

> 挤出机备件自带一根挤出霍尔连接线，如果出现排线断裂可以进行更换。
>
> ![](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/replace-dual-extruder-unit/017.png)

在安装新挤出机组件之前，先将原本的挤出霍尔连接线插入插座，并确保连接线上的白线处于水平状态，再扣合插座。

![](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/replace-dual-extruder-unit/018.png)

接下来开始正式安装新挤出机组件，为了使切换电机连接线和挤出电机连接线能够顺利通过工具头中框，需要先调整一下两根线缆的角度。

将两根连接线的头部略微向下弯曲，后半部分则略微向上弯曲，将有助于连接线通过中框。

![wanzhe.webp](https://wiki.bambulab.com/h2c/maintenance/nozzle-cold-pull-maintenance-and-cleaning/wanzhe.webp)

捋顺顶部排线，缓慢将挤出机向内推入，向内推入时需要将底部切刀向上抬起插入对应的槽内。

|  |  |
| --- | --- |
|  |  |

安装挤出机组件时，可以用镊子或螺丝刀从中框侧面将连接线往上顶，来辅助连接线穿过中框。

![](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/replace-dual-extruder-unit/031.webp)

先将**①挤出电机连接线**插入插座，确保连接线上的白线处于水平状态，再扣合插座。如果挤出电机连接线的卡扣难以扣合，可以使用六角扳手来辅助扣合插座；然后将**②切换电机连接线**也插入插座，确保连接线上的白线处于水平状态，扣合插座。

![](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/replace-dual-extruder-unit/004.png)

最后将挤出机左上方的挤出霍尔连接线塞入工具头左侧的缝隙中。

![](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/replace-dual-extruder-unit/021.png)

使用 H2.0 内六角扳手拧紧六颗固定螺丝（最上方的两颗螺丝:BT2.6x8 \* 2，剩余的四颗螺丝:M2.5x8 \* 2）。安装前盖导向下方的两颗螺丝时，可以按住切刀，再拧入螺丝。

![](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/replace-dual-extruder-unit/001.jpg)

### 2. 安装部件冷却风扇风道和风扇

|  |  |
| --- | --- |
|  |  |

详细步骤可参考这篇 Wiki 安装部件冷却风扇风道和风扇：[更换 H2D 部件冷却风扇](../../h2/maintenance/replace-part-cooling-fan.md)

### 3. 安装挤出机前盖导向组件

![](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/replace-dual-extruder-unit/024.webp)

详细步骤可参考这篇 wiki 安装挤出机前盖导向组件：[H2C挤出机前导向更换指南](replace-dual-extruder-filament-guide.md)

### 4. 安装左右热端

**左喷嘴安装**：将左喷嘴组件放入对应装配位，扣紧固定卡扣，确保喷嘴无松动；同时装回左喷嘴的硅胶套。

|  |  |
| --- | --- |
|  |  |

**右喷嘴安装**：确认拉柄的拉出的状态，将右喷嘴组件对准装配位推入，按下拉柄完成锁定；之后轻轻晃动喷嘴，确认锁定到位、无松动迹象。

![](https://public-cdn.bblmw.com/wiki/new/h2c/maintenance/replace-induction-hotend-latch/007.webp)

详细安装步骤可参考wiki：[H2C 感应热端安装指南](replace-induction-hotend.md)

### 5. 安装工具头增强散热风扇

|  |  |
| --- | --- |
|  |  |

详细步骤可参考 wiki 移除：[更换工具头散热增强风扇](../../h2d-pro/maintenance/replace-toolhead-enhanced-cooling-fan.md)

## 如何验证成功

连接电源并打开打印机，发起打印，检查是否可以完成打印。

## 螺丝清单

| **螺丝规格** | **用途** | **位置示意图** | **螺丝数量** |
| --- | --- | --- | --- |
| BT3x8 | 用于固定部件冷却风扇风道 |  | 4 |
| BT3x20 | 用于固定部件冷却风扇 |  | 2 |
| M2.5x7 | 用于固定挤出机前盖导向组件 |  | 3 |
| BT2.6x8 | 用于固定部件冷却风扇 |  | 2 |
|  | 用于固定挤出机 |  | 2 |
| M2.5x8 | 用于固定挤出机 |  | 4 |

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
