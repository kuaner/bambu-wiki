---
path: zh/p2s/maintenance/replace-x-axis-assembly
title: "更换 P2S X 轴组件"
description: "更换 P2S 打印机 X 轴组件的操作流程"
tags: []
created: 2025-12-11T07:11:52.223Z
updated: 2026-10-12T06:50:54.618Z
source: https://wiki.bambulab.com/zh/p2s/maintenance/replace-x-axis-assembly
---

## X 轴组件

X 轴组件是工具头载体，工具头安装在X轴上，通过电机的驱动，可实现左右方向的移动。不同于 X1/P1 系列采用的碳杆方案，P2S 使用光杆方案。光杆为空心钢棒，性能与碳杆相似，但由于表面光滑，附着物更容易清理，日常保养更为方便。

![fac173.jpg](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/p2s-sku-pics/fac172.jpg)

## 适用场景

- X 轴组件损坏，需要更换

## 所需工具与材料

- 全新的 X 轴组件
- H1.5 内六角扳手
- H2.0 内六角扳手

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 移除工具头滑车与 X 轴组件

### 步骤 1. 移除工具头滑车

请参考 [更换 P2S 工具头滑车](replace-toolhead-carriage.md) 移除工具头滑车。

### 步骤 2. 移除 AP 板盖板与打印机外壳

1. 请参考 [更换 P2S AP 板盖/LED 补光灯 - 左](replace-ap-board-cover-and-led-light-left.md) 移除 AP 板盖：
2. 请参考以下指南拆卸后盖板和侧盖板：  
   [更换 P2S 背板](replace-rear-panel.md)  
   [更换 P2S 左侧板](replace-left-side-panel.md)  
   [更换 P2S 右侧板](replace-right-side-panel.md)

### 步骤 3. 移除 XY 皮带

使用内六角扳手顶住皮带固定座，将皮带固定块顶出一点，然后将皮带固定块从皮带上取下，即可将皮带取出。

|  |  |
| --- | --- |
|  |  |

> **ℹ️ 提示**：
>
> 1. 需要移除工具头左右的两个皮带固定座。
> 2. 如果皮带固定的比较松，您可以直接推动皮带取出固定块，无需使用内六角扳手顶出。
> 3. XY 皮带分为上下 2 条，左右两侧固定座上共 4 个固定点：上同步带 1 2 ；下同步带 3 4 。  
>    ![p2s-x2d_xy_belt1.jpg](https://wiki.bambulab.com/x2d/maintenance/x-axis-assembly/p2s-x2d_xy_belt0.jpg)

拉动 X 轴左右两侧的皮带。

![09_009.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-x-axis-assembly-and-toolhead-carriage/09_009.png)

将皮带从左右两个 Y 滑车上取下。

![11_011.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-x-axis-assembly-and-toolhead-carriage/11_011.png)

### 步骤 4. 移除 X 轴组件

使用 H1.5 内六角扳手移除 Y 滑车外侧挡板的四颗固定螺丝，将左右两个 Y 滑车的挡板都移除

![10_010.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-x-axis-assembly-and-toolhead-carriage/10_010.png)

转动 X 轴组件至打印机对角线方向，将 X 轴组件取出。

![12_012.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-x-axis-assembly-and-toolhead-carriage/12_012.png)

## 安装 X 轴组件与工具头滑车组件

### 步骤 1. 安装 X 轴组件

将 X 轴组件斜着放入打印机，将 Y 滑车与 Y 直线轴承对准，然后转动 X 轴组件装入；

![12_012.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-x-axis-assembly-and-toolhead-carriage/12_012.png)

👉 注意：安装完成后，请检查 Y 直线轴承的边缘是否与 Y 滑车对齐。若未对齐，请轻推轴承使与滑车对齐；若轴承突出过多，请将其拆下并重新安装。

![13_013.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-x-axis-assembly-and-toolhead-carriage/13_013.png)

在装挡板前请先查看挡板上的字母，左：L；右：R。标有 L 的挡板装在打印机的左侧，即靠近左侧板一侧；

![23_023.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-x-axis-assembly-and-toolhead-carriage/23_023.png)

安装左右两侧的挡板后，使用 H1.5 内六角扳手拧紧 8 颗固定螺丝（每侧 4 颗）

![10_010.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-x-axis-assembly-and-toolhead-carriage/10_010.png)

### 步骤 2. 安装 XY 皮带

将皮带末端对折，便于穿过 Y 滑车。

![14_014.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-x-axis-assembly-and-toolhead-carriage/14_014.png)

> **ℹ️ XY 皮带示意图**：同步带分为上下 2 条，工具头左右两侧各有 1 个皮带固定座，每个固定座含 2 个固定点。
>
> - 上同步带固定点： 1 2
> - 下同步带固定点：3 4
> - Y 滑车位置示意：5 6  
>   ![p2s-x2d_xy_belt1.jpg](https://wiki.bambulab.com/x2d/maintenance/x-axis-assembly/p2s-x2d_xy_belty.jpg)

先穿工具头左侧的皮带。如下图所示，将 1 侧的上同步带穿过 Y 滑车顶部的惰轮，将 3 的下同步带穿过 Y 滑车底部的惰轮。

|  |  |
| --- | --- |
|  |  |

将下同步带依次穿过机身前方的惰轮和 Y 滑车底部的惰轮。

|  |  |
| --- | --- |
|  |  |

将工具头左侧两根皮带分别穿入皮带固定座，使固定块的齿与皮带的齿准确对齐，确保凸起的点位于皮带的末端。

![](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-xy-belt/08_008.png)

拉动皮带，将固定块和皮带一起卡入固定座中。

|  |  |
| --- | --- |
|  |  |

用相同的方法穿好工具头右侧的皮带。

### 步骤 3. 安装 AP 板盖板与打印机外壳

1. 请参考以下指南安装后盖板与侧盖板：  
   [更换 P2S 背板](replace-rear-panel.md)  
   [更换 P2S 左侧板](replace-left-side-panel.md)  
   [更换 P2S 右侧板](replace-right-side-panel.md)
2. 请参考 [更换 P2S AP 板盖/LED 补光灯 - 左](replace-ap-board-cover-and-led-light-left.md) 安装 AP 板盖：

### 步骤 4. 安装工具头滑车

请参考 [更换 P2S 工具头滑车](replace-toolhead-carriage.md) 安装工具头滑车。

## 成功验证

接通电源并启动打印机，运行整机校准流程，确认校准能够顺利完成。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
