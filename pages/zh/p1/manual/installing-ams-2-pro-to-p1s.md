---
path: zh/p1/manual/installing-ams-2-pro-to-p1s
title: "连接 AMS 2 Pro 到 P1S"
description: "学习如何连接 AMS 2 Pro 到 P1S"
tags: ["ams 2 pro", "p1s"]
created: 2025-08-26T08:30:38.272Z
updated: 2025-12-24T12:18:39.725Z
source: https://wiki.bambulab.com/zh/p1/manual/installing-ams-2-pro-to-p1s
---

本 Wiki 提供了将 AMS 2 Pro 连接到 P1S 3D 打印机的分步指南，从而实现多材料打印与耗材干燥功能。

## 所需准备

#### 方案一：您已经拥有一台 P1S，并单独购买了 AMS 2 Pro

如果您是分别购买 P1S 和 AMS 2 Pro，则需要准备以下额外配件来完成 AMS 2 Pro 的安装：

- 1 个耗材缓冲器
- 1 条 4-pin 总线线缆
- 1 个 AMS 2 Pro 电源适配器 (电源)
- 3 个气动接头
- 3 根 PTFE 料管

> 📌*将一台 AMS 2 Pro 连接到 P1 或 X1 系列打印机时，需要耗材缓冲器（H2D 系列除外）；若将多台 AMS 2 Pro 连接到同一台打印机，则需要 AMS 集线器。*

#### 方案二：您购买的是P1S AMS 2 Pro Combo

如果您购买的是 P1S AMS 2 Pro Combo，那么其中已经包含 P1S 打印机、AMS 2 Pro 组件、以及上述所有配件。不同之处在于 Combo 配备的是 AMS 集线器，而非耗材缓冲器。

## 连接 AMS 2 Pro 到 P1S

### 步骤 1: 更新固件

在连接 AMS 2 Pro 之前，请先将固件更新至最新版本，以避免初始化问题。详细操作请参考 [P1S 固件升级指南](firmware-upgrading.md)。

### 步骤 2: AMS 2 Pro 开箱

拆除 AMS 2 Pro 的所有包装材料，并确认所附配件齐全。您可以查阅 [AMS 2 Pro 开箱指南](../../ams-2-pro/manual/unboxing-and-setup.md)，了解具体的开箱步骤。

> *📌按照该指南逐步操作，操作完“检查干燥剂”这一步骤即可。*

将 AMS 2 Pro 放置在 P1S 顶部，以实现最佳空间利用率。

