---
path: zh/h2/maintenance/servomotor-replacement
title: "H2 系列舵机更换指南"
description: "本文介绍了排气格栅和挡风板的详细更换指南"
tags: []
created: 2025-04-21T10:42:11.551Z
updated: 2026-03-13T03:28:18.831Z
source: https://wiki.bambulab.com/zh/h2/maintenance/servomotor-replacement
---

> **注意**：本页面以 H2D 机器为例。**H2S 和 H2C 的更换步骤完全相同**。

## 舵机

H2D 关键的执行元件之一，主要用于驱动滤芯风门和排气格栅的开合动作。通过接收 MC 板发出的信号，舵机能够实现精确的角度定位，确保滤芯风门与排气格栅准确开闭，从而实现有效的空气流通与排气控制。

|  |  |
| --- | --- |
| 风门舵机 | 排气格栅舵机 |

> 如果您收到的备件是整个右内衬上盖，可以从右内衬上盖中拆出新的舵机单独更换。  
> ![](https://wiki.bambulab.com/h2/maintenance/replace-right-inner-lining/img_v3_02l5_fdfe06ec-f84e-4efa-91de-2c9b37fe3a3g.jpg)

## 适用打印机型号

Bambu Lab H2D

## 何时使用

当舵机出现故障或失效时，便需要进行更换，例如滤芯风门或格栅无法正常开启或关闭、动作迟缓或不稳定，甚至完全无法响应控制信号。

## 所需要工具和材料

- H2.0 内六角螺丝刀
- H1.5 内六角螺丝刀
- 25 分钟

## 安全提示

> **重要提醒 ！**  
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。  
> 如果您对本指南有任何疑问，请[点击这里提交工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)，我们将及时回复并为您提供所需的帮助。

## 更换风门舵机

### 1.移除滤芯盖和滤芯

扣住顶端槽位缓慢向后拉移除滤芯盖，然后以同样的方式移除滤芯。

|  |  |
| --- | --- |
|  |  |

### 2.移除齿轮磁铁

可以使用 H1.5 螺丝刀移除齿轮槽内磁铁，**请务必小心操作，以防磁铁掉入机箱内部。**

|  |  |
| --- | --- |
|  |  |

> 如果移除滤芯之后发现风门处于底部位置，可以手动缓慢抬升至顶部。  
> ![风门.jpg](https://wiki.bambulab.com/h2/maintenance/servomotor-replacement/%E9%A3%8E%E9%97%A8.jpg)

### 3.移除齿轮

拧松齿轮和舵机轴固定螺丝。

![移除.jpg](https://wiki.bambulab.com/h2/maintenance/servomotor-replacement/%E7%A7%BB%E9%99%A4.jpg)

移除螺丝时以防止其落入机箱内部时，**可以使用磁铁吸附螺丝，将其缓慢取出**，避免寻找小零件的麻烦。

![吸出来.jpg =600x](https://wiki.bambulab.com/h2/maintenance/servomotor-replacement/%E5%90%B8%E5%87%BA%E6%9D%A5.jpg)

移除齿轮和舵机轴固定螺丝后后取下齿轮。

|  |  |
| --- | --- |
|  |  |

### 4.移除背板

由于风门舵机安装在机箱内部，因此对风门舵机拆装需要移除打印机背板，接下来您需要移动到打印机的背面，可以[参考这篇指南来移除打印机背板。](replace-rear-panel.md)

风门舵机位于电源模块左上角和排气格栅下方的位置。

![背部_(1).jpg](https://wiki.bambulab.com/h2/maintenance/servomotor-replacement/%E8%83%8C%E9%83%A8_(1).jpg)

### 5.移除风门舵机

移除舵机上下两颗固定螺丝（BT2-8），移除时同样可以使用磁铁吸住，避免螺丝脱落至机舱内部。

![风门舵机.jpg =600x](https://wiki.bambulab.com/h2/maintenance/servomotor-replacement/%E9%A3%8E%E9%97%A8%E8%88%B5%E6%9C%BA.jpg)

压住接线端子解锁扣，断开舵机连接线缆。

![舵机线缆2.jpg](https://wiki.bambulab.com/h2/maintenance/servomotor-replacement/%E8%88%B5%E6%9C%BA%E7%BA%BF%E7%BC%862.jpg)

### 6.安装新的风门舵机

安装舵机时，请确保线缆朝上方向定位。**依次安装上下两颗固定螺丝，其中第一颗螺丝初步锁入即可，无需完全拧紧。待两颗螺丝均安装到位后，再同时均匀拧紧，确保舵机稳固安装并避免偏移**。

![线缆朝上.jpg](https://wiki.bambulab.com/h2/maintenance/servomotor-replacement/%E7%BA%BF%E7%BC%86%E6%9C%9D%E4%B8%8A.jpg)

舵机安装完成后，连接舵机线缆。

![安装卡扣.jpg =600x](https://wiki.bambulab.com/h2/maintenance/servomotor-replacement/%E5%AE%89%E8%A3%85%E5%8D%A1%E6%89%A3.jpg)

### 7.安装齿轮

安装齿轮时，**首先需要确保风门处于最顶端位置**，然后将齿轮压入舵机输出轴，需要保证**齿轮上磁铁槽为水平状态**。

|  |  |
| --- | --- |
|  |  |

齿轮安装完成之后，两齿面平齐即为正确安装。

![红线对齐.jpg =600x](https://wiki.bambulab.com/h2/maintenance/servomotor-replacement/%E9%BD%BF%E9%9D%A2%E5%AF%B9%E9%BD%90.jpg)

### 8.安装螺丝和磁铁

接下来安装齿轮与舵机轴固定螺丝（**注意避免过度锁紧**），安装完成后需确保齿轮上的**磁铁槽处于水平位置**。  
![舵机螺丝1.jpg](https://wiki.bambulab.com/h2/maintenance/servomotor-replacement/%E8%88%B5%E6%9C%BA%E8%9E%BA%E4%B8%9D1.jpg)  
随后安装磁铁，应将磁铁上带有**红色标记的一端准确对准霍尔传感器**（如下图所示），以确保信号识别准确与系统正常运行。

![抬起安装前齿轮.jpg =600x](https://wiki.bambulab.com/h2/maintenance/servomotor-replacement/%E7%BA%A2%E7%BA%BF%E5%AF%B9%E9%BD%90.jpg)

> 注意：需确保磁铁处于水平位置，并将红色标记端精确对准霍尔传感器。若安装偏差，可能导致风门舵机发生失步，从而无法正确开启或关闭风门，影响系统正常运行。

### 9.安装背板

完成风门舵机更换后您可以将[背板安装回打印机](replace-rear-panel.md)，如果您需要继续更换排气格栅舵机，可以等更换完成排风格栅舵机后再安装背板。

## 更换排气格栅舵机

### 1.移除背板

由于排气格栅舵机安装在机箱内部，因此对排风格栅舵机拆装需要移除打印机背板，接下来您需要移动到打印机的背面，可以[参考这篇指南来移除打印机背板。](replace-rear-panel.md)

### 2. 移除排气格栅舵机

排气格栅舵机位于电源模块左侧和风门舵机下方。  
![排气格栅舵机.png](https://wiki.bambulab.com/h2/maintenance/servomotor-replacement/%E6%8E%92%E6%B0%94%E6%A0%BC%E6%A0%85%E8%88%B5%E6%9C%BA.png)  
移除舵机上下两颗固定螺丝。

![格栅舵机.jpg =600x](https://wiki.bambulab.com/h2/maintenance/servomotor-replacement/%E6%A0%BC%E6%A0%85%E8%88%B5%E6%9C%BA.jpg)

### 3. 断开线缆并移除舵机

断开线缆时，应按住解锁扣的同时轻轻拔出线缆，避免因用力不当损坏连接器或线缆本体。

![img_20250421_190355.jpg](https://wiki.bambulab.com/h2/maintenance/servomotor-replacement/img_20250421_190355.jpg)

### 4.移除舵机齿轮

取出舵机后，需先卸下舵机轴上的固定螺丝，再移除齿轮。。

![移除舵机螺丝.jpg =600x](https://wiki.bambulab.com/h2/maintenance/servomotor-replacement/%E7%A7%BB%E9%99%A4%E8%88%B5%E6%9C%BA%E8%9E%BA%E4%B8%9D.jpg)

### 5.将齿轮安装至新舵机

将齿轮安装至新的舵机轴上，并锁入固定螺丝。

![安装齿轮.jpg =600x](https://wiki.bambulab.com/h2/maintenance/servomotor-replacement/%E5%AE%89%E8%A3%85%E9%BD%BF%E8%BD%AE.jpg)

> 注意：螺丝锁紧力度适中，避免过度用力导致螺纹滑牙，影响后续稳定性与维修操作。

### 6.安装舵机

安装舵机时需将**排气格栅齿条向上顶起**，并确保**排气格栅处于关闭状态**。在顶住排气格栅齿条的同时，锁入固定螺丝。

![关闭.jpg](https://wiki.bambulab.com/h2/maintenance/servomotor-replacement/%E5%85%B3%E9%97%AD.jpg)

**依次安装上下两颗固定螺丝，其中第一颗螺丝初步锁入即可，无需完全拧紧。待两颗螺丝均安装到位后，再同时均匀拧紧，** 确保舵机稳固安装并避免偏移。

|  |  |
| --- | --- |
|  |  |

> 注意：安装时需确保舵机线缆朝上布置，并**确认排气格栅处于关闭状态**。若安装位置不当，可能导致舵机失步，进而造成排气格栅无法正常开启或关闭。

### 7.连接舵机线缆

将线缆接头插入，直到听到或感觉到塑料卡扣卡住。

![安装卡扣.jpg =600x](https://wiki.bambulab.com/h2/maintenance/servomotor-replacement/%E5%AE%89%E8%A3%85%E5%8D%A1%E6%89%A3.jpg)

### 8.安装背板

完成所有的安装后，建议您跳过此步骤进行功能验证，**确认舵机功能一起正常后再安装打印机背板。**

[H2D 背板更换指南](replace-rear-panel.md)

## 功能验证

> ⚠️**注意!** 完成舵机更换后，如果出现风门运动异常，如只向一个方向运动然后卡住，并报错过滤风门错误 请参考[【更换 H2D 右内衬上盖/腔温加热组件/腔温加热循环风扇 | Bambu Lab Wiki】](repalce-right-inner-lining.md) -“齿轮位置校准”，重新校准舵机齿轮。

### 风门舵机验证

为打印机接通电源，进入控制界面点击空调系统，将冷却模式调整为仓温模式，此时观察到风门正常上升下降即为正确安装。  
![1280x1280.png](https://wiki.bambulab.com/h2/maintenance/servomotor-replacement/1280x1280.png)

![过滤切换风门](https://wiki.bambulab.com/h2/manual/h2d-intro/9.gif)

如果风门无法正常上升或下降，请参考安装[步骤 7 和 8](#step7) ，确保安装时风门位于最顶端位置，同时确认磁铁保持水平且带有红色标记的一端朝向霍尔传感器。

### 排气格栅舵机验证

为打印机接通电源，进入控制界面点击**空调系统 => 冷却模式 => 外排**，此时可以观察到排气格栅正常开启和关闭即为正确安装。

|  |  |
| --- | --- |
|  |  |

![排气格栅和腔体外排风扇](https://wiki.bambulab.com/h2/manual/h2d-intro/8.gif)

若排气格栅不能正常开启或关闭，请参阅安装[步骤 6](#step6)，确保安装时排气格栅处于关闭状态，并检查舵机齿轮与齿条是否正确啮合。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南并未解决您的问题，[*请点击此处联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
