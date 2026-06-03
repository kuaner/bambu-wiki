---
path: zh/ams-2-pro/remove-broken-stuck-material
title: "AMS 2 Pro 断裂耗材移除与五通组件传感器检查"
description: "学习如何移除 AMS 2 Pro 中的断裂堵塞耗材并检查五通组件传感器。"
tags: ["ams-2-pro"]
created: 2025-07-25T06:19:53.087Z
updated: 2025-10-13T01:55:01.418Z
source: https://wiki.bambulab.com/zh/ams-2-pro/remove-broken-stuck-material
---

耗材有时会发生断裂并堵塞在 AMS 2 Pro 中，导致进退料失败。本指南为移除断裂耗材提供逐步指导，呈现耗材断裂的可能原因与解决办法，以及如何避免出现类似问题。

## 何时使用本指南？

- 当您遇到错误代码 [0700-8004]，表示 AMS 2 Pro 无法拉回耗材，并且您已经排除了诸如耗材未正确插入等其他可能问题时，请参考本指南进行操作。

![error.jpg](https://wiki.bambulab.com/ams-2-pro/maintenance/broken-material/remove-broken-stuck-material-zh/error.jpg)

- 异常咔哒声或摩擦声：挤出机发出的声音可能表明其推送打印耗材时遇到困难。
- 可见的残余耗材：在铁氟龙料管的透明段内壁或者挤出机路径附近，您可能看见部分耗材碎屑。

## 所需要的工具和材料

- H2.0 和 H1.5 内六角扳手
- 一小段耗材（长度大于 250 mm）

## 安全提示

> *在对打印机及其电子设备（包括工具头电线）进行任何维护工作之前，务必**断开打印机电源**。在打印机开启的情况下执行任务可能会导致短路，从而造成电子损坏和安全隐患。*
>
> *在维护或故障排除过程中，您可能需要拆卸部件，包括热端。这会暴露出电线和电子元件，如果它们在打印机处于开启状态时相互接触、接触其他金属或电子元件，可能会发生短路。**这可能会导致打印机的电子设备损坏并引发其他问题。***
>
> *因此，在进行任何维护之前，务必**关闭打印机并断开电源**。这可以防止短路或损坏打印机的电子设备，确保维护安全有效。*

为了移除 AMS 2 Pro 中堵塞的断裂耗材，您需要在卸下料管后，将一小段耗材推入挤出机。请按照以下步骤操作。

## 将耗材推入挤出机并移除堵塞物

### 第一步：拆卸料管

一只手按住黑色按钮松开料管，然后另一只手取出料管。

![hands_removing_tubes.png](https://wiki.bambulab.com/ams-2-pro/maintenance/broken-material/hands_removing_tubes.png)

### 第二步：将耗材插入入料口

取一小段耗材，插入 AMS 2 Pro 入料口直至其穿过料管，如下图所示:

![](https://wiki.bambulab.com/ams-2-pro/maintenance/broken-material/removing_stuck_filament.png)  
![](https://wiki.bambulab.com/ams-2-pro/maintenance/broken-material/pushing_filament_through.png)

所有堵塞的耗材应从铁氟龙料管口移除。您可以多次操作，直至确认残留物完全清除。操作时请保持动作轻柔，避免耗材在内部再次断裂。操作完成后，取出耗材，继续组装。

### 第三步：将料管插回原位

将料管插回原来的插槽。

![removing_the_tubes.png](https://wiki.bambulab.com/ams-2-pro/maintenance/broken-material/removing_the_tubes.png)

如果耗材在五通组件内部断裂，则需要拆卸、检查和清洁。

## 清洁五通组件

### 第一步：拆卸AMS 2 Pro

要清洁五通组件，您需要拆卸 AMS 2 Pro；阅读 [AMS 2 Pro 拆装指南](maintenance/disassembly-and-assembly.md)学习如何操作。

### 第二步：取出五通组件

拧下并取走固定五通组件的 3 颗螺丝。仔细存放五通组件的防震硅胶套，防止丢失。

![](https://wiki.bambulab.com/ams-2-pro/maintenance/broken-material/removing-three-screws.png)  
![](https://wiki.bambulab.com/ams-2-pro/maintenance/broken-material/internal-hub.png)

接下来，从五通组件中取出电机。

### 第三步：清洁五通组件

拆卸五通组件，清理堵塞的耗材。阅读[拆解和清洁 AMS 五通组件](troubleshooting/clean-the-filaments-hub.md)学习如何操作。

如果五通组件中没有耗材堵塞，但测试后仍检测到存在耗材（通常表现为对应插槽的挤出机中没有插入耗材但红色指示灯仍持续亮起），可能是内部磁铁复位不畅导致。

### 第四步：检查五通磁铁

检查并确认 4 个内部磁铁复位顺畅，如下 Gif 所示：

![checking_magnets.gif](https://wiki.bambulab.com/ams-2-pro/maintenance/broken-material/checking_magnets.gif)

您需要检查磁铁方向，确保它们朝向正确。

![](https://wiki.bambulab.com/ams-2-pro/maintenance/broken-material/normal.jpg)  
![](https://wiki.bambulab.com/ams-2-pro/maintenance/broken-material/not-good.jpg)

如果磁铁朝向错误，您需要取出并安装至正确的方向。阅读[移除和安装 AMS 五通磁铁](../x1/maintenance/install-the-magnets-in-filaments-hub.md)学习如何操作。

如果您发现任何部件失灵，请联系技术支持团队。

完成上述故障排除后，请重新组装相关部件。

## 验证功能

确认所有部件状态正常后，请接通 3D 打印机电源。随后在屏幕上的**耗材**页面，选择一种耗材并点击**进料**选项，测试耗材路径。若成功进料，屏幕将不再出现错误提示。

## AMS 2 Pro 内耗材断裂可能原因与解决办法

尽管您已操作正确，但仍可能在 AMS 2 Pro 的使用中遇到耗材断裂问题，以下因素会进一步提高其发生概率：

1. 使用不兼容或质量差的耗材：使用非官方的不兼容耗材或者易碎和长期暴露的耗材会增加内部断裂的风险。阅读[拓竹耗材指南](https://bambulab.cn/zh-cn/filament-guide)，避免使用易碎和长期暴露的耗材。
2. 使用受潮的耗材：耗材中的水分也会导致耗材断裂。务必确保耗材干燥。在干燥环境中存储料盘或启用 AMS 干燥功能。
3. 错误进退料：手动进退料会导致耗材断裂。请仔细按照 AMS 2 Pro进退料流程操作，避免因错位或用力过猛导致耗材断裂。
4. 铁氟龙料管磨损或损坏：长期使用会导致铁氟龙料管磨损，使耗材更容易内部断裂。一旦发现料管异常，请立即更换。您可从[京东](https://item.jd.com/10069072081747.html)、[天猫](https://detail.tmall.com/item.htm?abbucket=16&id=694059763089&pisk=gVtq7R2BZmn4D51Ao3saTPvkSlsADGlCIh11IdvGhsfmWqKN7pOoHApG1hSwwQbMci9Xa1R6KEOfcNiM4O6QnOqco7blL97M119bHUdBKotjkGZNDGIiOXiIAxpAXGcF2qgUMaXGpcZciZjAqg91xViIAKpzhtDBEDt6BBlfnPqMsZbuEO1uo5bMsgmlI_qcIojGZY5RZt4corqlq9WQnGXgoTvldtP0SsjgE0fRIGfMsGDPq_Big5_G8uWOoYxSjS9-SYbPtKfzjkyd3Z4D3PZab1WcuKdFaa_W4t7VtNcrXu-DNdxXDa34oGpW8C8MtbafieWeawTqToReMOvNIIoLL_x2Q37vPS4cLi5V-nAupv9FSU-PcncTJL9PiwSWP4hf5iR2J6QmybdwUsOM0aVqN1TBFnbytbZy6N8McgxmZDSPm5BloBt9u54NoTBPOYkP7bvQ-YY5-hzTWZNRU6MmnPUOoTBPOYkzWPQjyT5Inxf..&rn=929c91d567831d36c7081d406c033d10&spm=a1z10.3-b-s.w4011-25177047232.212.f2a13c0eAe9bfv)购买替换件。

## 结束语

> 我们希望本指南能帮助您解决问题。如果您对本文中描述的过程有任何疑虑或疑问，您可以联系我们的客户服务团队。我们随时准备为您提供帮助并回答您的任何问题。[点击这里提交服务工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)。我们将为您提供及时回复与所需支持。
