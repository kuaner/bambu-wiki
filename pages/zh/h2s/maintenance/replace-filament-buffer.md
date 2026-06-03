---
path: zh/h2s/maintenance/replace-filament-buffer
title: "更换 H2S 缓冲器及连接线"
description: "本文介绍了如何更换 H2S 缓冲器及连接线"
tags: []
created: 2025-08-26T06:45:04.455Z
updated: 2025-10-13T01:38:09.049Z
source: https://wiki.bambulab.com/zh/h2s/maintenance/replace-filament-buffer
---

## 缓冲器

缓冲器安装在打印机上盖中，由一个滑块、一个弹簧和一个缓冲板组成。

缓冲器的备件包含以下：

1. 缓冲器 \* 1
2. BT3x8 螺丝 \* 4  
   ![dsc04123_compressed.jpg](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-filament-buffer/dsc04123_compressed.jpg)

## 何时更换

- AMS 工作不正常，经检查是缓冲器元器件出现明显损坏；
- 经过 Bambu Lab 技术支持的分析确认，需要更换缓冲器

## 所需的工具和材料

1. 新的缓冲器
2. H2.0 内六角扳手

**更换 H2D 缓冲器所涉及的螺丝规格及数量（建议妥善保管拆下的螺丝，避免丢失）：**

| **螺丝规格** | **螺丝图片** | **用途** | **位置示意图** |  | **螺丝数量** |
| --- | --- | --- | --- | --- | --- |
| BT3x8 |  | 用于固定缓冲器 |  |  | 4 |

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。
>
> 如果您对本指南有任何疑问，请点击此处联系在线技术支持 （服务时间 9:00-21:00），我们将及时回复并为您提供所需的帮助。

## 移除缓冲器

### 步骤 1：取下 AP 板盖

使用 H2.0 内六角扳手拧下 1 颗固定螺丝（BT2.6x8），然后从靠近前门的一侧取下 AP 板盖。

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-ap-board/image-6.png)

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-ap-board/image-5.png)

### 步骤 2：断开 6-pin 连接线

如果打印机连接了 AMS，需要从打印机背面断开 6-pin 连接线。

|  |  |
| --- | --- |
|  |  |

### 步骤 3：断开 PTFE 管

- 按下打印机背面的气动接头，将 PTFE 管和缓冲器断开连接。

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-filament-buffer/pixpin_2025-08-14_13-24-00.png)

- 将缓冲滑块推到最右侧，然后按住气动接头，依次将两根与工具头连接的 PTFE 管与缓冲器断开连接；

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-filament-buffer/pixpin_2025-08-14_12-31-29.png)

> 注意：如果是激光版打印机，还需断开气管。按压内置气泵的气动接头，即可抽出气管。  
> ![移除气管.png](https://wiki.bambulab.com/h2/maintenance/replace-filament-buffer/%E7%A7%BB%E9%99%A4%E6%B0%94%E7%AE%A1.png)

### 步骤 4：移除缓冲器螺丝

使用 H2.0 内六角扳手移除四颗缓冲器固定螺丝（BT3x8）。

> 当移除固定螺丝后，请用手拿住缓冲器，避免缓冲器掉下。

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-filament-buffer/dsc04104_compressed.jpg)

### 步骤 5：断开缓冲器线缆

用螺丝刀撬动线缆侧边；

