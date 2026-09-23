---
path: zh/r1/maintenance/replace-y-axis-linear-rod
title: "Y 轴光轴更换指南"
description: ""
tags: []
created: 2026-09-22T13:30:08.519Z
updated: 2026-09-22T13:30:09.823Z
source: https://wiki.bambulab.com/zh/r1/maintenance/replace-y-axis-linear-rod
---

## Y 轴光轴 Y-axis Linear Rod

![001.png](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-y-axis-linear-rod/zh/001.png)

Y 轴光轴共有 2 根，从设备正面看，左侧的光轴同步轮端有一块凸起磁铁，请勿用错。

## 所需工具和材料

- H2.0 内六角螺丝刀
- H1.5 内六角螺丝刀

## 安全提示

> 在对激光切割机及其电子设备（包括工具头线缆）进行任何维护前，请先关闭设备电源并断开电源连接，以防屏幕误触或电路短路造成额外的设备损坏与安全隐患。维护或排查故障前，请确认相关部件已冷却。

## 移除 Y 轴光轴

### 步骤 1.移除冷却模组

参照[水箱更换指南](https://wiki.bambulab.com/zh/r1/maintenance/replace-water-tank)中的移除冷却模组步骤移除冷却模组（无需拆卸水箱）。

### 步骤 2.移除 Y 电机编码板

参照[Y 电机编码板更换指南](replace-y-axis-motor-encoder.md)移除 Y 电机编码板。

### 步骤 3.移除 Y 轴光轴

将X轴推到最后方，使用开箱时的固定件，锁定X轴。

![002.png](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-y-axis-linear-rod/zh/002.png)

使用 H2.0 内六角螺丝刀移除左右各两颗螺丝，取下两侧 Y 轴张紧器盖板。

![003.png](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-y-axis-linear-rod/zh/003.png)

使用 H2.0 内六角螺丝刀拧松三颗螺丝（无需拧下），释放张紧器。另一侧同样操作。

![004.png](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-y-axis-linear-rod/zh/004.png)

解锁张紧弹簧，同样方法释放另一侧弹簧。

![005.webp](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-y-axis-linear-rod/zh/005.webp)

拧松联轴器靠外的两颗螺丝，将光轴从联轴器内抽出。

|  |  |
| --- | --- |
| 006.png | 007.webp |

将 Y 皮带从同步轮上拨开，从侧面抽出光轴。同样方法拆除另一端。

|  |  |
| --- | --- |
| 008.webp | 009.png |

## 安装 Y 轴光轴

### 步骤 1.安装 Y 轴光轴

将 Y 轴电机两侧联轴器螺丝对准外侧，然后将两侧光轴插入联轴器。

> 注意:从设备正面看，左侧（靠近主控板侧）光轴末端有一个额外的凸起，请勿用错。

|  |  |
| --- | --- |
| 010.png | 011.webp |

将 Y 皮带重新套回光轴上的同步轮，检查两侧光轴法兰轴承是否正常卡在固定槽位中，没有到位的手动推动光轴，确保法兰轴承卡入到位。

|  |  |
| --- | --- |
| 012.webp | 013.webp |

轻微转动光轴，将X轴向后轻微拉紧后，使用 H2.0 内六角螺丝刀锁紧图示两颗螺丝。

![014.png](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-y-axis-linear-rod/zh/014.png)

检查安装后的 X 轴是否与后侧框架平行，如果 X 轴过于倾斜可能导致光路异常，损坏设备。

> 注意：如果发现 X 轴有明显倾斜请重新进行上一步中的：轻微转动光轴，将X轴向后轻微拉紧后，使用 H2.0 内六角螺丝刀锁紧图示两颗螺丝。确保锁入张紧器后X轴两侧都紧贴后侧框架。

![015.png](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/replace-y-axis-linear-rod/zh/015.png)

### 步骤 2.安装 Y 轴编码板

参照[Y 电机编码板更换指南](replace-y-axis-motor-encoder.md)装回 Y 电机编码板。

### 步骤 3.安装冷却模组

参照[水箱更换指南](https://wiki.bambulab.com/zh/r1/maintenance/replace-water-tank)装回冷却模组。

## 功能验证

更换完成后请参照[光路校准](../manual/laser-alignment-guide.md)教程，重新运行自动光路校准，如果光路校准正常完成，则上述安装正确。

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。
>
> 如果问题仍未解决，请提交 [服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5) 并附上您近期的设备日志，以及相关的照片或其他详细信息，我们的客户支持团队将随时为您答疑解惑并提供支持。
>
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
