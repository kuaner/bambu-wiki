---
path: zh/r1/maintenance/replace-radiator-fan
title: "R1 液冷风扇更换指南"
description: ""
tags: []
created: 2026-10-27T07:26:38.302Z
updated: 2026-10-27T07:26:39.328Z
source: https://wiki.bambulab.com/zh/r1/maintenance/replace-radiator-fan
---

## 液冷风扇 Radiator Fan

![SLA078.png](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-radiator-fan/zh/sla078.png)

## 何时更换

1. 液冷风扇异响、停转。
2. 液冷风扇漏液。

## 所需工具和材料

- H2.0 内六角螺丝刀
- H1.5 内六角螺丝刀

## 安全提示

> 在对激光切割机及其电子设备（包括工具头线缆）进行任何维护前，请先关闭设备电源并断开电源连接，以防屏幕误触或电路短路造成额外的设备损坏与安全隐患。维护或排查故障前，请确认相关部件已冷却。

## 移除液冷风扇

### 步骤 1.移除整机后盖板

参照[前后盖板组更换指南](replace-front-rear-panel-set.md)中移除后盖板步骤，移除后盖板，无需移除前盖板。

### 步骤 2.放出水箱内的水

装回注水孔塞。

![image.png](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-radiator-fan/zh/image_4.png)

拉出水箱右侧排水管，先开排水管塞子，再打开水箱注水孔塞，等待水箱内液体排空，装回排水管塞子。

|  |  |
| --- | --- |
| image.png | image.png |

### 步骤 3.取出冷却模组

将水管夹的锁扣分别上下掰动，解锁水管夹。同样方法拆除另一个水管夹。

|  |  |
| --- | --- |
| image.png | PixPin_2026-08-10_14-28-36.webp |

拔出水箱侧排水管、液冷风扇侧水管，拔除困难时可以使用镊子尾部撬动水管辅助拔出。

> 初次拔出时可能较为困难，可以使用镊子尾部辅助拔出。
>
> 拔出水管时管内可能仍然剩余少量液体，请注意不要溅到设备内，如不慎溅到设备内部请及时擦干。如液体不慎溅到PCB板上，及时擦除液体并使用吹风机吹干水分并联系技术支持获取帮助。

|  |  |
| --- | --- |
| C9856.MP4_20260828_104457.webp | C9858.MP4_20260828_105044.webp |

剪断水箱控制板线缆扎带，拔除四根线缆（1.AP控制线、2.电源线、3.火焰传感器、4.火焰传感器）  
注意：3、4号插头有卡扣，需要按下卡扣后拔出。

|  |  |
| --- | --- |
| PixPin_2026-08-10_14-22-29.jpg | PixPin_2026-08-10_14-26-14.jpg |

使用 H2.0 内六角螺丝刀移除 6 颗冷却模组固定螺丝。

![PixPin_2026-08-11_10-56-00.jpg](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-radiator-fan/zh/pixpin_2026-08-11_10-56-00_1.jpg)

将冷却模组拉出。

> 注意：拉出冷却模组时请尽量保持模组水平，取出该组件后请勿歪斜或者倒置，组件内可能仍然有液体未排出。

![C0018.MP4_20260922_141237.webp](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-radiator-fan/zh/c0018.mp4_20260922_141237.webp)

> 如果您只是取出冷却模组，到此步骤已经完成。安装步骤请跳转到安装冷却模组。

### 步骤 4.移除水箱组件

断开水箱相关的四根连接线。1、3、4号插头有卡扣，需要按下卡扣后拔出。

![PixPin_2026-08-11_10-12-57.jpg](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-radiator-fan/zh/pixpin_2026-08-11_10-12-57.jpg)

使用 H2.0内六角螺丝刀移除图示 5 颗螺丝。

![PixPin_2026-08-11_10-05-47.jpg](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-radiator-fan/zh/pixpin_2026-08-11_10-05-47.jpg)

使用 H2.0内六角螺丝刀移除图示两颗螺丝。

![PixPin_2026-08-11_10-07-29.jpg](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-radiator-fan/zh/pixpin_2026-08-11_10-07-29.jpg)

解锁水管夹，从液冷风扇端断开水管。

![PixPin_2026-08-11_10-17-26.webp](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-radiator-fan/zh/pixpin_2026-08-11_10-17-26.webp)

### 步骤 5.移除液冷风扇

按下插头卡扣，断开液冷组件的三根连接线。

