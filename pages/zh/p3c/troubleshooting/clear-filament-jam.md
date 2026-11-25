---
path: zh/p3c/troubleshooting/clear-filament-jam
title: "P3C 进料失败排查指南"
description: ""
tags: []
created: 2026-11-24T14:06:13.429Z
updated: 2026-11-24T14:06:13.429Z
source: https://wiki.bambulab.com/zh/p3c/troubleshooting/clear-filament-jam
---

## 介绍

P3C 的送料路径中经过了多根料管以及气动接头，当耗材断裂后卡在转接部分时，可能导致进料过程受阻。此外，料管和气动接头之间如果存在安装间隙，也可能导致进料受阻。

## 所需工具

- H2.0 内六角扳手
- 一段较长的耗材

## 观察耗材进料过程

手动向内推入耗材，从设备侧面观察耗材卡在进料路径的哪一部分。

### 耗材无法送出AMS

耗材无法送出 AMS 的原因，通常是料管未安装到位，或存在断料堵塞。

1. 向气动接头内部轻推料管，确保料管安装到位。

|  |  |
| --- | --- |
| image.png | image.png |

2. 2/6 号槽位的气动接头与料管存在一定角度，因此气动接头可能产生轻微偏移。只需多尝试几次推入耗材，并晃动该处料管即可成功进料。

![image.png](https://public-cdn.bblmw.com/wiki/new/p3c/troubleshooting/clear-filament-jam/zh/image_6.png)

3. 耗材堵塞在该处时，可按压气动接头，取下料管，从底部插入一截耗材进行疏通。

![PixPin_2026-11-17_17-49-45.webp](https://public-cdn.bblmw.com/wiki/new/p3c/troubleshooting/clear-filament-jam/zh/pixpin_2026-11-17_17-49-45.webp)

### 耗材无法送出料管支架滑块

1. 料管支架滑块两端采用气动接头与料管连接。

![image.png](https://public-cdn.bblmw.com/wiki/new/p3c/troubleshooting/clear-filament-jam/zh/image_2.png)

轻推料管，确保料管安装到位。

|  |  |
| --- | --- |
| image.png | image.png |

2. 按压气动接头压块，取下后侧的料管。

![image.png](https://public-cdn.bblmw.com/wiki/new/p3c/troubleshooting/clear-filament-jam/zh/image.png)

向料管支架滑块插入一截耗材，疏通断料堵塞。

![PixPin_2026-11-17_18-21-42.webp](https://public-cdn.bblmw.com/wiki/new/p3c/troubleshooting/clear-filament-jam/zh/pixpin_2026-11-17_18-21-42.webp)

断料进入打印头料管后，再参考后文进行处理。

3. 若无法推出断料，可参考[AMS 料管支架滑块更换指南](../../ams3p/maintenance/replace-ptfe-tube-bracket-slider.md) 拆下该组件进行清理。

### 耗材无法送入打印头组件

1. 若断料卡在打印头料管中，可**按压住两侧料管卡扣，先向下按压料管，再将料管向外拔出，使用一截较长的耗材捅出断料。**

|  |  |
| --- | --- |
| image.png | image.png |

2. 若耗材已经进入打印头组件，但设备依然提示“未进料”，请参考[打印头进料霍尔排查指南](../../h3c/troubleshooting/filament-sensor-test.md)进行故障排查。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
