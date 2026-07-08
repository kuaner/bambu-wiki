---
path: zh/h2/maintenance/hotend-heating-assembly
title: "更换 H2D/H2C 左右热端加热组件"
description: "本文介绍如何更换 H2D/H2C 左右热端加热组件"
tags: []
created: 2025-03-25T08:46:41.904Z
updated: 2026-06-23T08:11:16.153Z
source: https://wiki.bambulab.com/zh/h2/maintenance/hotend-heating-assembly
---

## 热端加热组件

> H2C 和 H2D 左热端加热组件拆装步骤几乎一致。

在 H2D 打印机上有两个热端加热组件，左右热端加热组件互不通用，如果其中一个损坏，您需要选择对应的热端加热组件进行更换。左右热端加热组件以及配件明细如下：

**左热端加热组件：**

- 左热端加热组件（预装理线片） × 1
- 挡风片 × 1
- M1.6×4 螺丝（用于固定理线片和挡风片） × 2
- M2.5×7 螺丝（用于固定左热端加热组件） × 4  
  ![pixpin_2025-07-11_21-53-17.png](https://wiki.bambulab.com/h2/maintenance/hotend-heating-assembly-new/pixpin_2025-07-11_21-53-17.png)

**右热端加热组件：**

- 右热端加热组件 × 1
- 隔热片 × 1
- M3×10 螺丝 × 3

![](https://wiki.bambulab.com/h2/maintenance/hotend-heating-assembly/image-10.png)

> 部分批次的备件包装中包含一管白色电子硅胶。如果您收到了这管硅胶，可以选择将其丢弃或保留用于其他用途。在本文的拆装步骤中，无需使用该电子硅胶。  
> ![sillicon_glue.png](https://wiki.bambulab.com/h2/maintenance/hotend-heating-assembly/sillicon_glue.png)

> 部分批次的备件配套有新版泡棉，其功能与现有泡棉保持一致，仅外观有所调整。  
> 若原有泡棉在拆卸过程中未受损，可继续使用原有泡棉。  
> 若原有泡棉在拆卸过程中出现损坏，可更换为新版泡棉。  
> ![20250911-101347.jpg](https://wiki.bambulab.com/h2/maintenance/hotend_blob/20250911-101347.jpg)

> **注意：**请使用 H2D 热端加热组件；H2D 和 A1 系列的热端加热组件**无法兼容**。H2D 加热组件专为 H2D 打印机优化设计，具有更高的适配性。

## 何时更换

- 热端加热功能异常
- 卡扣无法锁紧热端

## 所需的工具和材料

- 新的热端加热组件（左/右，请根据实际情况更换对应的配件）
- H2.0 内六角螺丝刀
- H1.5 内六角螺丝刀

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。
>
> 如果您对本指南有任何疑问，[*请联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im?from=5)，我们将及时回复并为您提供所需的帮助。

## 更换左热端加热组件

### 移除左热端加热组件

#### 步骤 1：移除工具头左热端

将热端切换至左热端，关闭打印机电源并断开电源线，随后移除硅胶套和左热端。

|  |  |
| --- | --- |
|  |  |

#### 步骤 2：移除部件冷却风扇和风道

您可以参考以下视频或 [Wiki](replace-part-cooling-fan.md)来移除部件冷却风扇和风道：

|  |  |
| --- | --- |
| Part cooling fan | Air duct |

#### 步骤 3：移除左热端加热组件

使用 H2.0 内六角螺丝刀移除四颗热端固定螺丝（M2.5x7）.

![](https://wiki.bambulab.com/h2/maintenance/hotend-heating-assembly-new/%E5%B7%A6%E5%96%B7%E5%98%B44%E9%A2%97%E8%9E%BA%E4%B8%9D.jpg)

然后使用 H1.5 内六角螺丝刀移除两颗理线片/挡风片固定螺丝（M1.6x4）

![](https://wiki.bambulab.com/h2/maintenance/hotend-heating-assembly-new/%E6%8C%A1%E9%A3%8E%E7%89%87%E8%9E%BA%E4%B8%9D.jpg)

然后将左热端加热组件连接线从线扣中取出，并撕开泡棉和 TH 板的粘接，断开左热端加热组件与 TH 板连接。

> 注意：撕开泡棉时需要从下往上撕，避免泡棉撕开损坏。

|  |  |
| --- | --- |
|  |  |

断开线缆后，即可完全移除左热端加热组件。

![移除左喷嘴后.jpg](https://wiki.bambulab.com/h2/maintenance/hotend-heating-assembly-new/%E7%A7%BB%E9%99%A4%E5%B7%A6%E5%96%B7%E5%98%B4%E5%90%8E.jpg)

### 安装左热端加热组件

#### 步骤 1：安装左热端加热组件

先将新的左热端加热组件和理线片对准工具头上的螺丝孔位，使用 H2.0 内六角螺丝刀先拧紧四颗左热端加热组件固定螺丝（M2.5x7）。

![左喷嘴4颗螺丝.jpg](https://wiki.bambulab.com/h2/maintenance/hotend-heating-assembly-new/%E5%B7%A6%E5%96%B7%E5%98%B44%E9%A2%97%E8%9E%BA%E4%B8%9D.jpg)

然后进一步确定挡风片位置，使用 H1.5 内六角螺丝刀拧紧两颗固定螺丝（M1.6x4）。

> 注意：需要先安装**理线片**再安装**挡风片**。

![挡风片螺丝安装.jpg](https://wiki.bambulab.com/h2/maintenance/hotend-heating-assembly-new/%E6%8C%A1%E9%A3%8E%E7%89%87%E8%9E%BA%E4%B8%9D%E5%AE%89%E8%A3%85.jpg)

将左热端加热组件的线缆依次扣入两个理线槽中，然后将插头与 TH 板连接，并重新贴好泡棉。

|  |  |
| --- | --- |
|  |  |

![左侧接头.jpg](https://wiki.bambulab.com/h2/maintenance/hotend-heating-assembly-new/%E5%B7%A6%E4%BE%A7%E6%8E%A5%E5%A4%B4.jpg)

#### 步骤 2：安装部件冷却风扇和风道

您可以参考以下视频或 [Wiki](replace-part-cooling-fan.md)来安装部件冷却风扇和风道：

|  |  |
| --- | --- |
| Part cooling fan | Air duct |

#### 步骤 3：安装工具头前盖和左热端

将左热端和工具头前盖依次装回。

|  |  |
| --- | --- |
|  |  |

## 更换右热端加热组件

### 移除右热端加热组件

#### 步骤 1：移除工具头右热端

扣动底部堵嘴片，切换至右热端。

![左切换右.webp](https://wiki.bambulab.com/h2/maintenance/hotend-heating-assembly-new/%E5%B7%A6%E5%88%87%E6%8D%A2%E5%8F%B3.webp)

依次移除硅胶套和右热端。

|  |  |
| --- | --- |
|  |  |

#### 步骤 2：移除部件冷却风扇和风道

您可以参考以下视频或 [Wiki](replace-part-cooling-fan.md)来移除部件冷却风扇和风道：

|  |  |
| --- | --- |
| Part cooling fan | Air duct |

#### 步骤 3：移除右热端加热组件

使用 H2.0 内六角螺丝刀移除三颗右热端加热组件固定螺丝，然后将右热端加热组件的线缆从**摄像头支架线扣中取出**；

|  |  |
| --- | --- |
|  |  |

接下来从背部 TH 板上断开加热组件接头连接，并将隔热片取出即可。

|  |  |
| --- | --- |
|  |  |

### 安装右热端加热组件

#### 步骤 1：安装右热端加热组件

将新的隔热片装入工具头

![取出或安装垫片.jpg](https://wiki.bambulab.com/h2/maintenance/hotend-heating-assembly-new/%E5%8F%96%E5%87%BA%E6%88%96%E5%AE%89%E8%A3%85%E5%9E%AB%E7%89%87.jpg)

然后将右热端加热组件线缆装入卡线槽内。

|  |  |
| --- | --- |
|  |  |

确保左右两热端加热组件平行，使用 H2.0 内六角螺丝刀拧紧三颗固定螺丝（M3×10）。

|  |  |
| --- | --- |
|  |  |

右热端线缆装入喷嘴摄像头理线槽内。

![20250711-223153.jpg](https://wiki.bambulab.com/h2/maintenance/hotend-heating-assembly-new/20250711-223153.jpg)  
锁紧加热组件固定螺丝后，插入右加热组件线缆接头完成安装。

![右喷嘴截图2.jpg](https://wiki.bambulab.com/h2/maintenance/hotend-heating-assembly-new/%E5%8F%B3%E5%96%B7%E5%98%B4%E6%88%AA%E5%9B%BE2.jpg)

#### 步骤 2：安装部件冷却风扇和风道

您可以参考以下视频或 [Wiki](replace-part-cooling-fan.md)来安装部件冷却风扇和风道：

|  |  |
| --- | --- |
| Part cooling fan | Air duct |

#### 步骤 3：安装工具头前盖和右热端

将右热端和工具头前盖依次装回。

|  |  |
| --- | --- |
|  |  |

## 如何验证成功

连接电源并开启打印机，在屏幕上将热端温度设置为 220℃，检查热端是否正常加热。  
若热端正常加热，则更换成功；若出现报错或无法升温，请检查 TH 板上加热组件接头是否连接正确。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南未解决您的问题，[*请联系在线技术支持**（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
