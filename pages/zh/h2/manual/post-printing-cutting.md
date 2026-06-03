---
path: zh/h2/manual/post-printing-cutting
title: "H2D 打印后刀切功能指南"
description: ""
tags: []
created: 2025-04-29T13:21:46.596Z
updated: 2026-03-31T07:14:20.871Z
source: https://wiki.bambulab.com/zh/h2/manual/post-printing-cutting
---

> **注意**：本页面以 H2D 机器为例。**H2S 和 H2C 的操作步骤完全相同**。

## 1. 功能介绍

打印后刀切（Print Then Cut） 是 H2D 打印机的一项智能功能，允许用户先在普通纸张上打印彩色图案，再通过挂载的刀切模组沿图案轮廓精准切割，高精度实现贴纸、标签、贺卡等作品制作。

**核心优势：**

- **多色作品制作：**可打印复杂彩色设计后切割，适用于贴纸、装饰品制作；
- **精准对齐切割：**打印图案与切割路径自动对齐；
- **兼容多种材料：**支持不干胶贴纸、卡纸等薄型材料。

## 2. 操作流程

### **步骤 1：设计图案**

1. 在 Bambu Suite 中导入/绘制 2D 图案（可以是位图或者矢量图）。
2. 调整图案尺寸，以及对图案进行其他编辑处理，例如去除背景等。

