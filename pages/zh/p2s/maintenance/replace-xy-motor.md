---
path: zh/p2s/maintenance/replace-xy-motor
title: "更换 P2S/X2D  XY 电机"
description: ""
tags: []
created: 2025-10-14T13:14:02.903Z
updated: 2026-04-30T06:09:06.153Z
source: https://wiki.bambulab.com/zh/p2s/maintenance/replace-xy-motor
---

## XY 电机

XY 电机是安装在打印机背部，用于驱动工具头完成 XY 方向移动的步进电机。左右各一个，为了方便区分，根据位置分别称为 A 电机、B 电机。  
![38-ab-motor.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-xy-motor/38-ab-motor.png)

## 何时更换

- 电机烧坏
- 售后人员通过 log 分析，确认是 XY 电机故障。

> 更换XY 电机后，需要重新对 XY 皮带进行张紧，具体的操作请查阅 [XY 皮带张紧](belt-tension.md) 。

## 需要的工具和材料

- H2.0 内六角扳手
- H1.5 内六角扳手（仅在更换 B 电机时需要使用）
- 镊子
- 新的 XY 电机  
  ![fac173.jpg](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/p2s-sku-pics/fam020.jpg)

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 更换 A 电机

### 移除 A 电机

#### 步骤 1：移除背板

您可以根据机型，参考对应 Wiki 来移除打印机背板：

- [P2S](replace-rear-panel.md)
- [X2D](../../x2d/maintenance/replace-rear-panel.md)

| rear_panel_screws_010.png | 背板螺丝.jpg |
| --- | --- |
| P2S | X2D |

#### 步骤 2：移除废料滑梯

使用 H1.5 内六角扳手移除四颗废料滑梯固定螺丝，将废料滑梯从打印机上取下。

![excess_purge_026.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-mc-and-ac-boards/excess_purge_026.png)

#### 步骤 3：松出 A 电机连接线

1. 从 MC 板上断开 A 电机连接线，从右往左依次将电机电缆从线扣和胶带中松脱出来；

![01_001.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-xy-motor/01_001.png)

![02_002.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-xy-motor/02_002.png)

2. 将胶布从线缆上撕开，将电机线缆分离。

![03_003.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-xy-motor/03_003.png)

#### 步骤 4：松出 XY 皮带张紧器

移除 A 电机这一侧的 XY 皮带张紧器。使用 H2.0 内六角扳手依次移除下图所示的 4 颗螺丝，将张紧器松开。注意：在拧张紧器支架螺丝时，请用手按住张紧器支架，避免张紧器支架弹开。

![04_004.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-xy-motor/04_004.png)

![05_005.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-xy-motor/05_005.png)

![06_006.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-xy-motor/06_006.png)

#### 步骤 5：移除 A 电机

1. A 电机由 4 颗螺丝固定，其中两颗明显可见，另外两颗需要用较长的 H2.0 内六角螺丝刀从上往下穿到螺丝位置。使用 H2.0 内六角扳手移除这四颗螺丝，在移除最后一颗螺丝时，请用手扶住电机，避免电机掉落；

![09_009.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-xy-motor/09_009.png)

2. 将皮带从电机主动轮上移除，取下 A 电机，并将电机连接线穿过小孔，即可取下电机。

![10_010.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-xy-motor/10_010.png)

![11_011.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-xy-motor/11_011.png)

### 安装 A 电机

#### 步骤 1：安装 A 电机

1. 将 A 电机线穿过穿线孔，用手托住电机，将皮带装到主动轮上。

![11_011.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-xy-motor/11_011.png)

![12_012.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-xy-motor/12_012.png)

2. 使用 H2.0 内六角扳手锁入固定电机的 4 颗螺丝。在锁入背面的两颗螺丝时，可以先将 H2.0 内六角扳手从上往下穿到螺丝孔位上方，然后使用镊子将螺丝放置在螺丝孔位中，然后将螺丝锁紧。

![09_009.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-xy-motor/09_009.png)

![13_013.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-xy-motor/13_013.png)

#### 步骤 2；安装 XY 皮带张紧器

将 XY 皮带张紧器重新装回，使用 H2.0 内六角扳手依次拧紧张紧器支架固定螺丝和张紧螺丝。

