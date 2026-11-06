---
path: zh/h3c/manual/tpu-printing-guide
title: "H3C TPU 打印指南"
description: "本文介绍了如何使用 H3C 打印 TPU 耗材。"
tags: []
created: 2026-11-03T13:19:28.813Z
updated: 2026-11-06T08:13:42.454Z
source: https://wiki.bambulab.com/zh/h3c/manual/tpu-printing-guide
---

## 前言

TPU（热塑性聚氨酯）是一种柔性耗材，具有弹性，可被拉伸并回弹。根据软硬程度可分为 **TPU for AMS、TPU 95A HF、TPU 90A、TPU 85A、TPU 75A**。该材料性能优异、应用广泛，不同硬度可满足多样化场景的使用需求。

TPU 容易吸湿，受潮会影响打印质量。为了避免这种情况，建议：

- 将料盘存放在湿度低于 20% RH 的环境中；
- 使用收纳盒或 AMS 3H/AMS HT 的烘干槽进行存放；
- 在收纳盒内放置干燥剂。

### H3C 支持打印的 TPU 种类

| **热端规格** | **支持的 TPU 类型** |
| --- | --- |
| 1.75 mm 线径 | 1.75 mm 95A / 90A / 85A |
| 2.85 mm 线径 | 2.85 mm 90A / 85A / 75A |

> **注意**：打印 2.85 mm TPU 时，需更换为 **2.85 mm 专用热端**；更换时请确保新热端的线缆与管路按原有走向布置，避免走线扭曲、拉扯或干涉，以保证运动顺畅与打印安全。

### AMS 3H 耗材直通口

AMS 3H 共有 **7 个耗材直通口**，分别为 1、3、5、6、7、8、9 号槽，其中 **6 号和 8 号**槽位于烘干仓内，支持**边烘边打**。

> 温馨提示：使用 6 号槽直通口打印 TPU 时，建议**仅进行单色打印**。若将该直通口的 TPU 与其他材料混用进行多色/多材料打印，存在 TPU 脱出风险，易导致打印失败。其他直通口的 TPU 槽位打印多色或多材料模型时，没有该换头风险。

![001.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/tpu-printing-guide/zh/001.png)

TPU 耗材根据硬度不同，进料方式有所区别：

- **TPU for AMS**：硬度相对较高（相比普通软质 TPU），进退料顺畅， 可直接放入 AMS 并通过 **AMS 自动进料口**打印；
- **95A 及以下硬度的 TPU**：质地较软，进料阻力大， 需通过 AMS 的**耗材直通口**进料，且对进料通路有一定要求，否则易因阻力过大影响打印质量。

## 视频指南

## 打印前准备

### 烘干耗材

TPU 具有较强的吸湿性，在自然环境中容易吸收水分。若含有水分的 TPU 直接用于 3D 打印，打印过程中水分受热会迅速汽化，从而在打印制品中形成气泡、空洞等缺陷，严重影响打印质量，甚至可能导致打印失败。因此我们推荐您使用下述设备及参数进行烘干。详情请参考[耗材准备——干燥](../../filament-acc/filament/dry-filament.md)。

- **AMS 3H：** 75 ℃ x 18 h
- **鼓风式烤箱**：70 ℃ x 8 h
- **AMS HT**: 75 ℃ x 18 h

烘干前料盘外沿宽度约为 **65.4 mm**；烘干过程中 TPU 受热膨胀会导致料盘变形，**烘干后料盘边缘宽度可能增大至约 69.4 mm**。请手动转动料盘，**确认是否与 AMS 框架存在剐蹭**。轻微滚动摩擦属于正常现象，但若因局部严重变形导致明显剐蹭，则会严重影响打印，建议更换料盘。

![002.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/tpu-printing-guide/zh/002.png)

若料盘因烘干膨胀等原因导致宽度超出 AMS 的兼容范围、无法正常放入，建议改用外挂方式进料，并穿过 AMS 支架和卡扣，具体操作请参考下图；此时建议使用靠近左/右侧板的 1 或 9 号打印头进行打印。此时建议使用靠近左/右侧板的 1 或 9 号打印头进行打印。如需长时间打印，建议使用米桶等密封箱，防止耗材打印中途受潮。

|  |  |
| --- | --- |
|  |  |

### 检查热端硬料残留

若不是全新热端，请检查打印头及热端内是否有残余硬料；

> **注意：** 为防止进料时发生卷料故障，请在更换软料前彻底移除残留硬料。建议通过冷拔清理喷嘴，确保通道畅通后再进行进料操作。

