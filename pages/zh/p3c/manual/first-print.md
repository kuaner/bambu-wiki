---
path: zh/p3c/manual/first-print
title: "P3C 首次打印"
description: "本文介绍 P3C 首次打印流程，包括进料、发起打印、退料及常见进料问题。"
tags: []
created: 2026-11-24T14:02:07.932Z
updated: 2026-11-24T14:49:19.166Z
source: https://wiki.bambulab.com/zh/p3c/manual/first-print
---

## 打印流程概览

- 将 AMS 3P 及打印头[连接至打印机](#%E6%AD%A3%E7%A1%AE%E5%AE%89%E8%A3%85-ams-3p-%E5%92%8C%E6%89%93%E5%8D%B0%E5%A4%B4)并[装载耗材](#ams-3p-%E8%BF%9B%E6%96%99)。
- [打印前](#%E6%89%93%E5%8D%B0%E5%89%8D%E5%87%86%E5%A4%87)，先检查打印板和热床的状态，再[发起打印任务](#%E5%BC%80%E5%A7%8B%E6%89%93%E5%8D%B0)。
- [打印结束后](#%E5%8F%96%E4%B8%8B%E5%B9%B6%E7%BB%84%E8%A3%85%E6%A8%A1%E5%9E%8B)，等待模型冷却至室温后再取下模型，[按需将耗材退出](#%E9%80%80%E5%87%BA%E8%80%97%E6%9D%90)。

## 视频指南

## 正确安装 AMS 3P 和打印头

1. 按照纸质快速入门指南正确安装 AMS 3P，确保打印头正确安装到闪切挂架上。

![printtool-status.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/first-print/zh/printtool-status.png)

2. 确保打开电源开关，并在首次校准后移除了热床底部泡棉。

|  |  |
| --- | --- |
| image.png | image.png |

3. 检查 HMS 助手消息，升级至最新固件以获得更流畅的交互体验；如提醒打印头脱落，请将其正确安装至对应泊位。

![screenshot_20261013_103410.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/first-print/zh/screenshot_20261013_103410.png)

## AMS 3P 进料

### 进料步骤

> ***进料前，请先将料盘放入料槽，切勿将耗材直接塞入打印头。请按屏幕提示完成进料流程。经验丰富的用户若能确保耗材正确穿过打印头，可跳过引导程序直接进料。***

1. 将所有需要使用的料盘放进料槽。  
   ![place-spool.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/first-print/zh/place-spool.png)
2. 在打印机屏幕进入①耗材页，点击②左下角刷新按钮，读取所有耗材信息。  
   ![](https://public-cdn.bblmw.com/wiki/new/p3c/manual/first-print/zh/annotated_screenshot_20261013_103627.png)

> AMS 3P 支持不插入耗材读取耗材信息。  
> 打印机仅支持读取官方耗材信息。如使用第三方耗材，需手动编辑耗材信息。

3. 点击 ③AMS 进料->④全选->⑤进料，启动进料流程。

|  |  |
| --- | --- |
| Annotated_screenshot_20261013_103944.png | Annotated_screenshot_20261013_103956.png |

4. 根据屏幕上**进料流程**的提示，依次将耗材送入上下料料嘴，直至无法继续推进。

|  |  |
| --- | --- |
| screenshot_20261013_114540.png | img_v3_0216e_c9e18c88-5df2-48bc-a670-973fc235d25g.jpg |

> 送料前如发现耗材末端弯曲或磨损严重，请剪掉这一截后再送入耗材，以免挤出轮咬合失败。

### 快捷进料提示

前一个打印头挤出时，即可将后续待进料的耗材预先送入到图示位置。等屏幕提示插入下一个打印头对应耗材时，只需再送入一小段。送料与挤出同时进行，可明显缩短进料时间。

> 送料至图示位置即可，请勿直接将耗材送入打印头。

![fast-loading-en.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/first-print/zh/fast-loading-cn.png)

### 确认进料状态

正常进料后，耗材从打印头顶部向下进入热端，此时可从挤出轮视窗观察到耗材，并能观察到喷嘴处耗材顺畅挤出。

|  |  |
| --- | --- |
| image.png | image.png |

若屏幕出现下图弹窗，说明在点击进料之前，已将耗材送入打印头。此时工具头尚未夹取打印头，进料路径不够准确，后续可能无法被挤出轮咬合。

![screenshot_20261013_104126.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/first-print/zh/screenshot_20261013_104126.png)

请先回转料盘，将耗材从打印头中拉出。在屏幕上点击进料后，再按屏幕进料流程提示送料。

![screenshot_20261013_114540.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/first-print/zh/screenshot_20261013_114540.png)

**解决方法**：先回转料盘，将耗材从打印头中拉出。在屏幕点击**进料**后，再根据屏幕上的进料流程提示送料。

## 打印前准备

### 检查热床

在放置打印板前，请检查并清洁热床表面，确保无异物残留。若存在异物，在加热过程中可能对软磁贴表面造成不可逆损伤。

![AM407078.JPG](https://public-cdn.bblmw.com/wiki/new/p3c/manual/first-print/zh/am407078.jpg)

### 清洁打印板

请避免在开箱或操作过程中直接用手接触打印板表面，以免油污影响打印附着力。

如不慎触碰，请参考[纹理 PEI 板清洁指南](../../filament-acc/acc/pei-plate-clean-guide.md)进行清洁。

## 开始打印

建议自行准备一个 U 盘并插入打印机，用于保存工作录像和历史打印缓存。

![img_v3_0216e_76fdb236-711d-4537-8056-d5bf0eaada1g.jpg](https://public-cdn.bblmw.com/wiki/new/p3c/manual/first-print/zh/usb.png)

### 选择模型

在首页点击**打印文件**，选择想要打印的模型，首次打印推荐刮刀手柄。

|  |  |
| --- | --- |
| Annotated_screenshot_20261013_115312.png | Annotated_image \(7\).png |

### 确认配置

确认使用的打印板和热端配置正确，并在打印选项中根据需要设置延时摄影和高级选项（默认为自动模式），然后点击**下一步**。

![image.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/first-print/zh/image_11.png)

### 匹配耗材

选择本次打印使用的耗材，点击**打印**。

![image.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/first-print/zh/image_1.png)

## 取下并组装模型

1. 打印结束后，等待热床和模型冷却至室温。随后取下打印板，轻轻弯折打印板以取下模型和擦拭塔。
2. 将工具盒中附赠的刀片卡入刀柄上的凸起位置。

![Annotated_image (20).png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/first-print/zh/annotated_image_20.png)

注意：如果刀片无法卡入，说明方向错误，请翻转刀片调整方向。请确保刀片安装方向正确，避免使用中脱落导致受伤。

3. 对齐刀片、刀柄和抵手块上的螺丝孔位，使用 H2.0 扳手拧紧 2 颗螺丝。

|  |  |
| --- | --- |
| image.png | image.png |

注意：刀片锋利，装配时请小心操作，防止划伤。请将刮刀放置在儿童无法触及的地方。

4. 使用刮刀清除打印板上的预挤出线，再将打印板重新放回热床。

|  |  |
| --- | --- |
| image.png | image.png |

## 退出耗材

打印成功后，耗材将继续保持进料状态。如后续继续使用，可直接存放于 AMS 内。

![img_v3_0216e_8f06812b-e3f9-426b-addc-83522065627g.jpg](https://public-cdn.bblmw.com/wiki/new/p3c/manual/first-print/zh/store-spools.png)

如需更换耗材，在屏幕进入耗材页，点击②对应槽位→③退料，根据屏幕退料流程提示手动旋转料盘收回耗材，并将耗材末端收纳在料盘上的固定孔位中。

|  |  |
| --- | --- |
| Annotated_screenshot_20261013_121402.png | image.png |

如需一次性退出多个耗材，可在屏幕点击②退料→③全选→④退料。待屏幕退料流程提示后，手动旋转料盘收回所有耗材，并将耗材末端收纳在料盘上的固定孔位中。

|  |  |
| --- | --- |
| Annotated_screenshot_20261013_121408.png | Annotated_screenshot_20261013_121414.png |

## 常见问题

**Q：为什么无法在屏幕发起“进料”程序？**

![image.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/first-print/zh/faq-cannot-start-load.png)

这通常是因为在发起进料程序前，**手动将耗材送入了打印头**，提前触发了进料霍尔传感器，导致系统判定为“已进料”或进入了**进料待确认状态**（即系统无法确认耗材是否已正确贯穿打印头）。

建议升级至最新固件。在打印机空闲状态下直接手动送料到打印头时，可能会出现下图弹窗，便于立即确认进料状态。

![screenshot_20261013_104126.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/first-print/zh/screenshot_20261013_104126.png)

**常见的 3 种“进料待确认状态”场景：**

1. **耗材路径偏移**
2. **新进耗材未到达挤出轮处**，无法被正确咬合：
   - 旧料卡在挤出轮处，新料未到位。
   - 新料根本未到达挤出轮位置。

**💡 建议与解决方法：**

- **如果您是新手用户：**
  - 建议在进料前**切勿**直接将耗材送入打印头，应先将料盘放入料槽。
  - 在屏幕点击“进料”，待屏幕提示手动送料后再推送耗材完成进料流程，这样可确保进料正常。

![screenshot_20261013_114540.png](https://public-cdn.bblmw.com/wiki/new/p3c/manual/first-print/zh/screenshot_20261013_114540.png)

- **如果您是经验丰富的用户：**
  - 若能确保耗材已正确穿过打印头，且认为此前已完成“进料”，您可以**直接发起打印**。
  - 系统为了确保进料万无一失，打印前可能会有提示确保正确进料，忽略对应提示即可。

详细手动进料指引，请参见 [AMS 3P 进料](#ams-3p-%E8%BF%9B%E6%96%99)。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
