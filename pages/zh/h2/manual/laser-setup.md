---
path: zh/h2/manual/laser-setup
title: "激光模组主要部件和工作流程介绍"
description: ""
tags: []
created: 2025-03-25T11:23:10.349Z
updated: 2026-02-02T08:17:00.706Z
source: https://wiki.bambulab.com/zh/h2/manual/laser-setup
---

## 开始之前

### 免责声明

请仔细阅读包装箱中的免责声明

### 安全宣导

a.阅读手册和安全声明

b.正确组装机器并通风排烟

c.设置正确的工作参数

d.加工时需要有人值守，紧急情况立即按下急停按键以切断电源

e.在机器旁放置灭火装置

f. 每次激光加工后都需进行清洁，并定期进行常规保养维护

### 激光安全教学

[激光模组使用安全指引](imp-info-laser.md)

## 软件与固件

需要提前下载Bambu Suite，打印机固件需升级到最新版本。

## 激光模组介绍和组装

### 激光模块介绍

![](https://wiki.bambulab.com/h2/manual/laser-setup/img_v3_02hl_cb9423d1-119a-4909-ac7e-0e5996e106bg.jpg)

### 激光模组安装步骤

急停按键、排烟管等详细安装过程可以参考视频： [激光模组安装指南](laser-module-lnstallation-guide.md)

1. 从包装箱中取出激光模组后，参考以下步骤安装：

   A. 按压工具头透明前面盖上方的2个角，使其与工具头分离并将其移。

![](https://wiki.bambulab.com/h2/manual/laser-setup/image-7.png)

B. 确保激光模组的快拆锁扣处于解锁状态，然后对准激光模组和工具头的滑槽，从上往下将激光模组滑入到底。

![](https://wiki.bambulab.com/h2/manual/laser-setup/image.png)

C. 确保激光模组的"Click"标识对齐工具头的刻度线，然后向下锁紧快拆锁扣，如下图所示。

![](https://wiki.bambulab.com/h2/manual/laser-setup/image-1.png)

D. 打开工具头扩展接口处的防尘塞，将激光模组连接线插入接口。

![](https://wiki.bambulab.com/h2/manual/laser-setup/image-2.png)

E. 取下上盖玻璃。从配件盒中取出黑色气管，两端分别连接激光模组和缓冲器中间的气管接头，插入后轻拉气管不脱出即为连接到位。将气管中间段卡入拖链上方的理线卡位，然后整理气管确保各个位置没有过度弯折。最后，将上盖玻璃放回原位。

- 如果未使用激光模块，请取下气管，让拖链自由移动。

![](https://wiki.bambulab.com/h2/manual/laser-setup/image-3.png)

### 激光垫板使用说明

当你安装上激光模组后，需要在热床上放置激光垫板来配合激光模块进行加工制作。关于激光垫板的使用说明，可以参考wiki了解更多：[激光垫板和刀切垫板的使用介绍](laser-platform-cutting-platform-use-intro.md)

## 初始化和校准

在使用机器的激光模块加工之前，需要从“助手”中找到激光模组校准的提示。该提示通常包括“激光模组初始化”、“激光模组挂载校准”和“俯视相机初始化”。

### 激光模组初始化

**首次安装使用激光模组的时候，需要运行一次初始化，之后就无需再执行该过程。如果更换了另一个激光模组，则需要重新初始化。该过程会校准激光焦点的位置和激光焦距，并使得机器进入绝对位置模式**。**该步骤需要在热床上放置激光平台和耗材（校准卡），如下图所示。**关于激光焦点标定可以参考wiki了解更多：[**激光焦点标定wiki**](laser-focus-calibration-intro.md)

![](https://wiki.bambulab.com/h2/manual/laser-setup/img_v3_02ho_1248118a-007b-445b-91a1-138140d8f89g.jpg)

### 激光模组挂载校准

**每次机器重新上电、电机重新上电、电机丢步等情况发生后，如果想要使用激光模组，则需要重新校准一次。需要校准时该校准会在Assistant页面自动弹出，无需用户自行判断。**该校准的主要目的是回中激光模组，确定激光模组和热床的相对位置。**该步骤需要提前在热床上放置激光垫板，如下图所示。**

![](https://wiki.bambulab.com/h2/manual/laser-setup/image-4.png)

### 俯视相机初始化

俯视相机初始化用于校准俯视相机，以提高其拍照转正的精度。**该校准需要配合热床上的四个marker来实现，所以该步骤热床上不需要放任何东西，需要把热床上的marker暴露给俯视相机。**俯视相机出厂时已经经过校准，用户到手可以直接使用。但是由于运输、长期使用等原因，俯视相机的校准参数可能会逐渐失效。当您对激光加工精度不满意时，可以在“设置”-“工具箱”中触发俯视相机初始化，从而再次对俯视相机进行校准。

![](https://wiki.bambulab.com/h2/manual/laser-setup/am400483.jpg)

## 开始激光雕刻作业

1. 连接机器。Bambu Handy扫描绑定打印机，PC端打开Bambu Suite并登录账号（ [Bambu Suite制作套装软件操作手册](../../software/bambu-suite/manual/quick-start-guide.md)）。
2. 在Bambu Suite的画布中，导入想要加工的图片，并为其选择特定的工艺（ [2D制作工艺介绍](../../software/bambu-suite/manual/2d-processing-type-intro.md)）。
3. 确保在机器的热床上放置好激光垫板和需要加工的材料（ [激光任务前摆放材料](placement-of-laser-materials.md)），点击准备进入准备页面，在软件最右侧的“材料组”选择要加工的材料。然后点击“拍照”，几秒钟后获取加工的背景图，在加工背景上调整图案至所需位置，确认无误后再点击“制作”发送任务。

| **放置好激光垫板和加工的材料** | **在Bambu Suite中获取加工背景并将调整图案位置，发送任务** |
| --- | --- |
| img_v3_02ho_7149b202-d7f9-4b88-980f-321053b8077g.jpg | 01.gif |

如果您先在材料组中选择了材料，再点击“拍照”，则相机获取加工背景图的时候，会顺便测量材料厚度。如果您需要单独测量材料厚度，也可以在“材料组”——“厚度”中点击“测量”来重新测量所放置材料的厚度，关于测量厚度的解释可以参考wiki了解更多： [材料厚度测量](../../software/bambu-suite/manual/material-thickness-measurement.md)。

![](https://wiki.bambulab.com/h2/manual/laser-setup/1.gif)

- 确保打印机的顶盖还有前门都是关闭的。发送任务后，需要点击打印机屏幕上的“开始”按钮或者按住打印机上方的物理按钮（约1秒钟）进一步确认，即可开始激光雕刻任务。

![](https://wiki.bambulab.com/h2/manual/laser-setup/image-5.png)

![](https://wiki.bambulab.com/h2/manual/laser-setup/image-6.png)

- 注意：激光生产可能存在火灾等安全隐患。**在生产过程中，请不要走开，不要让打印机无人看管。**

## 每次任务后的清洁

每个项目结束后清理工作区域的碎屑和灰尘，以降低火灾和有害颗粒物的风险。

视频待补充

## 定期常规保养维护

烟雾会在机器内部积聚，导致效率降低、性能下降和潜在损坏，请定期根据设备的维护提示进行常规保养和维护。

文档正在建设中，敬请期待。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南并未解决您的问题，[*请点击此处联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
