---
path: zh/x1/troubleshooting/how-to-upload-log
title: "如何创建工单及上传日志"
description: "本指南将引导您通过 Bambu Handy 或在 Bambu Lab 官网创建工单及上传日志，以及上传日志常见问题。"
tags: []
created: 2024-10-08T04:14:08.421Z
updated: 2026-06-02T03:11:16.881Z
source: https://wiki.bambulab.com/zh/x1/troubleshooting/how-to-upload-log
---

## 通过 Bambu Handy 提交工单及日志

### 提交工单

打开 Bambu Handy 应用，点击底部导航栏中的 “**我的**”，再选择 “**帮助中心**”，进入帮助中心界面。

在帮助中心页面，找到 “**工单服务**” 区域，点击 “**提工单**”。选择遇到[问题类型](../../create-support-ticket.md)，这里以**打印机**类型为例，点击 “**下一步**” 按钮以进入工单提交页面。

![](https://wiki.bambulab.com/x1/troubleshooting/upload-log-file/3_step_for_handy.jpg)

选择打印机对应的**地区**、[**序列号**](../../general/find-sn.md)、**机型**。若 Bambu Handy 中绑定了对应打印机，可通过点击右侧箭头选择对应打印机，系统将自动填写 SN 号。完成后，点击 “**下一步**” 按钮。

![](https://wiki.bambulab.com/x1/troubleshooting/upload-log-file/4-portrait.png)

在问题描述中添加详细描述，以帮助我们更准确地了解问题；选择问题类型，您可通过点击右侧 “**自动识别**” 按钮，系统将自动识别问题类型并填入。同时，可上传相关图片和视频，上传完成后，点击“**下一步**”。

![](https://wiki.bambulab.com/x1/troubleshooting/upload-log-file/5-portrait.png)

根据提示依次**上传 [打印机日志](#jump5)、HMS 图片、耗材类型** 等附件信息，点击 “**提交**” 即完成工单上传。

![](https://wiki.bambulab.com/x1/troubleshooting/upload-log-file/6-portrait.png)

### 日志上传

点击 “**添加日志**” 后，选择需要上传日志的对应打印机，即可进入日志上传页面。日志上传一共有两种方式，分别是：

- 关联打印历史：选择出现问题时对应的打印记录。
- 手动填写：手动设置日志导出的时间段。

点击 “**确定**” 即可完成日志上传。

![](https://wiki.bambulab.com/x1/troubleshooting/upload-log-file/2_steps_for_handy.jpg)

## 通过 [Bambu Lab 官网](https://bambulab.cn/zh-cn/my/support/tickets)提交工单及日志

### 提交工单

点击服务工单页面右侧 “**创建工单**” 按钮，选择遇到问题类型，这里以**打印机**类型为例，点击以进入工单提交页面。

![](https://wiki.bambulab.com/x1/troubleshooting/upload-log-file/official_web_1.jpg)

选择打印机对应的**地区**、[**序列号**](../../general/find-sn.md)、**机型**。在问题描述中添加详细描述，以帮助我们更准确地了解问题；选择问题类型，您可通过点击 “**自动识别**” 按钮，系统将自动识别问题类型并填入。同时，可上传相关图片和视频及故障发生时间。

![](https://wiki.bambulab.com/x1/troubleshooting/upload-log-file/official_web_2.jpg)

根据提示依次**上传 [打印机日志文件](#jump6)、HMS 图片、耗材类型** 等附件信息，点击 “**提交**” 即完成工单上传。

> **注意**：上传时可全选所有日志文件，系统将自动将其打包成一个文件。

![](https://wiki.bambulab.com/x1/troubleshooting/upload-log-file/official_web_3.jpg)

### 日志导出

您也可先从打印机导出日志到外部存储，再使用电脑，通过官网上传日志。本章节适用于:

[H2 系列打印机](#jump1)  
[P2S 打印机](#jump1)  
[X2D 打印机](#jump1)  
[X1 系列打印机](#jump2)  
[P1 系列打印机](#jump3)  
[A 系列打印机](#jump4)

点击所需机型名字，跳转至对应指南：

#### H2 系列 / P2S / X2D 打印机

1. 点击打印机屏幕进入**设置界面**，选择**导出日志到外部存储**。  
   ![h2d-导出-1.png](https://wiki.bambulab.com/x1/troubleshooting/upload-log-file/h2d-%E5%AF%BC%E5%87%BA-1.png)
2. 点击“导出”。如果遇到的故障类型和 AI 或视觉相关，请务必勾选导出关键图片选项。  
   ![h2d-导出-2.png](https://wiki.bambulab.com/x1/troubleshooting/upload-log-file/h2d-%E5%AF%BC%E5%87%BA-2.png)
3. 导出完成后，取出 U 盘并插入电脑，您会发现一个 **.tar 或者 .tar.gz 文件**，即为刚导出的日志。  
   ![日志文件格式.png](https://wiki.bambulab.com/x1/troubleshooting/upload-log-file/%E6%97%A5%E5%BF%97%E6%96%87%E4%BB%B6%E6%A0%BC%E5%BC%8F.png)

> **注意**：导出打印机日志时请勿更改文件名。

#### X1 系列打印机

1. 将 SD卡（FAT32 格式）插入显示屏组件右侧的 SD卡插槽中。
2. 从打印机屏幕左侧进入**设置**界面，点击**设置**；点击**导出日志到外部存储**。  
   ![x-导出-1.png](https://wiki.bambulab.com/x1/troubleshooting/upload-log-file/x-%E5%AF%BC%E5%87%BA-1.png)
3. 导出日志的同时，也可选择导出关键照片或 G-code 文件。若故障与激光雷达或 AI 相关，请勾选**导出关键照片**。选择完毕后，单击**导出**。该过程将持续几分钟。  
   ![x-导出-2.png](https://wiki.bambulab.com/x1/troubleshooting/upload-log-file/x-%E5%AF%BC%E5%87%BA-2.png)
4. 导出完成后，从显示屏组件插槽中取出 SD 卡并插入电脑，您会发现一个 **.tar 或者 .tar.gz 文件**，即为刚导出的日志。  
   ![日志文件格式.png](https://wiki.bambulab.com/x1/troubleshooting/upload-log-file/%E6%97%A5%E5%BF%97%E6%96%87%E4%BB%B6%E6%A0%BC%E5%BC%8F.png)

> **注意**：  
> 移除打印机 SD 卡前，**建议在打印机的设置中进行 SD 卡弹出**，避免造成文件损坏。  
> **导出打印机日志时请勿更改文件名。**

#### P1 系列打印机

1. 点击左侧菜单栏中的**设置**图标，选择**SD 卡**，点击**弹出**。  
   ![p-导出-1.png](https://wiki.bambulab.com/x1/troubleshooting/upload-log-file/p-%E5%AF%BC%E5%87%BA-1.png)
2. 将 SD 卡插入电脑查看日志。打印日志分别存放在 SD 卡下的三个文件夹中：logger，recorder 和 corelogger。

- **logger:** 提供简明的打印流程日志，所有问题的排查都需参考该文件夹中的日志。
- **recorder**: 用于定位调平校准异常、打印质量问题、传感器异常导致的打印停止、打印失败，以及打印过程中异常停止等问题的关键日志。
- **corelogger**: 记录系统异常时的状态信息，用于诊断打印异常停止问题。  
  ![sd卡-文件.png](https://wiki.bambulab.com/x1/troubleshooting/upload-log-file/sd%E5%8D%A1-%E6%96%87%E4%BB%B6.png)

> **注意**：  
> 移除打印机 SD 卡前，**建议在打印机的设置中进行 SD 卡弹出**，避免造成文件损坏。  
> **导出打印机日志时请勿更改文件名。**

#### A 系列打印机

1. 点击主页中的**设置**，选择**SD 卡**，点击**弹出**。  
   ![a-导出-1.png](https://wiki.bambulab.com/x1/troubleshooting/upload-log-file/a-%E5%AF%BC%E5%87%BA-1.png)
2. 将 SD 卡插入电脑查看日志。打印日志分别存放在 SD 卡下的三个文件夹中：logger，recorder 和 corelogger。

- **logger:** 提供简明的打印流程日志，所有问题的排查都需参考该文件夹中的日志。
- **recorder**: 用于定位调平校准异常、打印质量问题、传感器异常导致的打印停止、打印失败，以及打印过程中异常停止等问题的关键日志。
- **corelogger**: 记录系统异常时的状态信息，用于诊断打印异常停止问题。  
  ![sd卡-文件.png](https://wiki.bambulab.com/x1/troubleshooting/upload-log-file/sd%E5%8D%A1-%E6%96%87%E4%BB%B6.png)

> **注意**：  
> 移除打印机 SD 卡前，**建议在打印机的设置中进行 SD 卡弹出**，避免造成文件损坏。  
> **导出打印机日志时请勿更改文件名。**

## **FAQ**

### **打印机日志是什么，为什么在上传技术工单时需要提交日志信息？**

打印机日志是记录打印机操作过程的一些异常信息的文件，是判断打印机故障的重要依据。通过分析打印机日志，有助于售后团队快速定位问题所在，找出故障原因并提供解决方案。因此，提售后工单时包含打印机日志信息，能够有效提高问题解决的效率，节省时间和反复沟通成本。

### **我需要提交什么样的视频，打印机没有开启延时录影怎么办？**

如果您遇到打印机故障，可以使用手机拍摄一段描述故障现象的视频。根据故障类型,我们提供以下建议:

- 外观可见的机械和电子件结构损坏：拍摄一段描述损坏位置的视频。
- 供电/电子电路异常：拍摄线缆连接状态视频，并参考[硬件指示灯语义解释](../../general/indicator-led-explanation.md)。
- 工具头模块异常：拍摄2段视频，一段视频记录线缆连接状态，一段视频记录耗材从挤出机上端送入和送出时，屏幕或者Bambu Software上挤出机的进料指示标志。请参考[更换工具头电路板（新版）](../maintenance/toolhead_boards_v9.md)的步骤 13。
- 热床模块异常：拍摄热床回中和调平的视频。
- 微型激光雷达、AI 模块、屏幕、SD 卡、相机、LED、风扇、腔温异常：拍摄异常模块及周边线缆连接状态视频。
- X/Y/Z 轴异响/异常：拍摄 XYZ 轴运动时的视频。
- AMS 自动供料系统工作异常：拍摄将料线插入上下料的全过程视频,包括料线走向和屏幕报错信息。如果想了解 AMS 的工作流程，请参见 [AMS 主要功能和工作流程介绍](../../ams/manual/ams-function-introduction.md)。
- 打印机固件/网络异常：拍摄打印机联网步骤的视频。
- 拓竹软件 (Bambu Studio/Handy) 异常：拍摄描述异常细节的视频。
- 打印模型质量与预期不符：拍摄描述异常细节的视频。

如果遇到不易复现的故障，建议检查 SD 卡是否有延时录像，这有助于问题诊断。

### **打印机没有联网，我无法登录账号，如何上传打印机日志？**

除了打印机联网通过云端的方式上传，您也可以通过电脑网页端直接上传 SD 卡中的日志文件。

- 请先将日志文件导出到 SD 卡中，再上传到网页端。具体步骤如下:

1. 将 SD 卡插入打印机。

2. 在屏幕设定页面上点击"导出"操作,即可将日志文件保存到 SD 卡中。

3. 然后将 SD 卡插入电脑,通过电脑网页端上传 SD 卡中的日志文件。

- P1 系列和 A 系列打印机，由于日志是默认保存在 SD 卡中的，因此无需导出，直接通过网页端上传 SD 卡内的日志即可。

### **如果没有 SD 卡，还有没有其他方式上传打印机日志？**

如果打印机没有 SD 卡 或者 SD 卡功能出现故障，导致无法上传日志文件。理论上，这种情况下我们不会将日志作为必填项。

如果您遇到无法导出日志，但工单系统又要求您上传日志的情况，您可以通过售前工单或参考下一个问题以提交。我们会根据实际情况进行处理，评估该问题要求上传日志的必要性。

### **我尝试了以上所有方式，但都不可用，我如何成功提交技术工单？**

如果您遇到的问题不在以上的选项中，可以选择"其他"选项进行提交。在这种情况下，我们不会强制要求您上传图片、视频或打印机日志。

后续您与技术支持人员进行沟通时，如果他们建议您录制视频或上传日志，您可以直接将信息提交至工单内。这些信息对于我们解决问题非常重要，有助于我们更好地诊断和解决您的问题。

**我们理解有时候提供这些信息可能会带来一些不便，但相信通过您的配合，我们定能更高效地解决您的问题。如果您在提供信息的过程中遇到任何困难，也欢迎随时告知我们，我们会尽力提供帮助。**

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)；点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
