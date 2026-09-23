---
path: zh/r1/maintenance/periodic-maintenance
title: "R1 定期维护建议"
description: "本文将介绍设备上需要定期维护的部件以及方式。"
tags: []
created: 2026-09-22T12:51:34.323Z
updated: 2026-09-22T13:30:07.457Z
source: https://wiki.bambulab.com/zh/r1/maintenance/periodic-maintenance
---

## 清洁要点

1. **越靠近工具头的部件，维护频率越高。**  
   距离加工区域越近，越容易受到碎屑和烟雾的影响，应优先检查、勤加清洁。
2. **反射镜须断电冷却后清洁，湿巾只能单向擦拭。**  
   严禁干擦或来回擦拭，否则容易划伤镜面，影响激光输出效果。
3. **优先保证排烟通畅。**  
   风机积垢或滤网堵塞会导致烟雾在设备内部回流，加速所有镜片的污染，排烟不畅是镜片脏污的主要原因之一。
4. **加工高烟雾材料时，需增加清洁频次。**  
   如皮革、亚克力、密度板等材料在加工中会产生大量烟雾，使用后应及时清理。

## 安全提示

> 在对激光切割机及其电子设备（包括工具头线缆）进行任何维护前，请先关闭设备电源并断开电源连接，以防屏幕误触或电路短路造成额外的设备损坏与安全隐患。维护或排查故障前，请确认相关部件已冷却。

## 维护周期

| 部件 | 维护周期 |
| --- | --- |
| 工作仓 | 每次加工 |
| 支撑刀条 | 每次加工 |
| 排烟风扇和滤网 | 每工作 20h 或滤网明显脏污 |
| 导轨/同步带 | 每工作 50-100h |
| 反射镜 | 每工作 8h 或镜面出现明显脏污。 |
| 工具头相机 | 每工作 8h 或提示镜头脏污时 |
| 聚焦镜 | 每工作 16 h |
| 俯视相机 | 每工作 8h 或拍照不清晰时 |
| 火焰传感器 | 每次加工前检查 |
| 定位标签 | 每工作 200 h |
| 冷却液 | 每半年更换一次 |

## 维护部件

## 整机

### 上盖视窗

检查上盖视窗表面是否有模糊的雾状痕迹，可使用纸巾擦拭清理。

![001.png](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/periodic-maintenance/zh/001.png)

### 工作仓

每次加工前，请清理蜂窝板或托盘中残留的加工碎屑和粉尘。碎屑堆积不仅会影响加工精度，更会大幅增加起火燃烧的风险，务必在开机前彻底清除。

![002.png](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/periodic-maintenance/zh/002.png)

### 机箱内壁

检查机箱内是否有较多灰尘，可使用纸巾擦拭，避免灰尘累积。

|  |  |
| --- | --- |
| 003.png | 004.png |

### 支撑刀条

定期使用清洁湿巾擦拭支撑刀条，避免刀条上的残留物污染加工材料，从而影响成品的最终效果。

![005.png](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/periodic-maintenance/zh/005.png)

### 排烟风扇和滤网

加工过程中产生的烟雾和粉尘会通过排烟风扇排出设备。当滤网被大量粉尘堵塞时，请及时清洗，确保排烟通畅，避免烟雾回流污染内部镜片。

可参考[滤网和风扇维护教程](smoke-ventilation-fan.md)冲洗滤网，并维护排气风扇。

![006.png](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/periodic-maintenance/zh/006.png)

### 导轨/同步带

烟尘堆积会加速润滑油/脂的风干，残留的污渍还会增大导轨的运动阻力，甚至产生异响。建议每工作 50–100 小时清洁并润滑一次导轨，可参考[导轨维护教程](xy-axis.md)进行操作。

### 俯视相机窗口

当拍照画面明显模糊，或镜头存在明显灰尘时，使用清洁湿巾擦拭俯视相机窗口。

打开顶盖后，俯视相机就在顶盖内侧。

![007.png](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/periodic-maintenance/zh/007.png)

### 火焰传感器

设备总共有7个火焰传感器，可阅读[部件介绍](../manual/r1-intro.md)了解安装位置。

确保火焰传感器周围不存在加工残料、异物等遮挡。

![008.png](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/periodic-maintenance/zh/008.png)

使用清洁湿巾擦拭传感器表面。

![009.png](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/periodic-maintenance/zh/009.png)

### 左右侧定位标签

建议工作 200h 检查一次定位标签是否破损，清除异物和灰尘。

|  |  |
| --- | --- |
| 010.png | 011.png |

## 工具头

### 工具头相机

工具头相机镜头如有脏污，可能影响视觉定位的准确性。建议每工作 8 小时使用清洁湿巾擦拭一次。

首先需要使用 H1.5 内六角螺丝刀拆卸工具头前盖的两颗螺丝。

|  |  |
| --- | --- |
| 012.jpg | 013.jpg |

取下工具头前盖。

![014.webp](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/periodic-maintenance/zh/014.webp)

使用清洁湿巾擦拭右半部分，清理摄像头镜片，完成后装回前盖。

|  |  |
| --- | --- |
| 015.png | 016.png |

### 光学镜组

可参考[光学镜组维护教程](reflective-mirror.md)进行操作。

其中，2 号和 3 号反射镜建议每工作 8 小时清洁一次。当镜面出现镀膜灼烧、脱膜或划伤时，需及时更换新的反射镜。

![017.png](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/periodic-maintenance/zh/017.png)

聚焦镜脏污会导致激光功率下降，直接影响加工效果。建议每工作 16 小时清洁一次。

![018.jpg](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/periodic-maintenance/zh/018.jpg)

### 气嘴

长期使用激光雕刻后，气嘴表面也会附着加工污渍，严重时可能会降低气流或堵塞。

![019.png](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/periodic-maintenance/zh/019.png)

拧下气嘴。

![020.webp](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/periodic-maintenance/zh/020.webp)

使用清洁湿巾擦拭表面污渍，确保表面干净后装回设备，再装回工具头前盖。

![021.png](https://public-cdn.bblmw.com/wiki/new/r1/maintenance/periodic-maintenance/zh/021.png)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