![](https://wiki.bambulab.com/p1/manual/installing-ams-2-pro-to-p1s/p1s_with_ams_2_pro_on_top3.jpg)

### 步骤 3: 连接料管

AMS 2 Pro 背面可能已经预装了一根 PTFE 料管；如果没有，则在其背面装上随机附带的 500mm PTFE 料管。

持续推送该料管，直至无法再送入或轻易拉出。然后，将其另一端插入耗材缓冲器的左侧接口。

|  |  |
| --- | --- |

接下来，将 370mm PTFE 料管一端插入耗材缓冲器的右侧接口，另一端插入气动接头的黑色部分。

|  |  |
| --- | --- |

请注意检查弹簧状态，弹簧不应被卡住或压缩，而应能在耗材缓冲器内自由移动。您可以轻轻拉动料管，以确认料管是否正确插入。在拉动料管时，内部的弹簧会随之伸缩。  
![testing-movement-of-the-tube.gif](https://wiki.bambulab.com/x1/manual/x1c-with-ams-2-pro/testing-movement-of-the-tube.gif)

### 步骤 4: 安装耗材缓冲器

在 P1S 打印机背面找到与耗材缓冲器形状相匹配的凹槽。将缓冲器放置到位，确保卡扣插入底部的孔中，如下图所示。(下图是以 X1 机型为示例，但安装方法完全一样）  
![inserting-the-filament-buffer-to-the-slot.png](https://wiki.bambulab.com/x1/manual/x1c-with-ams-2-pro/inserting-the-filament-buffer-to-the-slot.png)  
![mounting-filament-buffer.gif](https://wiki.bambulab.com/x1/manual/x1c-with-ams-2-pro/mounting-filament-buffer.gif)

使用 H2.0 内六角扳手，用 2 颗 M3 × 21.5 螺丝，将缓冲器固定到打印机上。

![securing_the_screws.png](https://wiki.bambulab.com/x1/manual/x1c-with-ams-2-pro/securing_the_screws.png)

接下来，将气动接头的另一端连接到位于 P1S 背面右上方的黑色管子上，该管子连接挤出机。

![ptfe_coupler_connector.png](https://wiki.bambulab.com/x1/manual/x1c-with-ams-2-pro/ptfe_coupler_connector.png)

完整的连接效果如下图所示。

![ams_2与p1s连接效果图.png](https://wiki.bambulab.com/ams-2-pro/manual/ams_2%E4%B8%8Ep1s%E8%BF%9E%E6%8E%A5%E6%95%88%E6%9E%9C%E5%9B%BE.png)

请确保 PTFE 料管经由料盘支架下方连接到气动接头上，而不是从上方绕过。

> *📌 如果需要连接多台 AMS，请将耗材缓冲器替换为 AMS 集线器，这样可以最多连接四台 AMS。具体操作请参考 [AMS 集线器连接指南](../../x1/manual/Connect-AMS-Hub-and-multi-AMS.md)。*

### 步骤 5: 连接总线线缆

将 4-pin 总线电缆的 L 型端插入打印机背面的 4-pin 接口。请注意插入方向，包括底部的锁扣位置。

|  |  |
| --- | --- |

接着，将电缆的另一端连接到耗材缓冲器底部的接口。同样需要注意锁扣朝向打印机一侧。

![connecting-end-of-cable-to-filament-buffer.png](https://wiki.bambulab.com/x1/manual/x1c-with-ams-2-pro/connecting-end-of-cable-to-filament-buffer.png)

然后，将 6-pin 总线电缆的一端插入 AMS 2 Pro 背面的任意一个接口，另一端插入耗材缓冲器左侧接口（或者 AMS 集线器底部接口）。

![connecting-6-pin-cable.png](https://wiki.bambulab.com/x1/manual/x1c-with-ams-2-pro/connecting-6-pin-cable.png)

### 步骤 6: 为 AMS 2 Pro 供电 (烘干功能)

如果您打算使用烘干功能，请将电源适配器先插入 AMS 2 Pro 背面，然后再将其接入电源插座。

![inserting-power-cable.png](https://wiki.bambulab.com/x1/manual/x1c-with-ams-2-pro/inserting-power-cable.png)

> *📌 每台用于烘干的 AMS 2 Pro 都需要单独配备一个电源适配器。如果您使用多台 AMS 2 Pro，请确保每一台都有相应的电源适配器。*

### 步骤 7: 启动打印机并检查 AMS 2 Pro

启动 P1S，并确认 AMS 2 Pro 已正确连接。在 P1S 的主界面右上角，应显示 AMS 图标。

![](https://wiki.bambulab.com/p1/manual/installing-ams-2-pro-to-p1s/p1s_screen_with_ams_symbol2.jpg)

如果未显示 AMS 图标，请检查所有电缆连接，确保 4-pin 和 6-pin 电缆都已插入到位。

![](https://wiki.bambulab.com/p1/manual/installing-ams-2-pro-to-p1s/p1s_screen_without_ams_symbol2.jpg)

### 步骤 8: 插入并装载耗材

打开 AMS 2 Pro 的顶盖即可看到料槽，将料盘放入槽内，持续插入耗材，直到 AMS 2 Pro 自动检测到耗材并开始拉入。

|  |  |
| --- | --- |

对于拓竹官方耗材，RFID 线圈会自动识别耗材的类型和颜色。对于第三方耗材，则需要在 Bambu Studio 中手动设置耗材类型和颜色。

> *⚠️注意：请勿在打印过程中修改耗材信息。*

## 使用 AMS 2 Pro 进行多色打印或耗材干燥

连接完成后，您就可以开始使用 AMS 2 Pro 进行多色 3D 打印或烘干耗材。您可以查阅[多色打印指南](../../software/bambu-studio/multi-color-printing.md)，了解如何通过 AMS 2 Pro 实现多色打印。如果需要使用 AMS 2 Pro 的烘干功能，请参考[此页面](../../ams-2-pro/ams-2-pro-for-drying-in-x1-p1-series.md)的操作说明。

## 故障排查

- **一台 AMS 2 Pro 未被识别**：如果 AMS 2 Pro 完全无法被识别，请检查所有电缆是否已牢固插好。详细步骤可参考拓竹官方 AMS 故障排查指南，或提交技术支持工单获取帮助。
- **多台 AMS 2 Pro 未被识别**：如果多台 AMS 2 Pro 未被检测到，请确认您使用的是 AMS 集线器，而不是耗材缓冲器。
- **AMS 2 Pro 功能异常**：如果 AMS 2 Pro 无法正常工作，尤其是无法使用烘干功能，请确保 P1S 固件已更新至最新版本，同时确认您使用的是拓竹电源适配器。
- **电缆走线错误**：请避免将电缆绕过尖锐转角或靠近打印机的运动部件。过度拉扯或反复弯折可能导致线缆内部断裂，从而引发 AMS 2 Pro 故障。
- **AMS 2 Pro 无法烘干**：在 P1S 上使用烘干功能时，AMS 2 Pro必须连接电源适配器。

## 结束语

> 我们希望这份指南为您提供了有效的信息，并真实地帮助了您。
>
> 如果您对本文中描述的过程有任何疑虑或疑问，您可以[点击这里提交服务工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)。我们随时准备为您提供帮助并回答您的任何问题。
