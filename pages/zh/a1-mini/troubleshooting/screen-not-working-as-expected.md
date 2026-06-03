---
path: zh/a1-mini/troubleshooting/screen-not-working-as-expected
title: "A1 mini -显示屏异常排查 "
description: "A1 mini 显示屏不亮、触摸功能失灵排查"
tags: ["黑屏", "触摸屏失灵", "刷新", "不开机"]
created: 2023-11-10T04:20:55.991Z
updated: 2025-06-16T09:09:51.562Z
source: https://wiki.bambulab.com/zh/a1-mini/troubleshooting/screen-not-working-as-expected
---

## 显示屏黑屏

### 问题现象

启动打印机，显示屏黑屏无显示。

![](https://wiki.bambulab.com/n1/troubleshooting/display-anomalies/%E6%98%BE%E7%A4%BA%E5%B1%8F%E9%BB%91%E5%B1%8F_blackscreen.jpg)

### 原因及解决方案

1. MicroSD 卡故障，需更换 MicroSD 卡；
2. 电源供电异常，需更换电源或电源连接线；
3. 主板供电异常，需检查主板的电源连接线；
4. 主板损坏，需更换主板；
5. 显示屏排线损坏，需更换连接排线；
6. 显示屏损坏，需更换显示屏；
7. 地线接触不良导致显示异常：如屏幕显示时好时坏、触摸操作不灵敏等现象，可能由于插座地线接触不良引起。建议检查供电插座的接地情况，确保地线连接良好。

### 安全和操作提示

在进行拆装作业时，需要确认打印机是断电状态。

### 所需的工具

- H2.0 内六角扳手
- 镊子
- 万用表（非必须）

### 排查指引

#### 一. 排查 MicroSD 卡

启动打印机后，若显示屏黑屏无显示，首先可排查 MicroSD 卡问题。

**注意事项：在进行以下操作前，请务必先关闭打印机电源**

1. 关闭打印机电源，并小心地从打印机中拔出 MicroSD 卡。
2. 重启打印机，观察显示屏是否能正常亮起。若显示屏在拔出 MicroSD 卡后能正常显示，那么请在关机状态下将 MicroSD 卡重新插入打印机，并再次开机以验证是否因 MicroSD 卡故障导致之前的黑屏问题。

![6058346d-2211-46bb-901a-046f2b09f9e3.png](https://wiki.bambulab.com/a1/a1mini-heating/6058346d-2211-46bb-901a-046f2b09f9e3.png)

#### 二. 检查打印机工作指示灯的状态

打印机开机状态下，若显示屏上方的工作指示灯白灯常亮，则表示打印机主板工作正常。灯亮则跳转第四步排查显示屏排线；灯不亮则继续第三步排查。

![](https://wiki.bambulab.com/n1/troubleshooting/display-anomalies/%E6%89%93%E5%8D%B0%E6%9C%BA%E5%B7%A5%E4%BD%9C%E6%8C%87%E7%A4%BA%E7%81%AF_working_status_light.jpg)

#### 三. 检查打印机电源和主板工作灯的状态

#### 断电并移除 A1 mini 底板

向后放倒打印机，用 H2.0 内六角扳手移除 2 颗螺丝 A，再移除 14 颗螺丝B，拉扯尼龙扎网使底板松动，移除底板。

|  |  |  |  |
| --- | --- | --- | --- |
|  |  |  |  |

##### 拆除底板后接通电源（请注意用电安全）

在拆开底板后，您可以将打印机再次接通电源，**但是在接通电源期间请不要触碰打印机任何部件，观察完打印机的指示灯状态后部请重新断电并拔出电源插头。**

![20250220-093125.png](https://wiki.bambulab.com/n1/troubleshooting/display-anomalies/20250220-093125.png)

##### 检查电源工作指示灯的状态

正常情况下电源工作状态灯是常亮绿灯的。如果此灯不亮说明电源供电异常，需更换电源或电源连接线。

![电源.jpg](https://wiki.bambulab.com/n1/troubleshooting/display-anomalies/%E7%94%B5%E6%BA%90.jpg)

##### 检查主板工作指示灯的状态

**正常情况下，MC 板指示灯每 5 秒闪 1 次绿光，AP 板指示灯每 1 秒闪烁 1 次绿光。**

###### 情形1：主板工作正常

如果 MC 板和 AP 板正常闪烁，说明主板处于正常状态，黑屏原因来源于显示屏或显示屏排线，请跳转至第三步。

![正常闪烁.jpg](https://wiki.bambulab.com/n1/troubleshooting/display-anomalies/%E6%AD%A3%E5%B8%B8%E9%97%AA%E7%83%81.jpg)

###### 情形2：主板工作异常

如果 MC 板和/或 AP 板灯闪烁异常，说明主板异常，可能是主板损坏或主板的电源连接线损坏。  
![异常闪烁.jpg](https://wiki.bambulab.com/n1/troubleshooting/display-anomalies/%E5%BC%82%E5%B8%B8%E9%97%AA%E7%83%81.jpg)

如果家中有万用表，可以尝试测量一下主板上这两端的电压是否为 0（非必须），这是主板的直流电源输入端，如果为0说明主板电源连接线可能有损坏。

![](https://wiki.bambulab.com/n1/troubleshooting/display-anomalies/%E4%B8%BB%E6%9D%BF%E7%94%B5%E5%8E%8B%E6%B5%8B%E9%87%8F_voltage_of_main_board.jpg)

#### 四. 检查显示屏排线

**注意事项：需要先关闭打印机电源**

在已经确认主板和电源能正常工作的情况下，可以尝试重新连接显示屏排线。请检查接口和PIN针有无异常，FPC排线有无损伤，如果排线有损伤请联系售后团队处理。

|  |  |
| --- | --- |

**如果以上步骤中发现了有明显损坏的组件（或是状态灯不亮），请您联系售后团队确认。**

## 显示屏触控异常

### 问题现象

启动打印机，显示屏可以正常显示，但是触控功能失灵

![](https://wiki.bambulab.com/n1/troubleshooting/display-anomalies/%E8%A7%A6%E6%8E%A7%E5%A4%B1%E7%81%B5_touch_screen_malfunction.gif)

### 原因及解决方案

A1 mini 内部的结构比较紧凑，可能受运输的影响，显示屏的连接出现了松动，需要重新连接显示屏排线。

### 所需的工具

- H2.0 内六角扳手
- 镊子

### 排查指引

#### 一. 关机断电

|  |  |
| --- | --- |

#### 二. 移除A1 mini 底板

向后放倒打印机，用H2.0内六角扳手移除2颗螺丝A，再移除14颗螺丝B，拉扯尼龙扎网使底板松动，移除底板。

|  |  |  |
| --- | --- | --- |

#### 三. 将USB-C上的磁环向上推

请尝试将磁环的位置向上推，使得磁环的两端分别靠着FPC座和下面的螺丝钉，从而不会压着中间的几颗芯片。

|  |  |
| --- | --- |

| 向上推磁环 |
| --- |

## 显示屏刷新异常

### 问题现象

机器下载切片文件过程中，显示画面卡顿。

![](https://wiki.bambulab.com/n1/troubleshooting/display-anomalies/%E5%88%B7%E6%96%B0%E5%BC%82%E5%B8%B8_refreshing_abnormal.gif)

### 原因及解决方案

机器处于下载切片文件的过程中，系统正全力处理下载任务，屏幕的刷新会变慢，出现显示画面卡顿的情况，是正常的，切片文件下载完成后会恢复正常。

## 结束语

> *我们希望本指南能为您提供有用的信息，帮助您解决问题。*
>
> *我们希望能确保您安全有效地进行操作。如果您对本指南描述的过程有任何疑虑或问题，建议您在开始操作前联系我们友好的客户服务团队。*  
> *我们随时准备为您解答疑问并提供帮助。[点击此处联系在线技术支持 （服务时间 9:00-21:00）](https://support.bambulab.cn/cn/im)*
