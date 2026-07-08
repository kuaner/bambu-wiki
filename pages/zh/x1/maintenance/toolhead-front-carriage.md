---
path: zh/x1/maintenance/toolhead-front-carriage
title: "更换工具头滑车前盖/后盖"
description: "本指南提供了更换工具头前滑车前盖/后盖的详细步骤"
tags: ["p1", "x1"]
created: 2025-03-17T09:14:27.009Z
updated: 2026-06-29T03:53:31.685Z
source: https://wiki.bambulab.com/zh/x1/maintenance/toolhead-front-carriage
---

## 工具头滑车前盖/后盖

以下我们将展示滑车前盖/后盖更换的详细步骤。

![toolhead-carriage.jpg](https://wiki.bambulab.com/x1/maintenance/replace-toolhead-front-carriage/toolhead-carriage.jpg)

## 适用打印机型号

X1系列

## 何时使用

- 挤出机固定螺母滑牙
- 切刀轴弯曲
- 拓竹技术支持建议更换

## 所需工具和材料

- 新的工具头滑车前盖/后盖
- H2.0 内六角扳手
- H1.5 内六角扳手
- 25 分钟

## 安全提示

> **重要提醒 ！**  
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。  
> 如果您对本指南有任何疑问，请[点击这里提交工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)，我们将及时回复并为您提供所需的帮助。

## 移除旧工具头滑车前盖/后盖

### 1.移除工具头前盖

揭开工具头前盖，断开连接电缆，取下前盖。

![](https://wiki.bambulab.com/x1/maintenance/th-boards-v9/disconnect_the_front_housing.jpg)

### 2.移除刀柄

按压接头，然后断开挤出机PTFE管，用H1.5 内六角扳手拧松切刀柄螺丝并移除[切刀刀柄](replace-cutter-lever.md)。

|  |  |
| --- | --- |
|  |  |

### 3.移除工具头外壳

用H1.5内六角扳手移除固定工具头外壳的8颗螺丝，取下工具头后盖和中框。

|  |  |
| --- | --- |
|  |  |

### 4.断开 USB 连接

从挤出主板上断开 USB 线缆的连接，然后将 USB 线缆连同支架一起，从工具头上移除。

![](https://wiki.bambulab.com/x1/maintenance/th-boards-v9/disconnect_the_usb_cable.jpg)

### 5.移除FPC排线

用H1.5内六角扳手拧下FPC排线两端的固定螺丝，移除固定支架，断开排线连接，取下FPC排线。

注意：这里使用的4颗螺丝，尺寸较小，避免大力拧螺丝，防止螺丝断，且不能与另外的螺丝混用。

|  |  |
| --- | --- |
|  |  |

### 6.移除接口板

断开接口板上的4条连接电缆，用H1.5内产角扳手移除2颗螺丝，取下接口板。

|  |  |
| --- | --- |
|  |  |

> 请注意：热敏电阻插头上有一个锁扣装置（不同于风扇和加热器插头），这个插头需要按下锁扣装置来解开，而不是拉扯线缆来拔出PCB接头。  
> ![20250319-161638.jpg](https://wiki.bambulab.com/x1/maintenance/replace-toolhead-front-carriage/20250319-161638.jpg)

### 7.移除挤出主板

断开挤出主板正面上的3条连接电缆，用H1.5内产角扳手移除3颗螺丝，然后向左翻转挤出主板，断开2根激光电缆，取下挤出主板。

|  |  |
| --- | --- |
|  |  |

### 8.移除激光雷达组件

用H1.5内六角扳手，移除2颗螺丝，取下激光雷达组件。

|  |  |
| --- | --- |
|  |  |

### 9.移除工具头滑车前盖（含挤出机）和后盖

用H2.0内六角螺丝，依次移除8颗螺丝。

![](https://wiki.bambulab.com/x1/maintenance/replace-the-e-motor/remove_8_screws.jpg)

移除 8 颗螺丝之后，向前推动前滑车，即可移除。

![](https://wiki.bambulab.com/x1/maintenance/replace-the-e-motor/remove_the_front_part.jpg)

小心向后推动滑车后盖，移除后盖。  
![rear_carriage.jpg](https://wiki.bambulab.com/x1/maintenance/replace-toolhead-front-carriage/rear_carriage.jpg)

> 注意：新版本使用的为铝套，工具头滑车后盖装有 4 根弹簧，要防止脱落丢失。

|  |  |
| --- | --- |
|  |  |

### 10.移除挤出机

如图所示移除 3 颗挤出机固定螺丝，将挤出机和喷嘴组件一起移除。

![挤出机_-_副本.jpg](https://wiki.bambulab.com/x1/maintenance/replace-toolhead-front-carriage/%E6%8C%A4%E5%87%BA%E6%9C%BA_-_%E5%89%AF%E6%9C%AC.jpg)

下一步移除两个电机固定螺丝，将电机移除。

![电机固定螺丝_-_副本.jpg](https://wiki.bambulab.com/x1/maintenance/replace-toolhead-front-carriage/%E7%94%B5%E6%9C%BA%E5%9B%BA%E5%AE%9A%E8%9E%BA%E4%B8%9D_-_%E5%89%AF%E6%9C%AC.jpg)

## 安装新的工具头滑车前盖/后盖

### 1.安装挤出机电机

将挤出电机安装到新的工具头滑车前盖上，注意电缆在上方，然后锁入2颗螺丝固定电机，同时可以安装[切刀刀柄](replace-cutter-lever.md)。。

|  |  |
| --- | --- |
|  |  |

### 2.安装挤出机

将挤出机和热端一起安装到滑车前盖上，锁入3颗螺丝进行固定。

![](https://wiki.bambulab.com/x1/maintenance/replace-the-e-motor/install_the_extruder.jpg)

### 3.安装滑车前盖/后盖组件

将工具头滑车后盖对准铜套位置进行安装，请小心弹簧。  
![install-rear-carriage.jpg](https://wiki.bambulab.com/x1/maintenance/replace-toolhead-front-carriage/install-rear-carriage.jpg)

将装有挤出电机的滑车前盖装上，注意不要压到电机电缆。  
![](https://wiki.bambulab.com/x1/maintenance/replace-the-e-motor/mount_the_front_part.jpg)

如果下图所示依次交叉锁入 8 颗螺丝。

|  |  |
| --- | --- |
|  |  |

### 4.安装激光雷达组件

将激光雷达组件安装到工具头下方，锁入2颗螺丝固定。

|  |  |
| --- | --- |
|  |  |

### 5.安装挤出主板

首先安装LED线缆

|  |  |
| --- | --- |
|  |  |

将挤出主板安装到工具头上，锁入3颗螺丝进行固定。然后连接相机软排线，装上固定支架并锁入2颗螺丝进行固定。

|  |  |
| --- | --- |
|  |  |

下一步连接工具头线缆。

|  |  |
| --- | --- |
|  |  |

### 6.安装接口板

将接口板安装到工具头上，拧入2颗螺丝进行固定。然后连接霍尔开头板（挤出机）电缆，建议点上硅胶进行加固，再连接3条热端电缆。

|  |  |
| --- | --- |
|  |  |

接下来安装 FPC 排线；强烈建议您在安装前仔细检查连接排线的接口，因为这些接口必须要公母配对才能正确安装。  
![](https://wiki.bambulab.com/x1/maintenance/th-boards-v9/%E7%AC%AC%E5%8D%81%E4%B8%80%E6%AD%A5_1.png)  
确认连接排线的方向后，安装到工具头上方的线槽。然后分别连接到接口板和挤出主板的连接器上，并用压线支架和螺丝进行加固。

> 注意：这里使用的4颗螺丝，尺寸较小，避免大力拧螺丝，防止螺丝断，且不能与另外的螺丝混用。

|  |  |
| --- | --- |
|  |  |

### 7.连接 USB 线缆

将 USB 电缆连接到挤出主板上，将 USB 线压入线材底座后，将线材支架扣装到位。

![](https://wiki.bambulab.com/x1/maintenance/th-boards-v9/connect_usb_cable.jpg)

### 8.安装工具头外壳

安装工具头中框和后盖，并在两侧分别锁入4颗螺丝进行固定。

|  |  |
| --- | --- |
|  |  |

### 9.安装切刀柄以及前盖

用手抬起切刀柄，将切刀沿刀槽滑入挤出机内，锁紧固定螺丝，然后接上PTFE管。  
接下来连接前盖线缆，合上前盖。

|  |  |
| --- | --- |
|  |  |

## 功能验证

连接打印机电源，首先，可以尝试提高热端温度并开启部件冷却风扇，然后观察温度是否上升以及风扇是否运转正常。  
![升温风扇.png](https://wiki.bambulab.com/x1/maintenance/replace-toolhead-front-carriage/%E5%8D%87%E6%B8%A9%E9%A3%8E%E6%89%87.png)

接下来可以对打印机进行校准操作，校准通过无异常即可发起打印测试。

|  |  |
| --- | --- |
|  |  |

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南并未解决您的问题，[*请点击此处联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
