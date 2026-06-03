---
path: zh/x1/maintenance/replace-typec-cable
title: "更换 USB-C 通信电缆"
description: "本指南提供更换 X1 系列打印机 USB-C 通信电缆的详细步骤。"
tags: ["usb-c 数据线", "x1"]
created: 2022-07-31T03:14:13.725Z
updated: 2025-12-24T12:18:39.659Z
source: https://wiki.bambulab.com/zh/x1/maintenance/replace-typec-cable
---

## 什么是 USB-C 通信电缆

USB-C 通信电缆是连接 AP 主板和工具头主板的一根使用 Type C 接口的电缆。

![](https://wiki.bambulab.com/x1/maintenance/replace-usb-cable/usb_cable.jpg)

## 何时更换

1. USB-C 电缆通信不稳定导致打印机工作异常;

2. 售后人员通过日志文件分析，确认是 USB-C 通信故障。

## 需要的工具和材料

- 全新的 USB-C 通信电缆
- H1.5/H2.0 内六角扳手

> 新版 USB-C 线的接头上带有导电布，请勿撕掉！
>
> ![](https://wiki.bambulab.com/x1/maintenance/replace-typec-cable/conductive-tape.png)

## 开始操作前的安全警告和机器状态

请仔细按照本指南步骤进行更换。在开始任何拆卸和组装之前，请确保机器已断电。

## 操作指南

### **第 1 步 - 松开料管**

移除玻璃上盖，将料管从拖链卡扣上松脱出来。

![](https://wiki.bambulab.com/x1/maintenance/replace-usb-cable/tube_buckle.jpg)

### **第 2 步 - 移除 AP 主板盖**

用 H1.5 内六角扳手移除 1 颗位于机器背面、耗材入料口下方的螺丝，然后从两端分别将 AP 主板盖揭开，将 AP 主板盖横梁上松脱出来。

|  |  |
| --- | --- |
|  |  |

### **第 3 步 - 断开 USB 连接（ AP 板端）**

将线缆从 USB 线夹紧块上移除，用 H2.0 内六角扳手拆下 1 颗螺丝，将 USB 线从 AP 板上断开。

|  |  |
| --- | --- |
|  |  |

### **第 4 步 - 移除工具头的后盖**

使用内六角扳手移除固定工具头后盖的 4 颗螺丝，然后取下工具头后盖。

![](https://wiki.bambulab.com/x1/maintenance/replace-micro-lidar/1020px-lidar_ds4.png)

### **第 5 步 - 断开 USB 连接（工具头端）**

从挤出主板上断开 USB 线的连接，如图所示调整 USB 线支架的方向，将 USB 线连同支架一起，从工具头上移除。

|  |  |
| --- | --- |
|  |  |

### **第 6 步 - 移除 USB-C 通信电缆**

将 USB 线从 AP 主板盖和拖链中松脱出来，移除 USB-C 通信电缆， 移除 USB 线夹紧块。

|  |  |
| --- | --- |
|  |  |

### **第 7 步 - 安装新的 USB-C 通信电缆**

将 USB-C 电缆装入拖链和 AP 主板盖上，装上 USB 线夹紧块。

|  |  |
| --- | --- |
|  |  |

### **第 8 步 - 连接 USB 电缆（工具头端）**

将 USB 线连接到工具头主板上，将 USB 线压入线材底座后，将线材支架扣装到位。

|  |  |
| --- | --- |
|  |  |

### **第 9 步 - 安装工具头后盖**

重新安装工具头的后盖并用 4 颗螺丝（每侧 2 颗）将其固定。

![](https://wiki.bambulab.com/x1/maintenance/replace-micro-lidar/1047px-lidar_as4.png)

### **第 10 步 - 连接 USB 电缆（ AP 板端）**

将 USB 线连接到 AP 板接口上，注意字母 A 朝外，用 1 颗螺丝固定夹紧块，将电缆卡到夹紧块上。

|  |  |
| --- | --- |
|  |  |

> 注意：新版本在该处粘附了一块导电布，因此无法看到字母 A，可将电缆**凸起位置朝外**插入。
>
> ![](https://wiki.bambulab.com/x1/maintenance/replace-typec-cable/20250121-093559.jpg)

### **第 11 步 - 安装 AP 主板盖**

先对齐下图所示的缺口进行安装 AP 主板盖，再将 AP 主板盖安装到位，在机器背面、耗材入料口下方锁入 1 颗螺丝进行固定。

|  |  |
| --- | --- |
|  |  |

### **第 12 步 - 扣好料管**

将料管扣到拖链上，盖上玻璃上盖。

![](https://wiki.bambulab.com/x1/maintenance/replace-usb-cable/tube_buckle.jpg)

## 如何验证完成/成功

1.启动打印机，确认机箱内部干净无异物；

2. 在屏幕上找到“工具”菜单，首先点击“校准”按钮，完成校准后，再进行一次“设备自检”操作。

![calibration.png](https://wiki.bambulab.com/screen-operation/calibration.png)  
![selftest.png](https://wiki.bambulab.com/screen-operation/selftest.png)

如果以上操作一切顺利，并且在校准和自检过程中没有出现错误或警告，则更换成功。否则，请检查连接后重试。  
如果问题仍然存在，请联系服务团队寻求进一步帮助。
