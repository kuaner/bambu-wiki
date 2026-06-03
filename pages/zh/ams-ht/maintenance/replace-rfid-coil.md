---
path: zh/ams-ht/maintenance/replace-rfid-coil
title: "更换 AMS HT RFID 线圈"
description: "本文将详细为您介绍更换 AMS HT RFID 线圈的详细步骤和注意事项"
tags: []
created: 2025-10-28T02:40:41.078Z
updated: 2025-11-17T03:00:53.726Z
source: https://wiki.bambulab.com/zh/ams-ht/maintenance/replace-rfid-coil
---

## RFID 线圈

AMS HT 中配备了 RFID 线圈，通过它可以识别 Bambu Lab 官方耗材上的 RFID 标签，还可以通过它实现耗材余量估算、自动续料等功能。

|  |  |
| --- | --- |
|  |  |

## 适用机型

AMS HT

## 何时更换

RFID 线圈的线缆断连或者线圈损坏

## 所需工具和材料

- 新的 RFID 线圈
- H 2.0 内六角扳手
- H 1.5 内六角扳手

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 移除旧的 RFID 线圈

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

接下来，拔出 AMS HT 电源板上的信号连接线和电源连接线。

|  |  |
| --- | --- |
|  |  |

移除电源插座到主板连接线，移除绝缘橡胶套**抵住解锁扣**，拉出线缆接头。

|  |  |
| --- | --- |
|  |  |

### 4. 移除旧的 RFID 线圈

移除 RFID 固定螺丝（BT2\*5），缓慢向上拉出 RFID 线圈。

|  |  |
| --- | --- |
|  |  |

## 安装新的 RFID 线圈

### 1. 安装新的 RFID 线圈

将新的 RFID 线圈插入槽内，并锁紧固定螺丝（BT2\*5）。

|  |  |
| --- | --- |
|  |  |

### 2. 安装中框

如下图所示连接 1、2 号位的线缆。其中1号位为主板通讯线（14pin），2号位为主板电源线（2pin）。

![](https://wiki.bambulab.com/ams-ht/disassembly-and-assembly/58%E8%BF%9E%E6%8E%A5%E4%B8%A4%E4%B8%AA%E7%BA%BF%E7%BC%86.jpg)

将电源插座线缆插接在主板上并安装好绝缘橡胶套。  
![](https://wiki.bambulab.com/ams-ht/disassembly-and-assembly/59ac%E7%BA%BF%E7%BC%86.jpg)

> 注意：此处连接不区分正负极。

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

### 3. 安装主从动支撑轴

主动支撑轴压入 AMS HT 前端槽内，直到听到“咔嗒”声，注意主动支撑轴黑色齿轮一端需要和中框组件内的黄色齿轮一端对齐。

![](https://wiki.bambulab.com/ams-ht/disassembly-and-assembly/2%E5%AE%89%E8%A3%85%E4%B8%BB%E5%8A%A8%E8%BD%B4.jpg)

将从动支撑轴压入中框组件内，直到听到“咔嗒”声。

![](https://wiki.bambulab.com/ams-ht/disassembly-and-assembly/%E4%BB%8E%E5%8A%A8%E8%BD%B4%E3%80%81.jpg)

> 注意：安装完成后可以手动转动**主动支撑轴和从动支撑轴**，需要确保旋转顺滑。

### 4. 插入背面料管

最后将料管从 AMS HT 尾部推入。装完后，拉动料管，确认料管已固定。

![](https://wiki.bambulab.com/ams-ht/disassembly-and-assembly/65%E6%8F%92%E6%96%99%E7%AE%A1.jpg)

## 功能验证

连接电源线，将 AMS HT 连接到打印机，打开电源，放入耗材，通过打印机显示屏观察 HT 能否正常读取 RFID 耗材信息，若可以正常读取并且没有出现错误提示，则更换成功。

否则，请检查所有连接，然后重试。如果问题仍然存在，请联系 Bambu Lab 服务团队寻求进一步帮助。

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
