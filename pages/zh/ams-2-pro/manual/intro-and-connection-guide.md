---
path: zh/ams-2-pro/manual/intro-and-connection-guide
title: "AMS 2 Pro 各模块介绍和连接配置"
description: ""
tags: []
created: 2025-03-25T12:33:50.571Z
updated: 2026-06-02T03:00:28.080Z
source: https://wiki.bambulab.com/zh/ams-2-pro/manual/intro-and-connection-guide
---

## 模块介绍

### 外观和三维尺寸

| **AMS 2 Pro外观** | **三维尺寸图** |
| --- | --- |
|  |  |

### 耗材插槽

AMS 2 Pro有 4 个耗材插槽，每个槽内各有一个上下料器。它有独立的电机和齿轮推动耗材丝向前或将其绕回料盘，有一个传感器来检测耗材。当插入耗材丝时，它会往里拉动耗材丝；当需要将耗材卷回料盘时，主动轴会转动料盘将耗材缠绕回收。每个上下料器入口**内嵌陶瓷加强防磨衬套**，可以更好地保护入料口防止其在长时间使用后被耗材丝磨损。

| **耗材插槽** | **上下料器入口** |
| --- | --- |
|  |  |

### 五通

**五通**位于AMS 2 Pro的尾部，由四个霍尔传感器、一个磁性旋转编码器和一个无刷电机组成。 它将四个耗材插槽合并为一个。 霍尔传感器检测耗材丝何时到达特定位置，激活无刷电机为耗材提供第二级驱动力。

|  |  |
| --- | --- |

### **供料缓冲器**

AMS 2 Pro和打印机之间需要连接一个缓冲器，它由滑块、弹簧和霍尔传感器组成。AMS将耗材推入工具头挤出机时，由于耗材的压力，滑块向前移动，通过霍尔传感器检测滑块移动的位置，供料缓冲器将信号反馈回 AMS 和打印机。通过控制AMS的进给速度，可以确保耗材的张力在控制范围内，这样工具头挤出机就可以轻松而精确地工作。

H2D打印机内部自带供料缓冲器，缓冲器内部还具有耗材传感器，**可以检测是否有耗材丝通过缓冲器或者耗材丝是否断在缓冲器内部**。另外，在用外挂料盘打印时，缓冲器还具备缠料检测功能，可以检测到外挂料盘是否缠料。

![](https://wiki.bambulab.com/ams-2-pro/manual/part-intro-and-connection-guide/image-7.png)

如果您需要将AMS 2 Pro连接至X1或P1系列打印机，则需要额外购买缓冲器（连接1台）或 [AMS Hub](https://item.jd.com/10147107132256.html)（连接多台）来连接使用。

![](https://wiki.bambulab.com/ams-2-pro/manual/part-intro-and-connection-guide/image-8.png)

如果您需要将 AMS 2 Pro 连接至 A1 系列打印机，则需要额外购买 A1 系列料线选通器来连接使用。请勿使用 AMS 自带的缓冲器或 AMS Hub 连接，否则会导致缓冲器使用功能异常或损坏，在此种情况下，该缓冲器或 AMS Hub 将不予保修。

![ams_hub.png](https://wiki.bambulab.com/a1/ams-connection-guide/ams_hub.png)

### 防潮系统

#### 湿度传感器

AMS 2 Pro的正前方配备了一个湿度传感器，可以检测AMS舱内的湿度和温度。您可以在打印机的显示屏/Bambu Studio/Bambu Handy中查看AMS当前的湿度状态。

![](https://wiki.bambulab.com/ams-2-pro/manual/part-intro-and-connection-guide/image.png)

![](https://wiki.bambulab.com/ams-2-pro/manual/part-intro-and-connection-guide/image-1.png)

#### 烘干模块

AMS 2 Pro配备了两个烘干模块，它由加热片，风扇，以及NTC温度传感器构成，最大可以烘干的温度是65℃。

![](https://wiki.bambulab.com/ams-2-pro/manual/part-intro-and-connection-guide/image-2.png)

![](https://wiki.bambulab.com/ams-2-pro/manual/part-intro-and-connection-guide/image-3.png)

#### 内循环系统

烘干模块位于AMS主框架下面，烘干时热风从内循环出风口吹出（靠近五通），加热耗材后，再从前面两个内循环进风口把空气吸到加热模块，重新加热，形成一套内循环系统。

![](https://wiki.bambulab.com/ams-2-pro/manual/part-intro-and-connection-guide/image-4.png)

#### 进出气口

AMS 2 Pro配备了两个主动开关的进出气风门，底部风门为进气口，后侧风门为出气口。

在烘干耗材时，AMS 2 Pro会通过外循环的方式，将湿气从内部排出。在进行外循环时，进气口和出气口会打开，请确保进气口和出气口不被其他物品遮挡，以获得最佳烘干效果。

|  |  |
| --- | --- |

#### 干燥剂和密封胶圈

AMS 2 Pro出厂配备变色硅胶干燥剂，位于后方的从动支撑轴下方。干燥剂吸收水分，保持舱内空气干燥。吸湿后，黄色颗粒变为深绿色，此时需更换或烘干干燥剂后重复使用。  
**注意**：干燥剂需从密封透明袋中取出后再放入 AMS。

上盖与外壳之间的橡胶密封圈可保持 AMS 密封性，防止外部湿气进入。当湿度超出预设标准时，湿度传感器会提醒用户。

| **干燥剂状态** | **干燥剂** | **橡胶密封圈** |
| --- | --- | --- |
| 左：失效干燥剂；右：正常干燥剂 |  |  |

***注意：干燥剂需从密封透明塑料袋中取出后，再放入AMS中。***

### 电源适配器

使用6-pin连接线连接H2系列打印机和单台AMS 2 Pro，即可使用AMS 2 Pro的烘干功能**。如果需要同时烘干多台AMS 2 Pro内的耗材，则需要使用拓竹官方电源适配器来给其余的AMS 2 Pro供电。**  
如果X1或P1系列打印机配合AMS 2 Pro一起使用并启用AMS 2 Pro的烘干功能，则每台AMS 2 Pro都需要使用拓竹官方电源适配器来为其供电。电源适配器的使用方式如下图所示：

![](https://wiki.bambulab.com/ams-2-pro/manual/part-intro-and-connection-guide/image-15.png)

### RFID模块

AMS 2 Pro中配备了两个RFID线圈，通过它们可以识别 Bambu Lab官方耗材上的 RFID 标签，还可以通过它实现耗材余量估算、自动续料等功能。

![](https://wiki.bambulab.com/ams-2-pro/manual/part-intro-and-connection-guide/image-16.png)

### 料管拓展口

料管拓展口能同时将4个进料模块连接到打印机，在连接多台AMS 2 Pro至H2系列打印机时，需要用到料管拓展口，最多可以连接4台AMS 2 Pro以实现16色打印。

![](https://wiki.bambulab.com/ams-2-pro/manual/part-intro-and-connection-guide/image-17.png)

## 连接和配置AMS 2 Pro

- 连接AMS 2 Pro至H2系列打印机
- 连接 AMS 2 Pro 至 X2D 打印机
- 连接 AMS 2 Pro 至 X1 和 P1 系列打印机
- 连接 AMS 2 Pro 至 P2S 打印机
- 连接 AMS 2 Pro 至 A1 系列打印机
