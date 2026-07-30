---
path: zh/ams-2-pro/ams-2-pro-for-drying-in-x1-p1-series
title: "使用 X1/P1S 打印机连接 AMS 2 PRO 进行烘干"
description: "本文介绍了使用 X1/P1S 打印机连接 AMS 2 PRO 进行烘干的注意事项和步骤。"
tags: ["ams", "drying"]
created: 2025-07-02T08:23:47.135Z
updated: 2026-07-09T10:02:04.563Z
source: https://wiki.bambulab.com/zh/ams-2-pro/ams-2-pro-for-drying-in-x1-p1-series
---

AMS 2 Pro 不仅是一套多色打印供料系统，还内置了干燥模块，可用于保持耗材处于最佳的干燥状态。本文将为您详细介绍如何在 X1/P1 系列打印机上使用 AMS 2 Pro 进行耗材干燥。

## 为什么要对耗材进行干燥？

1. **避免打印缺陷**：潮湿的耗材会导致气泡、拉丝、层间附着不良，从而造成打印缺陷。
2. **提升力学性能**：干燥的耗材能减少因水汽造成的挤出空隙，使打印件更坚固耐用。
3. **改善表面质量**：去除水分可消除表面瑕疵，使打印表面更平滑、专业。
4. **减少堵头与卡料问题**：干燥的耗材可防止喷嘴堵塞与送料异常，确保稳定挤出。

## 所需设备

