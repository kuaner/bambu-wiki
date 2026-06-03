---
path: zh/h2d/troubleshooting/remove-broken-filament-in-ams-2-pro-and-h2d-tubes
title: "AMS 2 Pro 与 H2D 料管中断裂耗材的移除 "
description: "学习如何从 AMS 2 Pro 和 H2D 的料管中安全移除断裂耗材。"
tags: ["ams 2 pro", "h2d"]
created: 2025-07-31T10:26:17.256Z
updated: 2025-12-24T12:18:39.725Z
source: https://wiki.bambulab.com/zh/h2d/troubleshooting/remove-broken-filament-in-ams-2-pro-and-h2d-tubes
---

耗材有时会在 AMS 2 Pro 和 H2D 的铁氟龙料管中发生断裂，造成进料失败或者 AMS 2 Pro 报错。本指南为移除料管中的断裂耗材提供逐步指导。

## 何时使用本指南？

- 当您遇到错误代码 [0700-8004]，表示 AMS 2 Pro 无法拉回耗材，并且您已经排除了诸如耗材未正确插入等其他可能问题时，请参考本指南进行操作。
- 异常咔哒声或摩擦声。挤出机发出的声音可能表明其推送打印耗材时遇到困难。
- AMS 2 Pro 的料管中或者连接 AMS 2 Pro 和 H2D 的料管中有可见的残留耗材。

## 需要的工具

