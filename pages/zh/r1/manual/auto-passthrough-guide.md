---
path: zh/r1/manual/auto-passthrough-guide
title: "R1 滚轮送料加工指南"
description: "本文介绍了如何进行 R1 滚轮送料加工"
tags: []
created: 2026-09-22T12:48:37.324Z
updated: 2026-09-22T12:48:38.591Z
source: https://wiki.bambulab.com/zh/r1/manual/auto-passthrough-guide
---

## 滚轮送料加工介绍

滚轮送料加工是 R1 的一项进阶功能，需搭配**增高底座与滚轮送料系统**使用，常用于长条木板、亚克力板等板材的雕刻与切割加工。增高底座将设备垫高，提供更充足的加工空间并承托长板材；滚轮送料系统通过滚轮带动板材沿送料方向前后移动，突破单次加工的长度限制，实现超出常规幅面的长料/大幅面加工。

![001.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/auto-passthrough-guide/zh/001.png)

滚轮送料系统包含两个加工物边缘探测器，用于检测板材（加工物）的两端边缘，确认板材已正确摆放、覆盖到位并被稳定压紧，从而保证测长、测距、分段拍照和拍图结果准确可靠。

|  |  |
| --- | --- |
| 002.png | 003.png |

## 加工材料要求与范围限制

### 尺寸与形状

- 板材需平整，**无明显翘曲、起拱或扭曲**，否则影响拍图、测距与加工精度；
- 板材尺寸需落在可加工范围内（见下“加工范围限制”）；
- 板材宽度需适配送料槽口，避免过宽无法送入或过窄导致夹持不稳、滚轮空转。

### 材质

- **支持常见的不透明平整板材**（如木板、不透明亚克力等）；
- **不支持黑色材料**（黑色会吸收红外光线导致边缘传感器无法检测到材料）；
- **不建议吸光和高透材料**；在材质上我们对吸光和高透的耗材感知不够明显，因此不建议使用类似耗材，但透明亚克力除外。

### 材料长度

机器支持雕刻材料的最大长度取决于是否使用延长导轨（下图右框）及延长导轨数量。

![004.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/auto-passthrough-guide/zh/004.png)

> 以下为各种情况下可加工的材料长度信息，仅供参考。

- **仅使用送料导轨，不使用延长导轨**：450 mm＜长度＜ 1500 mm

![image34.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/auto-passthrough-guide/zh/image34.png)

- **使用送料导轨和 1 套延长导轨**：450 mm＜长度＜ 2000 mm

![image34.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/auto-passthrough-guide/zh/image35.png)

- **使用送料导轨和 2 套延长导轨**：450 mm＜长度＜ 2500 mm
- **使用送料导轨和 3 套延长导轨**：450 mm＜长度＜ 3000 mm

> **注意：**
>
> - 无论使用多少套延长导轨（建议最多不超过 3 套），材料长度不得超过导轨 + 机器总长外 200 mm。
> - 单机最长可加工长度为 300 mm，安装滚轮送料系统后最短可加工长度为 450 mm（参考下图）；因此，如需加工 **300 ~ 450 mm** 长度的材料，建议将其粘在长木板上辅助加工。
>
> ![005.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/auto-passthrough-guide/zh/005.png)

### 加工范围限制

- **可加工长度**：最短为 **450 mm**；自动测量上限为 **3000 mm**，超过 3000 mm 的材料仍可加工，但需手动输入长度；实际可加工长度会因板材两端被滚轮压住而在前后各预留一小段：**上区域 110 mm，下区域 25 mm**，因此实际可加工长度略小于板材实际长度；
- **可加工宽度**：最宽约 600 mm，最窄约 300 mm；

![006.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/auto-passthrough-guide/zh/006.png)

- **可加工厚度**：结构兼容的最大厚度为 **20mm**；最小厚度无硬性限制，但不建议小于 **3 mm**，过薄/过窄的板材可能无法覆盖全部滚轮，或无法检测是否被压紧；板材厚度在 3 mm 以上时，宽度无特殊限制。

> 注意：具体数值请以设备屏幕与 Bambu Suite 中的提示为准。

- **加工预留空间：** 加工时，材料会在机器内部前后快速移动，请确保机器前方至少预留 **材料长度 - 400 mm**、后方至少预留 **材料长度 - 550 mm** 的禁入区域，以免妨碍机器加工或导致人员受伤。

## 加工流程

### 加工前准备

为获得更高的测量精度，加工前请点击屏幕：**“设置 > 校准 > 滚轮送料校准”**，完成校准。

|  |  |
| --- | --- |
| 007.png | 008.png |

### 安装配件

#### **滚轮送料系统**

关于安装滚轮送料系统的具体步骤请参考：[滚轮送料系统开箱指南](conveyor-unboxing.md)。

#### **延长导轨**

- 将送料导轨和延长导轨的螺丝分别对准支架内侧的两个孔位；

![009.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/auto-passthrough-guide/zh/009.png)

- 依次锁紧螺丝；

![010.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/auto-passthrough-guide/zh/010.png)

- 按此方法依次安装延长导轨；安装至最后一根延长导轨时，需将螺丝对准支架的两个外侧孔位；

![011.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/auto-passthrough-guide/zh/011.png)

- 锁紧螺丝后，即可完成安装。

![012.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/auto-passthrough-guide/zh/012.png)

### 放置材料

1. 打开上盖，将板材从前门方向对准滚轮送料系统的送料槽口，向内插入；

> **注意**：**请勿从机器后方进料！**

![013.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/auto-passthrough-guide/zh/013.png)

