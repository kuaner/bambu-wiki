---
path: zh/h3c/manual/first-print
title: "H3C 首次打印"
description: ""
tags: []
created: 2026-11-03T12:11:35.968Z
updated: 2026-11-04T03:10:50.894Z
source: https://wiki.bambulab.com/zh/h3c/manual/first-print
---

## 打印流程概览

- 将 AMS 3H 及打印头连接至打印机并[装载耗材](#ams-3h-load)。
- 打印前，先[检查打印板和热床](#pre-print)的状态，再[发起打印](#start-print)任务。
- 打印结束后，等待模型冷却至室温后再[取下模型](#remove-model)，并将[耗材退出](#unload-filament)打印机，以便下次使用。

## 视频指南

## 正确安装 AMS 3H 和打印头

1. 按照纸质快速入门指南或 [H3C AMS 套装开箱指南](unboxing-h3c-ams-combo.md)正确安装 AMS 3H，确保打印头正确安装到闪切挂架上。

|  |  |
| --- | --- |
| 001.png | 002.png |

2. 确保打开电源开关，并在首次校准后移除了热床底部泡棉。

|  |  |
| --- | --- |
| 003.png | 004.png |

3. 检查 HMS 助手消息。如提示打印头脱落，请将打印头正确安装到对应泊位，并确认挂架上的白色指示灯全部亮起。

|  |  |
| --- | --- |
| 005.png | 006.png |

## AMS 3H 进料

> 打印机标配 8 个 1.75 mm 线径用打印头及 1 个 2.85 mm 线径用打印头（8 号位），2.85 mm 线径用打印头仅可打印 2.85 mm 柔性耗材。如需使用 8 号头打印 2.85 mm 柔性耗材，请参考 [H3C TPU 打印指南](tpu-printing-guide.md)。如需移动或更换打印头，请参考[打印头组件更换指南](../maintenance/replace-printtool.md)。

> 💡 关于 8 号打印头的特别说明：  
> 2.85 mm 线径用打印头采用直通进料设计，耗材直接进入打印头而无需通过料管，因此其配套的料管收纳在打印头的侧槽中，主要起到支撑和引导作用，确保进料顺畅。

将料盘沿绕线方向放进料槽，将耗材插入上下料料嘴**至少 70 mm**，AMS 在检测到耗材后自动预上料。

|  |  |
| --- | --- |
| 007.png | 008.png |

确认上下料料嘴对应的白灯点亮后，可开始打印。

![009.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/first-print/zh/009.png)

## 打印前准备

### 检查热床

在放置打印板前，请检查并清洁热床表面，确保无异物残留。若存在异物，在加热过程中可能对软磁贴表面造成不可逆损伤。

![010.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/first-print/zh/010.png)

### 清洁打印板

请避免在开箱或操作过程中直接用手接触打印板表面，以免油污影响打印附着力。

如不慎触碰，请参考[纹理 PEI 板清洁指南](../../filament-acc/acc/pei-plate-clean-guide.md)进行清洁。

## 开始打印

建议自行准备一个 U 盘并插入打印机，用于保存工作录像和历史打印缓存。

![011.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/first-print/zh/011.png)

### 选择模型

在首页点击**打印文件**，选择想要打印的模型，首次打印推荐刮刀手柄。

|  |  |
| --- | --- |
| 012.png | 013.png |

### 确认配置

确认使用的打印板和热端配置正确，并在打印选项中根据需要设置延时摄影和高级选项（默认为自动模式），然后点击**下一步**。

![014.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/first-print/zh/014.png)

### 匹配耗材

选择本次打印使用的耗材，点击**打印**。

![015.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/first-print/zh/015.png)

### 其他打印方式

#### 从 Bambu Studio 发起打印

1. 参考[打印机账号绑定指南](../../knowledge-sharing/printer-account-binding-guide.md)连接 Wi-Fi。
2. 参考 [Bambu Studio 快速上手教程](../../software/bambu-studio/studio-quick-start.md) 安装软件，连接打印机。
3. 进入 Bambu Studio 主页，挑选想要打印的模型，选择打印配置后点击**下载并打开**。

![016.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/first-print/zh/016.png)

4. 点击**切片单盘-打印单盘**，确认打印所需耗材信息，按需设置高级选项，点击**发送**。

![017.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/first-print/zh/017.png)

#### 从 Bambu Handy 发起打印

1. 参考[打印机账号绑定指南](../../knowledge-sharing/printer-account-binding-guide.md)连接 Wi-Fi。
2. 参考 [Bambu Handy 快速入门指南](../../studio-handy/handy/bambu-handy-quick-start.md)安装软件，连接打印机。
3. 在 Bambu Handy 中选择想要打印的模型，点击**准备打印**，选择打印配置，确认打印信息，再点击**开始打印**即可将打印任务发送给打印机。

您可前往 [Bambu Lab 软件页](../../software.md) 获取更多软件使用教程。

|  |  |
| --- | --- |
| 018.png | 019.png |

## 取下并组装模型

1. 打印结束后，等待热床和模型冷却至室温。随后取下打印板，轻轻弯折打印板以取下模型和擦料塔。

|  |  |
| --- | --- |
| 020.png | 021.png |

2. 将工具盒中附赠的刀片卡入刀柄上的凸起位置。

![022.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/first-print/zh/022.png)

> 注意：如果刀片无法卡入，说明方向错误，请翻转刀片调整方向。请确保刀片安装方向正确，避免使用中脱落导致受伤。

3. 对齐刀片、刀柄和抵手块上的螺丝孔位，使用 H2.0 扳手拧紧 2 颗螺丝。

|  |  |
| --- | --- |
| 023.png | 024.png |

> 注意：刀片锋利，装配时请小心操作，防止划伤。请将刮刀放置在儿童无法触及的地方。

4. 使用刮刀清除打印板上的预挤出线，再将打印板重新放回热床。

|  |  |
| --- | --- |
| 025.png | 026.png |

## 退出耗材

打印成功后，耗材将继续保持进料状态。如后续继续使用，可直接存放于 AMS 内。

![027.png](https://public-cdn.bblmw.com/wiki/new/h3c/manual/first-print/zh/027.png)

如需更换耗材，在屏幕进入耗材页，点击②对应槽位→③退料，根据屏幕退料流程提示手动旋转料盘收回耗材，并将耗材末端收纳在料盘上的固定孔位中。

|  |  |
| --- | --- |
| 028.png | 029.png |

如需一次性退出多个耗材，可在屏幕点击②退料→③全选→④退料。待屏幕退料流程提示后，手动旋转料盘收回所有耗材，并将耗材末端收纳在料盘上的固定孔位中。

|  |  |
| --- | --- |
| 030.png | 031.png |

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
