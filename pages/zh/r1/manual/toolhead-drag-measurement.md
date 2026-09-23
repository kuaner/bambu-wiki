---
path: zh/r1/manual/toolhead-drag-measurement
title: "R1 手拖工具头功能介绍"
description: "本文介绍了 R1 手拖工具头功能"
tags: []
created: 2026-09-22T12:48:29.614Z
updated: 2026-09-22T12:48:30.871Z
source: https://wiki.bambulab.com/zh/r1/manual/toolhead-drag-measurement
---

## 手拖工具头功能介绍

R1 支持用户手动拖动工具头，可完成**材料****选点****测距、加工选区和曲面测量**等操作，适合材料摆放不规则、摄像头视野受限等场景。

## 手拖工具头测量

除了在 Bambu Suite 画布选点测距外，还可直接将工具头拖动到需要测量的位置，获取激光焦点到材料表面的距离。

### 适用场景

- 材料表面不平整，在画布上难以准确选到测量点；
- 作为选点测距、快速测距之外的补充方式，适合精确定位单点距离/厚度。

### 操作步骤

有关手拖工具头测量和触碰测量的具体信息请参考：[R1 材料距离测量](../../../en/r1/manual/material-thickness-measurement.md)。

![](https://public-cdn.bblmw.com/wiki/new/r1/manual/material-thickness-measurement/zh/011.png)

### 限制与前提条件

- 主要用于**平面加工**和**滚轮送料加工**模式，其他模式需使用对应的测距方式；
- 若设备已装载**旋转轴组件**，则无法使用测距功能，须先拆卸旋转轴组件；
- 部分机型可能不支持，具体是否显示该测量方式，取决于机型配置；
- 设备测距过程中请勿移动材料，避免测量失败或数值偏差。

## 手动选择加工区域

当需要在材料上选定某一块可加工区域作为参考时，可手拖工具头进行选择。

### 适用场景

- 材料形状不规则，拍照后无法准确获取材料轮廓，难以框选边界；

![008.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/toolhead-drag-measurement/zh/008.png)

- 俯视摄像头故障，无法拍照获取加工平面图像，但需要准确定位材料位置用于摆放图案。

### 操作步骤

1. 进入“准备”页面，在上方工具栏里选择“标定加工区域”图标；

![009.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/toolhead-drag-measurement/zh/009.png)

选择需要标定加工区域的形状；

![010.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/toolhead-drag-measurement/zh/010.png)

2. 按照提示打开上盖，将工具头拖到目标位置，即为打点；按下设备按钮，完成每个打点的标记；

![011.webp](https://public-cdn.bblmw.com/wiki/new/r1/manual/toolhead-drag-measurement/zh/011.webp)

**以下为各加工区域形状的打点要求：**

| **形状** | **需标记点数** | **备注** |
| --- | --- | --- |
| 矩形 | 2 | **两点不能在同一水平线上**，否则无法正确生成矩形 |
| 三点画圆 | 3 | 三点确定一个圆 |
| 中心画圆 | 2 | 圆心点——边缘点 |
| 多边形 | 多点 | 按顺序标记各顶点 |
| 线段 | 2 | 线段两端 |

3. suite 会实时显示已标记的点、当前工具头 XY 坐标及生成的区域预览；

![012.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/toolhead-drag-measurement/zh/012.png)

4. 标记完成后，在 suite 或者屏幕上点击“完成”/“确认”；如需放弃，可点击“取消”或在设备端结束操作。

|  |  |
| --- | --- |
| 013.png | 014.png |

5. 在 suite 中将需要加工的图案放进框选的加工区域中。

![015.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/toolhead-drag-measurement/zh/015.png)

### 限制与前提条件

- 设备须在线且空闲，离线、连接中或正在执行其他任务时无法启用该功能；
- 设备须插入**安全钥匙**，否则 suite 会提示并阻止进入流程；
- 若该功能已被其他项目占用，需先结束占用项目的操作。

## 手拖工具头曲面测量

曲面加工前，可手拖工具头标记待扫描区域，设备将对该区域进行曲面扫描，生成高度图和可加工区域预览。

与框选曲面测量不同的是，手拖曲面测量不强求先完成曲面拍照，进入流程时仅校验设备状态与能力，但仍建议保持设备就绪状态，且正确放置材料。

![016.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/toolhead-drag-measurement/zh/016.png)

### 适用场景

- 加工曲面材料（如弧形木板、不规则凹凸面），需要获取表面高度信息；
- 工具头摄像头故障，难以框选边界；

### 操作步骤

1. 进入“准备”页面，在右侧“模式”中选择“曲面加工”模式；

![017.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/toolhead-drag-measurement/zh/017.png)

2. 在上方工具栏中点击“测量”图标，选择“工具头拖动测量”；

![018.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/toolhead-drag-measurement/zh/018.png)

3. 根据页面提示，手拖工具头并打点标记区域；

> 注意：需标记两个不在同一水平线上的点以生成矩形测量区；

|  |  |
| --- | --- |
| 019.png | 020.png |

4. suite 和屏幕将实时显示已标记点数、当前工具头坐标、区域预览；标记完成后，在 suite 或屏幕点击“完成”；

|  |  |
| --- | --- |
| 021.png | 022.png |

5. 设备开始进行曲面扫描，扫描过程中会显示进度条；

![023.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/toolhead-drag-measurement/zh/023.png)

6. 扫描结束后，suite 自动生成点云、更新背景纹理，并计算可加工区域，可继续摆放对象并发起加工。

![024.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/toolhead-drag-measurement/zh/024.png)

### 限制与前提条件

- 该功能属于曲面测量流程，须在**曲面加工模式**下使用；
- 设备须**插入安全钥匙**，否则 Suite 会提示并阻止进入流程；
- 若设备已装载旋转轴组件，则无法使用手拖曲面测量功能，**须先拆卸旋转轴组件**；
- 设备须在线且满足曲面测量前置条件（如激光垫板已放置、上盖关闭等，具体以 suite 弹窗提示为准）；
- 确认选区后设备进入测量态，此时**请勿移动材料或打开上盖**，等待扫描完成；
- 为减少俯视偏差，**测量区域框的面积需略大于待加工图案**，并尽量覆盖材料最高点附近。

## 手拖工具头圆柱测长

当需要手动测量圆柱体长度时，可手拖工具头进行选点，机器将自动测量。

### 适用场景

需要单独测量圆柱体长度时。

### 操作步骤

- 点击“手拖工具头长度测量”;

![revolve-measure.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/rotary-attachment-guide/zh/revolve-measure.png)

- 手拖工具头依次选中两个点：物体起始点和结束点；

> 注意：起始点和结束点均需对准杯子的边缘位置，才能获得准确的展开图。

![061.webp](https://public-cdn.bblmw.com/wiki/new/r1/manual/rotary-attachment-guide/en/061.webp)

- 机器会自动测量出选中的长度，确认后将自动填写至 suite 中；

![060.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/rotary-attachment-guide/zh/060.png)

## 常见问题与解决方案

1. **手拖测距失败**

**解决方案：** 确认工具头位于可测量区域内、材料未移动、未装载旋转组件；移动到平整位置后重试。

2. **矩形选区生成异常**

**解决方案：** 检查两个标记点是否落在同一水平线上；矩形模式要求**两点不在同一水平线**。

|  |  |
| --- | --- |
| 025.png | 026.png |

3. **找不到“手动选择加工区域”或“手拖工具头选区测量”入口**

**解决方案：** 当前机型或固件版本可能不支持手拖能力；请确认连接的是 R1 打印机且固件为最新版本。

4. **点击后提示须插入安全钥匙**

**解决方案：** 手拖选区与手拖曲面测量均须插入安全钥匙后重试。

![027.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/toolhead-drag-measurement/zh/027.png)

5. **曲面手拖测量点击“完成”后无进度**

**解决方案：** 设备须先完成选区并进入测量态后才会显示进度条；确认已打满所需点数且设备状态正常。

6. **设备端已结束操作，suite 仍停留在手拖界面**

**解决方案：** 在 suite 手动点击“取消”退出；建议在设备端和 suite 两端保持操作同步。

7. **手拖工具头加工误差较大**

**解决方案：** 将设备升级至最新固件后重试。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
