---
path: zh/p2s/maintenance/replace-x-axis-assembly-and-toolhead-carriage
title: "更换 P2S X 轴组件/工具头滑车组件"
description: ""
tags: []
created: 2025-10-14T13:14:14.544Z
updated: 2025-10-14T14:25:08.463Z
source: https://wiki.bambulab.com/zh/p2s/maintenance/replace-x-axis-assembly-and-toolhead-carriage
---

## X 轴组件

X 轴组件是工具头载体，工具头安装在X轴上，通过电机的驱动，可实现左右方向的移动。不同于 X1/P1 系列采用的碳杆方案，P2S 使用光杆方案。光杆为空心钢棒，性能与碳杆相似，但由于表面光滑，附着物更容易清理，日常保养更为方便。  
![fac173.jpg](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/p2s-sku-pics/fac172.jpg)

## 工具头滑车组件

工具头滑车组件主要由滑车前盖和滑车后盖组成，安装在 X 轴组件的石墨铝套上，可以在 XY 皮带的牵引下实现在 X 方向上的移动。  
![fac170-1.jpg](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/p2s-sku-pics/fac170-1.jpg)

> 注：更换工具头滑车组件时，不需要移除打印机外壳。

## 何时更换

- X 轴组件损坏
- 工具头滑车组件损坏

## 需要的工具和材料

- 新的 X 轴组件 或 工具头滑车组件
- H1.5 内六角扳手
- H2.0 内六角扳手

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 移除 X 轴组件/工具头滑车组件

### 步骤 1：移除工具头上的组件

1. 参考以下 WIKI 移除 工具头外壳、热端、热端加热组件和热端风扇：  
   [更换 P2S 热端加热组件/热端风扇 | Bambu Lab Wiki](replace-hotend-heating-assembly-and-cooling-fan.md)
2. 参考以下 WIKI 移除切刀刀柄和挤出机组件：  
   [更换切刀刀柄 | Bambu Lab Wiki](replace-filament-cutter-lever.md)  
   [更换 P2S 挤出机配件 | Bambu Lab Wiki](replace-extruder-components.md)
3. 参考以下 WIKI 移除 TH 板/挤出接口板：  
   [更换 P2S 工具头电路板 | Bambu Lab Wiki](replace-th-boards-and-fpc-cable.md)  
   然后断开拖链支架，将工具头线缆及拖链从滑车上移除。
4. 参考以下 WIKI 移除涡流线圈：  
   [更换 P2S 涡流线圈 | Bambu Lab Wiki](replace-eddy-sensor.md)
5. 参考以下 WIKI 移除挤出电机：  
   [更换 P2S 挤出电机 | Bambu Lab Wiki](replace-3508-extruder-servo-motor.md)

### 步骤 2：移除皮带固定座

使用 H2.0 内六角扳手拧松（**拧松 1-2 圈即可，请勿卸下螺丝**）四颗张紧螺丝，放松 XY 皮带。

![](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/belt-tension/image.png)  
使用 H2.0 内六角扳手移除三颗皮带固定座螺丝，将皮带固定座取下。同样的操作，取下另一侧的皮带固定座。

![01_001.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-x-axis-assembly-and-toolhead-carriage/01_001.png)

![02_002.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-x-axis-assembly-and-toolhead-carriage/02_002.png)

### 步骤 3：移除工具头滑车组件

使用 H2.0 内六角扳手移除 8 颗固定螺丝，然后拿住工具头滑车前壳和后壳，先轻微倾斜滑车前壳，再将滑车取下，防止工具头滑车前壳顶部的四个弹簧掉落。

![03_003.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-x-axis-assembly-and-toolhead-carriage/03_003.png)

![04_004.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-x-axis-assembly-and-toolhead-carriage/04_004.png)

![05_005.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-x-axis-assembly-and-toolhead-carriage/05_005.png)

> 以下步骤是更换 X 轴组件才需要进行的步骤。

### 步骤 4：移除 AP 板盖

您可以参考这篇 Wiki 将 AP 板盖从框架上移除。

