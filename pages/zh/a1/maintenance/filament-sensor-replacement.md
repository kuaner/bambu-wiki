---
path: zh/a1/maintenance/filament-sensor-replacement
title: "A1 系列进料霍尔板更换指南"
description: "本指南演示如何更换 A1 系列进料霍尔板。"
tags: []
created: 2024-05-11T02:13:59.044Z
updated: 2026-01-20T09:10:09.019Z
source: https://wiki.bambulab.com/zh/a1/maintenance/filament-sensor-replacement
---

![](https://wiki.bambulab.com/a1m/replace-filament-sensor/a1_filament_sensor.jpg)

## **何时使用本指南？**

本指南用于解决进料霍尔板出现的问题。

需要更换进料霍尔板的常见情况包括：

- 上料、下料和打印时，打印机未检测到耗材
- 打印频繁中止，报告耗材出现问题
- 拓竹技术支持建议更换

## **工具和材料**

A1 进料霍尔板（购买链接：[京东](https://item.jd.com/10086620804757.html) [天猫](https://detail.tmall.com/item.htm?abbucket=19&id=742413890652&rn=a2c4a71cc1ebc454113082a1179bbdfd&spm=a1z10.3-b-s.w4011-25177047232.13.59d31c79bCV2UL&skuId=5118758836326)）

- H2.0 六角扳手
- H1.5 六角扳手
- 15 分钟

### **安全警告**

> **重要提醒！**
>
> **在进行任何维护工作之前，务必关闭打印机的电源**，包括对打印机的电子元件和工具头电线进行维护。在打印机通电时进行此类操作可能会导致短路，从而损坏电子设备和造成安全隐患。
>
> 在维护或故障排除过程中，您可能需要拆卸热端等部件，从而暴露电线和电子元件。如果它们在打印机仍处于通电状态时相互接触或与其他金属、电子元件接触，就可能发生短路。**这将损坏打印机的电子元件和造成其他问题。**
>
> 因此，**在进行任何维护前，务必关闭打印机并断开电源**，以防止短路或损坏打印机的电子原件，从而确保维护工作安全有效地进行。如果您对本指南有任何疑问，请[点击这里提交工单](https://bambulab.com/zh/my/support/tickets?from=5)，我们将及时回复并提供帮助。

## **拆除旧进料霍尔板**

### 1. **拆除工具头的后盖**

如下图所示，拉住后盖底部，小心撬开后盖。

![](https://wiki.bambulab.com/a1m/replace-th-board/remove_back_cover.jpeg)

### 2.  **移除 USB-C 数据线**

然后，移除4颗螺丝。这些螺丝用于将 USB-C 数据线固定在 A1 的工具头上。

卸下螺丝后，向上拉动 USB-C 数据线即可将其取下。

![](https://wiki.bambulab.com/a1m/replace-usb-c-cable/remove_usb_c_cable_from_a1_print_head.jpeg)

### 3. **拆除挤出主板的螺丝**

拆除固定挤出主板的3颗黑色螺丝。

![](https://wiki.bambulab.com/a1m/replace-th-board/remove_the_th_board_screws.jpeg)

### 4. **断开线缆**

下一步，移除挤出主板上的4根线缆。

抓住接头小心将线缆拔出，请勿直接拔动线缆。

我们建议使用扁平工具将其轻轻撬出，以避造成免任何损坏。

![](https://wiki.bambulab.com/a1m/replace-th-board/disconnect_the_th_board_cables.jpeg)

请不要忘记拆下由2颗螺丝固定的涡流传感器线缆。

![](https://wiki.bambulab.com/a1m/replace-th-board/remove_the_eddy_sensor_screws.jpeg)

### 5. **取下挤出主板并断开进料霍尔板**

您现在可以将挤出主板从工具头上取下。**取下时，请小心地断开进料霍尔板的 FPC 柔性排线。**

慢慢向上拉直。

![a1_霍尔板线座.webp](https://wiki.bambulab.com/a1/troubleshooting/hms/1200_4500_0002_0003/a1_%E9%9C%8D%E5%B0%94%E6%9D%BF%E7%BA%BF%E5%BA%A7.webp)
![](https://wiki.bambulab.com/a1m/replace-th-board/remove_the_filament_sensor_ribbon_cable.jpeg)

### 6. **移除五通组件和传感器**

首先，卸下2颗将五通组件固定至挤出机的螺丝。

然后，轻轻地拔起五通组件，并将其放置在工具头上。

![](https://wiki.bambulab.com/a1m/replace-extruder-unit/remove_the_4-in-1_buffer_and_filament_sensor.jpeg)

### 7. **从五通组件上分离进料霍尔板**

卸下图中2颗螺丝，即可完全拉出进料霍尔板及其 FPC 排线。

![](https://wiki.bambulab.com/a1m/replace-filament-sensor/remove_the_2_screws_holding_the_filament_sensor.jpg.jpeg)

### **可选步骤**

在更换进料霍尔板的过程中，最好检查一下五通组件内部的磁铁是否完好无损。

下图为磁铁的完好外观。

![](https://wiki.bambulab.com/a1m/replace-filament-sensor/filament_buffer_magnet.jpg)

## **安装新的进料霍尔板**

### 1. **安装进料霍尔板至五通组件**

按照下图，对齐进料霍尔板和五通组件，使用2颗螺丝将其固定。

![](https://wiki.bambulab.com/a1m/replace-filament-sensor/align_sensor_and_screw_in_place.jpeg)

请注意，进料霍尔板上有一小块粘合区域。

您需要取下排线上的蓝色保护层，然后将排线压向进料霍尔板，使其就位。

排线需要与下图所示的两个孔之间的小槽对齐。

![](https://wiki.bambulab.com/a1m/replace-filament-sensor/filament_sensor_adhesive.jpeg)
![](https://wiki.bambulab.com/a1/maintenance/filament-sensor-replacement/20250313-175901.webp)

### 2. **安装五通组件至挤出机**

轻轻地将五通组件装回原位，并确保将排线放置至工具头的后方。

然后，拧紧上方的螺丝。

![](https://wiki.bambulab.com/a1m/replace-extruder-unit/insert_the_filament_buffer_back_in_the_extruder.jpeg)

### 3. **安装挤出主板至工具头**

打开挤出主板上 FPC 排线的卡扣，然后将 FPC 排线轻轻推入接头中，并关闭卡扣。

> 注意！插接时需注意排线正反，下左图的排线是正确的，右图金属面朝上是错误的！

![](https://wiki.bambulab.com/a1/maintenance/filament-sensor-replacement/线缆正反_new-ch.jpg)

按照下图所示的方式，小心地将挤出机电机电缆放置在 FPC 排线旁边。

完成这一步后，您可以轻轻地将挤出主板推回至原来的位置。

![](https://wiki.bambulab.com/a1m/replace-th-board/extruder_motor_wiring_on_th_board.jpeg)

### 4. **安装挤出主板螺丝**

使用3颗黑色螺丝，将挤出主板重新固定到工具头上。

![](https://wiki.bambulab.com/a1m/replace-th-board/install_the_th_board_screws.jpeg)
> 重要提醒！
>
> 不要过度拧紧螺丝，以免造成任何损坏。
>
> 在拧紧螺丝之前需要注意确认背面线缆避开螺丝孔，防止拧螺丝时扎穿线缆。
>
> ![](https://wiki.bambulab.com/a1/maintenance/filament-sensor-replacement/螺丝需注意1.jpg)

### 5. **重新接线**

将挤出主板放回原位后，您可以按照下图重新连接所有线缆。

- 热端加热组件（购买链接：[京东](https://item.jd.com/10086621431814.html) [天猫](https://detail.tmall.com/item.htm?abbucket=19&id=742608647813&rn=85cf658c1b1b317c1571024be894ae11&spm=a1z10.3-b-s.w4011-25177047232.13.352f1c79UnoIGf&skuId=5293816695460)）
- 挤出机电机
- 热端冷却风扇（购买链接：[京东](https://item.jd.com/10085237113101.html) [天猫](https://detail.tmall.com/item.htm?abbucket=19&id=742494478597&rn=50348b313765fa58496bd7e872f33726&spm=a1z10.3-b-s.w4011-25177047232.13.2b001c79zzjU9Z&skuId=5122905509690)）
- 部件冷却风扇（购买链接：[京东](https://item.jd.com/10085237672213.html) [天猫](https://detail.tmall.com/item.htm?abbucket=19&id=742158008755&rn=e96fdc9668de1bfe06ae88dd77fe78a2&spm=a1z10.3-b-s.w4011-25177047232.29.69711c792eXiBU&skuId=5122266397335)）
- 涡流传感器

![](https://wiki.bambulab.com/a1m/replace-th-board/th_board_cables_on_a1.jpeg)

### 6. **重新连接 USB-C 数据线**

将 USB- C 以正确的方向插入接口后，使用在第一步中拆下的4颗螺丝重新安装 USB-C 数据线。

![](https://wiki.bambulab.com/a1m/replace-th-board/install_the_usb_cable_and_4_screws.jpeg)
> **重要提醒！**
>
> **请不要过度拧紧螺丝，否则可能会导致螺纹损坏**。请注意对齐 USB-C 数据线的方向和背面的小凹槽。 USB-C 数据线只能用一种方式安装，正确的方向是数据线接头的凸起对准后方的凹槽。
>
> ![](https://wiki.bambulab.com/a1m/replace-usb-c-cable/usb_cable_orientation.jpeg)

### 7. **安装工具头后盖**

最后，安装 A1 工具头的后盖板。

后盖板使用卡扣固定。只需将后盖板上的两个卡扣对准，然后推入盖板，直到听到几声“咔嗒”声。

![](https://wiki.bambulab.com/a1m/replace-th-board/back_cover_of_the_print_head_a1m.jpeg)

## **功能验证**

将一段耗材插入至任意进料口直至到底，屏幕中的右下角图标会显示绿点；将耗材退出，绿点消失，则表明进料霍尔板正常工作。

![](https://wiki.bambulab.com/n1/maintenance/filaments_hub/20250226-191718.webp)

**操作后的校准步骤**

建议您在更换挤出机后进行一次全面校准，以确保打印机顺畅运行。

此外，强烈建议在进行打印之前[清洗纹理PEI打印板](../../general/textured-PEI-plate-not-working-as-expected.md)，因为在更换挤出机的过程中，构建板可能会受到污染。

## **潜在问题和解决方案**

如果您在安装新的进料霍尔板时遇到问题，请查阅以下列出的问题及其解决方案：

### **进料霍尔板无法工作**

参照步骤3 安装挤出主板至工具头，确保 FPC 排线正确连接至[挤出主板](../../a1-mini/th-board-replacement-guide.md)。

另外，参照可选步骤，确保五通组件内的磁铁能按照预期移动，并无附着任何杂物。

如果 FPC 排线已损坏，您需要更换进料霍尔板。（购买链接：[京东](https://item.jd.com/10086620804757.html) [天猫](https://detail.tmall.com/item.htm?abbucket=19&id=742413890652&rn=a2c4a71cc1ebc454113082a1179bbdfd&spm=a1z10.3-b-s.w4011-25177047232.13.59d31c79bCV2UL&skuId=5118758836326)）

### **热端温度为0**

参照步骤 5 重新接线，检查热端加热组件接头是否正确插入。

务必仔细对齐接头的引脚和[挤出主板](../../a1-mini/th-board-replacement-guide.md)。

如果问题仍然存在，热敏电阻线可能已损坏（白线）。

### **热端无法加热**

参照步骤 5 重新接线，检查热端加热组件接头是否正确插入。

 务必仔细对齐接头的引脚和[挤出主板](../../a1-mini/th-board-replacement-guide.md)。

如果问题仍然存在，加热器线可能已损坏（半透明线）。

### **打印机无法正确回中**

参照步骤 5 重新接线，检查涡流传感器线缆（5 和 6）是否正确连接至挤出主板。

## 结束语

> 我们希望这份指南为您提供了有效的信息，并真实地帮助了您。
>
> 如果您对本文中描述的过程有任何疑虑或疑问，您可以在开始操作前联系我们的客户服务团队。 我们随时准备为您提供帮助并回答您的任何问题。
>
> [点击这里提交服务工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)
