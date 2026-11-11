---
path: zh/h3c/manual/print-with-external-spool
title: "拓竹H3C 外挂进料指南"
description: ""
tags: []
created: 2026-11-03T12:12:36.555Z
updated: 2026-11-10T08:47:12.333Z
source: https://wiki.bambulab.com/zh/h3c/manual/print-with-external-spool
---

## 使用场景

**打印纤维增强耗材和 PLA glow 等表面粗糙的耗材**，从 AMS 上下料料嘴自动进料的阻力较大，且部分纤维增强耗材易脆断，打印风险较高，建议从外挂料盘进料。

> 连接 AMS 3H 后，打印机默认耗材来自 AMS 槽位，UI 界面将不显示外挂料盘的进料状态。因此，若需使用外挂料盘进料，请务必严格按照本文指引，通过‘手动进料’程序进行操作
>
> ![001.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/print-with-external-spool/zh/001.png)

## 所需配件

使用拓竹H3C 外挂进料所需的配件如下：

![002.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/print-with-external-spool/zh/002.png)

| **名称** | **备注** |
| --- | --- |
| **①料管** | 约 450 mm  建议[另购 PTFE 料管裁剪使用](../../filament-acc/acc/ptfe-tube.md)。 工具盒内附赠的 FEP 料管为工具头专用，直接用于长距离送料阻力较大，有卡料风险。 |
| **②料盘支架接头** | 工具盒中 |
| **③料盘支架** | 从机器屏幕的 **“机内存储”** 中打印： Image |

## 进料前准备

1. 组装料盘支架；

> 组装方向可根据需使用的打印头位置进行调整。

![004.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/print-with-external-spool/zh/004.png)

2. 从配件盒里取出料盘支架接头和螺丝，将螺丝放进接头中；

![005.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/print-with-external-spool/zh/005.png)

3. 将接头安装到料盘支架上，使用 H2.0 内六角扳手拧紧螺丝；

|  |  |
| --- | --- |
| 006.png | 007.png |

4. 安装料管；

![008.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/print-with-external-spool/zh/008.png)

5. 将料盘支架滑入打印机背部的料盘支架底座；

|  |  |
| --- | --- |
| 009.png | 010.png |

## 进料步骤

请暂勿直接将耗材送入打印头，按后续进料指引程序的提示步骤操作。

### 步骤 1. 设置耗材信息

1. 在打印机屏幕，进入 **①“耗材”** 页面，**点击“②… > ③手动进料”**；

![011.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/print-with-external-spool/zh/011.png)

2. 选定**④“1 号槽位”**，再点击**⑤“编辑耗材”**；

![012.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/print-with-external-spool/zh/012.png)

3. **⑥设置耗材类型及颜色**后，点击**⑦“进料”**。

![013.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/print-with-external-spool/zh/013.png)

### 步骤 2. 手动进料

1. **待屏幕提示“送出新耗材到挤出机”时**，开始手动进料；

![014.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/print-with-external-spool/zh/014.png)

> **注意**：如果打印头已通过 AMS 进料，则需根据屏幕提示手动抽回 AMS 中的耗材，再送入新耗材。
>
> ![015.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/print-with-external-spool/zh/015.png)

2. 移除 AMS 左侧板；

![016.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/print-with-external-spool/zh/016.png)

3. 按压 1 号打印头气动接头，移除后半部分料管；

![017.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/print-with-external-spool/zh/017.png)

4. 将外挂支架料管另一端穿过 AMS 背板上的孔洞插入料管接头的黑色外圈；

![018.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/print-with-external-spool/zh/018.png)

连接 1 号打印头气动接头；

![019.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/print-with-external-spool/zh/019.png)

> **注**：除1号打印头外，其他打印头也可使用外挂料盘打印，再从料管架上的缓冲滑块处断开料管，再连接外挂料管。若您在按压气动接头以断开料管的操作中感到困难，建议提前移除 AMS 舱体（参考 wiki：[AMS 舱体移除与安装指南](../maintenance/replace-chamber.md)。
>
> ![020.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/print-with-external-spool/zh/020.png)

5. 放置耗材，并将耗材末端插入料盘支架接头，向前推送，直至无法推动为止，屏幕将显示“咬入新耗材”。

|  |  |
| --- | --- |
| 021.png | 022.png |

## 进料异常排查