[更换 P2S AP 板盖/LED 补光灯 - 左 | Bambu Lab Wiki](replace-ap-board-cover-and-led-light-left.md)

### 步骤 5：移除打印机外壳

1. 移除料管支架、缓冲器和打印机背板：

[更换 P2S 背板 | Bambu Lab Wiki](replace-rear-panel.md)

2. 移除AP板盖和打印机左侧板

[更换 P2S 左侧板 | Bambu Lab Wiki](replace-left-side-panel.md)

3. 移除自适应风道切换组件和打印机右侧板

[更换 P2S 右侧板 | Bambu Lab Wiki](replace-right-side-panel.md)

### 步骤 6：移除 XY 皮带

1. 使用内六角扳手顶住皮带固定座，将皮带固定座顶出一点，然后将皮带固定块从皮带上取下，即可将皮带取出。如果皮带固定的比较松，您可以直接推动皮带取出固定块，无需使用内六角扳手顶出。

![](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-xy-belt/03_003.png)

![](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-xy-belt/04_004.png)

2. 拉动 X 轴左右两侧的皮带，将皮带从两个 Y 滑车上取下。

![09_009.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-x-axis-assembly-and-toolhead-carriage/09_009.png)

![11_011.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-x-axis-assembly-and-toolhead-carriage/11_011.png)

### 步骤 7：移除 X 轴组件

1. 使用 H1.5 内六角扳手移除 Y 滑车外侧挡板的四颗固定螺丝，将左右两个 Y 滑车的挡板都移除；

![10_010.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-x-axis-assembly-and-toolhead-carriage/10_010.png)

2. 转动 X 轴组件至打印机对角线方向，将 X 轴组件取出。

![12_012.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-x-axis-assembly-and-toolhead-carriage/12_012.png)

## 安装 X 轴组件/工具头滑车组件

> 以下第 1 步~第 3 步适用于安装X轴组件，第 4 步之后为更换 X 轴组件和更换工具头滑车共用步骤。

### 步骤 1：安装 X 轴组件

1. 将 X 轴组件斜着放入打印机，将 Y 滑车与 Y 直线轴承对准，然后转动 X 轴组件装入；

![12_012.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-x-axis-assembly-and-toolhead-carriage/12_012.png)

注：在装入后请检查 Y 直线轴承边缘是否和 Y 滑车对齐，如果没有对齐请推动轴承，将轴承与滑车对齐。如果凸出部分较多，请拆下重新安装。

![13_013.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-x-axis-assembly-and-toolhead-carriage/13_013.png)

2. 在装挡板前请先查看挡板上的字母，左：L；右：R。标有 L 的挡板装在打印机的左侧，即靠近左侧板一侧；

![23_023.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-x-axis-assembly-and-toolhead-carriage/23_023.png)

3. 将左右两侧的挡板装入，使用 H1.5 内六角扳手拧紧 8 颗固定螺丝（左右各四颗）。

![10_010.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-x-axis-assembly-and-toolhead-carriage/10_010.png)

### 步骤 2：穿 XY 皮带

1. 弯折皮带头部，便于皮带穿过 Y 滑车；

![14_014.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-x-axis-assembly-and-toolhead-carriage/14_014.png)

2. 参考下图将皮带穿过 Y 滑车上的惰轮；

![15_015.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-x-axis-assembly-and-toolhead-carriage/15_015.png)

3. 将皮带先穿过 Y 滑车，然后将皮带穿过前部的惰轮，最后从底部惰轮穿过；

![16_016.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-x-axis-assembly-and-toolhead-carriage/16_016.png)

![17_017.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-x-axis-assembly-and-toolhead-carriage/17_017.png)

![18_018.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-x-axis-assembly-and-toolhead-carriage/18_018.png)

3. 将皮带穿过皮带固定座，然后将皮带固定座的齿面对准皮带的齿面，并且凸起的点位于皮带的末端。然后拉动皮带，将固定快和皮带一起卡入固定座中。

![](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-xy-belt/08_008.png)

