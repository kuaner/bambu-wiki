---
path: zh/ams-2-pro/manual/setup-and-printting
title: "AMS 2 Pro 工作流程和功能介绍"
description: ""
tags: []
created: 2025-03-25T08:25:02.694Z
updated: 2026-07-09T10:36:58.308Z
source: https://wiki.bambulab.com/zh/ams-2-pro/manual/setup-and-printting
---

## AMS 初始化设置

当首次连接 AMS 2 Pro 到 H2D 打印机时，需要进行一次初始化。因为H2D配有双挤出机，这一步的目的是检测 AMS 连接到了哪一侧的挤出机。在“耗材”——“AMS 初始化”中，可选择自动模式或手动模式开启 AMS 初始化。

![](https://wiki.bambulab.com/h2/manual/ams2pro/image-13.png)

![](https://wiki.bambulab.com/h2/manual/ams2pro/image-14.png)

### **自动模式**

**操作步骤：**

- 进入打印机屏幕「耗材」→「AMS 初始化」→ 选择「自动模式」；
- 系统自动检测 AMS 连接的挤出机侧（左/右）。

**注意事项**：

- AMS 2 Pro 内需插入一卷耗材（任意一个槽位即可）；
- 已进料的耗材需提前退料；
- 确保缓冲器内部无残留耗材丝（避免断料残留在内部）。

**工作原理**：  
AMS 将耗材送至挤出机，左右挤出机各有一个霍尔传感器，通过霍尔传感器触发信号来判断AMS所配对的挤出机。

![](https://wiki.bambulab.com/h2/manual/ams2pro/image-11.png)

### **手动模式**

**适用场景**：AMS中无耗材时手动调整 AMS 与挤出机的配对关系。  
**操作步骤**：

- 进入「耗材」→「AMS 初始化」→「手动模式」；
- 手动指定 AMS 连接的挤出机侧（左/右）。

![](https://wiki.bambulab.com/h2/manual/ams2pro/image-10.png)

**限制条件**：

- 若 AMS 已进料至挤出机，则该 AMS 图标为灰色，并且无法修改配对关系。

![](https://wiki.bambulab.com/h2/manual/ams2pro/image-12.png)

## AMS 功能

### 预上料

**作用：** 拉紧耗材丝，避免料盘上的耗材松散，并提供插料时的交互反馈。

**触发方式**：在 AMS 2 Pro 空闲状态时，插入耗材至进料口 → 自动预上料（上下料器送料至 AMS 五通传感器后往回拉）。

**插入辅助功能**：点击空槽图标 → 上下料器电机开始转动，可用于辅助插料。

### 读取 RFID

**模式设置**：

你可以在屏幕的**设置——AMS 选项**里对自动读取RFID功能进行相关设置。

**插入耗材时读取**：插料后自动读取RFID；

**开机时读取**：重启AMS后自动读取已插入的耗材的RFID信息；

![](https://wiki.bambulab.com/h2/manual/ams2pro/image.png)

1. **手动读取**：点击对应槽位 →「重读」，即可重新读取该槽位的RFID。

![](https://wiki.bambulab.com/h2/manual/ams2pro/image-1.png)

![](https://wiki.bambulab.com/h2/manual/ams2pro/image-2.png)

### **剩余容量估算**

**工作原理：** 通过 RFID 标签转动一圈送出的耗材丝长度来估算余量（1kg 料卷默认为 100%）。若启用了剩余容量估计功能，则读取RFID的过程会进行两次，第一次读取耗材信息，第二次估算剩余容量。

**显示位置**：槽位上方耗材名称下的横条显示了耗材大致剩余的容量。

![](https://wiki.bambulab.com/h2/manual/ams2pro/image-3.png)

### **AMS 排序与连接**

**默认排序逻辑**：每台AMS都会被分配一个顺序并显示在屏幕上。通过6pin线直连打印机为 AMS A，级联依次为 B、C、D；

**手动重置**：「设置」→「AMS选项」→ 「重置」→ 按需重新连接 AMS。

![](https://wiki.bambulab.com/h2/manual/ams2pro/image-4.png)

### AMS**自动续料**

**启用条件**：

- 耗材属性完全一致（品牌、类型、颜色）即可以形成续料关系。
- 耗材需位于同一挤出机连接的 AMS（左对左，右对右）。

![](https://wiki.bambulab.com/h2/manual/ams2pro/image-5.png)

**操作路径**：

- 「设置」→「AMS选项」→ 选择「AMS自动续料」来启用自动续料功能。

![](https://wiki.bambulab.com/h2/manual/ams2pro/image-6.png)

- 「耗材」→「自动续料」→ 分左右挤出机页面查看续料关系。

![](https://wiki.bambulab.com/h2/manual/ams2pro/image-7.png)

### **湿度与温度监控**

AMS 2 Pro 的2号槽和3号槽中间有个传感器，可以用于检测AMS内部的湿度和温度。

![](https://wiki.bambulab.com/h2/manual/ams2pro/image-8.png)

- **查看路径**：「耗材」→ 点击 AMS 湿度图标 → 进入「烘干和湿度」页面；

![](https://wiki.bambulab.com/h2/manual/ams2pro/image-9.png)

![](https://wiki.bambulab.com/h2/manual/ams2pro/image-15.png)

- **显示内容**：点击左上角的图标，可以切换不同设备，查看每台AMS的实时湿度、温度数据。

![](https://wiki.bambulab.com/h2/manual/ams2pro/image-16.png)

### 烘干功能

#### 功能概述

- **硬件配置**：AMS 2 Pro 内置加热烘干模块（位于中框下方）
- **最高烘干温度 65°C：**  
  最高温度需在环境温度 ≥ 25°C 的条件下方可实现。当环境温度低于 25°C 时，**受自然散热影响**，实际烘干温度可能无法达到最高值，这并非是产品故障。由于低温环境可能影响烘干效果，建议**在适宜的室温条件下**使用该功能，或在低温环境中采取相应的保温措施，以获得更稳定的烘干效果。

![](https://wiki.bambulab.com/h2/manual/ams2pro/image-17.png)

- **适用场景**：如果耗材受潮了，可使用烘干功能将其烘干。所有耗材均可使用AMS来烘干，但部分材料所需烘干温度高于65℃，可能无法完全干燥。

![](https://wiki.bambulab.com/h2/manual/ams2pro/image-18.png)

#### **操作指南**

**烘干流程**：

- 关闭 AMS 2 Pro 上盖 → 进入「烘干和湿度」页面；
- 选择所需烘干的耗材 → 设置温度与时长 → 启动烘干。连接多台 AMS 时，可以通过「耗材」页面逐一切换设备启动烘干，或在烘干页面左上角切换 AMS 设备。

![](https://wiki.bambulab.com/h2/manual/ams2pro/img_v3_02hd_486cda82-1440-445b-b417-18440e4a4f0g.png)

![](https://wiki.bambulab.com/h2/manual/ams2pro/image-19.png)

#### **注意事项**

- **电源要求**：H2D 打印机支持1台 AMS 2 Pro 从打印机取电烘干，如果需要同时烘干多台 AMS 2 Pro 内的耗材，其余的AMS需要从AMS电源适配器供电烘干。如果 AMS 2 Pro 连接了 X/P 系列打印机（P2S 除外），则每台都必须通过电源适配器供电才能使用烘干功能。

> **注意**：AMS 2 Pro 官方电源适配器规格为 24V 4A。为确保设备安全与正常使用，**请务必使用官方配件。使用第三方适配器可能会导致设备损坏，并影响保修权益**。

![连接电源适配器](https://wiki.bambulab.com/h2/manual/ams2pro/image-20.png)

- **状态指示**：  
  ▸ 未连接电源 → 页面右下角电源标识置灰，仅支持1台 AMS 2 Pro 从打印机取电烘干；  
  ▸ 已连接电源 → 页面右下角电源标识变绿。

![未连接电源](https://wiki.bambulab.com/h2/manual/ams2pro/image-21.png)

![已连接电源](https://wiki.bambulab.com/h2/manual/ams2pro/image-22.png)

- **干燥后其他耗材变形**：烘干高温耗材时需要将低温耗材取出，如烘干 ABS 时，AMS 中不能放置 PLA 耗材。
- 支持AMS远程烘干  
  现支持从软件“设备”页面发起AMS 2 PRO与AMS HT的烘干操作。

  - 点击对应AMS的“湿度”按钮，打开对应控制弹框。
  - 弹窗中**启动**或**停止**烘干来控制烘干，同时支持**边烘边打**。
  > ⚠️固件最低支持版本：**01.02.30.00**（H2D）

|  |  |
| --- | --- |
|  |  |

#### **烘干方法说明**

**方法一：旋转料盘烘干**

**做法**：从进料口中拔出耗材，并收纳至料盘；

**料盘转动规则**：每5分钟旋转30°，均匀烘干。

**方法二：静止烘干**

**不适用耗材：** 软化温度 ＜ 烘干温度的耗材（如 PLA、PVA、Support for PLA/PETG 和 TPU）；

**做法**：将耗材插入进料口；

**原理**：料盘固定，仅依赖热风循环。

![](https://wiki.bambulab.com/h2/manual/ams2pro/image-23.png)

#### 进出气口控制

**作用：**

AMS 2 Pro 新增了两个主动开关的进出气风门，烘干过程中 AMS 会打开进出气口，通过外循环排出湿气。

|  |  |
| --- | --- |
|  |  |

**工作逻辑：**

**不烘干状态：** 进出气口关闭，隔绝外部潮湿空气；

**开始烘干：** 进出气口开合一次，提示用户开始烘干，同时进行自检；

**烘干过程腔内温度小于目标值：** 进出气口关闭，快速提升腔温；

**烘干过程腔体温度达到目标值：** 进出气口打开，通过外循环排除腔体湿气；

**送料前检测：** AMS开始送料之前，如果测得腔温高于需要送料材料的软化温度，则会开启风扇冷却一段时间进行冷却，等到温度降下来，再开始送料。

| **内循环烘干** | **外循环排湿气** |
| --- | --- |
| 1.jpg =700x |  |

### 自动分组功能

在发起多色打印任务时，会自动分配最省料的双头打印方案。您也可以在发送打印任务的窗口里自定义选择耗材丝，具体可以参考： [双喷嘴打印机耗材切片分组](../../software/bambu-studio/manual/dual-nozzles-slicing-filament-grouping.md)

## AMS工作流程

### **进料/退料操作**

**进料**：选择槽位 → 点击「进料」或发送打印任务，AMS 2 Pro会自动进料至挤出机。

**退料**：已进料槽位 → 点击「退料」即可自动退料。打印结束也会自动退料，但如果手动中止打印任务则不会自动退料。退料过程中，上下料器和内部助力电机同时工作，上下料器负责驱动料盘往回转，助力电机拉回耗材，直到耗材退到AMS内部。

![](https://wiki.bambulab.com/h2/manual/ams2pro/image-26.png)

![](https://wiki.bambulab.com/h2/manual/ams2pro/image-27.png)

### 发起多色打印任务

您可以参考 wiki 用 AMS 2 Pro 发起一个多色打印任务：[H2D Combo首次打印](../../h2/manual/h2d-first-print.md)

### 送料助力模式

打印时AMS根据缓冲区的信号来助力送料或者回抽（滑块位置反馈阻力状态）;

**AMS把料送至挤出机后就会切换到助力模式**，重启后恢复空闲状态。助力模式仅根据缓冲区的信号反馈来判断是否需要送料，与当前是否有打印任务无关。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南并未解决您的问题，[*请点击此处联系在线技术支持（服务时间 9:00-21:00）*](https://support.bambulab.cn/cn/im)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
