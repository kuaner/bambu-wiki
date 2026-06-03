---
path: zh/h2s/maintenance/replace-th-board
title: "更换 H2S TH 板"
description: ""
tags: []
created: 2025-08-26T04:20:38.787Z
updated: 2026-04-27T08:42:50.490Z
source: https://wiki.bambulab.com/zh/h2s/maintenance/replace-th-board
---

## H2S TH 板

## 何时使用？

可能需要更换 H2S 打印机挤出主板（简写为 TH 板）的常见问题包括：

- 进料霍尔板连接器损坏
- 热端加热片和 NTC 传感器电路损坏
- 挤出机电机未按预期转动，可能是由于步进电机驱动故障
- 拓竹技术支持推荐更换

## 工具和材料

- 新的 TH 板
- H1.5 内六角扳手
- 30 分钟

## 螺丝清单

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-th-board/image-14.png)

- 螺丝 A: 部件冷却风扇背面（和后盖共锁）以及工具头后盖螺丝，共 3 颗：BT2x6.5
- 螺丝 B: 部件冷却风扇左右两侧螺丝，共 2 颗： BT2x5
- 螺丝 C: TH 板螺丝，共 3 颗：BT2x5

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，**请关闭打印机电源并断开电源连接**，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。
>
> 如果您对本指南有任何疑问，请[点击提交服务工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)，我们将及时回复并为您提供所需的帮助。

## 移除旧的 TH 板

### 步骤 1：松开部件冷却风扇

拧下部件冷却风扇的 3 颗螺丝，其中背面的1颗螺丝与工具头后盖共锁。

松开螺丝后，请勿拉扯风扇，使风扇自然下垂即可，以免损坏连接器。

![左侧螺丝（从前往后看）](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-th-board/image-13.png)

![右侧螺丝（从前往后看）](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-th-board/image-12.png)

![背面螺丝（从前往后看）](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-th-board/image-10.png)

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-th-board/image-9.png)

### 步骤 2：松开工具头后盖

移除工具头后盖上方的2颗螺丝，打开模块接口盖子。

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-th-board/image-8.png)

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-th-board/image-11.png)

打开接口盖子后，手指可从内壁轻微用力，往后推工具头后盖。

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-th-board/image.png)

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-th-board/image-1.png)

### 步骤 3：断开 TH 板上的所有插头（进料霍尔插头和 USB-C 插头除外）

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-th-board/image-2.png)

| 序号 | 部件名称 | 序号 | 部件名称 |
| --- | --- | --- | --- |
| 1 | 挤出电机 | 2 | 进料霍尔组件 |
| 3 | 热端加热组件 | 4 | 热端风扇 |
| 5 | 部件冷却风扇 | 6 | 工具头摄像头 |
| 7 | 涡流线圈 |  |  |

断开挤出电机和工具头摄像头插头；

![12.webp](https://wiki.bambulab.com/h2s/maintenance/replace-extruder-unit/12.webp)

断开热端加热组件插头；

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-th-board/image-4.png)

撕开部件冷却风扇插头上的醋酸胶布并保存好，安装时需要贴回此胶布，可重复使用。

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-th-board/image-6.png)

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-th-board/image-7.png)

捏住根部，以垂直PCB板的方向施力，断开部件冷却风扇和热端风扇插头。

![hotend-fan.webp](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-th-board/hotend-fan1.webp)

![part-cooling-fan.webp](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-th-board/part-cooling-fan1.webp)

同理，撕开涡流线圈的胶布并保存好，断开涡流线圈的插头。

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-th-board/image-15.png)

![eddy_current_coil.webp](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-th-board/eddy_current_coil.webp)

### 步骤 4：拧下 TH 板上的 3 颗螺丝

松开工具头上最靠近拖链支架的那段拖链

![remove-cable-chain.webp](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-th-board/remove-cable-chain1.webp)

拧下 TH 板上的 3 颗螺丝；

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-th-board/image-16.png)

### 步骤 5：断开进料霍尔插头和 USB-C 插头

小心移动 TH 板（手指抵着散热片，防止散热片脱落），创造出断开进料霍尔板插头的操作空间后，断开插头。

![move_th_board.webp](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-th-board/move_th_board.webp)  
![disconnect_th_board.webp](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-th-board/disconnect_th_board.webp)

翻转 TH 板，慢慢地晃动拉出 USB-C 线缆；

![pull_usb-c.webp](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-th-board/pull_usb-c.webp)  
![pull_usb-c-2.webp](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-th-board/pull_usb-c-2.webp)

## 安装新的 TH 板

### 步骤 1：为新的 TH 板涂抹导热硅脂

如图片所示，为新的 TH 板这 3 个部位的电子器件涂抹上导热硅脂，并利用散热片压住导热硅脂，请小心操作，不要将导热硅脂粘到插头或插座上；为了清晰的看出涂抹位置，你也可与旧的 TH 板进行对比。

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-th-board/image-17.png)

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-th-board/glue.webp)

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-th-board/new_th.webp)

