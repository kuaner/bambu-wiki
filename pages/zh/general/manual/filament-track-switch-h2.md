---
path: zh/general/manual/filament-track-switch-h2
title: "耗材变轨器使用指南 - H2 系列"
description: "本指南涵盖耗材变轨器的详细介绍，以及 H2 系列打印机搭配耗材变轨器进行打印的具体操作步骤。"
tags: []
created: 2026-05-12T04:18:47.643Z
updated: 2026-05-22T07:07:06.934Z
source: https://wiki.bambulab.com/zh/general/manual/filament-track-switch-h2
---

本指南涵盖耗材变轨器的详细介绍，以及 H2 系列打印机搭配耗材变轨器进行打印的具体操作步骤。

## 耗材变轨器介绍

耗材变轨器专为双喷嘴打印机设计，配备 2 个进料口与 2 个出料口，可支持 AMS 与双喷嘴的任意映射。

![](https://wiki.bambulab.com/general/filament-track-switch/017.jpg)

### 适配机型

- H2C
- X2D：请参考 [X2D 耗材变轨器使用指南](filament-track-switch.md)

> 更多机型正在适配中，计划将于今年陆续支持其他 H2 系列机型，请关注固件更新获取最新适配进展。

### **优势**

以往双喷嘴打印机的 AMS 与喷嘴为固定绑定关系——每台 AMS 仅能为其连接的左或右喷嘴供料。连接单台 AMS 时，另一个喷嘴无 AMS 可用，只能通过外挂料架手动进料；连接双台 AMS 时，若目标喷嘴与耗材所在 AMS 不匹配，则需手动调整耗材位置或重新连接料管，操作繁琐且容易影响打印流程。

|  |  |
| --- | --- |
|  |  |

安装耗材变轨器后，AMS 与喷嘴之间的固定绑定将被解除。无论连接一台还是多台 AMS，所有 AMS 中的耗材均可自由进料至任意喷嘴，无需区分左右，真正实现喷嘴与 AMS 的灵活映射，大幅减少手动干预，提升多色打印效率。

|  |  |
| --- | --- |
|  |  |

## 安装与使用步骤

本文将详细介绍 H2C 打印机通过耗材变轨器连接两台 AMS 的步骤，如需使用变轨器连接三台及以上数量 AMS，可使用四进一料管拓展口（黑色），请参考以下摆放方式；在不影响正常进料的前提下，尽可能缩短料管长度，降低进料阻力。

- AMS HT 顶置方案：AMS 到变轨器的料管推荐长度不超过 700mm
- AMS HT 侧置方案：AMS 到变轨器的料管推荐长度不超过 700mm
- 变轨器（按官方摆放方式）到机身进料口的料管长度推荐 400 mm

|  |  |
| --- | --- |
|  |  |

> 注意：
>
> - 如需连接 AMS HT，**强烈建议按照图示把 AMS HT 摆放在右侧板旁**，减少进退料阻力；
> - 可从 MakerWorld 官网下载合适的 AMS 支架模型。
> - **料管拓展口只能接在变轨器和 AMS 之间，**不能接在变轨器和缓冲器之间。  
>   ![](https://wiki.bambulab.com/general/filament-track-switch-h2/009.png)

### 准备工作

#### 工具和材料

- 耗材变轨器（包装内包括耗材变轨器、6-pin 线、700mm 料管 \*2、400 mm 料管 \*2、螺丝 \*6）

> 注：包装内配有 4 颗 ST3×10 螺丝，实际安装仅需使用 2 颗，剩余 2 颗为备用件，请妥善保存。

|  |  |
| --- | --- |
|  |  |

- 额外的 6-pin 线 \* 2
- H1.5 & H2.0 内六角扳手

#### 支架打印

请根据实际需求，提前打印以下模型。**模型链接：**[耗材变轨器支架（适配H2C/H2D）](https://makerworld.com.cn/zh/models/2500588-hao-cai-bian-gui-qi-zhi-jia-gua-pei-h2c-h2d)

![](https://wiki.bambulab.com/general/filament-track-switch-h2/018.png)

| **序号** | **名称** | **用途** | **需打印数量** |
| --- | --- | --- | --- |
| 1、2、3 | AMS 固定支架 | 料管导向支架底，分别适配 AMS、AMS 2 Pro 和 AMS HT | 根据 AMS 型号及数量决定 |
| 4 | 耗材变轨器支架 | 将变轨器固定至打印机背板 | 1 |
| 5 | AMS 料管导向支架 | 有效降低料管磨损概率 | 根据 AMS 数量决定 |
| 6 | 气动接头卡扣 | 有效优化变轨器卡料问题 | 2 |

#### 固件/软件版本说明

- H2C：01.01.50.00
- Bambu Studio：2.5.3.60
- Bambu Handy：3.18.0

### 耗材变轨器安装

- 将支架带有凸起的一面对准耗材变轨器底面的孔位安装；

|  |  |
| --- | --- |
|  |  |

- 取出变轨器包装内的两颗银色螺丝（BT2\*8），使用 H1.5 内六角扳手将支架固定至耗材变轨器上；

![](https://wiki.bambulab.com/general/filament-track-switch-h2/034.png)

- 移除打印机背板的两颗螺丝；

![](https://wiki.bambulab.com/general/filament-track-switch-h2/035.png)

- 取出包装内的两颗黑色螺丝（ST3\*10），将支架对准背板螺丝孔位，使用 H2.0 内六角扳手将支架固定至打印机背板。

![](https://wiki.bambulab.com/general/filament-track-switch-h2/011.png)

- 耗材变轨器安装完成。

![](https://wiki.bambulab.com/general/filament-track-switch-h2/006.jpg)

### 料管连接

- 取出两根 400 mm 的料管，插入打印机的两个进料口；

> 注：出料口与进料口无需区分顺序，可任意连接。

![](https://wiki.bambulab.com/general/filament-track-switch-h2/012.png)

- 将料管另一端穿过气动接头卡扣，然后插入变轨器出料口；

|  |  |
| --- | --- |
|  |  |

- 将气动接头卡扣前移，靠近变轨器出料口；

![](https://wiki.bambulab.com/general/filament-track-switch-h2/015.png)

- 将料管固定支架的凹槽对准 AMS 底部插入；

![](https://wiki.bambulab.com/general/filament-track-switch-h2/004.webp)

- 将一根 700mm 左右的料管插入料管导向支架中；

![](https://wiki.bambulab.com/general/filament-track-switch-h2/001.webp)

- 将料管插入 AMS 中，将料管导向支架下移到底部对准 AMS 料管接头，往上卡紧；

![](https://wiki.bambulab.com/general/filament-track-switch-h2/002.webp)

- 调整料管导向支架角度，保证料管无大角度弯折，送料顺畅；

![](https://wiki.bambulab.com/general/filament-track-switch-h2/003.webp)

- 将料管另一端穿过气动接头卡扣，然后插入变轨器任一进料口；

|  |  |
| --- | --- |
|  |  |

- 使用另一根 700mm 左右的料管，用同样的方法安装另一台 AMS 的料管固定支架；

![](https://wiki.bambulab.com/general/filament-track-switch-h2/019.png)

- 将料管另一端穿过气动接头卡扣，然后插入耗材变轨器的另一个进料口；

![](https://wiki.bambulab.com/general/filament-track-switch-h2/020.png)

- 料管连接完成。

![](https://wiki.bambulab.com/general/filament-track-switch-h2/021.png)

### 线缆连接

- 使用一根 6-pin 线连接耗材变轨器和打印机；

![](https://wiki.bambulab.com/general/filament-track-switch-h2/022.png)

- 使用一根 6-pin 线连接一台 AMS 和耗材变轨器;

![](https://wiki.bambulab.com/general/filament-track-switch-h2/023.png)

- 使用一根 6-pin 线连接两台 AMS；

![](https://wiki.bambulab.com/general/filament-track-switch-h2/024.png)

- 连接完成。

![](https://wiki.bambulab.com/general/filament-track-switch-h2/025.png)

### AMS 初始化

点击打印机屏幕，进入“耗材”页面，点击左下角的提示，进行 AMS 初始化设置，可选择自动模式或手动模式。

|  |  |
| --- | --- |
|  |  |

- **自动模式：**AMS 将耗材送至耗材变轨器进料口，变轨器的两个进料口各对应一个档位传感器，通过传感器触发信号，设备可识别该 AMS 连接到的是哪一个进料口。

> 注意：
>
> - 每台 AMS 内均需插入一卷耗材（任意槽位即可）；
> - 已进料的耗材需提前退料。

|  |  |
| --- | --- |
|  |  |

- **手动模式：**点击 AMS 图标，可手动指定 AMS 连接的耗材变轨器进料口（A/B），再点击右上角“确认”即可完成连接。

  > 注意：当 AMS 中无耗材时，建议手动调整 AMS 与耗材变轨器的配对关系。

|  |  |
| --- | --- |
|  |  |

若 AMS 已进料至挤出机，则该 AMS 图标为灰色，并且无法修改配对关系。

![](https://wiki.bambulab.com/general/filament-track-switch-h2/030.png)

### 进料

点击需要进料的耗材，可选择进料至左喷嘴或右喷嘴。

![](https://wiki.bambulab.com/general/filament-track-switch-h2/043.png)

首次进料时，由于设备尚未识别耗材变轨器进料口与出料口的对应关系，因此会保持当前开关状态进行试进料。若**连续 3 次试进料均未进入指定喷嘴**，耗材自动退回后，设备将切换变轨器的档位开关，然后重新尝试进料。当耗材抵达指定喷嘴，则进料成功，系统会自动保存此次正确的对应关系，后续进料将直接沿用该匹配关系进行送料。

![](https://wiki.bambulab.com/general/filament-track-switch-h2/044.png)

## Bambu Studio 耗材映射

双喷嘴打印机未安装耗材变轨器时，打印任务下发后，左右喷嘴与 AMS 为固定映射绑定：左喷嘴无法选择右侧 AMS 内的耗材，右喷嘴无法选择左侧 AMS 内的耗材（如下图），未能实现喷嘴与双 AMS 耗材的自由分配匹配。在此场景下，省料模式的切片结果可能需要手动调整耗材位置；若设备处于无人值守状态，无法及时调整，则只能改用便捷模式或自定义模式切片，进而产生额外的耗材冲刷浪费。

|  |  |
| --- | --- |
|  |  |

安装耗材变轨器后，打印机将解除喷嘴与 AMS 之间的固定绑定限制，每种颜色均可选择调用两台 AMS 内的任意耗材，支持喷嘴与 AMS 耗材的自由分配和灵活映射。

![](https://wiki.bambulab.com/general/filament-track-switch-h2/033.png)

当打印机连接两台 AMS 时，系统会自动优化换料效率，将本次打印中切换最频繁的两种耗材分配至耗材变轨器的两个进料口（原理与此前将高频换料的耗材分配至不同热端对应 AMS 的逻辑一致），可大幅节省换料过程中耗材进退料的耗时。除此之外，若打印机已连接两台 AMS，但单次打印仅需使用两种耗材，Studio 会建议将这两种耗材分别装入两台 AMS 中，可进一步缩短换料的等待时间。

> 有关动态映射切片功能的详细介绍请参考：[耗材变轨器动态映射切片功能介绍](../../software/bambu-studio/filament-track-switch-dynamic-mapping.md)。

## FAQs

**Q：H2 系列打印机安装耗材变轨器时，最多可连接多少台 AMS？**

**打印机可连接的 AMS 数量和耗材变轨器安装与否无关**，因此 H2 系列打印机最多支持同时连接 4 台 AMS 2 Pro 和 8 台 AMS HT，一共 12 台合计 24 个槽，可使用四进一料管拓展口进行连接。

**Q：连接两台 AMS 时，能否使用四进一料管拓展口？**

连接**两台**AMS 时强烈不推荐使用四进一料管拓展口转接，会增加进退料的阻力，可能会影响打印稳定性。

> 注意：连接多台 AMS 时，需使用 H2C 专用料管拓展口（黑色）。

**Q：能否使用耗材变轨器连接外挂料盘？**

不可以。因为使用外挂料盘时，料盘会永久占用一条挤出通道，导致耗材变轨器无法将 AMS 中的耗材动态映射到两台挤出机。因此，如果需使用外挂料盘打印，则需断开耗材变轨器。

**Q：使用耗材变轨器打印，是否存在耗材限制？**  
部分耗材因为材料特性问题（如 PLA‑CF、PLA Glow 和 PLA Silk）受进料阻力影响较大，可能会导致进退料失败，所以尽量避免接入变轨器后使用此类耗材；如已出现异常，仍要继续打印，可进行以下尝试：

1. 手动调整异常耗材所在的 AMS 槽位；
2. 使用官方推荐的料管长度；
3. 参考官方推荐的 AMS 摆放方式进行摆放；

如果调整后，打印仍然失败，请在本次打印任务中停用耗材变轨器。

**Q: 如果耗材变轨器卡料或堵塞，应该如何处理？**

如果耗材变轨器发生卡料或堵塞，请参考[耗材变轨器拆解与排障指南](../troubleshooting/filament-track-switch.md)进行疏通。

**Q：如果耗材卡在变轨器出料口，应该如何处理？**

如果耗材卡在变轨器出料口，可尝试以下方法进行解决：

1. 重新插拔变轨器到缓冲器间的料管；
2. 安装变轨器出料口的气动接头卡扣；
3. 更换变轨器到缓冲器之间的这段料管。

**Q：使用耗材变轨器时，打印机能否进行校准？**

目前 H2C 安装耗材变轨器后，将无法执行高精度喷嘴偏移校准操作；如需执行该校准，必须先拆除变轨器，恢复设备未接入变轨器的状态，后续将通过功能更新优化解决该问题。

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