![撬动连接线.png](https://wiki.bambulab.com/h2/maintenance/replace-filament-buffer/%E6%92%AC%E5%8A%A8%E8%BF%9E%E6%8E%A5%E7%BA%BF.png)

小心撬出接头，断开线缆。  
![彻底扣出.png](https://wiki.bambulab.com/h2/maintenance/replace-filament-buffer/%E5%BD%BB%E5%BA%95%E6%89%A3%E5%87%BA.png)

## 安装缓冲器

### 步骤 1：连接线缆

- 将缓冲器连接线重新与缓冲器连接；

![连接线缆-.jpg](https://wiki.bambulab.com/h2/maintenance/replace-filament-buffer/%E8%BF%9E%E6%8E%A5%E7%BA%BF%E7%BC%86-.jpg)

> **注意**：在这一步中可能会有磁铁丢失的情况，若您的磁铁和弹簧在安装过程中掉落请参考下图进行安装。  
> 请把下图三个被标红的螺丝用 H1.5 内六角扳手先拆除；并取下缓冲器。  
> ![连接线缆-螺丝1.jpg](https://wiki.bambulab.com/h2/maintenance/replace-filament-buffer/%E8%BF%9E%E6%8E%A5%E7%BA%BF%E7%BC%86-%E8%9E%BA%E4%B8%9D1.jpg)  
> 注意下图中标注的红色梯形磁铁的安装方向。另外建议可以用 H2.0 内六角扳手辅助安装，安装方式参考下图。  
> ![安装磁铁.jpg](https://wiki.bambulab.com/h2/maintenance/replace-filament-buffer/%E5%AE%89%E8%A3%85%E7%A3%81%E9%93%81.jpg)  
> 下图是正确安装后的示意图。  
> ![安装磁铁_正确实例.jpg](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-filament-buffer/d123.jpg)  
> 然后请重新把卸除的三颗螺丝重新安装上去。

- 如果是激光版本，还需连接气管；

![插入气管.png](https://wiki.bambulab.com/h2/maintenance/replace-filament-buffer/%E6%8F%92%E5%85%A5%E6%B0%94%E7%AE%A1.png)

- 将缓冲器装回原位。

![安装缓冲器.jpg](https://wiki.bambulab.com/h2/maintenance/replace-filament-buffer/%E5%AE%89%E8%A3%85%E7%BC%93%E5%86%B2%E5%99%A8.jpg)

### 步骤 2：固定缓冲器

使用 H2.0 内六角扳手拧紧背板的四颗固定螺丝（BT3×8）。

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-filament-buffer/dsc04104_compressed.jpg)

### 步骤 3：连接 PTFE 管

- 依次将两根与工具头连接的 PTFE 管与缓冲器重新连接；

![20250530-105238.jpg](https://wiki.bambulab.com/h2/maintenance/replace-filament-buffer/20250530-105238.jpg)

- 将打印机背面的 PTFE 管与缓冲器连接。

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-filament-buffer/pixpin_2025-08-14_13-24-00.png)

### 步骤 4：装回 AP 板盖

> 注意：安装 AP 板盖前，需检查线缆是否阻碍 PTFE 管路，避免影响后续 PTFE 管的安装。  
> ![20250408-115319.jpg](https://wiki.bambulab.com/h2/maintenance/replace-filament-buffer/20250408-115319.jpg)

先从靠近打印机背面的一侧扣回 AP 板盖，将箭头所示的两处均按压到位，右侧与缓冲器齐平，底部与护线盖齐平，然后使用 H2.0 内六角扳手拧紧一颗固定螺丝（BT2.6x8）。

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-ap-board/image-26.png)

![](https://wiki.bambulab.com/ams-2-pro/maintenance/replace-ap-board/image-25.png)

## 移除缓冲器连接线

### 步骤 1：移除 AP 板盖和护线盖

- 使用 H2.0 内六角扳手拧下 1 颗固定螺丝（BT2.6x8），然后从靠近前门的一侧取下 AP 板盖。

![](https://wiki.bambulab.com/h2/maintenance/replace-the-h2d-printer-cable-package/image-65.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-the-h2d-printer-cable-package/image-67.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-the-h2d-printer-cable-package/image-66.png)

- 护线盖由卡扣固定，您可以将护线盖向外拔出；此时可以断开缓冲器线缆。

![](https://wiki.bambulab.com/h2/maintenance/replace-the-h2d-printer-cable-package/image-68.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-the-h2d-printer-cable-package/20250326-204841.jpg)

### 步骤 2：移除背板

您可以参考这篇 Wiki 来移除 H2S 的背板：

[更换 H2S 背板](../../h2/maintenance/replace-rear-panel.md)

### 步骤 3：移除废料滑梯

使用 H2.0 内六角扳手移除 1 颗固定螺丝（BT3x8），然后向下拉动废料滑梯，直到可以看见废料滑梯的两个卡扣，然后向外取出废料滑梯。

> 废料滑梯除了通过顶部的螺丝固定外，底部也有两个卡扣扣在内衬上来进行固定。

![](https://wiki.bambulab.com/h2/maintenance/replace-the-h2d-printer-cable-package/image-64.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-the-h2d-printer-cable-package/image-63.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-the-h2d-printer-cable-package/image-62.png)

### 步骤 4：移除缓冲器连接线

先将缓冲器连接线与 MC 板断开连接，然后将缓冲器连接线与缓冲器断开连接，将连接先从左内衬中抽出。

![](https://wiki.bambulab.com/h2/maintenance/replace-the-h2d-printer-cable-package/20250324-102341-1.jpg)

## 安装缓冲器连接线

### 步骤 1：连接缓冲器连接线

- 将新的线缆接头插入缓冲器，沿此路径从内衬的走线孔中穿过。

![](https://wiki.bambulab.com/h2/maintenance/replace-the-h2d-printer-cable-package/20250326-204825.jpg)

![](https://wiki.bambulab.com/h2/maintenance/replace-the-h2d-printer-cable-package/20250326-204837.jpg)

- 然后将缓冲器连接线的另外一端与 MC 板连接。

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/replace-filament-buffer/dsc03861003.png)

### 步骤 2：安装废料滑梯

- 先将废料滑梯底部的两个卡扣对准内衬上的两个孔位；

![](https://wiki.bambulab.com/h2/maintenance/replace-the-h2d-printer-cable-package/image-84.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-the-h2d-printer-cable-package/image-82.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-the-h2d-printer-cable-package/image-80.png)

- 然后将废料滑梯往上扣，确保底部的卡扣扣入内衬中，用手托住废料滑梯的顶部，将废料滑梯的顶部的螺丝孔位对齐，最后使用 H2.0 内六角扳手拧紧一颗固定螺丝，并将黄绿和红白两根线缆扣在废料滑梯顶部的线扣后。

![](https://wiki.bambulab.com/h2/maintenance/replace-the-h2d-printer-cable-package/image-81.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-the-h2d-printer-cable-package/image-77.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-the-h2d-printer-cable-package/image-79.png)

注：在安装废料滑梯的时候，需要注意将废料滑梯的两侧扣在内衬的外侧，如果扣在内侧可能无法正常安装。

![](https://wiki.bambulab.com/h2/maintenance/replace-the-h2d-printer-cable-package/image-73.png)

### 步骤 3：安装 AP 板盖和护线盖

- 将护线盖扣入打印机中；

![](https://wiki.bambulab.com/h2/maintenance/replace-the-h2d-printer-cable-package/image-78.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-the-h2d-printer-cable-package/image-75.png)

- 先从靠近打印机背面的一侧扣回 AP 板盖，将箭头所示的两处均按压到位，右侧与缓冲器齐平，底部与护线盖齐平，然后使用 H 2.0 内六角扳手拧紧一颗固定螺丝（BT2.6x8）。

![](https://wiki.bambulab.com/h2/maintenance/replace-the-h2d-printer-cable-package/image-76.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-the-h2d-printer-cable-package/image-74.png)

### 步骤 4：安装背板

您可以参考[更换 H2S 背板](../../h2/maintenance/replace-rear-panel.md)来安装打印机背板。

## 如何验证完成/成功

打开打印机电源，使用 AMS 发起一次打印，检查是否可以正常打印。如果可以正常打印，则更换成功。

否则，请检查缓冲器的连接线与 PTFE 管是否连接正确，然后重试。

如果问题仍然存在，请联系 Bambu Lab 技术支持寻求进一步帮助。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 为了确保您安全有效地进行操作，如果对指南中的任何步骤有疑虑或问题，请在开始操作前联系我们的客户服务团队，我们随时乐意为您解答疑问并提供支持。  
> [点击此处联系在线技术支持 （服务时间 9:00-21:00）](https://support.bambulab.cn/cn/im)
