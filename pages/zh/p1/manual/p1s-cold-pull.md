---
path: zh/p1/manual/p1s-cold-pull
title: "冷拔的概念及其操作"
description: "学习冷拔喷嘴的原因和操作步骤，清除喷嘴堵塞，保持其畅通。"
tags: ["p1s"]
created: 2025-08-05T08:58:28.810Z
updated: 2026-04-27T03:03:24.697Z
source: https://wiki.bambulab.com/zh/p1/manual/p1s-cold-pull
---

## 什么是冷拔？

冷拔是一种 3D 打印机的清理维护手段，通过拔出耗材清理喷嘴内部的灰尘、堵塞或残留物。因为耗材在冷却时可以与喷嘴内部残留物结合，拔出时即可物理带出一些烧焦耗材、灰尘或小堵塞。

定期执行冷拔可使耗材流动一致性更好，避免挤出不足或打印线条不均等缺陷。尤其在更换耗材类型打印时，建议及时冷拔。

操作基本流程为先将喷嘴加热以软化耗材，然后降温至部分固化，最后拔出耗材以带出内部污染物。

## 注意事项

冷拔可使用多种耗材，温度视耗材而定。以下示例以 PLA 为例，也可使用 PA、ABS、ASA 等。

如果热端内已有严重堵塞，可能需先手动清除堵塞才能冷拔。

若之前打印过普通耗材，在切换到使用 TPU 前，需要用原耗材进行冷拔，清除热端残留耗材。因为 TPU 柔软，可能无法自己将之前的热端残留耗材顶出，易导致堵塞。

## 如何在 P1S 上执行冷拔？

将喷嘴温度设置为比耗材正常打印温度略高。本例以 PLA 为例，设为 230 °C。

![cold_pull_p1_heat_nozzle.jpg](https://wiki.bambulab.com/p1/manual/p1s-cold-pull/cold_pull_p1_heat_nozzle.jpg)

待热端达到设定温度后，选中**挤出机**选项，连续点击**进料**按钮（**向下键**）几次，直至看到耗材从喷嘴中出来。

![cold_pull_p1_extrude_filament.jpg](https://wiki.bambulab.com/p1/manual/p1s-cold-pull/cold_pull_p1_extrude_filament.jpg)

将热端温度调至 70 °C，待其降温。温度降至 200 °C 以下后，每隔 2–3 秒点击几次**进料**按钮，同时倾听挤出机声音。 如果听到挤出机开始丢步，请立即停止挤出。PLA 通常在约 150 °C 丢步。

![cold_pull_p1_confirm_build_plate_down.jpg](https://wiki.bambulab.com/p1/manual/p1s-cold-pull/cold_pull_p1_confirm_build_plate_down.jpg)

此操作可将耗材推进喷嘴内部，与残留物结合。热端继续冷却至 70 °C 时，取下工具头前盖并拔出料管。

![cold_pull_p1_remove_ptfe.jpg](https://wiki.bambulab.com/p1/manual/p1s-cold-pull/cold_pull_p1_remove_ptfe.jpg)

当温度降至 70 °C 后，选中**挤出机**选项，点击**退料**按钮（**向上键**）开始退料。

![cold_pull_p1_retract_filament.jpg](https://wiki.bambulab.com/p1/manual/p1s-cold-pull/cold_pull_p1_retract_filament.jpg)

退料操作结束后，手动向上帮助挤出机松脱耗材。无需用力过猛，只需轻轻拉动尝试，您如果感觉到耗材脱离挤出机齿轮了再将其完整拉出。手动拔出只是协助挤出机完成耗材的退出，避免丢步或拉丝。

![cold_pull_p1_pull_on_filament.jpg](https://wiki.bambulab.com/p1/manual/p1s-cold-pull/cold_pull_p1_pull_on_filament.jpg)

正确操作后，拔出的耗材末端会呈类似喷嘴内壁的微锥形。

![cold_pull_p1_result.jpg](https://wiki.bambulab.com/p1/manual/p1s-cold-pull/cold_pull_p1_result.jpg)

完成冷拔后，若耗材上附着黑色灰尘或碎屑，可重复执行几次，直至耗材干净为止。

## 视频指南

以下视频演示冷拔流程（视频是针对 X1C 机型的，但与 P1S 操作仅在屏幕交互上有所不同，过程其实是相同的）：

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑并提供帮助！
>
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn) ; 点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5) 。
