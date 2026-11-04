---
path: zh/h3c/maintenance/replace-heatbed-assembly
title: "热床组件更换指南"
description: ""
tags: []
created: 2026-11-03T12:41:54.616Z
updated: 2026-11-03T12:41:55.672Z
source: https://wiki.bambulab.com/zh/h3c/maintenance/replace-heatbed-assembly
---

## 热床组件

打印机的热床是安装在打印机腔体内，能沿 Z 方向上下运动并能根据用户的设定温度进行加热的平台。设置合适的热床温度能有效提升模型与打印板的粘接力和防止模型翘边。  
![img_fa7401ecaf3e.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-heatbed-assembly/zh/img_fa7401ecaf3e.jpg)

## 何时更换

- 热床不升温， 且已排查过，确认热床故障；
- 影响功能的物理损坏或明显的形变；
- 经过 Bambu Lab 官方确认需要更换热床。

## 工具和材料

- H2.0 内六角扳手
- H1.5 内六角扳手

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> ![img_01457bbe50f0.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-heatbed-assembly/zh/img_01457bbe50f0.jpg)

> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 移除热床组件

### 第 1 步 下降热床并锁定

启动打印机，执行一次回 XYZ 回零操作，然后在屏幕上点击下降热床的图标，将热床下降到底部。  
![img_4bdc3e292d25.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-heatbed-assembly/zh/img_4bdc3e292d25.jpg)

请根据实际作业场景，选择对应的热床滑块固定方式（选做）：

> 使用螺丝固定滑块的作用：后续锁紧热床螺丝时，保证三个滑块高度一致。操作时若足够细心，即便不用螺丝固定滑块，三只Z轴滑块理论上也可保持齐平。

**方式一：利用原厂开箱固定件螺丝（适用于仅拆装热床、无新配件更换的场景）**

- **操作说明**：下载并打印**专用模型**，搭配**开箱时从固定支架上拆下的 4 颗螺丝**进行固定。

|  |  |
| --- | --- |
| img_5ee9fbf07847.jpg | img_4197bb5d48e5.jpg |

**方式二：利用新配件赠送螺丝（适用于更换热床配件的场景）**

> **部分批次缺少4颗专用螺丝：按方法一打印模型，使用开箱拆除的4颗螺丝。**

- **操作说明**：直接使用热床配件附送的螺丝对滑块进行锁定。

### 第 2 步 移除 背板

请参考 WIKI：[背板更换指南](replace-back-panel.md)，断开电源线并将背板移除。  
![img_9284139891bb.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-heatbed-assembly/zh/img_9284139891bb.jpg)

### 第 2 步 断开线缆

从 MC 板上断开两根连接线缆（RGB状态指示灯插头和热床NTC&喷嘴偏移校准传感器二合一插头）；从 AC 板上断开 3 根快速连接端子线缆。  
![img_5783abeb3b6d.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-heatbed-assembly/zh/img_5783abeb3b6d.jpg)

用 H2.0 内六角扳手移除 1 颗地线螺丝，松出地线；移除内侧的 1 颗线夹螺丝，将热床线缆从线夹中松出。  
![img_9c5a6dabdb85.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-heatbed-assembly/zh/img_9c5a6dabdb85.jpg)

将热床线缆从后滑块线扣上松出。  
![img_314ffe44c335.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-heatbed-assembly/zh/img_314ffe44c335.jpg)

### 第 3 步 移除热床

热床与 3 个滑块共有 6 颗螺丝固定，先移除位置 1 处的 2 颗螺丝，然后揭开位置 2 和位置 3 处的硅胶条，移除 两处共 4 颗螺丝。

![img_495155601d45.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-heatbed-assembly/zh/img_495155601d45.jpg)

> **注意：请提前给 H2.0 内六角扳手上磁，方便在螺丝拧松后直接带出。**  
> ![img_6acebd097606.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-heatbed-assembly/zh/img_6acebd097606.jpg)

将热床线缆往打印机腔室方向回收，倾斜热床，从打印机前门位置将热床取出。  
![img_6c072fbb9186.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-heatbed-assembly/zh/img_6c072fbb9186.jpg)

## 安装热床组件

### 第 1 步 安装热床

将热床线缆从后光轴左侧穿到打印机背面，并将热床放置到 3 个滑块上。  
![img_5eb0695e3671.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-heatbed-assembly/zh/img_5eb0695e3671.jpg)

\*\*后滑块：\*\*对齐螺丝孔，预锁 2 颗螺丝。  
![img_7cabbbb724c8.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-heatbed-assembly/zh/img_7cabbbb724c8.jpg)

\*\*左右滑块：\*\*确认左右两侧的定位柱都位于两个螺丝孔中间，然后各预锁入 2 PCS 螺丝。  
![img_9a2be1e41914.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-heatbed-assembly/zh/img_9a2be1e41914.jpg)

然后将 3 个滑块上固定热床的的 6 颗螺丝都进行拧紧。固定热床后，可以移除固定滑块的 4 颗螺丝（和打印模型）。  
![img_6bdbb6909a12.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-heatbed-assembly/zh/img_6bdbb6909a12.jpg)

### 第 2 步 连接线缆

先将热床线缆从压入后滑块的卡扣处。  
![img_eed885ceb8f5.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-heatbed-assembly/zh/img_eed885ceb8f5.jpg)

再将热床线缆及地线卡进右后立柱的线卡中，锁入 1 颗螺丝固定线卡；用地线螺丝（含垫圈）将热床地线锁到立柱上。  
![img_42008c250d2c.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-heatbed-assembly/zh/img_42008c250d2c.jpg)

根据快速连接端子的尺寸，连接到 AC 板对应的插头上。连接MC 板上两根连接线缆插头（RGB状态指示灯插头和热床NTC&喷嘴偏移校准传感器二合一插头）  
![img_d773d6e729a1.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-heatbed-assembly/zh/img_d773d6e729a1.jpg)

## 第 3 步 安装背板

请参考 WIKI：[背板更换指南](replace-back-panel.md)，将背板及其他配件安装好。  
![img_2980526540f2.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-heatbed-assembly/zh/img_2980526540f2.jpg)

> **安装背板提示：请务必检查并确保热床线缆位于左右内衬锁螺丝的位置上方，以防止线缆被锁在下方而导致热床无法正常抬升。**  
> ![img_709dd1f927bd.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-heatbed-assembly/zh/img_709dd1f927bd.jpg)

## 功能验证

连接电源线并启动打印机，设置热床温度为 50 ℃，确认热床温度能升高到目标值。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
