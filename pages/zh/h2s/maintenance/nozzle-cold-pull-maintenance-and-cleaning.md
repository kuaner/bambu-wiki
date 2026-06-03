---
path: zh/h2s/maintenance/nozzle-cold-pull-maintenance-and-cleaning
title: "H2S 喷嘴冷拔维护清理"
description: "学习如何对 H2S 进行冷拔清洁操作。"
tags: ["h2s"]
created: 2025-08-26T06:22:33.304Z
updated: 2026-03-03T07:21:16.621Z
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

## 热六角扳手疏通（适用于冷端堵塞）

> 注意：此方法只能使用 H1.5 及以下扳手。

少部分堵塞现象是耗材由于热蠕变问题而卡在热端散热片位置。这篇文章 [热蠕变](../../filament-acc/filament/heat-creep.md)详细介绍了这种现象，我们建议您阅读这篇文章，了解如何避免此类堵塞。

接下来的步骤需要拆下喷嘴。 这个wiki页面涵盖了  [H2D 喷嘴的完整拆卸和重新安装步骤](../../h2/maintenance/replace-hotend.md)，以备您随时查阅。

> 注意：**我们建议在操作过程中佩戴防护手套** 。  
> 熔化的耗材可能会滴到您的手指上，造成灼伤。

### 步骤 1. 加热六角扳手

首先**加热六角扳手**约 10 s 。用钳子牢牢夹住六角扳手，以免烫伤自己。

![](https://wiki.bambulab.com/h2/troubleshooting/clogging/heat_up_allen_key.jpg)

### 步骤2. 将六角扳手插入喷嘴入口

当扳手尖端还热的时候，快速将其推入热端，穿过散热器的顶端。

将热扳手插入耗材内部，如下图所示。然后等待约 30 s ，让六角扳手冷却。

![](https://wiki.bambulab.com/h2/troubleshooting/clogging/insert_the_hex_wrench.jpg)

### 步骤 3. 加热喷嘴尖端并拉出耗材堵塞物

六角扳手现在卡在喷嘴里了，耗材也卡在了它周围。要取出卡住喷嘴的六角扳手，你需要加热喷嘴的尖端。

首先，取下热端的硅胶套，然后使用打火机对喷嘴尖端加热约 20 s（使用普通打火机时）。

> **警告！** **避免长时间加热喷嘴或使用高功率丁烷喷灯。**  
> 建议使用普通气体打火机。
>
> 喷嘴的热侧只需足够热，以便您可以取出带有耗材的六角工具。
>
> 喷嘴过热会导致耗材从喷嘴尖端滴落或爆裂。请仔细按照说明操作，操作时请勿将喷嘴尖端朝向自己。

![](https://wiki.bambulab.com/h2/troubleshooting/clogging/heat_up_hot_end.jpg)

将喷嘴尖端加热 20 s 后，慢慢拉动扳手。你会发现耗材可以从喷嘴中完整地拔出，堵塞的部位也随之清除。

![](https://wiki.bambulab.com/h2/troubleshooting/clogging/pulled_filament.jpg)

## 冷拔完成后

流程结束后，务必将铁氟龙料管牢固插回工具头原位，以确保耗材通道密封，便于后续使用。现在，您可以重新装载耗材并进行挤出测试，以确认耗材流动顺畅。如果一切顺利，就可以发起新的打印任务了。

![image.png](https://wiki.bambulab.com/h2s/maintenance/nozzle-cold-pull-maintenance-and-cleaning/image.png)

![image8.png](https://wiki.bambulab.com/h2s/maintenance/nozzle-cold-pull-maintenance-and-cleaning/image8.png)

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
