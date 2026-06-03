---
path: zh/filament-acc/filament/print-quality/warping-falling-off-collapsing
title: "模型翘边、脱落或倒塌"
description: ""
tags: ["打印质量", "翘边", "脱落", "倒塌"]
created: 2023-12-10T05:42:42.482Z
updated: 2026-01-26T08:08:54.760Z
source: https://wiki.bambulab.com/zh/filament-acc/filament/print-quality/warping-falling-off-collapsing
---

## 模型翘边、脱落或倒塌

模型翘边、脱落或倒塌一般是由模型局部收缩、与打印板的粘接力不足导致的，且翘边后模型表面会有一条凸出横纹，因为模型翘边区域与喷嘴的距离变小，导致正在打印的这一层的挤出线被压扁而溢出。

![](https://wiki.bambulab.com/knowledge-sharing/print-quality/%E6%A8%A1%E5%9E%8B%E7%BF%98%E8%BE%B9.png)

> 相关 wiki:
>
> - [模型翘边](../../../knowledge-sharing/printed-model-warping.md)
> - [小圆片的使用技巧——防止翘曲](../../../software/bambu-studio/use-disc-to-avoid-warping.md)

## **潜在原因和解决方法**

### 1. 模型过于瘦高，重心较高，导致在打印过程中因晃动而出现脱落或倒塌的情况

- 建议开启或增加支撑；[支撑绘制](../../../software/bambu-studio/support-painting.md)

![支撑.jpg](https://wiki.bambulab.com/miniwiki/hms/h2/0c00_0300_0003_0008/%E6%94%AF%E6%92%91.jpg)

- 降低打印速度和加速度；
- 切片前更改摆放方式，尽量让模型平躺，或将模型切割后打印。

### **2. 喷嘴撞击模型**

- 如果喷嘴温度不足，在高速打印过程中，耗材熔融不充分，挤出的熔体的粘度较高，流动性较差，易造成喷嘴刮蹭模型。此种情况下，建议适当提高喷嘴温度。另外，如喷嘴或者模型局部粘了料块，也可能导致打印过程中喷嘴撞模型。此种情况下，建议适当将喷嘴清洁干净后，升高温度并降低速度来进行打印。
- 有些填充图案的走线方式在单层之内存在交叉（如网格、三角形等），所以喷嘴在打印填充时会在交叉点发生刮蹭，这通常对打印不会有太大的影响，但如果确实发生了这种情况且影响了某些模型的粘接，可以尝试降低填充速度，或把填充图案改为单层之内没有交叉点的线、直线排列、螺旋体、同心等。

![](https://wiki.bambulab.com/knowledge-sharing/print-quality/%E9%99%8D%E4%BD%8E%E5%A1%AB%E5%85%85%E6%89%93%E5%8D%B0%E9%80%9F%E5%BA%A6.png)

**降低稀疏填充打印速度**

|  |  |
| --- | --- |
| **网格填充，单层存在交叉** | **线填充，单层无交叉** |

### **3. 耗材选择与打印设置**

模型局部翘边通常是由于与热床的粘接力不足、冷却过快或局部收缩过大导致的。模型尺寸越大，收缩风险越高；填充率越高，收缩可能性也越大。ABS、ASA、PC、POM、PP、PA 和 PA-CF 等材料更容易发生收缩。因此，建议在进行大尺寸打印时尽量避免使用这些材料。相反，建议选择不易翘曲的耗材，如 PLA、PLA-CF、PETG、PETG-CF 和 PET-CF 等

- 床温温度偏低，导致模型与热床的粘接力不足——适当提高热床温度。

![热床温度.jpg](https://wiki.bambulab.com/miniwiki/hms/h2/0c00_0300_0003_0008/%E7%83%AD%E5%BA%8A%E6%B8%A9%E5%BA%A6.jpg)

- 腔温偏低、风扇转速过高，导致模型冷却过快——适当提高热床温度，并关闭打印机的前门、盖上顶盖，适当调小风扇转速。

![封闭仓门.jpg](https://wiki.bambulab.com/miniwiki/hms/h2/0c00_0300_0003_0008/%E5%B0%81%E9%97%AD%E4%BB%93%E9%97%A8.jpg)

- 模型尺寸较大且填充率过高——如果模型尺寸较大且填充率设置得较高，如 60%（默认值是 15%），发生了翘边，可适当调低。另外，填充图案带有较多直线的更容易收缩，可以把填充图案改成螺旋体来降低收缩风险。对于部分对强度要求较高的结构件，可以设置 5 层墙和 25% 左右的填充率，尽量避免使用 50% 以上的填充率，以降低收缩趋势；对于大多数对强度要求较低的非结构件，则可以直接选择默认的 2 层墙和 15% 的填充率。

![填充与填充图案.jpeg](https://wiki.bambulab.com/knowledge-sharing/print-quality/%E5%A1%AB%E5%85%85%E4%B8%8E%E5%A1%AB%E5%85%85%E5%9B%BE%E6%A1%88.jpeg)  
![](https://wiki.bambulab.com/knowledge-sharing/print-quality/%E8%9E%BA%E6%97%8B%E4%BD%93%E5%A1%AB%E5%85%85.png)

**螺旋体填充**

### **4. 模型与打印板的粘接力不足**

- 打印使用的打印板和切片软件中选择的“打印板类型”不一致——同一种材料通常可以在不同的热床打印板使用不同的热床温度进行打印，如果选错热床类型，则有可能因为打印的热床温度不足而导致粘接力不足。另外，PEI 纹理板由于表面有颗粒物，所以在热床调平后，打印机会下压喷嘴 0.04mm 确保首层粘接。如果您使用PEI板打印却在切片时选择其他的“热床类型”，则会导致喷嘴高度过高，影响首层粘接。
- 首层调平不当——先清洁打印板和喷嘴，再重新打印。详情请参考：[纹理 PEI 板清理指南](../../acc/pei-plate-clean-guide.md)。
- 打印板脏污或破损——清洗打印板（用清水和洗涤剂即可），或更换新贴膜或打印板。详情请参考：[纹理 PEI 板清理指南](../../acc/pei-plate-clean-guide.md)。
- Brim 不足——启用 Brim 、调大其宽度。注意：减少 birm 和模型的间隙也有改善效果，但打印后需要修剪 birm 的难度会增⼤。

![开启brim.jpg](https://wiki.bambulab.com/miniwiki/hms/h2/0c00_0300_0003_0008/%E5%BC%80%E5%90%AFbrim.jpg)

- 未正确涂胶——在打印板表面均匀涂胶。详情请参考：[如何使用 Bambu Lab 胶水](../../../general/how-to-use-bbl-liquid-glue.md)。
- 热床温度偏低——适当调高热床温度。

## **结束语**

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南并未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/cn/im)，我们随时准备为您解答疑问并提供帮助。
>
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
