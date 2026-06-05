---
path: zh/general/manual/filament-track-switch
title: "X2D 耗材变轨器使用指南"
description: "本指南涵盖耗材变轨器的详细介绍，以及 X2D 搭配耗材变轨器进行打印的具体操作步骤。"
tags: []
created: 2026-03-16T02:50:15.541Z
updated: 2026-06-04T07:48:34.081Z
source: https://wiki.bambulab.com/zh/general/manual/filament-track-switch
---

本指南涵盖耗材变轨器的详细介绍，以及 X2D 打印机加装耗材变轨器的具体步骤。

## 耗材变轨器介绍

耗材变轨器专为双喷嘴打印机设计，配备 2 个进料口与 2 个出料口，可支持 AMS 与双喷嘴的任意映射。

![](https://wiki.bambulab.com/general/filament-track-switch/017.jpg)

### 适配机型

- H2C：请参考 [H2 系列耗材变轨器使用指南](filament-track-switch-h2.md)

- X2D

> 更多机型正在适配中，计划将于今年陆续支持其他 H2 系列机型，请关注固件更新获取最新适配进展。

### 优势

以往双喷嘴打印机的 AMS 与喷嘴为固定绑定关系——每台 AMS 仅能为其连接的左或右喷嘴供料。连接单台 AMS 时，另一个喷嘴无 AMS 可用，只能通过外挂料架手动进料；连接双台 AMS 时，若目标喷嘴与耗材所在 AMS 不匹配，则需手动调整耗材位置或重新连接料管，操作繁琐且容易影响打印流程。

|  |  |
| --- | --- |
|  |  |

安装耗材变轨器后，AMS 与喷嘴之间的固定绑定将被解除。无论连接一台还是多台 AMS，所有 AMS 中的耗材均可自由进料至任意喷嘴，无需区分左右，真正实现喷嘴与 AMS 的灵活映射，大幅减少手动干预，提升多色打印效率。

|  |  |
| --- | --- |
|  |  |

## 视频教程

## 安装与使用步骤

本部分将详细介绍 X2D 如何加装耗材变轨器并连接两台 AMS 2 Pro，如需使用变轨器连接三台及以上数量 AMS，可使用四进一料管拓展口，请参考下图进行摆放。**在不影响正常进料的前提下，尽可能缩短料管长度，可有效降低进料阻力**。

料管长度推荐：

- AMS 到变轨器：不超过 700mm
- 变轨器到缓冲器：不超过 115mm

![](https://wiki.bambulab.com/general/filament-track-switch/077.png)

> 注意：H2C 专用四进一料管拓展口（黑色）不适用于 X2D，请勿使用！

### 准备工作

#### 工具和材料准备

- 耗材变轨器（包装清单：耗材变轨器、6-pin 线、700mm 料管 \*2、400 mm 料管 \*2、螺丝 \*6）

|  |  |
| --- | --- |
|  |  |

> 注：包装内共含有 4 颗 ST3×10 螺丝，实际安装仅需 2 颗，剩余 2 颗作为备用，请妥善保管。

- 额外的 6-pin 线 \* 2
- H1.5 & H2.0 内六角扳手

#### 支架打印

**模型链接：**[耗材变轨器支架（适配X2D）](https://makerworld.com.cn/zh/models/2383488-hao-cai-bian-gui-qi-zhi-jia-gua-pei-x2d#profileId-2706018)

![](https://wiki.bambulab.com/general/filament-track-switch/033.png)

| **序号** | **名称** | **用途** | **需打印数量** |
| --- | --- | --- | --- |
| 1、2、3 | AMS 固定支架 | 料管导向支架底，分别适配 AMS、AMS 2 Pro 和 AMS HT | 根据 AMS 型号及数量决定 |
| 4 | 耗材变轨器支架 | 将变轨器固定至打印机背板 | 1 |
| 5 | AMS 料管导向支架 | 有效降低料管磨损概率 | 根据 AMS 数量决定 |
| 6 | 气动接头卡扣 | 有效优化变轨器卡料问题 | 2 |

> 注意：打印机如需打印高温耗材，建议使用**耐高温材质**（如 PC、耐高温 CF-GF）打印支架，避免在后续的打印任务中，设备温度过高导致模型变形。

#### 固件/Bambu Studio 版本

- X2D：01.01.00.00 及以上
- Bambu Studio：2.5.3 及以上

### 安装耗材变轨器

- 使用 H2.0 内六角扳手移除打印机背板的两颗螺丝；

![](https://wiki.bambulab.com/general/filament-track-switch/044.png)

- 截取两段 115mm 左右的料管；

![](https://wiki.bambulab.com/general/filament-track-switch/055.png)

- 将两根料管的一端插入缓冲器；

![](https://wiki.bambulab.com/general/filament-track-switch/066.png)

另一端穿过气动接头卡扣，需注意卡扣方向；

|  |  |
| --- | --- |
|  |  |

然后将料管插入耗材变轨器出料口；

> 注：出料口与进料口无需区分顺序，可任意连接。

![](https://wiki.bambulab.com/general/filament-track-switch/027.png)

并将卡扣前移，贴紧出料口；

![](https://wiki.bambulab.com/general/filament-track-switch/004.webp)

- 将变轨器背面的螺丝孔位对准支架孔位；

|  |  |
| --- | --- |
|  |  |

- 取出变轨器包装内的两颗银色螺丝（BT2\*8），使用 H1.5 内六角扳手**轻锁**螺丝，**无需完全拧紧，确保变轨器和支架间有一定的活动余量；**

|  |  |
| --- | --- |
|  |  |

- 取出包装内两颗黑色螺丝（ST3\*10），将支架对准背板螺丝孔位，使用 H2.0 内六角扳手将支架固定至背板；

![](https://wiki.bambulab.com/general/filament-track-switch/028.png)

- 使用 H1.5 内六角扳手拧紧耗材变轨器与支架间的螺丝。

![](https://wiki.bambulab.com/general/filament-track-switch/029.png)

### AMS 料管连接

- 将料管固定支架的凹槽对准 AMS 底部插入；

|  |  |
| --- | --- |
|  |  |

- 取出包装袋中 700mm 的料管，将其捋直；

![](https://wiki.bambulab.com/general/filament-track-switch/010.webp)

- 将料管插入料管导向支架中；

![](https://wiki.bambulab.com/general/filament-track-switch/019.png)

- 将料管插入 AMS 中；

![](https://wiki.bambulab.com/general/filament-track-switch/021.png)

- 将料管导向支架下移到底部，对准支架卡扣，往上卡紧；

![](https://wiki.bambulab.com/general/filament-track-switch/012.webp)

- 调整料管导向支架角度，保证料管无大角度弯折，送料顺畅；

![](https://wiki.bambulab.com/general/filament-track-switch/014.webp)

- 用同样的方法安装另一台 AMS 的料管固定支架，并插入包装内 400mm 的料管；

![](https://wiki.bambulab.com/general/filament-track-switch/034.png)

> AMS HT 安装料管固定支架示意图：  
> ![](https://wiki.bambulab.com/general/filament-track-switch/048.png)

- 将两台 AMS 的料管穿过气动接头卡扣；

![](https://wiki.bambulab.com/general/filament-track-switch/035.png)

然后插入变轨器进料口，并将卡扣前移，贴紧进料口。

![](https://wiki.bambulab.com/general/filament-track-switch/036.png)

- 料管连接完成。

![](https://wiki.bambulab.com/general/filament-track-switch/037.png)

### AMS 线缆连接

- 使用一根 6-pin 线连接一台 AMS 和缓冲器;

![cable-1.jpg](https://wiki.bambulab.com/general/filament-track-switch/cable-1.jpg)

- 使用一根 6-pin 线连接该台 AMS 和耗材变轨器；

![cable-1.jpg](https://wiki.bambulab.com/general/filament-track-switch/cable-2.jpg)

- 使用一根 6-pin 线连接耗材变轨器和另一台 AMS；

![cable-1.jpg](https://wiki.bambulab.com/general/filament-track-switch/cable-3.jpg)

- 如果线缆较长，可适当整理线缆。

![](https://wiki.bambulab.com/general/filament-track-switch/041.png)

### AMS 初始化

点击打印机屏幕，进入“耗材”页面，点击左下角的提示，进行 AMS 初始化设置，可选择“自动模式”或“手动模式”。

|  |  |
| --- | --- |
|  |  |

- **自动模式：**AMS 将耗材送至耗材变轨器进料口，变轨器的两个进料口各对应一个档位传感器，通过传感器触发信号，设备可识别该 AMS 连接到的是哪一个进料口。

> 注意：
>
> - 每台 AMS 内均需插入一卷耗材（任意槽位即可）；
> - 已进料的耗材需提前退料。

![](https://wiki.bambulab.com/general/filament-track-switch/042.png)

- **手动模式：**点击 AMS 图标，可手动指定 AMS 连接的耗材变轨器进料口（A/B），再点击右上角“确认”即可完成连接。

  > 注意：当 AMS 中无耗材时，建议手动调整 AMS 与耗材变轨器的配对关系。

![](https://wiki.bambulab.com/general/filament-track-switch/043.png)

若 AMS 已进料至挤出机，则该 AMS 图标为灰色，并且无法修改配对关系。

![](https://wiki.bambulab.com/general/filament-track-switch/045.png)

### 进料

点击需要进料的耗材，可选择进料至主喷嘴（左边）或辅助喷嘴（右边）。

![](https://wiki.bambulab.com/general/filament-track-switch/107.png)

首次进料时，由于设备尚未识别耗材变轨器进料口与出料口的对应关系，因此会保持当前开关状态进行试进料。若**连续 3 次试进料均未进入指定喷嘴**，耗材自动退回后，设备将切换变轨器的档位开关，然后重新尝试进料。当耗材抵达指定喷嘴，则进料成功，系统会自动保存此次正确的对应关系，后续进料将直接沿用该匹配关系进行送料。

![](https://wiki.bambulab.com/general/filament-track-switch/108.png)

## Bambu Studio 耗材映射

双喷嘴打印机未安装耗材变轨器时，打印任务下发后，主/辅助喷嘴与 AMS 为固定映射绑定：主喷嘴无法选择连接至辅助喷嘴 AMS 内的耗材，辅助喷嘴无法选择连接至主喷嘴 AMS 内的耗材（如下图），未能实现喷嘴与双 AMS 耗材的自由分配匹配。

在此场景下，省料模式的切片结果可能需要手动调整耗材位置；若设备处于无人值守状态，无法及时调整，则只能改用便捷模式或自定义模式切片，进而产生额外的耗材冲刷浪费。

![](https://wiki.bambulab.com/general/filament-track-switch/056.png)

安装耗材变轨器后，打印机将解除喷嘴与 AMS 之间的固定绑定限制，每种颜色均可选择调用两台 AMS 内的任意耗材，支持喷嘴与 AMS 耗材的自由分配和灵活映射。

![](https://wiki.bambulab.com/general/filament-track-switch/054.png)

> 有关动态映射切片功能的详细介绍请参考：[耗材变轨器动态映射切片功能介绍](../../software/bambu-studio/filament-track-switch-dynamic-mapping.md)。

## **工作原理**

耗材变轨器主体配备 **2 个进料口（In-A、In-B）**与 **2 个出料口（Out-A、Out-B）**，每个进料口对应 1 个独立的档位传感器，内部集成电磁铁驱动的路径切换部件。

基于双进料口 + 双出料口的结构设计，变轨器支持进料口与出料口的自由组合，共可实现 4 种送料路径：

1. In-A → Out-A
2. In-A → Out-B
3. In-B → Out-A
4. In-B → Out-B

![](https://wiki.bambulab.com/general/filament-track-switch/002.jpg)

耗材变轨器的两个进料口各对应一个独立的档位传感器，当耗材插入变轨器进料口后，档位传感器被触发并发送信号，设备即可精准识别当前 AMS 所接入的进料口。

![](https://wiki.bambulab.com/general/filament-track-switch/049.png)

当需要切换送料路径时，**档位传感器（#1）**通过铜线传输路径切换信号，驱动内部**电磁铁组件（#2）**拨动**变轨装置磁铁（#3）**。

![](https://wiki.bambulab.com/general/filament-track-switch/050.png)

变轨装置磁铁背面为导向指针，可引导耗材进入对应送料通道，从而完成送料链路的切换。

![](https://wiki.bambulab.com/general/filament-track-switch/099.webp)

下图以 In-A → Out-A 和 In-A → Out-B 路径为例，展示变轨装置磁铁在不同位置时对应的送料路径变化。

|  |  |
| --- | --- |
|  |  |

## FAQs

#### **Q：X2D 打印机安装耗材变轨器时，最多可连接多少台 AMS？**

**打印机可连接的 AMS 数量和耗材变轨器安装与否无关**，因此 X2D 打印机最多支持同时连接 4 台 AMS 2 Pro 和 8 台 AMS HT，一共 12 台合计 24 个槽，可使用四进一料管拓展口进行连接。

#### **Q：连接多台 AMS 时，能否使用四进一料管拓展口？**

- 连接**两台** AMS 时，可直接将 AMS 分别连接耗材变轨器的两个进料口，**不推荐使用四进一料管拓展口转接**，会增加进退料的阻力，可能会影响打印稳定性;
- 连接的 AMS 数量大于两台时，**则需使用四进一料管拓展口（白色）** 进行转接。

![](https://public-cdn.bblmw.com/wiki/new/a2l/manual/a2l-ams-connection-guide/048.png)

> 注意：H2C 专用料管拓展口（黑色）不适用于 X2D，请勿使用！

#### **Q：连接一台 AMS 时，能否实现双喷嘴打印？**

安装耗材变轨器后，双喷嘴打印机连接单台 AMS 时也可实现双喷嘴打印，并支持耗材在左右热端之间切换。**但左右热端仅支持交替供料，不支持同步供料**。在切换过程中，AMS 会先执行退料，再重新进料。  
如需在双喷嘴打印机上连接变轨器与一台 AMS，只需将 AMS 接入变轨器的任一进料口，再将变轨器的两个出料口分别与打印机的两个进料口相连。

#### **Q：能否使用耗材变轨器连接外挂料盘？**

不可以。因为使用外挂料盘时，料盘会永久占用一条挤出通道，导致耗材变轨器无法将 AMS 中的耗材动态映射到两台挤出机。因此，如果需使用外挂料盘打印，则需断开耗材变轨器。

#### **Q：使用耗材变轨器打印，是否存在耗材限制？**

部分耗材因为材料特性问题（如 PLA‑CF 和 PLA Glow）受进料阻力影响较大，可能会导致进退料失败，所以尽量避免接入变轨器后使用此类耗材；如已出现异常，仍要继续打印，可进行以下尝试：

1. 手动调整异常耗材所在的 AMS 槽位；
2. 使用官方推荐的料管长度；
3. 参考官方推荐的 AMS 摆放方式进行摆放；

如果调整后，打印仍然失败，请在本次打印任务中停用耗材变轨器。

#### **Q: 如果耗材变轨器卡料或堵塞，应该如何处理？**

如果耗材变轨器发生卡料或堵塞，请参考[耗材变轨器拆解与排障指南](../troubleshooting/filament-track-switch.md)进行疏通。

#### **Q：如果耗材卡在变轨器出料口，应该如何处理？**

1. 重新插拔变轨器到缓冲器间的料管；
2. 安装变轨器出料口的气动接头卡扣；
3. 更换变轨器到缓冲器之间的这段料管进行重试。

#### **Q：使用耗材变轨器时，打印机能否进行校准？**

目前打印机安装耗材变轨器后，将**无法执行高精度喷嘴偏移校准操作**。如需执行该校准，必须先拆除变轨器，恢复设备未接入变轨器的状态。

后续我们将通过功能更新优化解决该问题。

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
