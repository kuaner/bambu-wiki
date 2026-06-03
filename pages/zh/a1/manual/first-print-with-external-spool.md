---
path: zh/a1/manual/first-print-with-external-spool
title: "A1 初次打印指南（使用外挂料盘）"
description: "本文介绍了如何在 A1 系列打印机上使用外挂料盘开启首次打印"
tags: ["a1"]
created: 2023-12-18T02:48:47.191Z
updated: 2025-02-28T07:43:02.168Z
source: https://wiki.bambulab.com/zh/a1/manual/first-print-with-external-spool
---

## 视频教程

## 打印准备

### 使用附赠耗材

![](https://wiki.bambulab.com/n1/manual/first-print-with-external-spool/%E8%B5%A0%E9%80%81%E8%80%97%E6%9D%90.jpg)

#### 1. 插入耗材

将耗材插入，向工具头里推送耗材，直至其无法前进。

|  |  |
| --- | --- |
|  |  |

#### 2. 进料

1. 点击打印机屏幕的**耗材**，工具头处会出现小绿灯，表示检测到耗材进入。

|  |  |
| --- | --- |
|  |  |

2. 编辑耗材信息，点击进料。

|  |  |  |
| --- | --- | --- |
|  |  |  |

3. 喷嘴开始加热到 250 ℃ 后，再次手动推入耗材。

|  |  |
| --- | --- |
|  |  |

4. 观察喷嘴，如果挤出机正常吐料，在屏幕上选择**继续**，则完成进料。

|  |  |
| --- | --- |
|  |  |

如果耗材没有被吐出，选择**重试**，然后重复推入耗材的动作，直至耗材挤出。

### 使用料盘

#### 1. 安装料盘

根据耗材绕线的方向，安装料盘。

|  |  |
| --- | --- |
|  |  |

#### 2. 进料

将耗材的一端插入料管，向工具头里推送耗材直至无法前进。此时，打印机屏幕上的工具头处会出现小绿灯，表示检测到耗材进入。

|  |  |
| --- | --- |
|  |  |

在屏幕上选择"进料"

![](https://wiki.bambulab.com/a1/manual/first-print-external/%E9%80%89%E6%8B%A9load.png)

喷嘴开始加热到 250 ℃后，再次手动推入耗材

|  |  |
| --- | --- |
|  |  |

观察喷嘴，以确保挤出机正常吐料。

![](https://wiki.bambulab.com/a1/manual/first-print-external/%E7%BB%A7%E7%BB%AD%E6%8E%A8%E6%96%993.png)

喷嘴顺利吐出融化的线材后，在屏幕上选择“完成”。

![](https://wiki.bambulab.com/a1/manual/first-print-external/%E7%BB%A7%E7%BB%AD%E6%8E%A8%E6%96%994.png)

如果耗材没有被吐出，选择“重试”，然后重复推入耗材的动作。

## 开始打印

**在确保装载好线材和放置打印板后，可以开始打印。**

![](https://wiki.bambulab.com/a1/manual/first-print-external/%E5%BC%80%E5%A7%8B%E6%89%93%E5%8D%B01.png)

> **注意**：在打印机开箱时，由于热床放置时间较久，首层打印时的移动摩擦力可能较大，这可能导致直接打印时出现错位，从而损坏打印板。为避免此情况，**建议手动将热床移动至最大行程**，以确保顺利打印。

### 1. 使用 Bambu Studio 发起打印任务

点击此处[下载Bambu Studio](https://bambulab.cn/zh/download/studio)。

![](https://wiki.bambulab.com/n1/manual/first-print-with-ams/start-print2-cn.png)

选择模型，切片和发送打印任务。

|  |  |
| --- | --- |
|  |  |

### 2. 使用内置文件发起打印

点击“Print files”，访问 microSD 卡的内置文件。

![](https://wiki.bambulab.com/a1/manual/first-print-external/%E5%8F%91%E8%B5%B7%E5%86%85%E7%BD%AE1.png)

选择想要打印的模型。

![](https://wiki.bambulab.com/a1/manual/first-print-external/%E5%8F%91%E8%B5%B7%E5%86%85%E7%BD%AE2.png)

推荐启用热床调平和动态流量校准功能。

![](https://wiki.bambulab.com/a1/manual/first-print-external/%E5%8F%91%E8%B5%B7%E5%86%85%E7%BD%AE3.png)

开始“打印”。

![](https://wiki.bambulab.com/a1/manual/first-print-external/%E5%8F%91%E8%B5%B7%E5%86%85%E7%BD%AE4.png)

## 如何续料

如果在打印过程中，料已经用完了，则可以从外挂支架上取下空料盘，并安装新料盘，参考上述的 **"打印准备"** 操作进行续料。

## 如何换料

如果想换料，则需要暂停当前打印任务，先将工具头中耗材退出，再装载新耗材。

### 1. 退料

在屏幕上选择 **退料/Unload**，打印机将开始自动加热热端，并切断耗材。

|  |  |
| --- | --- |
|  |  |

### 2. 抽出耗材

完成上一步后，需要手动抽出耗材才能完成退料流程。

请根据 APP/Studio 上的提示，尽快手动抽出耗材。如果喷嘴温度保持在 142℃ 且不下降，说明挤出机内仍有余料，则表示退料尚未完成。

|  |  |
| --- | --- |
|  |  |

如果没有及时抽出耗材，请在屏幕上选择 **重试/Retry** 并重新抽出。

### 3. 进料

完成退料操作后，按照上述的 **“打印准备”** 操作进料。

**结束语**

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南并未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/cn/im)，我们随时准备为您解答疑问并提供帮助。
>
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
