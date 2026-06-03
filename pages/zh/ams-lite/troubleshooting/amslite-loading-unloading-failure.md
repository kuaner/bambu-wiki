---
path: zh/ams-lite/troubleshooting/amslite-loading-unloading-failure
title: "AMS lite 进退料失败故障排查"
description: "本章节将为您详细讲解 AMS lite 进退料失败的原因和故障排除方法。"
tags: []
created: 2025-06-10T01:49:24.509Z
updated: 2025-06-16T03:45:36.355Z
source: https://wiki.bambulab.com/zh/ams-lite/troubleshooting/amslite-loading-unloading-failure
---

本文详述了 AMS lite 进退料故障的排查和解决方案。当您在使用打印机过程中遇到进退料失败的情况，可以根据打印机显示的错误信息及具体故障表现，参照本文提供的指南进行问题诊断与处理。

鉴于内容较为详细，您可以直接依据打印机的具体报错信息，选择相应部分进行阅读和操作。

- [耗材送往挤出机失败](#%E9%80%81%E5%BE%80%E6%8C%A4%E5%87%BA%E6%9C%BA)
- [耗材挤出异常](#intro)
- [耗材退出工具头失败](#%E9%80%80%E5%87%BA%E5%B7%A5%E5%85%B7%E5%A4%B4)
- [无法检查工具头内部的耗材位置](#%E8%80%97%E6%9D%90%E4%BD%8D%E7%BD%AE)

## 耗材送往挤出机失败

出现此报错信息：说明在送料过程中，挤出机霍尔传感器持续未检测到耗材。

![送往失败、.png](https://wiki.bambulab.com/ams/ams-lite/troubleshooting/%E9%80%81%E5%BE%80%E5%A4%B1%E8%B4%A5%E3%80%81.png)

故障排查流程：

![耗材送往挤出机失败.png](https://wiki.bambulab.com/ams/ams-lite/troubleshooting/%E8%80%97%E6%9D%90%E9%80%81%E5%BE%80%E6%8C%A4%E5%87%BA%E6%9C%BA%E5%A4%B1%E8%B4%A5.png)

### 1. 耗材打结

耗材缠绕可能导致输送失败，请检查料盘是否存在缠绕或卡滞现象。

|  |  |
| --- | --- |
| 缠绕 | 卡滞 |

### 2. 输送距离超限

AMS lite 最大有效输送距离为 **1.2** 米。若输送达到该距离后挤出机霍尔传感器仍未检测到耗材，就会报错耗材送往挤出机失败。

![](https://wiki.bambulab.com/ams/ams-lite/troubleshooting/image-7.png)

### 3. 入料口组件的里程轮卡涩

若某个槽相比其他槽明显阻力过大：

1. 检查对应槽位上下料器齿轮是否存在料屑残留，需及时清理
2. 测试里程轮转动状态：插入耗材进行往复拉动，观察转动是否顺畅，如发现明显阻力，建议您更换[入料口组件。](../../ams/maintenance/ams-lite-filament-funnel.md)  
   。

|  |  |
| --- | --- |
| 里程轮存在卡涩 | 正常里程轮 |

### 4. 耗材直径过细导致齿轮打滑

AMS Lite 的每个槽都配有一个入料口组件。入料口组件中的齿轮会挤压耗材，并在有刷电机的驱动下将耗材送入或拉出工具头，如下图所示：

![](https://wiki.bambulab.com/ams/ams-lite/troubleshooting/image.png)

当耗材过细或齿轮损坏时，齿轮与耗材的间距变大，导致齿轮打滑，最终引发进进退料失败。可以参考以下Wiki进行故障排查：

[AMS1 有刷电机1打滑，可能挤出轮磨损或料线过细](https://wiki.bambulab.com/zh/a1/troubleshooting/hmscode/1200_1200_0001_0001)

### 5. 挤出机传感器异常

如果每个槽位都出报错的情况，建议优先检查挤出机传感器。手动插入耗材后，观察屏幕上是否挤出机位置是否显示绿点。

|  |  |
| --- | --- |
| 插入耗材 | 挤出机亮绿点 |

![测试.webp](https://wiki.bambulab.com/ams/ams-lite/troubleshooting/%E6%B5%8B%E8%AF%95.webp)

检测不到耗材时，除了霍尔传感器本身可能存在问题外，还可能是底座摇臂问题。插入一段耗材，观察摇臂是否正常运作，取出耗材后是否会自动归位。

参考Wiki：[A1 系列五通组件拆解与清理](../../a1/maintenance/filament_hub_cleaning.md)

![](https://wiki.bambulab.com/ams/ams-lite/troubleshooting/image-3.png)

![摇臂.webp](https://wiki.bambulab.com/ams/ams-lite/troubleshooting/%E6%91%87%E8%87%82.webp)

### 6. 五通内部有断料

如果断料位于五通的出口处，当另外一个槽进料时，两根耗材堵在五通出口无法送，从而导致工具头霍尔检测不到耗材。可以参考以下 Wiki 清理五通：

[A1 系列五通组件拆解与清理](../../a1/maintenance/filament_hub_cleaning.md)

![](https://wiki.bambulab.com/ams/ams-lite/troubleshooting/image-4.png)

## 耗材挤出异常

出现此报错信息，说明在送料过程中，挤出机霍尔传感器检测到耗材，但挤出机无法咬合上耗材并挤出，或者对应槽位的里程轮未转动。

![](https://wiki.bambulab.com/ams/ams-lite/troubleshooting/img_v3_02k8_95326f0b-b4fa-4a28-9ee6-362f4df2d5dg.jpg)

**故障排查流程：**

![耗材挤出异常.png](https://wiki.bambulab.com/ams/ams-lite/troubleshooting/%E8%80%97%E6%9D%90%E6%8C%A4%E5%87%BA%E5%BC%82%E5%B8%B8.png)

### 1. 喷嘴堵塞或挤出机堵塞

如果将工具头移动到吐料组件位置，单独测试挤出，仍然无法顺利挤出耗材丝，通常可以观察到挤出机齿轮转动不顺畅且不停发出“咔哒”声，这可能是喷嘴堵塞了。

在打印机的“设置——维护”页面，启用维护模式。将喷嘴温度设置至170℃（最低可挤出温度），并手动测试挤出：

![a1-维护模式.jpg](https://wiki.bambulab.com/a1-screen-operation/a1-%E7%BB%B4%E6%8A%A4%E6%A8%A1%E5%BC%8F.jpg)

如果在没有喷嘴时，挤出机能顺利挤出耗材丝，说明是喷嘴堵塞了。参考以下Wiki清理：

[A1 系列打印机喷嘴堵塞清理](../../a1-mini/troubleshooting/nozzle-clog.md)

如果在没有喷嘴时，挤出机仍然无法挤出耗材丝，说明是挤出机堵塞了。参考以下Wiki清理：

[A1 系列挤出机清理](../../a1-mini/troubleshooting/extruder-clog.md)

### 2. 挤出机齿轮或电机异常

如果喷嘴和挤出机并未堵塞，但挤出机齿轮转动异常或停止转动，导致打印过程中无法顺利挤出耗材丝。可以拆开挤出机，检查挤出电机是否顺利转动，黄色齿轮是否有磨损或缺齿。

![](https://wiki.bambulab.com/ams/ams-lite/troubleshooting/%E6%A3%80%E6%9F%A5%E6%8C%A4%E5%87%BA%E7%94%B5%E6%9C%BA1.gif)

### 3. 耗材太细导致在挤出机打滑或挤出机未正确安装

如果在进料或打印过程中，耗材丝完全无法挤出，但挤出机齿轮能够顺畅转动，则可能是挤出机齿轮未完全咬合住耗材，或者齿轮与耗材打滑了。

![](https://wiki.bambulab.com/ams/ams-lite/troubleshooting/%E7%A9%BA%E6%89%93%E7%A4%BA%E6%84%8F.gif)

#### 齿轮和耗材打滑

耗材丝可能被磨损。  
首先，关闭打印机电源。接着，按下切刀以切断耗材。然后，按住压紧轮并将当前的耗材取出。检查取出的耗材，确认是否存明显磨损的迹象。

|  |  |
| --- | --- |
|  |  |

![](https://wiki.bambulab.com/ams/ams-lite/troubleshooting/image-12.png)

如果有，说明是耗材被齿轮磨损了。

尝试用另一卷耗材进料，观察是否能顺利挤出：

- 如果任何耗材都只能看到齿轮空转，而无耗材挤出，参考[喷嘴堵塞](../../a1-mini/troubleshooting/nozzle-clog.md)的排查方法，检查喷嘴是否堵塞。
- 如果只有某一卷耗材容易被磨损，可能是耗材本身问题，建议更换其他耗材打印。

#### 挤出机未正确安装

如果喷嘴未堵塞，且耗材未被齿轮磨损，但挤出时齿轮始终空转，可能是挤出机从动轮安装不当，齿轮间隙过大，无法咬合住耗材。

![](https://wiki.bambulab.com/ams/ams-lite/troubleshooting/image-13.png)

![](https://wiki.bambulab.com/ams/ams-lite/troubleshooting/image-14.png)

### 4. 里程轮阻力过大或失效

如果只有一个槽出现此报错，可能是对应槽上的里程轮阻力过大或失效。

#### 里程轮阻力过大

里程轮阻力过大会导致挤出机无法顺畅拉动耗材，里程轮也无法正常转动。将耗材插入 AMS lite 的四个插槽中，手动前后拉动耗材，检查经常报错的槽位是否拉动阻力明显大于其它槽，如下方动图所示，阻力大时里程轮转动困难。

|  |  |
| --- | --- |
| 里程轮存在卡涩 | 正常里程轮 |

#### 里程轮本身失效

如果仅有一个槽出现挤出失败，且对应槽位里程轮未存在阻力，耗材已挤出。  
在使用 AMS lite 进料时，是否成功挤出是由里程轮判断的，如果里程轮未正常记录送出长度，就会报错。建议您更换[入料口组件](../../ams/maintenance/ams-lite-filament-funnel.md)。

### 5. 缠料模块霍尔值异常

由于当前版本缠料检测与挤出异常共用一个报错信息，当缠料模块损坏时，也可能导致挤出异常。可以关闭缠料检查，观察是否报错。如果不再报错，则需要更换霍尔传感器。

![a1-打印选项.jpg](https://wiki.bambulab.com/ams/ams-lite/troubleshooting/a1-%E6%89%93%E5%8D%B0%E9%80%89%E9%A1%B9.jpg)

### 6. 五通磨损

如果五通磨损，会导致耗材挤不出来或卡在喷嘴上。请参考以下Wiki检查五通十字架是否磨损，如果五通十字架磨损严重，建议您更换五通组件：

[A1 系列五通组件拆解与清理](../../a1/maintenance/filament_hub_cleaning.md)

![](https://wiki.bambulab.com/ams/ams-lite/troubleshooting/image-16.png)

## 耗材退出工具头失败

出现此报错信息：说明当AMS lite退料或换料时，耗材应从工具头中退出，工具头霍尔传感器应检测到耗材退出，但霍尔传感器仍检测到耗材。

![](https://wiki.bambulab.com/ams/ams-lite/troubleshooting/img_v3_02k8_28066175-19f9-4794-a78b-0145e4c877bg.jpg)

故障排查流程：

![退出失败3.png](https://wiki.bambulab.com/ams/ams-lite/troubleshooting/%E9%80%80%E5%87%BA%E5%A4%B1%E8%B4%A53.png)

### 1. 检查五通、霍尔板底座和挤出机内部是否存在断料。

请参考以下 Wiki 指南检查五通及霍尔板底座内部是否有断料残留。如发现断料，请使用镊子将其清除：

[A1 系列五通组件拆解与清理](../../a1/maintenance/filament_hub_cleaning.md)

![](https://wiki.bambulab.com/ams/ams-lite/troubleshooting/image-17.png)

关闭打印机电源。接着，按下切刀以切断耗材丝。然后，按住压紧轮并将当前的耗材取出。如果无法拔出，说明挤出机堵塞，请参考Wiki清理挤出机：[A1 清理挤出机](../../a1-mini/troubleshooting/extruder-clog.md)

|  |  |
| --- | --- |
|  |  |

![](https://wiki.bambulab.com/ams/ams-lite/troubleshooting/image-26.png)

### 2. 检查挤出机霍尔传感器是否异常

观察挤出机在无耗材状态下，指示灯是否仍保持常亮。

![](https://wiki.bambulab.com/ams/ams-lite/troubleshooting/image-18.png)

若未装载耗材时绿灯持续亮起，请参考 Wiki 检查底座摇臂的复位功能是否正常。

[A1 系列五通组件拆解与清理](../../a1/maintenance/filament_hub_cleaning.md)

![](https://wiki.bambulab.com/ams/ams-lite/troubleshooting/image-19.png)

![](https://wiki.bambulab.com/ams/ams-lite/troubleshooting/20241212190114_rec_-1.gif)

### 3. 验证上下料组件齿轮安装方向是否正确

请按以下Wiki指引拆解上下料组件，并校准齿轮安装方位：

[AMS lite 上下料组件拆装指引](../../../en/ams/maintenance/ams-lite-feeder.md)

**槽1和槽2的正确方向**

![摇臂.png](https://wiki.bambulab.com/ams/ams-lite/troubleshooting/%E6%91%87%E8%87%82.png)

![](https://wiki.bambulab.com/ams/ams-lite/troubleshooting/image-21.png)

**槽3和槽4的正确方向**

![](https://wiki.bambulab.com/ams/ams-lite/troubleshooting/image-22.png)

![](https://wiki.bambulab.com/ams/ams-lite/troubleshooting/image-23.png)

## 无法检查工具头内部的耗材位置

出现此报错信息：说明当发起进料或退料流程时，挤出机的霍尔传感器检测到工具头内部仍有耗材，但未能成功判断耗材来自哪个槽。检测过程通过挤出和拉回耗材结合里程轮数据进行判断。如果检测失败，说明工具头内的耗材无法正常挤出或退出工具头。

![](https://wiki.bambulab.com/ams/ams-lite/troubleshooting/img_v3_02k9_2f04116e-e398-47a1-a07d-309641d725dg.jpg)

故障排查流程：  
![耗材位置检测失败1.png](https://wiki.bambulab.com/ams/ams-lite/troubleshooting/%E8%80%97%E6%9D%90%E4%BD%8D%E7%BD%AE%E6%A3%80%E6%B5%8B%E5%A4%B1%E8%B4%A51.png)

### 1. 挤出机堵塞

关闭打印机电源。接着，按下切刀以切断耗材丝。然后，按住压紧轮并将当前的耗材取出。如果无法拔出，说明挤出机堵塞，请参考Wiki清理挤出机：[清理挤出机](../../a1-mini/troubleshooting/extruder-clog.md)

|  |  |
| --- | --- |
|  |  |

![](https://wiki.bambulab.com/ams/ams-lite/troubleshooting/image-26.png)

### 2. 耗材在工具头中打滑

检查工具头侧面的螺丝是否拧紧。

![](https://wiki.bambulab.com/ams/ams-lite/troubleshooting/image-27.png)

如果螺丝已拧紧，尝试更换其他耗材测试。如果只有特定耗材出现问题，可能是耗材直径过细。

如果所有耗材都会出现这个问题，并且使用外挂耗材打印也会出现挤出问题，可能是挤出机本身打滑，建议您参考此 [Wiki](../../a1-mini/troubleshooting/extruder-clog.md) 打开挤出机检查是否出现损坏。

### 3. 里程轮打滑

如果仅在特定槽中**进料或者退料**时出现此错误，说明该槽的入料口组件内部里程轮打滑。建议您更换[入料口组件。](../../ams/maintenance/ams-lite-filament-funnel.md)

|  |  |
| --- | --- |
| 里程轮存在卡涩 | 正常里程轮 |

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南并未解决您的问题，[*请点击此处联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
