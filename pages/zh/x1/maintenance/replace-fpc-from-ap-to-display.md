---
path: zh/x1/maintenance/replace-fpc-from-ap-to-display
title: "更换屏幕FPC"
description: "更换显示屏主排线的操作步骤和检验方法"
tags: ["x1"]
created: 2022-08-01T03:42:51.825Z
updated: 2025-12-18T11:39:40.788Z
source: https://wiki.bambulab.com/zh/x1/maintenance/replace-fpc-from-ap-to-display
---

## 什么是屏幕 FPC

屏幕 FPC 是连接 AP 主板和高清屏幕的软排线，早期的版本可能没有保护胶带。

|  |  |
| --- | --- |
| 配有保护胶带的新版本 | 旧版本 |

## 何时更换

屏幕 FPC 有明显的损伤（主要是早期版本），或者 FPC 上的连接器变形或损坏时，需要更换。

![](https://wiki.bambulab.com/x1/maintenance/replace-fpc-from-ap-to-display/350px-broken.png)

## 所需工具和材料

- 新的屏幕 FPC
- H2.0 内六角扳手
- 电吹风
- 硅胶

![](https://wiki.bambulab.com/x1/maintenance/replace-the-chamber-led/silicone_glue.jpg)

仅供参考

## 开始运行前的安全警告和机器状态

请按照指导步骤进行更换，在进行拆卸和组装作业时需关闭打印机电源。

## 操作指南

### \*\*第 1 步 -\*\*关闭电源

关闭打印机电源，取下玻璃盖板。

### **第 2 步 - 移除高清屏幕**

将屏幕向上倾斜并按压图示位置以松开卡扣，再向右推动以解锁高清屏幕，按下 FPC 连接器的两侧以解锁连接器，移除高清屏幕。

|  |  |
| --- | --- |
|  |  |

### **第 3 步 - 打开 AP 主板盖**

揭开位于机器左上方的 AP 主板盖，如下图所示。

|  |  |
| --- | --- |
|  |  |

### **第 4 步 - 断开电缆**

使用吹风机加热软化固定连接器的硅胶，然后断开摄像头电缆、LED 灯电缆和按钮板电缆的连接。

![](https://wiki.bambulab.com/x1/maintenance/replace-fpc-from-ap-to-display/400px-dis_3cables.png)

### **第 5 步 - 回抽屏幕 FPC**

取下透明固定胶带，将 屏幕 FPC 从方孔中往回抽出。

|  |  |
| --- | --- |
|  |  |

### **第 6 步 - 取下 AP 板**

如下图所示拆下 5 颗螺丝，将 AP 主板与腔体分离。

|  |  |
| --- | --- |
|  |  |

### **第 7 步 - 断开 FPC**

用吹风机加热软件 UV 胶，去除 UB 胶后解锁连接器并断开屏幕 FPC。

|  |  |
| --- | --- |
|  | x1-display-fpc.webp |

### **第 8 步 -** 连接屏幕 FPC

将新的 FPC 连接到 AP 主板上。

> \*\*注意：\*\*连接 FPC 时，如下图所示，接点面朝上，不能反向连接。

![fpc2.webp](https://wiki.bambulab.com/x1/maintenance/replace-fpc-from-ap-to-display/fpc2.webp)

### **第 9 步 -** 点 UV 胶（或贴附胶布）

在连接器上点上 UV 胶，需要将 UV 用紫外线灯照射硬化。也可以使用粘性较强的胶布进行加固，防止 FPC 从连接器上松脱。

![](https://wiki.bambulab.com/x1/maintenance/replace-fpc-from-ap-to-display/fpc_connected.jpg)

### **第 10 步 - 安装 AP 主板**

对齐槽位和限位块将 AP 主板安装到位，锁紧 5 颗螺丝。

|  |  |
| --- | --- |
|  |  |

### **第 11 步 - 连接电缆**

连接按键板排线、LED 排线和摄像头排线，在 3 个连接器上涂上硅胶进行加固，让它们静置至少 30 分钟等待固化。

|  |  |
| --- | --- |
|  |  |

### **第 12 步 - 穿屏幕 FPC**

将连接 FPC 折叠起来，穿过方孔，理好排线、电缆，贴上透明固定胶带。

|  |  |  |
| --- | --- | --- |
|  |  |  |

### **第 13 步 - 安装高清屏幕**

将屏幕 FPC 连接到高清屏幕上的连接器，将多余的 FPC 排线退回打印机，将高清屏幕安装到打印机的 4 个插槽中，然后轻轻向左推，直到听到卡扣到位的声音，完成安装。

|  |  |  |
| --- | --- | --- |
|  |  |  |

### **步骤 14 - 合上 AP 主板盖**

合上 AP 主板盖，放回玻璃盖板。

![](https://wiki.bambulab.com/x1/maintenance/replace-fpc-from-ap-to-display/350px-cover3.png)

## 如何验证完成/成功

打开打印机电源。如果液晶屏点亮并显示无误，并且在触摸屏时触摸屏响应正常，则更换完成。

![](https://wiki.bambulab.com/x1/maintenance/replace-high-resolution-screen/615px-screen.png)

否则，请检查连接并重试。如果问题仍然存在，请联系 Bambu Lab 服务团队寻求进一步帮助。

## **结束语**

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 我们希望能确保您安全有效地进行操作。如果您对本指南描述的过程有任何疑虑或问题，建议您在开始操作前联系我们友好的客户服务团队。
>
> 我们随时准备为您解答疑问并提供帮助。[点击此处联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/cn/im)
