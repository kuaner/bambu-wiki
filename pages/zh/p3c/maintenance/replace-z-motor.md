---
path: zh/p3c/maintenance/replace-z-motor
title: "P3C Z 电机更换指南"
description: "本文主要介绍更换 P3C Z 电机的具体操作方法。"
tags: []
created: 2026-11-24T14:06:50.330Z
updated: 2026-11-24T14:06:50.330Z
source: https://wiki.bambulab.com/zh/p3c/maintenance/replace-z-motor
---

## Z 电机

简述：Z 电机是安装在打印机背部，用于驱动热床完成 Z 方向移动的电机。

![p3c_z_______-p3c_z_motor_replacement_guide-pixpin_2026-11-19_20-19-16.jpg](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-z-motor/zh/p3c_z_______-p3c_z_motor_replacement_guide-pixpin_2026-11-19_20-19-16.jpg)

## 何时更换

- 电机烧坏
- 经 Bambu Lab 技术支持确认需要更换 Z 电机

## 所需工具和材料

- H2.0 内六角扳手
- 热床滑块固定支架

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 移除 Z 电机

### 步骤 1. 下降并锁定热床

> 为了确定更换配件后，热床高度的同步，在开始进行产品拆装前，需要将热床下降到底部，并对滑块进行锁定，本指南是基于热床滑块已锁定的前提下进行的。

使用原厂开箱固定支架的螺丝或配件包装内的螺丝，通过 H2.0 内六角扳手将 4 颗螺丝锁入图示位置。

|  |  |
| --- | --- |
| p3c_z_______-p3c_z_motor_replacement_guide-pixpin_2026-11-19_21-29-36.jpg | p3c_z_______-p3c_z_motor_replacement_guide-pixpin_2026-11-19_21-30-13.jpg |

### 步骤 2. 移除背板与废料滑梯

您可以参考WIKI：[废料滑梯更换指南](replace-purge-chute.md)，移除背板及滑梯。

![p3c_z_______-p3c_z_motor_replacement_guide-image.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-z-motor/zh/p3c_z_______-p3c_z_motor_replacement_guide-image.png)

### 步骤 3. 移除 Z 电机

两个人操作，将打印机平稳侧放在桌面，使用 H2.0 内六角扳手移除 Z 惰轮盖；

|  |  |
| --- | --- |
| p3c_z_______-p3c_z_motor_replacement_guide-pixpin_2026-11-19_20-35-55.jpg | p3c_z_______-p3c_z_motor_replacement_guide-pixpin_2026-11-19_21-40-37.jpg |

用力将张紧器向弹簧压缩方向推，使皮带处于放松状态，然后将 Z 皮带从电机轴上取下；

|  |  |
| --- | --- |
| p3c_z_______-p3c_z_motor_replacement_guide-pixpin_2026-11-19_21-43-06.jpg | p3c_z_______-p3c_z_motor_replacement_guide-pixpin_2026-11-19_21-45-04.jpg |

使用 H2.0 内六角扳手移除 Z 电机 4 颗固定螺丝，随后在 MC 板端断开 Z 电机线缆，将线缆从线扣中松出后移除 Z 电机。

|  |  |
| --- | --- |
| p3c_z_______-p3c_z_motor_replacement_guide-pixpin_2026-11-19_21-48-20.jpg | p3c_z_______-p3c_z_motor_replacement_guide-pixpin_2026-11-19_21-50-30.jpg |

## 安装 Z 电机

### 步骤 1. 安装 Z 电机

保持 Z 电机线缆朝打印机背板方向，将 Z 电机对准底座螺丝孔装入，并使用 H2.0 内六角扳手先预锁入 1、2 号对角螺丝，再预锁入 3、4 号对角螺丝，最后再将 4 颗螺丝拧紧；

|  |  |
| --- | --- |
| p3c_z_______-p3c_z_motor_replacement_guide-pixpin_2026-11-19_21-55-33.jpg | p3c_z_______-p3c_z_motor_replacement_guide-pixpin_2026-11-19_21-53-55.jpg |

用力将张紧器向弹簧压缩方向推，使弹簧处于极限压缩状态，然后将 Z 皮带套入 Z 电机转轴；

|  |  |
| --- | --- |
| p3c_z_______-p3c_z_motor_replacement_guide-pixpin_2026-11-19_22-00-48.jpg | p3c_z_______-p3c_z_motor_replacement_guide-pixpin_2026-11-19_22-01-53.jpg |

将 Z 惰轮盖对准螺丝孔装到位，随后使用 H2.0 内六角扳手锁入 4 颗螺丝固定；扶起打印机正放在桌面，将 Z 线缆依序埋入内衬上的理线扣，最后将 Z 电机线缆接头连接到 MC 板端 Z 电机插座中。

|  |  |
| --- | --- |
| p3c_z_______-p3c_z_motor_replacement_guide-pixpin_2026-11-19_20-35-55-1.jpg | p3c_z_______-p3c_z_motor_replacement_guide-pixpin_2026-11-19_22-11-30.jpg |

### 步骤 2. 安装废料滑梯与背板

您可以参考WIKI：[废料滑梯更换指南](replace-purge-chute.md)，安装废料滑梯和背板。

![p3c_z_______-p3c_z_motor_replacement_guide-image-1.png](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-z-motor/zh/p3c_z_______-p3c_z_motor_replacement_guide-image-1.png)

### 步骤 3. 解锁热床

使用 H2.0 内六角扳手将 4 颗螺丝移除。

![p3c_z_______-p3c_z_motor_replacement_guide-pixpin_2026-11-19_21-29-36-1.jpg](https://public-cdn.bblmw.com/wiki/new/p3c/maintenance/replace-z-motor/zh/p3c_z_______-p3c_z_motor_replacement_guide-pixpin_2026-11-19_21-29-36-1.jpg)

## 功能验证

配置好打印机，运行一次热床自动调平的程序，通过即可。

## 所涉及到的螺丝（非必要）

更多关于螺丝相关内容介绍可参考 [Bambu Lab 常见螺钉](../../knowledge-sharing/common-screws.md)。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
