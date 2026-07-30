---
path: zh/filament/petg
title: "PETG 使用指南"
description: ""
tags: ["耗材"]
created: 2025-10-09T09:07:39.753Z
updated: 2026-07-23T03:23:22.097Z
source: https://wiki.bambulab.com/zh/filament/petg
---

> 📌 **耗材使用注意事项**：
>
> 1. 请在**阴凉、避光、干燥**环境中存放耗材，避免阳光直射或高温环境。
> 2. 请将耗材及折断的碎屑放在**婴幼儿及宠物无法触及的地方**，避免吞咽和窒息的风险。
> 3. PETG 属于**吸水性较强**的材料，未使用完的耗材应立即放入含有有效干燥剂的**密封容器**内，并且在打印前按照指南中推荐的温度和时间进行**充分烘干**。
> 4. 建议在**通风良好**的区域使用打印机，或安装有效的空气过滤、外排风系统。
> 5. PETG 耗材**不属于**食品接触级耗材，请避免将打印成品用于存放或接触食品。
> 6. **PETG-CF** 耗材表面及端口处可能带有肉眼不可见的硬质微刺，在处理该类耗材线、拆除支撑或者打磨打印件时，建议佩戴防刺防割**手套**并佩戴**护目镜**。

## 1.耗材基本信息

### 耗材介绍

PETG 相较于 PLA 有更好的韧性，具备接近 PLA 的简便打印体验；同时又避免了 ABS 材料常见的翘曲与异味。

> 名词解释：**“翘曲”**（warpage）一词，在 3D 打印语境下，通常指的是零件脱模或冷却后发生的形状变形 / 面外（out-of-plane）位移，即原本应该平直或按设计轮廓的部分因为热收缩或残余应力而弯曲、翘起或扭曲。

下图为 **Bambu PETG-CF** 的实际运用案例：

