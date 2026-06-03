---
path: zh/ams-ht/maintenance/replace-filament-retraction-assembly
title: "更换 AMS HT 退料回卷组件"
description: "本文介绍了如何更换 AMS HT 退料回卷组件"
tags: []
created: 2025-10-28T03:08:21.576Z
updated: 2025-11-17T01:49:13.448Z
source: https://wiki.bambulab.com/zh/ams-ht/maintenance/replace-filament-retraction-assembly
---

## 退料回卷组件

AMS HT 退料回卷组件包含一个电机和一个摇臂齿轮，位于中框上。在退料过程中，摇臂齿轮带动主轴旋转，将耗材拉回到料盘上。

![退料.png](https://wiki.bambulab.com/ams-ht/maintenance/replace-filament-retraction-assembly/%E9%80%80%E6%96%99.png)

## 何时更换

- 退料回卷组件损坏

## 所需工具和材料

- 新的退料回卷组件
- H 2.0 内六角扳手
- H 1.5 内六角扳手

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。
>
> 如果您对本指南有任何疑问，[*请联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)，我们将及时回复并为您提供所需的帮助。

## 移除旧的退料回卷组件

### 1. 移除背面料管

从 AMS HT 背面按压料管释放按钮，解锁接头，然后从 AMS HT 背面拉出料管。

![取出料管.jpg](https://wiki.bambulab.com/ams-ht/disassembly-and-assembly/%E5%8F%96%E5%87%BA%E6%96%99%E7%AE%A1.jpg)

### 2. 取下主从动支撑轴

首先需要拆下料槽的**从动支撑轴**和**主动支撑轴**，取出轴承套时，小心两端的轴承，避免丢失。

|  |  |
| --- | --- |
|  |  |

### 3. 取出中框

移除底部两颗螺丝（BT3\*8）。

![3.底壳螺丝.jpg =800x](https://wiki.bambulab.com/ams-ht/disassembly-and-assembly/3.%E5%BA%95%E5%A3%B3%E8%9E%BA%E4%B8%9D.jpg)

移除螺丝后缓慢向上拉动中框组件。

|  |  |
| --- | --- |
|  |  |

打开缝隙后向上提起中框组件，**注意有电缆连接，请勿暴力操作**。

![6分离.jpg =800x](https://wiki.bambulab.com/ams-ht/disassembly-and-assembly/6%E5%88%86%E7%A6%BB.jpg)

解锁插头卡扣，拔出前端屏幕连接线缆。

![9移除前线缆.jpg](https://wiki.bambulab.com/ams-ht/disassembly-and-assembly/9%E7%A7%BB%E9%99%A4%E5%89%8D%E7%BA%BF%E7%BC%86.jpg)

### 4. 拔出主板上的组件插头

在 AMS HT 主板上拔出退料回卷组件线缆的插头（下图序号1处）。  
![退料组件插头.jpg](https://wiki.bambulab.com/ams-ht/maintenance/replace-filament-retraction-assembly/%E9%80%80%E6%96%99%E7%BB%84%E4%BB%B6%E6%8F%92%E5%A4%B4.jpg)

### 5. 移除退料回卷组件

移除 2 颗摇臂盖固定螺丝（BT2\*5），上去取出摇臂盖。

|  |  |
| --- | --- |
|  |  |

捏住摇臂组件两侧，缓慢向上取出摇臂组件。

|  |  |
| --- | --- |
|  |  |

取出退料回卷电机 2 颗固定螺丝（M3\*5），然后向外侧移除电机。

|  |  |
| --- | --- |
|  |  |

## 安装新的退料回卷组件

### 1. 安装退料回卷组件

安装退料回卷电机。注意线缆需要朝向外侧，锁紧 2 颗固定螺丝（M3\*5）。

|  |  |
| --- | --- |
|  |  |

捏住摇臂组件两侧，将摇臂组件安装至槽内。

|  |  |
| --- | --- |
|  |  |

安装摇臂盖，并锁紧 2 颗摇臂盖固定螺丝（BT2\*5）。

|  |  |
| --- | --- |
|  |  |

### 2. 连接组件线缆插头

将退料回卷组件线缆的插头插回到 AMS HT 主板的对应接口（图示序号1处）。  
![退料组件插头.jpg](https://wiki.bambulab.com/ams-ht/maintenance/replace-filament-retraction-assembly/%E9%80%80%E6%96%99%E7%BB%84%E4%BB%B6%E6%8F%92%E5%A4%B4.jpg)

### 3. 安装中框

连接 AMS HT 前端屏幕线缆，连接完成后需要注意将线缆卡入理线槽内。

|  |  |
| --- | --- |
|  |  |

用手指勾住凸出的线缆，将中框组件安装至下盖组件内。

|  |  |
| --- | --- |
|  |  |

需要确保中框组件完全压入下壳组件且前后没有翘起的情况，安装底部两颗固定螺丝（BT3\*8）。

|  |  |
| --- | --- |
|  |  |

### 4. 安装主从动支撑轴

将主动支撑轴压入 AMS HT 前端槽内，直到听到“咔嗒”声，注意主动支撑轴黑色齿轮一端需要和中框组件内的黄色齿轮一端对齐。

![](https://wiki.bambulab.com/ams-ht/disassembly-and-assembly/2%E5%AE%89%E8%A3%85%E4%B8%BB%E5%8A%A8%E8%BD%B4.jpg)

将从动支撑轴压入中框组件内，直到听到“咔嗒”声。

![](https://wiki.bambulab.com/ams-ht/disassembly-and-assembly/%E4%BB%8E%E5%8A%A8%E8%BD%B4%E3%80%81.jpg)

> 注意：安装完成后可以手动转动**主动支撑轴和从动支撑轴**，需要确保旋转顺滑。

### 5. 插入料管

最后将料管从 AMS HT 尾部推入。装完后，拉动料管，确认料管已固定。

![](https://wiki.bambulab.com/ams-ht/disassembly-and-assembly/65%E6%8F%92%E6%96%99%E7%AE%A1.jpg)

## 功能验证

连接电源线，将 AMS HT 连接到打印机，打开电源，通过机器显示屏的操作，开始使用 AMS HT 上料和退料，如果能完成退料动作并且整个退料过程没有出现错误提示，则更换成功。

否则，请检查所有连接，然后重试。如果问题仍然存在，请联系 Bambu Lab 服务团队寻求进一步帮助。

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
