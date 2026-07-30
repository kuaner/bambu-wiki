---
path: zh/h2c/maintenance/upgrade-from-h2s-to-h2c
title: "H2S 升级 H2C 指引全流程指引 - 上篇"
description: "本文概述了从 H2S 升级至 H2C 的完整流程，包括打印机注册、硬件更换、线缆连接及关键注意事项，帮助用户顺利完成升级并保持设备稳定运行。"
tags: []
created: 2025-12-03T09:35:45.792Z
updated: 2026-07-21T01:42:45.595Z
source: https://wiki.bambulab.com/zh/h2c/maintenance/upgrade-from-h2s-to-h2c
---

本文将详细介绍 H2S 升级至 H2C 的操作流程。本次升级核心是为 H2S 搭载 Vortek 系统，实现从单喷嘴到七喷嘴的进阶升级，主要涉及热床、工具头线轨、AP 板、前面盖的更换，以及热端挂架组件、拉柄解锁组件的新增安装。

全文分上下两篇：

- [H2S 升级 H2C 指引全流程指引 - 上篇](.md)
- [H2S 升级 H2C 指引全流程指引 - 下篇](upgrade-from-h2s-to-h2c-part-b.md)

本文为 **H2S 升级 H2C 指引全流程指引 - 上篇**，将聚焦核心安装步骤，具体介绍**热床、工具头线轨及 AP 板**的安装方法。

## H2S-H2C升级包

H2S 升级至 H2C 需要 5 个核心组件，分别为工具头线轨组件、热床、AP 板、热端挂架及 Vortek 升级包。其中，Vortek 升级包内含喷嘴偏移校准传感器、多规格备用螺丝、感应热端、专用打印板、热端挂架横梁等关键配件。

