---
path: zh/x1/manual/using-a-large-spool-on-the-spool-holder
title: "如何在料盘支架上使用更大的料盘"
description: "打印时，在背面的料盘支架上使用更大更宽的料盘"
tags: ["料盘"]
created: 2023-03-22T06:58:18.801Z
updated: 2025-07-24T09:34:52.578Z
source: https://wiki.bambulab.com/zh/x1/manual/using-a-large-spool-on-the-spool-holder
---

若你的料盘不能平放在位于打印机后部后面的料盘支架上，有下面的这几个方法可以解决这个问题。

1. 拆除缓冲器

2. 使用外部料盘支架或除湿盒

3. 打印您自己的料盘支架

## 一、拆除缓冲器指南

这一步适用于将大尺寸耗材料盘与 AMS（自动供料系统）一起使用的情况。大的料盘通常拥有较大的直径，在运行过程中可能会与耗材缓冲器产生冲突。如果您使用的是外挂大料盘，可能会由于空间限制而导致安装困难；因此建议暂时移除耗材缓冲器，以避免在大料盘使用时产生阻碍。若您未使用 AMS 自动供料系统，则不会需要安装耗材缓冲器，可以安全地跳过此步骤。

> **注意：在进行拆除动作之前，请先提前断电，注意安全。**

### 第1步：拆开蓝色的气管接头

按下蓝色气管接头连接处，取出铁氟龙料管（PTFE 管）。

![](https://wiki.bambulab.com/x1/manual/using-a-large-spool/large-spool-step1.jpg)

### 第2步：拆除总线电缆

分别拆除连接到打印机后面的4针电缆，以及连接到 AMS 的6针电缆。

![](https://wiki.bambulab.com/x1/manual/using-a-large-spool/拔出电源连接线.png)

### 第3步：拆除缓冲器

拧开固定缓冲器的两颗螺丝。

![](https://wiki.bambulab.com/x1/manual/using-a-large-spool/large-spool-step3a.jpg)

### 第4步：从缓冲器中取出 AMS PTFE 管

按住位于缓冲器中的黑色气动接头，取出 AMS PTFE 管。

> 注意：您可以选择使用官方提供的内六角扳手，压住气动接头。下图中使用的是镊子。

![](https://wiki.bambulab.com/x1/manual/using-a-large-spool/large-spool-step4.jpg)

### 第5步：尝试挂上料盘

请将取出的 AMS PTFE 管妥善存放起来。目前，您设备的的 PTFE 管入口应该处于如下图中的未接入状态，且缓冲器也被拆除了，应有足够的空间可以使用大料盘。您可以再次尝试挂上大料盘。

![](https://wiki.bambulab.com/x1/manual/using-a-large-spool/空闲状态1.jpg)

## 二、使用外部料盘支架或除湿盒

### 安装好外部料盘支架或除湿盒

- 1. 安装外部料盘支架。

![](https://wiki.bambulab.com/x1/manual/using-a-large-spool/自带料盘架.png)

- 2. 若上图中原装的料盘架不符合实际应用的尺寸需求，您可以参考 MakerWorld 上的相关模型资讯。如搜索关键字**“ X1 外部料盘支架”**来选择并下载打印适合的模型。请选择适合的外部料盘支架，并安装好。另外，如果您需要自行设计或者下载料盘支架还可参考下一个章节中的链接。

> 注意：对于料盘过大的、却又需要干燥的耗材，您也可以考虑参考[装密封盒](../../filament-acc/acc/sealed-box.md)自制一个适合大小的除湿盒。若您对所选择的耗材是否需要除湿盒存疑，也可以参考这个网站进行耗材的对比选择：[选择合适的耗材 - Bambu Lab 打印机 3D 耗材丝指南](https://bambulab.cn/zh-cn/filament-guide)

## 三、打印属于自己的料盘支架

MakerWorld 上有很多优秀的模型组件可以参考，比如适配 A1 的支架：来自 **@TheMechanic** 创作的 [Bambu Lab A1 料盘支架](https://makerworld.com.cn/zh/models/523150-bambuliao-pan-zhi-jia-zhuo-mian-zhi-jia-a1#profileId-450043)

还有适配 X1 和 P1 的支架：来自 @**Mdesign** 设计的 [P1S、X1C 侧面料卷支架](https://makerworld.com.cn/zh/models/127016-p1s-x1cce-mian-liao-juan-zhi-jia?from=search#profileId-14210)

您可以根据自己的需求打印出最适配您目前实际应用场景中机器的料盘支架。

![](https://wiki.bambulab.com/x1/manual/using-a-large-spool/x1外挂料盘支架.jpg)

图片及模型来自@Mdesign

> 注意：本文中引用的模型版权归原作者所有，仅用于学习与交流。如有侵权，请联系删除。

## 四、设置及检验

### 第1步：在 Bambu Studio 中设置外接耗材参数

从版本 1.9.1.0 起，Bambu Studio 不仅支持内置的**系统耗材**配置文件，还支持创建和自定义**第三方耗材**配置文件，这些被称为“自建耗材”（详见下方图示中的步骤 三）。

对于大多数打印需求，用户只需选择一个通用耗材配置文件即可。这些配置文件兼容多种材料，通常可以正常使用，无需额外调整。

然而，如果您希望针对特定耗材进一步优化打印质量，例如调整打印温度、流速或冷却设置，也可以创建并管理专属于该材料的自定义配置文件。

这些自定义设置将同步至您的打印机和移动应用，确保在多个平台之间保持一致性。

![新功能6.png](https://wiki.bambulab.com/p1/manual/firmware-history/%E6%96%B0%E5%8A%9F%E8%83%BD6.png)

在 Bambu Studio 内除了在**预览**界面处设置耗材外，还需要在**设备**界面处进行外接耗材的设置，具体步骤可按照下图中1,2,3的顺序进行操作设置。

![](https://wiki.bambulab.com/x1/manual/using-a-large-spool/bambustudio设置.png)

若您想要了解更多关于耗材丝的参数设置可参阅：[切片参数设置指南](../../software/bambu-studio/how-to-set-slicing-parameters.md)

### 第2步：配置参数以及进料

接下来请按照视频步骤指引配置耗材参数，并在设备上点击进料。

### 第3步：尝试发起打印并验证外接料盘支架是否能够正常使用

可以在 Bambu Studio 中导入想要打印的模型，修改打印参数后点击切片单盘，再点击打印单盘即可将打印任务发送给打印机。

又或者在打印机中自带的模型库中选取一个进行打印测试。发起打印的具体操作可以参考如下链接：[从 Bambu Studio 开始打印](print-from-bambu-studio.md)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/cn/im?from=5)，我们随时准备为您解答疑问并提供帮助。
>
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
