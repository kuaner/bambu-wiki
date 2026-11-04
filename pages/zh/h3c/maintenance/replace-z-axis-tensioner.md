---
path: zh/h3c/maintenance/replace-z-axis-tensioner
title: "Z轴张紧器 及 Z 皮带更换指南"
description: ""
tags: []
created: 2026-11-03T12:44:19.490Z
updated: 2026-11-03T12:48:30.501Z
source: https://wiki.bambulab.com/zh/h3c/maintenance/replace-z-axis-tensioner
---

## Z轴张紧器

Z 轴张紧器是安装在打印机底部，用于张紧 Z 轴皮带的零件。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-z-axis-tensioner/zh/66_z_______z________z_axis_tensioner_and_z_belt_replacement_guide_36bddbec53.jpg)

## 何时更换

- 张紧器惰轮异响，打油未能解决；
- 张紧器惰轮轴承损坏

## 工具和材料

- H2.0 内六角扳手
- 热床滑块固定支架

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> ![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-z-axis-tensioner/zh/01__________2012_toollock_motor_replacement_guide_01457bbe50.jpg)

> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 拆装提示

> 1. 顶部螺丝的拆装需要提前移除 AMS 3H，请参考 WIKI： [AMS 3H 拆除与安装指南](replace-ams3.md)，将 AMS 3H 从打印机上移除和重新安装，本指南的操作均在已移除 AMS 3H 的场景下进行。
> 2. 为了确定更换配件后，热床高度的同步，以开始进行产品拆装前，需要将热床下降到底部，并使用热床滑块固定支架锁定热床。本指南是基于热床滑块已锁定的前提下进行的。  
>    ![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-z-axis-tensioner/zh/12_z________z_motor_replacement_guide_fc554e7a4e.jpg)

> 注：我们后续将提供用于固定滑块的打印模型，有同等的效果。

## 移除 Z 轴张紧器 / Z 皮带

### 第 1 步 下降热床并锁定

启动打印机，执行一次回 XYZ 回零操作，然后在屏幕上点击下降热床的图标，将热床下降到底部。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-z-axis-tensioner/zh/12_z________z_motor_replacement_guide_4bdc3e292d.jpg)

使用固定热床支架，固定 3 个滑块，锁入 4 颗螺丝。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-z-axis-tensioner/zh/12_z________z_motor_replacement_guide_0d5524cc30.jpg)

### 第 2 步 侧放打印机

将打印机电源断开，然后两个人一起操作，将打印机侧放在平整的台面上。  
![图](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-z-axis-tensioner/zh/12_z________z_motor_replacement_guide_3248b91755.jpg)

### 第 3 步 将 Z 皮带从电机主动轮上松出

用 H2.0 内六角扳手拧松 1 圈张紧器螺丝，然后如图所示用手压紧 Z 皮带，使张紧弹簧处于完全压缩的状态，然后重新锁紧张紧螺丝，锁定弹簧的状态。

|  |  |
| --- | --- |
| 图 | 图 |

此时，Z 皮带处于完全松驰的状态，可以轻松将皮带从电机主动轮上松出并放置到前面的挡块上。

|  |  |
| --- | --- |
| 图 | 图 |

### 第 4 步 移除 Z 张紧器 / Z 皮带

缓慢拧松张紧螺丝，弹簧会进行释放。继续拧张紧螺丝直至取下。然后用H2.0 内六角扳手移除 4 颗螺丝，取下张紧器盖子。

|  |  |
| --- | --- |
| 图 | 图 |

这时，可以轻松取下张紧器和 Z 皮带。如果 Z 皮带有被同步轮卡住，直接拉扯皮带松出即可。

|  |  |
| --- | --- |
| 图 | 图 |

## 安装 Z 皮带/ Z 轴张紧器

### 第 1 步 放置 Z 皮带

如图所示放置 Z 皮带，注意 Z 皮带不能安装到 Z 电机主动轮上。

|  |  |
| --- | --- |
| 图 | 图 |

### 第 2 步 安装Z 轴张紧器

将 Z 轴张紧器带着张紧弹簧一起安装到张紧器的滑槽上，安装张紧器盖子，锁入 4 颗螺丝固定。

|  |  |
| --- | --- |
| 图 | 图 |

然后如图所示向上拉扯皮带，使张紧器弹簧处于完全压缩的状态，锁入张紧器螺丝进行固定。

|  |  |
| --- | --- |
| 图 | 图 |

### 第 3 步 将 Z 皮带安装到电机主动轮上

将 Z 皮带挂到电机主动轮上，缓慢拧松张紧螺丝，Z 皮带将会被张紧，保留张紧螺丝拧松 2 圈的状态。

|  |  |
| --- | --- |
| 图 | 图 |

### 第 4 步 解除热床锁定，拧紧张紧螺丝

用 H2.0 内六角扳手，移除固定支架的 4 颗螺丝，取下固定支架（尽量尝试保持侧放打印机的情况下移除，这样可以避免反复的调整打印机的放置方式）。往复拉动 Z 皮带 2~3 次，确认无异常，锁紧张紧螺丝，最后正放打印机。

|  |  |
| --- | --- |
| 图 | 图 |

## 功能验证

配置好打印机，运行一次热床自动调平的程序，通过即可。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