- 在拧螺丝时请用手扶住张紧器，避免张紧器弹出；

![07_007.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-xy-motor/07_007.png)

- 张紧螺丝无需完全拧紧，在后续张紧皮带后再拧紧该螺丝。

![08_008.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-xy-motor/08_008.png)

#### 步骤 3：连接 A 电机线缆

1. 用胶布将电机线和另外两根线缆粘在一起，然后从左往右依次将线缆扣入线扣中，并使用胶布将线缆贴在框架上（编号 4位置处）；

![03_003.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-xy-motor/03_003.png)

![02_002.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-xy-motor/02_002.png)

2. 最后将电机连接线与 MC 板连接。

![01_001.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-xy-motor/01_001.png)

#### 步骤 4：安装废料滑梯

将废料滑梯对准打印机上的螺丝孔位，使用 H1.5 内六角扳手依次拧紧四颗固定螺丝。

![excess_purge_026.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-mc-and-ac-boards/excess_purge_026.png)

#### 步骤 5：安装背板

您可以根据机型，参考对应 Wiki 来安装打印机背板：

- [P2S](replace-rear-panel.md)
- [X2D](../../x2d/maintenance/replace-rear-panel.md)

| rear_panel_screws_010.png | 背板螺丝.jpg |
| --- | --- |
| P2S | X2D |

## 更换 B 电机

### 移除 B 电机

#### 步骤 1：移除背板

您可以根据机型，参考对应 Wiki 来移除打印机背板：

- [P2S](replace-rear-panel.md)
- [X2D](../../x2d/maintenance/replace-rear-panel.md)

| rear_panel_screws_010.png | 背板螺丝.jpg |
| --- | --- |
| P2S | X2D |

#### 步骤 2：移除 AP 板盖

您可以参考这篇 Wiki 将 AP 板盖移除：[更换 P2S/X2D AP 板盖/LED 补光灯 - 左](replace-ap-board-cover-and-led-light-left.md)

#### 步骤 3：移除废料滑梯

使用 H1.5 内六角扳手移除四颗废料滑梯固定螺丝，将废料滑梯从打印机上取下。

![excess_purge_026.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-mc-and-ac-boards/excess_purge_026.png)

#### 步骤 4：松出 XY 皮带张紧器

1. 移除 B 电机一侧的 XY 皮带张紧器。先使用 H2.0 内六角扳手移除两颗张紧器固定螺丝，再使用 H2.0 内六角扳手移除张紧器支架固定螺丝。在移除张紧器支架固定螺丝时，请用手按住张紧器支架，避免张紧器支架弹开；

![15_015.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-xy-motor/15_015.png)

![16_016.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-xy-motor/16_016.png)

2. 按照张紧器支架，将张紧器支架先松开，再将其从打印机上取下；

![17_017.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-xy-motor/17_017.png)

![18_018.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-xy-motor/18_018.png)

3. 最后将张紧器从框架上抽出，挂在皮带上即可。

![19_019.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-xy-motor/19_019.png)

#### 步骤 5：移除 MC 板

您可以根据机型，参考对应 Wiki 来移除 MC 板：

- [P2S](replace-mc-and-ac-boards.md)
- [X2D](../../x2d/maintenance/replace-mc-board-and-the-cooling-fan.md)

在移除 MC 板时，您可以将 B 电机连接线从打印机内侧的线扣中取出。

![37_037.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-xy-motor/37_037.png)

#### 步骤 6：移除 B 电机

1. 先使用 H2.0 内六角扳手移除三颗内衬固定螺丝；

![20_020.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-xy-motor/20_020.png)

2. B 电机由 4 颗螺丝固定，其中两颗明显可见，另外两颗需要用较长的 H2.0 内六角螺丝刀从上往下穿到螺丝位置。先使用 H2.0 内六角扳手移除后侧两颗螺丝，当螺丝拧松后，可使用镊子夹住螺丝，将螺丝取下；

![21_021.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-xy-motor/21_021.png)

![22_022.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-xy-motor/22_022.png)

![23_023.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-xy-motor/23_023.png)