![PixPin_2026-08-11_10-20-10.jpg](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-radiator-fan/zh/pixpin_2026-08-11_10-20-10.jpg)

使用 H2.0 内六角螺丝刀移除图示四颗螺丝。

|  |  |
| --- | --- |
| PixPin_2026-08-11_11-07-56.jpg | PixPin_2026-08-11_11-07-33.jpg |

取下风扇罩，取出液冷风扇组件。

![PixPin_2026-08-11_11-10-35.webp](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-radiator-fan/zh/pixpin_2026-08-11_11-10-35.webp)

## 安装液冷风扇

### 步骤 1.安装液冷风扇

将新的液冷风扇装回冷却模组支架。

![PixPin_2026-08-11_11-12-52.webp](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-radiator-fan/zh/pixpin_2026-08-11_11-12-52.webp)

安装风扇罩。

![PixPin_2026-08-11_11-14-49.webp](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-radiator-fan/zh/pixpin_2026-08-11_11-14-49.webp)

使用 H2.0 内六角螺丝刀锁入 4 颗螺丝。

|  |  |
| --- | --- |
| PixPin_2026-08-11_11-07-56.jpg | PixPin_2026-08-11_11-07-33.jpg |

连接液冷风扇的三根线缆插头，**插头完全相同，没有顺序要求。**

![PixPin_2026-08-11_10-20-10.jpg](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-radiator-fan/zh/pixpin_2026-08-11_10-20-10_1.jpg)

### 步骤 2.安装水箱组件

连接水箱组件水管，并安装水管夹。

|  |  |
| --- | --- |
| PixPin_2026-08-11_10-35-54.webp | PixPin_2026-08-11_10-38-05.webp |

使用 H2.0 内六角螺丝刀锁入7颗螺丝固定水箱组件。

|  |  |
| --- | --- |
| image.png | image.png |

根据相应的颜色和插头型号，装回水箱连接插头。

![image.png](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-radiator-fan/zh/image_3.png)

### 步骤 3.安装冷却模组

将冷却模组装回，注意不要压到线缆和水管。

![image.png](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-radiator-fan/zh/image_1.png)

对齐安装孔位，锁入 6 颗螺丝固定。

![PixPin_2026-08-11_10-56-00.jpg](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-radiator-fan/zh/pixpin_2026-08-11_10-56-00.jpg)

根据插头颜色和型号，连接冷却组件转接板插头。

![image.png](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-radiator-fan/zh/image_2.png)

连接水管，安装水管夹。

> 注意：安装水管时，请将水管推动到接头最底部，并用力锁紧水管夹。

![PixPin_2026-08-11_11-17-52.jpg](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-radiator-fan/zh/pixpin_2026-08-11_11-17-52.jpg)

将排水管装回固定位置。

![image.png](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-radiator-fan/zh/image_10.png)

### 步骤 4.安装整机后盖板

装回后盖板。

![PixPin_2026-08-06_16-09-40.webp](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-radiator-fan/zh/pixpin_2026-08-06_16-09-40.webp)

使用 H2.0 内六角螺丝刀分别锁入图示 13 颗螺丝固定后盖板。

|  |  |
| --- | --- |
| PixPin_2026-08-04_12-06-05.jpg | rear screws from the bottom.png |

安装注水口塞。

![image.png](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-radiator-fan/zh/image_9.png)

将线缆插头对齐安装孔位，使用 H1.5 内六角螺丝刀，锁入两颗螺丝固定。

![PixPin_2026-08-04_12-18-02.jpg](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-radiator-fan/zh/pixpin_2026-08-04_12-18-02.jpg)

装好排烟风扇安装座，注意风扇座方向，使用 H2.0内六角螺丝刀锁入四颗螺丝固定。

|  |  |
| --- | --- |
| PixPin_2026-08-04_12-21-59.webp | PixPin_2026-08-04_12-14-40.jpg |

连接风扇插头，整理风扇线缆。将风扇对齐安装位置，逆时针转动风扇，直到听到咔哒一声。

![PixPin_2026-08-06_15-50-13.webp](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-radiator-fan/zh/pixpin_2026-08-06_15-50-13.webp)

### 步骤 5.重新加入冷却液

参照[R1 冷却液更换教程](coolant.md)重新加入冷却液，如果使用环境温度较低还需要配比防冻液，以免冷却液结冰损坏设备。

## 所涉及到的螺丝（非必要）

更多关于螺丝相关内容介绍可参考 [Bambu Lab 常见螺钉](../../knowledge-sharing/common-screws.md)。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
