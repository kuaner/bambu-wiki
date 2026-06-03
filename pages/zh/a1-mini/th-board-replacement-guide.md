---
path: zh/a1-mini/th-board-replacement-guide
title: "A1 mini 挤出主板更换指南"
description: "本指南演示了如何更换A1 mini上的挤出主板（TH板）。"
tags: []
created: 2024-02-28T06:58:02.483Z
updated: 2026-02-11T08:50:06.499Z
source: https://wiki.bambulab.com/zh/a1-mini/th-board-replacement-guide
---

在本指南中，我们将演示更换A1 mini 挤出主板（TH板）的步骤。

![](https://wiki.bambulab.com/a1m/replace-th-board/a1_mini_th_board.jpg)

## 何时更换

A1 mini 挤出主板需要更换的常见情况有：

- 热床调平出现问题，喷嘴不能准确地执行回零程序
- 步进电机出现故障，挤出机电机没有转动
- USB-C 接口损坏
- 耗材传感器排线接口损坏
- 热端加热组件损坏
- 无法检测工具头，并在打印机屏幕上显示错误信息
- Bambu Lab的技术支持人员建议您更换挤出主板

## 工具和材料

[Bambu Lab A1 mini 挤出主板](https://item.jd.com/10086621148773.html)

- H2.0 六角扳手
- H1.5 六角扳手

# 安全警告

> ***重要提醒！***
>
> *在进行打印机和其电子设备的任何维护工作之前，请关闭打印机的电源，包括工具头的电缆。这是因为在更换零部件时让打印机保持开启状态可能会导致电路短路，从而引起额外的电子设备损坏和安全隐患。*
>
> *当您对打印机进行维护或故障排查时，可能需要拆卸一些部件，包括热端。这个过程可能会使电线或电子元件暴露，如果它们在打印机通电状态下相互接触或与其他金属、电子元件接触，可能会发生短路。这将损坏打印机的电子元件，并且可能造成进一步的损坏。*
>
> *因此，在进行任何维护工作之前，请将打印机断电。以防止任何线路短路或打印机电子元件损坏。断开电源再进行维护工作，可以避免对打印机的电子元件造成潜在伤害，并确保维护工作安全有效地进行。*
>
> *如果您对本指南有任何疑问或建议，请*[*点击这里提交工单*](https://bambulab.com/zh/my/support/tickets?from=5)*，我们将及时回复并提供您所需的帮助。*

## 拆除旧挤出主板

### 1. 拆除工具头后盖板

首先将工具头后部的盖板取下，  
如下图所示，请小心地用手拉开后部盖板的底部。

![](https://wiki.bambulab.com/a1m/replace-th-board/remove_back_cover.jpeg)

### 2.  从工具头上取下 USB-C 数据线

接下来，拆下固定在A1 mini工具头上的 USB-C 数据线的四颗螺钉。  
拧下螺钉后，可以向上拉动 USB-C 数据线将其拆卸。

![](https://wiki.bambulab.com/a1m/replace-usb-c-cable/remove_usb_c_cable_from_a1_print_head.jpeg)

### 3. 拆下挤出主板的螺钉

取下固定挤出主板的三颗黑色螺钉。

![](https://wiki.bambulab.com/a1m/replace-th-board/remove_the_th_board_screws.jpeg)

### 4. 断开连接的线缆

拆下连接到挤出主板上的四根电缆。  
小心地捏住接头将它们拉出来，请避免直接拉动线缆。  
我们建议使用扁平工具（例如平头螺丝刀、镊子尾端）轻轻地撬开线缆接头与接口，以避免造成任何线缆损坏。

![](https://wiki.bambulab.com/a1m/replace-th-board/disconnect_the_th_board_cables.jpeg)

请不要忘记拆下由两颗螺钉固定的涡流传感器线缆。

![](https://wiki.bambulab.com/a1m/replace-th-board/remove_the_eddy_sensor_screws.jpeg)

### 5. 取下挤出主板

您现在可以将挤出主板从工具头上取下。

**在拆下时需要小心，请仔细断开耗材传感器的 FPC 柔性排线。**

缓慢拨开黑色的夹子。避免晃动 FPC 排线，否则可能会导致损坏。如果该排线已经损坏，您可以[提交工单](https://bambulab.com/zh/my/support/tickets?from=5)，向我们的技术人员购买一个替换品。

![](https://wiki.bambulab.com/a1m/replace-th-board/remove_the_filament_sensor_ribbon_cable.jpeg)

## 安装新挤出主板

### 1. 将挤出主板安装到工具头上

将挤出主板安装回打印头外壳中。首先，将耗材传感器的 FPC 排线重新安装到板子的顶部。轻轻地将 FPC 排线插入接口中，拨下黑色夹子，请确保排线安装到位。

![](https://wiki.bambulab.com/a1m/replace-th-board/install_the_filament_sensor_ribbon_cable.jpeg)

请小心地将挤出机电机电缆按照下图所示的方式放置在FPC柔性排线旁边。  
完成这一步后，您可以轻轻地将挤出主板推回至原来的位置。

![](https://wiki.bambulab.com/a1m/replace-th-board/extruder_motor_wiring_on_th_board.jpeg)

### 2. 安装挤出主板螺丝

使用三颗黑色螺钉将挤出主板重新固定到工具头上。

![](https://wiki.bambulab.com/a1m/replace-th-board/install_the_th_board_screws.jpeg)

> ***重要提示！***  
> *请勿过度拧紧螺钉，以避免螺纹滑丝。*

### 3. 重新接线

将新的挤出主板放回原位后，您可以按照下图所示重新连接所有线缆。

1. [热端加热组件](https://item.jd.com/10086621431814.html)
2. 挤出电机
3. [热端散热风扇](https://item.jd.com/10085237113101.html)
4. [部件冷却风扇](https://item.jd.com/10085237672213.html)
5. 热端传感器

![](https://wiki.bambulab.com/a1m/replace-th-board/th_board_cables_on_a1.jpeg)

### 4. 重新连接 USB-C 数据线

将 USB- C 以正确的方向插入接口后，使用我们在第一步中拆下的四颗螺钉重新安装 USB-C 数据线。

![](https://wiki.bambulab.com/a1m/replace-th-board/install_the_usb_cable_and_4_screws.jpeg)

> ***注意！***
>
> ***请不要过度拧紧螺丝，可能会导致螺纹损坏**。请注意* *USB-C 数据线的方向和背面的小凹槽对齐。* *USB-C 数据线只能用一种方式安装，正确的方向是数据线接头的凸起对准后方的凹槽。*
>
> ![](https://wiki.bambulab.com/a1m/replace-usb-c-cable/usb_cable_orientation.jpeg)

### 5. 安装工具头后盖板

最后，安装A1 mini 工具头的后盖板。  
后盖板使用卡扣固定。只需将后盖板上的两个卡扣对准，然后推入盖板，直到听到几声“咔嗒”声。

### 6. 校验是否安装成功

#### 根据电路板灯语判断

**正常状态：TH板指示灯常亮绿灯**

在拧回所有螺丝前，可先预装或不装盖子（小心用电安全，断电操作），再通电检查该电路板灯语是否正常，灯语正常，再拧回螺丝，这样可以避免返工。

<https://public-cdn.bblmw.com/wiki/video/A1M-TH.mp4>

#### 连接电源线并打开电源，发起打印，检查是否有报错。

如有报错，请检查工具头板上所有电缆是否连接正确，然后重试。如果问题仍然存在，请联系 Bambu Lab 技术支持寻求进一步帮助。

## 更换完毕后的校准工作

建议您在更换完挤出主板后进行一次全面校准，以确保打印机顺畅运行。

此外，强烈建议在进行打印之前[清洗PEI构建板](../general/textured-PEI-plate-not-working-as-expected.md)，因为在更换挤出主板的过程中，构建板可能会受到污染。

## **结束语**

> *希望这篇指南能对您有所帮助。*
>
> *我们希望确保您能够安全有效地进行操作。如果您对本文描述的过程有任何疑问，我们建议您在开始操作前联系我们的技术支持团队。我们的团队会随时帮助您，并解答您可能会遇到的问题。*
>
> *您可以*[*点击此处开启新的工单*](https://bambulab.com/zh/my/support/tickets?from=5)*。*
>
> *我们将尽力及时回复并为您提供您所需的帮助。*
