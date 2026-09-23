---
path: zh/r1/manual/laser-alignment-guide
title: "R1 光路校准介绍"
description: "本文介绍了如何对 R1 进行光路校准"
tags: []
created: 2026-09-22T13:29:08.515Z
updated: 2026-09-22T13:29:09.771Z
source: https://wiki.bambulab.com/zh/r1/manual/laser-alignment-guide
---

## 为什么需要调光？

R1 使用二氧化碳激光器，激光并非直接照射到材料上，而是从激光管射出后，经过多面反射镜依次反射，最终通过聚焦镜汇聚到材料表面，完成切割、雕刻等加工。R1 打印机共有 **M1、M2、M3** 三个反射镜，位置如下图所示；其中，M1 和 M2 镜架上各有两个电机驱动旋钮，用于自动调整反射镜角度。

**激光光路顺序为：**  
激光玻璃管 → 第一反射镜 → 第二反射镜 → 第三反射镜（工具头内）→ 聚焦透镜 → 加工件。

![001.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/laser-alignment-guide/zh/001.png)

如果这些镜片的角度存在微小偏差，激光路径就会发生偏移，可能导致以下后果：

- **出射功率下降：** 切不透、切割力度不足；
- **加工位置偏移：** 雕刻/切割不准，精度下降；
- **光斑变形：** 激光光斑不圆，边缘毛糙；
- **区域不一致：** 工作区不同位置加工效果不一致，近端较好、远端较差；
- **安全隐患：** 最严重时，远处激光被完全截断、无法出光，可能引发安全风险。

因此，当出现上述问题时，需要通过光路校准对激光光路进行重新校正。光路校准的目的是使激光稳定、居中地汇聚到目标位置。本机器提供两种校准方式：**自动光路校准**和**手动光路校准**。

| 方式 | 具体操作 | 适用场景 | 耗时 |
| --- | --- | --- | --- |
| **自动光路校准（优先）** | 机器自动测量、调节、校准与检查 | 配有**光路校准传感器**时 | 3~5 分钟 |
| **手动光路校准** | 用户参考本教程进行操作 | 光斑位置传感器丢失/故障；镜架电动旋钮故障；光斑偏离过多、超出探测区域 | 15~30 分钟 |

## 何时需要进行光路校准？

- 首次使用机器时；
- 搬运、撞击或剧烈振动机器后；
- 更换激光管、镜片等部件后；
- 切割/雕刻效果明显变差时；
- **定期维护：** 建议每月调节一次，以保持最佳加工性能。

## 自动光路校准

### 步骤 1. 进入功能

在机器屏幕上进入“设置”页面，点击：校准 > 自动光路校准；

> 首次开机时可能会出现引导提示，按引导操作即可。

![003.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/laser-alignment-guide/zh/003.png)

### 步骤 2. 阅读提示并开始

- 根据提示，在工具头入光孔处安装光路校准传感器；

![004.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/laser-alignment-guide/zh/004.png)

- 确保工作台已清空后，关闭上盖；

![005.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/laser-alignment-guide/zh/005.png)

- 点击“开始”，并按下机器“启停按钮”；

![006.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/laser-alignment-guide/zh/006.png)

### 步骤 3. 等待机器自动完成

调光过程中，机器会自动检测多个位置，以确保整个工作区的光路均已对准，而非仅校准单个角落。

![007.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/laser-alignment-guide/zh/007.png)

> 该过程包含多个阶段，请耐心等待，**期间请勿触碰机器**。

| **机器动作** | **动作含义** |
| --- | --- |
| 激光头开始移动 | 准备校准 |
| 激光头在工作区多个位置停下 | 在多个点位检测光路 |
| 偶尔出现短暂的激光闪烁 | 正在测量光斑偏移方位 |
| 激光头回到原位 | 校准完成 |

校准结束后，若屏幕显示"校准完成"，即表示校准成功，可放心使用机器；若校准失败，请根据屏幕提示进行排查。

![calibration-complete.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/laser-alignment-guide/zh/calibration-complete.png)

## 手动校准

