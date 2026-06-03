---
path: zh/x1/manual/multi-color-printing
title: "多色打印操作指导"
description: "介绍如何用Bambu studio、SD卡以及内置模型进行多色打印"
tags: []
created: 2022-09-13T10:07:40.469Z
updated: 2025-12-24T12:18:39.659Z
source: https://wiki.bambulab.com/zh/x1/manual/multi-color-printing
---

#### 提示:由于最大挤出流量的限制，用 0.2mm 喷嘴进行多色打印时，换料的冲刷速度会非常慢，可能需要等待一段时间。

## 给 AMS 上料并配置耗材信息

在使用多色打印功能之前，要给 AMS 上料并配置对应的耗材信息。如果使用的是拓竹官方的耗材，则 AMS 会根据 RFID 自动识别耗材的种类和颜色。如果使用的是第三方耗材，则需要手动给耗材配置对应的信息。具体操作步骤可以参考[AMS的配置和上料步骤](ams-setup-and-filament-loading.md)。

## 在 Bambu studio 里切片并发送打印任务

配置完 AMS 中的信息后，需要在 Bambu Studio 对多色模型进行设置和切片。具体的在 Bambu Studio 上色和参数设置可以参考 [多色打印指南 | Bambu Lab Wiki](../../software/bambu-studio/multi-color-printing.md)。

### 同步耗材信息

将设备页面切换到对应的打印机，点击**同步信息按钮**，同步喷嘴信息和 AMS 数量。  
**请注意，设备页面此时是哪台打印机，同步的就是哪台设备的耗材信息。**

![屏幕截图_2025-09-22_112625.png](https://wiki.bambulab.com/x1/manual/muti-color-print/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE_2025-09-22_112625.png)

点击**继续同步耗材**。

![屏幕截图_2025-09-22_11285888.png](https://wiki.bambulab.com/x1/manual/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE_2025-09-22_11285888.png)

可以看到匹配后的项目与耗材的对应关系。用 Bambu studio 发起打印时，它会先自动映射匹配相同种类最接近颜色的耗材，你可以手动修改它。

![屏幕截图_2025-09-22_180042.png](https://wiki.bambulab.com/x1/manual/muti-color-print/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE_2025-09-22_180042.png)

在发送打印任务前，注意在弹窗页面确认每个颜色选择的槽位是否符合自己预期，如果不符，仍可随时修改。

如果某个槽位信息是“？”，说明使用的是第三方的耗材且尚未配置耗材信息，不过仍然可以选择它进行打印（**注意要确保该槽位的耗材与切片材料种类一致**）。

![屏幕截图_2025-09-22_1133056.png](https://wiki.bambulab.com/x1/manual/muti-color-print/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE_2025-09-22_1133056.png)

## 使用 SD 卡发起打印任务

如果是用 SD 卡发起打印任务，则用 Bambu Studio 切片的时候无需预先选择 AMS 槽位信息，直接切片后导入到 SD 卡中即可。

在打印机上选择 SD 卡中的打印文件后，它会首先自动映射匹配同种类最接近颜色的耗材所在的槽位，如下图所示。

![pipei.jpg](https://wiki.bambulab.com/x1/manual/muti-color-print/pipei.jpg)

如果想修改自动映射，可以在屏幕上手动选择每个颜色对应的槽位。

![pipei2.jpg](https://wiki.bambulab.com/x1/manual/muti-color-print/pipei2.jpg)

如果打印切片时选择的材料和 AMS 上的耗材种类不一致，则无法选择该耗材打印。例如下图：用 PLA 切片的打印文件，可以选择 1/2/4 号槽的 PLA 进行打印，但无法选择 3 号槽的 ABS。

![](https://wiki.bambulab.com/x1/manual/muti-color-print/%E6%9D%90%E6%96%99%E4%B8%8D%E5%90%8C%E4%B8%8D%E5%8F%AF%E9%80%89%E6%8B%A9.png)

## 打印机内置模型

如果是用在内置模型页面发起打印，在正式打印前可在匹配耗材的页面可以选择挤出机耗材的类型。

![20250925-101113z.png](https://wiki.bambulab.com/x1/manual/muti-color-print/20250925-101113z.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南未解决您的问题，[*请联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
