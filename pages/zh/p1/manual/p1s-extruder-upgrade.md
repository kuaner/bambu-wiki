---
path: zh/p1/manual/p1s-extruder-upgrade
title: "P1S 挤出机升级指南——打印磨蚀性耗材"
description: "学习如何升级 P1S 以打印磨蚀性耗材，提升打印性能。"
tags: ["p1s"]
created: 2025-08-05T08:43:38.935Z
updated: 2026-01-04T09:51:50.335Z
source: https://wiki.bambulab.com/zh/p1/manual/p1s-extruder-upgrade
---

P1S 3D 打印机配备不锈钢热端和挤出机，适合打印标准、非磨蚀性耗材，如 PLA、PETG、ABS、PA（尼龙）和 TPU。

![p1_extruder_gears.jpg](https://wiki.bambulab.com/p1/manual/p1s-extruder-upgrade/p1_extruder_gears.jpg)

但在打印磨蚀性耗材（如碳纤维、玻璃纤维、金属颗粒或夜光耗材）时，不锈钢部件会因耗材中的磨蚀颗粒而迅速磨损。对于最具磨蚀性的耗材，仅一次打印就可能损坏喷嘴。

下图对比了全新喷嘴（左）与磨损喷嘴（右）。右侧不锈钢喷嘴打印 PETG-CF 约 10 小时后出现了明显磨损。

![p1_nozzle_comparison.jpg](https://wiki.bambulab.com/p1/manual/p1s-extruder-upgrade/p1_nozzle_comparison.jpg)

从正面看，您可以观察到磨损的喷嘴已形成了更大的喷孔。

![abrasive_filament_nozzle_wear.jpg](https://wiki.bambulab.com/p1/manual/p1s-extruder-upgrade/abrasive_filament_nozzle_wear.jpg)

升级为硬化钢热端和硬化钢挤出机是一种性价比极高的改造方案，可以提升 P1S 性能，使其稳定打印这类高级耗材。

## **为什么不锈钢部件不适合磨蚀性耗材？**

不锈钢热端与挤出机相对硬化钢更软，适合打印通用耗材。而磨蚀性耗材中含有的碳纤维、玻璃纤维或夜光耗材中的磷光颗粒会如同砂纸，逐步侵蚀喷嘴内壁和挤出齿轮，导致：

- **挤出不一致：** 磨损的喷嘴会导致孔径不规则或扩大，使耗材流量不均、层间粘结不良、打印质量下降。
- **更换频繁：** 打印磨蚀性耗材时，不锈钢部件需经常更换，增加维护成本与停机时间。
- **精度下降：** 挤出齿轮磨损会造成上下料时耗材打滑，出现挤出不足或跳层。

## **升级为硬化钢热端与挤出机的优势**

为 P1S 更换硬化钢热端和挤出机可显著提升性能， 让 P1S 能可靠打印碳纤维、玻璃纤维、金属填充或夜光耗材，而不易快速磨损。

硬化钢更高的硬度和耐磨性，可与 P1S 的高速打印性能和封箱设计相结合，提供媲美专业工程机型的性能，却无需更换整机。对于希望在现有设备上打印磨蚀性耗材的玩家或专业用户，这是理想且经济的方案。

> ⚠️注意：硬化钢喷嘴有多种直径（如 0.4 mm、0.6 mm、0.8 mm），但不提供 0.2 mm 直径。建议使用 0.6 mm 或 0.8 mm 喷嘴以减少堵塞风险、改善熔融耗材流动状况，但可能略微降低细节表现。

## 如何升级挤出机与热端

### 选择升级路径

购买 P1S 硬化钢升级件，有两种方式：

- **整套组件**: 购买完整[硬化钢挤出机齿轮](https://item.jd.com/10069934893639.html)与[热端组件](https://item.jd.com/10067926410536.html)（请选择 P1 系列专用版本）。价格稍高，可保留原装不锈钢部件作为备用，且更换热端更快捷。
- **单独部件**:仅购买[硬化钢挤出机齿轮](https://item.jd.com/10069934893639.html)和[硬化钢喷嘴](https://item.jd.com/10058365307258.html)，成本略低，但需拆卸原挤出机与喷嘴进行安装。

由于整套组件升级更简便，我们提供了以下教程，操作前，请先完成退料操作，将工具头内的耗材退出工具头：

### 单独挤出机齿轮升级步骤

若打算单独更换部件，可接着参考以下步骤：

> ⚠️注意：下列步骤假设已按教程将挤出机和热端从打印机上拆下，需要先查看上面两个链接的整体拆装流程。

拆下挤出机后，**拧下后盖的四颗螺丝**。

![p1_extruder_assembly_screws.jpg](https://wiki.bambulab.com/p1/manual/p1s-extruder-upgrade/p1_extruder_assembly_screws.jpg)

**取出黄色挤出机齿轮**：从侧面轻拉，注意不要让中心的轴承掉落遗失。

![p1_yellow_extruder_gear.jpg](https://wiki.bambulab.com/p1/manual/p1s-extruder-upgrade/p1_yellow_extruder_gear.jpg)

**拆下挤出机从动轮**：松开侧面螺丝（见下图），注意不要将其拧下，且弹簧中的金属垫圈应保持原位。

![p1_extruder_idler_screw.jpg](https://wiki.bambulab.com/p1/manual/p1s-extruder-upgrade/p1_extruder_idler_screw.jpg)

松开螺丝后，取下从动轮组件，小心弹簧与垫圈不要脱落。

![p1_extruder_disassembled.jpg](https://wiki.bambulab.com/p1/manual/p1s-extruder-upgrade/p1_extruder_disassembled.jpg)

**安装硬化钢从动轮**：将其放入挤出机，从动杆弹簧如图所示对齐，拧紧螺丝以压缩弹簧。

![p1_extruder_reassembly_idler_gear.jpg](https://wiki.bambulab.com/p1/manual/p1s-extruder-upgrade/p1_extruder_reassembly_idler_gear.jpg)

**安装硬化钢挤出齿轮**：对准轴心，轻推入挤出机体，别忘记安装背部轴承。

![p1_extruder_reassembly_yellow_gear.jpg](https://wiki.bambulab.com/p1/manual/p1s-extruder-upgrade/p1_extruder_reassembly_yellow_gear.jpg)

复位后盖并拧紧四颗螺丝。

![p1_extruder_reassembly_cover.jpg](https://wiki.bambulab.com/p1/manual/p1s-extruder-upgrade/p1_extruder_reassembly_cover.jpg)

至此，挤出机齿轮升级完成。

### 单独升级喷嘴步骤

喷嘴升级较为复杂，需更多步骤：

首先取下的整个热端组件如下。

![p1_nozzle_assembly.jpg](https://wiki.bambulab.com/p1/manual/p1s-extruder-upgrade/p1_nozzle_assembly.jpg)

拆下热端风扇的两颗螺丝，并取下风扇。

![p1_hotend_fan_screws.jpg](https://wiki.bambulab.com/p1/manual/p1s-extruder-upgrade/p1_hotend_fan_screws.jpg)

小心拉出热端卡扣上的硅胶套。

![p1_nozzle_silicone_sock.jpg](https://wiki.bambulab.com/p1/manual/p1s-extruder-upgrade/p1_nozzle_silicone_sock.jpg)

拆下固定加热组件的金属卡箍，向下拉出。

![p1_nozzle_heater_clip.jpg](https://wiki.bambulab.com/p1/manual/p1s-extruder-upgrade/p1_nozzle_heater_clip.jpg)

取出加热器和热敏电阻，它们与喷嘴之间涂有导热脂，可能已干结，可以通过吹风机稍加加热以软化，移除时需要轻柔操作，避免拉断线缆。

- 将白色加热片向外滑出；
- 将热敏电阻从喷嘴侧孔轻拉取出。

![p1_nozzle_heater_and_thermistor_removal.jpg](https://wiki.bambulab.com/p1/manual/p1s-extruder-upgrade/p1_nozzle_heater_and_thermistor_removal.jpg)

移出的热敏电阻和加热片如下图。然后清理导热脂，用异丙醇擦拭加热器和热敏电阻，清除残留。

![p1_nozzle_heater_and_thermistor.jpg](https://wiki.bambulab.com/p1/manual/p1s-extruder-upgrade/p1_nozzle_heater_and_thermistor.jpg)

在硬化钢喷嘴上涂少量导热脂，注意方向，应该涂在和加热片接触的那一面上。

![p1_nozzle_thermal_grease.jpg](https://wiki.bambulab.com/p1/manual/p1s-extruder-upgrade/p1_nozzle_thermal_grease.jpg)

可以用棉签将导热脂薄薄涂在热端表面，并在热敏电阻孔内侧也涂抹适量，不要涂太多，可能会溢出。

![p1_nozzle_thermal_grease_spread.jpg](https://wiki.bambulab.com/p1/manual/p1s-extruder-upgrade/p1_nozzle_thermal_grease_spread.jpg)

**安装加热器与热敏电阻**：将加热器放在已涂脂的表面上，插入热敏电阻，理顺线缆，这时可能会挤出多余的导热脂，需要清理干净。

![p1_nozzle_heater_thermistor_reinstall.jpg](https://wiki.bambulab.com/p1/manual/p1s-extruder-upgrade/p1_nozzle_heater_thermistor_reinstall.jpg)

**复位金属卡箍**：将卡箍向上推至中部位置，确保其热敏电阻槽朝向热敏电阻线缆一侧。

![p1_nozzle_heater_clip_reinstall.jpg](https://wiki.bambulab.com/p1/manual/p1s-extruder-upgrade/p1_nozzle_heater_clip_reinstall.jpg)

完成上述步骤后，热端如下图所示。

![p1_nozzle_heater_reinstalled.jpg](https://wiki.bambulab.com/p1/manual/p1s-extruder-upgrade/p1_nozzle_heater_reinstalled.jpg)

然后重新安装硅胶套、安装热端风扇并拧紧螺丝，注意线缆方向。如下图所示。

![p1_hotend_fan_reinstalled.jpg](https://wiki.bambulab.com/p1/manual/p1s-extruder-upgrade/p1_hotend_fan_reinstalled.jpg)

## 将所有部件装回打印机

将挤出机与热端组件组合后再一起装回打印机会更容易操作，将热端和挤出机的两个螺孔位置对准，理顺线缆并穿过侧边的线缆卡扣，如下图所示。

![p1_extruder_reinstall_wire_management.jpg](https://wiki.bambulab.com/p1/manual/p1s-extruder-upgrade/p1_extruder_reinstall_wire_management.jpg)

用两颗螺丝将热端固定至挤出机体，如下图所示。

![p1_hotend_screw_reinstall.jpg](https://wiki.bambulab.com/p1/manual/p1s-extruder-upgrade/p1_hotend_screw_reinstall.jpg)

将整个组件对准工具头，拧入三颗螺丝，如下图所示。

![p1_extruder_screw_reinstall.jpg](https://wiki.bambulab.com/p1/manual/p1s-extruder-upgrade/p1_extruder_screw_reinstall.jpg)

连接三个线缆至工具头 MC 板，注意对齐针脚，避免损坏接口，如下图所示。

![p1_extruder_hotend_connectors_reinstall.jpg](https://wiki.bambulab.com/p1/manual/p1s-extruder-upgrade/p1_extruder_hotend_connectors_reinstall.jpg)

最后小心地插回切刀刀片，拧紧切刀刀柄上的固定螺丝，如下图所示。

![p1_cutter_reinstall.jpg](https://wiki.bambulab.com/p1/manual/p1s-extruder-upgrade/p1_cutter_reinstall.jpg)

安装完成后，工具头如下图所示。最后将前盖装回即可。

![p1_tool_head_reinstalled.jpg](https://wiki.bambulab.com/p1/manual/p1s-extruder-upgrade/p1_tool_head_reinstalled.jpg)

> ⚠️注意  
> 升级完成后，请在打印机屏幕上的设置页面，依次点击配件 > 喷嘴，选择您所更换的硬化钢喷嘴规格。

此时，您就可以使用磨蚀性耗材打印了！

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑并提供帮助！
>
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn) ; 点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