![003.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/tpu-printing-guide/zh/003.png)

若存在残料，请进入屏幕\*\*“①设置”**页面，点击**“②工具箱 > ③喷嘴冷拔维护”\*\*，待热端升温后，用 **PLA / PETG** 冷拔 2–3 次，**请勿使用纤维增强耗材**（例如 -CF 和 -GF）进行冷拔。

|  |  |  |
| --- | --- | --- |
| 004.png | 005.png | 006.png |

> **注意：** **2.85 mm 热端** 不支持上述程序自动冷拔功能，如果遇到堵塞场景，建议使用通针处理，通针清理方法请参考：[堵塞排查](../troubleshooting/unclogging.md)。

### 安装 2.85 mm 线径打印头（选做）

H3C 打印机标配了一个 2.85 mm 线径打印头。如需使用更多 2.85 mm 线径打印头打印 2.85 mm TPU，您可前往商城选购额外的 2.85 mm 打印头，并参考 wiki：[打印头组件更换指南](../maintenance/replace-printtool.md) 进行安装。

## 进料步骤

### 步骤 1：调整料管

- 拆下靠近目标打印头一侧的 AMS 磁吸侧板；

|  |  |
| --- | --- |
| 007.png | 008.png |

- 从挂架上取下需要使用的打印头；

> 请确保热端温度降至室温再操作，以防烫伤。

![009.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/tpu-printing-guide/zh/009.png)

- 按压两侧料管卡扣，**先向下按压料管**，再将料管向外拔出；

|  |  |
| --- | --- |
| 010.png | 011.webp |

- 将料管插入侧槽固定；

![012.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/tpu-printing-guide/zh/012.png)

- 裁剪一段 **35mm**的料管，将其插入料管口（仅 1.75 mm 线径 TPU 需要此步骤）；

|  |  |
| --- | --- |
| 013.png | 014.png |

> **注意：**
>
> 1. 短料管须严格按照指定长度裁剪，并确保其高度低于线缆根部，以保证料管可顺利拔出，并防止打印过程中料管与打印头线缆根部发生干涉；
>
> ![015.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/tpu-printing-guide/zh/015.png)  
> 2. 关于辅助短料管的使用建议：
>
> - 引导作用：实操表明，安装短料管能够为主体提供良好的引导，使手动将耗材送至挤出轮处的操作更加便捷顺畅。因此，官方建议优先使用短料管。
> - 灵活选择：短料管并非强制性配件。如果您认为安装短料管操作繁琐，且在实际推送耗材时能够确保挤出轮顺利咬合，可选择不插入短料管，直接进行手动送料。
>
> 3. 使用 2.85mm 线径用打印头打印 TPU 时**无需使用短料管**，后续送料时，可将 TPU 75A 直接推入打印头中。
>
> ![016.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/tpu-printing-guide/zh/016.png)

- 将打印头重新放回挂架；

![017.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/tpu-printing-guide/zh/017.png)

### 步骤 2：屏幕操作

- 进入① **“耗材”** 页面，**点击“②… > ③** **外挂手动进料”**；

![018.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/tpu-printing-guide/zh/018.png)

- ④选定需使用的槽位，再点击 **“⑤编辑耗材”**；

> 请优先使用 3、5、6、7 和 8 号槽位。

![019.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/tpu-printing-guide/zh/019.png)

设置 TPU 耗材类型及颜色；

|  |  |  |
| --- | --- | --- |
| 020.png | 021.png | 022.png |

- 点击 **“⑦进料”**；

![023.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/tpu-printing-guide/zh/023.png)

机器此时会自动取用对应打印头，并开始升温；

|  |  |
| --- | --- |
| 024.png | 025.png |

升温成功后，机器会提示手动送入耗材。

![026.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/tpu-printing-guide/zh/026.png)

### 步骤 3：送料（料盘旋转方向很关键，请务必查看详情）

- 打开 AMS 上盖；

![027.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/tpu-printing-guide/zh/027.png)

- 打开对应槽位的耗材直通口（本篇使用 7 号槽）；

> 注意：请确保 AMS 槽位和打印头对应，避免出现槽位与打印头不对应导致打印失败的情况。

![028.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/tpu-printing-guide/zh/028.png)

- 放置料盘时，**使耗材出线位置位于料盘下方（与自动进料的方向相反）**，然后将耗材插入耗材直通口；

