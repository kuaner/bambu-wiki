---
path: zh/ams-ht/Intr-to-ams-ht-workflow-and-features
title: "AMS HT工作流程和功能介绍"
description: ""
tags: []
created: 2025-03-28T12:12:34.658Z
updated: 2026-03-31T01:38:49.363Z
source: https://wiki.bambulab.com/zh/ams-ht/Intr-to-ams-ht-workflow-and-features
---

## **AMS 初始化设置**

当首次连接 AMS HT 到 H2D 打印机时，需要进行一次初始化。因为H2D配有双挤出机，这一步的目的是检测AMS连接到了哪一侧的挤出机。在“耗材”——“AMS 初始化”中，可选择自动模式或手动模式开启 AMS 初始化。

|  |  |
| --- | --- |

### **自动模式**

进入打印机屏幕「耗材」→「AMS初始化」→ 选择「自动模式」；

系统自动检测 AMS 连接的挤出机侧（左/右）。

**注意事项**：

AMS HT 内需插入一卷耗材；

已进料的耗材需提前退料；

确保缓冲器内部无残留耗材丝（避免断料残留在内部）。

**工作原理**：  
AMS 将耗材送至挤出机，左右挤出机各有一个霍尔传感器，通过霍尔传感器触发信号来判断AMS所配对的挤出机。

