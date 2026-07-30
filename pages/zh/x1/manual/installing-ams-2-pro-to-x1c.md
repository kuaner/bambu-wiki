---
path: zh/x1/manual/installing-ams-2-pro-to-x1c
title: "如何在X1C上安装AMS 2 Pro"
description: ""
tags: []
created: 2025-07-18T01:44:06.572Z
updated: 2026-07-09T10:01:02.217Z
source: https://wiki.bambulab.com/zh/x1/manual/installing-ams-2-pro-to-x1c
---

## 如何在 X1C 上安装AMS 2 Pro

本Wiki提供了将 AMS 2 Pro 安装到 X1C 的详细步骤，以帮助实现多材料打印和耗材干燥功能。

### 所需准备

#### 情况1：仅拥有 X1C

由于 X1C 的配件只包含 H2.0 内六角扳手，其余配件需要您另行购买，包括：

- AMS 2 Pro 组件：可在[淘宝](https://detail.tmall.com/item.htm?abbucket=2&fpChannel=101&fpChannelSig=f97522187d98673564d7c1a2d76c5b891e0f0b5c&id=901351999976&ltk2=1752825194169pc6ymmn89fh7ecqkksayj&ns=1&priceTId=undefined&skuId=5926264634739&spm=a21n57.1.hoverItem.1&u_channel=bybtqdyh&umpChannel=bybtqdyh&utparam=%7B%22aplus_abtest%22%3A%22a6d366fec2b5bb1b017ec3d81ab3a6f3%22%7D&xxc=taobaoSearch)购买。
- 供料缓冲器（或适用于多机型的AMS Hub 集线器）：[淘宝](https://detail.tmall.com/item.htm?id=693987695729&pisk=g_tZYo2WtcnN9T5OSHs4ac8kghIOVilWSn1fnKvcC1fikVKVuLOnBxpcGnS29BbDfG96TsAWgtt6cK2VnBsGkF1f1sS2HQkIN0iWBdIAxbGSV7iBS1IRISj0G6VhHiWgWAv5qdIAmjyQm4iyBCpwJn4Gn9DFhtNGIIbctJfd3sqDi1b3ttBAmiAciMfhEtqgm1qcxvWPQl2gml4nxT6RnRAcmv7h9tjcIIjmir1cNkWPSvAx2kqqks7NZdfU4pKFI2fr26qmGHXwL_pGkoqDYO7wxiufet_6oLQJfLm4vG9y-MX2DY4Vga8DfMxit0bdoHAhKCMbk982n3IO4-mMLG5NrO7s0ARkLKY58HMo2GSGsEs9h8l6LhR6BHJbnyjNfe7ybgm8ssTBUnW2DjneaKvJow-4_gWTM9bMNnLair7Gp95SLv7qtLalcuwzLrUAWeBFNAHTkrQG395SLXUYkNgNL_MN5&rn=5a93f711843ef4aa3be390a6e81be5a9&spm=a1z10.3-b-s.w4011-25177047232.13.1c983c0e8xjKry&skuId=4927627985197) ,供料缓冲器自带 2 个 M3 × 21.5 螺丝用于固定。
- 4-pin 和 6-pin 数据线（供料缓冲器接AMS）：[淘宝](https://detail.tmall.com/item.htm?abbucket=11&id=694052067560&pisk=gIzoRdxPtuoWM26xDrg5V0OGEjjYw4gI9JLKp2HF0xkfO_NRAe53pJneJ7I5t6D0dYn-zTgnTReseXK8aq-qwXpraUoe0Ek0Uen8-WTnTWyCNvC5D7NSR2WOBJbTN7iDQ5carvuq0SGp8QSx4ziFhSBOBNQh4IuhEOep2O5cufcZ8boe8q5m6blE8DlzgscE9LkEUJ5ciXhKLU8EYSPqOb0eY3kUgElnTHJraXPViXMqL2uULq5mOj8c4YaUurWnJse1axA_ibmoQ7kzw7U2W0K7MxbRzrq0VAktne8UobV3mFtJSMHafYntK-7vr2Vqt-mTqOYuKWP_Ym4HU_ea3k2EGo6HxAqUwlZEm_7zi4DuIrw2aH0uY8anVuAC1SuzhlMs4i6jizUtxAiD3TPYiYogx8BX8YEgg-mTkKLt7lw0-cuN44t2bjVXRj5LuHtI4jGmB2az-Ek6c5DAisxNO0ljNACciH9n4jGm_sfDj4mrGbbG.&rn=99ea745c0c8863c4cf135fd608380e77&spm=a1z10.3-b-s.w4011-25177047232.56.210b3c0e027BvB), 6-pin 线可选择 510 mm 或 1.5 m 长度。
- 2根 PTFE 料管：550 mm（用于 AMS 2 Pro 到耗材缓冲器）；370 mm（用于耗材缓冲器到打印机）。
- 电源适配器： [淘宝](https://detail.tmall.com/item.htm?abbucket=11&id=901639674058&pisk=gNomxrb2IqzbyVd8y0ZXlrGEtI8RcoZ_tfIT6lFwz7PWCKMv5GJi6fUNXxLXIdVo1SUY0SIgjAcs6PoT6cXjqXjODITjQGqTbBdpvHHXhlZw9WJh2vfbB-72X5SaUowt-qaLzHHjh56c_p3yvOxNAG1N75la4zybQlya_5Ju4Rw3bizN0YPzN7ra3-rNaTy_31PZ_Zkz4J213NS4_YSzh7Pab5lZUL2Ta5l4jEPjb0oyslKPQbF8v020oWkkRGSMz-5Ltx8GjGoorzPEv7jNb02mI4jCkMYTT2NYJ5cy2iqiURcuJqAhmfDZdVzojsJxTbui_8gWsNVn7x3I7zv20Yq0iXmSat7gmVljjrgcCpMz0bgQOr8WN8mxvPVQr_RqeYV4-VcvNGPx-YluJ0CRvkuIZc4UYgS5zwyoFGwyB0715ry7EWEs0cjzOaM3wLvl8da4F-NpELb1sry7EJJkEwq0u8wDx&rn=d911f63154147b16a193b8c98874a56d&skuId=5927195091249&spm=a1z10.3-b-s.w4011-25177047232.13.12b33c0e6Hrj9f)（X1C 实现干燥功能所必需）。
- PTFE 接头

#### 情况2：拥有 X1C combo 版

X1C AMS 2 Pro combo已包含 X1C 打印机、AMS 2 Pro，以及上述所需的全部配件（除了 6-pin 数据线——因为电源适配器已具备同样的功能，所以未包含 6-pin 线）。因此您无需另行购买其他配件。

> 注意：如果您只需要对耗材进行干燥，则只需准备 AMS 2 Pro 和电源适配器即可。

#### 情况3：分开购买 X1C 和 AMS 2 Pro

如果您是分开购买的 X1C 和 AMS 2 Pro，那么可用配件仅包含 6-pin 数据线，因此还需要额外购买以下配件：

- 4-pin 数据线
- 两根 PTFE 料管：550 mm（用于 AMS 2 Pro 到耗材缓冲器）；370 mm（用于耗材缓冲器到打印机）
- 电源适配器
- 供料缓冲器
- PTFE 接头

> **注意**：AMS 2 Pro 官方电源适配器规格为 24V 4A。为确保设备安全与正常使用，**请务必使用官方配件。使用第三方适配器可能会导致设备损坏，并影响保修权益**。

## 如何连接 AMS 2 Pro 与 X1C

### 第一步：更新固件

在连接 AMS 2 Pro 之前，请先将固件更新到最新版本，以避免初始化故障。

### 第二步：开箱 AMS 2 Pro

去除 AMS 2 Pro 的所有包装材料，并检查所有附件是否齐全。您可以参考[AMS 2 Pro 开箱与安装](../../ams-2-pro/manual/unboxing-and-setup.md) Wiki 了解详细的开箱步骤，并按照指南进行，直到**检查主动支撑轴**的部分为止。

为了节省空间，建议将 AMS 2 Pro 放置在 X1C 顶部。

### 第三步：连接料管

从 AMS 后方插入 PTFE 料管（500 mm），安装后轻轻拉动料管，确认已固定，然后将另一端插入供料缓冲器左侧的接口。

|  |  |
| --- | --- |
|  |  |

接着，将 370 mm PTFE 料管的一端插入供料缓冲器右侧接口，另一端插入 PTFE 接头的黑色部分。

|  |  |
| --- | --- |
|  |  |

注意弹簧不要被卡住或被压缩，您可以尝试轻轻拉动弹簧，检查是否正确安装。

![testing-movement-of-the-tube.gif](https://wiki.bambulab.com/ams-2-pro/testing-movement-of-the-tube.gif)

### 第四步：安装供料缓冲器

在 X1C 背面，找到与供料缓冲器形状对应的凹槽。请正确放置供料缓冲器，确保底部的卡扣对准下方的孔并插入，如下图所示。

![inserting-the-filament-buffer-to-the-slot.png](https://wiki.bambulab.com/x1/manual/x1c-with-ams-2-pro/inserting-the-filament-buffer-to-the-slot.png)

下方的动图也演示了整个操作过程。

![mounting-filament-buffer.gif](https://wiki.bambulab.com/x1/manual/x1c-with-ams-2-pro/mounting-filament-buffer.gif)

使用 H2.0 内六角扳手，用两颗 M3 × 21.5 螺丝将供料缓冲器固定在打印机上。

![securing_the_screws.png](https://wiki.bambulab.com/x1/manual/x1c-with-ams-2-pro/securing_the_screws.png)

接着，将 PTFE 接头连接到 X1C，将耗材导向挤出机。

![ptfe_coupler_connector.png](https://wiki.bambulab.com/x1/manual/x1c-with-ams-2-pro/ptfe_coupler_connector.png)

机器的部件位置如下图所示。

![connection.png](https://wiki.bambulab.com/ams-2-pro/connection.png)

> 注意：如果需要连接多台 AMS 2 Pro，请将耗材缓冲器替换为 AMS Hub，即可最多连接四台 AMS 单元。请参考[连接AMS Hub和多台AMS](Connect-AMS-Hub-and-multi-AMS.md)，了解详细连接方式。

### 第五步：连接数据线

取出 L 形的 4-pin 数据线，将其连接到打印机背面的 4-pin 接口，确保方向正确。

|  |  |
| --- | --- |
|  |  |

接着，将另一端连接到供料缓冲器底部的接口。

![connecting-end-of-cable-to-filament-buffer.png](https://wiki.bambulab.com/x1/manual/x1c-with-ams-2-pro/connecting-end-of-cable-to-filament-buffer.png)

取出 6-pin 数据线，将一端连接到 AMS 2 Pro 上任意一个 6-pin 接口（两个接口功能相同）。另一端连接到供料缓冲器左侧的接口（数据线两端均相同）。

![connecting-6-pin-cable1.png](https://wiki.bambulab.com/ams-2-pro/connecting-6-pin-cable1.png)

### 第六步：给 AMS 2 Pro 接电（用于干燥功能）

如果您计划使用干燥功能，必须将电源适配器插入 AMS 2 Pro 的电源接口，然后再将适配器插入电源插座。

![inserting-power-cable.png](https://wiki.bambulab.com/x1/manual/x1c-with-ams-2-pro/inserting-power-cable.png)

> 注意：每台带干燥功能的 AMS 2 Pro 都需要单独的电源适配器。如果您使用多台 AMS 2 Pro，请确保为每台准备对应的电源适配器。

### 第七步：启动打印机并检查 AMS 2 Pro

打开 X1C，确保 AMS 2 Pro 已连接。在 X1C 触摸屏上进入耗材页面，如果 AMS 2 Pro 连接正常，您将在该页面看到相关信息。

![ams-2-pro-connected-to-x1c_2.jpg](https://wiki.bambulab.com/ams-2-pro/ams-2-pro-connected-to-x1c_2.jpg)

如果未检测到 AMS，请检查所有线缆连接，确保 4-pin 和 6-pin 线插好。

### 第八步：插入并进料

打开 AMS 2 Pro 顶盖，露出耗材槽，然后将料盘放入对应槽位。按下屏幕进料按钮，插入约 2 厘米的耗材线。AMS 2 Pro 会自动检测耗材并开始拉入。

![](https://wiki.bambulab.com/x1/manual/x1c-with-ams-2-pro/filament-spools-in-ams.png)

加载耗材时，点击每个耗材选项，然后选择“进料”。

![loading-filament-.jpg](https://wiki.bambulab.com/ams-2-pro/loading-filament-.jpg)

Bambu Lab 耗材会通过 RFID 读卡器自动识别耗材类型和颜色。第三方耗材则需要在 Bambu Studio 软件或 X1C 触摸屏上手动设置耗材类型和颜色。

> 注意：打印过程中请勿修改耗材信息。

## 使用 AMS 2 Pro 进行多色 3D 打印或耗材干燥

连接完成后，您即可开始使用 AMS 2 Pro 进行多色 3D 打印或耗材干燥。

想了解如何使用 AMS 2 Pro 实现多色打印，请参阅[多色打印指南](../../software/bambu-studio/multi-color-printing.md)。

如果您想用它进行耗材干燥，请参考 X1C Wiki 中关于[使用 X1/P1S 打印机连接 AMS 2 PRO 进行烘干](../../ams-2-pro/ams-2-pro-for-drying-in-x1-p1-series.md)。

## 故障排除

- AMS 2 Pro 无法识别：如果 AMS 2 Pro 完全无法识别，请检查所有线缆是否已经插好。您可参考 Bambu Lab 官方 AMS 故障排查指南，或提交技术支持工单获取帮助。
- 多台 AMS 无法识别：如果多台 AMS 2 Pro 无法被检测到，请确认已使用 AMS Hub 而非供料缓冲器进行连接。
- AMS 2 Pro 工作异常：若 AMS 2 Pro 出现功能异常，尤其是干燥功能，请确认 X1C 固件已更新至最新版本，并确保使用了 Bambu Lab 电源适配器。
- 线缆布线错误：请避免将线缆绕过尖锐转角或靠近打印机活动部件。线缆受拉或反复弯折可能导致内部导线损坏，从而引发 AMS 故障。
- AMS 2 Pro 无法干燥：若 AMS 在 X1C 上无法启用干燥功能，请确认已连接电源适配器。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)，点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
