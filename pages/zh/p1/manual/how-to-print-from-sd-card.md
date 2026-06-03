---
path: zh/p1/manual/how-to-print-from-sd-card
title: "如何在 Bambu Lab P1 系列 3D 打印机中使用 SD 卡进行打印"
description: "本指南介绍从 SD 卡中进行打印的步骤"
tags: ["p1", "p1p", "p1s", "sd卡"]
created: 2024-09-05T01:48:34.146Z
updated: 2024-10-10T09:51:36.061Z
source: https://wiki.bambulab.com/zh/p1/manual/how-to-print-from-sd-card
---

在本指南中，我们将介绍使用 P1 系列 3D 打印机的 SD 卡进行打印的步骤。

## 适用打印机型号

- P1P
- P1S

## 何时使用?

- 打印机未联网时，可将文件导出至 SD 卡，并从中发起打印任务；
- 打印机联网时，可通过云端服务器发起打印任务，也可选择通过局域网将文件发送至 SD 卡，并从打印机屏幕发起打印任务。

## 如何在 P1P/P1S 中使用 SD 卡进行打印？

### 1. 弹出 SD 卡

Bambu Lab P1 系列 3D 打印机**不支持热插拔卡**，因此每次取出 SD 卡时，**请务必从菜单中安全弹出**，具体步骤如下：

- 进入 **设置 → SD 卡**
- 在 SD 卡菜单中点击**弹出**
- 点击**是**，确认选项

![中-p1-弹出sd.jpg](https://wiki.bambulab.com/p1/screen-operation/%E4%B8%AD-p1-%E5%BC%B9%E5%87%BAsd.jpg)

只需按下 SD 卡再松开，即可将其从打印机中弹出。

![](https://wiki.bambulab.com/p1/manual/print-from-sd/remove_micro_sd_card_from_p1.jpeg)

### 2. 使用 Bambu Studio 对 3D 模型进行切片

打开 Bambu Studio，导入要打印的模型，按照以下步骤进行操作：

- 选择正确的**打印机型号**
- 选择正确的**打印板类型**
- 选择要打印的**耗材丝**
- 点击**切片单盘**

![p1-发送单盘.jpg](https://wiki.bambulab.com/p1/screen-operation/p1-%E5%8F%91%E9%80%81%E5%8D%95%E7%9B%98.jpg)

模型切片完成后，将显示模型预览。

- 选择打印单盘旁边的**小箭头**
- 点击**导出单盘切片文件**选项
- 再次点击**导出单盘切片文件**

![p-a_导出单盘切片.jpg](https://wiki.bambulab.com/studio-print-all/p-a_%E5%AF%BC%E5%87%BA%E5%8D%95%E7%9B%98%E5%88%87%E7%89%87.jpg)

系统会弹出提示，让您选择保存文件的位置。

### 3. 复制文件并将 SD 卡插入打印机

当电脑出现保存提示时：

- 请为模型**设置文件名**。
- 选择**文件保存的位置**。在本例中，文件保存在**打印机的 SD 卡**中。
- 点击**保存**

![保存文件.jpg](https://wiki.bambulab.com/studio-print-all/%E4%BF%9D%E5%AD%98%E6%96%87%E4%BB%B6.jpg)

> **注意： 不要将文件保存在 SD 卡的任何文件夹中，请保存在 SD 卡的根目录下。**

然后从电脑中取出 SD 卡，并将其插入打印机的 SD 卡插槽中。

![](https://wiki.bambulab.com/p1/manual/print-from-sd/remove_micro_sd_card_from_p1.jpeg)

### 4. 开始打印

文件切片完成并复制到打印机的 SD 卡后，可开始进行打印。

- 点击屏幕上的文件夹选项
- 选择之前保存的文件
- 按 **OK 键**即可开始打印

![](https://wiki.bambulab.com/p1/manual/print-from-sd/start_the_print.jpeg)

### 发送单盘打印任务

#### 1. 使用 Bambu Studio 对 3D 模型进行切片

打开 Bambu Studio，导入要打印的模型，按照以下步骤进行操作：

- 选择正确的**打印机型号**
- 选择正确的**打印板类型**
- 选择要打印的**耗材丝**
- 点击**切片单盘**

![p1-发送单盘.jpg](https://wiki.bambulab.com/p1/screen-operation/p1-%E5%8F%91%E9%80%81%E5%8D%95%E7%9B%98.jpg)

#### 2. 发送模型至打印机 SD 卡

模型切片完成后，将显示模型预览。

- 选择打印单盘旁边的**小箭头**
- 点击**发送**选项
- 再次点击**发送**

![a1-发送-中.png](https://wiki.bambulab.com/a1-sd/a1-%E5%8F%91%E9%80%81-%E4%B8%AD.png)

在弹出的窗口中选择想要发送的打印机，并点击**发送**。

![a1-发送2-中.png](https://wiki.bambulab.com/a1-sd/a1-%E5%8F%91%E9%80%812-%E4%B8%AD.png)

> ***注意**：强烈建议在开始打印前清洗打印表面。*  
> *这将最大限度地提高打印成功的几率，并将因附着不良导致打印失败的风险降到最低。*  
> *请关注[纹理PEI板清理指南](../../filament-acc/acc/pei-plate-clean-guide.md) 以了解更多信息*

## 结束语

> *我们希望本指南能为您提供有用的信息，帮助您解决问题。*
>
> *我们希望能确保您安全有效地进行操作。如果您对本指南描述的过程有任何疑虑或问题，建议您在开始操作前联系我们友好的客户服务团队。*  
> *我们随时准备为您解答疑问并提供帮助。[点击此处联系在线技术支持 （服务时间 9:00-21:00）](https://support.bambulab.cn/cn/im)*  
> *我们将尽最大努力及时回复，并为您提供所需的帮助。*