正常进料后，耗材从打印头顶部向下进入热端，此时可从挤出轮视窗观察到耗材，并能观察到喷嘴处耗材顺畅挤出。

|  |  |
| --- | --- |
| 023.png | 024.png |

若耗材进料状态异常，**请先区分是否通过屏幕“手动进料”进行进料**，再按以下情况进行排查。

![025.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/print-with-external-spool/zh/025.png)

### 未通过屏幕“手动进料”

#### 情况 1：屏幕提示检查进料状态

- **现象：** 屏幕出现“请检查当前的进料状态”提示；

![026.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/print-with-external-spool/zh/026.png)

- **原因：**

1. 使用 TPU 直通口或外挂料盘打印时，不通过屏幕“手动进料”流程，直接将耗材插入打印头，会弹此框；
2. AMS 3H 离线，不通过屏幕“手动进料”流程，直接将耗材插入打印头时，会弹此框。

- **解决方法**：将耗材从打印头中拉出后，在屏幕点击\*\*“... > 手动进料”\*\*，再根据屏幕上的进料流程进行送料。

![027.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/print-with-external-spool/zh/027.png)

#### 情况 2：耗材显示有误

- **现象：** 手动进料后，屏幕未显示正确的外挂耗材信息，而显示 AMS 内的耗材信息；
- **可能原因**：AMS 在线且目标打印头对应的 AMS 槽位内有耗材，此时直接从背板或 AMS 耗材直通口手动插入耗材到打印头，未经屏幕“手动进料”流程，机器会将耗材识别为 AMS 耗材而非外挂耗材。
- **解决方法：**将耗材从打印头中拉出后，在屏幕点击**“... > 手动进料”**，再根据屏幕上的进料流程进行送料。

![028.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/print-with-external-spool/zh/028.png)

### 通过屏幕“手动进料”

#### **情况 1：耗材路径偏移**

- **现象：** 耗材无法顺利进入热端，脱离路径；

![029.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/print-with-external-spool/zh/029.png)

- **原因：** 在屏幕提示手动送料（下图步骤③）之前，就将耗材送入打印头，且耗材路径偏移，无法被挤出轮咬合。

![030.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/print-with-external-spool/zh/030.png)

- **解决方法：** 将耗材从打印头中拉出后，在屏幕点击 **“... > 手动进料”**，再根据屏幕上的进料流程进行送料，这是因为当屏幕提示手动送料（步骤③）时，代表打印头已成功抓取。此时前推耗材路径精准不偏移，可被挤出轮顺利咬合。

![031.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/print-with-external-spool/zh/031.png)

#### **情况 2：打印头内有残留耗材**

- **现象：** 手动送入耗材后，打印头内仍有残留耗材，导致新耗材无法进料；

![032.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/print-with-external-spool/zh/032.png)

- **原因：** 在屏幕提示手动送料后将耗材送入打印头，但由于打印头内有残留耗材，**且残留耗材熔化温度高于当前耗材**，导致当前耗材无法正常进入挤出轮。
- **解决方法：**

**方法一：** 先停止进料，将打印头重新放回挂架；

![033.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/print-with-external-spool/zh/033.png)

待热端冷却后，用钳子将残留耗材夹出，再放回打印头，重新进料。

![034.gif](https://public-cdn.bblmw.com/wiki/new/h3c/manual/print-with-external-spool/zh/034.gif)

**方法二：在屏幕上操作** 将工具头夹持对应的打印头，并选择以下两种方式之一送入新耗材：

1. **AMS 路径**：当 AMS 槽位处于空挡时，从 AMS 上下料口手动推入新耗材至挤出轮处；
2. **直插路径**：断开工具头上方的打印头气动接头（建议在工具头取用打印头前先断开打印头接头，再执行取用操作），随后直接将新耗材插入

①将热端温度设置为略高于打印头残余旧耗材要求的温度，再②点击屏幕上的\*\*“向下（挤出）”\*\*按钮，利用新耗材推出旧耗材。

![035.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/print-with-external-spool/zh/035.png)

## 退料步骤

1. 在屏幕上点击**退料；**

![036.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/print-with-external-spool/zh/036.png)

2. 当打印机提示“抽回当前耗材”时，旋转料盘，拉回耗材；

|  |  |
| --- | --- |
| 037.png | 038.png |

并将其插入料盘上的孔洞固定，完成退料。

![039.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/print-with-external-spool/zh/039.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
