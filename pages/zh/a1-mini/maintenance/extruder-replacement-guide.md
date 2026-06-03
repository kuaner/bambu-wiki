---
path: zh/a1-mini/maintenance/extruder-replacement-guide
title: "挤出机更换指南 - A1 系列"
description: "本指南演示如何更换 A1 系列的挤出机。"
tags: []
created: 2024-05-11T02:12:34.642Z
updated: 2025-12-01T03:07:25.246Z
source: https://wiki.bambulab.com/zh/a1-mini/maintenance/extruder-replacement-guide
---

![](https://wiki.bambulab.com/a1m/replace-extruder-unit/a1_extruder_unit.jpg)

## **何时使用本指南？**

本指南适用于挤出机出现无法轻易修复的问题。

需要更换挤出机的常见情况包括：

- 切刀刀柄损坏、螺纹滑丝
- 挤出机其他部件出现螺纹滑丝，导致挤出机出现问题
- 挤出机的涡流传感器故障、热床调平未达预期效果
- 挤出机电机疑似出现故障，并出现丢步
- 拓竹技术支持建议更换

## **工具和材料**

A1 mini 挤出机（购买链接：[京东](https://item.jd.com/10088164799110.html) [天猫](https://detail.tmall.com/item.htm?abbucket=19&id=743072298482&rn=83c0712a5bb1ed745bd488ffe671b258&spm=a1z10.3-b-s.w4011-25177047232.28.5e7c1c79nAM22c&skuId=5294017594255)）

- H2.0 六角扳手
- H1.5 六角扳手
- 25 分钟

### **安全警告**

> **重要提醒！**
>
> **在进行任何维护工作之前，务必关闭打印机的电源**，包括对打印机的电子元件和工具头电线进行维护。在打印机通电时进行此类操作可能会导致短路，从而损坏电子设备和造成安全隐患。
>
> 在维护或故障排除过程中，您可能需要拆卸热端等部件，从而暴露电线和电子元件。如果它们在打印机仍处于通电状态时相互接触或与其他金属、电子元件接触，就可能发生短路。**这将损坏打印机的电子元件和造成其他问题。**
>
> 因此，**在进行任何维护前，务必关闭打印机并断开电源**，以防止短路或损坏打印机的电子原件，从而确保维护工作安全有效地进行。如果您对本指南有任何疑问，请[点击这里提交工单](https://bambulab.com/zh/my/support/tickets?from=5)，我们将及时回复并提供帮助。

## **拆除旧的挤出机**

### 1. **拆除工具头后盖**

如下图所示，拉住后盖底部，小心撬开后盖。

![](https://wiki.bambulab.com/a1m/replace-th-board/remove_back_cover.jpeg)

### 2.  **拆除 USB-C 数据线**

然后，移除4颗螺丝。这些螺丝用于将 USB-C 数据线固定在 A1 mini 的工具头上。

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

### 5. **取下挤出主板**

您现在可以将挤出主板从工具头上取下。

**取下时，请小心地断开进料霍尔板的 FPC 柔性排线。**

慢慢向上拉直。避免晃动 FPC 排线，否则可能会导致损坏。如果该排线已经损坏，您可以[提交工单](https://bambulab.com/zh/my/support/tickets?from=5)，向我们的技术人员购买一个替换品。

![](https://wiki.bambulab.com/a1m/replace-th-board/remove_the_filament_sensor_ribbon_cable.jpeg)

### 6. **移除工具头前盖**

抓住前盖的底部，轻轻地按图示方向把它拉向自己。然后，固定前盖的夹子会松开，您即可将其取下。

![](https://wiki.bambulab.com/a1m/replace-filament-cutter/remove_the_print_head_front_cover.jpeg)

### 7. **移除打印机热端**

将喷嘴硅胶套轻轻拉向自己，取下喷嘴硅胶套，然后从加热器上取下热端。所有步骤都已标注在挤出机贴纸上。

执行此步骤后，才能在下一步中移除挤出机。

![](https://wiki.bambulab.com/a1m/replace-hotend-cooling-fan/remove_the_nozzle.jpg)

### 8. **移除挤出机**

卸下下图所示的4颗螺丝后，您可以轻轻地将挤出机拉向您的方向。但是，暂时不要卸下挤出机。

> **注意事项**
>
> 挤出机左侧有一根传感器线缆。请勿卸下挤出机，以免造成损坏。

![](https://wiki.bambulab.com/a1m/replace-hotend-cooling-fan/remove_the_extruder_on_a1.jpeg)

### 9. **移除左侧线缆槽**

热端冷却风扇线缆、连接到挤出机的涡流传感器线缆，都是通过左侧的线缆槽布线的。

移除挤出机前，您需要轻轻将线缆槽推向打印头的背面，具体操作请参考下图。

![](https://wiki.bambulab.com/a1m/replace-hotend-cooling-fan/remove_the_left_cable_channel.jpeg)

移除线缆槽后，可以将挤出机拉向自己，将其从打印机上取下。

### 10. **移除五通组件和传感器**

首先，卸下2颗将五通组件固定至挤出机的螺丝。

然后，轻轻地拔起五通组件，并将其放置在工具头上。

避免用力将其拔出，否则可能会损坏进料霍尔板的 FPC 排线。

![](https://wiki.bambulab.com/a1m/replace-extruder-unit/remove_the_4-in-1_buffer_and_filament_sensor.jpeg)

## **安装新的挤出机**

### 1. **安装五通组件和传感器至挤出机**

为了安装刚拆下来的五通组件，先将挤出机暂时放置在工具头上。

然后，轻轻地将五通组件推回原位。

![](https://wiki.bambulab.com/a1m/replace-extruder-unit/insert_the_filament_buffer_back_in_the_extruder.jpeg)

### 2. **将风扇和涡流传感器线缆穿过线缆槽**

如下图所示，小心地将风扇和挤出机传感器线缆穿过线槽。

按图示方向，沿着热端上的小夹子将线缆槽盖推回。

![](https://wiki.bambulab.com/a1m/replace-hotend-cooling-fan/route_the_wires_and_put_the_channel_cover_back.jpeg)

> 布线时请格外小心，您需要像下图那样仔细放置线缆。
>
> 如果线缆未按图中所示布线，您将无法重新成功安装挤出机。
>
> ![](https://wiki.bambulab.com/a1m/replace-hotend-cooling-fan/route_the_left_channel_wires.jpeg)

### 3. **重新安装挤出机至工具头**

安装好线缆槽后，您可以使用4个螺丝将挤出机固定到工具头上，如下图所示。

![](https://wiki.bambulab.com/a1m/replace-hotend-cooling-fan/remove_the_extruder_on_a1.jpeg)

### 4. **安装挤出主板至工具头**

首先，打开黑色的塑料卡扣，将进料霍尔板的 FPC 排线轻轻推入，插入卡扣中，然后将卡扣扣上，听到清脆的“咔哒”一声，则表明排线已锁紧。

![](https://wiki.bambulab.com/a1m/replace-th-board/install_the_filament_sensor_ribbon_cable.jpeg)

按照下图所示的方式，小心地将挤出机电机电缆放置在 FPC 排线旁边。

完成这一步后，您可以轻轻地将挤出主板推回至原来的位置。

![](https://wiki.bambulab.com/a1m/replace-th-board/extruder_motor_wiring_on_th_board.jpeg)

### 5. **安装挤出主板螺丝**

使用3颗黑色螺丝，将挤出主板重新固定到工具头上。

![螺丝.png](https://wiki.bambulab.com/%E8%9E%BA%E4%B8%9D.png)

> 重要提醒！
>
> 不要过度拧紧螺丝，以免造成任何损坏。

### 6. **重新接线**

将新的挤出主板放回原位后，您可以按照下图重新连接所有线缆。

- 热端加热组件（购买链接：[京东](https://item.jd.com/10086621431814.html) [天猫](https://detail.tmall.com/item.htm?abbucket=19&id=742608647813&rn=85cf658c1b1b317c1571024be894ae11&spm=a1z10.3-b-s.w4011-25177047232.13.352f1c79UnoIGf&skuId=5293816695460)）
- 挤出机电机
- 热端冷却风扇（购买链接：[京东](https://item.jd.com/10085237113101.html) [天猫](https://detail.tmall.com/item.htm?abbucket=19&id=742494478597&rn=50348b313765fa58496bd7e872f33726&spm=a1z10.3-b-s.w4011-25177047232.13.2b001c79zzjU9Z&skuId=5122905509690)）
- 部件冷却风扇（购买链接：[京东](https://item.jd.com/10085237672213.html) [天猫](https://detail.tmall.com/item.htm?abbucket=19&id=742158008755&rn=e96fdc9668de1bfe06ae88dd77fe78a2&spm=a1z10.3-b-s.w4011-25177047232.29.69711c792eXiBU&skuId=5122266397335)）
- 热端传感器  
  ![线缆.png](https://wiki.bambulab.com/%E7%BA%BF%E7%BC%86.png)

### 7. **重新连接 USB-C 数据线**

将 USB- C 以正确的方向插入接口后，使用在第一步中拆下的4颗螺丝重新安装 USB-C 数据线。

![](https://wiki.bambulab.com/a1m/replace-th-board/install_the_usb_cable_and_4_screws.jpeg)

> **重要提醒！**
>
> **请不要过度拧紧螺丝，否则可能会导致螺纹损坏**。请注意对齐 USB-C 数据线的方向和背面的小凹槽。 USB-C 数据线只能用一种方式安装，正确的方向是数据线接头的凸起对准后方的凹槽。
>
> ![](https://wiki.bambulab.com/a1m/replace-usb-c-cable/usb_cable_orientation.jpeg)

### 8. **安装工具头后盖**

最后，安装 A1 mini 工具头的后盖板。

后盖板使用卡扣固定。只需将后盖板上的两个卡扣对准，然后推入盖板，直到听到几声“咔嗒”声。

![](https://wiki.bambulab.com/a1m/replace-th-board/back_cover_of_the_print_head_a1m.jpeg)

### 9. **安装热端和硅胶套**

按照挤出机贴纸上的指引，将热端重新安装到工具头上。

然后，使用夹子将其锁紧，并安装硅胶套。

![](https://wiki.bambulab.com/a1m/replace-hotend-cooling-fan/remove_the_nozzle.jpg)

### 10. **装工具头前盖**

将工具头顶部的卡扣对准，然后轻轻按压前盖的底部。

安装完成后，您可以听到“咔嗒”声。

![](https://wiki.bambulab.com/a1m/replace-filament-cutter/attach_the_front_cover.jpeg)

## **功能验证**

打开打印机并尝试上料。如果操作成功，您应该可以听到电机的声音，上料过程也将正常进行。

## **操作后的校准步骤**

建议您在更换挤出机后进行一次全面校准，以确保打印机顺畅运行。

此外，强烈建议在进行打印之前[清洗纹理PEI打印板](../../general/textured-PEI-plate-not-working-as-expected.md)，因为在更换挤出机的过程中，构建板可能会受到污染。

## **潜在问题和解决方案**

如果您在安装新的挤出机时遇到问题，请查阅以下列出的问题及其解决方案：

### **热端温度为0**

参照\_步骤 6 重新接线\_，检查热端加热组件接头是否正确插入。

务必仔细对齐接头的引脚和[挤出主板](../th-board-replacement-guide.md)。

如果问题仍然存在，热敏电阻线可能已损坏（白线）。

### **热端无法加热**

参照\_步骤 6 重新接线\_，检查热端加热组件接头是否正确插入。 务必仔细对齐接头的引脚和[挤出主板](../th-board-replacement-guide.md)。 如果问题仍然存在，加热器线可能已损坏（半透明线）。

### **打印机无法正确回中**

参照\_步骤 6 重新接线\_，检查涡流传感器线缆（5 和 6）是否正确连接至挤出主板。

### **进料霍尔板不再工作**

参照\_步骤4 安装挤出主板至工具头\_，检查 FPC 排线是否正确连接至[挤出主板](../th-board-replacement-guide.md)。

如果 FPC 排线已损坏，您需要更换进料霍尔板。（购买链接：[京东](https://item.jd.com/10086620804757.html) [天猫](https://detail.tmall.com/item.htm?abbucket=19&id=742413890652&rn=a2c4a71cc1ebc454113082a1179bbdfd&spm=a1z10.3-b-s.w4011-25177047232.13.59d31c79bCV2UL&skuId=5118758836326)）

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 我们希望能确保您安全有效地进行操作。如果您对本指南描述的过程有任何疑虑或问题，建议您在开始操作前联系我们友好的客户服务团队。
>
> 我们随时准备为您解答疑问并提供帮助。[点击此处联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/cn/im)
