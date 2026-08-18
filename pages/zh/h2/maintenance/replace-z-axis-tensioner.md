---
path: zh/h2/maintenance/replace-z-axis-tensioner
title: "更换 H2 系列 Z 轴张紧器组件/Z 轴皮带/Z 轴同步轮"
description: "本文介绍了如何更换 H2 系列 Z 轴张紧器组件/Z 轴皮带/Z 轴同步轮"
tags: []
created: 2025-03-25T02:13:05.191Z
updated: 2026-08-06T09:28:10.678Z
source: https://wiki.bambulab.com/zh/h2/maintenance/replace-z-axis-tensioner
---

## Z 轴皮带/Z 轴同步轮/Z 轴张紧器

Z 轴皮带是安装在打印机底部、节线长为 1444mm ，宽度为 6mm 的闭口皮带。它连接 Z 轴电机和 Z 轴同步轮，带动热床完成在 Z 方向的移动。

**Z 轴皮带备件包含以下：**

1. Z 轴皮带 \* 1
2. Z 轴同步轮 \* 1
3. Z 轴同步轮盖 \* 1
4. M3x6 螺丝 - 用于将 Z 轴同步轮盖锁紧到 Z 轴同步轮上 \* 1
5. M3x35 螺丝 - 用于固定热床 \* 4

**Z 轴张紧器组件备件包含以下：**

1. Z 轴张紧器（含螺母）\* 1
2. Z 轴张紧器盖 \* 1
3. 扭簧 \* 1
4. 螺丝（银色）- 用于固定 Z 轴张紧器盖 \* 3
5. 螺丝（黑色）- 用于固定 Z 轴张紧器 \* 1

## 何时更换

- Z 轴皮带磨损
- Z 轴皮带断裂
- Z 轴同步轮损坏

## 所需的工具和材料

1. 新的 Z 轴皮带备件
2. H2.0 内六角扳手
3. H1.5 内六角扳手

**更换 H2D Z 电机所涉及的螺丝规格及数量（建议妥善保管拆下的螺丝，避免丢失）：**

| **螺丝规格** | **螺丝图片** | **用途** | **位置示意图** |  | **螺丝数量** |
| --- | --- | --- | --- | --- | --- |
| M3x6 |  | 用于固定 Z 张紧器滑块 |  |  | 1 |
| M3x6（螺帽直径 10mm） |  | 用于固定 Z 轴同步轮盖 |  |  | 1 |
| M3x35x8 |  | 用于固定 Z 滑块 |  |  | 4 |

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。
>
> 如果您对本指南有任何疑问，请点击此处联系在线技术支持 （服务时间 9:00-21:00），我们将及时回复并为您提供所需的帮助。

## 移除 Z 轴皮带/Z 轴同步轮

### 步骤 1：清洁打印机底座

清理打印机底座上的异物，特别是光杆处的残留物。

### 步骤 2：固定热床/Z 轴滑块

- **皮带/同步轮可以正常使用的情况**：

通过屏幕来控制热床，将热床下降至打印机底部。