![petg_cf.png](https://wiki.bambulab.com/filament-acc/petg/petg_cf.png)

- 更多的相关资讯可以参考天猫商品详情页：[PETG](https://detail.tmall.com/item.htm?abbucket=9&id=816799102364&pisk=gmExo6Dus_f0s8A2H5bkIEa2sQXu6a2qPSyBjfcD57F8653cQxViXVh8dqX4s54-67N-GobqshdTNRvmlqM1V4MIBIMshVaJBJP86VWqsfGTsRacEMj33-oZfcChxMmFAKFLMEMshOTSLAWohSh8bTmZf6f9rhgVvcPjF1cccUMSaAH61ENsN0MENAtj55GSPvM6cci_1ThSBvtjhxGfVUMmNCMjCns5VADsCnMs1TeSaAhsfcNsVTHZNfisfbOF6b9jshUAh5p27GOW7Fr-Hqh9jbKT4oKnuXTtahKtwvuYo-GJfhZ8rKifVj_eEfomg8HY_M-qcVU_m0ZfNGiQ87EtRDQG3qwTy5o0VOTjOrVmVoapChw-DrgZH2dAwXZ4FkoSrM6LFuP03ueMCGMutbw4ccICLmnjG0Hzj_-j6za_mqowG1ha28ZbWgyUxkHOXBcKIE6ReF8ZlYJejEBLish3iYhhHGLw74WyjEEwuFT61kD-ttBH7Fu2B&rn=4e7dc14c46e4815a2b4c882c59822636&spm=a1z10.5-b-s.w4011-25176969463.73.31dc6b8eLy91Fo)
- 海外官方商品详情页：[PETG](https://asia.store.bambulab.com/products/petg-hf)

### 硬件兼容性

PETG 适配拓竹全系机型，更多的硬件兼容性内容可参考下表：

| 材料 | 喷嘴兼容性 | 打印板兼容性 | 配件兼容性 |
| --- | --- | --- | --- |
| PETG Basic / PETG HF | 兼容全部常规喷嘴（无特别限制） | 兼容全部打印板 | AMS 系列全兼容 |
| PETG CF | 兼容于硬化钢喷嘴；不建议使用 0.4 mm 高流量喷嘴 | 兼容全部打印板 | AMS lite 不兼容 |
| PETG Translucent | 兼容常规喷嘴（不含 0.2 mm） | 兼容全部打印板 | AMS 系列全兼容 |
| PETG Matte | 兼容全部常规喷嘴（无特别限制） | 纹理 PEI 打印板 / 光面 PEI 打印板 / 增稳低温打印板 | AMS 系列全兼容 |

## 2.打印准备

> **❗ 重要提示**：**PETG-CF** 为碳纤增强耗材，在其使用、后处理、或接触其打印件的粗糙/断裂表面过程中，可能产生细小的纤维碎屑，存在皮肤机械性刺伤、皮肤过敏或异物刺激等风险。因此，**请避免裸手直接触摸或摩擦**粗糙边缘或断面。建议在装卸耗材、剪切打磨及其他后处理操作时**佩戴防护手套**，并根据实际需要佩戴其他防护用具。

### 烘干耗材

PETG 暴露在空气中存放时（湿度50%-60%）会逐渐吸收环境中的水分。环境的相对湿度越高、存放时间越长，材料吸收的水分就越多。如果模型拉丝明显，如下面右图所示，则说明耗材受潮，需要烘干。 对于 PETG-HF 耗材，可以打印测试模型来判断耗材是否受潮：

![8.png](https://wiki.bambulab.com/filament-acc/beginner/8.png)

为保障打印质量，建议打印前对 PETG 耗材进行充分烘干，避免因受潮导致拉丝、气泡等问题，具体烘干参数如下：

| 材料 | **鼓风式烤箱** | **热床** | **AMS HT / AMS 2 Pro** |
| --- | --- | --- | --- |
| **PETG Basic / PETG HF / PETG CF / PETG Translucent / PETG Matte** | 60 - 65 °C，8 h | 80 °C，12 h | 65 °C，8 h |

> **注意：**
>
> 使用热床进行耗材烘干时需注意：
>
> - X1、H2系列和 P2S 打印机可在屏幕上选择**使用“烘干耗材”功能**，如 **H2 系列**具体设置位置为： “设置” → 选择 “工具箱” → 工具“烘干耗材”。不同的打印机位置略有不同。
> - 请**每隔 6 小时**将耗材**翻面**一次，并在耗材上方覆盖耗材包装盒或 PC 盒。

### 未烘干 PETG HF 的打印建议

在未具备烘干条件的情况下，若直接使用 **Bambu Studio 默认的 Bambu PETG HF 打印参数**，容易出现明显的**拉丝、漏料、气泡**等问题。建议按以下方式调整参数：

- **优先使用 Generic PETG HF 参数**（喷嘴温度 220 ℃，体积速度 16 mm³/s），该方案整体打印速度低于默认的 Bambu PETG HF 参数，可显著改善打印稳定性（具体参数对比可以看下图）。
- 若打印质量仍不理想，可进一步**降低打印速度**，避免使用 Bambu PETG HF 默认参数，以减少堵头或挤出异常的风险。
- 打印效果会随耗材湿度变化而波动，若出现明显拉丝或表面瑕疵，请**烘干耗材**或**再次降低打印速度**后重试。

|  |  |
| --- | --- |
| Generic PETG HF 参数 | Bambu PETG HF 参数 |

## 3.常见打印问题与解决方案

PETG 耗材因吸水性较强，打印时易出现**粘嘴**与**拉丝**两类问题，同时可能伴随表面质量不佳、翘边等情况，具体解决方案如下：

### 耗材粘嘴

粘嘴是指打印开始一段时间后，挤出的耗材熔体中少部分粘附在喷嘴上，导致打印件出现局部缺料、粗糙等缺陷。这种情况一般出现在 PETG 类耗材中，特别是 **PETG-CF**，下图展示了典型的粘嘴现象。为解决这一问题，您先可以佩戴好隔热手套，然后通过加热喷嘴，等耗材充分融化后，小心地将粘附的耗材移除。

> **重要提醒 ！**  
> 1.在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，**请佩戴好隔热手套**，以确保安全有效地执行维护工作。  
> 2.如果您对本操作有任何疑问，请[点击这里登录账号并提交工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)，我们将及时回复并为您提供所需的帮助。

![](https://wiki.bambulab.com/filament-acc/petg/image.png)

#### 适当降低流量比例与打印温度

**降低流量比例**

PETG 类耗材的推荐流量比例范围为 0.93 – 0.96。

- 低于 0.93：可能造成缺料，并减弱层间结合强度。
- 高于 0.96：可提高层间强度，但易引发漏料或粘嘴。

Bambu PETG Basic 与 Bambu PETG-CF 的默认流量比例为 0.95，不建议调高该值。若使用充分干燥的线材打印时出现粘嘴，可尝试将流量比例略微调低至 0.93 – 0.94。

![cyeabtje0ozwwjxsdbacfjsbnin.jpg](https://wiki.bambulab.com/filament-acc/petg/cyeabtje0ozwwjxsdbacfjsbnin.jpg)

**适当降低打印温度**

当打印速度较高时，喷嘴在短时间内需要熔化更多材料，此时应适当**提高喷嘴温度**，以避免因加热不足造成模型缺料或断层。  
相反，当**降低打印速度**或**减小最大体积流速**时，应同步**降低喷嘴温度**。打印速度变慢会使材料受热更充分、流动性增强，若温度过高，容易出现拉丝、漏料或喷嘴粘料等问题。

![qta6bfs7pox7x7x9emzcyvkdnxd.jpg](https://wiki.bambulab.com/filament-acc/petg/qta6bfs7pox7x7x9emzcyvkdnxd.jpg)

#### 适当减小线宽

线宽决定了挤出路径的宽度，直接影响打印质量和模型强度。通常使用 0.4 mm 喷嘴时，默认内墙线宽为 0.45 mm，外墙为 0.42 mm。略大于喷嘴直径的线宽可使相邻路径轻微重叠，有助于提高部件强度，但由于需要使用喷嘴的熨平环来扩大线宽，会有少许的耗材沾附在喷嘴上。

若对模型强度要求不高，可适当减小线宽，建议设置在 0.36 mm - 0.40 mm 之间，以改善粘嘴情况。

> 注意：线宽的调整，建议保持在喷嘴直径的 0.75 - 1.5 倍范围内。

![](https://wiki.bambulab.com/filament-acc/petg/setting1.jpg)

### 模型表面质量不佳

#### 表面出现拉丝、气泡

在打印受潮的 PETG 耗材时，这些水汽在温度很高的喷嘴中受热后会迅速汽化，从而使耗材熔体膨胀、流动更快并产生气孔，进而使打印件出现拉丝、漏料、孔洞、表面粗糙、强度低等问题。

![image-22.png](https://wiki.bambulab.com/filament-acc/petg/image-22.png)

上述图片中的情况一般是 PETG 耗材吸水受潮而导致的，需要重新烘干耗材，具体操作可以参考本文中的[《耗材干燥》](https://wiki.bambulab.com/zh/filament/petg#%E7%83%98%E5%B9%B2%E8%80%97%E6%9D%90)章节。

#### 表面局部缺料

当外墙打印从低流速切换至高流速（例如模型悬空进行架桥时流速降低，打印完架桥之后流速增加），可能出现异常的凸起或者缺料凹陷。

为了避免速度突变而造成表面缺料（如下图），可以参考以下调节方案进行修改。

![](https://wiki.bambulab.com/filament-acc/petg/image-6.png)

- 降低打印速度：在低速打印时，挤出相较稳定，建议将打印速度控制在 90 mm/s。

![](https://wiki.bambulab.com/filament-acc/petg/image-24.png)

- 降低平滑系数：将平滑系数调至 0.1 可将速度变化的量变得更加平缓。

![](https://wiki.bambulab.com/filament-acc/petg/image-3.png)

### 模型翘边

PETG 比 PLA 更容易出现翘边。大多数情况下，由于打印层冷却过快，使得层间产生应力，最终导致翘边。

您可以参考下面这个方案避免打印时出现翘边的情况。

#### 增加打印板和模型粘附

- 增加打印板的粘附：涂抹胶水或固体胶（如下左图）
- 开启裙边：增大模型与打印板接触面积（如下右图）

![image-23.png](https://wiki.bambulab.com/filament-acc/petg/image-23.png)

### 优化悬垂质量

为了获得高质量的 PETG 悬垂打印效果，需要特别注意切片设置。其中一个关键点是，避免将打印接缝设置在悬垂区域，否则会显著影响该处的表面质量，如下图箭头所示。

![接缝6.png](https://wiki.bambulab.com/filament-acc/petg/%E6%8E%A5%E7%BC%9D6.png)

为解决该问题，可以调整接缝位置或者开启**接缝远离悬垂点放置**选项。（如下图所示）

![接缝3.png](https://wiki.bambulab.com/filament-acc/petg/%E6%8E%A5%E7%BC%9D3.png)

## 4.进阶学习

### 优化模型表面质量

在盒子类模型的大底面与薄壁交界处，或小船模型的腰部区域，外壁表面可能出现异常的环形凸起纹路，这类现象我们通常统称为变截面类层纹。若想要彻底解决此类问题，最推荐的做法是直接为模型添加一个内侧圆角。

![image-29.png](https://wiki.bambulab.com/filament-acc/pla/image-29.png)

> 注意：加内侧圆角需要在其他建模软件如 **Fusion 360 / SolidWorks** 中操作。

- 模型增加内侧圆角后，切片后桥接将不再与内墙接触。

![](https://wiki.bambulab.com/filament-acc/petg/image-19.png)

- 在增加了**模型增加内侧斜角**后，对模型进行切片后可观察打印轨迹，桥接几乎不与内墙接触。

> 名词解释：
>
> - 在 3D 打印 中，打印头会一层层地挤出融化的塑料丝。如果某一层的部分区域 没有下面的支撑结构，而喷嘴又要在空中跨越这段“悬空的间隙”进行打印，这段横跨空隙的部分就叫：桥接（Bridge）。
> - **桥接 = 打印机在“空中”跨越两个点之间打印一条或多条丝线，就像搭一座桥一样。**

![](https://wiki.bambulab.com/filament-acc/petg/output.gif)

> 如遇到的打印问题非以上几点，可以进入该链接中根据图片展示的现象对应处理：[打印质量与解决办法](../filament-acc/filament/print-quality.md)

### 提高模型强度

1. **改变墙层数以及稀疏填充密度**

我们可以通过改变墙层数以及稀疏填充密度来改善模型的强度。推荐墙层数不大于 6 层，填充密度不大于 50%，并选择**螺旋体**为稀疏填充图案；具体参数需要**根据实际情况减小调节幅度**，否则可能会有**翘边**的风险。

> 注意：提高墙层数以及稀疏填充密度后会增大耗材冷却收缩的翘边风险，建议在有强度打印需求时在打印板表面[涂胶](../general/how-to-use-bbl-liquid-glue.md)打印或在 Bambu Studio 中增加 Brim 裙边。

![](https://wiki.bambulab.com/filament-acc/petg/image-16.png)

2. **确定模型的受力方向**

在打印前，建议您先考虑模型在实际使用中的主要受力方向。然后可以根据这一方向来调整打印时的摆放角度，建议受力方向与耗材挤出平面呈 90 度的夹角，这样能够显著提升打印成品的强度和耐用性。

> 提示：您可以参考下方示意图，对比不同摆放方式，从而判断当前的打印摆放方式是否已经接近模型最佳的受力方案。
>
> ![](https://wiki.bambulab.com/filament-acc/petg/image-15.png)
>
> ![](https://wiki.bambulab.com/filament-acc/petg/image-18.png)

### 提升透明耗材的透明度

为了让 PETG Transparent 呈现出更好的透明效果，其核心在于减少材料内部的光散射和表面瑕疵。您可以下载下面的预设 .3MF 文件并替换成你想的打印模型（用其他打印机机型打印时，可迁移下述 X1C 的相应的工艺参数和耗材丝参数）：

1. X1C，0.4 mm 喷嘴：[petg\_-\_transparent\_parameters\_-\_0.4\_mm\_nozzle.3mf](https://wiki.bambulab.com/filament-acc/filament/petg_-_transparent_parameters_-_0.4_mm_nozzle.3mf)
2. X1C，0.6 mm 喷嘴：[petg\_-\_transparent\_parameters\_-\_0.6\_mm\_nozzle.3mf](https://wiki.bambulab.com/filament-acc/filament/petg_-_transparent_parameters_-_0.6_mm_nozzle.3mf)
3. X1C，0.8 mm 喷嘴：[petg\_-\_transparent\_parameters\_-\_0.8\_mm\_nozzle.3mf](https://wiki.bambulab.com/filament-acc/filament/petg_-_transparent_parameters_-_0.8_mm_nozzle.3mf)

详细的操作流程与参数设置请参考下面的步骤：

**推荐操作**

- 烘干耗材：打印前请务必充分烘干材料。这一步能有效避免因水汽而产生的挤出气泡和孔洞，是实现均匀透光的基础。
- 选用 0.8 mm 喷嘴：我们推荐使用更大尺寸的喷嘴。它可以减少模型表面的打印线条数量，从而显著淡化层纹，提升整体透光表现。

**优化打印设置**

- 降低打印速度：在低速打印时，挤出相较稳定，建议将打印速度控制在 20 mm/s。

![](https://wiki.bambulab.com/filament-acc/petg/image-14.png)

- 调整填充与壳层：将顶部与底部壳层数设置为 0，并选择**直线**填充图案。此举可确保光路方向一致，最大程度减少内部折射与重叠。

![](https://wiki.bambulab.com/filament-acc/petg/image-17.png)

- 提高打印温度并提高流量比例：适当提升打印温度，可使材料熔融更充分、挤出更均匀，增强层间结合力。适度提高流量比例，有助于彻底填满打印线条间的微小缝隙，减少光线散射。（请注意：此操作需在耗材完全干燥的前提下进行）

![](https://wiki.bambulab.com/filament-acc/petg/image-13.png)

- 关闭冷却风扇：打印时请关闭所有风扇，让挤出材料自然缓慢冷却。这样可以有效减少因冷却不均带来的内部应力与雾化现象。

![](https://wiki.bambulab.com/filament-acc/petg/image-12.png)

不同的墙层数有一定的区别，可以参考下图的打印效果进行调节。

![](https://wiki.bambulab.com/filament-acc/petg/image-11.png)

> 温馨提示：
>
> 如果以上的进阶调整无法满足您的需求，推荐您可以进入到“拓竹学院”——“[Bambu Studio](https://bambulab.cn/zh-cn/support/academy)”中进行学习，这是一个官方 3D 打印学习平台，致力于为用户提供从基础到进阶的全方位 3D 打印知识培训，助力用户在 3D 打印领域不断提升技能，实现创新与发展。

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