![](https://wiki.bambulab.com/h2/manual/intr-to-ams-ht-workflow-and-features/zh2/image-2.png)

### **手动模式**

**适用场景**：AMS中无耗材时，手动调整 AMS 与挤出机的配对关系。  
**操作步骤**：

进入「耗材」→「AMS初始化」→「手动模式」；

手动指定 AMS 连接的挤出机侧（左/右）。

![](https://wiki.bambulab.com/h2/manual/intr-to-ams-ht-workflow-and-features/zh2/image-3.png)

**限制条件**：

- 若 AMS 已进料至挤出机，则该 AMS 图标为灰色，并且无法修改配对关系。

![](https://wiki.bambulab.com/h2/manual/intr-to-ams-ht-workflow-and-features/zh2/image-4.png)

## AMS功能

### 预上料

**作用：** 绷紧耗材丝，避免料盘上的耗材松散，并提供插料时的交互反馈。

**触发方式**：在AMS HT在空闲状态的时候，插入耗材至进料口 → 自动预上料（助力电机送料至AMS 尾部霍尔传感器后往回拉）。

**插入辅助功能**：点击空槽图标 → 内部助力电机开始转动，可用于辅助插料。

### 读取RFID

**模式设置**：

你可以在屏幕的**设置——AMS选项**里对自动读取RFID功能进行相关设置。

**插入时读取**：插料后自动读取RFID；

**开机时读取**：重启AMS后自动读取已插入的耗材的RFID信息；

![](https://wiki.bambulab.com/h2/manual/intr-to-ams-ht-workflow-and-features/zh2/image-5.png)

- **手动读取**：点击槽位 →「重读」，即可重新读取该槽位的RFID。

![](https://wiki.bambulab.com/h2/manual/intr-to-ams-ht-workflow-and-features/zh2/image-6.png)

![](https://wiki.bambulab.com/h2/manual/intr-to-ams-ht-workflow-and-features/zh2/image-7.png)

### **剩余容量估算**

**工作原理：** 通过 RFID 标签转动一圈送出的耗材丝长度来估算余量（1kg 料卷默认为 100%）。若启用了剩余容量估计功能，则读取RFID的过程会进行两次，第一次读取耗材信息，第二次估算剩余容量。

**显示位置**：槽位上方耗材名称下的横条显示了耗材大致剩余的容量。

![](https://wiki.bambulab.com/h2/manual/intr-to-ams-ht-workflow-and-features/zh2/image-8.png)

### **AMS 排序与连接**

**默认排序逻辑**：每台AMS都会被分配一个顺序并显示在屏幕上。通过6pin线直连打印机为 AMS A，级联依次为 B、C、D；

**手动重置**：点击「重置」→ 按需重新连接 AMS。

![](https://wiki.bambulab.com/h2/manual/intr-to-ams-ht-workflow-and-features/zh2/image-9.png)

### AMS**自动续料**

**启用条件**：

耗材属性完全一致（品牌、类型、颜色）即可以形成续料关系。

耗材需位于同一挤出机连接的 AMS（左对左，右对右）。

![](https://wiki.bambulab.com/h2/manual/intr-to-ams-ht-workflow-and-features/zh2/image-10.png)

**操作路径**：

- 「设置」→「AMS选项」→ 选择「AMS自动续料」来启用自动续料功能。

![](https://wiki.bambulab.com/h2/manual/intr-to-ams-ht-workflow-and-features/zh2/image-11.png)

- 「耗材」→「自动续料」→ 分左右挤出机页面查看续料关系。

![image-112.png](https://wiki.bambulab.com/h2/manual/intr-to-ams-ht-workflow-and-features/zh2/image-112.png)

### **耗材烘干功能**

#### 功能概述

- **硬件配置**：AMS HT 内置加热烘干模块（位于中框下方），**最高烘干温度 85°C；**

![](https://wiki.bambulab.com/h2/manual/intr-to-ams-ht-workflow-and-features/zh2/image-12.png)

- **适用场景**：如果耗材受潮了，可使用烘干功能将其烘干。所有耗材均可使用AMS来烘干，但部分需高温烘干的材料可能无法完全干燥，例如 PPS，PPA。

![](https://wiki.bambulab.com/h2/manual/intr-to-ams-ht-workflow-and-features/zh2/image-13.png)

#### **操作指南**

**烘干流程**：

关闭 AMS HT 上盖 → 进入「烘干和湿度」页面；

选择所需烘干的耗材 → 设置温度与时长 → 启动烘干。连接多台 AMS 时，可以通过「耗材」页面逐一切换设备启动烘干，或在烘干页面左上角切换 AMS 设备。

![](https://wiki.bambulab.com/h2/manual/intr-to-ams-ht-workflow-and-features/zh2/image-15.png)

#### **注意事项**

- **电源要求**：必须使用标配电源线独立供电 **（打印机无法为AMS HT的烘干功能供电）**；

![AMS HT 电源适配器连接示意图](https://wiki.bambulab.com/h2/manual/intr-to-ams-ht-workflow-and-features/zh2/image-16.png)

**状态指示**：

未连接电源 → 页面右下角电源标识置灰，无法启动烘干；

已连接电源 → 页面右下角电源标识变绿。

![未连接电源](https://wiki.bambulab.com/h2/manual/intr-to-ams-ht-workflow-and-features/zh2/image-17.png)

![已连接电源](https://wiki.bambulab.com/h2/manual/intr-to-ams-ht-workflow-and-features/zh2/image-18.png)

> 由于AMS HT内部体积较小，在使用AMS HT烘干含水量比较高的耗材（饱和吸水的PVA）时，若观察到冷凝水出现，请及时打开AMS HT上盖散出水汽，避免冷凝水导致硬件短路。

**支持AMS远程烘干**  
现支持从软件“设备”页面发起AMS 2 PRO与AMS HT的烘干操作。

- 点击对应AMS的“湿度”按钮，打开对应控制弹框。
- 弹窗中**启动**或**停止**烘干来控制烘干，同时支持**边烘边打**。

> ⚠️固件最低支持版本：**01.02.30.00**（H2D）

|  |  |
| --- | --- |
|  |  |

#### **烘干方法说明**

**模式一：旋转料盘烘干**

**做法**：从进料口中拔出耗材，并将其收纳至料盘；

**料盘转动规则**：每 5 分钟旋转 30°，均匀烘干。

**模式二：静止烘干**

\*\*不适用耗材：\*\*软化温度 ＜ 烘干温度的耗材（如 PLA、PVA、Support for PLA/PETG 和 TPU）；

**做法**：耗材插入进料口时启动；

**原理**：料盘固定，仅依赖热风循环，进行烘干。

![](https://wiki.bambulab.com/h2/manual/intr-to-ams-ht-workflow-and-features/zh2/image-19.png)

#### 进出气口控制

**作用：**

AMS HT新增了两个主动开关的进出气风门，烘干过程中 AMS 会打开进出气口，通过外循环排出湿气 。

![进气口](https://wiki.bambulab.com/h2/manual/intr-to-ams-ht-workflow-and-features/zh2/image-20.png)

![出气口](https://wiki.bambulab.com/h2/manual/intr-to-ams-ht-workflow-and-features/zh2/image-21.png)

**工作逻辑：**

**不烘干状态**：进出气口关闭，隔绝外部潮湿空气；

**开始烘干**：进出气口开合一次，提示用户开始烘干，同时进行自检；

**烘干过程腔内温度小于目标值**：进出气口关闭，快速提升腔温；

**烘干过程腔体温度达到目标值**：进出气口打开，通过外循环排除腔体湿气；

**送料前检测**：在AMS开始送料之前，如果测得腔温高于需要送料材料的软化温度，则会开启风扇冷却一段时间进行冷却，等到温度降下来，再开始送料。

| **内循环烘干** | **外循环排湿气** |
| --- | --- |
| 1645569a-9966-4c2b-a096-fea6c152c6d1.jpg |  |

### **湿度与温度监控**

AMS HT的烘干模块中有个传感器，可以用于检测AMS内部的湿度和温度。

![](https://wiki.bambulab.com/h2/manual/intr-to-ams-ht-workflow-and-features/zh2/image-23.png)

**查看路径**：「耗材」→ 点击 AMS 湿度图标 → 进入「烘干和湿度」页面；

**显示内容**：点击左上角的图标，可以切换不同设备，查看每台AMS的实时湿度、温度数据。

|  |  |
| --- | --- |

### 切片自动分组功能

在发起多色打印任务时，会自动分配最省料的双头打印方案。您也可以在发送打印任务的窗口里自定义选择耗材丝，具体可以参考： [双喷嘴打印机耗材切片分组](../software/bambu-studio/manual/dual-nozzles-slicing-filament-grouping.md)

## AMS工作流程

### **进料/退料操作**：

**进料**：选择槽位 → 点击「进料」或发送打印任务，AMS HT会自动进料至挤出机。

**退料**：已进料槽位 → 点击「退料」即可自动退料。打印结束也会自动退料，但如果手动中止打印任务则不会自动退料。退料过程中，退料回转组件电机和内部助力电机同时工作，退料回转组件负责驱动料盘往回转，助力电机拉回耗材，直到耗材退到AMS内部。

![](https://wiki.bambulab.com/h2/manual/intr-to-ams-ht-workflow-and-features/zh2/image-26.png)

![](https://wiki.bambulab.com/h2/manual/intr-to-ams-ht-workflow-and-features/zh2/image-27.png)

### 发起多色打印任务

您可以参考wiki用AMS HT发起一个多色打印任务： [H2D Combo首次打印](../h2/manual/h2d-first-print.md)

### 送料助力模式

打印时AMS根据缓冲区的信号来助力送料或者回抽（滑块位置反馈阻力状态）;

**AMS把料送至挤出机后就会切换到助力模式**，重启后恢复空闲状态。助力模式仅根据缓冲区的信号反馈来判断是否需要送料，与当前是否有打印任务无关。

## 灯语

AMS HT 灯语和 AMS 2 Pro 的类似，可将 AMS HT 看做 AMS 2 Pro 的其中一个槽。

|  |  |  |
| --- | --- | --- |
| 序号 | LED 灯 | AMS HT 状态 |
| **错误状态（红灯）** |  |  |
| 1 | 红灯双闪 | 1. 打印机没检测到 AMS，通信异常  2. 错误状态，且进料器和出料霍尔组件都检测到有料，可能是进料或者退料失败 |
| 2 | 红灯呼吸 | 1. 打印开始后进料器没有检测到料，插入料后即可恢复工正常  2. 烘干时状态异常  3. 空闲时烘干模块 NTC 掉线，或者检测到风道温度过高等异常，需要检测各部件是否插紧 |
| 3 | 红灯常亮 | 错误状态，进料器没检测到料但出料霍尔组件检测到料，可能是耗材丝断在出料霍尔组件内部 |
| 4 | 红灯单闪 | 错误状态，进料器检测到有料，出料霍尔组件没检测到料，通常是是进料失败，需要检查进料器是否工作 |
| **正常状态（白灯）** |  |  |
| 1 | 间隔点亮 | AMS 上电初始化的时候，隔 3 秒左右闪一次白灯 |
| 2 | 白灯常亮 | 1. AMS 上电初始化结束后，或者唤醒屏幕时槽里有料（唤醒屏幕会点亮有插入耗材的槽位）  2. 进行预上料、读取 RFID 或者正常打印过程中（包含进退料） |
| 3 | 白灯熄灭 | 1. 息屏后 15 分钟内该槽无预上料、读取 RFID 或打印（进退料）动作，白灯熄灭  2. 在预上料或者读取 RFID 时白灯会再次点亮,动作结束 10 秒后白灯熄灭  3. AMS 上电初始化结束后，20 分钟内无预上料、读取 RFID 或打印（进退料）动作，白灯熄灭 |
| 4 | 白灯呼吸 | 正常烘干状态 |

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)，点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
