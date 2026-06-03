---
path: zh/p2s/maintenance/replace-z-motor
title: "更换 P2S/X2D  Z 电机"
description: ""
tags: []
created: 2025-10-14T13:12:22.532Z
updated: 2026-04-30T06:39:07.490Z
source: https://wiki.bambulab.com/zh/p2s/maintenance/replace-z-motor
---

## Z 电机

Z 电机是一个通过 Z 轴同步皮带驱动热床在 Z 轴方向的运动的步进电机，它会带有电机电缆和主动轮。  
![fac173.jpg](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/p2s-sku-pics/fam021.jpg)

## 何时更换

- Z 电机烧坏，不能动作
- 售后人员通过 log 分析，确认是 Z 电机故障。

## 所需的工具和材料

1. H2.0 内六角扳手
2. H1.5 内六角扳手
3. 新的 Z 电机

## 安全提示

> 重要提醒 ！
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，请关闭打印机电源并断开电源连接，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。

## 移除 Z 电机

### 步骤 1：清洁打印机底座

清理打印机底座上的异物，特别是光杆处的残留物，移除打印机玻璃上盖。

### 步骤 2：锁定热床

1. 电机还能使用的情况：

在显示屏上操作，将热床下降到底部，使用 H2.0 内六角扳手将 3 颗螺丝拧入，将 3 个滑块进行锁定，就像当初开箱时，固定热床那样。然后关闭打印机，断开电源连接。

![15_015.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-belt-tensioner/15_015.png)

![16_016.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-belt-tensioner/16_016.png)

2. 电机完全不能使用的情况：

关闭打印机电源，断开电源连接，倾斜打印机，手动移动 Z 轴皮带，将热床下降到底部，再用 3 颗螺丝将 3 个滑块进行锁定。

![13_013.webp](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-motor/13_013.webp)

> 锁定热床是一个关键预备步骤，此操作能有效固定三根Z轴丝杆的相对位置，防止在松开皮带时，丝杆因外力或床身自重而发生意外旋转或位移。从而使热床的基准面得以维持，避免产生超出允许范围的倾斜，保证打印平台的初始水平度。

### 步骤 3：移除背板

您可以根据机型，参考对应 Wiki 来移除打印机背板：

- [P2S](replace-rear-panel.md)
- [X2D](../../x2d/maintenance/replace-rear-panel.md)

| rear_panel_screws_010.png | 背板螺丝.jpg |
| --- | --- |
| P2S | X2D |

### 步骤 4：断开电机连接线

1. 找到位于机器背面右侧的 MC 板，并将 MC 板底部的 Z 电机连接线断开；

![02_002.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-motor/02_002.png)

2. 将 Z 电机连接线依次从线扣中取出；

![04_004.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-motor/04_004.png)

![03_003.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-motor/03_003.png)

3. 将胶布撕开，将 Z 电机连接线取出。

![05_005.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-motor/05_005.png)

### 步骤 5：释放张紧弹簧和张紧轮

1. 移除玻璃上盖，将打印机侧放；

![17_017.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-belt-tensioner/17_017.png)

如需倒放打印机，在将打印机倒置前请务必拆除显示屏避免造成损坏！拆除显示屏的方式可参考：[更换屏幕 | Bambu Lab Wiki](replace-screen.md)

2. 释放弹簧，用 H2.0 内六角扳手拧松黑色的螺丝。

![06_006.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-motor/06_006.png)

### 步骤 6：移除 Z 电机

1. 使用 H2.0 内六角扳手移除 4 颗螺丝，这 4 颗螺丝锁定力矩较大，建议使用可靠的工具进行移除，否则容易滑牙。拆到最后一颗螺丝时，请用手接住电机，防止掉落。

![07_007.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-motor/07_007.png)

2. 将 Z 电机斜着从打印机中取下。

![08_008.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-motor/08_008.png)

![09_009.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-motor/09_009.png)

## 安装 Z 电机

### 步骤 1：安装 Z 电机

1. 斜着将 Z 电机装入打印机（电机的线缆的方向朝外，可参考下图进行安装）。在安装时需稍微用力推动电机，将电机装入，并将 Z 皮带套在电机主动轮上；

![10_010.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-motor/10_010.png)

![11_011.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-motor/11_011.png)

![12_012.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-motor/12_012.png)

2. 用对角线锁螺丝的方式将 4 颗螺丝拧紧。

![07_007.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-motor/07_007.png)

### 步骤 2：卡弹簧，锁张紧轮

将弹簧的长臂卡到位，将张紧轮螺丝锁到位。

![06_006.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-motor/06_006.png)

### 步骤 3：移除滑块固定螺丝，动作检查

1. 将打印机正向放置，移除 3 个滑块上的锁定螺丝；

![17_017.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-belt-tensioner/17_017.png)

![15_015.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-belt-tensioner/15_015.png)

![16_016.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-belt-tensioner/16_016.png)

2. 然后倾斜打印机，来回移动 Z 轴皮带，确认热床能上下移动。

![13_013.webp](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-motor/13_013.webp)

### 步骤 4：穿电机电缆

将胶布重新贴在线缆上，再将电机电缆穿过底座的卡扣位，并扣到侧边上的线扣上，如同拆除前那样。

![05_005.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-motor/05_005.png)

![03_003.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-motor/03_003.png)

![04_004.png](https://public-cdn.bblmw.com/wiki/new/p2s/maintenance/replace-z-motor/04_004.png)

### 步骤 5：安装背板

您可以根据机型，参考对应 Wiki 来安装打印机背板：

- [P2S](replace-rear-panel.md)
- [X2D](../../x2d/maintenance/replace-rear-panel.md)

| rear_panel_screws_010.png | 背板螺丝.jpg |
| --- | --- |
| P2S | X2D |

## 如何验证成功

连接电源，启动打印机。通过屏幕控制热床，检查热床是否可以正常上升下降。如果可以正常运行，则说明 Z 电机更换成功。

如果热床运行异常，请按照操作步骤排查组装是否有问题，排除后，再次运行设备自检。如果问题仍然存在，请联系 Bambu Lab 服务团队寻求进一步的帮助。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 为了确保您安全有效地进行操作，如果对指南中的任何步骤有疑虑或问题，请联系我们的客户服务团队，我们随时乐意为您解答疑问并提供支持。  
> [点击此处联系技术支持](https://support.bambulab.cn)
