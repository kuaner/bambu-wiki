---
path: zh/h3c/troubleshooting/clear-filament-jam
title: "拓竹H3C 与AMS料管中断裂耗材的清理"
description: ""
tags: []
created: 2026-11-03T12:07:11.841Z
updated: 2026-11-10T12:18:37.038Z
source: https://wiki.bambulab.com/zh/h3c/troubleshooting/clear-filament-jam
---

## 介绍

当送料路径的任一零件中存在耗材断料时，会导致 AMS 自动送料失败，需及时疏通该槽位，保证送料路径通畅。

## 所需工具

- H2.0 内六角扳手
- 一段较长的耗材

## 观察耗材进料过程

拆卸左右两侧的 AMS 磁吸侧板。

|  |  |
| --- | --- |
| 图 | 图 |

在屏幕上重新选择 AMS 进料。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/clear-filament-jam/zh/04_h3c_ams__________-03.png)

从侧面观察进料过程，若某一槽位提示进料失败，可先尝试《简单疏通》。

## 简单疏通

通过屏幕观察热端温度。若热端处于高温状态，请设置 0 ℃ 并等待降温结束。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/clear-filament-jam/zh/04_h3c_ams__________-04.png)

按压打印头上的黑色或橙色压块，向前轻推料管，再向外拔出。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/clear-filament-jam/zh/03_h3c___________-04.webp)

重启一次设备，确保AMS 将自动变为“空状态”。  
空状态：该状态下 AMS 不会咬合耗材，此时能够轻易手动插入耗材，可通过观察黄色进料导向块与黑色外壳的间距判断。

|  |  |
| --- | --- |
| 图 | 图 |

AMS 状态为“空”后，再次关闭打印机电源。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/clear-filament-jam/zh/04_h3c_ams__________-08.png)

打开 AMS，手动向内推入耗材。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/clear-filament-jam/zh/04_h3c_ams__________-09.png)

观察断料是否被顶出。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/clear-filament-jam/zh/04_h3c_ams__________-10.png)

若耗材被成功顶出，则问题解决，可继续使用设备。  
若耗材无法进入乳白色 PTFE 管，请检查 AMS 3H 以及料管导向组件。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/clear-filament-jam/zh/04_h3c_ams__________-11.png)

若耗材无法送出透明 FEP 管，请检查料管支架滑块是否堵塞。

|  |  |
| --- | --- |
| 图 | 图 |

## 全面排查

### 步骤一： 检查 AMS 3H 是否堵塞

开机后在屏幕上选择退出所有耗材。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/clear-filament-jam/zh/04_h3c_ams__________-14.png)

退料完成后 ，AMS 将自动变为“空状态”。确保 AMS 状态为 “空”后，关闭打印机电源。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/clear-filament-jam/zh/04_h3c_ams__________-08.png)

将料头固定在料盘侧孔中，取下所有耗材。

|  |  |
| --- | --- |
| 图 | 图 |

拧下 AMS 的 4 颗固定螺丝。

|  |  |
| --- | --- |
| 图 | 图 |

抱住 AMS 前后侧，取下 AMS。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/clear-filament-jam/zh/04_h3c_ams__________-20.png)

向入料口中插入一截耗材。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/clear-filament-jam/zh/04_h3c_ams__________-09.png)

观察断料是否从底部捅出。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/clear-filament-jam/zh/04_h3c_ams__________-22.png)

若耗材无法从底部送出，则斜向外侧拔下进料导向块。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/clear-filament-jam/zh/04_h3c_ams__________-23.png)

检查入料口中是否有断料，并尝试使用镊子清理。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/clear-filament-jam/zh/04_h3c_ams__________-24.png)

### 步骤二： 检查料管导向组件是否堵塞

先将料管支架滑块推向最后侧，再按压气动接头的黑色压块，拔出尾部的料管。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/clear-filament-jam/zh/04_h3c_ams__________-25.png)

插入一截耗材进入料管导向组件。

|  |  |
| --- | --- |
| 图 | 图 |

当耗材进入料管导向组件后，观察断料是否被捅出料管。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/clear-filament-jam/zh/04_h3c_ams__________-28.webp)

若内部存在堵塞，可参考[AMS 料管导向组件及料管连接件更换指南](../../ams3/maintenance/replace-ptfe-tube-guide-assembly.md)清理分岔料管连接件或直列料管连接件。  
若料管导向组件中没有断料，则继续排查。

### 步骤三： 检查料管支架滑块是否堵塞

按压打印头上的黑色压块，拔出打印头上的料管。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/clear-filament-jam/zh/03_h3c___________-04.webp)

插入一截耗材进入打印头料管。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/clear-filament-jam/zh/04_h3c_ams__________-30.png)

当耗材反向进入料管支架滑块后，观察断料是否被捅出滑块。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/clear-filament-jam/zh/04_h3c_ams__________-31.webp)

若滑块内部存在堵塞，可参考[AMS 料管支架滑块更换指南](../../ams3/maintenance/replace-ptfe-tube-bracket-slider.md)拉出滑块疏通或更换新滑块。

**若整个送料路径中都不存在断料堵塞，则可能是料管未完全插入气动接头，导致耗材卡在气动接头间隙中。可重新安装每段料管，并用力向内推压到极限。**  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/clear-filament-jam/zh/04_h3c_ams__________-32.png)

## 功能验证

开机后重新选择进料，若进料成功，则问题解决。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/troubleshooting/clear-filament-jam/zh/04_h3c_ams__________-33.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