![19_019.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-x-axis-assembly-and-toolhead-carriage/19_019.png)

![08_008.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-x-axis-assembly-and-toolhead-carriage/08_008.png)

相同的方法装好另外一侧的皮带。

### 步骤 3：安装打印机外壳

1. 安装打印机右侧板和自适应风道切换组件

[更换 P2S 右侧板 | Bambu Lab Wiki](replace-right-side-panel.md)

2. 安装打印机左侧板和 AP 板盖

[更换 P2S 左侧板 | Bambu Lab Wiki](replace-left-side-panel.md)

3. 安装打印机背板、缓冲器和料管支架：

[更换 P2S 背板 | Bambu Lab Wiki](replace-rear-panel.md)

### 步骤 4：安装工具头滑车组件

1. 在安装前请先检查弹簧是否在工具头滑车前壳上；

![04_004.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-x-axis-assembly-and-toolhead-carriage/04_004.png)

2. 将 X 轴上两个铝套上下对齐，先将工具头滑车前壳的底部贴住铝套，再慢慢转动工具头滑车前壳直至前壳顶部贴住铝套；

![06_006.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-x-axis-assembly-and-toolhead-carriage/06_006.png)

![07_007.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-x-axis-assembly-and-toolhead-carriage/07_007.png)

3. 再将工具头滑车后盖装入，使用 H2.0 内六角扳手拧紧 8 颗固定螺丝，使用对角线的顺序来拧这八颗螺丝。

![03_003.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-x-axis-assembly-and-toolhead-carriage/03_003.png)

### 步骤 5：安装皮带固定座

1. 先将右侧的皮带固定座（靠近右侧板）安装至工具头上，使用 H2.0 内六角扳手拧紧三颗固定螺丝；

![20_020.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-x-axis-assembly-and-toolhead-carriage/20_020.png)

2. 将工具头推动至右后方，将另一侧皮带固定座用力推动至工具头上，使用 H2.0 内六角扳手拧紧三颗固定螺丝。

![21_021.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-x-axis-assembly-and-toolhead-carriage/21_021.png)

![22_022.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-x-axis-assembly-and-toolhead-carriage/22_022.png)

手动推动工具头滑车，沿 XY 方向尽可能大范围地往返移动 3-5 次，然后使用 H2.0 内六角扳手拧紧四颗张紧螺丝。

![](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/belt-tension/image.png)

### 步骤 6：安装工具头上的组件

1. 安装挤出电机：  
   [更换 P2S 挤出电机 | Bambu Lab Wiki](replace-3508-extruder-servo-motor.md)
2. 安装涡流线圈：  
   [更换 P2S 涡流线圈 | Bambu Lab Wiki](replace-eddy-sensor.md)

> 涡流线圈在所有配件安装好后，需要手动进行调整。

3. 安装 TH 板/挤出接口板：  
   安装拖链支架，将工具头线缆及拖链连接到工具头滑车上，然后安装工具头电路板。  
   [更换 P2S 工具头电路板 | Bambu Lab Wiki](replace-th-boards-and-fpc-cable.md)
4. 安装挤出机组件和切刀刀柄  
   [更换 P2S 挤出机配件 | Bambu Lab Wiki](replace-extruder-components.md)  
   [更换切刀刀柄 | Bambu Lab Wiki](replace-filament-cutter-lever.md)
5. 安装热端加热组件、热端风扇、工具头外壳和热端：  
   [更换 P2S 热端加热组件/热端风扇 | Bambu Lab Wiki](replace-hotend-heating-assembly-and-cooling-fan.md)

### 步骤 7：调整涡流线圈

参考以下 WIKI，调整涡流线圈位置。  
[P2S 涡流线圈调整 | Bambu Lab Wiki](adjust-the-eddy-sensor.md)

## 如何验证成功

连接电源，打开打印机，执行机器校准流程，确认能正常通过。

如果您遇到任何问题，请先查看所有更换步骤，并检查所有部件是否安装正确，然后重试。如果问题仍然存在，请联系 Bambu Lab 服务团队寻求进一步帮助。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)，点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