3. 然后使用 H2.0 内六角扳手移除前侧的两颗螺丝，在移除最后一颗螺丝时，请用手托住电机，避免电机掉落；

![24_024.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-xy-motor/24_024.png)

![14_014.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-xy-motor/14_014.png)

4. 将皮带从 B 电机主动轮上取下，并将电机线缆从线槽中抽出；

![25_025.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-xy-motor/25_025.png)

![26_026.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-xy-motor/26_026.png)

5. 将电机往下推动。由于电机底部被横梁挡住，您需要将内衬往打印机内侧推动，并将 B 电机斜着推下，以避开横梁。

![27_027.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-xy-motor/27_027.png)

![28_028.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-xy-motor/28_028.png)

### 安装 B 电机

#### 步骤 1：安装 B 电机

1. 将电机连接线从下往上穿过大线槽，再将线缆穿过左侧的小线槽；

![31_031.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-xy-motor/31_031.png)

2. 将电机线缆朝向右侧板，即参考下图所示的方向。将内衬往打印机机箱内部推，为电机穿过预留空间。然后将电机从下往上穿过内衬的小孔；

![32_032.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-xy-motor/32_032.png)

![33_033.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-xy-motor/33_033.png)

3. 将皮带套过电机主动轮，然后扶住电机，使用 H2.0 内六角扳手拧紧前面的两颗固定螺丝；

![34_034.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-xy-motor/34_034.png)

![35_035.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-xy-motor/35_035.png)

![24_024.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-xy-motor/24_024.png)

4. 将 H2.0 内六角扳手先穿过框架至螺丝孔位上方，然后使用镊子将螺丝送至螺丝孔位处，再将螺丝拧紧。背面这两颗螺丝均可参考相同的方法拧紧。

![22_022.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-xy-motor/22_022.png)

![21_021.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-xy-motor/21_021.png)

![23_023.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-xy-motor/23_023.png)

5. 使用 H2.0 内六角扳手拧紧 3 颗内衬固定螺丝

![20_020.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-xy-motor/20_020.png)

#### 步骤 2：安装 MC 板

您可以根据机型，参考对应 Wiki 来安装 MC 板：

- [P2S](replace-mc-and-ac-boards.md)
- [X2D](../../x2d/maintenance/replace-mc-board-and-the-cooling-fan.md)

在安装 MC 板时，您可以将电机线缆卡入打印机内侧的线扣中，并将线缆与 MC 板连接。

![37_037.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-xy-motor/37_037.png)

#### 步骤 3：安装 XY 皮带张紧器

将 XY 皮带张紧器重新装回，使用 H2.0 内六角扳手依次拧紧张紧器支架固定螺丝和张紧螺丝（张紧螺丝无需完全拧紧，在后续张紧皮带后再拧紧该螺丝）。

![18_018.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-xy-motor/18_018.png)

![16_016.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-xy-motor/16_016.png)

- 在拧螺丝时请用手扶住张紧器，避免张紧器弹出；

![15_015.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-xy-motor/15_015.png)

#### 步骤 4：安装废料滑梯

将废料滑梯对准打印机上的螺丝孔位，使用 H1.5 内六角扳手依次拧紧四颗固定螺丝。

![excess_purge_026.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-mc-and-ac-boards/excess_purge_026.png)

#### 步骤 5：安装打印机背板

您可以参考这篇 Wiki 将背板重新装回：[更换背板 | Bambu Lab Wiki](replace-rear-panel.md)

#### 步骤 6：安装 AP 板盖

您可以参考这篇 Wiki 将 AP 板盖重新装回：[更换 P2S/X2D AP 板盖/LED 补光灯 - 左](replace-ap-board-cover-and-led-light-left.md)

## 如何验证成功

连接电源，启动打印机，执行机器校准操作，确认是否有报错。

如果出现报错，请排查组装是否有问题，并重新张紧皮带后，再次运行设备自检。如果问题仍然存在，请联系 Bambu Lab 服务团队寻求进一步的帮助。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 为了确保您安全有效地进行操作，如果对指南中的任何步骤有疑虑或问题，请联系我们的客户服务团队，我们随时乐意为您解答疑问并提供支持。  
> [点击此处联系技术支持](https://support.bambulab.cn)