![](https://wiki.bambulab.com/h2/post-printing-cutting/%E4%BD%8D%E5%9B%BE%E5%8E%BB%E8%83%8C%E6%99%AF.gif)

### **步骤 2：设置打印后刀切工艺类型**

将图案的**工艺类型修改为打印后刀切**。如果你使用了贴纸工具，则**软件会自动将贴纸图案设置为打印后刀切的制作工艺，**详情可以参考：[贴纸工具](../../software/bambu-suite/manual/sticker-tool.md)

![](https://wiki.bambulab.com/h2/post-printing-cutting/20250424151930_rec_.gif)

### **步骤 3：选择材料，发送加工和打印任务**

1. 在材料组选择合适的材料，例如制作贴纸时选择不干胶打印纸。

![1280x1280.png](https://wiki.bambulab.com/h2/manual/1280x1280.png)

2. 点击“制作”，发送任务。在这一步总共会发送两个任务，一个是发送加工任务给 3D 打印机，另一个是发送 2D 打印任务给纸质打印机**（需确保电脑已经成功连上纸质打印机）**。

![](https://wiki.bambulab.com/h2/post-printing-cutting/%E6%B7%BB%E5%8A%A0%E8%B4%B4%E7%BA%B8%E8%BE%B9%E6%A1%86.gif)

> **重要提醒！**  
> 使用 2D 打印机时，请务必将比例设置为 **100%（实际尺寸）**。  
> 打印前，请检查 2D 打印机的**默认设置**，确保关闭“适应页面”或“缩放以适应”等选项，避免因比例被自动调整而导致后续刀切任务出现尺寸误差或位置偏差。

### **步骤 4：开始制作**

参考软件和屏幕上的说明，将打印出来的纸张贴在垫板的对应位置，然后在机器上按住按钮启动任务，即可开始。

![20250617-140848.jpg](https://wiki.bambulab.com/h2/manual/20250617-140848.jpg)

![](https://wiki.bambulab.com/h2/post-printing-cutting/image-1.png)

![](https://wiki.bambulab.com/h2/post-printing-cutting/img_v3_02hv_aeea2915-700b-47c4-b752-4ffd1313225g.jpg)

![](https://wiki.bambulab.com/h2/post-printing-cutting/image-2.png)

## 3. **操作规范**

### 2D 打印注意事项

使用 2D 工艺打印图案时，**请避免进行任何缩放设置**。由于切割路径已在 G-code 中预设，图案缩放会导致切割轨迹与外轮廓错位，无法实现精准切割，易造成打印后刀切发生偏位。

### 材料粘贴规范

在打印后刀切作业中，需通过工具头摄像头识别纸张上的 **4 个定位标记（Marker）** 来确定切割位置。在发送2D打印任务时，会在图案的四周自动生成这4个 marker 并打印出来。

![](https://wiki.bambulab.com/h2/post-printing-cutting/image-3.png)

- **标记功能**：

  - 4 个 Marker 用于精确定位图案位置，才可以确保设备能够精准沿着图案轮廓切割。
  - 其中左上角的 Marker 旁有 **"向上箭头"**，代表纸张需按此方向粘贴。

  ![](https://wiki.bambulab.com/h2/post-printing-cutting/image-4.png)
- **操作要求**：

  - **用户需要将打印出图案的纸沿着第二条虚线框的左上角位置贴好，**如下图所示：

  ![](https://wiki.bambulab.com/h2/post-printing-cutting/image-5.png)

  ![](https://wiki.bambulab.com/h2/post-printing-cutting/image-6.png)

  ![](https://wiki.bambulab.com/h2/post-printing-cutting/image-7.png)
- **注意事项：**

  - 若摄像头无法识别全部 4 个 Marker，加工作业将被终止；
  - 当前摄像头识别范围有限，纸张粘贴位置偏移超过一定距离可能导致识别失败。**注：对于XY方向贴纸允许的最大偏差，x允许±10mm，Y允许±5mm。我们争取在未来版本固件中优化，允许在更大范围内搜索定位标识。**

### 出血框设置

#### **什么是出血框？**

出血框是设计时在图案边缘**额外扩展的区域**，**用于补偿纸质打印机打印图案时出现的的微小尺寸偏差，**确保切割后图案边缘完整无白边。

#### **如何设置出血框**

您可以在发送2D打印任务的窗口，启用**出血框，**即可进行出血框设置。**启用后图案四周各会扩展0.15mm左右。**

![](https://wiki.bambulab.com/h2/post-printing-cutting/image-8.png)

### 手眼标定注意事项

#### **为什么需要手眼标定？**

因为模切刀头是可拆装，在拆装过程中可能导致刀头机械位置偏移，需通过标定消除其在XY方向上的误差差，确保加工的时候能准确定位。

#### **标定流程**

在正式加工任务开始前，切刀自动在材料左下角 Marker 附近切割 **一横一竖两道参考线**，然后工具头摄像头扫描参考线位置，计算刀头实际偏移量，存储数据用于后续加工。

![20251128-111342.jpg](https://wiki.bambulab.com/h2/manual/post-printing-cutting/20251128-111342.jpg)

#### **关键参数说明**

##### 切割标定线的刀压

- 使用官方材料：为了保证能切出这两道参考线，切割使用的是**当前所选材料的内置刀压，用户是无法更改的。**
- 使用自定义材料：由于自定义材料没有内置的刀压，所以切割参考线时会参考用户设置的**切穿刀压。若未设置切穿刀压，或者设置的切穿刀压小于普通切割刀压，则扔会采用切割刀压来切割标定线（注：只有在Bambu suite 进入专家模式后才会显示切穿刀压参数）。**

![](https://wiki.bambulab.com/h2/post-printing-cutting/image-10.png)

![](https://wiki.bambulab.com/h2/post-printing-cutting/image-11.png)

##### **常见标定失败原因**

- **参考线未切透：**

  - 自定义材料的切穿刀压设置不足，可适当增加刀压；
  - 刀头磨损严重，检查确认后可更换新刀头。
- **参考线超出加工材料的区域：**

  在Bambu Suite的准备页面中，默认打印后刀切使用的是A4纸，而且图案只能摆放在红框内（如下左图所示），这样就能确保实际切割的时候能预留出足够的切割参考线位置。

  若使用非A4纸（尺寸更小的纸），实际图案摆放位置可能太靠近边缘，导致右下角 Marker 旁没有足够预留位置，实际切割参考线的时候会超出纸张区域，导致参考线切割在垫板上导致无法被摄像头识别。

![](https://wiki.bambulab.com/h2/post-printing-cutting/image-12.png)

![Marker旁预留的切割空间不足](https://wiki.bambulab.com/h2/post-printing-cutting/image-13.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南未解决您的问题，[*请联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
