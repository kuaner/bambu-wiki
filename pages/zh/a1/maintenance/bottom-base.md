---
path: zh/a1/maintenance/bottom-base
title: "A1 底座拆装指引"
description: "本文提供 A1 底座拆装的相关指引和注意事项，在这个拆解过程中涉及的可更换配件的拆装也可参考本文进行处理。"
tags: ["底座", "a1"]
created: 2023-11-28T05:51:26.586Z
updated: 2026-02-05T04:13:01.715Z
source: https://wiki.bambulab.com/zh/a1/maintenance/bottom-base
---

## A1 底座

A1 底座包含热床组件、Y 轴组件、触摸屏、前后底盖、AC 板、主板、电源模块以及开关模块。

![](https://wiki.bambulab.com/a1/maintenance/botttom/bottom_base.jpg)

## 相关组件拆解指引

本文提供 A1 底座拆解和组装的相关指引和注意事项。  
如果您需要拆卸打印机的其他主要组件，您可以点击以下链接快速查看。

- 拆除料盘支架。[A1 料盘支架拆装指引 | Bambu Lab Wiki](spool-holder.md)
- 拆除工具头。[A1 工具头拆装指引 | Bambu Lab Wiki](../../a1-mini/maintenance/toolhead.md)
- 拆除 X 轴组件。[A1 X轴组件拆装指引 | Bambu Lab Wiki](x-axis.md)
- 拆除热床。[A1 热床拆装指引 | Bambu Lab Wiki](heatbed.md)
- 拆除龙门架。[A1 龙门架拆装指引 | Bambu Lab Wiki](z-axis.md)

如果您还需要将 A1 整机拆解成各主要组件并重新组装成整机，请参考 [A1 整机拆装指引 | Bambu Lab Wiki](printer.md)。

## 工具

- H2.0/H1.5 内六角扳手
- 十字螺丝刀
- 平头镊子

## 前期操作

在开始操作前，请务必断开打印机电源。

![](https://wiki.bambulab.com/a1/maintenance/botttom/disconnect_power.jpg)

## 安全提示

> **❗❗ 重要提醒**   
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请**关闭打印机电源并断开电源连接**，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，**请佩戴好隔热手套**，以确保安全有效地执行维护工作。  
> 如果您对本指南有任何疑问，请[点击这里提交工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)，我们将及时回复并为您提供所需的帮助。

## 拆解指引

### 步骤 1 ：拆除前、后底盖

移除底壳红色标记螺丝，轻轻撬开底壳即可。  
![](https://wiki.bambulab.com/a1/maintenance/heatbed/16_screws.jpg)

### 步骤 2 ：移除触摸屏

您可以参考 [A1 屏幕拆卸指南 | Bambu Lab Wiki](touchscreen-replacement-guide.md) 移除触摸屏组件。

![](https://wiki.bambulab.com/a1/manual/replace-touchscreen/a1_touchscreen.jpg)

### 步骤 3 ：移除 AMS 接口板

断开连接电缆，用 H1.5 内六角扳手移除 2 颗螺丝，取下 AMS 接口板。

|  |  |
| --- | --- |
| ams_int_board_1 | pry_up_the_interface_board |

### 步骤 4 ：移除电源模块

您可以参考 [A1 电源模块拆卸指南 | Bambu Lab Wiki](power-supply-replacement-guide.md) 移除电源模块。

![](https://wiki.bambulab.com/a1/maintenance/power-supply/a1_mini_power_supply.jpg)

### 步骤 5 ：移除 AC 控制板

您可以参考 [A1 AC 板拆卸指南 | Bambu Lab Wiki](ac-board-replacement.md)移除 AC 板。

![](https://wiki.bambulab.com/a1/maintenance/ac-board-replacement/a1_ac_board.jpg)

### 步骤 6 ：移除主板

您可以参考 [A1 主板拆卸指南 | Bambu Lab Wiki](mainboard-replacement-guide.md) 移除旧主板。

![](https://wiki.bambulab.com/a1/manual/replace-mainboard/remove_the_boadrd_completely.jpg)

### 步骤 7 ：移除电缆

1. 将 AMS 接口板电缆从卡扣中松出，然后往安装接口板的方向移除。

![](https://wiki.bambulab.com/a1/maintenance/botttom/remove_the_m_to_ams_cable.jpg)

2. 用平头镊子撬起 Wi-Fi 板，取下 Wi-Fi 天线。

![](https://wiki.bambulab.com/a1/maintenance/botttom/remove_wifi_cable.jpg)

3. 移除主板到 AC 板的连接软排线。

![](https://wiki.bambulab.com/a1/maintenance/botttom/remove_the_m_t_ac_cable.jpg)

### 步骤 8 ：移除 Y 轴组件

您可以参考 [A1 Y 轴组件更换指南 | Bambu Lab Wiki](guide-for-Replacing-y-axis-components.md) 移除 Y 轴组件。

![](https://wiki.bambulab.com/a1/maintenance/y-axis/y_assembly.jpg)

## 组装指引

### 步骤 1 ：安装 AC 控制板

您可以参考 [A1 AC 板安装指南 | Bambu Lab Wiki](ac-board-replacement.md) 安装AC 板。

### 步骤 2 ：安装电源模块

您可以参考 [A1 电源模块安装指南 | Bambu Lab Wiki](power-supply-replacement-guide.md) 安装电源模块。

### 步骤 3 ：安装 AMS 接口板

1. 安装 AMS 接口板，确认对齐位置后，需要用力按压一下，才能安装到位。

|  |  |
| --- | --- |
| ams_int_board_1 | pry_up_the_interface_board |

2. 锁 2 颗螺丝进行固定。

![](https://wiki.bambulab.com/a1/maintenance/botttom/lock_ams_board.jpg)

### 步骤 4 ：安装主板

您可以参考 [A1 主板安装指南 | Bambu Lab Wiki](mainboard-replacement-guide.md) 安装主板。

### 步骤 5 ：连接 AMS 接口板电缆

连接 AMS 接口板电缆，并整理好线缆，特别是有螺柱的位置，需要做好避让，以免后面被螺丝损伤。

|  |  |  |
| --- | --- | --- |

### 步骤 6 ：安装 Y 轴组件

您可以参考 [A1 Y 轴组件更换指南 | Bambu Lab Wiki](guide-for-Replacing-y-axis-components.md) 安装 Y 轴组件。

### 步骤 7 ：安装触摸屏

您可以参考 [A1 屏幕安装指南 | Bambu Lab Wiki](touchscreen-replacement-guide.md) 安装触摸屏组件。

## 功能验证

1. 外观检查，检查连接线没有插错或漏接，并整理好线材。
2. 新更换的 Y 轴导轨，需要进行润滑处理，具体的操作请查阅 [A1 润滑 Y 轴导轨操作指南 | Bambu Lab Wiki](lubricate-y-axis.md)。

## 配件清单

以下是本指引会涉及到的配件。

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| 序号 | 名称 | 实物照片 | 序号 | 名称 | 实物照片 |
| 1 | 触摸屏幕组件 |  | 2 | AMS接口板 |  |
| 3 | 电源模块 |  | 4 | AC控制板 |  |
| 5 | 主板 |  | 6 | 底座 |  |
| 7 | WIFI 天线 |  | 8 | 线材包 |  |

> **📌 注意**：
>
> 1. 如果涉及更换主板，请更换主板后，向拓竹的售后人员提供新主板的 SN 以及旧主机的 SN，需要进行 SN 的注册。  
>    [如何获取打印机的序列号（SN）| Bambu Lab Wiki](../../general/find-sn.md)
> 2. 如果更换了底座，需要将贴在底座后侧的 SN 标签贴到新底座上。

![](https://wiki.bambulab.com/general/find-sn/a1_sn.jpg)

## 螺丝清单

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | 型号 | 位置 | 规格/图纸 |  | 型号 | 位置 | 规格/图纸 |
| 螺丝A | B0026 | 显示屏弹片 |  | 螺丝B | B0018 | AMS 接口板/主板 |  |
| 螺丝C | B0020 | 电源模块 |  | 螺丝D | B0022 | AC控制板 |  |
| 螺丝E | B00222 | 主板散热片  2PCS |  | 螺丝F | B0063 | 主板散热片  1PCS |  |
| 螺丝G | B0060 | 电源地线 |  | 螺丝H | B00236 | Y轴组件 |  |

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 我们希望能确保您安全有效地进行操作。如果您对本指南描述的过程有任何疑虑或问题，建议您在开始操作前联系我们友好的客户服务团队。
>
> 我们随时准备为您解答疑问并提供帮助。[点击此处联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/cn/im)