- H2.0 内六角扳手
- 备用铁氟龙料管。您可从[京东](https://item.jd.com/10069072081747.html)、[天猫](https://detail.tmall.com/item.htm?abbucket=16&id=694059763089&pisk=gVtq7R2BZmn4D51Ao3saTPvkSlsADGlCIh11IdvGhsfmWqKN7pOoHApG1hSwwQbMci9Xa1R6KEOfcNiM4O6QnOqco7blL97M119bHUdBKotjkGZNDGIiOXiIAxpAXGcF2qgUMaXGpcZciZjAqg91xViIAKpzhtDBEDt6BBlfnPqMsZbuEO1uo5bMsgmlI_qcIojGZY5RZt4corqlq9WQnGXgoTvldtP0SsjgE0fRIGfMsGDPq_Big5_G8uWOoYxSjS9-SYbPtKfzjkyd3Z4D3PZab1WcuKdFaa_W4t7VtNcrXu-DNdxXDa34oGpW8C8MtbafieWeawTqToReMOvNIIoLL_x2Q37vPS4cLi5V-nAupv9FSU-PcncTJL9PiwSWP4hf5iR2J6QmybdwUsOM0aVqN1TBFnbytbZy6N8McgxmZDSPm5BloBt9u54NoTBPOYkP7bvQ-YY5-hzTWZNRU6MmnPUOoTBPOYkzWPQjyT5Inxf..&rn=929c91d567831d36c7081d406c033d10&spm=a1z10.3-b-s.w4011-25177047232.212.f2a13c0eAe9bfv)购买。
- 一小段耗材

## 安全提示

> 在对打印机及其电子设备（包括工具头电线）进行任何维护工作之前，务必**断开打印机电源**。在打印机开启的情况下执行任务可能会导致短路，从而造成电子损坏和安全隐患。  
> 在维护或故障排除过程中，您可能需要拆卸部件，包括热端。这会暴露出电线和电子元件，如果它们在打印机处于开启状态时相互接触、接触其他金属或电子元件，可能会发生短路。**这可能会导致打印机的电子设备损坏并引发其他问题。**  
> 因此，在进行任何维护之前，务必**关闭打印机并断开电源**。这可以防止短路或损坏打印机的电子设备，确保维护安全有效。  
> 如果您在按照本指南操作的过程中有任何疑虑或疑问，请[点击这里提交服务工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)，我们将为您提供及时回复与所需支持。

## 排障指南

首先判断耗材断裂的具体位置。请查看打印机屏幕或者 Bambu Studio 是否有错误提示，如“耗材断裂在路径”或 HMS 错误代码，尤其是 [0700-2000-0002-0003](../../x1/troubleshooting/hmscode/0700_2000_0002_0003.md) 或 [0700 8004]。请记录红色 LED 灯亮起的 AMS 2 Pro 料槽编号（1-4）并检查从 AMS 2 Pro 出口到 H2D 缓冲器或工具头之间的铁氟龙料管和 AMS 2 Pro 内部的料管，查看是否有可见的耗材碎屑。耗材可能断裂的位置包括：

- AMS 2 Pro 和 H2D 打印机之间的特氟龙料管
- AMS 2 Pro 内部的料管
- H2D 的挤出机组件

## 移除 AMS 2 Pro 和 H2D 打印机之间的铁氟龙料管中的堵塞耗材

如果耗材断裂在 AMS 2 Pro 和 H2D 打印机之间的铁氟龙料管内，您需要拆卸并清洁该料管。

![ptfetubes.png](https://wiki.bambulab.com/h2/maintenance/replace-ptfe-tube-on-h2d-printer/ptfetubes.png)

### 第一步：拆卸料管

首先从 AMS 2 Pro 背面移除耗材。一只手按压黑色区域，另一只手拉出料管。

|  |  |
| --- | --- |
|  |  |

接下来，从 H2D 机箱背面的侧边处移除料管。按住气动接头的黑色外圈，解锁并拉出料管。

![移除背部料管.gif](https://wiki.bambulab.com/h2/troubleshooting/%E7%A7%BB%E9%99%A4%E8%83%8C%E9%83%A8%E6%96%99%E7%AE%A1.gif)

### 第二步：断开腔室内所有铁氟龙料管的连接

按住黑色外圈，解锁挤出机上方的两个气动接头。

![移除背部料管.gif](https://wiki.bambulab.com/h2/troubleshooting/%E7%A7%BB%E9%99%A4%E8%83%8C%E9%83%A8%E6%96%99%E7%AE%A1.gif)

### 第三步：断开与耗材缓冲器连接的料管

按住缓冲器的气动接头黑色外圈，向右推气动接头，以解锁缓冲区上下两端的气动接头，然后拔出左右两根铁氟龙料管。

|  |  |
| --- | --- |
|  |  |

### 第四步：推出断裂耗材

用一段较长的耗材从一端将断裂的耗材推出料管。

![removing-broken-filament.jpg](https://wiki.bambulab.com/h2/maintenance/removing-broken-material/removing-broken-filament.jpg)

### 第五步：重新连接料管

移除断裂的耗材后，需要重新连接铁氟龙料管。将两根铁氟龙料管从拖链卡扣侧面的孔中穿过。

![reconnecting-the-tubes.png](https://wiki.bambulab.com/h2/maintenance/removing-broken-material/reconnecting-the-tubes.png)

将铁氟龙料管重新连接至 AMS 2 Pro、耗材缓冲器和 H2D 工具头，确保连接牢固（持续推入直到听到咔嗒声）。然后装入新的耗材并测试进料。

|  |  |
| --- | --- |
|  |  |

> 注意：拖链上方的铁氟龙料管需要连接到右挤出机，拖链下方的铁氟龙料管需要连接到左挤出机。

这些料管长时间使用可能会出现磨损，导致摩擦力增加，进而提高耗材断裂的风险。您需要对它们进行仔细检查。如果发现磨损，可以在[京东](https://item.jd.com/10069072081747.html)、[天猫](https://detail.tmall.com/item.htm?abbucket=16&id=694059763089&pisk=gVtq7R2BZmn4D51Ao3saTPvkSlsADGlCIh11IdvGhsfmWqKN7pOoHApG1hSwwQbMci9Xa1R6KEOfcNiM4O6QnOqco7blL97M119bHUdBKotjkGZNDGIiOXiIAxpAXGcF2qgUMaXGpcZciZjAqg91xViIAKpzhtDBEDt6BBlfnPqMsZbuEO1uo5bMsgmlI_qcIojGZY5RZt4corqlq9WQnGXgoTvldtP0SsjgE0fRIGfMsGDPq_Big5_G8uWOoYxSjS9-SYbPtKfzjkyd3Z4D3PZab1WcuKdFaa_W4t7VtNcrXu-DNdxXDa34oGpW8C8MtbafieWeawTqToReMOvNIIoLL_x2Q37vPS4cLi5V-nAupv9FSU-PcncTJL9PiwSWP4hf5iR2J6QmybdwUsOM0aVqN1TBFnbytbZy6N8McgxmZDSPm5BloBt9u54NoTBPOYkP7bvQ-YY5-hzTWZNRU6MmnPUOoTBPOYkzWPQjyT5Inxf..&rn=929c91d567831d36c7081d406c033d10&spm=a1z10.3-b-s.w4011-25177047232.212.f2a13c0eAe9bfv)购买替换件。

如果耗材断裂在挤出机内部，您需要拆卸挤出机，移除堵塞的耗材，然后重新组装。请查看 [H2D 挤出机拆解与组装指引](../../h2/troubleshooting/extruder-assembly.md)了解具体操作方法。

## 移除 AMS 2 Pro 料管中的堵塞耗材

### 第一步：拆卸料管

一只手按住黑色按钮松开料管，另一只手拉出耗材。

![hands_removing_tubes.png](https://wiki.bambulab.com/ams-2-pro/maintenance/broken-material/hands_removing_tubes.png)

### 第二步：将耗材插入入料口

取一小段耗材，插入 AMS 2 Pro 入料口直至其穿过料管，如下图所示:

|  |  |
| --- | --- |
|  |  |

所有堵塞的耗材应从铁氟龙料管口移除。您可以多次操作，直至确认残留物完全清除。操作时请保持动作轻柔，避免耗材在内部再次断裂。操作完成后，继续组装部件。

### 第三步：将料管插回原位

将料管插回原来的料槽。

![removing_the_tubes.png](https://wiki.bambulab.com/ams-2-pro/maintenance/broken-material/removing_the_tubes.png)

如果耗材在五通组件内部断裂，则需要拆卸、检查和清洁。

## 移除五通组件内部的堵塞耗材

### 第一步：拆卸五通组件

要清洁五通组件，您需要拆卸 AMS 2 Pro；阅读 [AMS 2 Pro 拆装指南](../../ams-2-pro/maintenance/disassembly-and-assembly.md)学习如何操作。请按照 Wiki 中的步骤操作至第 7 步（拆除五通组件）。

### 第二步：清洁五通组件

拆卸五通组件，清理堵塞的耗材。阅读[拆解和清洁 AMS 五通组件](../../x1/troubleshooting/clean-the-filaments-hub.md)学习如何操作。

![55_可以撬开气动接头.gif](https://wiki.bambulab.com/ams-2-pro/maintenance/clean-the-filaments-hub/55_%E5%8F%AF%E4%BB%A5%E6%92%AC%E5%BC%80%E6%B0%94%E5%8A%A8%E6%8E%A5%E5%A4%B4.gif)

如果五通组件中没有耗材堵塞，但测试后仍检测到存在耗材（通常表现为对应插槽的挤出机中没有插入耗材但红色指示灯仍持续亮起），可能是内部磁铁复位不畅导致。

### 第三步：检查内部磁铁

检查并确认 4 个内部磁铁复位顺畅。

![checking_magnets.gif](https://wiki.bambulab.com/ams-2-pro/maintenance/broken-material/checking_magnets.gif)

您需要检查磁铁方向，确保它们朝向正确，并且不得有任何磨损的迹象。

完成上述故障排除后，请重新组装相关部件。

## 移除挤出机内的断裂耗材

如果耗材断裂堵塞在挤出机内，您需要拆卸、检查和清洁挤出机。请参考 [H2D 挤出机拆解与组装指引](../../h2/troubleshooting/extruder-assembly.md)逐步操作。您也可以查阅 [H2D 堵塞排查](../../h2/troubleshooting/clogging.md)确定挤出机中耗材堵塞的位置。

## 验证功能

确保打印机能够恢复打印且成功进料，不再出现错误提示。

## AMS 2 Pro 内耗材断裂可能原因与解决办法

1. **质量差的耗材**：使用易碎耗材或者非官方的不兼容耗材更容易发生断裂。建议使用拓竹原装耗材[拓竹耗材指南](https://bambulab.cn/zh-cn/filament-guide)以确保打印的稳定性和可靠性。
2. **耗材受潮**：潮湿的耗材更容易断裂。保持料盘干燥或启用 AMS 干燥功能。
3. **手动进料/退料**：操作不当也会导致耗材断裂。请始终通过打印机屏幕进行进退料操作。
4. **铁氟龙料管损坏**：磨损的料管会增加耗材断裂的风险。如果发现有磨损迹象，请及时更换。您可从[京东](https://item.jd.com/10069072081747.html)、[天猫](https://detail.tmall.com/item.htm?abbucket=16&id=694059763089&pisk=gVtq7R2BZmn4D51Ao3saTPvkSlsADGlCIh11IdvGhsfmWqKN7pOoHApG1hSwwQbMci9Xa1R6KEOfcNiM4O6QnOqco7blL97M119bHUdBKotjkGZNDGIiOXiIAxpAXGcF2qgUMaXGpcZciZjAqg91xViIAKpzhtDBEDt6BBlfnPqMsZbuEO1uo5bMsgmlI_qcIojGZY5RZt4corqlq9WQnGXgoTvldtP0SsjgE0fRIGfMsGDPq_Big5_G8uWOoYxSjS9-SYbPtKfzjkyd3Z4D3PZab1WcuKdFaa_W4t7VtNcrXu-DNdxXDa34oGpW8C8MtbafieWeawTqToReMOvNIIoLL_x2Q37vPS4cLi5V-nAupv9FSU-PcncTJL9PiwSWP4hf5iR2J6QmybdwUsOM0aVqN1TBFnbytbZy6N8McgxmZDSPm5BloBt9u54NoTBPOYkP7bvQ-YY5-hzTWZNRU6MmnPUOoTBPOYkzWPQjyT5Inxf..&rn=929c91d567831d36c7081d406c033d10&spm=a1z10.3-b-s.w4011-25177047232.212.f2a13c0eAe9bfv)购买替换件。

## 结束语

> 我们希望本指南能帮助您解决问题。如果您对本文中描述的过程有任何疑虑或疑问，您可以联系我们的客户服务团队。我们随时准备为您提供帮助并回答您的任何问题。[点击这里提交服务工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)。我们将为您提供及时回复与所需支持。
