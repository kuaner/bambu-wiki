---
path: zh/h2c/troubleshooting/clogging
title: "H2C 堵塞排查"
description: "本文介绍如何进行 H2C 堵塞排查"
tags: []
created: 2025-11-18T13:15:41.343Z
updated: 2026-06-12T09:04:51.997Z
source: https://wiki.bambulab.com/zh/h2c/troubleshooting/clogging
---

## 故障现象

- **打印时不出料或出料量极少：** 即使挤出机齿轮在正常转动，喷嘴也没有线材挤出，或者挤出的线材非常细弱。
- **挤出机发出“嗒嗒嗒”的异响：** 这是挤出机电机因为无法将线材推入热端而打滑发出的声音。
- **打印件出现欠挤出或断层：** 打印层与层之间无法很好地粘合，出现明显的缝隙或孔洞。
- **打印刚开始就失败：** 打印头在移动但喷嘴没有线材挤出。

![](https://public-cdn.bblmw.com/wiki/new/h2c/troubleshooting/clogging/clogging.png)

## 可能出现故障的位置

要解决堵塞问题，我们需要从线材路径的三个关键位置进行排查：

- **PTFE 管内部：** 线材在从卷轴到工具头的 PTFE 管中受到阻碍。
- **挤出机内部（包括挤出从动杆、主动轮与从动杆缝隙处、前盖导向）：** 挤出机齿轮与热端入口之间的线材路径发生堵塞。
- **热端与喷嘴：** 喷嘴内部或热端喉管处存在堵塞。

## 排障思路

1. 先尝试在室温下手动切断耗材，然后手动上拉耗材，若过程中遇到明显阻力或无法取出，直接判定为挤出机侧堵塞，转至 [3. 挤出机堵塞排查](#sec-extruder-jam) 处理。
2. 若上拉耗材顺利，可插入一段新耗材，在打印机屏幕上点击 “挤出”：
   - 若能顺利挤出（此时喷嘴已取下），说明堵塞多发生在热端或喷嘴，转至 [2. 热端/喷嘴堵塞排查](#sec-hotend-nozzle)。
   - 若无法挤出或回抽操作失败，按挤出机堵塞处理，转至 [3. 挤出机堵塞排查](#sec-extruder-jam)。

## 排障步骤

### 1. 手动挤出

***本文以右侧喷嘴的排查流程为例，左侧喷嘴的操作逻辑一致，仅需对应切换左侧相关组件。***

#### 步骤 1. 移除工具头增强散热风扇

1. 打开打印机前门，往上拔工具头增强散热风扇连接插头，将其断开；

![](https://public-cdn.bblmw.com/wiki/new/h2c/troubleshooting/clogging/1.png)

2. 捏住工具头散热增强风扇的顶部；向上提起，将其移除。

![](https://public-cdn.bblmw.com/wiki/new/h2c/troubleshooting/clogging/2.png)

3. 在屏幕上确认喷嘴温度为室温后，按压切刀切断耗材。

![](https://public-cdn.bblmw.com/wiki/new/h2c/troubleshooting/clogging/14.webp)

> **请注意一定要等到喷嘴温度降到室温后再切料，否则可能导致切刀处出现二次堵塞。**
>
> ![](https://public-cdn.bblmw.com/wiki/new/h2c/troubleshooting/clogging/3.png)

#### 步骤 2. 断开 PTFE 管

按压接头的黑色外圈，同时轻轻上拉 PTFE 管，使其与接头分离。

![](https://public-cdn.bblmw.com/wiki/new/h2c/troubleshooting/nozzle_unclogging/18.webp)

#### 步骤 3. 移除喷嘴

向右拉动喷嘴的拉柄完成解锁，取下右喷嘴组件。

![](https://public-cdn.bblmw.com/wiki/new/h2c/troubleshooting/clogging/method_for_removing_the_right_nozzle.webp)

#### 步骤 3. 释放进料通道并取出耗材

1. 用力向右推右从动杆（需要较大力度）。

![](https://public-cdn.bblmw.com/wiki/new/h2c/troubleshooting/clogging/push_right_idler_arm_to_right.png)

2. 一手继续保持从动杆的位置，另一手轻轻上拉耗材将其取出。

![](https://public-cdn.bblmw.com/wiki/new/h2c/troubleshooting/clogging/remove_filament.webp)

> **注意：** 若上拉过程中出现明显阻力或无法顺利取出，可能为挤出机堵塞。请**立即停止**，不要强行拉扯，以免卡得更紧；转到 **[排查方案 3](#sec-extruder-jam)** 继续处理。

3. 接着，找一段新耗材，尝试将其送入挤出机并尝试手动挤出，点击屏幕上的**挤出键**。如果打印机提示“请将喷嘴加热至170℃以上”，可选择“**本次不再提醒**”。

![](https://public-cdn.bblmw.com/wiki/new/h2c/troubleshooting/clogging/8.png)

- 若耗材顺利挤出，说明很可能是喷嘴堵塞了，建议您参考 **[2. 热端/喷嘴堵塞排查](#sec-hotend-nozzle)**
- 若耗材无法正常挤出或回抽，说明挤出机故障或者卡料，建议您参考 **[3. 挤出机堵塞排查](#sec-extruder-jam)**

### 2. 热端/喷嘴堵塞排查

若通过 “手动挤出” 无法将料线从喷嘴中挤出，或挤出的料线未完全替换为新加载的料线，则需使用通针疏通热端，并重复 “通针疏通 + 手动挤出” 的流程，直至堵塞解除，具体操作如下：

1. 在打印机触控屏主界面，依次点击 “**控制**” → “**喷嘴和挤出机**”，进入挤出机控制界面。

![](https://wiki.bambulab.com/h2c/troubleshoting/clogging/image1.png)

2. 选择 “**右边**”（针对右喷嘴），接着将右喷嘴温度设为略高于耗材的正常打印温度。（以 PLA 为例，可将温度设置为 220 ℃。）

![](https://wiki.bambulab.com/h2c/troubleshoting/clogging/image-2.png)

3. 待温度达标后，将通针缓慢插入喷嘴，上下反复疏通数次。

![](https://wiki.bambulab.com/h2c/troubleshoting/clogging/image-3.webp)

> ⚠️ **警告：** 使用清洁针疏通时，喷嘴内部压力可能突然释放，导致高温耗材意外喷出。清洁全程务必佩戴防护手套，且头部需远离打印机腔体，避免烫伤。

更多喷嘴疏通方法，可参考 [H2C 喷嘴/热端堵塞清理指南](unclogging.md)。

### 3. 挤出机堵塞排查

在 **2. 手动挤出** 中，**若向上拉动耗材时感受到明显阻力、无法顺利取出，说明堵塞可能发生在挤出机组件内部。** 此时请立即停止强行拉扯 —— 蛮力拔出可能导致耗材异常卡入从动杆组件，大幅增加后续清理难度。这种情况下，需拆除前盖导向组件，对挤出机内部（包括挤出从动杆、主动轮与从动轮的缝隙处及前盖导向本身）的堵塞进行清理。  
需要注意的是，前盖导向与左右切刀刀柄存在结构干涉，拆装过程会有一定难度；尤其当有耗材同时穿过挤出机齿轮与前盖导向时（如双色打印场景中，可能有两段耗材分别穿过左右两侧），操作难度会进一步增加。但请不必担心，只要按照下述建议操作，即可顺利完成前盖导向组件的拆除。

***在进行后续操作中，确保热端处于室温后***

![](https://public-cdn.bblmw.com/wiki/new/h2c/troubleshooting/clogging/3.png)

#### 步骤 1. 移除左、右切刀

1. 使用 H2.0 内六角扳手移除一颗左切刀固定螺丝，将切刀从挤出机中取出。

![](https://public-cdn.bblmw.com/wiki/new/h2c/troubleshooting/clogging/screw_for_left_cutter.png)

![](https://public-cdn.bblmw.com/wiki/new/h2c/troubleshooting/clogging/remove_left_cutter.webp)

2. 适用 H2.0 内六角扳手移除一颗右切刀固定螺丝，将切刀从挤出机中取出。

![](https://public-cdn.bblmw.com/wiki/new/h2c/troubleshooting/clogging/screw_for_right_cutter.png)

|  |  |
| --- | --- |
|  |  |

#### 步骤 2. 移除挤出机前盖导向

1. 用 H2.0 内六角扳手拧出前盖导向上的3颗螺丝。

![](https://public-cdn.bblmw.com/wiki/new/h2c/troubleshooting/clogging/4.png)

2. 依靠前盖导向两侧突起，直向外拉出前盖导向；若阻力较大，可在左侧螺丝孔后的加厚塑料区以螺丝刀顶住作支点配合外拉。该区域受力更稳，因此建议仅在此处辅助发力。

|  |  |
| --- | --- |
|  |  |

成功移除前盖导向后，请根据实际情况进行清理：

### 可能 1. 异常耗材可能堵在挤出机主动轮与从动轮缝隙中

1. 从挤出机上方剪断耗材，用镊子或者斜口钳夹住堵塞的耗材并向下用力。

![](https://public-cdn.bblmw.com/wiki/new/h2c/troubleshooting/clogging/7.webp)

> **注意：** 若拔出困难，可尝试在屏幕上切换挤出机，利用挤出机进行左右切换时松开耗材的间隙，将耗材拔出。
>
> ![](https://wiki.bambulab.com//h2/troubleshooting/clogging/image-262.png)

### 可能 2. 异常耗材可能堵在前盖导向入口或者内部。

1. 观察是否有异常耗材堵在前盖导向的入口处，使用斜口钳将耗材拔出即可。

![](https://public-cdn.bblmw.com/wiki/new/h2c/troubleshooting/clogging/remove_clogged_filament_in_dual_extruder_filament_guide.png)

2. 如果异常耗材堵塞在前盖导向的内部，那么需要将前盖导向拆开清理。先拧开1颗螺丝，然后沿着导轨移除黑色连接件，拆下切刀和弹簧。

![](https://public-cdn.bblmw.com/wiki/new/h2c/troubleshooting/clogging/disassemble_dual_extruder_filament_guide_1.png)

|  |  |
| --- | --- |
|  |  |

3. 使用H1.5的螺丝刀疏通黑色连接件以及导向组件的内部，防止有耗材仍然堵塞在里面。

|  |  |
| --- | --- |
|  |  |

4. 清理完成后，将弹簧重新安装到黑色连接件上，并沿着导轨装回连接件，请确保弹簧刚好套在红框中的滑块上。然后重新拧入螺丝并放回切刀。需要注意的是，切刀有一侧凹面，请确保装入切刀的时候凹面是朝上的。

![](https://public-cdn.bblmw.com/wiki/new/h2c/troubleshooting/clogging/disassemble_dual_extruder_filament_guide_6.png)

|  |  |
| --- | --- |
|  |  |

#### 步骤 4. 安装挤出机前盖导向与左切刀

1. 左切刀需要跟随前盖导向一起安装。确保左切刀的缺口面朝上，然后将其放入前盖导向的切刀槽中。

|  |  |
| --- | --- |
|  |  |

2. 安装前盖导向时，需要一直往上顶住黑色热端连接件；并轻微按压左切刀，将其调整到一个合适的角度便于左切刀进入，然后将前盖导向装入。最后按压两侧切刀，同时用力将前壳完全压平。

|  |  |
| --- | --- |
|  |  |

3. 然后重新锁紧前盖导向上的3颗螺丝（M2.5 x 7）。

![](https://public-cdn.bblmw.com/wiki/new/h2c/troubleshooting/clogging/remove_the_dual_extruder_filament_guide.png)

### 可能 3. 针对右喷嘴，异常耗材堵在从动杆出口或内部

这种情况非常罕见，若发生，建议使用H1.5的螺丝刀，尝试捅出耗材，若不能捅出，请参考 [H2C 从动杆卡料处理指南](dual-extruder-Idlers-clogging.md) 对从动杆出口进行清理。

如果仍然难以完成清理，则可以参考此教程：[H2C 挤出机拆解与安装](../../h2/troubleshooting/extruder-assembly.md)，更换从动杆组件。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)，点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
