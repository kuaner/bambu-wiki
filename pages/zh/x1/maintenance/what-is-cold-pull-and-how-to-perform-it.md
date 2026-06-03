---
path: zh/x1/maintenance/what-is-cold-pull-and-how-to-perform-it
title: "冷拔的概念及其操作（X1系列）"
description: "学习冷拔喷嘴的原因和操作步骤，清除喷嘴堵塞，保持其畅通。"
tags: ["x1"]
created: 2025-08-18T03:58:23.680Z
updated: 2026-05-06T03:15:38.472Z
source: https://wiki.bambulab.com/zh/x1/maintenance/what-is-cold-pull-and-how-to-perform-it
---

## 什么是冷拔？

冷拔是一种 3D 打印机的清理维护手段，用于清理喷嘴内部的杂质、堵塞物或残余耗材。它的原理是先加热喷嘴以软化耗材，然后冷却使耗材部分固化，再将其拉出，从而带出附着在喷嘴内部的污染物。

耗材在冷却阶段会像一个“塞子”一样，与喷嘴内部的残留物粘附在一起。将其拉出时，便会粘走这些污染物，例如烧焦的耗材、灰尘或细小堵塞物。

定期执行冷拔可使耗材流动一致性更好，避免挤出不足或打印线条不均等缺陷。尤其在更换耗材类型打印时，建议及时冷拔。

## 注意事项

- 冷拔可使用多种耗材，温度视耗材而定。以下示例以 PLA 为例，也可使用 PA、ABS、ASA 等。
- 如果热端内已有严重堵塞，可能需先手动清除堵塞才能冷拔。
- 若之前打印过普通耗材，在切换到使用 TPU 前，需要用原耗材进行冷拔，清除热端残留耗材。因为 TPU 柔软，可能无法自己将之前的热端残留耗材顶出，易导致堵塞。

> 对于 PLA 耗材，推荐冷拔温度一般在 70–100°C 之间。若是第一次操作，建议设置为 70°C，以避免耗材过软而造成挤出机堵塞。

将喷嘴温度设置为比耗材正常打印温度略高。本例以 PLA 为例，设为 220 °C。

![nozzletemp.png](https://wiki.bambulab.com/x1/maintenance/cold-pull/nozzletemp.png)

等待热端升温到设定温度，然后通过控制面板挤出一些耗材。通常点击几次挤出按钮，直到看到耗材从喷嘴挤出即可。

![喷嘴温度.png](https://wiki.bambulab.com/x1/maintenance/cold-pull/%E5%96%B7%E5%98%B4%E6%B8%A9%E5%BA%A6.png)

下方动图展示了耗材挤出的过程。  
![filament-extruding.gif](https://wiki.bambulab.com/x1/maintenance/cold-pull/filament-extruding.gif)

接下来，将热端温度设置为 70°C，并等待其冷却。

![70度.png](https://wiki.bambulab.com/x1/maintenance/cold-pull/70%E5%BA%A6.png)

当温度降至 200°C 以下时，可以每隔 2-3 秒点击一次挤出按钮，继续缓慢挤出耗材，这能帮助耗材被压入喷嘴内部，与杂质融合。同时仔细倾听挤出机声音。

> 喷嘴温度低于 170℃ 时，设备会提示请将喷嘴温度升高至170℃ 以上，请点击“不再提醒”。

当听到电机打滑的异响（通常发生在 PLA 约 150°C 时），请立即停止点击。在热端继续冷却至 70°C 的过程中，取下工具头的前盖并断开 PTFE 管。

![](https://wiki.bambulab.com/x1/maintenance/cold-pull/removing-hotend-cover.jpeg)

以下动图展示了操作方法。

![removing-the-cover.gif](https://wiki.bambulab.com/x1/maintenance/cold-pull/removing-the-cover.gif)

当热端降至设定温度 70°C 后，点击屏幕上向上的三角按钮进行耗材回抽。

![70.png](https://wiki.bambulab.com/x1/maintenance/cold-pull/70.png)

回抽完成后，可以手动向上拉耗材，帮助挤出机将其拔出。**不要用力过猛** —— 无需施加很大力气。手动操作只是为了协助挤出机顺利拉出耗材，避免其打滑或磨损耗材。

![](https://wiki.bambulab.com/x1/maintenance/cold-pull/pulling-the-filament-upwards.png)

通常在点击几次回抽按钮后，耗材会脱离挤出机的夹持，此时就可以将剩余耗材拉出。如果操作正确，拉出的耗材尖端会带有一个微小锥形，类似喷嘴内部的形状。

![](https://wiki.bambulab.com/x1/maintenance/cold-pull/filament-nozzle-tip.png)

完成了！您已经成功学会用冷拔来清理喷嘴。如果发现拉出的耗材上带有黑点或杂质，建议多重复几次，直到耗材表面干净为止。

## **视频指南**

以下为冷拔操作的教学视频：

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑并提供帮助！
>
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn) ; 点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5) 。
