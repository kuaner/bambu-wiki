---
path: zh/ams-ht/manual/intro-and-connection-guide
title: "AMS HT 模块介绍和连接配置 "
description: ""
tags: []
created: 2025-04-10T09:27:04.415Z
updated: 2026-03-25T06:35:58.082Z
source: https://wiki.bambulab.com/zh/ams-ht/manual/intro-and-connection-guide
---

## 模块介绍

本指南介绍 AMS HT 各个模块的部件、连接方式和功能，同时涵盖安装、设置及多台设备连接的方法，帮助用户正确完成配置，获得最佳性能。

### 外观和部件示意图

| **AMS HT 外观** | **部件示意图** |
| --- | --- |
|  |  |

### 显示屏

AMS HT 正面配备了一个显示屏，从左到右依次显示实时湿度、实时温度和剩余烘干时长，如下图所示。

![](https://wiki.bambulab.com/ams-ht/manual/intro-and-connection-guide/image-6.png)

### 开盖传感器

AMS HT 配备了一个开盖传感器，由磁铁和霍尔传感器组成。如果在烘干过程中打开上盖，打印机会发出提醒。磁铁位于上盖的把手组件上，而霍尔传感器位于中框上。

|  |  |
| --- | --- |
| 磁铁 | 霍尔传感器 |

### 进料口和指示灯

AMS HT 的进料口如下图所示。插入耗材时，进料口会自动拉动耗材；当需要收回耗材时，主动轴会转动料盘将其缠绕回收。进料口**内嵌陶瓷加强防磨衬套**，有效防止长时间使用后耗材丝对进料口的磨损。

进料口旁边是指示灯，不同灯光状态对应 AMS HT 的不同工作模式。

![](https://wiki.bambulab.com/ams-ht/manual/intro-and-connection-guide/image-8.png)

### 耗材释放按钮

进料口后方有一个耗材释放按钮。当耗材在 AMS 内部且需要手动取出时，按下该按钮可释放齿轮压力，轻松拉出耗材。

![](https://wiki.bambulab.com/ams-ht/manual/intro-and-connection-guide/image.png)

### 单通组件

单通组件位于 AMS HT 的头部，由**上下料组件、内部助力电机**和**退料回转组件**组成。

- **上下料组件**：包含进料检测传感器和里程轮。霍尔传感器用于检测耗材是否插入，里程轮用于计算送料长度。
- **内部助力电机**：驱动耗材的送入和拉回。
- **退料回转组件**：包含电机和摇臂齿，退料时驱动主动轴回转，带动料盘收回耗材。

|  |  |
| --- | --- |
|  |  |

|  |  |
| --- | --- |
|  |  |

### 序列号

AMS HT 的序列号贴纸贴在设备内部，耗材释放按钮的正下方。

- 序列号由数字和字母组成，序列号贴纸上还有一个二维码。
- 在申请保修或技术支持时，请使用此序列号。

![sn_ht_yellowarrow.png](https://wiki.bambulab.com/ams-ht/maintenance/sn_ht_yellowarrow.png)

### TPU 出料口

AMS HT 上盖后方设有专门的 TPU 出料口。由于 TPU 耗材较软，使用 AMS 自动进料功能时容易失败。使用 TPU 时，将其放入 AMS HT 并确保料盘按正确方向转动，然后将料管插入 TPU 出料口。手动将耗材从铁氟龙料管推至挤出机，直到耗材完全进入。  
**注意**：使用 TPU 时，AMS HT 无法使用自动进退料功能，但可作为干燥箱使用，防止材料受潮。

|  |  |  |
| --- | --- | --- |
|  |  |  |

### 出料口和释放按钮

AMS HT 背部的出料口用于连接 PTFE 料管，下方有一个方形释放按钮。按下按钮可释放料管并轻松取出。

![](https://wiki.bambulab.com/ams-ht/manual/intro-and-connection-guide/image-9.png)

### 出料霍尔组件

在 AMS HT 后方靠近出料口的位置，设有一个出料霍尔组件。该组件用于检测耗材是否成功送出 AMS。当遇到断料、卡料等异常情况时，出料霍尔组件可帮助判断耗材的具体位置，便于用户快速排查问题。

|  |  |
| --- | --- |
|  |  |

### **供料缓冲器**

AMS HT 和打印机之间需要连接一个供料缓冲器，由滑块、弹簧和霍尔传感器组成。当 AMS 将耗材推入工具头挤出机时，滑块会因耗材压力向前移动，霍尔传感器检测滑块位置并将信号反馈给 AMS 和打印机。通过控制 AMS 的进给速度，确保耗材张力在合理范围内，使挤出机工作更轻松、精确。

H2D 打印机内置供料缓冲器，还配备了耗材传感器，可检测耗材是否通过或断裂在内部。此外，使用外挂料盘时，缓冲器还支持缠料检测功能。

![](https://wiki.bambulab.com/ams-ht/manual/intro-and-connection-guide/image-17.png)

如需将 AMS HT 连接至 X1 或 P1 系列打印机，需额外购买缓冲器（连接 1 台）或 AMS Hub（连接多台）。

![](https://wiki.bambulab.com/ams-ht/manual/intro-and-connection-guide/image-18.png)

如果您需要将 AMS HT 连接至 A1 系列打印机，则需要额外购买 **A1 系列料线选通器** 来连接使用。请勿使用供料缓冲器或 AMS Hub 连接，否则会导致缓冲器或 AMS Hub 使用功能异常或损坏，在此种情况下，该缓冲器或 AMS Hub 将不予保修。

![ams_hub.png](https://wiki.bambulab.com/a1/ams-connection-guide/ams_hub.png)

### 防潮系统

#### 烘干模块

AMS HT 的烘干模块由加热片、风扇和 NTC 温度传感器组成，最高烘干温度为 85℃。

|  |  |
| --- | --- |
|  |  |

#### 湿度传感器

AMS HT 配备湿度传感器，它位于烘干模块的内部，可用于检测舱内湿度和温度。您可通过打印机显示屏、Bambu Studio 或 Bambu Handy 查看当前湿度状态。

|  |  |
| --- | --- |
|  |  |

#### 内循环系统

烘干模块位于 AMS HT 中框下方。烘干时，热风从内循环进风口（靠近进料口）吹出，加热耗材后，空气通过后方的内循环出风口被吸回加热模块，形成内循环系统。

![](https://wiki.bambulab.com/ams-ht/manual/intro-and-connection-guide/image-24.png)

#### 进出气口

AMS HT 配备两个主动开关的进出气风门：**底部为进气口，后侧为出气口。**

烘干时，AMS HT 会通过外循环排出湿气。请确保进出气口未被遮挡，以获得最佳烘干效果。

|  |  |
| --- | --- |
| 进气口 | 出气口 |

#### 干燥剂和密封胶圈

AMS HT 出厂配备变色硅胶干燥剂，位于后方的从动支撑轴下方。干燥剂吸收水分，保持舱内空气干燥。吸湿后，黄色颗粒变为深绿色，此时需更换或烘干干燥剂后重复使用。  
**注意**：干燥剂需从密封透明袋中取出后再放入 AMS。

上盖与外壳之间的橡胶密封圈可保持 AMS 密封性，防止外部湿气进入。当湿度超出预设标准时，湿度传感器会提醒用户。

| **干燥剂状态** | **干燥剂位置** | **橡胶密封圈** |
| --- | --- | --- |
| 左：失效干燥剂；右：正常干燥剂 |  |  |

***注意：干燥剂需从密封透明塑料袋中取出后，再放入 AMS 中。***

### RFID 模块

AMS HT 配备 RFID 线圈，可识别 Bambu Lab 官方耗材的 RFID 标签，实现耗材余量估算、自动续料等功能。

![1](https://wiki.bambulab.com/ams-ht/manual/intro-and-connection-guide/image-34.png)

### 电源线

由于 **AMS HT 烘干功能功率较高，无法通过打印机直接供电**。因此，**AMS HT 标配电源线**，使用烘干功能时需连接电源线。连接方式如下图所示：

![](https://wiki.bambulab.com/ams-ht/manual/intro-and-connection-guide/image-35.png)

### 料管拓展口

料管拓展口可将 4 个进料模块连接至打印机。连接多台 AMS HT 至 H2 系列打印机时，需使用此接口。

![](https://wiki.bambulab.com/ams-ht/manual/intro-and-connection-guide/image-32.png)

## 连接和配置 AMS HT

具体步骤请参考：[多机型 AMS 连接指南](../../ams/manual/multi-model-AMS-compatibility-guide.md)。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南未解决您的问题，[*请联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
