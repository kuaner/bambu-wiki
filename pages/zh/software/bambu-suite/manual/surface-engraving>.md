---
path: zh/software/bambu-suite/manual/surface-engraving>
title: "Bambu H2D 曲面雕刻功能使用指南"
description: "本文将详细为您介绍Bambu Suite 曲面激光雕刻功能和使用 H2D 进行曲面激光雕刻的详细步骤。"
tags: []
created: 2025-09-25T11:00:02.959Z
updated: 2026-02-25T01:31:49.903Z
source: https://wiki.bambulab.com/zh/software/bambu-suite/manual/surface-engraving>
---

> **注意**：请将 H2D 或 H2C 的固件更新到最新版本，H2S 预计四月份发布相关固件支持。  
> 本页面以 H2D 机器为例。**H2C 的操作方式相同**。

## 曲面雕刻介绍

曲面雕刻是Bambu H2D 3D打印机的一项高级功能，它利用高精度激光模组和集成的测高激光器，实现在三维曲面物体上进行图案雕刻。与传统的平面激光雕刻不同，H2D的曲面雕刻功能可以自动测量物体表面形状，并调整激光路径，确保激光光斑对焦于曲面表面进行图案雕刻。

![](https://wiki.bambulab.com/software/bambu-suite/manual/curved-surface-machining/image-10.png)

**常见应用场景：**在日常生活中的曲面物体（如易拉罐、保温杯、餐具）上雕刻文字或图案，或是工具手柄等物体上进行序列号打标等。

![](https://wiki.bambulab.com/software/bambu-suite/manual/curved-surface-machining/%E5%8F%AF%E4%B9%90.png)

[

Your browser does not support the video tag.
](https://public-cdn.bblmw.com/wiki/software/bambu-suite/manual/curved-surface-laser-engraving-CN.mp4)

**固件版本要求：**H2D固件版本不低于01.02.00.00。

## 曲面雕刻材料要求

在加工曲面物体之前，要确保材料的形状和材质符合以下要求：

### 表面特性

- 需平滑曲面，不能有剧烈起伏**（最大支持15mm高度差）**
- 曲面任意位置的切线与水平面夹角≤40°

![](https://wiki.bambulab.com/software/bambu-suite/manual/curved-surface-machining/image-9.png)

### 几何限制

- 高度突变（如阶梯状物体）
- 尖角/内斜角（某些面激光难以扫描到）

不支持高度突变、尖角和内斜角

![](https://wiki.bambulab.com/software/bambu-suite/manual/curved-surface-machining/image-8.png)

- 镂空结构（扫描和雕刻会不稳定）

![](https://wiki.bambulab.com/software/bambu-suite/manual/curved-surface-machining/img_v3_02ov_ecbc3464-2103-45fc-9d86-87563d70b84g.jpg)

### 材质限制

- **不支持透明材质（普通玻璃、透明亚克力等）和镜面材质（强反光金属、镜子等）**。测高激光器在扫描透明或镜面材质物体时会有噪声或者异常，如果需要加工该类型物体，请谨慎确认扫描结果。如扫描结果有异常，则不要继续加工，以免造成加工材料的损坏。
- **尺寸限制。**若物体尺寸偏小（横截面小于3cm \* 3cm），在雕刻前建议在下面用方垫块面积较大的平板或者垫高物体（高度>2cm)，材料均需要不透明不反光（防止扫描的时候将物体周围的底板和刀条等都扫描进去）。这种情况请尽量把小物体固定在平板上，防止其在机器运动过程中晃动影响雕刻质量。

|  |  |
| --- | --- |
| 未垫平板 | 未垫平板的扫描结果 |
| 物体下垫平板 | 物体下垫平板的扫描结果 |

## 曲面雕刻使用流程

### 1. **添加图案并选择加工模式**

（1）在 Bambu Suite 设计页面导入或者创建要加工的图案（支持 SVG、PNG 等格式），并在工艺类型选择**激光线条雕刻**、**激光填充雕刻** 或 **激光图像雕刻。**

|  |  |
| --- | --- |
|  |  |

（2）进入**制作页面，**在加工模式中选择**曲面加工**

![](https://wiki.bambulab.com/software/bambu-suite/manual/curved-surface-machining/no1%E8%8B%B1%E6%96%87.png)

### 2. **曲面拍照和测量**

#### 准备工作

- 确保材料最高点不超过H2D激光模组的高度（防止碰撞）
- 待加工物体应稳固放置于热床中央，避免晃动
- 机箱内只放置唯一的待加工物体

#### 俯视相机拍照

> 注意：在放置好工件拍照扫描后，**不要进行任何移动工件、热床**的操作，以免损坏打印机内的部件。

- 点击**"拍照"**，H2D的俯视摄像头会拍摄物体表面，确保完整捕捉物体表面轮廓。**在曲面测量前，需要先拍照获得加工平面图，该图片用于在曲面测量时框选测量区域**

![](https://wiki.bambulab.com/software/bambu-suite/manual/curved-surface-machining/100.png)

#### 曲面测量

- 点击**“曲面测量”**，根据引导在软件上框选要测量区域进行曲面测量**（建议框选略大于物体的测量区域，且只支持框选唯一的测量区域）。若未正确框选，重新框选一次即可。测量过程中请勿关闭打印机或者使电脑处于休眠状态。**

![](https://wiki.bambulab.com/software/bambu-suite/manual/curved-surface-machining/no2%E4%B8%AD%E6%96%87.png)

![](https://wiki.bambulab.com/software/bambu-suite/manual/curved-surface-machining/no3%E4%B8%AD%E6%96%87.png)

- H2D 会通过激光模组的测高激光器进行高精度曲面建模，生成点云数据后，可预览物体 3D 轮廓。

![](https://wiki.bambulab.com/software/bambu-suite/manual/curved-surface-machining/no4%E4%B8%AD%E6%96%87.png)

- 如需重新扫描，需等到热床停止移动时，再点击 **"重新测量"**，回到测量页面后重新选择区域测量即可。

![](https://wiki.bambulab.com/software/bambu-suite/manual/curved-surface-machining/5.png)

### 3. **加工设置**

（1）在准备页面将图案对齐至点云区域，可以通过点云预览图案在曲面的摆放位置和效果

![](https://wiki.bambulab.com/software/bambu-suite/manual/curved-surface-machining/no5%E4%B8%AD%E6%96%87.png)

（2）在材料组中选择材料，设置**激光功率、速度、次数**（建议先测试合适的参数）

![](https://wiki.bambulab.com/software/bambu-suite/manual/curved-surface-machining/8-1.png)

（3）点击**“制作”**按钮，软件将会把加工任务发送给打印机，即可开始加工。

![](https://wiki.bambulab.com/software/bambu-suite/manual/curved-surface-machining/no6%E5%8F%91%E9%80%81%E6%89%93%E5%8D%B0_.gif)

### 4. 检查雕刻效果

雕刻完成后，检查图案清晰度和曲面适配度。若效果不理想，可调整参数后重新扫描+雕刻。

![](https://wiki.bambulab.com/software/bambu-suite/manual/curved-surface-machining/no7.png)

## 曲面雕刻注意事项

### 材料放置

- **物体尽量放在热床中央，**避避免边缘扫描盲区。垫板盲区范围（测高激光器扫描限制）：**左侧约 6cm 内和靠近前门侧约 4cm 内的范围是扫描不到的，**故故不建议将材料放置在这个范围内，曲面测量时也无法测量这个区域。

|  |  |  |
| --- | --- | --- |
|  |  |  |

- **物体高度＜240mm**
- 拍照前，机器会移动工具头到废料槽位置，为了防止工具头撞倒加工件，**放置材料后务必确保激光模组位于材料最高点上方**，确保加工安全。

![](https://wiki.bambulab.com/software/bambu-suite/manual/curved-surface-machining/img_v3_02p2_1c13e0e3-2332-4043-b6c4-8b034961c0cg.png)

- **需要扫描的面朝向门的方向摆放，**否则可能会导致激光被遮挡，无法扫描到目标区域

### 参数调试

由于 H2D 曲面雕刻涉及非标准材料，官方未提供固定参数，因此我们建议：

- 可先选择材料较为接近的官方材料参数进行测试（如加工金属可选择易拉罐的加工参数）
- 若官方参数未能满足加工需求，可使用边角料进行多组参数测试。在同一物体上测试不同功率/速度组合，记录最佳参数，并在材料组的左下角点击“新建材料”，将其保存方便后续使用。

![](https://wiki.bambulab.com/software/bambu-suite/manual/curved-surface-machining/image-13.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)；点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