![](https://wiki.bambulab.com/h2c/maintenance/upgrade-from-h2s-to-h2c/pixpin_2025-12-02_17-29-11.png)

建议收到包裹后，第一时间核对包装内物料是否齐全、无缺失，具体配件明细可参考专项文档[《H2S 升级包配件清单》](../../h2s/manual/h2s-to-h2c-acc-in-the-box.md)。

## 难度

⭐⭐⭐⭐⭐

预计更换时长：4 - 5小时

## 准备工作

### 1. 升级版本固件

在正式开始设备升级操作之前，请务必确认打印机固件已更新至 01.02.00.00 或更高版本。  
这一步非常重要，否则可能导致升级过程失败，甚至需要额外更换 MC 板。

### 2. 设备注册

收到升级包后，需联系 [**Bambu Lab 技术支持**](https://bambulab.com/en/support/activate-sn)，提交**新设备序列号**与**当前设备序列号**，完成新设备注册流程。

- **新设备序列号**位于 AP 板背面，需提交该序列号对应的二维码照片，确保二维码清晰可识别。

![](https://wiki.bambulab.com/h2c/maintenance/upgrade-from-h2s-to-h2c/mainboard.jpeg)

**当前设备序列号**可在打印机屏幕的“设备和序列号”中查询，同时打印机右侧内立柱上的二维码也对应设备序列号。

|  |  |
| --- | --- |
|  |  |

序列号查找及新序列号注册的详细操作可参考指引文档：[如何查找序列号及注册新序列号](../../general/find-sn.md)。

> **注意：** 设备未成功注册前，无法完成 WiFi 绑定及 Bambu 账号绑定操作。

### 3. 工具和材料

- 升级包
- H2.0 / H1.5 内六角螺丝刀（优先选用带磁吸功能的款式，便于螺丝取放）
- 撬棒 或 一字螺丝刀（用于拆卸 LED 灯盖及设备侧板）
- 头灯（可选）
- 美工刀
- 斜口钳
- 润滑油&润滑脂
- [螺丝盒](https://makerworld.com.cn/zh/models/1346631-ke-dui-die-de-xiao-ling-jian-he#profileId-1453263)（拆装涉及多种规格螺丝，需分类存放，避免混淆、丢失）

![](https://wiki.bambulab.com/h2c/maintenance/upgrade-from-h2s-to-h2c/screw_box.jpeg)

> **补充说明：** 您可查阅 [Bambu Lab 打印机常见螺钉](../../knowledge-sharing/common-screws.md)，熟悉各类螺丝的适配位置与使用场景。

## 升级步骤

### 步骤 1. 更换打印机热床 （耗时约1.5个小时）

#### 移除打印机背板

依次拆下 **11 颗钣金自攻螺钉（ST3×6）** 与 **12 颗塑料自攻螺钉（BT3×8）**。

1. 使用 H2.0 直柄内六角扳手移除 11 颗 ST3×6（前面图片中的红色圆圈标记， ST3×6）
2. 使用 H2.0 直柄内六角扳手移除 12 颗 BT3×8（前面图片中的绿色方框标记，BT3×8）
3. 黄色标记为外挂料盘固定螺钉（M3×12）

![](https://wiki.bambulab.com/h2c/maintenance/upgrade-from-h2s-to-h2c/rear_panel.png)

4. 按压气管接头以避开干涉，然后将背板向后轻轻倾斜并取出。

![](https://wiki.bambulab.com/h2c/maintenance/upgrade-from-h2s-to-h2c/connection.png)

#### 移除右侧板

1. 使用 **H2.0 内六角扳手**，先拆下固定于上框的 **2 颗固定螺丝（BT3×8）** 和固定于横梁的 **1 颗固定螺丝（BT3×8）**。

![](https://wiki.bambulab.com/h2c/maintenance/upgrade-from-h2s-to-h2c/screw_right.png)

- 拧下固定在立柱上的**2 颗 M3×3**螺丝。这两颗螺丝隐藏在**胶条后方**，需从胶条的预留开孔处轻轻撬动胶条，露出螺丝后再进行拆卸。

|  |  |
| --- | --- |
|  |  |

> **注意：**右侧板除螺丝固定外，还通过卡扣与机身定位。操作前请先找到右侧板边缘的硅胶，从硅胶断口处小心撕断，为后续拆板做好准备。

- 随后从设备后方**先释放卡扣，**从**正面**缓慢掰右左侧板；将贴附在右侧板上的胶布**撕下**后，取下右侧板。

![](https://wiki.bambulab.com/h2c/maintenance/upgrade-from-h2s-to-h2c/pixpin_2025-11-28_11-25-19.png)

#### 移除状态灯

1. **握住状态灯两侧，从后面用力掰解锁后面的卡扣**，当卡扣解锁后再将状态灯往后推，以解锁前面的卡扣，即可取出状态灯；

> 注意：状态灯背后右连接线

![](https://wiki.bambulab.com/h2c/maintenance/upgrade-from-h2s-to-h2c/pixpin_2025-11-28_15-43-40.png)

- 将状态灯的连接线断开连接

![](https://wiki.bambulab.com/h2c/maintenance/upgrade-from-h2s-to-h2c/image-8.png)

#### 断开热床连接线

1. 如下图所示，断开 MC 板（运动控制板）上的 **1 号和 4 号线缆接头，2 号和 3 号为空。**

![](https://wiki.bambulab.com/h2c/maintenance/upgrade-from-h2s-to-h2c/image-12.png)

- 拆除 AC 板（交流控制板）盖的固定螺丝(BT3x8 )，取下 AC 板盖。

|  |  |
| --- | --- |
|  |  |

- 待加热模块供电线移除后，用镊子顶住热床供电线接头上的卡扣凸起处，向外施力即可拔出供电线，完成该线缆的移除。

|  |  |
| --- | --- |
|  |  |

- 将热床地线从卡扣中取出并撕开胶带，然后使用 H2.0 内六角扳手拧松一颗热床地线固定螺丝（STW3x5），将热床地线松开；

|  |  |
| --- | --- |
|  |  |

- 使用 H2.0 内六角扳手拧松一颗线扣固定螺丝（BT3x12），将线扣打开，将热床线缆一起从卡扣中抽出，然后从左内衬的缝隙中抽出，最后从 Z 滑块后面的卡扣中取出。

|  |  |
| --- | --- |
|  |  |

#### 移除热床

1. 使用 H2.0 规格内六角扳手或镊子，轻轻撬开热床左右两侧的两个硅胶塞。

|  |  |
| --- | --- |
|  |  |

- 移除硅胶塞后，露出热床固定螺丝；使用 H2.0 规格内六角扳手，按依次移除六颗 M3x8 规格的热床固定螺丝

![](https://wiki.bambulab.com/h2/maintenance/replace-heatbed-unit/image-44.png)

![heatbed.jpeg](https://wiki.bambulab.com/h2/maintenance/replace-heatbed-unit/heatbed.jpeg)

- 确认所有固定螺丝移除后，小心取下 H2S 热床。

![](https://wiki.bambulab.com/h2c/maintenance/upgrade-from-h2s-to-h2c/remove_heatbed.webp)

#### 安装 H2C 热床

1. 将 H2C 热床线缆逐根穿过后方 Z 轴滑块，从滑块尾部将线缆拉出。

|  |  |
| --- | --- |
|  |  |

- 清洁打印机底部的废料与灰尘，防止后续 Z 轴滑块压到异物，导致热床安装倾斜。

![](https://wiki.bambulab.com/h2c/maintenance/upgrade-from-h2s-to-h2c/image-24.png)

- 将 H2C 热床靠左侧板放置，随后放倒打印机。

![](https://wiki.bambulab.com/h2c/maintenance/upgrade-from-h2s-to-h2c/image-23.png)

- 拉动底部皮带，将 Z 轴滑块降至最底部（拉不动为止）。

![](https://wiki.bambulab.com/h2c/maintenance/upgrade-from-h2s-to-h2c/image-29.png)

- 摆正打印机。

|  |  |
| --- | --- |
|  |  |

- 将热床放置在 3 个 Z 轴滑块上方。

![](https://wiki.bambulab.com/h2c/maintenance/upgrade-from-h2s-to-h2c/image-21.png)

> 如果您有保留开箱时的热床固定螺丝或类似螺丝(M3x35 螺纹长度8)可以将锁紧此处四颗螺丝，确保底部三个滑块完全处于同一高度，等待热床与滑块固定后再移除此处四颗螺丝。如果您没有保留着四颗螺丝可跳过此步骤，确保三颗 Z 滑块完全贴近打印机底部即可。
>
> |  |  |
> | --- | --- |
> |  |  |

- 最后锁紧热床与滑块连接的 6 颗固定螺丝，可以使用原有热床固定螺丝或新热床包装内附赠螺丝（蓝胶M3x8) 。

![](https://wiki.bambulab.com/h2c/maintenance/upgrade-from-h2s-to-h2c/image-18.png)

#### 调整辅助冷却部件风扇

1. 使用 H2.0 内六角扳手，拆除辅助部件冷却风扇底部的两颗固定螺丝（BT3x16）。对于将H2S升级为H2C，需将原来的螺丝位置移动至蓝色位置。

> **注：** H2S 的辅助部件冷却风扇固定螺丝均位于**底部小孔**内。

![](https://wiki.bambulab.com/h2c/maintenance/upgrade-from-h2s-to-h2c/image.png)

- 待底部两颗固定螺丝完全拆除后，托住风扇本体，拔出整个风扇组件。

![](https://wiki.bambulab.com/h2c/maintenance/upgrade-from-h2s-to-h2c/image-3.png)

- 取出风扇后，调整固定螺丝安装位置：先用螺丝刀从辅助冷却部件风扇背部将固定螺丝顶出，再将硅胶套取出（左右两侧固定螺丝操作方式一致）。

|  |  |
| --- | --- |
|  |  |

- 将原位于下方的固定螺丝硅胶套换装至上方对应位置。

![](https://wiki.bambulab.com/h2c/maintenance/upgrade-from-h2s-to-h2c/11月28日.webp)

- 调整软螺钉固定硅胶套位置：将原下排的软螺钉固定硅胶套全部移至上排安装位。
- 安装辅助部件冷却风扇：将软螺钉穿过辅助部件冷却风扇靠近内侧的小孔，用尖嘴钳等工具将软螺钉向外拉出少许，随后手动拉动软螺钉，将风扇初步固定到位。最后使用 H2.0 内六角扳手，将风扇底部的两颗固定螺丝拧紧即可。

|  |  |
| --- | --- |
|  |  |

> 注意：若操作中出现软螺钉断裂，或无法触及软螺钉的情况，请参考 [更换 H2S 辅助部件冷却风扇](../../h2s/maintenance/replace-auxiliary-part-cooling-fan.md) 中的步骤移除左侧板。

#### 安装喷嘴偏移传感器&状态指示灯

1. 在 Vortek 升级包中的 5 号标签盒中找到喷嘴偏移校准传感器，将其安装至热床尾部；连接线缆接头，放入指定槽位后，使用 H1.5 螺丝刀锁紧 2 颗固定螺丝(M2x5)。

|  |  |
| --- | --- |
|  |  |

> 安装喷嘴偏移传感器时，务必注意方向，以防装反。请确认银色的擦嘴钢片位于左侧。
>
> ![](https://wiki.bambulab.com/h2c/maintenance/upgrade-from-h2s-to-h2c/image-41.png)

- 拉动底部皮带，手动升高热床，连接状态指示灯线缆，对照热床底部扣位，将状态指示灯安装到位。

|  |  |
| --- | --- |
|  |  |

- 安装热床左右两侧的硅胶块。

![](https://wiki.bambulab.com/h2c/maintenance/upgrade-from-h2s-to-h2c/070.webp)

#### 连接 H2C 热床连接线

1. 在打印机背面，先将热床线缆卡入 Z 轴滑块的理线扣内，再将线缆穿过侧边孔隙。

|  |  |
| --- | --- |
|  |  |

- 将热床线缆插入 AC 板对应接头（按下图所示，分别对应棕色、蓝色、红色线缆）。

![](https://wiki.bambulab.com/h2c/maintenance/upgrade-from-h2s-to-h2c/image-35.png)

- 锁紧热床地线固定螺丝(M3x3)，完成后再锁紧热床线缆固定螺丝(BT3x12)。

|  |  |
| --- | --- |
|  |  |

- 安装 AC 板盖，锁紧其固定螺丝(M3x8)。

![](https://wiki.bambulab.com/h2c/maintenance/upgrade-from-h2s-to-h2c/image-38.png)

- 插接之前拔下的线缆接头以及**喷嘴偏移传感器接头**，并将线缆卡入 AC 板盖的理线槽内，避免线缆松动。

|  |  |
| --- | --- |
|  |  |

### 步骤 2. 更换工具头线轨（耗时约1个小时）

#### 移除 PTFE 管

1. 按压工具头上方的气动接头，断开工具头上方的PTFE管。推出缓冲器的气动接头，按压解锁气动接头。

|  |  |
| --- | --- |
|  |  |

- 从拖链中抽出PTFE管。

![](https://wiki.bambulab.com/h2c/maintenance/upgrade-from-h2s-to-h2c/image-31.png)

#### 移除 AP 理线盖

1. 使用 H2.0 内六角扳手拧下 1 颗固定螺丝（BT2.6x8），然后从靠近前门的一侧取下 AP 板盖。

![](https://wiki.bambulab.com/h2c/maintenance/upgrade-from-h2s-to-h2c/image-55.png)

#### 移除缓冲器并断开 USB-C 线缆

1. 拧下USB-C理线扣中的螺丝。

![](https://wiki.bambulab.com/h2c/maintenance/upgrade-from-h2s-to-h2c/image-53.png)

- 从卡扣中抽出线缆，断开 USB-C 数据线。

![](https://wiki.bambulab.com/h2c/maintenance/upgrade-from-h2s-to-h2c/image-54.png)

- 使用H2.0内六角扳手，移除缓冲器上的4颗固定螺丝（BT3x8），松开缓冲器。

![](https://wiki.bambulab.com/h2c/maintenance/upgrade-from-h2s-to-h2c/image-52.png)

#### 移除拖链

按图示方向，向下按压拖链右上角的卡扣使其脱离卡槽，随后握住拖链用力拔出整段拖链。

|  |  |
| --- | --- |
|  |  |

#### 移除皮带

移除工具头皮带固定座上的4颗螺丝（左右两侧各2颗），取下皮带。

|  |  |
| --- | --- |
|  |  |

#### 粘贴防护胶布

在线轨两侧粘贴无痕胶布（若无无痕胶布，可先用纸片覆盖线轨，再外层粘贴透明胶固定）。此举用于限制工具头移动，防止拆除线轨时工具头滑出线轨导致滑块滚珠脱落。

![](https://wiki.bambulab.com/h2c/maintenance/upgrade-from-h2s-to-h2c/image-49.png)

#### 移除线轨组件

1. 使用一字螺丝刀或撬棒，小心撬开工具头左右两侧的LED灯盖。

|  |  |
| --- | --- |
|  |  |

- 打印机顶部设有专用螺丝刀插孔，将长柄内六角扳手穿过顶部泡棉，对准下方对应螺丝(M3x6)并将其移除。

> 务必遵循教程，使用螺丝刀穿过泡棉以及预留孔，禁止从螺丝侧面斜向拧动螺丝。

|  |  |
| --- | --- |
|  |  |

- 依次拆除线轨侧面的4颗螺丝(M3x8)，以及滑车底部的2颗螺丝(M3x6)。

|  |  |
| --- | --- |
|  |  |
|  |  |

- 待所有螺丝拆除后，先将右侧线轨与滑车分离，再分离左侧线轨，随后倾斜线轨组件将其取出。

![](https://wiki.bambulab.com/h2c/maintenance/upgrade-from-h2s-to-h2c/image-66.png)

#### 安装 MC-TH 电源通讯转接线

将 MC-TH 电源通讯转接线从内衬的走线孔中穿过，再与 MC 板连接。

![](https://wiki.bambulab.com/h2/maintenance/replace-toolhead-to-mc-board-cable/image-16.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-toolhead-to-mc-board-cable/image-17.png)

![](https://wiki.bambulab.com/h2/maintenance/replace-toolhead-to-mc-board-cable/image-18.png)

#### 安装 H2C 工具头线轨组件

1. 将线轨组件左右两侧的滑块调整至一前一后的位置，倾斜角度后平稳放入安装位。

![](https://wiki.bambulab.com/h2c/maintenance/upgrade-from-h2s-to-h2c/059.webp)

> 注意：工具头线轨组件未完全安装到位前，**禁止剪断**左右两侧的固定扎带。

- 将线轨组件向前推动至无法移动，借助前门立柱进行限位，确保线轨保持平行状态。

![](https://wiki.bambulab.com/h2c/maintenance/upgrade-from-h2s-to-h2c/060.webp)

- 锁紧线轨组件的 8 颗螺丝：先锁紧左右两侧顶部螺丝（红胶M3x6），垂直向下操作时螺丝易滑脱，建议使用带磁吸功能的螺丝刀。

|  |  |
| --- | --- |
|  |  |

- 接着锁紧线轨组件后方螺丝（BT3x8），左右各 2 颗。

|  |  |
| --- | --- |
|  |  |

- 锁紧底部螺丝（红胶M3x6），左右各 1 颗。

|  |  |
| --- | --- |
|  |  |

- 使用斜口钳剪断左右两侧的固定扎带。

|  |  |
| --- | --- |
|  |  |

- 使用剪刀剪断皮带与皮带固定块的重叠部分（5 个齿数），至此完成皮带的预处理操作（左右两侧皮带均需按此方式修剪）。

|  |  |
| --- | --- |
|  |  |

> 若出现皮带过短的情况，可使用备用皮带，参考 [更换 H2 系列 X/Y 皮带](../../h2/maintenance/replace-xy-belt.md) 完成更换；若皮带长度偏长，可借助剪刀剪去多余齿数，调整至适配长度

- 将皮带穿过 H2C 皮带固定块，然后将皮带固定座的齿面对准皮带的齿面，并且凸起的点位于皮带的末端。然后拉动皮带，将固定座和皮带一起卡入固定块中。

|  |  |
| --- | --- |
|  |  |

- 将皮带固定座装入工具头对应的安装槽位，锁紧两侧的蓝胶M3x8固定螺丝（左右各3颗）。

> 锁紧顺序：先预锁紧中间螺丝，再依次锁紧上下两颗，最后再次加固中间螺丝，确保固定座安装牢固无松动。

|  |  |
| --- | --- |
|  |  |

- 先将拖链末端压入对应安装槽内，再用力向左推动拖链，使其卡入卡槽完成固定。

|  |  |
| --- | --- |
|  |  |

- 重新连接MC-TH线的两个插头，将线缆穿过理线扣并整理整齐，避免缠绕。

|  |  |
| --- | --- |
|  |  |

- 对准打印机上框卡槽，安装左右两侧 LED 灯盖并按压固定。

|  |  |
| --- | --- |
|  |  |

#### 安装双头后限位块

![](https://wiki.bambulab.com/h2c/maintenance/upgrade-from-h2s-to-h2c/dsc09972.jpg)

将后限位块放置于 Y 轴后侧对应位置，其**左右两侧各一个**。使用 H1.5 规格内六角螺丝刀，将双头后限位块的固定螺丝（M2x5）拧紧到位。

|  |  |
| --- | --- |
|  |  |

#### 更换切刀顶杆

H2C 切刀顶块组件安装于打印机腔体左右两侧，核心作用是顶住切刀以切断耗材，进而完成换料、退料等操作。H2S 和 H2C 的工具头尺寸不一致，若需将 H2S 升级为 H2C 配置，需先拆除原有切刀顶杆，安装两个全新的 H2C 切刀顶杆，具体操作步骤如下：

|  |  |
| --- | --- |
|  |  |

1. 使用 H2.0 内六角扳手拧下原切刀顶杆的固定螺丝，取下切刀顶杆

![](https://wiki.bambulab.com/h2c/maintenance/upgrade-from-h2s-to-h2c/pixpin_2025-11-28_17-23-56.png)

- 将切刀顶块对准打印机上的螺丝孔位，使用 H2.0 内六角扳手拧紧四颗固定螺丝（螺丝规格标注：红色圆圈为 BT2.6×8；蓝色方块为 M2.5×5）

> 注：左右两侧切刀顶块的螺丝孔位布局一致，均为上排两颗、下排两颗。

![](https://wiki.bambulab.com/h2c/maintenance/upgrade-from-h2s-to-h2c/install_6.png)

#### 移除缓冲器

1. 使用 H2.0 内六角扳手移除打印机背部料管支架固定螺丝(BT3x5)。

![](https://wiki.bambulab.com/h2c/maintenance/upgrade-from-h2s-to-h2c/pixpin_2025-11-28_18-43-47.png)

- 用螺丝刀撬动线缆侧边；

![](https://wiki.bambulab.com/h2c/maintenance/upgrade-from-h2s-to-h2c/image-81.png)

- 小心撬出接头，断开线缆。

![](https://wiki.bambulab.com/h2c/maintenance/upgrade-from-h2s-to-h2c/image-85.png)

#### 安装 H2C 缓冲器

1. 使用 H2.0 内六角扳手安装新的打印机背部料管支架固定螺丝(BT3x5)。

![](https://wiki.bambulab.com/h2c/maintenance/upgrade-from-h2s-to-h2c/pixpin_2025-11-28_18-44-06.png)

- 将缓冲器连接线重新与缓冲器连接

![](https://wiki.bambulab.com/h2c/maintenance/upgrade-from-h2s-to-h2c/image-80.png)

#### 固定缓冲器

使用 H2.0 内六角扳手拧紧背板的四颗固定螺丝（BT3×8）。

![](https://wiki.bambulab.com/h2c/maintenance/upgrade-from-h2s-to-h2c/install_7.png)

### 步骤 3. 更换 AP 板（耗时约20分钟）

#### 移除 AP 板

依次拔下 AP 板上的 1-10 号插头。

![](https://wiki.bambulab.com/h2c/maintenance/upgrade-from-h2s-to-h2c/image-84.png)

1. 屏幕排线
2. USB 接口板
3. 左LED灯连接线（红色插头）
4. 右LED灯连接线（蓝色插头）
5. MC-AP 线缆（通信）
6. MC-AP 线缆（供电）
7. TH供电线缆（借AP中转）
8. USB-C 数据线
9. 实况摄像头连接线

左下角螺丝连接了一根接地线缆。

#### 移除 TH 供电线缆

1. 使用 H2.0 内六角扳手拧下 1 颗固定螺丝（规格 BT3×8），随后向下拉动废料滑梯，直至可见滑梯的两个卡扣，再向外取出废料滑梯。

|  |  |
| --- | --- |
|  |  |

- 在缓冲器旁断开与 TH 板自带线缆的连接。

|  |  |
| --- | --- |
|  |  |

- 在 MC 板处断开 TH 供电线缆的连接，再将该转接线从设备内衬中抽出。

![](https://wiki.bambulab.com/h2c/maintenance/upgrade-from-h2s-to-h2c/pixpin_2025-12-01_10-18-45.webp)

#### 安装 H2C TH 供电线缆

1. 从升级包中取出 18 号的 H2C TH 供电线缆。

![](https://wiki.bambulab.com/h2c/maintenance/upgrade-from-h2s-to-h2c/h2s-to-h2c-acc-in-the-box/18_improve.png)

- 将新的 TH 供电线缆从打印机内衬中穿入。

![](https://wiki.bambulab.com/h2c/maintenance/upgrade-from-h2s-to-h2c/pixpin_2025-12-01_10-21-22.webp)

- 将 TH 供电线缆连接至 MC 板对应接口。

![](https://wiki.bambulab.com/h2c/maintenance/upgrade-from-h2s-to-h2c/vlcsnap-2025-12-01-10h30m26s672.png)

#### 取下 AP 板并拆下 WIFI 天线座子

1. 使用 H2.0 内六角扳手拧下 4 颗固定螺丝（BT3×5）

![](https://wiki.bambulab.com/h2c/maintenance/upgrade-from-h2s-to-h2c/image-94.png)

- 断开 WIFI 天线插头，取下 AP 板。

![](https://wiki.bambulab.com/h2c/maintenance/upgrade-from-h2s-to-h2c/gif_3.webp)

#### 安装 H2C AP 板

1. 先连接 WiFi 天线，避免 AP 板固定后安装困难；将 AP 板对准上框螺丝孔位，用 H2.0 螺丝刀锁紧 4 颗固定螺丝（BT3x5），同时将地线安装至左下角对应螺丝位。

|  |  |
| --- | --- |
|  |  |

- 连接 AP 板相关线缆，共需安装 10 个线缆接头，具体对应如下：

![](https://wiki.bambulab.com/h2c/maintenance/upgrade-from-h2s-to-h2c/image-90.png)

1. 俯视相机排线（激光版本配备）
2. 屏幕排线
3. 右 LED 灯
4. 左 LED 灯
5. WiFi 天线
6. USB 接口板
7. MC-AP 线缆（通信）
8. MC-AP 线缆（供电）
9. 实况摄像头排线
10. 工具头 USB-C 线缆

> **注意：安装工具头 USB-C 线缆时，需确保带有字母 “A” 的一面朝外。**
>
> ![](https://wiki.bambulab.com/h2c/maintenance/upgrade-from-h2s-to-h2c/image-92.png)

#### 安装 AP 板盖

1. 从靠近打印机背部的一侧开始安装 AP 板盖，确保盖体右侧与缓冲器齐平，再将整个 AP 板盖压入槽位卡紧。

|  |  |
| --- | --- |
|  |  |

- 最后使用 H2.0 内六角螺丝刀锁紧一颗固定螺丝（BT2.6x8）。

![](https://wiki.bambulab.com/h2c/maintenance/upgrade-from-h2s-to-h2c/image-88.png)

---

本升级指引全文分为上下两篇，可通过以下链接访问对应内容：

- [H2S 升级 H2C 指引全流程指引 - 上篇](.md)
- [H2S 升级 H2C 指引全流程指引 - 下篇](upgrade-from-h2s-to-h2c-part-b.md)

关于感应热端架横梁、感应热端架组件、前面盖、安装侧板、背板及其他相关配件的具体操作说明，请跳转至 [H2S 升级 H2C 指引全流程指引 - 下篇](upgrade-from-h2s-to-h2c-part-b.md) 查阅。

## FAQ

### Q1：将 H2S 升级成 H2C 激光版后，是否能使用 40 W 的激光模组，还是只能继续使用 10 W；

激光版的H2S升级成激光版的H2C 后，支持40W 激光模组，H2S 不支持40W 激光模组主要是空间结构上的限制，升级成H2C 的工具头后就没有这种结构限制了。

### Q2：非接触3D mesh功能在升级成H2C后是否支持；

H2S（10W） 和H2C (10W和40W)激光版都支持非接触3D mesh功能，只不过需要等新固件，H2S 预计 2026 年 3 月底会提供最新固件支持该功能。

### Q3：如果将 H2S 升级成 H2C 并加装激光侧板，请问侧板的霍尔传感器是否能正常连接并使用。

虽然可以将 H2S 激光版升级为 H2C 激光版，但我们**不建议**这样操作。

原因是：H2S 升级为 H2C 后，将运行 H2C 固件，而 H2C 固件需要检测左右侧窗的霍尔传感（每个侧板 2 个，共 4 个）。因此，如需将 H2S 激光版升级为 H2C，除 H2S Vortek 升级套件外，还需**额外购买 H2C 的左右侧板**。

同时，如升级为 H2C 并使用激光功能，还需联系售后，售后将为您的Vortek升级订单**免费补发上盖框组件**（**左右侧板需用户自行承担费用**）。

拆卸指南：

- [更换 H2S 上盖组件](../../h2s/maintenance/replace-enclosure-top-frame.md)
- [更换 H2S 左右侧板](../../h2s/maintenance/replace-side-panel.md)

安装指南：

- [更换 H2C 上盖组件](../../h2/maintenance/replace-enclosure-top-frame.md)
- [更换 H2C 左/右侧板](../../h2/maintenance/replace-side-panel-with-glass-window.md)

|  |  |
| --- | --- |
| 右侧板 | 左侧板 |

(Upper Hall Sensor 位于上盖框组件上，且该霍尔板的线缆走线路径较为复杂，几乎无法单独加装这 2 个霍尔板。因此无法仅通过增加霍尔板来完成升级。为表达我们的好意，如您选择进行升级，售后将为您的升级订单免费补发所需的上盖框组件备件，以协助您完成安装。)

整体来看，该升级方案会增加硬件成本与安装复杂度，因此我们不建议将激光版 H2S 升级为 H2C。

### Q4：不使用激光功能的情况下，H2S 升级 H2C 是否需要更换 H2C 侧板？

不需要额外购买 H2C 侧板。若您有 H2C 双侧透视窗的外观需求，可选择加购 H2C 左右侧板。

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
