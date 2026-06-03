---
path: zh/a1/maintenance/cable-pack
title: "更换 A1 线材包"
description: "本文将介绍如何更换 A1 线材包中的线缆。"
tags: ["a1"]
created: 2026-05-08T07:13:01.836Z
updated: 2026-05-15T10:44:47.460Z
source: https://wiki.bambulab.com/zh/a1/maintenance/cable-pack
---

## 线材包

线材包中包含摄像头线缆、AC 板信号线缆、电源模块供电线缆、AMS 接口板线缆。

![all.jpg](https://wiki.bambulab.com/a1/maintenance/cable-pack/all.jpg)

## 何时更换

1. 线缆外观明显破损或断裂；
2. 可能由于线缆引发的相关模块故障；

## 所需工具

- 线材包
- 内六角扳手
- 十字螺丝刀

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 摄像头线缆

![cam.jpg](https://wiki.bambulab.com/a1/maintenance/cable-pack/cam.jpg)

### 移除旧线缆

从电机罩右侧卡扣处用力，移除电机罩前盖。

![电机罩前盖卡扣.jpg](https://wiki.bambulab.com/a1/maintenance/usb-c-cable-replacement-guide/%E7%94%B5%E6%9C%BA%E7%BD%A9%E5%89%8D%E7%9B%96%E5%8D%A1%E6%89%A3.jpg)

用手按压线夹两侧，取出线夹。

![双手捏紧线夹.jpg](https://wiki.bambulab.com/a1/maintenance/usb-c-cable-replacement-guide/%E5%8F%8C%E6%89%8B%E6%8D%8F%E7%B4%A7%E7%BA%BF%E5%A4%B9.jpg)

参考下图从摄像头下方用力推动使其旋转一定的角度，然后断开摄像头连接线，取下摄像头。

|  |  |
| --- | --- |
|  |  |

> 如果取下较困难，可以参照下方动图使用螺丝刀辅助。  
> ![remove-with-allen-key.webp](https://wiki.bambulab.com/a1/maintenance/camera-replacement/remove-with-allen-key.webp)

将屏幕翻转到一侧，轻轻地将打印机正面朝下放置，如下图所示。建议使用一盒耗材将打印机顶部抬起，避免挤压挤出机和屏幕。

![](https://wiki.bambulab.com/a1/maintenance/power-supply/place_the_a1_printer_on_its_front.jpeg)

卸下下图所示的 1 颗螺丝，然后断开摄像头、X 轴电机和 Z 轴电机的线缆；向上推动线缆盒，断开 USB-C 数据线。

|  |  |
| --- | --- |
| usb-c线固定螺丝.jpg |  |

再拧松下图所示的 1 颗螺丝，打开线缆盒；

|  |  |
| --- | --- |
| 线夹螺丝.jpg | 线夹打开关闭.jpg |

撕下粘贴在金属套管上的胶布，抽出摄像头线缆。

> 可将撕下的胶布的末端贴在打印机或桌面上，安装时可重复使用。

![醋酸胶布.jpg](https://wiki.bambulab.com/a1/maintenance/usb-c-cable-replacement-guide/%E9%86%8B%E9%85%B8%E8%83%B6%E5%B8%83.jpg)

### 安装新线缆

将新线缆推入编织网管中，将套管压短后更容易让线缆穿过：

![](https://wiki.bambulab.com/a1m/replace-usb-c-cable/compress_the_wire_loom.jpg)

将摄像头与连接线连接，并将摄像头安装到电机罩上。

|  |  |
| --- | --- |
|  |  |

参考下图依次将 X 电机、Z 电机和摄像头的连接线放入对应的线槽中，并扣上卡扣，拧紧螺丝。

|  |  |  |
| --- | --- | --- |
| 线插入线缆支架.jpg | 理线盒螺丝.jpg |  |

> **注意**：USB-C 的连接需区分方向，USB-C 数据线接口上有一个凸点，请将其朝上，按图示方向安装。  
> ![usbc方向.jpg](https://wiki.bambulab.com/a1/maintenance/usb-c-cable-replacement-guide/usbc%E6%96%B9%E5%90%91.jpg)

对齐线缆支架后，向下推动，确保将 USB-C 数据线完全插入（不会露出 type-c 口），并拧紧图中所示的螺丝以将其锁定到位。

> **注意**：由于这颗螺丝是拧入塑料框架的，请避免过度拧紧。

![](https://wiki.bambulab.com/a1/maintenance/wifi-antenna/%E5%AE%89%E8%A3%85%E6%94%AF%E6%9E%B6.jpg)

重新连接摄像头、X 轴电机和 Z 轴电机线缆以完成安装。

> **注意：左侧较短线缆为 X 轴电机线缆，插入右上方接口；右侧较长线缆为 Z 轴电机线缆，插入右下方接口。**

![](https://wiki.bambulab.com/a1/maintenance/wifi-antenna/%E6%8E%A5%E7%BA%BF%E7%BC%86.jpg)

参考下图将线夹重新插入到位。

|  |  |  |
| --- | --- | --- |
|  |  |  |

然后将电机罩前盖重新扣上，直到听到卡扣“咔哒”声。

|  |  |
| --- | --- |
|  |  |

## 其余线缆

### 移除底壳

首先将屏幕翻转到一侧，然后轻轻将打印机正面朝下放置，如下图所示。建议使用一盒耗材将打印机顶部抬起，避免压迫挤出机和屏幕。  
![place_the_a1_printer_on_its_front.jpeg](https://wiki.bambulab.com/a1/maintenance/ac-board-replacement/place_the_a1_printer_on_its_front.jpeg)

拧松黄色标记螺丝不用完全取出，移除 1、2、3 号线缆（分别是摄像头、Z 轴电机、X 轴电机），之后向上推出线缆支架断开 USB-C 线缆。

![disconnect_the_a1_wires_and_remove_the_wire_bracket_-_22.jpeg](https://wiki.bambulab.com/a1/maintenance/ac-board-replacement/disconnect_the_a1_wires_and_remove_the_wire_bracket_-_22.jpeg)

> **注意**：若不能轻易移除线缆支架，可以完全取出黄色标记螺丝并再次尝试。

移除底壳 10 颗红色标记螺丝，轻轻撬开底壳即可。

![remove_the_bottom_housing_cover_screws.jpeg](https://wiki.bambulab.com/a1/maintenance/ac-board-replacement/remove_the_bottom_housing_cover_screws.jpeg)

### 更换线缆

> 可根据需求选择更换。

- 更换 AC 板信号线缆
- 更换电源模块供电线缆
- 更换 AMS 接口板线缆
