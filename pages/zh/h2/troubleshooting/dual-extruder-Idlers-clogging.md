---
path: zh/h2/troubleshooting/dual-extruder-Idlers-clogging
title: "H2D 从动杆卡料处理指南"
description: ""
tags: []
created: 2025-06-05T03:54:01.539Z
updated: 2026-01-26T13:46:57.843Z
source: https://wiki.bambulab.com/zh/h2/troubleshooting/dual-extruder-Idlers-clogging
---

## 适用场景

![卡料.jpg](https://wiki.bambulab.com/h2/troubleshooting/dual-extruder-idlers-clogging/%E5%8D%A1%E6%96%99.jpg)

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

### 移除挤出机前盖

![](https://wiki.bambulab.com/h2/troubleshooting/image-14.png)

**按下切刀刀柄**，以释放耗材张力。

![按下切刀_结果.jpg](https://wiki.bambulab.com/h2/troubleshooting/dual-extruder-idlers-clogging/%E6%8C%89%E4%B8%8B%E5%88%87%E5%88%80_%E7%BB%93%E6%9E%9C.jpg)

**打开特氟龙管接口**，剪断耗材，避免清理过程中耗材拉扯导致清理困难（此步骤可以尝试向上拔出如果不能轻松拔出请立刻停止，可能会导致耗材卡的更紧）。

![简单耗材_结果.jpg](https://wiki.bambulab.com/h2/troubleshooting/dual-extruder-idlers-clogging/%E7%AE%80%E5%8D%95%E8%80%97%E6%9D%90_%E7%BB%93%E6%9E%9C.jpg)

接下来您可以参考此 wiki 将[挤出机前盖移除](../maintenance/replace-quick-change-tool-interface.md)。

### 初步清理残余废料

在移除前盖后，您可以尝试进行初步的残余耗材清理，使用尖嘴钳将耗材垂直向下拉出。

![钳子向下拔出_结果.jpg](https://wiki.bambulab.com/h2/troubleshooting/dual-extruder-idlers-clogging/%E9%92%B3%E5%AD%90%E5%90%91%E4%B8%8B%E6%8B%94%E5%87%BA_%E7%BB%93%E6%9E%9C.jpg)

如果残余耗材的料头太短，或者通过初步尝试未能完全清理干净，则需要进一步拆卸从动轮组件进行彻底清理。

### 移除从动轮组件

要彻底清理内部残留，您需要将从动轮组件从工具头上取下，可以参考此wiki将[从动轮组件轮组件移除。](../maintenance/replace-dual-extruder-idlers-and-filament-sensor.md)

> 在移除从动轮组件时，请务必小心内部的排线，避免过度用力拉扯，以免造成排线损坏。

### 清理从动轮组件

如下图所示，左右从动杆上各带有一个圆柱销，一侧凹陷，另一侧平齐。

![从动轮_结果.jpg](https://wiki.bambulab.com/h2/troubleshooting/dual-extruder-idlers-clogging/%E4%BB%8E%E5%8A%A8%E8%BD%AE_%E7%BB%93%E6%9E%9C.jpg)

> 注意：部分版本的从动杆正面两侧均为平齐，背面则为下凹。拆卸时请务必从下凹侧向平齐侧顶出。

以左侧从动杆为例。

![正反1.png](https://wiki.bambulab.com/h2/troubleshooting/dual-extruder-idlers-clogging/%E6%AD%A3%E5%8F%8D1.png)

使用 H1.0 内六角螺丝刀（或合适尺寸的工具）将圆柱销顶出。注意螺丝刀应从**下凹侧向平齐侧顶出**。

![顶出固定销1_结果.jpg](https://wiki.bambulab.com/h2/troubleshooting/dual-extruder-idlers-clogging/%E9%A1%B6%E5%87%BA%E5%9B%BA%E5%AE%9A%E9%94%801_%E7%BB%93%E6%9E%9C.jpg)

顶出后，会发现平齐一端的圆柱销带有滚花纹，这是其固定在从动杆上的关键结构。

![顶出固定销_结果.jpg](https://wiki.bambulab.com/h2/troubleshooting/dual-extruder-idlers-clogging/%E9%A1%B6%E5%87%BA%E5%9B%BA%E5%AE%9A%E9%94%80_%E7%BB%93%E6%9E%9C.jpg)

拧下霍尔小板的固定螺丝，并小心地移除霍尔小板。在移除过程中，请务必注意内部有一枚扭簧，可能会在霍尔小板移除时弹出并遗失。

![移除螺丝.jpg](https://wiki.bambulab.com/h2/troubleshooting/dual-extruder-idlers-clogging/%E7%A7%BB%E9%99%A4%E8%9E%BA%E4%B8%9D.jpg)

使用镊子小心地取出扭簧和摇臂。

![镊子取出_结果.jpg](https://wiki.bambulab.com/h2/troubleshooting/dual-extruder-idlers-clogging/%E9%95%8A%E5%AD%90%E5%8F%96%E5%87%BA_%E7%BB%93%E6%9E%9C.jpg)

整个从动杆组件由以下几个部分构成：

1. 从动杆主体
2. 扭簧
3. 摇臂
4. 霍尔小板

![部件_结果.png](https://wiki.bambulab.com/h2/troubleshooting/dual-extruder-idlers-clogging/%E9%83%A8%E4%BB%B6_%E7%BB%93%E6%9E%9C.png)

> 注意： 内部组件非常小，在拆卸和组装过程中请务必小心，避免遗失任何部件。建议在整洁、光线充足的工作台面上操作，并准备一个收纳盒来放置拆下的零件。

取出所有内部组件后，使用 H1.5 内六角螺丝刀（或合适的清理工具）穿过从动杆的侧边孔道，彻底清除内部残余的耗材碎片或堵塞物。确保通道完全畅通无阻。

![清理废料_结果.jpg](https://wiki.bambulab.com/h2/troubleshooting/dual-extruder-idlers-clogging/%E6%B8%85%E7%90%86%E5%BA%9F%E6%96%99_%E7%BB%93%E6%9E%9C.jpg)

### 安装从动杆组件

首先，将摇臂正确放入从动杆主体对应的槽内。  
![安装摇臂.jpg](https://wiki.bambulab.com/h2/troubleshooting/dual-extruder-idlers-clogging/%E5%AE%89%E8%A3%85%E6%91%87%E8%87%82.jpg)

接下来是安装扭簧。将扭簧较长的一端插入左侧的小槽内。然后，使用镊子小心地微调扭簧和摇臂的位置，确保它们正确啮合。由于零件微小且有弹性，此步骤需要一定的耐心和精确操作。

![安装弹簧.webp](https://wiki.bambulab.com/h2/troubleshooting/dual-extruder-idlers-clogging/%E5%AE%89%E8%A3%85%E5%BC%B9%E7%B0%A7.webp)

下图所示为扭簧和摇臂正确安装后的状态。

![安装完成_结果.jpg](https://wiki.bambulab.com/h2/troubleshooting/dual-extruder-idlers-clogging/%E5%AE%89%E8%A3%85%E5%AE%8C%E6%88%90_%E7%BB%93%E6%9E%9C.jpg)

将圆柱销重新插入，以固定摇臂和扭簧。在插入圆柱销时，可以使用镊子辅助，轻轻按住扭簧，防止其弹出。**注意插入方向： 应先插入光滑的一端，然后向内推入，直到圆柱销与从动杆表面平齐。**

![插入销子_结果.jpg](https://wiki.bambulab.com/h2/troubleshooting/dual-extruder-idlers-clogging/%E6%8F%92%E5%85%A5%E9%94%80%E5%AD%90_%E7%BB%93%E6%9E%9C.jpg)

最后，安装回霍尔小板并拧紧固定螺丝。

![移除螺丝.jpg](https://wiki.bambulab.com/h2/troubleshooting/dual-extruder-idlers-clogging/%E7%A7%BB%E9%99%A4%E8%9E%BA%E4%B8%9D.jpg)

### 安装从动轮组件

完成从动杆组件的重新组装后，即可将其重新安装回工具头。可以参考此 wiki [安装从动轮组件。](../maintenance/replace-dual-extruder-idlers-and-filament-sensor.md)

### 安装挤出机前盖

最后一步是重新安装挤出机前盖。可以参考此 wiki [安装挤出机前盖](../maintenance/replace-quick-change-tool-interface.md)。

## 功能测试

打印机的触摸屏或控制界面上，点击“**进料**”选项，观察喷嘴是否能正常挤出耗材。如果喷嘴出料顺畅且无异常，则表明修复工作已成功完成。

![](https://wiki.bambulab.com/h2/manual/screen-operation/image-1.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南并未解决您的问题，[*请点击此处联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
