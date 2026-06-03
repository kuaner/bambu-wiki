---
path: zh/h2/software/bambu-suite/manual/smart-detection-and-precise-control
title: "Bambu Suite机箱状态检测和交互功能"
description: ""
tags: []
created: 2025-03-26T03:38:00.399Z
updated: 2025-03-26T03:39:22.392Z
source: https://wiki.bambulab.com/zh/h2/software/bambu-suite/manual/smart-detection-and-precise-control
---

## **功能概述**

Bambu Suite 在加工全周期提供机器的状态感知，能够提供用户更加智能化的加工制作体验。

- **加工准备阶段**：实时显示垫板类型、材料信息、箱门状态，并推送安全检查提示；
- **智能参数匹配**：配合官方材料的 CodeSync 二维码，自动适配最佳加工参数；
- **制作执行阶段**：通过 Liveview 实时监控加工进度与设备状态。

## 机箱内状态展示

### **垫板类型检测与安全防护**

正确使用垫板是加工成功的基础，直接影响设备安全与成品质量。如果使用了错误的垫板，比如使用激光烧蚀刀切垫板，会损坏打印机并产生有毒有害气体。因此，让用户全面感知机箱内的状态就尤为重要。

当用户的项目所需要的垫板类型与机箱内的垫板类型不一致时，Bambu Suite会在多个地方进行提示，以便用户能够及时更换正确的垫板，成功制作项目。

#### 1. 逐盘标识和提示

准备页面右侧显示垫板状态图标，通常有以下几种提示类型：

- 机箱内放置的垫板错误，检测到垫板类型与项目不匹配。

![动画1.gif](https://wiki.bambulab.com/software/bambu-suite/manual/smart-detection-and-precise-control/%E5%8A%A8%E7%94%BB1.gif)

- 未检测出机箱内的垫板类型，可能是机箱门和上盖未关闭，或者垫板识别码被遮挡。

![image-5.png](https://wiki.bambulab.com/software/bambu-suite/manual/smart-detection-and-precise-control/image-5.png)

- 检测到机箱内未放置垫板。

![](https://wiki.bambulab.com/software/bambu-suite/manual/smart-detection-and-precise-control/image-7.png)

#### 2. **拍照后弹窗警告**

用户在Bambu Suite触发拍照功能时，若垫板类型不符 → 立即弹窗提示更换。

![动画2.gif](https://wiki.bambulab.com/software/bambu-suite/manual/smart-detection-and-precise-control/%E5%8A%A8%E7%94%BB2.gif)

#### 3. **任务发送前强制确认**

如果用户没有注意前面的信息，点击「制作」时软件会再次强化提醒用户更换正确的垫板。

![](https://wiki.bambulab.com/software/bambu-suite/manual/smart-detection-and-precise-control/image.png)

### **材料识别与匹配管理**

#### 1. 准备页面提示拍照

当Bambu Suite连接上打印机后，若检测到机箱内有材料，会主动提醒用户拍照，以便能正确放置加工图案到材料上。

![](https://wiki.bambulab.com/software/bambu-suite/manual/smart-detection-and-precise-control/image-1.png)

#### 2. 材料位置变化提示

- 如果用户更改了机箱内的材料或者调整了材料位置，Bambu Suite也会提醒用户之前拍照的照片已过期，需要重新拍照。

![](https://wiki.bambulab.com/software/bambu-suite/manual/smart-detection-and-precise-control/image-2.png)

- 当用户从机箱内取出材料时，Bambu Suite会提醒用户机箱内已经无材料，此时不可直接进行加工制作。

![](https://wiki.bambulab.com/software/bambu-suite/manual/smart-detection-and-precise-control/image-3.png)

#### 3. **材料信息提示**

##### 材料组右上角**状态标识说明**

当用户处于准备页面时，材料组的右上角会提示机箱内的材料信息或者状态以及当前的箱门状态。材料组右上角实时显示以下信息：

- **箱内已放置材料类型**（如白色卡纸）
- **箱门状态**（开/闭）
- **匹配状态标识**（不匹配/未知材料/未放置材料）

##### **材料识别与匹配流程**

**场景一：使用带CodeSync二维码的材料**

1. **自动识别**

   - 用户放置带CodeSync二维码的材料 → 打印机自动识别类型并同步至Bambu Suite。
2. **智能参数匹配**

   - 若机箱材料与项目所选不一致 → 右上角显示不匹配标识
   - 点击标识 → 选择切换为机箱内材料 → 系统自动调用本地材料库中相匹配的参数用于制作。

![动画3.gif](https://wiki.bambulab.com/software/bambu-suite/manual/smart-detection-and-precise-control/%E5%8A%A8%E7%94%BB3.gif)

**场景二：未知材料**

- 放置无二维码材料 → 显示对应的灰色标识
- **操作要求**：需要用户人工确认放置的材料和项目中选择的材料是否相匹配。

![](https://wiki.bambulab.com/software/bambu-suite/manual/smart-detection-and-precise-control/image-4.png)

**场景三：空箱检测**

- 机箱内没有检测到放置了材料时，Bambu Suite也会有相应的图标提示。

![](https://wiki.bambulab.com/software/bambu-suite/manual/smart-detection-and-precise-control/image-6.png)

##### **拍照后材料校验**

用户完成拍照定位后：

- 若机箱材料与项目设定不符 → 弹窗提示实际检测到的材料类型
- 用户可选择「使用」或「暂不使用」，使用后材料组将会自动切换至对应材料用于后续制作。

![动画4_(1).gif](https://wiki.bambulab.com/software/bambu-suite/manual/smart-detection-and-precise-control/%E5%8A%A8%E7%94%BB4_(1).gif)

### **制作阶段实时监控（Liveview）**

在制作阶段，可通过实时监控（liveview）查看当前打印任务状态，用户可以对加工状态和进度一目了然。

![动画6.gif](https://wiki.bambulab.com/software/bambu-suite/manual/smart-detection-and-precise-control/%E5%8A%A8%E7%94%BB6.gif)