|  |  |
| --- | --- |
| 029.png | 030.png |

> **注意：**
>
> 1. TPU耗材的进料出线（料盘旋转）方向与自动进料正好相反，操作时非常容易出错。如果出线方向接反，耗材很容易从料盘中脱落，从而导致打印失败。
>
> ![031.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/tpu-printing-guide/zh/031.png)

> 2. 如需使用 6 和 8 号槽，同样需要**将耗材出线位置位于料盘下方**送料，请参考下图：
>
> ![032.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/tpu-printing-guide/zh/032.png)

- 手动将耗材从对应打印头的间隙中穿出，并穿过卡扣，慢慢送入打印头；

|  |  |
| --- | --- |
| 033.webp | 034.png |

> 注：由于本次打印使用的是 7 号槽位，因此耗材需从 7 号线缆旁穿过，如下图：
>
> ![035.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/tpu-printing-guide/zh/035.png)

❗**请仔细检查耗材是否从正确的间隙中穿出，料管和耗材走线是否顺畅，无扭曲或缠绕；**

- **正确示例：**

|  |  |
| --- | --- |
| 036.png | 037.png |

- **错误示例：**

|  |  |  |
| --- | --- | --- |
| 038.png | 039.png | 040.png |

> #### 💡6 & 8 号槽送料注意事项
>
> 6 号和 8 号槽位于 AMS 后方，进料便捷性不如前方的 1、3、5 和 7 号槽，尤其是 6 号槽；因此，**建议送****料时借助****长****镊子****将耗材小心夹出。**
>
> 其次，建议**在 6 号槽仅进行单色****TPU****打印**，避免混色或多色打印，原因是因为该打印头走线较为复杂，整体阻力偏大，自动换头放置时，耗材有概率被拉出挤出机造成打印失败。
>
> ![041.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/tpu-printing-guide/zh/041.png)

> 以下为 6 号和 8 号槽 TPU 的具体走向：
>
> - **6 号：** 将耗材从 5 号和 6 号料管和线缆中间穿出；
> - **8 号：** 将耗材从 9 号料管上方绕过，然后穿入 8 号和 9 号料管中间；
>
> |  |  |
> | --- | --- |
> | 042.png | 043.png |

- 观察视窗中是否出现耗材；

![044.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/tpu-printing-guide/zh/044.png)

待耗材均匀、流畅挤出，即完成进料。

|  |  |
| --- | --- |
| 045.webp | 046.png |

> **注意**：发起打印时，擦料塔位置默认位于打印板右下方。  
> ![tower.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/tpu-printing-guide/zh/tower.png)  
> 不建议将擦料塔移至打印板后半部分，原因如下：
>
> - 喷嘴从挂架到擦料塔会经过模型，可能漏料至打印件上。
> - 重新升温后，挤出阻力有时会偏大，喷嘴运动到后方位置时阻力也会增加，两种阻力可能发生叠加，影响挤出稳定性。

## 退料步骤

### 步骤 1： 退料

- 点击屏幕进入 **“①耗材”** 页面，选择② **需要退料的耗材** ，点击 **“③退料”**；

![047.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/tpu-printing-guide/zh/047.png)

- 升温成功后，机器会提示手动拉出耗材，此时需缓慢拉出耗材。

|  |  |
| --- | --- |
| 048.png | 049.png |

### 步骤 2： 取出耗材

- 进入 **“①控制”** 页面，点击 **“②工具与挤出机 > ③放置”**，机器会自动将打印头放回挂架上；

|  |  |
| --- | --- |
| 050.png | 051.png |

- 按住料管两侧的卡扣，先轻微向下按压料管（以释放锁紧结构），再将其向外拔出。若操作时手滑，可使用纤维布包裹料管以增加摩擦力；

> 请确保热端温度降至室温再操作，以防烫伤。

![052.webp](https://public-cdn.bblmw.com/wiki/new/h3c/manual/tpu-printing-guide/zh/052.webp)

- 从侧槽中取出长料管，插入料管槽，确保插入到位；

![053.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/tpu-printing-guide/zh/053.png)

- 将打印头重新放回挂架对应位置，请勿放置错误；

![054.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/tpu-printing-guide/zh/054.png)

- 装回两侧 AMS 磁吸侧板。

|  |  |
| --- | --- |
| 055.png | 056.png |

## 打印后处理

若 TPU 材料与支撑结构或打印底板接触面积较大、粘附过牢，建议喷洒适量酒精以辅助模型剥离。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
