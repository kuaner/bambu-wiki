---
path: zh/x1/maintenance/replace-the-ams-main-frame
title: "更换AMS主框架"
description: "介绍更换AMS主框架相关步骤"
tags: []
created: 2022-10-31T10:55:42.727Z
updated: 2026-02-09T08:13:45.713Z
source: https://wiki.bambulab.com/zh/x1/maintenance/replace-the-ams-main-frame
---

# AMS 主框架

AMS 主框架是安装在 AMS 内部的一个注塑件，AMS的主要部件都安装在这个主框架上面。

![](https://wiki.bambulab.com/x1/maintenance/replace-ams-main-frame/ams_main_frame_v3.jpg)

V3：强化版

## 什么时候更换

AMS 主框架发生物理损坏且影响使用时，需要更换。

## 工具和材料

新的AMS主框架，, H2.0 /H1.5 内六角扳手,  镊子

# 安全提示

> **重要提醒 ！**
>
> 在对AMS及其电子设备进行任何维护工作之前，请断开AMS与打印机的连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 如果您对本指南有任何疑问，请[点击这里提交工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)，我们将及时回复并为您提供所需的帮助。

# 操作指引

## 第 1 步 - 拆下 PTFE 管 （拆解）

打开AMS上盖， 按压AMS 五通按钮，解锁接头，然后从AMS背面拉出PTFE管。

|  |  |
| --- | --- |
|  |  |

## 第 2 步 - 取出干燥剂

取下 2 个盖子并取出干燥剂。

![](https://wiki.bambulab.com/x1/maintenance/replace-ams-main-frame/remove_the_cover.png)

## 第 3 步 - 取出AMS主框架组件

移除固定AMS主框架上2颗螺丝。

![](https://wiki.bambulab.com/x1/maintenance/replace-ams-main-frame/remove_2_screws.png)

按压五通组件上的按钮来将主框架后部完全提起来， 将主框架组件竖立放置在AMS底盖上，注意有电缆连接；

将485连接线和电源连接线从AMS电源板上断开，取出AMS主框架组件

|  |  |  |
| --- | --- | --- |
|  |  |  |

## 第 4 步 - 断开 11 根电缆

断开主板上连接器的所有电缆， 如果需要，请做一些标记或对连接拍照。

![](https://wiki.bambulab.com/x1/maintenance/repalce-ams-main-board/disconnect_11_cables.png)

## 第 5 步 - 拆下主板

拆下2颗螺丝，从4个卡扣中解锁主板，然后拆下主板。

![](https://wiki.bambulab.com/x1/maintenance/repalce-ams-main-board/install_the_ams_main_board.png)

## 第 6 步 - 拆下五通组件

按下按钮断开 4 根 PTFE 管，从卡扣中松开 3 根电缆，拧下 4 颗螺丝，然后卸下五通组件。

|  |  |  |
| --- | --- | --- |
|  |  |  |

## 第 7 步 - 拆下**主动/从动支撑套筒组件**

拆下 4 个从动套支撑套筒单元和 4 个主动支撑套筒单元。

|  |  |
| --- | --- |
|  |  |

## 第 8 步 - 移除 4 个上下料组件

拆下4颗螺丝，然后按压上下料组件两侧，拆下上下料组件。 以同样的操作拆除另外 3 个上下料组件。

|  |  |
| --- | --- |
|  |  |

## 第 9 步 -  移除2块RFID板

用镊子去除RFID板边上的UV胶。取下RFID板和连接线。

|  |  |
| --- | --- |
|  |  |

## **第10步 - 安装RFID板 (组装)**

将2块 RFID 板安装到安装槽内，确认安装到位，然后在原先用 UV 胶的位置，再次用 UV 胶或热熔胶将RFID板固定。

|  |  |
| --- | --- |
|  |  |

## 第11步 - **安装4个上下料**组件

将电缆和 PTFE 管穿过安装位置上的孔，将上下料组件安装到位，锁入4颗螺丝固定。

|  |  |  |
| --- | --- | --- |
|  |  |  |

## **第 12 步 -安装 AMS 主框架主动/从动支撑套筒组件**

安装 AMS 主框架主动支撑套筒组件，注意对齐齿轮位置，防止装反，然后安装支撑套筒组件。一共有四组，请依次安装。

|  |  |
| --- | --- |
|  |  |

## 第 13 步 - 安装 AMS 五通组件

将AMS五通组件安装到中框，并锁入4 颗螺丝，理好电缆走线，并依次连接 4 根 PTFE 管到五通组件。

|  |  |
| --- | --- |
|  |  |

## 第14 步 - 理线

如图所示，将线材根据整理入对应的卡扣位置

![](https://wiki.bambulab.com/x1/maintenance/replace-ams-main-frame/arrange_cables.png)

## 第15 步 - 安装AMS主板

安装AMS主板，确认主板有被装到4个卡扣位置内，锁入2颗螺丝。

![](https://wiki.bambulab.com/x1/maintenance/repalce-ams-main-board/install_ams_main_board.png)

## **第16 步 - 连接11根电缆**

现在，需要将11根电缆连接到AMS主板对应的连接器上，具体请参考以下图表。

![](https://wiki.bambulab.com/x1/maintenance/repalce-ams-main-board/connect_11_cables.png)

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **序号** | **连接对象** | **序号** | **连接对象** | **序号** | **连接对象** |
| 1 | 上下料组件1 | 5 | 五通组件（霍尔板） | 9 | 上下料组件3 |
| 2 | RFID 板1 | 6 | AMS电源板(供电) | 10 | RFID 板2 |
| 3 | 上下料组件2 | 7 | AMS电源板(BUS) | 11 | 上下料组件4 |
| 4 | 五通组件（测速） | 8 | 五通电机 |  |  |

## 第 17 步 - 安装AMS主框架组件

将AMS主框架组件装入AMS外壳，并将Bambu总线电缆和电源电缆连接到AMS电源板。

|  |  |
| --- | --- |
|  |  |

## 第 18 步 **- 固定AMS主框架**

将AMS主框架安装到位，然后锁入2颗螺丝固定。

![](https://wiki.bambulab.com/x1/maintenance/replace-ams-main-frame/remove_2_screws.png)

## 第19步 - 放入干燥剂

在2个干燥剂槽内放入专用的干燥剂，合上盖子。

![](https://wiki.bambulab.com/x1/maintenance/replace-ams-main-frame/remove_the_cover.png)

## 第 20 步 - 连接PTFE管

检查确认PTFE管硅胶支架与五通组件的料孔对齐，并从AMS后部推入PTFE管。装完后，拉动PTFE管，确认PTFE管已固定。

|  |  |
| --- | --- |
|  |  |

# 功能检查

1. 将 AMS 连接到打印机并打开电源，确认AMS菜单有显示；

![](https://wiki.bambulab.com/x1/maintenance/repalce-ams-main-board/ams_connected.png)

2. 检查SN和固件，连接成功后应该能正常显示固件版本和产品SN，如果发现新的固件则更新固件；

|  |  |
| --- | --- |
|  |  |

3. 将打印材料加载到 AMS 的所有料槽中，然后单击屏幕上的“进料”开始加载打印丝。检查上下料功能，1号料槽进完料后，点出2号料槽图标加载2号料槽的打印丝，以此类推，直至4个料槽都完成一次进料、退料的操作。

![](https://wiki.bambulab.com/x1/maintenance/replace-filament-hub/494px-load1.png)

![](https://wiki.bambulab.com/x1/maintenance/replace-filament-hub/485px-load234.png)

否则，检查所有电缆和 PTFE 管的连接后重试。如果故障仍然存在，请联系 Bambu Lab 服务团队以获得进一步帮助。
