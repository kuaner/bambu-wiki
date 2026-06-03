---
path: zh/a1/maintenance/guide-for-Replacing-y-axis-components
title: "A1 Y 轴组件更换指南"
description: "本篇内容讲述更换  Y 轴组件的详细步骤。"
tags: []
created: 2025-03-13T02:11:38.059Z
updated: 2025-10-21T02:11:33.922Z
source: https://wiki.bambulab.com/zh/a1/maintenance/guide-for-Replacing-y-axis-components
---

## Y轴组件

以下我们将展示 A1 Y轴组件更换的详细步骤。  
![](https://wiki.bambulab.com/a1/maintenance/y-axis/y_assembly.jpg)

## 适用打印机型号

A1

## 何时使用

- Y 轴异响、卡顿
- 拓竹技术支持建议更换

## 所需工具和材料

- 新的 Y 轴组件
- H2.0 内六角扳手
- 25 分钟

### 螺丝清单

|  |  |
| --- | --- |
| 线缆盒 BT3-27（1PCS） | 底壳固定螺丝 BT3-8（16PCS） |

|  |  |
| --- | --- |
| 地线 M3-6（2PCS） | 热床 M3-6（4PCS） |

|  |  |
| --- | --- |
| Y 轴组件中间固定螺丝 M3-23（8PCS） | Y 轴组件两端固定螺丝 BT3-23 （4PCS） |

## 安全提示

> **重要提醒 ！**  
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。  
> 如果您对本指南有任何疑问，请[点击这里提交工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)，我们将及时回复并为您提供所需的帮助。

## 移除旧的 Y 轴组件

### 1.将打印机正面朝下放置

将打印机正面朝下放置，方便操作打印机底部。

首先将屏幕翻转到一侧，然后轻轻将打印机正面朝下放置，如下图所示。建议使用一盒耗材将打印机顶部抬起，避免压迫挤出机和屏幕。  
![place_the_a1_printer_on_its_front.jpeg](https://wiki.bambulab.com/a1/maintenance/ac-board-replacement/place_the_a1_printer_on_its_front.jpeg)

### 2.拆除线缆盒

拧松黄色标记螺丝不用完全取出，移除 1、2、3 号线缆分别是摄像头、Z 轴电机、X 轴电机之后向上推出线缆支架断开 USB-C 线缆。

|  |  |
| --- | --- |
|  |  |

> **注意**：若不能轻易移除线缆支架，可以完全取出黄色标记螺丝并再次尝试。

### 3.移除打印机底壳

移除底部 16 颗螺丝，再依次移除打印机底壳。  
![底壳2.png](https://wiki.bambulab.com/a1/maintenance/replacement-power-switch/%E5%BA%95%E5%A3%B32.png)

### 4.移除底部螺丝和 Y 电机线缆

移除地线 2 颗**固定螺丝**。  
![地线螺丝.jpg](https://wiki.bambulab.com/a1/maintenance/y-axis-component/%E5%9C%B0%E7%BA%BF%E8%9E%BA%E4%B8%9D.jpg)  
接下来，移除**散热片固定螺丝**和 Y 电机**线缆接头**。  
![y线缆螺丝.png](https://wiki.bambulab.com/a1/maintenance/y-axis-component/y%E7%BA%BF%E7%BC%86%E8%9E%BA%E4%B8%9D.png)  
将 Y 电机接头移除之后，需要将线缆从走线槽移除，方便下一步移除整个 Y 轴组件。  
![y线缆.png](https://wiki.bambulab.com/a1/maintenance/y-axis-component/y%E7%BA%BF%E7%BC%86.png)

### 5.移除热床和 Y 轴盖板

将 A1 打印机放置在平整的桌面上，缓慢上升 X 轴至顶部；

![](https://wiki.bambulab.com/a1/maintenance/new-heatbed/x_axis_move_up.png)  
热床前移到底，移除 Y 轴上盖。

|  |  |
| --- | --- |
|  |  |

移除热床之前需要，使用 H2.0 内六角扳手移除 4 个软硅胶套；  
再拧松固定热床 4 颗螺丝，从底座上取下热床，放置在桌面上。

|  |  |
| --- | --- |
|  |  |

> 注意：目前最新版本的热床已取消软胶塞。  
> ![](https://wiki.bambulab.com/a1/maintenance/heatbed/new-heatbed.png)

### 6.移除 Y 轴组件

首先需要将 Y 轴滑车移动到前端移除下图 8 颗红色标记螺丝和 2 颗绿色标记螺丝。

螺丝移除完成之后将滑车移动到尾部，再移除前端 2 颗绿色标记螺丝。

|  |  |
| --- | --- |
|  |  |

之后移除尾部电机固定螺丝。

![](https://wiki.bambulab.com/a1/maintenance/botttom/y_rail_position.jpg)

**此时即可完全将Y轴组件移除。**

![](https://wiki.bambulab.com/a1/maintenance/botttom/remove_the_y_axis.jpg)

> 注意：部分版本 Y 轴组件和底座可能会有胶水粘连，移除之前需要清理残留胶水。  
> ![胶.jpg](https://wiki.bambulab.com/a1/maintenance/y-axis-component/%E8%83%B6.jpg)

## 安装新的 Y 轴组件

### 1.安装 Y 轴组件

将 Y 电机线缆从底部穿出，先将张紧器一段装入底座，再安装 Y 电机端；  
安装完成之后，首先锁入 Y 电机位置的黑色螺丝，这颗螺丝可用于确认是否安装到位。

|  |  |
| --- | --- |
|  |  |

接下来首先安装两端 4 颗绿色标记螺丝，再安装中间位置 8 颗红色标记螺丝。

> 注意：8 颗红色标记螺丝对应的安装底座位于龙门架组件上，用于固定 Y 轴组件。请确保龙门架组件已正确安装后再进行此步骤。

|  |  |
| --- | --- |
|  |  |

### 2.连接 Y 电机线缆及底部螺丝

将 Y 电机线缆从底部走线槽内穿过。

|  |  |
| --- | --- |
|  |  |

安装 2 颗地线固定螺丝；  
连接 Y 电机接头并锁紧散热片固定螺丝。

|  |  |
| --- | --- |
|  |  |

### 3.安装打印机底壳

现在可以对打印机底壳进行安装；需要注意的是**线缆盒位置电机线**，插入线缆接头之前避免底壳压住电机线缆；  
底壳安装之后锁入对应的 16 颗螺丝，此处螺丝为自攻螺丝，避免过度锁紧。

![底壳2.png](https://wiki.bambulab.com/a1/maintenance/replacement-power-switch/%E5%BA%95%E5%A3%B32.png)

### 4.安装底部线缆盒并连接线缆

在最后一步中，小心对齐线缆盒，将其向下推入，同时确保 USB-C 电缆插入对应的母座。  
然后，拧紧图中黄色标记螺丝，注意螺丝无需过度锁紧。  
之后依次连接摄像头、X 电机、Z 电机线缆。  
![安装.png](https://wiki.bambulab.com/a1/%E5%AE%89%E8%A3%85.png)

### 5.安装热床组件及 Y 轴盖板

将热床组件，从打印机左（或右）侧观察安装位置，将热床放置到热床支架上；

![](https://wiki.bambulab.com/a1/maintenance/new-heatbed/align_holes.png)

如图所示，对齐 4 个螺丝孔，用 H2.0 内六角扳手，按对角线锁螺丝的方式锁入 4 颗螺丝。

|  |  |
| --- | --- |
|  |  |

> 注意：目前最新版本的热床已取消软胶塞，同时修改为 1 个螺丝孔。  
> 新旧版本热床仅软胶塞和螺丝孔存在差异；热床更新旨在防止更换时误装。  
> ![](https://wiki.bambulab.com/a1/maintenance/heatbed/new-heatbed.png)

将热床前移到底，将 Y 轴上盖从热床底下穿过，并向前推到底，对齐卡扣，将 Y 轴上盖安装到位。

|  |  |
| --- | --- |
|  |  |

## 设备校准

为了确保 Y 轴组件更换之后，可以正常工作，在正式打印前您需要重新对设备进行校准。

|  |  |
| --- | --- |
|  |  |

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 我们希望能确保您安全有效地进行操作。如果您对本指南描述的过程有任何疑虑或问题，建议您在开始操作前联系我们友好的客户服务团队。
>
> 我们随时准备为您解答疑问并提供帮助。[点击此处联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/cn/im)