1. X1/P1 系列 3D 打印机
2. AMS 2 Pro
3. AMS缓冲器（或多个 AMS 时使用料线选通器）。购买链接： [耗材缓冲器](https://item.jd.com/10060212416887.html) 或 [AMS 集线器（料线选通器）](https://detail.tmall.com/item.htm?id=693987695729&pisk=gQPEYSZie6CeC3iKK5GybcUgtNlKibSbK7iSrz4oRDmhe9FrUrZGJaUoV7lzXlDuOXaQb0qb44NQNzYrrlGneJiSA0lzyo71cs1bJyh-sisfGG3yZjlvKpmkVhAiRbuHpw4jiyh-Zg86Zt14JkEjJ6vnrVbZP4tHtuDksVmtz2muqDDMj43-ZbqoxhviRqKnqvDHINuq8BYHZBvGsqgxreqoZNliX4corucoi_43rCujKaQAZndpYkMEmymwgPFZ-dnVMcAkC50U7maheQAu_2kUsoP1WwMQErHYOrfy6Xa4If0zwZvr4xyuOfVhjsDtE5qiSk_WeVyzrShKgUf37XoEn5DdaaZ07z2jQ5_cMXlnx8GLPESQ7WrQJ5zWrdcEORk4Tjfvx0w_u7uzwgCa0z4YEAPyYgP62VD3c7eeqLknWVof7NlSguy2cXfdPLp-Ij3ZcwgBeLH3fQ9UgI9JeA0Z7m_BZ&rn=98d268de7bf5190d27950c88e8aa85ce&spm=a1z10.3-b-s.w4011-25177047232.25.26e23c0ed4WR9b&skuId=4927627985197)
4. 6 pin 和 4 pin 数据线（AMS 2 Pro 随附）
5. PTFE 料管
6. AMS 2 Pro 专用电源适配器（用于开启干燥功能），可通过 [Bambu Lab 官方商店](https://detail.tmall.com/item.htm?abbucket=15&id=901639674058&pisk=glBrYMbD98eyE9LJZt9EuEIi8m9JKpz1Z9TBxMjHVUYu97BeTG_02kIHR9JFkZAhFLs5ueb18H65dMmexZ9k9_TBPeJFvNrb5Rw12gppnPa_C8ngsTvttHAnRxmDfp-owuj6IgppKyojK5wN2aQ62HGkxnq2AHgkxwAHm-YvYeDh-UAmoHKpKpbHZIADAHLHqvDlmo-Wx3cHrbcmohKnZ2bHKoSDkHvHqwvnMFjlxx-6ZkETpj2gLeAySgYqQiB2qFcR4Euozt52aFD6uvDh33Se4QCIQWTG6UO68Z2jUpSDYZR1aPkP8MjOtIWEru_Go67HDsUETF5hV1CHgu2l0L8ytt_mvb9PtaBew_oLXivlk1L9ZSUv0T66TFdqozjf0UANTaaxKU1NmZR1hqM6I1QVLCvG4GgpmQb1p_unTQxv0FZ40p9N81u6E8EI9XdDBn8_V3GK9QbjdbWZCXhpin-25uMh.&rn=9bcf506d7ca48c3fe87985b17ae97a1f&spm=a1z10.3-b-s.w4011-25177047232.16.245b3c0eXA3ooH&skuId=5927195091249) 购买。**如需多个 AMS 2 Pro 同时干燥，每个都需单独配备电源适配器。**

> **注意**：AMS 2 Pro 官方电源适配器规格为 24V 4A。为确保设备安全与正常使用，**请务必使用官方配件。使用第三方适配器可能会导致设备损坏，并影响保修权益**。

## 如何使用 AMS 2 Pro 进行耗材干燥

请按照以下步骤，在 X1/P1 系列上使用 AMS 2 Pro 进行耗材干燥：

### 步骤 1：更新固件

X1/P1 系列需通过 2025 年 4 月底发布的固件更新开启 AMS 2 Pro 的干燥功能。未更新固件时，该功能无法使用。  
请参考以下链接更新固件：

- [X1 固件更新指南](../x1/manual/X1-firmware-update-support-ams2pro-ams-ht.md)
- [P1 固件更新指南](../p1/manual/p1-firmware-update-support-ams2pro-ams-ht.md)

> **注意：** 固件需在连接 AMS 2 Pro 前完成更新，以避免初始化失败。

### 步骤 2：连接 AMS 2 Pro 与 X1/P1 打印机

用两颗 M3×21.5 螺丝将耗材缓冲器固定到打印机上，将 550 mm PTFE 管一端连接至 AMS 2 Pro 的出料口，另一端连接至缓冲器左侧端口；再将 370 mm PTFE 管一端接到缓冲器右侧端口，另一端接入打印机背面进料口。

![connecting_ams_2_pro_to_3d_printer.png](https://wiki.bambulab.com/ams-2-pro/manual/using-ams-2-pro-for-drying/%E8%BF%9E%E6%8E%A51.png)

接着，使用 4-pin 连接线一端连接打印机，另一端接入缓冲器底部接口；再用 6-pin 连接线连接 AMS 2 Pro 与缓冲器左侧。若为多个 AMS 2 Pro 设备，请改用 AMS 料线选通器。  
![connecting_ams_2_pro_to_3d_printer.png](https://wiki.bambulab.com/ams-2-pro/manual/using-ams-2-pro-for-drying/%E8%BF%9E%E6%8E%A5.png)

### 步骤 3：连接电源适配器

将电源适配器插入 AMS 2 Pro 电源接口。  
![connecting_the_switching_power_adapter.png](https://wiki.bambulab.com/ams-2-pro/manual/using-ams-2-pro-for-drying/connecting_the_switching_power_adapter.png)  
如未连接适配器尝试干燥，会弹出提示“电源不足”，且干燥图标为灰色；接入适配器后图标会变为绿色。

|  |  |
| --- | --- |
|  |  |

### 步骤 4：放入干燥剂与耗材

AMS 2 Pro 使用变色硅胶干燥剂（干燥为黄色，吸湿饱和变为紫色），请将其放置于 AMS 2 Pro 中部靠后区域。

|  |  |
| --- | --- |
|  |  |

随后，将**缠好的料盘** 、放置进 AMS 2 Pro，避免旋转烘干时散开。

> **注意：** 干燥时请勿将耗材插入进料口，否则会提示你需要退料。同时你也可以在**烘干准备**页面选择烘干时是否旋转料盘（如下左图）。

|  |  |
| --- | --- |
|  |  |

关闭 AMS 2 Pro 顶盖以确保密封，再开启 3D 打印机。

### 步骤 5：启动干燥程序

#### 在 X1C 上进行干燥

在屏幕中进入 **耗材** 页面，点击 AMS 湿度图标进入 **烘干和湿度** 页面，或从设置中进入 **AMS 烘干** 选项。

|  |  |
| --- | --- |
|  |  |

选择要干燥的耗材。对于 Bambu Lab 自有耗材，RFID 可自动识别设置（温度与时间）；也可手动调整，最大温度为 65°C。例如 PLA 建议设置为 45–55°C，时间 6–8 小时。

![filament_and_humidity_settings.png](https://wiki.bambulab.com/ams-2-pro/manual/using-ams-2-pro-for-drying/%E5%BC%80%E5%A7%8B.jpg)  
点击“开始”即可启动干燥。

另外，AMS 2 Pro 内置加热干燥模块位于中框下方，最高干燥温度为 65°C，可满足多数耗材干燥需求。但部分高温耗材干燥需求超过该温度，系统会提示您建议使用 AMS HT。  
![filament_and_humidity_settings.png](https://wiki.bambulab.com/ams-2-pro/manual/using-ams-2-pro-for-drying/%E6%B8%A9%E5%BA%A6%E6%9C%89%E9%99%90.jpg)

#### 在 P1 上启动干燥

选择**控制**菜单下的**烘干**选项。  
![filament_and_humidity_settings.png](https://wiki.bambulab.com/ams-2-pro/manual/using-ams-2-pro-for-drying/%E6%8E%A7%E5%88%B6.jpg)

正确连接 AMS 2 pro 和电源线并进入烘干页面后会显示“可用”。  
![filament_and_humidity_settings.png](https://wiki.bambulab.com/ams-2-pro/manual/using-ams-2-pro-for-drying/%E5%8F%AF%E7%94%A8.jpg)

如耗材已进料，会提示您退料和卷好耗材。  
![filament_and_humidity_settings.png](https://wiki.bambulab.com/ams-2-pro/manual/using-ams-2-pro-for-drying/%E6%94%B6%E8%B5%B7%E8%80%97%E6%9D%90.jpg)

> **注意：** 干燥前必须确认关好 AMS 2 Pro 上盖以保证密封性。

检查或修改好烘干预设和干燥时间后，选择开始烘干即可。  
![filament_and_humidity_settings.png](https://wiki.bambulab.com/ams-2-pro/manual/using-ams-2-pro-for-drying/%E5%BC%80%E5%A7%8B%E7%83%98%E5%B9%B2.jpg)

### 步骤 6：监测湿度

X1 系列可点击屏幕左上角查看实时温湿度信息，若连接多个 AMS，可在此切换查看每台设备的状态，包括湿度、温度与剩余时间。

|  |  |
| --- | --- |
|  |  |

P1 系列也可在屏幕中通过按键点击查看干燥进度。

![filament_and_humidity_settings.png](https://wiki.bambulab.com/ams-2-pro/manual/using-ams-2-pro-for-drying//%E6%B8%A9%E5%BA%A6%E9%A2%84%E8%AE%BE.jpg)

> 注意：干燥过程中，AMS 2 Pro 会通过底部通风孔排出湿气，请确保通风口畅通无阻。![vent_holes_in_ams_2_pro.png](https://wiki.bambulab.com/ams-2-pro/manual/using-ams-2-pro-for-drying/vent_holes_in_ams_2_pro.png)

## 干燥完成后的操作

### 步骤 1：待 AMS 2 Pro 冷却

若使用较高温度，建议等待 5–10 分钟冷却。

### 步骤 2：取出耗材并检查

取出耗材后，确认其表面光滑无潮湿感，同时检查是否有变形、压痕或散开等异常。如耗材干燥良好，即可开始打印或密封保存，建议使用带干燥剂的密封盒保存以防返潮。

## 常见问题与排查建议

1. **无法启用干燥功能**：请确认固件已更新至支持 AMS 2 Pro 干燥功能版本。
2. **提示“电源不足”**：干燥模块需外接电源，连接 Bambu Lab 官方电源适配器即可。**我们建议您使用拓竹官方电源适配器，用第三方电源适配器可能无法正常启用烘干功能。且因第三方电源适配器带来的硬件损坏，不在产品保修范围内。**
3. **干燥后其他耗材变形**：烘干高温耗材时需要将低温耗材取出，如烘干 ABS 时，AMS 中不能放置 PLA 耗材。
4. **干燥效果不佳**：请确认耗材类型及设置是否正确。如为高温材料，可改用 AMS HT 或使用热床干燥。参见此篇 Wiki：[耗材烘干操作指南](../filament-acc/filament/dry-filament.md)

## 结语

> 希望本指南对您有所帮助。如有疑问，请随时联系 Bambu Lab 客服支持。  
> [点击此处](https://bambulab.com/en/my/support/tickets) 提交服务请求，我们将尽快为您提供帮助。