当自动光路校准的光路偏移太多导致调光失败时，您可从“自动光路校准”页面底部进入“免工具手动校准”，阅读指引后进行手动校准，确保光路经过反射后能打在入光孔内部。

![009.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/laser-alignment-guide/zh/009.png)

### 校准位置

为保证校准精度，需确保激光经反射后能准确射入下一级反射镜的入光孔。手动校准请**按顺序完成以下 4 个位置**的校准：

| **顺序** | **反光镜（屏幕选择）** | **工具头位置** | 备注 |
| --- | --- | --- | --- |
| 1 | M1 | 机舱左上角 | 此时 M1-M2 距离最短 |
| 2 | M1 | 机舱左下角 | 此时 M1-M2 距离最长 |
| 3 | M2 | 从机舱左下角（位置 2 ）向右移动一段距离 | 移动约 10~15 cm |
| 4 | M2 | 机舱右下角 | 此时 M2-M3 距离最长 |

![010.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/laser-alignment-guide/zh/010.png)

### 校准流程

**每个位置的校准动作相同**，请按以下流程操作：

1. 在工具头入光孔上贴一小块美纹纸，需完全覆盖孔位；为了方便观察激光痕迹，可将美纹纸贴紧入光孔；

> 为避免痕迹重叠影响判断，**每次出光前都需更换美纹纸**。

![011.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/laser-alignment-guide/zh/011.png)

2. 在屏幕上选择 **M1** 或 **M2**，点击屏幕“出光”按钮；

![012.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/laser-alignment-guide/zh/012.png)

3. 按下机器“启停按钮”；

![013.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/laser-alignment-guide/zh/013.png)

4. 关闭上盖，等待出光完成；

![014.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/laser-alignment-guide/zh/014.png)

5. 几秒后，打开上盖；

![015.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/laser-alignment-guide/zh/015.png)

查看激光痕迹是否位于入光孔**中心**区域：

- **居中** → 将工具头移至下一个位置进行校准；

![016.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/laser-alignment-guide/zh/016.png)

- **偏移** → 按下方“手动调整”操作后重新校准。

![017.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/laser-alignment-guide/zh/017.png)

### 手动调整方法

- 根据激光痕迹的偏移方向，在屏幕转轴上点击**相反方向**按钮进行微调。例如，痕迹偏右，则点击转轴 **“-H”**（左）按钮进行微调；

![018.png](https://public-cdn.bblmw.com/wiki/new/r1/manual/laser-alignment-guide/zh/018.png)

- 重新执行手动校准流程，直至痕迹居中。

## 注意事项

### **安全须知**

- 调光前请认真阅读[《激光使用安全指南》](laser-important-info.md)及相关教程；
- 激光会伤害眼睛和皮肤，**切勿直视激光或将手伸入工作区**；
- 按要求佩戴防护眼镜，并关好舱盖；
- 工作台上请勿放置易燃物（如纸张、布料、木屑等）；
- 一旦闻到异味、看到冒烟或听到异响，请立即急停并断电检查，或联系售后；
- 儿童如果在场，须由成年人全程看护。

### **操作建议**

- 调光前请清空并擦净工作台；
- 建议优先完整运行自动调光；
- 手动调光时务必小步微调；
- 请勿自行拆卸或拧动镜片支架上的固定螺丝（除非售后指导）；
- 镜片若有灰尘或油污会影响调光效果，请按说明书方法轻柔清洁。

## 常见故障及处理方法

| **屏幕提示/现象** | **可能的问题** | **处理方法** |
| --- | --- | --- |
| 检测不到信号 / 传感器异常 | 检测部件未安装到位或表面脏污 | 卸下光斑位置传感器，清洁表面及 pogo pin 引脚后重新安装；仍无效请联系售后 |
| 光斑偏差过大 / 超出范围 | 光路偏移过多，自动调光无法检测 | 检查镜片是否明显松动或脏污；若无异常，先手动将光斑调至大致孔位附近，再执行自动调光 |
| 出现异味 / 冒烟 / 异响 | 存在安全风险 | 立即急停并断电，请勿继续操作，并联系售后 |

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
