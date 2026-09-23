---
path: zh/r1/manual/curved-surface-machining-guide
title: "R1 曲面加工指南"
description: "本文介绍了如何进行 R1 曲面加工"
tags: []
created: 2026-09-22T12:47:58.103Z
updated: 2026-09-22T12:47:59.371Z
source: https://wiki.bambulab.com/zh/r1/manual/curved-surface-machining-guide
---

## 曲面雕刻介绍

曲面雕刻是 Bambu Lab R1 激光切割机的一项高级功能，它利用高精度激光模组和集成的测高激光器，实现在三维曲面物体上进行图案雕刻。与传统的平面激光雕刻不同，R1 曲面雕刻可以自动测量物体表面形状，并调整激光路径，确保激光光斑对焦于曲面表面进行图案雕刻。

**常见应用场景：** 在日常生活中的曲面物体（如易拉罐、保温杯、餐具）上雕刻文字或图案，或是工具手柄等物体上进行序列号打标等。

## 材料要求

在加工曲面物体之前，要确保材料的形状和材质符合以下要求：

### 表面特性

- 需平滑曲面，不能有剧烈起伏，高度差不超过 6 cm；
- 曲面任意位置的切线与水平面夹角 ≤ 40°；

![001.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/curved-surface-machining-guide/zh/001.png)

### 几何限制

- 高度突变（如阶梯状物体）
- 尖角/内斜角（某些面激光难以扫描到）
- 不支持高度突变、尖角和内斜角
- 镂空结构（扫描和雕刻会不稳定）

### 材质限制

**不支持透明材质（普通玻璃、透明亚克力等）和镜面材质（强反光金属、镜子等）**。测高激光器在扫描透明或镜面材质物体时会有噪声或者异常，如果需要加工该类型物体，请谨慎确认扫描结果。如扫描结果有异常，则不要继续加工，以免造成加工材料的损坏。

## 加工流程

### 取下工具头气嘴

为获得更佳的曲面加工效果，建议在开始前取下工具头气嘴，可避免加工时气嘴撞到材料。

![002.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/curved-surface-machining-guide/zh/002.png)

### **添加图案并选择加工模式**

- 在 Bambu Suite 设计页面导入或者创建要加工的图案（支持 SVG、PNG、PDF 等格式）；

![003.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/curved-surface-machining-guide/zh/003.png)

- 在工艺类型中选择**激光线条雕刻**、**激光填充雕刻**或**激光线条切割**。

![004.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/curved-surface-machining-guide/zh/004.png)

- 进入**制作页面，** 在加工模式中选择**曲面加工**；

![005.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/curved-surface-machining-guide/zh/005.png)

### **曲面拍照和测量**

#### **放置材料**

如果材料较厚，可使用增高架，或将材料直接放置在托盘上加工，防止碰撞；各种情况下材料可加工最大厚度可参考下表：

| **材料放置位置** |  | **材料最大厚度** | **示意图** |
| --- | --- | --- | --- |
| 主机 | 刀条 | 21 mm | Image |
| 主机 | 托盘 | 59.8 mm | Image |
| 增高底座 | 托盘 1 | 120.66 mm | Image |
| 增高底座 | 托盘 2 | 165.66 mm | Image |
| 增高底座 | 托盘 3 | 210.66 mm | Image |

> **注意：**
>
> - 待加工物体应稳固放置，避免晃动；
> - 建议机箱内只放置**唯一**的待加工物体。

#### **拍照测量**

- 点击 **"一键准备"** 按钮，如果机箱内只放置了唯一的待加工物体，机器会自动拍照并测量物体表面；如果机箱内放置了多个物体，机器会提示您先框选区域，再开始测量；

> 注意：
>
> - 在放置好工件拍照扫描后，**请勿移动加工物体**，以免影响制作效果；
> - 过程中**请勿关闭打印机或者使电脑处于休眠状态。**

![011.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/curved-surface-machining-guide/zh/011.png)

- 测量完成后，suite 会显示点云数据，可预览物体 3D 轮廓；

![012.webp](https://public-cdn.bblmw.com/wiki/new/r1/manual/curved-surface-machining-guide/zh/012.webp)

- 如需框选特定区域进行扫描，可选择“框选选区测量”或“手拖工具头选区测量”；

> 有关手拖工具头选区测量的具体操作请参考：[手拖工具头功能介绍](toolhead-drag-measurement.md)。

![013.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/curved-surface-machining-guide/zh/013.png)

- 如需重新扫描，需等到工具头停止移动时，再点击“**重新测量**”，回到测量页面后重新选择区域测量即可。

|  |  |
| --- | --- |
| 014.png | 015.png |

### **加工设置**

- 在准备页面将图案对齐至点云区域，可以通过点云预览图案在曲面的摆放位置和效果；

![016.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/curved-surface-machining-guide/zh/016.png)

- 在材料组中选择材料，设置激光功率、速度和次数；如果使用的是官方材料，可直接使用对应材料的参数；如果使用的是第三方材料，建议进行材料加工参数标定，具体请参考后文【曲面雕刻注意事项——参数调试】；

![017.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/curved-surface-machining-guide/zh/017.png)

- 点击“制作”按钮，软件将会把加工任务发送给打印机，即可开始加工。

![018.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/curved-surface-machining-guide/zh/018.png)

### 检查雕刻效果

雕刻完成后，检查图案清晰度和曲面适配度。若效果不理想，可调整参数后重新扫描雕刻。

## 曲面雕刻注意事项

### 材料放置

- 物体**尽量靠近工具头**，但防止碰撞；
- 最优的扫描高度范围在工具头到滚轮送料平面之间，可以将低矮物体适当垫高，以保证扫描效果；
- 物体摆放需避开垫板左侧 6 cm 范围内的不可扫描区域；

![019.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/curved-surface-machining-guide/zh/019.png)

- 物体放置于增高架时，注意在水平方向避开上方或者周围可能放置的齿条，避免对扫描和雕刻造成影响。

### 雕刻位置

由于测距激光光路并非垂直向下，而是朝向右下方，且偏移量会随材料高度产生额外波动。

![020.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/curved-surface-machining-guide/zh/020.png)

- 当**曲面凹面朝上**时，在左侧面扫描的位置可能会被遮挡，建议优先将图案放在材料右侧雕刻；

![021.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/curved-surface-machining-guide/zh/021.png)

- 当**曲面凸面朝上**时，在右侧面扫描的位置可能会被遮挡，建议优先将图案放在材料左侧雕刻。

![022.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/curved-surface-machining-guide/zh/022.png)

### 参数调试

由于实际制作过程中可能涉及**非标准材料**，官方未提供固定参数，因此我们建议：

- 可先选择材料**较为接近的官方材料**参数进行测试（如加工金属可选择易拉罐的加工参数）；
- 若官方参数未能满足加工需求，可使用边角料进行多组参数测试。在同一物体上测试不同功率/速度组合，记录最佳参数，并在“选择材料”框的右上角点击 **“新建材料”**，将其保存方便后续使用。具体请参考：[Bambu Suite 材料参数标定、录入和加工优化指导](../../h2/software/bambu-suite/manual/material-parameter-calibration-and-machining-optimization.md)。

![023.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/curved-surface-machining-guide/zh/023.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