### 步骤 2：连接进料霍尔插头和 USB-C 插头

字母 A 朝 TH 板的背面，慢慢的晃动推动 USB-C 线缆，将 USB-C 线缆插到底，插不动的时候，表示插到底。

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-th-board/image-18.png)

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-th-board/plug_usb.webp)

翻转 TH 板（手指抵着散热片，防止散热片脱落），向上拉 USB-C 线缆，使进料霍尔板插头位于合适的高度，插入插头。

![insert-hall.webp](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-th-board/insert-hall.webp)

### 步骤 3：锁入 TH 板的 3 颗螺丝

检查其他 5 个插头没有被压住的后，对准螺丝孔位，锁入 3 颗螺丝。

![review-plug.webp](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-th-board/review-plug.webp)

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-th-board/image-20.png)

> 注意：如果你发现比较难对准螺丝孔位，可轻微向上拉扯 USB-C 线，避免多余线长影响对准螺丝孔。

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-th-board/image-19.png)

装回拖链支架。

![install_cable_chain_bracket.webp](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-th-board/install_cable_chain_bracket.webp)

### 步骤 4：插入 TH 板上的所有插头

![insert-all-plug.webp](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-th-board/insert-all-plug.webp)

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-th-board/image-2.png)

| 序号 | 部件名称 | 序号 | 部件名称 |
| --- | --- | --- | --- |
| 1 | 挤出电机 | 2 | 进料霍尔组件 |
| 3 | 热端加热组件 | 4 | 热端风扇 |
| 5 | 部件冷却风扇 | 6 | 工具头摄像头 |
| 7 | 涡流线圈 |  |  |

> 注意：插头4和插头5分别是热端风扇和部件冷却风扇的插头，为了避免插错，这里使用了防呆设计，热端风扇的针脚数量为5，部件冷却风扇的针脚数量为4，请勿插错或强行插入，以免损坏插头。

插入涡流线圈和 2 个风扇插头时，金属色的这面朝上,并且贴回醋酸胶布。

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-th-board/image-21.png)

工具头摄像头和挤出电机插头插到位后，卡扣应该是平整的，且指示线是水平的。

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-th-board/image-22.png)

预对准风扇的螺丝孔位，将风扇线缆排在 TH 上，并向上拉动，将多余的线缆折叠，避免被风扇外壳或工具头后盖压破导致风扇异常。

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-hotend-heating-assembly/manage_cable.webp)

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-th-board/image-23.png)

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-th-board/image-24.png)

整理好线缆后，插入热端加热组件插头，并用热端加热组件插头和线缆压住部件冷却风扇线缆。

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-th-board/image-25.png)

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-th-board/image-26.png)

> 插入热端加热组件时，确保对准孔位，不要错排。

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-th-board/image-27.png)

### 步骤 5：安装工具头后盖

安装工具头后盖；

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-th-board/image-28.png)

安装后，注意检查部件冷却风扇线缆是否位于专用的缺口处，避免被后盖边框挤压；

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-th-board/image-29.png)

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-th-board/image-30.png)

锁入 2 颗后盖固定螺丝。

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-th-board/image-31.png)

### 步骤 6：安装部件冷却风扇

对准螺丝孔，安装部件冷却风扇；卡入风扇时，注意不要压住风扇线缆。

> 如果线缆过长，需退回至安装指南的步骤一，先折叠多余的线缆。

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-th-board/image-32.png)

锁入 3 颗螺丝，固定部件冷却风扇。

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-th-board/image-33.png)

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-th-board/image-34.png)

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-th-board/image-35.png)

## 操作后的校准步骤

建议在完成更换后，对打印机进行校准操作。

![](https://public-cdn.bblmw.com/wiki/new/h2/h2s/maintenance/replace-th-board/image-36.png)

## 潜在问题和解决方案

如果在安装新挤出主板时遇到问题，请检查以下列出的潜在问题和解决方案：

### 热端温度为 0℃

检查热端加热组件连接器，确认其正确插入，如步骤 3 ，重新连接所有线缆。

请确保所有线缆跟挤出主板对齐。

如果问题仍然存在，则热敏电阻导线可能已损坏（白色导线）。

### 热端无法加热

检查热端加热组件连接器，确认其正确插入，如步骤 3 ，重新连接所有线缆。

请确保所有线缆跟挤出主板对齐。

如果问题仍然存在，加热器电线可能已损坏（半透明电线）。

### 打印机无法回中

检查涡流线圈插头，确认它们已正确安装在挤出主板背面，如步骤 3 ，重新连接所有线缆。

### 进料霍尔板不工作

检查进料霍尔插头，确认它们已正确安装在挤出主板背面，如步骤 3 ，重新连接所有线缆。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)，点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
