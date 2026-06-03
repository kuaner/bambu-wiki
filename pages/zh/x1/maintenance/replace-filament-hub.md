---
path: zh/x1/maintenance/replace-filament-hub
title: "更换AMS五通组件和AMS内部五通组件马达"
description: "本指南详细介绍了如何卸下和安装AMS五通组件和AMS内部五通组件马达。"
tags: ["ams", "五通组件", "五通组件马达"]
created: 2022-08-01T01:48:09.024Z
updated: 2025-05-19T13:47:46.978Z
source: https://wiki.bambulab.com/zh/x1/maintenance/replace-filament-hub
---

## AMS五通组件

![](https://wiki.bambulab.com/x1/maintenance/replace-filament-hub/ams%E4%BA%94%E9%80%9A.jpg)

AMS五通组件是AMS的选料（4进1出）装置，根据当前选用的材料位置，开通对应的进料口，并辅助将打印丝输送至打印机，同时也具有辅助将已送至打印机的打印丝拉回AMS的功能。

购买链接：  
[京东](https://item.jd.com/10069934119966.html)  
[天猫](https://detail.tmall.com/item.htm?abbucket=8&id=708119299745&rn=62b30f04d78690e9074f9afc466d28f9&spm=a1z10.3-b-s.w4011-25177047232.242.14a61c79BCpw29&skuId=5145716975121)

## AMS内部五通组件马达

![](https://wiki.bambulab.com/x1/maintenance/replace-filament-hub/ams_internal_hub_motor.jpg)

AMS内部五通组件马达用于为AMS五通组件的运行提供动力。

购买链接：  
[京东](https://item.jd.com/10072997295880.html)

## 何时更换

打印材料经常性卡在AMS五通组件中，且所有 PTFE 管检查正常且连接良好。或通过对打印日志的分析，确认是AMS五通组件的故障。

## 所需工具和材料

- 新的 AMS 五通组件和 AMS 内部五通组件马达
- H2.0 和 H1.5 内六角扳手

## 开始操作前的安全警告和机器状态

关闭打印机电源并断开AMS 与打印机的连接。

## 操作指南

### 步骤 1 - (拆卸) 拆除PTFE管

打开AMS上盖，按压AMS 五通组件上的按钮（解锁快速接头），然后从AMS背面拉出PTFE管。

|  |  |
| --- | --- |
|  |  |

### 第 2 步 - 移除螺丝

移除固定AMS主框架上2颗螺丝。

![](https://wiki.bambulab.com/x1/maintenance/replace-filament-hub/524px-pemove_2_screw.png)

### 第 3 步 - 移除AMS主框架组件

向上翻转中间框架组件，断开bambu总线电缆和电源电缆，移除AMS主框架组件。

![](https://wiki.bambulab.com/x1/maintenance/replace-filament-hub/378px-2_cables.png)

### 第 4 步 - 断开 4 条PTFE 管

依次按下快速接头上的按钮，解锁连接并断开 4 条PTFE 管。

|  |  |
| --- | --- |
|  |  |

### 第 5 步 - 移除 4 颗螺丝

移除 4 颗螺丝，然后将AMS五通组件翻转过来。

![](https://wiki.bambulab.com/x1/maintenance/replace-filament-hub/318px-4_screws_v2.png)

### 第 6 步 - 断开 3 根电缆

断开电机电缆、霍尔电缆和测速电缆，然后拆下AMS五通组件。

|  |  |
| --- | --- |
|  |  |

> **注意**：为了防止接口松动，电机电缆处已涂抹胶水。断开电缆时，请使用热风枪或镊子小心去除胶水（移除后不会影响保修）。

### 第 7 步 - 移除 AMS 内部五通组件马达

移除 2 颗螺丝，然后取下 AMS 内部五通组件马达。

![](https://wiki.bambulab.com/x1/maintenance/replace-filament-hub/617px-motor_unit_remove_v2.png)

### 第 8 步 - （组装）安装AMS内部五通组件马达

根据定位柱和螺丝孔将AMS内部五通组件马达安装到AMS五通组件上。

|  |  |
| --- | --- |
|  |  |

### 第 9 步 - 锁入2 个螺丝

用2 颗螺丝锁定电机。

![](https://wiki.bambulab.com/x1/maintenance/replace-filament-hub/612px-mas.png)

### 第 10 步 - 连接 3 根电缆

依次连接AMS内部五通组件马达电缆、霍尔电缆和速度电缆。

![](https://wiki.bambulab.com/x1/maintenance/replace-filament-hub/436px-3_filaments_hub_cables.png)

### 第 11 步 - 安装AMS线材五通

将AMS五通组件安装到中框，并锁入4 颗螺丝。

![](https://wiki.bambulab.com/x1/maintenance/replace-filament-hub/318px-4_screws_v2.png)

### 第 12 步 - 连接 4 根 PTFE 管

理好电缆走线，并依次连接 4 根 PTFE 管到五通组件。

![](https://wiki.bambulab.com/x1/maintenance/replace-filament-hub/376px-tubes.png)

### 第 13 步 - 安装AMS主框架组件

将AMS主框架组件装入AMS外壳，并将Bambu总线电缆和电源电缆连接到AMS电源板。

|  |  |
| --- | --- |
|  |  |

### 第 14 步 - 固定AMS主框架组件

如下图所示，将AMS主框架安装到位，用2颗螺丝固定AMS主框架组件。

![](https://wiki.bambulab.com/x1/maintenance/replace-filament-hub/524px-remove_2_screw.png)

### 第 15 步 - 连接PTFE管

检查确认PTFE管硅胶支架与五通组件的料孔对齐，并从AMS后部推入PTFE管。装完后，拉动PTFE管，确认PTFE管已固定。

|  |  |
| --- | --- |
|  |  |

## 如何验证完成/成功

将 AMS 连接到打印机并打开电源。将打印材料加载到 AMS 的所有料槽中，然后单击屏幕上的“进料”开始加载打印丝。

![](https://wiki.bambulab.com/x1/maintenance/replace-filament-hub/494px-load1.png)

1号料槽进完料后，点出2号料槽图标加载2号料槽的打印丝，以此类推，直至4个料槽都完成一次进料、退料的操作。

![](https://wiki.bambulab.com/x1/maintenance/replace-filament-hub/485px-load234.png)

如果所有进退料过程都表现正常，则更换完成。  
否则，检查所有电缆和 PTFE 管的连接后重试。

如果故障仍然存在，请联系 [Bambu Lab 服务团队](https://bambulab.cn/zh-cn/my/support/tickets?from=5)以获得进一步帮助。
