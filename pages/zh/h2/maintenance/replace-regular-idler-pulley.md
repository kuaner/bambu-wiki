---
path: zh/h2/maintenance/replace-regular-idler-pulley
title: "更换 H2 系列框架惰轮"
description: "本文提供 H2 系列打印机框架惰轮的更换步骤与关键安全注意事项。"
tags: []
created: 2025-09-25T06:06:47.403Z
updated: 2026-03-24T09:42:27.532Z
source: https://wiki.bambulab.com/zh/h2/maintenance/replace-regular-idler-pulley
---

## 套件清单

适用于 H2 系列（含 H2D、H2S）的 框架惰轮套件包含：

- 标准惰轮 ×1
- 惰轮轴 ×1（长）
- 张紧器惰轮轴 ×1（短）
- 石墨垫圈 ×2

![](https://wiki.bambulab.com/h2/maintenance/replace-regular-idler-pulley/00000018.png)

## 适用机型

H2D、H2S、H2C、H2D Pro

## 何时需要更换

- 框架惰轮出现异常噪音
- 惰轮或其轴承损坏

## 所需工具

- H2.0 内六角扳手
- H1.5 内六角扳手

## 抬起打印机上盖组件

### 步骤 1. 移除背板

依次拆下 **11 颗钣金自攻螺钉（ST3×6）** 与 **12 颗塑料自攻螺钉（BT3×8）**。

> 建议提前准备两个小盒子，分别存放两种规格的螺钉，避免混淆。

1. 使用 H2.0 直柄内六角扳手移除 11 颗 ST3×6（前面图片中的红色圆圈标记， ST3×6）
2. 使用 H2.0 直柄内六角扳手移除 12 颗 BT3×8（前面图片中的绿色方框标记，BT3×8）
3. 黄色标记为外挂料盘固定螺钉（M3×12）

![](https://wiki.bambulab.com/h2/maintenance/replace-rear-panel/image-29.png)

4. 按压气管接头以避开干涉，然后将背板向后轻轻倾斜并取出。

![](https://wiki.bambulab.com/h2/maintenance/replace-rear-panel/image-31.png)

您可以参阅这 [更换 H2系列背板](replace-rear-panel.md) 中的说明，了解拆卸背板的详细步骤。

### 步骤 2. 移除右侧板

1. 撬开硅胶条开口，用 H2.0 内六角扳手拆下两颗固定螺丝（ST3×3）。

> 若开口不易掀起，可用内六角扳手的刀柄端/短臂辅助撬开，注意勿划伤面板。

|  |  |
| --- | --- |

3. 使用 H2.0 内六角扳手拆下侧板内侧的两颗固定螺丝（BT3×8）。

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-38.png)

4. 拆卸横梁与侧边的固定螺丝（BT3×8）。

![](https://wiki.bambulab.com/h2s/maintenance/replace-side-panel/20250902-162020_compressed.jpg)

5. 双手握住右侧板靠近机背的一侧，向外用力掰开以解锁后部卡扣；随后依次解锁顶部卡扣与前门侧卡扣。

> 提示：顶部卡扣可用 H2.0 内六角扳手的撬动辅助解锁。

|  |  |  |
| --- | --- | --- |

您可以参阅这 [更换 H2S 左/右侧板](../../h2s/maintenance/replace-side-panel.md) 或 [更换 H2D 左/右侧板](replace-side-panel-with-glass-window.md)中的说明，了解拆卸右侧板的详细步骤。

### 步骤 3. 移除前门玻璃/左侧盖板

1. 用 H2.0 内六角扳手移除固定前门的 4 颗螺丝（M3x3，螺帽直径 10mm），上下各 2 颗，然后一只手扶住前门玻璃，将前门取下。

> 注意用手扶住前门玻璃，防止跌落。

|  |  |
| --- | --- |

2. 由于有一颗侧板固定螺丝位于辅助部件冷却风扇后方，需先取下风扇。该风扇由上排两颗软螺钉与下排两颗螺丝固定。请先使用 H2.0 内六角扳手拆下下排两颗 BT3×16，用力直拔风扇以便取出上排软螺钉，随后将风扇放置在热床上；无需从 MC 板断开连接线。

![](https://wiki.bambulab.com/h2/maintenance/replace-side-panel-with-glass-window/image-77.png)

3. 使用 H2.0 内六角扳手依次拆下上框两颗 BT3×8 与横梁一颗 BT3×8。

|  |  |
| --- | --- |

4. 两颗锁在立柱的螺丝（M3×3），这两颗螺丝在胶条后面，您需要从胶条的开孔处撬开胶条，然后即可看见螺丝。

|  |  |  |
| --- | --- | --- |

您可以参阅这 [更换 H2S 左/右侧板](../../h2s/maintenance/replace-side-panel.md) 或者 [更换 H2D 左/右侧板](replace-side-panel-with-glass-window.md)中的说明，了解拆卸左侧板的详细步骤。

### 步骤 4. 移除切刀顶块

您可以使用 H2.0 内六角扳手来移除切刀顶块的四颗固定螺丝（红色圆圈标记：BT2.6x8；蓝色方块标记：M2.5x5）。

|  |  |
| --- | --- |

### 步骤 5. 断开 AP 板部分线缆

依次断开下列线缆（见图中编号）：

- MC–AP 通信线（图中 1）
- MC–AP 供电线（图中 2）
- 实况摄像头连接线（经 AP 中转，图中 3）
- USB-C 数据线（图中 4）
- TH 供电线（图中 5）

![](https://wiki.bambulab.com/h2/maintenance/replace-regular-idler-pulley/00000019.png)

### 步骤 6. 断开前门立柱霍尔传感器

在前门立柱（靠启动/暂停按钮一侧）找到霍尔传感器插头，拔出插头，避免后续操作拽拉线缆。

|  |  |
| --- | --- |

### 步骤 7. 撕开前门立柱上的醋酸胶带

撕开启动/暂停按钮一侧底部的醋酸胶带，将线束理直并预留余量，以便后续操作。

|  |  |
| --- | --- |

### 步骤 8. 撕开侧边实况摄像头排线固定胶

在 USB 接口板一侧，找到实况摄像头排线（FFC）的固定胶/胶带，小心撕开以释放排线。

![](https://wiki.bambulab.com/h2/maintenance/replace-regular-idler-pulley/00000003.webp)

### 步骤 9. 解除线缆卡扣

解除线缆卡扣（位于缓冲块旁），避免干扰后续步骤。

![](https://wiki.bambulab.com/h2/maintenance/replace-regular-idler-pulley/00000016.png)

### 步骤 10. 抬起上盖

1. 使用 H2.0 内六角扳手，依次移除 8 颗固定螺丝（M3×10），每个立柱各 2 颗。

|  |  |
| --- | --- |
|  |  |

2. 向上抬起上盖，并向远离惰轮的一侧轻移，为拧动惰轮螺丝轴预留操作空间。

> 提醒：无需将上盖完全抬起，仅需预留出操作空间即可；请妥善避让线缆，避免牵拉导致损伤。

![](https://wiki.bambulab.com/h2/maintenance/replace-enclosure-top-fame/image-96.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-regular-idler-pulley/00000011.png)

## 移除框架惰轮

1. 使用 H2.0 内六角扳手移除任意一侧 的 2 颗工具头上皮带压块的螺丝（M3x8），释放皮带；

![](https://wiki.bambulab.com/h2s/maintenance/replace-xy-belt/001_(1).png)

1. 使用 H2.0 内六角扳手/螺丝刀先将轴端能旋出多少就旋出多少。接着做小角度左右旋转，缓慢带出轴，保持同轴直线外拉，不要折弯。

|  |  |
| --- | --- |

> **补充：对于靠近 USB 接口板一侧（深孔）建议顺序**
>
> 1. 仍先用 H2.0 尽量将轴端旋出/松出。
> 2. 待轴基本不再转动/露出有限时，使用 H2.0 移除 2 颗固定实况摄像头的螺丝（M3×6）：
>
> |  |  |
> | --- | --- |
>
> 3. 轻移摄像头以腾出下方通道，用直径小于 H1.5 的硬质细杆自底部沿轴心平直顶出轴
>
> ![](https://wiki.bambulab.com/h2/maintenance/replace-regular-idler-pulley/00000004.webp)

2. 待轴抽出后，从侧面托住惰轮，连同石墨垫圈一起取出。

## 更换框架惰轮

1. 在惰轮内圈/端面点涂极**少量润滑脂**，避免沾到皮带接触面。接着将石墨垫圈贴放在惰轮对应面，使其先与惰轮结合，**便于后续就位时不滑落**。涂抹位置如下：

![](https://wiki.bambulab.com/h2/maintenance/replace-regular-idler-pulley/00000020.png)

> **注意：** 在惰轮两侧都安装石墨垫圈。

![](https://wiki.bambulab.com/h2/maintenance/replace-regular-idler-pulley/00000013.png)

2. 将惰轮沿原位置放回支座内，接着插入惰轮轴，用 H2.0 内六角扳手拧紧。

![](https://wiki.bambulab.com/h2/maintenance/replace-regular-idler-pulley/00000006.webp)

![](https://wiki.bambulab.com/h2/maintenance/replace-regular-idler-pulley/00000010.webp)

> **注意：** 请确保在插入过程中石墨垫圈不会脱落。

3. 将皮带固定座装入工具头，并使用 H2.0 内六角扳手拧紧2颗固定螺丝（M3x8）。

![](https://wiki.bambulab.com/h2s/maintenance/replace-xy-belt/001_(1).png)

> **注意：** 由于皮带处于张紧状态，您需要用手将皮带固定块往里推，然后使用 H2.0 内六角扳手拧紧2颗螺丝（M3x8）。

## 安装打印机上盖组件

### 步骤 1. 安装上盖

1. 参考下图，将上盖组件重新插入打印机框架；对准左后方的线缆走线位置，沿该参照缓慢放入定位。

> **注意：** 安装前，请确认所有线缆已远离边缘，防止夹线。

|  |  |  |
| --- | --- | --- |

2. 使用 H2.0 内六角扳手拧紧 8 颗固定螺丝（M3×10），每根立柱各 2 颗。

|  |  |
| --- | --- |
|  |  |

### 步骤 2. 扣回线缆卡扣

对准键位后按压线缆卡扣，确认不会松脱。

![](https://wiki.bambulab.com/h2/maintenance/replace-regular-idler-pulley/00000016.png)

### 步骤 3. 粘贴侧边实况摄像头排线固定胶

在 USB 接口板一侧找到实况摄像头排线（FFC）的固定胶，按原有粘贴痕迹将其复位粘回。

### 步骤 4. 粘贴前门立柱上的醋酸胶带

将线束理顺拉直，按原有路径将多余长度整齐回收，并用醋酸胶带粘贴固定。

|  |  |
| --- | --- |

### 步骤 5. 连接前门立柱霍尔传感器

在前门立柱（靠启动/暂停按钮一侧）找到霍尔传感器插座，将插头按位插回并确认卡紧，避免后续操作中被拉拽松脱。

|  |  |
| --- | --- |

### 步骤 6. 安装 AP 板线缆

依次连接下列线缆（见图中编号）：

- MC–AP 通信线（图中 1）
- MC–AP 供电线（图中 2）
- TH 供电线（经 AP 中转，图中 3）
- USB-C 数据线（图中 4）
- 实况摄像头连接线（图中 5）

![](https://wiki.bambulab.com/h2/maintenance/replace-regular-idler-pulley/00000019.png)

### 步骤 7. 安装切刀顶块、左右侧板、前门玻璃、背板

参考 [更换 H2S 上盖组件](../../h2s/maintenance/replace-enclosure-top-frame.md)，依次安装切刀顶块、左右侧板、前门玻璃与背板。

## 张紧皮带

1. 拧松皮带张紧器左侧和右侧共 4 个螺丝。拧松 1-2 圈即可，请勿卸下螺丝；

|  |  |
| --- | --- |

2. 轻轻地前后来回移动工具头几次，最后将其移至打印机后端；

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/belt-tension/3.webp)

移动后，确保工具头和线轨位置如下图所示，即位于最后方，再进行下一步。

3. 再次拧紧 4 颗螺丝。皮带张紧器中的弹簧结构会将皮带张紧至正确的张紧度。

|  |  |
| --- | --- |

> 注意：请勿将螺钉拧得过紧，以免滑丝。

4. 完成皮带张紧后，请重新执行共振频率识别，以记录设备的最新共振特性。可在机器屏幕或 Bambu Studio 中进行该校准操作。

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/belt-tension/belt-tension-7.png)

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/belt-tension/belt-tension-9.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)；点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
