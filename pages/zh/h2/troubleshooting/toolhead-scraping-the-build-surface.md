---
path: zh/h2/troubleshooting/toolhead-scraping-the-build-surface
title: "H2D 工具头刮打印板故障排查指南"
description: "文章主要描述了当 H2D 的工具头刮擦打印板时如何排除故障"
tags: []
created: 2025-06-30T02:13:21.166Z
updated: 2025-07-21T02:28:58.336Z
source: https://wiki.bambulab.com/zh/h2/troubleshooting/toolhead-scraping-the-build-surface
---

## 故障描述

发起打印或者校准后，工具头上的部件剐蹭打印板导致打印板表面破损。该异常可能由多种原因造成，请根据下方描述尝试解决。

> 注意：请注意保留现场的图片，便于技术支持排查具体原因。例如您可以在打印时可以尽量插上 U 盘并开启录像，根据录像资料可以帮助技术支持人员更快速地排查问题。[点击此处可以了解开启录像的方法。](../../x1/troubleshooting/enable-the-video-recording-function.md)

## 可能原因

建议按照下列顺序依次进行排查。

### 一. 未正确安装热端夹扣

安装热端时夹扣未正确扣紧，导致热端实际上并没有被固定好，在挤出机挤出耗材的时候，热端被往下推动最终导致热端和热床之间的高度差异常而发生刮床。

![热端夹扣安装错误造成工具头刮打印板](https://wiki.bambulab.com/h2/troubleshooting/toolhead-scraping-the-build-surface/img_v3_02nh_155d250d-ae90-4ebe-8367-34c8a014a99g.png)

#### 如何判断

1. 刮床痕迹与喷嘴移动轨迹接近

![刮床痕迹.jpg](https://wiki.bambulab.com/h2/troubleshooting/toolhead-scraping-the-build-surface/%E5%88%AE%E5%BA%8A%E7%97%95%E8%BF%B9.jpg)

2. 摘掉硅胶套，观察夹扣的扣紧方式是否正确

|  |  |
| --- | --- |
| 热端夹扣未正确扣紧示例 | 热端夹扣正确扣紧示例 |

#### 解决方法

按照下面动图的操作用正确的方式重新扣紧热端。

![安装卡扣.gif](https://wiki.bambulab.com/h2/troubleshooting/toolhead-scraping-the-build-surface/%E5%AE%89%E8%A3%85%E5%8D%A1%E6%89%A3.gif)

### 二. 堵嘴片变形损坏

打印或者校准过程中，由于其他原因导致堵嘴片发生严重的变形，堵嘴片有可能会低于热端，从而在热端贴近热床移动过程中剐蹭打印版。

如下图为堵嘴片变形案例：  
![堵嘴片变形案例](https://wiki.bambulab.com/h2/troubleshooting/toolhead-scraping-the-build-surface/%E5%A0%B5%E5%98%B4%E7%89%87%E5%8F%98%E5%BD%A2.jpg)

#### 如何判断

1. 观察堵嘴片是否有严重变形，以至于低于热端底部；
2. 打印版上有许多细细的不规则的划痕

如下图中堵嘴片已变形且左边热端夹扣也安装错误：  
![刮痕2.jpg](https://wiki.bambulab.com/h2/troubleshooting/toolhead-scraping-the-build-surface/%E5%88%AE%E7%97%952.jpg)

#### 解决方法

请参考这个[链接](../maintenance/replace-flow-blocker.md)更换堵嘴片。

### 三. 热床不平

机器在出厂的时候都已进行热床调平，但是在运输过程中有的机器不可避免会受到颠簸而导致热床发生比较严重的倾斜。通常这不影响使用，只需要按照这个 [H2D 热床手动调平](../manual-bed-leveling.md)教程进行手动调平即可。

#### 如何判断

一般而言热床发生倾斜的时候会沿着 X 轴的方向发生旋转，这会导致靠近机箱门的一侧会比热床中心高，在打印机做自动调平（热床左下角）以及画预挤出线的时候（热床右下角）喷嘴会剐蹭到热床。

![前门刮伤1.jpg](https://wiki.bambulab.com/h2/troubleshooting/toolhead-scraping-the-build-surface/%E5%89%8D%E9%97%A8%E5%88%AE%E4%BC%A41.jpg)

#### 解决方法

1. 按照 [Wiki 教程](../manual-bed-leveling.md)进行一次手动调平
2. 后续固件会对此情况做保护，以确保即使没有做手动调平的情况下也不会对打印版造成损伤

### 四. 热端加热组件松动

加热组件（含加热底座、陶瓷底座）的螺丝如果没有锁紧，则会产生间隙，那么当挤出机开始挤出耗材的时候熔融耗材有可能会把整个加热组件往下推动，进而导致喷嘴距离热床太近而剐蹭打印板。

#### 如何判断

1. 剐蹭痕迹基本符合喷嘴移动轨迹。
2. 取下硅胶套确认喷嘴夹扣正确夹紧。
3. 取下热端确认锁紧加热组件的螺丝是否松动。

---

3.1 **锁紧陶瓷底座前后螺丝：**

- 首先拧松陶瓷底座固定螺丝（左侧4颗，右侧3颗），**若需要拆下左侧的加热组件，需要把左侧理线片的两颗螺丝一起取下，具体位置参照下图。**

![](https://wiki.bambulab.com/h2/troubleshooting/toolhead-scraping-the-build-surface/image.png)

- 随后适度拧紧加热组件背面的4颗螺丝，旋转幅度约为1/8圈。

> **注意：若发现螺丝已处于较紧状态，请勿强行继续拧紧，以免造成陶瓷底座损坏。**

![](https://wiki.bambulab.com/h2/troubleshooting/toolhead-scraping-the-build-surface/image-1.png)

![](https://wiki.bambulab.com/h2/troubleshooting/toolhead-scraping-the-build-surface/image-2.png)

- 重新安装左右陶瓷底座并锁紧固定螺丝。

3.2 **检查喷嘴的安装：**

- 安装时**向下按压喷嘴**后再扣紧夹扣，夹扣要按照正确的方式扣紧，确保无松动；
- 完成后手动摇晃喷嘴，检查是否牢固，若如下动图所示有明显晃动的话，则说明热端没有完全扣紧。

![dlh0bpluhowumcx5rzfcsiwin3f.gif](https://wiki.bambulab.com/h2/troubleshooting/toolhead-scraping-the-build-surface/dlh0bpluhowumcx5rzfcsiwin3f.gif)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南未解决您的问题，[*请联系在线技术支持（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
