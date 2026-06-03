---
path: zh/h2c/troubleshooting/dual-extruder-Idlers-clogging
title: "H2C 从动杆卡料处理指南"
description: ""
tags: []
created: 2025-11-18T13:16:24.325Z
updated: 2026-01-26T14:13:07.825Z
source: https://wiki.bambulab.com/zh/h2c/troubleshooting/dual-extruder-Idlers-clogging
---

## 适用场景

![卡料.jpg](https://wiki.bambulab.com//h2/troubleshooting/dual-extruder-idlers-clogging/%E5%8D%A1%E6%96%99.jpg)

- 打印机报错“挤出电机过载”或出现空打现象；
- 更换喷嘴组件后依然无法正常出料；
- 耗材卡在挤出机内，无法通过常规方式移除。

## 所需要工具和材料

- H2.0内六角螺丝刀
- H1.5内六角螺丝刀
- H1.0螺丝刀（用于顶出圆柱销）
- 尖嘴钳 （用于拔出残余耗材）
- 镊子（拆装小零件）

## 安全提示

> **重要提醒 ！**  
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。  
> 如果您对本指南有任何疑问，请[点击这里提交工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)，我们将及时回复并为您提供所需的帮助。

## 故障排除

### 步骤 1. 移除工具头增强散热风扇

1. 打开打印机前门，往上拔工具头增强散热风扇连接插头，将其断开；

![](https://public-cdn.bblmw.com/wiki/new/h2c/troubleshooting/clogging/1.png)

2. 捏住工具头散热增强风扇的顶部；向上提起，将其移除。

![](https://public-cdn.bblmw.com/wiki/new/h2c/troubleshooting/clogging/2.png)

3. **按下切刀刀柄**，以释放耗材张力。

![](https://public-cdn.bblmw.com/wiki/new/h2c/troubleshooting/clogging/14.webp)

按压接头的黑色外圈，同时轻轻上拉 PTFE 管，以断开 PTFE 管。

![](https://public-cdn.bblmw.com/wiki/new/h2c/troubleshooting/nozzle_unclogging/18.webp)

### 步骤 2. 移除左、右切刀

1. 使用 H2.0 内六角扳手移除一颗左切刀固定螺丝，将切刀从挤出机中取出。

![](https://public-cdn.bblmw.com/wiki/new/h2c/troubleshooting/clogging/screw_for_left_cutter.png)

![](https://public-cdn.bblmw.com/wiki/new/h2c/troubleshooting/clogging/remove_left_cutter.webp)

2. 适用 H2.0 内六角扳手移除一颗右切刀固定螺丝，将切刀从挤出机中取出。

![](https://public-cdn.bblmw.com/wiki/new/h2c/troubleshooting/clogging/screw_for_right_cutter.png)

|  |  |
| --- | --- |
|  |  |

接下来请您参考 [更换 H2C 挤出机前盖](../maintenance/replace-quick-change-tool-interface.md) 中的步骤，移除挤出机前盖。

### 步骤 3. 移除挤出机前盖导向

1. 用 H2.0 内六角扳手拧出前盖导向上的3颗螺丝。

![](https://public-cdn.bblmw.com/wiki/new/h2c/troubleshooting/clogging/4.png)

2. 依靠前盖导向两侧突起，直向外拉出前盖导向；若阻力较大，可在左侧螺丝孔后的加厚塑料区以螺丝刀顶住作支点配合外拉。该区域受力更稳，因此建议仅在此处辅助发力。

|  |  |
| --- | --- |
|  |  |

### 步骤 4. 初步清理残余废料

在移除前盖后，您可以尝试进行初步的残余耗材清理，使用尖嘴钳将耗材垂直向下拉出。

![](https://public-cdn.bblmw.com/wiki/new/h2c/troubleshooting/clogging/7.webp)

如果残余耗材的料头太短，或者通过初步尝试未能完全清理干净，则需要进一步拆卸从动轮组件进行彻底清理。

### 步骤 5. 移除从动轮组件

要彻底清理内部残留，您需要将从动轮组件从工具头上取下，您可以参考如下步骤移除从动轮组件。

> 注意：在移除从动轮组件时，请务必小心内部的排线，避免过度用力拉扯，以免造成排线损坏。

1. 使用 H1.5 内六角扳手卸下挤出机从动轮组件两侧用于固定霍尔排线的螺丝（BT2x5），随后拔出左右两侧霍尔排线插头

|  |  |
| --- | --- |
|  |  |
| 左侧霍尔排线 | |
|  |  |
| 右侧霍尔排线 | |

2. 使用 H2.0 内六角扳手卸下固定从动轮组件的两颗螺丝。

![](https://public-cdn.bblmw.com/wiki/new/h2c/troubleshooting/dual_extruder_idlers_clogging/5.png)

3. 取下从动轮组件。拆卸过程中凸轮可能松脱，请用手托住并妥善保管。

![](https://public-cdn.bblmw.com/wiki/new/h2c/troubleshooting/dual_extruder_idlers_clogging/6.png)

### 步骤 6. 清理从动轮组件

如下图所示，左右从动杆上各带有一个圆柱销，一侧凹陷，另一侧平齐。

![从动轮_结果.jpg](https://wiki.bambulab.com/h2/troubleshooting/dual-extruder-idlers-clogging/%E4%BB%8E%E5%8A%A8%E8%BD%AE_%E7%BB%93%E6%9E%9C.jpg)

> 注意：部分版本的从动杆正面两侧均为平齐，背面则为下凹。拆卸圆柱销时请务必从下凹侧向平齐侧顶出。

以左侧从动杆为例。

![正反1.png](https://wiki.bambulab.com/h2/troubleshooting/dual-extruder-idlers-clogging/%E6%AD%A3%E5%8F%8D1.png)

使用 H1.0 内六角螺丝刀（或合适尺寸的工具）将圆柱销顶出。注意螺丝刀应从**下凹侧向平齐侧顶出**。

![](https://wiki.bambulab.com/h2/troubleshooting/dual-extruder-idlers-clogging/顶出固定销1_结果.jpg)

顶出后可见平齐一端的滚花纹，这是其固定在从动杆上的关键结构。

![](https://wiki.bambulab.com/h2/troubleshooting/dual-extruder-idlers-clogging/顶出固定销_结果.jpg)

拧下霍尔小板的固定螺丝，缓慢抬起霍尔小板。

> **注意：** 从动杆内部有扭簧，在取下霍尔小板时可能弹出，请注意，避免丢失。

![](https://wiki.bambulab.com/h2/troubleshooting/dual-extruder-idlers-clogging/移除螺丝.jpg)

使用镊子依次取出扭簧与摇臂。

![](https://wiki.bambulab.com/h2/troubleshooting/dual-extruder-idlers-clogging/镊子取出_结果.jpg)

**从动杆组件构成：**

1. 从动杆主体
2. 扭簧
3. 摇臂
4. 霍尔小板

![](https://wiki.bambulab.com/h2/troubleshooting/dual-extruder-idlers-clogging/部件_结果.png)

> **注意：** 内部组件非常小，在拆卸和组装过程中请务必小心，避免遗失任何部件。建议在整洁、光线充足的工作台面上操作，并准备一个收纳盒来放置拆下的零件。

取出所有内部组件后，使用 H1.5 内六角螺丝刀（或合适的清理工具）从侧边孔道贯通，彻底清除通道内的耗材碎屑/堵塞物，确保完全畅通。

![](https://wiki.bambulab.com/h2/troubleshooting/dual-extruder-idlers-clogging/清理废料_结果.jpg)

### 步骤 7. 组装从动杆组件

1. 将摇臂正确放入从动杆主体对应的导向槽内。

![](https://wiki.bambulab.com/h2/troubleshooting/dual-extruder-idlers-clogging/安装摇臂.jpg)

2. 把扭簧较长的一端插入左侧小槽，用镊子微调扭簧与摇臂位置，使两者准确啮合。零件细小且有弹性，请耐心操作。

![](https://wiki.bambulab.com//h2/troubleshooting/dual-extruder-idlers-clogging/安装弹簧.webp)

3. 检查扭簧与摇臂是否完全到位

![](https://wiki.bambulab.com/h2/troubleshooting/dual-extruder-idlers-clogging/安装完成_结果.jpg)

4. 将圆柱销（固定销）重新插入，用镊子轻按住扭簧防止弹出。

> **注意插入方向： 应先插入光滑的一端，然后向内推入，直到圆柱销与从动杆表面平齐。**

![](https://wiki.bambulab.com/h2/troubleshooting/dual-extruder-idlers-clogging/插入销子_结果.jpg)

5. 将霍尔小板复位并拧紧固定螺丝

![](https://wiki.bambulab.com/h2/troubleshooting/dual-extruder-idlers-clogging/移除螺丝.jpg)

### 步骤 8. 安装从动轮组件

1. 将挤出机从动轮组件中部有螺丝的一侧朝向自己，然后拉动扭簧，将挤出机从动轮组件中部卡入凸轮，再往下按，直到卡到位。

![](https://public-cdn.bblmw.com/wiki/new/h2c/troubleshooting/dual_extruder_idlers_clogging/7.webp)

完成从动杆组件的重新组装后，即可将其重新安装回工具头。可以参考此 wiki [安装从动轮组件。](../../h2/maintenance/replace-dual-extruder-idlers-and-filament-sensor.md)

2. 使用 H2.0 内六角扳手拧紧固定从动轮组件的两颗螺丝。

|  |  |
| --- | --- |
|  |  |

### 步骤 9. 安装挤出机前盖

请您参考 [更换 H2C 挤出机前盖](../maintenance/replace-quick-change-tool-interface.md) 中的步骤，安装挤出机前盖。

## 功能测试

打印机的触摸屏或控制界面上，点击“**进料**”选项，观察喷嘴是否能正常挤出耗材。如果喷嘴出料顺畅且无异常，则表明修复工作已成功完成。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)；点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
