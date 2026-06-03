---
path: zh/h2/maintenance/replace-inner-lining-left
title: "更换 H2 系列左内衬"
description: "本文将详细为您介绍 H2 系列更换左内衬的详细步骤和注意事项。"
tags: ["h2"]
created: 2026-01-08T08:44:37.949Z
updated: 2026-05-09T08:23:30.040Z
source: https://wiki.bambulab.com/zh/h2/maintenance/replace-inner-lining-left
---

## 左内衬

左内衬是位于打印机后部左侧的塑料支架，用于承载 MC 板、AC 板、4-pin 接口板等电路元件及废料滑梯、吐料组件、内置气泵等配件，并将其与打印腔室隔离。

![replace-inner-lining-left-cover-1.jpg](https://wiki.bambulab.com/h2/maintenance/replace-inner-lining-left/replace-inner-lining-left-cover-1.jpg)

**左内衬的备件中包含以下物品：**

- 左内衬\*1；
- BT3-12 螺丝\*2 ：赠送热床线固定扣（锁线夹）的螺丝；
- BT3-8 螺丝\*2 ：左内衬上方固定螺丝；
- ST3-8 螺丝\*2 ：左内衬下方固定螺丝；
- 卡线扣\*2 ：撕下背胶即可粘在左内衬内帮助理线；
- 热床线固定扣\*1：用于固定热床线等线缆。

## 适用打印机型号

**H2S、H2C、H2D、H2D Pro**

## 何时更换

打印机左内衬出现变形或损坏。

## 所需工具和材料

- 新的左内衬（请[联系我们](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)获取）
- H2.0 内六角扳手
- H1.5 内六角扳手
- 平头镊子
- 十字螺丝刀
- [螺丝托盘（可选）](https://makerworld.com.cn/zh/models/720921-ke-dui-die-fen-lei-tuo-pan?from=search#profileId-676625)

> 该指南涉及螺丝类型较多，可选择打印螺丝托盘，按拆装顺序整理收纳，以确保使用正确的螺丝型号。

## 安全提示

> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生屏幕误触或电路短路从而引起额外的电子设备损坏和安全隐患。  
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 移除旧的左内衬

### 1.降低热床

通过屏幕控制热床降至底部，控制工具头移动至最左侧，为后续移除左内衬保留操作空间。然后，确认喷嘴及热床冷却至室温后，关闭打印机并断开电源线。

|  |  |
| --- | --- |
|  |  |

### 2. 移除护线盖

使用 H2.0 内六角扳手拧下 1 颗固定螺丝（BT2.6x8）;

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-ap-board/image-6.png)

从靠近前门的一侧取下 AP 板盖;

|  |  |
| --- | --- |
|  |  |

手指扣住下图绿色标注位置缺口，沿红色箭头方向，将护线盖移除。

|  |  |
| --- | --- |
|  |  |

### 3. 移除打印机背板

移除排烟管转接件（若有）的 4 颗固定螺丝。

![](https://wiki.bambulab.com/h2/laser/image-87.png)

移除打印机背板固定螺丝，即可取下背板：

- 红色圆圈标记的 11 颗螺丝（ST3×6）
- 绿色方框标记的 12 颗螺丝（BT3×8）
- 黄色方框标记的 2 颗外挂料盘固定螺丝（M3x12）

![](https://wiki.bambulab.com/h2/maintenance/replace-rear-panel/image-29.png)

详细步骤您可以参考这篇 Wiki 来[移除 H2 系列打印机背板](replace-rear-panel.md) 。

### 4. 移除吐料组件和废料滑梯

松开下图绿色方框的 2 颗吐料组件固定螺丝（BT3x8），向上移除吐料组件；

|  |  |
| --- | --- |
|  |  |

松开下图红色圆圈的废料滑梯固定螺丝（BT3x8），向下拉，移除废料滑梯；

|  |  |
| --- | --- |
|  |  |

### 5. 移除内置气泵（若有）

若打印机为激光版，请先移除位于打印机右下角的内置气泵。

![气泵位置.jpg](https://wiki.bambulab.com/h2/maintenance/built-in-air-pump/%E6%B0%94%E6%B3%B5%E4%BD%8D%E7%BD%AE.jpg)

详细步骤您可以参考这篇 Wiki 以[移除内置气泵](built-in-air-pump.md)。

### 6. 移除 4-pin 接口板

移除连接线，用 H2.0 扳手松开两颗固定螺丝，向前移除 4-pin 接口板。

|  |  |
| --- | --- |
|  |  |

### 7. 移除 AC 板理线盖和 AC 板

|  |  |
| --- | --- |
|  |  |

详细步骤您可以参考这篇 Wiki 以[移除 H2 系列 AC 板](replace-ac-board-for.md)。

### 8. 移除 MC 板

移除 MC 板上所有连接线，用 H1.5 内六角扳手拧开 6 颗固定螺丝，移除 MC 板。

![screws_location_for_mc_board1.jpg](https://wiki.bambulab.com/h2/maintenance/replace-inner-lining-left/screws_location_for_mc_board1.jpg)

详细步骤您可以参考以下 Wiki 以移除 MC 板：

- [H2D/H2C](replace-mc-board.md)
- [H2S](../../h2s/maintenance/replace-mc-board.md)

> 移除 MC 板后，单独的线缆有： 4-pin 接口板连接线、AC-MC 连接线、内置气泵连接线（若为激光版）。请妥善保管防止丢失。  
> ![seperate_cables.jpg](https://wiki.bambulab.com/h2/maintenance/replace-inner-lining-left/seperate_cables3.jpg)

### 9. 移除左内衬

使用 H2.0 内六角扳手先移除 1 颗热床线固定扣固定螺丝（BT3x12），将固定扣打开，将所有线缆一起从固定扣取出，然后移除另 1 颗固定螺丝；

|  |  |
| --- | --- |
|  |  |

将热床固定扣中的所有线缆从下图所示理线扣中取出；并撕开泡棉，然后使用 H2.0 内六角扳手移除一颗热床地线固定螺丝（STW3x5），将所有线缆从左内衬下方卡扣中取出；

|  |  |
| --- | --- |
|  |  |

将热床线束从左内衬间隙中穿过取出，然后将左侧线缆从卡扣中取出；

|  |  |
| --- | --- |
|  |  |

移除其余卡扣中的线缆；

|  |  |
| --- | --- |
|  |  |

将上方连接线从左内衬中抽出，可以暂时挂在打印机框架一侧以便后续操作；

|  |  |
| --- | --- |
|  |  |

移除左内衬 4 颗固定螺丝；将热床线置于右内衬一侧，微微弯曲左内衬，以便将两个右内衬卡扣从左内衬卡槽中分离；

|  |  |
| --- | --- |
|  |  |

取下打印板防止剐蹭；向上提左内衬，然后稍稍倾斜，从打印机前侧取出左内衬，最后将 Z 电机热床线从左内衬洞口中抽出。

|  |  |
| --- | --- |
|  |  |

> **注意**：若取出过程中，左右内衬卡扣不慎断裂，**不影响其正常使用**。请确认热床及喷嘴温度为室温，工具头移动至最右侧，取出过程中注意避让辅助部件冷却风扇、工具头及热床，以免损坏其他部件。

### 10. 移除 MC 板风扇

一只手向前拉住 MC 板风扇，另一只手按住白色软螺钉，依次向前拔出四颗软螺钉，移除 MC 板风扇。

|  |  |
| --- | --- |
|  |  |

## 安装新的左内衬

### 1. 安装 MC 板风扇和卡线扣

将软螺钉从外侧穿过左内衬上的小孔，然后拉住 MC 板风扇软螺钉前端；从左内衬外侧拉动软螺钉长端以固定，依次将四个软螺钉安装到位；

|  |  |
| --- | --- |
|  |  |

> 若安装或移除 MC 板风扇时不慎使软螺钉脱离，请使用 H1.5 内六角扳手辅助重新安装；
>
> |  |  |
> | --- | --- |
> |  |  |

在下图所示位置粘贴卡线扣。  
![install_clips.jpg](https://wiki.bambulab.com/h2/maintenance/replace-inner-lining-left/install_clips.jpg)

### 2. 安装左内衬

将 Z 电机热床线从左内衬洞口中放入；稍稍倾斜左内衬，从打印机前侧重新放回左内衬；

|  |  |
| --- | --- |
|  |  |

稍微弯曲左内衬，将右内衬卡扣卡入左侧卡槽中，重新固定左内衬 4 颗固定螺丝；

|  |  |
| --- | --- |
|  |  |

> **注意**：若安装过程中，左右内衬卡扣不慎断裂，**不影响其正常使用**。请确认热床及喷嘴温度为室温，安装过程中注意避让辅助部件冷却风扇、工具头及热床，以免损坏其他部件。

### 3. 整理连接线

以 H2C 激光版为例，将上方连接线从左内衬中重新穿过，根据下图重新整理所有线缆（该步骤序号与下步骤 MC 板接口序号一致）；

|  |  |
| --- | --- |
|  |  |

| 序号 | 图片 | 备注 | 序号 | 图片 | 备注 | 序号 | 图片 | 备注 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 |  |  | 13 |  |  | 25 |  |  |
| 2 |  | H2S 无该线缆 | 14 | 空闲 | 暂未使用 | 26 |  |  |
| 3 |  |  | 15 |  |  | 27 |  |  |
| 4 |  |  | 16 |  |  | 28 |  |  |
| 5 |  |  | 17 |  | H2S 无该线缆 | 29 |  |  |
| 6 |  |  | 18 |  |  | 30 |  | 非激光版本（无内置气泵）时，无该线缆 |
| 7 |  | 在 MC 板的背面 | 19 |  | H2S 无该线缆 | 31 | 空闲 | 暂未使用 |
| 8 |  | 仅 H2C 有该线缆 | 20 |  |  | 32 | 空闲 | 暂未使用 |
| 9 |  |  | 21 |  |  | A |  | 左边的电机 (从后背板往前看) |
| 10 |  |  | 22 |  |  | B |  | 右边的电机 (从后背板往前看) |
| 11 |  |  | 23 |  | H2S 无该线缆 | Z |  |  |
| 12 |  |  | 24 |  |  |  |  |  |

> 安装连接线时，请注意将热床线缆单独分离开，防止其他线缆缠绕，影响热床正常移动。  
> ![heatbed_cable_position.png](https://wiki.bambulab.com/h2/maintenance/replace-inner-lining-left/heatbed_cable_position.png)

### 4. 安装 MC 板

插入 MC 板背面的电源插头，将 MC 板对准内衬上的小孔；

|  |  |
| --- | --- |
|  |  |

用 H1.5 内六角扳手固定 6 颗固定螺丝，重新安装 MC 板上所有连接线。

|  |  |
| --- | --- |
|  |  |

详细步骤您可以参考以下 Wiki 以安装 MC 板:

- [H2D/H2C](replace-mc-board.md)
- [H2S](../../h2s/maintenance/replace-mc-board.md)

### 5. 安装 AC 板理线盖和 AC 板

|  |  |
| --- | --- |
|  |  |

详细步骤您可以参考这篇 Wiki 以[安装 AC 板](replace-ac-board-for.md)。

### 6. 安装 4-pin 接口板

将 4-pin 接口板重新装回卡槽中，用 H2.0 扳手重新安装 2 颗固定螺丝，重新安装连接线。

|  |  |
| --- | --- |
|  |  |

### 7. 安装内置气泵（若有）

若打印机为激光版，请重新安装位于打印机右下角的内置气泵。

![气泵位置.jpg](https://wiki.bambulab.com/h2/maintenance/built-in-air-pump/%E6%B0%94%E6%B3%B5%E4%BD%8D%E7%BD%AE.jpg)

详细步骤您可以参考这篇 Wiki 以[安装内置气泵](built-in-air-pump.md)。

> 注意正确放置热床线，以防有阻碍物，影响热床正常移动。  
> ![热床线缆.jpg](https://wiki.bambulab.com/h2/maintenance/built-in-air-pump/%E7%83%AD%E5%BA%8A%E7%BA%BF%E7%BC%86.jpg)

### 8. 安装吐料组件和废料滑梯

将吐料组件重新放入原位，将插销插入内衬中，并对准螺丝孔位；

|  |  |
| --- | --- |
|  |  |

对准废料滑梯下方 2 个卡扣位置，往前推，使这 2 个卡扣与内衬上的孔洞咬合。装回后，需检查螺丝孔位是否对齐；

|  |  |
| --- | --- |
|  |  |

> 注：在安装废料滑梯的时候，需要注意将废料滑梯的两侧扣在内衬的外侧，如果扣在内侧可能无法正常安装。
>
> ![](https://wiki.bambulab.com/h2/maintenance/replace-purge-chute/image-22.png)

重新安装吐料组件及废料滑梯固定螺丝，绿色方框标注为 2 颗吐料组件固定螺丝（BT3x8），红色圆圈标注为 1 颗废料滑梯固定螺丝（BT3x8）。  
![remove_purge_screws1.jpg](https://wiki.bambulab.com/h2/maintenance/replace-inner-lining-left/remove_purge_screws_1xx.jpg)

### 9. 安装打印机背板

重新拧上打印机背板固定螺丝，即可安装背板：

- 红色圆圈标记的 11 颗螺丝（ST3×6）
- 绿色方框标记的 12 颗螺丝（BT3×8）
- 黄色方框标记的 2 颗外挂料盘固定螺丝（M3x12）

![](https://wiki.bambulab.com/h2/maintenance/replace-rear-panel/image-29.png)

详细步骤您可以参考这篇 Wiki 来[安装 H2 系列打印机背板](replace-rear-panel.md) 。

重新安装排烟管转接件（若有）的 4 颗固定螺丝。

![](https://wiki.bambulab.com/h2/laser/image-87.png)

### 10. 安装护线盖及 AP 板盖

对准卡槽，重新安装护线盖。

![remove_cable_cover.jpg](https://wiki.bambulab.com/h2/maintenance/replace-inner-lining-left/install_cable_management_cover.jpg)

先从靠近打印机背面的一侧扣回 AP 板盖，将箭头所示的两处均按压到位，右侧与缓冲器齐平，底部与护线盖齐平，然后使用 H2.0 内六角扳手拧紧一颗固定螺丝（BT2.6x8）。

|  |  |
| --- | --- |
|  |  |

## 功能验证

### 根据电路板指示灯状态判断

**正常状态：MC 板指示灯常亮（左上）、慢速闪烁（左下）、快速闪烁（右）**

可先预装盖子并拧上少量螺丝（小心用电安全，断电操作），再通电检查该电路板灯语是否正常，若灯语正常，请再拧上剩余螺丝，减少返工；若灯语异常，请检查所有连接并重试。

<https://public-cdn.bblmw.com/wiki/H2D/MC1.mp4>

- 本视频包含了开机后的初始化状态，故左下的指示灯有一小段常亮。

### 连接电源线并打开电源，运行校准，检查是否有报错

接上打印机电源，开启打印机，在屏幕上操作，运行校准流程，如成功校准，说明上述操作成功。

![heatbed_cable_position.png](https://wiki.bambulab.com/h2/maintenance/replace-inner-lining-left/calibration_zh_202601.png)

否则，请再次检查所有连接并重试。如果仍然不行，请[联系 Bambu Lab 服务团队](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)寻求进一步帮助。

## 潜在问题及解决方案

若校准时，打印机报错：Z 轴回零失败，并观察到热床无法上升至最高点。请重新检查热床线线缆运动是否被其他线缆或组件阻碍。

![热床线缆.jpg](https://wiki.bambulab.com/h2/maintenance/built-in-air-pump/%E7%83%AD%E5%BA%8A%E7%BA%BF%E7%BC%86.jpg)

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