2. 参考前门与内部后侧的引导线，确认板材摆放位置与角度在允许范围内，且同时盖住前后两个加工物边缘探测器（下图虚线处）。

> 注意：板材摆放过斜或超出边界过多，可能在送料过程中撞到边框，导致电机堵转卡住。

|  |  |
| --- | --- |
| 014.png | 015.png |

### Bambu Suite 操作

1. 在 Bambu Suite 中打开或新建项目；

![016.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/auto-passthrough-guide/zh/016.png)

2. 点击“准备制作”，进入摆盘页面；

![017.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/auto-passthrough-guide/zh/017.png)

3. 在右侧“加工模式”中选择“滚轮送料加工”；

![018.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/auto-passthrough-guide/zh/018.png)

4. 选择所用的材料类型；

![019.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/auto-passthrough-guide/zh/019.png)

5. 点击 **“一键准备”** 按钮，设备将自动送料，并测长、测距、分段拍照；

![020.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/auto-passthrough-guide/zh/020.png)

> 注意：板材最前端有一小段在进入拍照区前已越过，无法被拍到，属正常现象。

![021.webp](https://public-cdn.bblmw.com/wiki/new/r1/manual/auto-passthrough-guide/zh/021.webp)

6. 拍图完成后，suite 在画布上按打印台实际尺寸显示可加工的板材长图，并显示测量的板材长度和距离；

![auto-passthrough-1.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/auto-passthrough-guide/zh/auto-passthrough-1.png)

> 注意：拍照/拍图完成后，**请勿移动设备内板材**；若发生上述操作，请重新拍照测量后再加工。

7. 此时可在长图上摆放并调整图案，将其拖动到目标加工区域，并设置加工参数；

![auto-passthrough-1.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/auto-passthrough-guide/zh/auto-passthrough-2.png)

8. 确认完毕后，点击“制作”按钮。

![024.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/auto-passthrough-guide/zh/024.png)

#### 快速测长和选点测距（可选）

除“一键准备”外，还可使用“快速测长”和“选点测距”功能，适用于**俯视摄像头拍照异常**的场景。

- **快速测长：** 点击“快速测长”按钮，机器会自动开始测长，具体介绍请参考：[快速测长介绍](roller-feed-processing-quick-length-measurement.md)。

|  |  |
| --- | --- |
| 025.png | 026.png |

- **选点测距：** 在拼好的长图上选中板材的某个具体位置，工具头会移动到该点上方，通过测距激光测量该处板材上表面高度，得出距离。测量完成后，厚度值自动回填到软件，设备复位以支持下一次测量。

|  |  |
| --- | --- |
| 027.png | 028.png |

> 注意：
>
> - 请尽量将测量点选在板材表面平整、无异物、无孔洞的位置，避免选在板材边缘，以提高测量成功率与准确；
> - 加工物边缘探测器应避免阳光直射，以免引起误检测；
> - 透明或强反光材质可能导致测距异常，此类材质请谨慎确认结果或改为手动输入；
> - 如果待加工材料长度超过 3000 mm，则无法进行自动测长，需手动输入长度。

此外，suite 也支持**手动输入长度和距离**，但传感器不会复核输入值是否准确，**请自行测量并填写准确数值。**

### 加工后操作

加工完成后，在 Bambu Suite 中点击“松开”按钮，待滚轮抬起后，即可取出板材。

> 注意：
>
> - 只有在**未发起加工或加工完成后**才能松开板材；
> - 若滚轮原本已处于松开状态，则不会重复动作。

![029.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/auto-passthrough-guide/zh/029.png)

## 异常排查

### 测量或拍图失败

1. 检查前盖是否已按提示打开；
2. 检查板材是否正确压紧、是否盖住前后两个加工物边缘探测器；
3. 检查加工物边缘探测器是否脏污或被遮挡；
4. 机器下方（前门加工物边缘探测器上方）遮光脚垫未安装或者脱落；

![030.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/auto-passthrough-guide/zh/030.png)

5. 检查板材是否平整、摆放是否对齐引导线；

### 送料过程中电机堵转/卡住

1. 检查板材摆放是否过斜或超界，重新对齐引导线；
2. 检查送料通道及边框是否有异物或卡阻；
3. 确认板材宽度是否适配送料槽口。

### 拍图或加工出现错位/重影

1. 检查拍照后是否移动过板材；
2. 检查板材在送料过程中是否打滑、松动或偏移；
3. 确认板材已稳定压紧，加工环境无明显震动;
4. 如果材料本身存在高低起伏，会导致拍图出现错位/重影。

### 第一次测量成功、第二次失败

多为板材在两次测量之间发生了小幅移动，导致某一端加工物边缘探测器检测不到板材边缘。

请重新摆正板材，并确保两端边缘充分覆盖探测器后重试。

### 材料头尾区域无法被加工

由于板材两端需被滚轮压住，因此板材上区域 110 mm 和下区域 25 mm 为不可加工区域，是正常现象。

### 加工精度存在误差

发起任务前，机器会通过加工物上边缘探测器定位木板上边缘，并将其作为加工原点。由于探测器每次测量都存在轻微偏差，不同任务之间的定位会略有差异。因此，若需在同一位置进行叠加雕刻，请勿拆分成多次任务先后完成，而应将其合并为一次任务一次性雕刻，以避免多次定位带来的位置偏差。

如果单次加工的实际位置与预览摆放位置偏差过大，通常是探测器误检所致，请按以下步骤依次排查：

- 将 Suite 和固件更新至最新版本；
- 若问题仍未解决，请检查加工材料是否满足上述材料要求与范围限制。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
