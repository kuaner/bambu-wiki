---
path: zh/p1/maintenance/mc-board
title: "更换 P 系列主控板（MC 板）"
description: "拆装 P 系列打印机主控板的操作步骤"
tags: ["mc板", "主控板"]
created: 2023-07-11T17:04:01.553Z
updated: 2026-02-11T08:50:06.499Z
source: https://wiki.bambulab.com/zh/p1/maintenance/mc-board
---

## P 系列主控板

主控板即机器控制电路板，它是打印机运动部件的控制中心。P1P 和 P1S 使用同样的主控板，只是散热片有所不同。

|  |  |
| --- | --- |
| P1P | P1S |

请注意：我们提供的主控板是预装了 P1P 散热片的，用在 P1S 上时，可以根据自己的需求更换散热片，更换指引请参考本文的**补充内容**。

### 何时更换

- 正常供电情况下， 主控板工作指示灯不闪烁；
- 连接器损坏，有明显的元器件损坏；
- 拓竹服务团队通过日志文件确认是主控板关联问题。

### 工具

H2.0/H1.5 内六角扳手

镊子

硅胶

### 连接器说明

![](https://wiki.bambulab.com/p1/maintenance/mc-board/connectors_on_mc_board.png)

| 序号 | 连接对象 | 序号 | 连接对象 | 序号 | 连接对象 |
| --- | --- | --- | --- | --- | --- |
| 1 | 工具头 | 5 | 机箱控温风扇 | 9 | 左边的电机 (从后盖往前看) |
| 2 | 主控板冷却风扇 | 6 | 辅助部件冷却风扇 | 10 | AMS 接口板 |
| 3 | 热床（通信） | 7 | Z 轴电机 | 11 | AP 主板 |
| 4 | MC -AC 板连接线 | 8 | 右边的电机 (从后盖往前看) |  |  |

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。
>
> 如果您对本指南有任何疑问，请[点击这里提交工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)，我们将及时回复并为您提供所需的帮助。

## 移除旧件

### **第 1 步 -**  移除废料滑梯

参考 [废料滑梯](excess-chute.md) 的相关内容，移除废料滑梯。

![](https://wiki.bambulab.com/p1/maintenance/mc-board/excess_chute_removed.jpg)

### **第 2 步 -** 断开连接电缆

断开主控板上所有的连接电缆，其中热床通信线有添加硅胶固定，需要先将硅胶清理。

![](https://wiki.bambulab.com/p1/maintenance/mc-board/disconnect_cables.jpg)

### **第 3 步 -** 移除主控板

拧下 4 颗螺丝，取下主控板。

![](https://wiki.bambulab.com/p1/maintenance/mc-board/4_screws_for_mc_board.jpg)

## 安装新件

### **第 1 步 -** 安装主控板

将主控板安装到内衬上，依次锁入 4 颗螺丝进行固定，其中右下角的螺丝需要同时固定地线。

|  |  |
| --- | --- |
|  |  |

### **第 2 步 -** 连接电缆

先将热床通信线连接好，打上硅胶加固，然后将其他电缆出连接到主控板上，需确认连接到位。

|  |  |
| --- | --- |
|  |  |

### **第 3 步 -** 组装好打印机

参考拆装废料滑梯的内容，安装上废料滑梯和背板。

![](https://wiki.bambulab.com/p1/maintenance/excess-chute/rear_panel_installed.jpg)

## 功能确认

接上打印机电源，开启打印机，在屏幕上操作，运行设备自检流程，如自检通过，说明操作成功。

![](https://wiki.bambulab.com/p1/maintenance/boards-on-toolhead/self-test.jpg)

否则，请再次检查所有连接并重试。如果仍然不行，请联系 Bambu Lab 服务团队寻求进一步帮助。

## 设备校准

更换运动控制板不涉及校准操作。

## 补充内容\_更换散热片

### 步骤 1 从旧的主控板 (P1S) 上移除散热片

|  |  |
| --- | --- |
| 移除 2 颗螺丝 | 将散热片与有故障的主控板分离，不需要清除散热片上的散热硅脂 |

### 步骤 2 从新的主控板上移除散热片

|  |  |
| --- | --- |
| 移除 2 颗螺丝 | 将散热片与有故障的主控板分离，不需要清除主控板上的散热硅脂 |

### 步骤3 安装散热片 (P1S) 到新的主控板

|  |  |
| --- | --- |
| 将散热片安装到新板上 | 然后锁上 2 颗螺丝 |

## 如何验证成功

### 根据电路板灯语判断

**正常状态：MC板每5秒闪烁一次绿灯**

<https://public-cdn.bblmw.com/wiki/video/P1-MC.mp4>

如果MC板的指示灯不是5s闪烁一次（比如30s闪烁一次），请检查FPC线连接是否正确：

![connectors_on_interface_board_cn.jpg](https://wiki.bambulab.com/p1/maintenance/boards-on-toolhead/connectors_on_interface_board_cn.jpg)

## 结束语

> 我们希望这份指南为您提供了有效的信息，并真实地帮助了您。
>
> 如果您对本文中描述的过程有任何疑虑或疑问，您可以在开始操作前联系我们的客户服务团队。 我们随时准备为您提供帮助并回答您的任何问题。
>
> [点击这里提交服务工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)
