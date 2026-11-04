---
path: zh/h3c/maintenance/replace-printtool
title: "打印头组件更换指南"
description: "本文介绍了如何更换打印头组件。"
tags: []
created: 2026-11-03T12:36:56.980Z
updated: 2026-11-03T12:37:21.874Z
source: https://wiki.bambulab.com/zh/h3c/maintenance/replace-printtool
---

## 打印头组件

由打印头基座、热端和 FEP 组成，由热端加热耗材并与工具头的挤出单元协同配合可完成耗材挤出，从而实现模型的打印。  
![451.jpeg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-printtool/451.jpeg)

## 何时更换

- 用户购买了新的打印头组件

## 工具和材料

- H2.0 内六角扳手
- H1.5 内六角扳手

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。
>
> ![001.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-printtool/zh/001.jpg)

> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作。如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 移除打印头组件

### 第 1 步 移除 AMS 舱体

> 1. 如果只是拆装靠近左右两侧的打印头组件，可以只移除 AMS 的左(右)侧板而不移除 AMS 舱体进行操作。
> 2. 注意：在移除或安装 AMS 舱体前，请先执行退料操作，并取出舱内的所有料盘。若未退料，残留的耗材可能在安装时被夹断或卡住，导致后续进退料困难；同时，料盘的自重也会增加操作难度。
>
> |  |  |
> | --- | --- |
> | 002.jpg | 003.jpg |

请参考 [AMS 舱体拆装指南](replace-chamber.md)，将 AMS 舱体从 AMS 支架上移除。

![004.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-printtool/zh/004.jpg)

### 第 2 步 移除 打印头组件

按压 6-pin 线缆插头进行解锁并断开连接。

![005.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-printtool/zh/005.jpg)

将 6-pin 线从 4 个卡扣上松出，并将 6-pin 插头穿到与打印头组件同侧。

![006.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-printtool/zh/006.jpg)

向前滑动料管支架滑块，露出气动接头。然后按压气动接头，将料管从滑块上断开。

![007.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-printtool/zh/007.jpg)

用手握住打印头组件的上部，斜向上提起，卸载打印头组件。

![008.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-printtool/zh/008.jpg)

### 第 3 步 移除料管和热端 （更换打印头基座时适用）

按压气动接头支架两侧进行解锁，拔出料管，然后将料管从卡扣及橡胶圈上松出，移除料管。

- 按压两侧料管卡扣，**先向下按压料管**，再将料管向外拔出；

|  |  |  |
| --- | --- | --- |
| 009.png | 010.webp | 011.jpg |

用 H1.5 内六角扳手按下图标记的顺序移除 3 颗螺丝，然后拔出热端。

|  |  |
| --- | --- |
| 012.jpg | 013.jpg |

## 安装打印头组件

### 第 1 步 安装热端和料管（更换打印头基座时适用）

如下图，根据定位柱将热端安装到打印头基座上。

|  |  |
| --- | --- |
| 014.jpg | 015.jpg |

将热端按压到位后，锁入 3 颗螺丝固定。

![016.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-printtool/zh/016.jpg)

锁入 3 颗螺丝的顺序可参考下图的标记。

![017.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-printtool/zh/017.jpg)

将料管穿过线缆上的橡胶圈并连接到打印头组件的气动接头上，同时，料管要卡到线缆的卡扣上。

|  |  |
| --- | --- |
| 018.jpg | 019.jpg |

调整 3 个橡胶圈的位置，使各个固定料管位置之间的距离均约为 60 毫米。

![020.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-printtool/zh/020.jpg)

### 第 2 步 安装打印头组件

将打印头收回到打印机腔体内，先对齐橙色安装导向槽，然后顺着磁铁吸附到位，放置到挂架上。

|  |  |
| --- | --- |
| 021.jpg | 022.jpg |

向前移动滑块，将料管连接到料管支架上。

![023.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-printtool/zh/023.jpg)

将 6-pin 线插头穿到另一侧，并将线缆固定到卡扣上。（注意实心橙标位置需要在卡扣的附近）

![024.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-printtool/zh/024.jpg)

> 下图中右侧为橙色实心标记，可用于安装线缆时进行位置参考，标记在接近对应卡扣的范围即可。
>
> ![025.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-printtool/zh/025.jpg)

连接 6-pin 线，可通过 6-pin 线的位置是否对齐来判断线缆是否插到位。

![026.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-printtool/zh/026.jpg)

### 第 3 步 装回 AMS 舱体

参考 [AMS 舱体拆装指南](replace-chamber.md)，安装好 AMS 舱体。

![027.jpg](https://public-cdn.bblmw.com/wiki/new/h3c/maintenance/replace-printtool/zh/027.jpg)

## 功能验证

抓取更换的打印头组件并执行进退料操作，耗材能正常挤出和完成退料动作。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
