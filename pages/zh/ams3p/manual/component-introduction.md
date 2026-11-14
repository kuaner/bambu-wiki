---
path: zh/ams3p/manual/component-introduction
title: "AMS 3P 部件介绍"
description: "本文介绍了 AMS 3P 的主要部件及功能。"
tags: []
created: 2026-11-13T08:52:49.569Z
updated: 2026-11-13T08:52:49.569Z
source: https://wiki.bambulab.com/zh/ams3p/manual/component-introduction
---

## AMS 3P

AMS 3P 是适配 P3C 的智能供料设备，可实现多色 / 多材料打印、自动续料，还具备耗材烘干防潮保护、RFID 耗材识别等功能，能减少手动操作，提升打印效率与智能化程度。本文将介绍 AMS 3P 的主要部件及功能。

![ams_3p_____-image-11.png](https://public-cdn.bblmw.com/wiki/new/ams3p/manual/component-introduction/zh/ams_3p_____-image-11.png)

## 料管导向组件

料管导向组件安装在 AMS 3P 正下方，用于衔接 AMS 3P 与料管架组件。为了优化进料路径并降低阻力，系统中包含 7 个直列料管连接件，分别对应 1–7 号料管。

![ams_3p_____-image-13.png](https://public-cdn.bblmw.com/wiki/new/ams3p/manual/component-introduction/zh/ams_3p_____-image-13.png)

料管导向组件上方共有 7 个孔位，分别对应 1-7 号槽位，打印机通过 AMS 3P 进料组件完成选料和送料操作，可将耗材通过导向支架送至对应的路径中，最终送入打印头内。

![ams_3p_____-image-9.png](https://public-cdn.bblmw.com/wiki/new/ams3p/manual/component-introduction/zh/ams_3p_____-image-9.png)

### 打印头控制板

打印头控制板位于料管导向组件前方，负责传递各类传感器信号，是打印头稳定运行的核心控制部件。

![ams_3p_____-image-12.png](https://public-cdn.bblmw.com/wiki/new/ams3p/manual/component-introduction/zh/ams_3p_____-image-12.png)

## 料管支架组件

料管支架组件分为主料管支架、左料管支架和右料管支架，避免料管垂放至机箱内部；

- **主料管支架：**位于料管导向支架正下方，用于固定打印头的线缆和料管；

![ams_3p_____-image-10.png](https://public-cdn.bblmw.com/wiki/new/ams3p/manual/component-introduction/zh/ams_3p_____-image-10.png)

- **左料管支架：**用于固定左侧的 4 根料管（1-4 号）；

![ams_3p_____-image-8.png](https://public-cdn.bblmw.com/wiki/new/ams3p/manual/component-introduction/zh/ams_3p_____-image-8.png)

- **右料管支架：**用于固定右侧的 3 根料管（5-7 号）。

![ams_3p_____-image-7.png](https://public-cdn.bblmw.com/wiki/new/ams3p/manual/component-introduction/zh/ams_3p_____-image-7.png)

## 撑杆组件

AMS 3P 有左右两个撑杆组件，完全打开 AMS 上盖后松手，撑杆可撑住上盖；再次完全打开上盖，即可释放撑杆，向下可合上上盖。

|  |  |
| --- | --- |
| ams_3p_____-image-5.png | ams_3p_____-image-6.png |

## 进料组件

进料组件将 AMS 分为上下两部分，上方包含 3 个槽位，分别对应 2、4、6 号上下料嘴；下方包含 4 个槽位，分别对应 1、3、5、7 号料嘴。

![ams_3p_____-image-4.png](https://public-cdn.bblmw.com/wiki/new/ams3p/manual/component-introduction/zh/ams_3p_____-image-4.png)

## 耗材信息读取

AMS 3P 配备了 6 个线圈（前面 3 个，后面 3 个），可以识别 Bambu Lab 官方耗材上的标签，并支持耗材自动续料等功能。

与传统 AMS 不同，将料盘放入槽位后，进入打印机屏幕的耗材页，点击左下角刷新键即可自动读取耗材信息。

![ams_3p_____-image-2.png](https://public-cdn.bblmw.com/wiki/new/ams3p/manual/component-introduction/zh/ams_3p_____-image-2.png)

## 烘干防潮系统

### 烘干模块（选配）

AMS 3P 可选配烘干升级套件，由加热片、风扇以及 NTC 温度传感器构成，最大烘干温度可达 **75℃。**

![ams_3p_____-image-3.png](https://public-cdn.bblmw.com/wiki/new/ams3p/manual/component-introduction/zh/ams_3p_____-image-3.png)

套件可安装至 2、4 槽位，并配备可磁吸快拆的**耗材烘干仓盖**，能够有效去除耗材中的水分，提升打印质量。

![ams_3p_____-image-1.png](https://public-cdn.bblmw.com/wiki/new/ams3p/manual/component-introduction/zh/ams_3p_____-image-1.png)

### 进出气口

AMS 3P 的进出气口位于烘干模块内，配备主动开关的进气和出气风门。在烘干耗材时，AMS 3P 会通过外循环将湿气从内部排出。进行外循环时，进气口和出气口会打开，**请确保进气口和出气口不被其他物品遮挡**，以获得最佳烘干效果。

![ams_3p_____-image.png](https://public-cdn.bblmw.com/wiki/new/ams3p/manual/component-introduction/zh/ams_3p_____-image.png)

> **注意**：仅在**安装烘干模块**前需要通过易撕角（绿圈内）移除贴纸，其余情况请勿撕除。
>
> |  |  |
> | --- | --- |
> | 有 PC 贴纸 | 无 PC 贴纸 |

### 温湿度传感器

AMS 3P 在烘干仓中配备了一个温湿度传感器，可以检测仓内的温度和湿度。您可以在打印机屏幕 / Bambu Studio / Bambu Handy 中查看 AMS 当前的湿度状态。

![ams_3p_____-image-15.png](https://public-cdn.bblmw.com/wiki/new/ams3p/manual/component-introduction/zh/ams_3p_____-image-15.png)

### 干燥剂和密封胶圈

AMS 3P 出厂配备**变色硅胶干燥剂**，可放置在撑杆旁及烘干仓盖内。干燥剂吸收水分，保持舱内空气干燥。吸湿后，黄色颗粒会变为深绿色，此时需要更换或烘干干燥剂后重复使用。上盖与外壳之间的橡胶密封圈可保持 AMS 的密封性，防止外部湿气进入。当湿度超出预设标准时，湿度传感器会提醒用户。

标配 80g 硅胶干燥剂，共 8 小包，烘干槽上盖的槽位最多可以放 4 小包，其他可以放在腔体内其他干燥剂槽位；如果对湿度要求特别高，也可以自己额外购买干燥剂放在 8 号槽右侧的槽位内。

> **注意**：干燥剂需从密封透明袋中取出后再放入 AMS。

![ams_3p_____-image-16.png](https://public-cdn.bblmw.com/wiki/new/ams3p/manual/component-introduction/zh/ams_3p_____-image-16.png)

## 耗材直通口

AMS 3P 设有 5 个专用的 TPU 进料口，分别在 1、3、4、5、7 号槽，无需通过料管即可直接将 TPU 耗材输送至工具头进行打印，从而降低打印阻力。关于 TPU 打印的具体步骤请参考：[TPU 打印指南](https://wiki.bambulab.com/zh/p3c/manual/tpu-printing-guide)。

![ams_3p_____-image-14.png](https://public-cdn.bblmw.com/wiki/new/ams3p/manual/component-introduction/zh/ams_3p_____-image-14.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
