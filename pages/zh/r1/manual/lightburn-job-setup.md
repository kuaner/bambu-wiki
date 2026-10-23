---
path: zh/r1/manual/lightburn-job-setup
title: "R1 通过 LightBurn 切片发起加工任务"
description: ""
tags: []
created: 2026-10-22T09:47:37.192Z
updated: 2026-10-22T11:51:00.274Z
source: https://wiki.bambulab.com/zh/r1/manual/lightburn-job-setup
---

## 免责声明与注意事项

- LightBurn 是第三方软件，不对因使用 LightBurn 造成的任何损失负责；
- LightBurn 仅支持 R1 完成**平面加工**，并不完全支持 R1 的所有功能。例如：**精细拍照、标定加工区域、曲面加工，旋转体加工**等功能均不支持。如需体验全部功能，请使用拓竹官方软件 Bambu Suite（[点击下载](https://bambulab.cn/zh-cn/download/suite)）。

## 第一步：下载并安装 LightBurn

前往 LightBurn 官网下载最新版本并安装（新用户有 30 天免费试用）<https://lightburnsoftware.com/>

> 请确保使用**最新版本**且**已授权**的 LightBurn。若使用旧版本或破解/盗版软件，发起任务可能失败。

![R1 LightBurn 下载与安装页面](https://wiki.bambulab.com/r1/manual/lightburn-job-setup/r1-lightburn-download-install-zh.jpeg)

## 第二步：导入 R1 设备配置

1. 点击[下载 R1 配置文件](https://wiki.bambulab.com/r1/manual/lightburn-job-setup/Bambu_Lab_R1_01.04.00.45%201.lbvendor)
2. 打开 LightBurn，在软件**右下角**的 **Laser（激光器）** 面板中点击 **Devices（设备）**。

![在 LightBurn 中打开 R1 设备面板](https://wiki.bambulab.com/r1/manual/lightburn-job-setup/r1-lightburn-devices-panel-zh.png)

3. 在 Devices 窗口中，点击 **Import（导入）**，导入 R1 配置文件 Bambu\_R1\_01.04.00.45.lbzip 。

|  |  |
| --- | --- |
| 在 LightBurn 中导入 R1 设备配置文件 | R1 设备配置文件导入窗口 |

4. 导入成功后，会显示对应的设备信息。在 LightBurn 显示出 R1 设备则说明连接成功。

![LightBurn 成功识别 R1 设备](https://wiki.bambulab.com/r1/manual/lightburn-job-setup/r1-lightburn-r1-device-detected-zh.jpeg)

## 第三步：导出 Lightburn 切片 gcode

### 1. 选择并放置材料

打开 R1 盖子，将待加工材料放在底板上（可加工材料及加工步骤等注意事项，请参考 Wiki：[R1 平面加工指南](plane-machining-guide.md)）

### 2. 设计加工图形

使用左侧工具栏，在画布上设计加工图案

![在 LightBurn 中设计 R1 加工图形](https://wiki.bambulab.com/r1/manual/lightburn-job-setup/r1-lightburn-design-processing-graphics-zh.jpeg)

### 3. 设置加工参数

在 **Cuts / Layers（图层）** 面板中双击某个图层打开设置窗口，根据材料特性和加工需求为每个图层设置合适的参数；

![在 LightBurn 中设置 Cuts Layers 加工参数](https://wiki.bambulab.com/r1/manual/lightburn-job-setup/r1-lightburn-cuts-layers-settings-zh.jpeg)

设置支撑厚度和材料厚度，以获取实际的加工高度。有两种填写方式，可以根据材料厚度填写（方法一），也可以通过 Bambu Suite 的测量值填写（方法二）。设置位置如下图所示。

![在 Bambu Suite 中测量 R1 材料高度](https://wiki.bambulab.com/r1/manual/lightburn-job-setup/r1-suite-measure-material-height-zh.jpg)

- 方法一，根据基准平面填写，如使用 3mm 木板，则 **Support** 列填 `44`（固定值），**Material** 列填 `3`（材料厚度）。

| 材料放置位置 | Support | Material |
| --- | --- | --- |
| 整机刀条 | 44 | 3 |

- 方法二，通过 Bambu Suite 获取测量值。（**推荐，精度更为可靠**）  
  用 **`79.73 - 测量值`**。如下图所示，测量结果为 `32.54`，则实际 Z 高度为`79.73-32.54 = 47.19`。则 **Support** 列填 `47.19`，**Material** 列填 `0`。

> **注**：79.73 为固定值，当材料距离超过 79.73 mm 时，软件会判定为测量异常。详细说明请查看 [R1 材料距离测量](material-thickness-measurement.md)。

| 材料放置位置 | Support | Material |
| --- | --- | --- |
| 其他位置 | 47.19 | 0 |

![设置 R1 LightBurn 任务的支撑和材料高度](https://wiki.bambulab.com/r1/manual/lightburn-job-setup/r1-lightburn-material-height-settings-zh.jpeg)

### 4. 导出 gcode

- 在软件**右下角**的 **Laser（激光器）** 面板中点击 **Save GCode**。

![在 LightBurn 中保存 R1 GCode](https://wiki.bambulab.com/r1/manual/lightburn-job-setup/r1-lightburn-save-gcode-zh.jpeg)

> **注**：由于不支持旋转体加工，在导出 gcode 前请确认已经关闭旋转体加工。

- 打开 Rotary Setup 窗口，关闭 **Enable Rotary**，点击 **OK**。

![导出 R1 GCode 前关闭旋转体设置](https://wiki.bambulab.com/r1/manual/lightburn-job-setup/r1-lightburn-disable-rotary-setup-zh.jpeg)

---

## 第四步：在 Bambu Suite 中发起加工

### 1. 下载并打开 Bambu Suite

- 点击链接[下载 Bambu Suite](https://bambulab.cn/zh-cn/download/suite)；
- 在 Suite 中连接设备。

### 2. 导入 gcode

- 连接成功后打开：**文件 > 导入 > 发送打印文件**；

![在 Bambu Suite 中导入发送打印文件](https://wiki.bambulab.com/r1/manual/lightburn-job-setup/r1-suite-import-send-print-file-zh.jpeg)

- 将 LightBurn 切片导出的文件拖入选框中；

![将 LightBurn GCode 拖入 Bambu Suite](https://wiki.bambulab.com/r1/manual/lightburn-job-setup/r1-suite-drag-lightburn-gcode-zh.jpeg)

### 3. 发起加工

- 合上 R1 盖子，点击设备按钮，开始加工。

**参考资料**：

- [LightBurn 视频教程](https://lightburnsoftware.com/pages/tutorials)
- [LightBurn 文档](https://docs.lightburnsoftware.com/index.html)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
