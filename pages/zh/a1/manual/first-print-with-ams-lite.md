---
path: zh/a1/manual/first-print-with-ams-lite
title: "A1 初次打印指南（使用 AMS lite）"
description: "本文介绍了如何在 A1 系列打印机上使用 AMS Lite 开启初次打印"
tags: ["a1", "ams lite"]
created: 2023-12-18T02:11:40.043Z
updated: 2026-07-08T06:13:30.473Z
source: https://wiki.bambulab.com/zh/a1/manual/first-print-with-ams-lite
---

## 视频指南

## 1. 打印准备

### 1. 安装料盘

根据耗材绕线的方向，安装料盘。正确的料盘安装方向是料头可以顺着绕线的方向从下方插入上下料嘴。

|  |  |
| --- | --- |
|  |  |

AMS lite 支持宽度为40-68毫米、内径为53-58毫米的料盘。

请避免使用 AMS lite 来打印柔性材料，包括 TPU（除了 AMS 专用 TPU）、TPE 或潮湿的水溶性耗材 PVA。请避免使用太硬(即模量过高)或太脆(即韧性不足)的材料，包括第三方线纤维增强材料，如 PA-CF/GF、PET-CF/GF 和 PLA-CF/GF 等。请使用外挂料盘的方式来打印这些耗材。

![](https://wiki.bambulab.com/n1/manual/first-print-with-ams/prepare3.png)

### 2. 往 AMS lite 进料口里插入线材

在确认料盘已安装到位后，可以通过进料口装载耗材。请对准插入口，避免插入失败。如果耗材卡住，可按释放按钮解除驱动电机的连接，以便更方便地插入耗材。插入线材后，上下料器会自动将耗材送入料管中，约 40 cm。

|  |  |
| --- | --- |
|  |  |

![](https://wiki.bambulab.com/a1/manual/first-print/%E6%8F%92%E5%85%A5%E8%80%97%E6%9D%902.png)

## 2. 开始打印

**线材装载完毕并确保构建板放置正确后，即可开始进行打印。**

![](https://wiki.bambulab.com/a1/manual/first-print/%E5%BC%80%E5%A7%8B%E6%89%93%E5%8D%B01.png)

> **注意**：在打印机开箱时，由于热床放置时间较久，首层打印时的移动摩擦力可能较大，这可能导致直接打印时出现错位，从而损坏打印板。为避免此情况，**建议手动将热床移动至最大行程**，以确保顺利打印。

### 1. 使用 Bambu Studio 发起打印任务

#### 安装 Bambu Studio

下载 Bambu Studio: <https://bambulab.cn/zh/download/studio>

![](https://wiki.bambulab.com/n1/manual/first-print-with-ams/start-print2-cn.png)

#### 模型切片和发送打印任务

选择想打印的模型，点击右上角切片单盘，再点击右上角打印单盘。

|  |  |
| --- | --- |
|  |  |

### 2. 使用内置文件发起打印

#### 点击首页的 “Print files”，访问 SD 卡的内置文件

![发起打印_主页.jpg](https://wiki.bambulab.com/a1/manual/first-print/%E5%8F%91%E8%B5%B7%E6%89%93%E5%8D%B0_%E4%B8%BB%E9%A1%B5.jpg)

#### 选择你想要打印的模型

![发起打印_内置文件.jpg](https://wiki.bambulab.com/a1/manual/first-print/%E5%8F%91%E8%B5%B7%E6%89%93%E5%8D%B0_%E5%86%85%E7%BD%AE%E6%96%87%E4%BB%B6.jpg)

#### 勾选启用 AMS，推荐启用热床调平功能。

![发起打印_打印设置.jpg](https://wiki.bambulab.com/a1/manual/first-print/%E5%8F%91%E8%B5%B7%E6%89%93%E5%8D%B0_%E6%89%93%E5%8D%B0%E8%AE%BE%E7%BD%AE.jpg)

#### 配置在打印中使用的耗材对应的 AMS 插槽：

|  |  |
| --- | --- |
| 发起打印_选择耗材.jpg |  |

如果没有与文件颜色一致的耗材可用，您可以在 AMS lite 中放置预设的耗材，或选择具有相似属性且接近颜色的其他耗材。

#### 点击“打印”

![发起打印_点击打印.jpg](https://wiki.bambulab.com/a1/manual/first-print/%E5%8F%91%E8%B5%B7%E6%89%93%E5%8D%B0_%E7%82%B9%E5%87%BB%E6%89%93%E5%8D%B0.jpg)

## 附录：移除料盘

### 1. 从 PTFE 管里退出线材

在料线退出工具头后，边旋转料盘，边拉回线材（如果线材卡住，按下释放按钮可分离驱动电机）。当线材接近气管接头时，用手接住料头，并将料线头塞进料盘的孔洞中。

|  |  |
| --- | --- |
|  |  |

在正常完成打印任务后，打印头的耗材会自动退回到 AMS lite。然而，如果打印任务在中途被取消或中断，您需要在屏幕上点击"退料"，手动退料，以便让被打印头咬合的线材退回到 AMS lite，再进行上述卸载料盘的操作。

|  |  |
| --- | --- |
| 发起打印_手动退料.jpg | 发起打印_退料过程.jpg |

### 2. 取下料盘

取出料盘时，请用双手环扣住整个料盘，而不是只抓住一边，同时用大拇指靠近转轴中心，向外取出料盘。

![](https://wiki.bambulab.com/a1/manual/first-print/%E5%8F%96%E6%B6%88%E6%96%99%E7%9B%981.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 我们希望能确保您安全有效地进行操作。如果您对本指南描述的过程有任何疑虑或问题，建议您在开始操作前联系我们友好的客户服务团队。
>
> 我们随时准备为您解答疑问并提供帮助。[点击此处联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/cn/im)
