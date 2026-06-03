---
path: zh/x1/maintenance/extruder-connection-board-replacement
title: "更换X1系列挤出接口板"
description: "本指南介绍如何更换X1系列打印机上的挤出接口板。"
tags: ["x1"]
created: 2025-07-31T02:31:28.522Z
updated: 2026-02-11T08:50:06.611Z
source: https://wiki.bambulab.com/zh/x1/maintenance/extruder-connection-board-replacement
---

## 挤出接口板-X1

![x1挤出主板.jpg](https://wiki.bambulab.com/x1/maintenance/replace-extruder-connection-board/x1%E6%8C%A4%E5%87%BA%E4%B8%BB%E6%9D%BF.jpg)

## 何时更换

- 连接器或组件损坏
- 通过打印机 LOG 分析发现了问题

## 所需工具与材料

1. H1.5  六角扳手
2. 新的挤出接口板
3. 硅胶
4. 刻刀或锋利小刀（**谨防划伤**）

## 安全提示

> **重要提醒 ！**
>
> 在对打印机及其电子设备（包括工具头线缆）进行任何维护工作之前，**请关闭打印机电源并断开电源连接**，以避免发生电路短路从而引起额外的电子设备损坏和安全隐患。
>
> 在您对打印机进行维护或故障排查时，请先确认热端和热床的温度，避免在高温状态下操作，如果必须在高温状态下操作，请佩戴好隔热手套，以确保安全有效地执行维护工作。
>
> 如果您对本指南有任何疑问，请[点击提交服务工单](https://bambulab.cn/zh/sign-in?to=%2Fmy%2Fsupport%2Ftickets)，我们将及时回复并为您提供所需的帮助。

## 拆除步骤

> **注意**： 对于使用硅胶加固的连接器，在从接头拔出连接件之前，请使用电吹风加热接头处的硅胶，或使用镊子去除一部分，以防止损坏连接器。并建议在重新连接后，追加硅胶进行加固。

### **第 1 步 - 移除工具头前盖**

打开前壳，并如图所示将其轻放在碳杆上。操作时请轻拿轻放，以免损坏连接的线缆。

![front-housing-removed-from-extruder.png](https://wiki.bambulab.com/x1/maintenance/th-boards-v9/front-housing-removed-from-extruder.png)

### **第 2 步 - 断开与挤出机接口板的线缆连接**

断开连接在接口板上的三根热端线缆。

|  |  |
| --- | --- |
|  |  |

> **注意**：对于线缆 1 和 2，请握住连接器拔出，不要拉扯导线本体。  
> 对于线缆 3，插头上有卡扣，请按下卡扣释放连接，不要直接拉扯线缆或插头，以免整个 PCB 接口被拉脱。卡扣位置如下图所示：

![latch-pointed.png](https://wiki.bambulab.com/x1/maintenance/th-boards-v9/latch-pointed.png)

### **第 3 步 - 拆下螺丝和 FPC 排线**

用 H1.5 内六角扳手移除 2 颗螺丝，前两颗螺丝处需保留金属固定夹。

![screws-to-removed.png](https://wiki.bambulab.com/x1/maintenance/th-boards-v9/screws-to-removed.png)

> **注意**：这些螺丝较小，请妥善保管，避免丢失。

然后，将接口板上的 FPC 排线拔出。

|  |  |
| --- | --- |
|  |  |

### **第 4 步 - 拆下接口板**

握住挤出机接口板，向左微倾后缓慢将其取出。

|  |  |
| --- | --- |
|  |  |

### **第 5 步 - 拆下挤出机线缆**

使用小刀清除接口板上固定挤出机线缆的硅胶。硅胶用于运输过程中的固定连接器，安装时可选择是否重新粘胶。

请小心操作，避免损坏连接器或线缆。

![removing-silicon-glue-around-the-cable-connector.png](https://wiki.bambulab.com/x1/maintenance/th-boards-v9/removing-silicon-glue-around-the-cable-connector.png)

然后，断开**挤出机线缆**连接。

至此，挤出机接口板已成功拆除。

## 安装步骤

### **第 1 步 - 安装接口板**

连接挤出机线缆。然后，将接口板安装回工具头，确保其位置正确。

接着，将 FPC 排线连接到接口板插座上，并使用金属固定夹和螺丝加固。

再拧紧剩余两颗螺丝，并重新连接三根热端线缆。

|  |  |  |
| --- | --- | --- |
|  |  |  |

> **注意**： 请勿将螺丝拧得过紧，以免损坏固定夹或接口板。

### **第 2 步 - 安装工具头前盖**

如下图所示连接前盖电缆，合上前盖。

![](https://wiki.bambulab.com/x1/maintenance/th-boards-v9/disconnect_the_front_housing.jpg)

## 如何验证更换完成/成功

- 检查接口板和各线缆，确认它们都已安装牢固。
- 打开打印机电源，启动**打印校准**流程，并检查是否顺利完成。

![打印校准.png](https://wiki.bambulab.com/x1/maintenance/replace-extruder-connection-board/%E6%89%93%E5%8D%B0%E6%A0%A1%E5%87%86.png)

- 如下图运行**设备自检**操作，如果没有出现错误，则更换成功。

![selftest.png](https://wiki.bambulab.com/x1/maintenance/replace-extruder-connection-board/selftest.png)

- 检查喷嘴与挤出机温度是否高于 0°C。然后将其加热至适合材料（如 PLA 的 220°C），并进行挤出测试。若有顺畅耗材从喷嘴挤出且无异常，即为正常。

|  |  |
| --- | --- |
| 温度2.png | 喷嘴温度.png |

如果您遇到任何问题，请先回看您的步骤，重新检查所有连接。 如果问题仍然存在，请联系服务团队寻求进一步帮助。

## 常见问题及解决方案

1. 挤出机电机不转动： 检查挤出机线缆是否连接稳固。
2. 热端温度无法检测： 检查拆解步骤第 2 步中编号为 1 的接口是否正确连接。
3. 热端不加热： 检查拆解步骤第 2 步中编号为 3 的接口是否连接稳固。
4. 打印机报 HMS 错误： 确认 FPC 排线方向正确并完全插入接口。

## **结束语**

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 如果本指南并未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/cn/im)，我们随时准备为您解答疑问并提供帮助。
>
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