![](https://wiki.bambulab.com/h2/maintenance/replace-z-axis-tensioner/image.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-z-axis-tensioner/image-1.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-z-axis-tensioner/image-2.png)

降低热床后使用螺丝将滑块固定，再关闭打印机电源，并断开电源连接。  
![](https://wiki.bambulab.com/h2/manual/unboxing-h2d//image-18.png)

![](https://wiki.bambulab.com/h2/manual/unboxing-h2d//image-19.png)

![](https://wiki.bambulab.com/h2/manual/unboxing-h2d//image-20.png)

> 注意：开箱时我们建议将拧下的四颗热床螺丝放入热床固定件中。  
> ![](https://wiki.bambulab.com/h2/manual/unboxing-h2d/img_v3_02ns_8f2b000d-f5a7-43ba-a7f0-74af6d413efg.jpg)

> **皮带/同步轮无法正常使用的情况：**
>
> 1. 关闭打印机电源，断开电源连接，拧下 6 颗热床螺丝，从 Z 轴滑块上取下热床，您可参阅移除热床的这篇 Wiki：[更换 H2D 热床组件](replace-heatbed-unit.md)；
> 2. 然后倾斜打印机，用手转动同步轮，将 Z 轴滑块下降到打印机底部，再用螺丝将滑块进行锁定。  
>    注：您可以左右转动同步轮来确认下降的方向。

### 步骤 3：移除上盖玻璃，放倒打印机

将打印机的上盖玻璃移除后，将打印机平稳地侧放在桌面上。

> 由于打印机比较重，建议两个人一起操作，避免由此带来的损伤。

### 步骤 4：移除 Z 轴张紧器组件

1. 释放 Z 轴张紧器扭簧，扭簧有力，小心操作，避免弹到伤人。  
   ![](https://wiki.bambulab.com/h2/maintenance/replace-z-axis-tensioner/image-11.png)
2. 使用 H2.0 内六角扳手移除圆圈标记的螺丝；该螺丝的另一端有个小螺母，若螺母掉出，需要保存好，后续安装的时候装回螺母；
3. 使用 H1.5 内六角扳手移除三颗 Z 轴张紧器盖的固定螺丝（绿色方框标记，BT2x5），取下 Z 轴张紧器盖和 Z 轴张紧扭簧；然后将 Z 轴张紧器滑块往前推，当张紧器底部的卡扣对准打印机底部的缺口时（上排两个，下排两个），即可将张紧器滑块取出。

![](https://wiki.bambulab.com/h2/maintenance/replace-z-axis-tensioner/image-6.png)

**注：在 Z 轴张紧器内部有一个螺母，在拆下 Z 轴张紧器时请注意该螺母，避免丢失。**

![](https://wiki.bambulab.com/h2/maintenance/replace-z-axis-tensioner/image-4.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-z-axis-tensioner/image-9.png)

### 步骤 5：移除 Z 轴皮带（无需更换 Z 皮带则请忽略该步骤）

将皮带沿着 Z 轴同步轮边缘取下。由于 Z 轴张紧器已经移除，这一步您可以直接将 Z 皮带取出。

![](https://wiki.bambulab.com/h2/maintenance/replace-z-axis-tensioner/image-10.png)

### 步骤 6：移除 Z 轴同步轮（无需更换同步轮则请忽略该步骤）

1. 使用 H2.0 内六角扳手移除 Z 轴同步轮盖固定螺丝（M3x6，螺帽直径 10mm），然后取下 Z 轴同步轮盖和固定螺丝；

![](https://wiki.bambulab.com/h2/maintenance/replace-z-axis-tensioner/image-3.png)

2. 将旧的 Z 轴皮带穿过 Z 轴同步轮下方，然后两手拿出皮带两端，拉动皮带，从而将同步轮取下。

> 需要将皮带靠近同步轮中心，避免在拉扯时脱落。

![](https://wiki.bambulab.com/h2/maintenance/replace-z-axis-tensioner/image-7.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-z-axis-tensioner/img_v3_02js_7a4995ea-e47f-42ec-9dfd-6905c57a2abg.jpg)

## 安装 Z 轴皮带/Z 轴同步轮/Z 轴张紧器组件

### 步骤 1：安装 Z 轴同步轮（如未拆同步轮则请忽略该步骤）

1. 将新的 Z 轴同步轮内侧的平面对准丝杆底部的平面，然后将同步轮装入丝杆；

![](https://wiki.bambulab.com/h2/maintenance/replace-z-axis-tensioner/image-5.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-z-axis-tensioner/img_v3_02js_1e8aca8f-d1ed-4c5f-9901-8ff82d43559g.jpg)

2. 将 Z 轴同步轮盖上的两个小孔对准同步轮上的凸起并扣入，然后使用一颗螺丝（M3x6，10mm）固定。

![](https://wiki.bambulab.com/h2/maintenance/replace-z-axis-tensioner/image-23.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-z-axis-tensioner/image-25.png)

### 步骤 2：安装 Z 轴皮带（如未拆 Z 轴皮带则请忽略该步骤）

参考下图，将新的 Z 轴皮带绕过三个同步轮和 Z 轴电机，安装至打印机上。皮带带齿的一面与同步轮接触。

![](https://wiki.bambulab.com/h2/maintenance/replace-z-axis-tensioner/image-24.png)

### 步骤 3：安装 Z 轴张紧器组件

按住热床，尝试再次拧紧热床固定螺丝，避免螺丝未紧固导致热床发生偏移。当热床固定螺丝均锁紧，即可开始下一步。

![](https://wiki.bambulab.com/h2/manual/unboxing-h2d//image-18.png)

![](https://wiki.bambulab.com/h2/manual/unboxing-h2d//image-19.png)

![](https://wiki.bambulab.com/h2/manual/unboxing-h2d//image-20.png)

**在安装前请确保 Z 轴张紧器的螺母装在 Z 张紧器滑块上**，然后参考下图将 Z 轴张紧器安装至对应位置。在安装的时候注意 Z 轴张紧器上的卡扣需要对准打印机底座上的缺口；然后先将扭簧安装至对应的立柱上，将短臂一侧卡在张紧器滑块上，长臂一侧卡在打印机底部的卡扣上。

![](https://wiki.bambulab.com/h2/maintenance/replace-z-axis-tensioner/image-22.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-z-axis-tensioner/image-26.png)

然后将 Z 轴张紧器盖装回，使用 H1.5 内六角扳手拧紧三颗 Z 轴张紧器盖固定的螺丝（绿色方框标记，BT2x5），然后给使用 H2.0 内六角扳手将 Z 张紧器滑块固定螺丝（红色圆圈标记，M3x6；不要完全拧紧，将在“**步骤 5**”中张紧皮带后再拧紧这一颗螺丝）。

![](https://wiki.bambulab.com/h2/maintenance/replace-z-axis-tensioner/img_v3_02js_ca4beede-0a54-4132-9d5f-323a0f57c5dg.jpg)

注：

- 在装回扭簧的时候，请检查短臂是否卡在 Z 轴张紧器滑块前端；
- 同时也请检查扭簧是否完全套在轴上，如果没有请按回。在按回扭簧的时候可能会由于震动导致 Z 轴张紧器滑块里面的螺母掉出，您可以使用一小节 PTFE 管（或其他物品）来堵住螺母，防止螺母掉出。

![](https://wiki.bambulab.com/h2/maintenance/replace-z-axis-tensioner/image-20.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-z-axis-tensioner/image-18.png)

### 步骤 4：正放打印机，解锁热床

将打印机正放在平稳的桌面/地面，然后使用 H2.0 内六角扳手移除四颗固定热床的螺丝（M3x35x8）。

> 由于打印机比较重，建议两个人一起操作，避免由此带来的损伤。

### 步骤 5：张紧皮带，拧紧螺丝，正放打印机

将打印机稍微倾斜，用手来回拉动 Z 轴皮带几次，确认动作顺畅，然后使用 H2.0 内六角扳手将 Z 轴张紧器滑块固定螺丝拧紧（M3x6）。

![](https://wiki.bambulab.com/h2/maintenance/replace-z-axis-tensioner/image-21.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-z-axis-tensioner/image-19.png)

拧紧之后将打印机重新正放在平稳的桌面/地面，并盖上上盖玻璃。

> 由于打印机比较重，建议两个人一起操作，避免由此带来的损伤。

## 如何验证成功

1. 连接电源，启动打印机
2. 如下图所示，运行设备自检流程，如果没有报错，更换同步带完成。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 为了确保您安全有效地进行操作，如果对指南中的任何步骤有疑虑或问题，请在开始操作前联系我们的客户服务团队，我们随时乐意为您解答疑问并提供支持。  
> [点击此处联系在线技术支持 （服务时间 9:00-21:00）](https://support.bambulab.cn/cn/im)
