---
path: zh/h2s/maintenance/nozzle-cold-pull-maintenance-and-cleaning
title: "H2S 喷嘴冷拔维护清理"
description: "本文介绍如何对 H2S 进行冷拔维护清理"
tags: ["h2s"]
created: 2025-08-26T06:22:33.304Z
updated: 2026-07-22T04:15:40.666Z
source: https://wiki.bambulab.com/zh/h2s/maintenance/nozzle-cold-pull-maintenance-and-cleaning
---

> \* 部分图片使用了 H2D 机型的显示屏、app 等界面截图，不影响实际操作。

## 什么是冷拔？

**冷拔**是一种 3D 打印机的清理维护手段，通过拔出耗材清理喷嘴内部的灰尘、堵塞或残留物。操作时，先加热喷嘴软化耗材，等待耗材冷却至部分固化后拔出，以带走内部污染物。

冷却阶段的耗材类似“塞子”，与喷嘴内部残留物粘合，拔出时即可物理带出一些烧焦耗材、灰尘或小堵塞。

定期执行冷拔可使耗材流动一致性更好，避免挤出不足或打印线条不均等缺陷。尤其在更换耗材类型打印时，建议您及时进行冷拔。

## 何时需要冷拔？

- 当出现挤出不足或打印线条不均等缺陷时；
- 从普通耗材切换到 TPU（TPU 非常柔软，对喷嘴阻力极为敏感）时；
- 当挤出电机频繁出现过载报错时；
- 日常维护，保持喷嘴清洁。

## 耗材类型与操作温度

PLA 或 PETG 最适用于执行冷拔操作。其他类型耗材容易断裂并在喷嘴内部残留，不适用于冷拔。

- **低温耗材（如PLA、PETG、TPU、PVA）：**冲刷温度约为 250°C；
- **高温耗材（ABS、ASA、PA、PC）：**冲刷温度约为 290°C；
- **超高温耗材（PPS、PPA）：**冲刷温度约为 320°C。

冷拔过程中，如果发现阻力较大且耗材丝容易断裂，可以适当提高冷拔温度； 如果耗材丝在过于容易被拉断，可以适当降低温度。

> 在使用 PPS-CF 等高温材料后，若需更换 PLA 等低温材料，务必先彻底清理残留的高温料。若未清理干净，后续低温材料熔融后可能无法将残留高温料完全顶出，极易导致挤出机堵料。  
> 清理方法如下：  
> **高温手动冲刷**：将喷嘴温度提升至适配前序高温材料（如 PPS-CF）的打印温度，手动推动耗材进料，利用新耗材的流动性冲刷喷嘴及喉管内残留的高温料。  
> **选用高温耗材过渡**：优先使用打印温度较高的过渡耗材（如 PETG）进行清理，待挤出料纯净后，再更换为目标低温材料；若没有 PETG，也可选用 ABS 作为过渡耗材。

## 如何在 H2S 上执行冷拔？

### 1. **启动冷拔功能**

在打印机屏幕上，依次选择 **工具箱 > 喷嘴冷拔维护**，然后点击 **下一步**\*。\*

![冷拔_(1).gif](https://wiki.bambulab.com/h2s/maintenance/nozzle-cold-pull-maintenance-and-cleaning/%E5%86%B7%E6%8B%94_(1).gif)

### 2. **设置冷拔参数**

选择打印机装载的喷嘴类型和耗材类型。例如，选择 **0.4 mm 喷嘴** 和 **PLA 耗材** 进行标准冷拔操作。确认后点击 **开始**。

![image-3.png](https://wiki.bambulab.com/h2s/maintenance/nozzle-cold-pull-maintenance-and-cleaning/image-3.png)

### 3. **拆卸铁氟龙料管**

按照屏幕提示，将料管从工具头上拔下。操作时，**向下按住端口**，同时**向上拔起料管**直至脱离。

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/h2-nozzle-cold-pull-maintenance-and-cleaning/1.webp)

### 4. 自动冲刷和冷拔

当喷嘴达到设定温度后，剪下至少 **30 cm 长度的耗材丝**插入挤出机。

![image.png](https://wiki.bambulab.com/h2s/maintenance/nozzle-cold-pull-maintenance-and-cleaning/image.png)

打印机会自动执行冲刷及耗材回填的动作。冲刷完成后，喷嘴会降温至冷拔温度，挤出机缓慢进行冷拔耗材丝来清理喷嘴。

> **注意:**
>
> 进入自动流程后喷嘴将会升温，请勿用手触摸喷嘴，以防烫伤。
>
> 在机器自动冲刷冷拔的过程中，可能由于冲刷温度过高产生烟雾。请关闭机器前盖以及上盖，等待冲刷完成后再打开。

![image-1.png](https://wiki.bambulab.com/h2s/maintenance/nozzle-cold-pull-maintenance-and-cleaning/image-1.png)

### 5. **自动或手动冷拔**

冷却后，挤出机会自动进行冷拔，直至耗材达到最大可回抽位置。手动拔出时，需要握住挤出机支架，再缓慢垂直向上拔出耗材。

![image6.png](https://wiki.bambulab.com/h2s/maintenance/nozzle-cold-pull-maintenance-and-cleaning/image6.png)

## 评估冷拔效果

观察冷拔后的耗材丝末端：

- 洁净的耗材末端应完整呈现喷嘴的形状，无残留物；
- 若有异色、杂质或碳化沉积物，需重复多次冷拔直到耗材丝达到表面洁净无且残留为止。

![image-2.png](https://wiki.bambulab.com/h2s/maintenance/nozzle-cold-pull-maintenance-and-cleaning/image-2.png)

## 冷拔完成后

流程结束后，务必将铁氟龙料管牢固插回工具头原位，以确保耗材通道密封，便于后续使用。现在，您可以重新装载耗材并进行挤出测试，以确认耗材流动顺畅。如果一切顺利，就可以发起新的打印任务了。

![image.png](https://wiki.bambulab.com/h2s/maintenance/nozzle-cold-pull-maintenance-and-cleaning/image.png)

![image8.png](https://wiki.bambulab.com/h2s/maintenance/nozzle-cold-pull-maintenance-and-cleaning/image8.png)

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
