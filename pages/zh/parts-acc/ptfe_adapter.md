---
path: zh/parts-acc/ptfe_adapter
title: "料管拓展口"
description: "关于四进一料管拓展口与 H2C 专用料管拓展口的用途说明"
tags: ["料管扩展口"]
created: 2024-01-12T13:56:39.225Z
updated: 2026-06-17T09:17:20.150Z
source: https://wiki.bambulab.com/zh/parts-acc/ptfe_adapter
---

## 料管拓展口

料管拓展口能够同时连接 4 个 AMS 到 3D 打印机。其进端有 4 个孔，通过插入四根铁氟龙料管连接至 AMS 或外挂料盘。出端为1孔，通过一根铁氟龙料管与打印机相连。

料管拓展口有两种型号，料管拓展口一代和四进一料管拓展口二代。

|  |  |
| --- | --- |
|  |  |
| 料管拓展口 | 四进一料管拓展口二代 |

相较于普通料管拓展口，H2C 新版本四进一料管拓展口在出口端集成了一块**清洁刮片**，用于拦截耗材碎屑与其他表面灰尘，将碎屑阻挡在刮片外侧，防止其进入工具头，从而减少堵塞和无线通信异常的风险。

> 📌**注意：** H2C 打印机需使用 [四进一料管拓展口二代](https://detail.tmall.com/item.htm?abbucket=10&id=995777888055&pisk=gh5sj-xZ1cmsDk4TDczERA6shVAfcyPrfqTArZhZkCd9hIsF0AR4I-XBkMSXgI7Yji1XvCpcQn-wcI_cVyrza77GSIAL4uPyu9bGIQm9DIn2vpLXGFLQC8DVSIAYc2lYU7_GbjaFQqLvJyT2oFhODKnp9HYj6AIvXpnpoEAvDiIv9eLJrFKvDnQppHYsWAht6D3pSFKxBFIx9yTDvndvHiQLRExpDj3jPEw6jNaxCUKiG-8FWHGxM1FDK3OI3jlVBFp1NNKC8w5B5dtJhHvmZ1IFk15MKRM9iwW5ctI8YA-OFUsBUOZS1gsMkZTAf70Wv1_fOdXEXALW1h9R6dgzrwJAd6ON6oDl8wt9FBWUKlJ21G6kqde3xi_BbiC6pcZe0T7F6ps8YXsDhtCw91ELNgyxa3alvxgBEjTB4yaInxY0DIqFjGocadLH5pzQRcBDBeYB4yaInxv9-FtURyiOn&rn=a27d1c6d3ef887905d64d1771cba3506&spm=a1z10.3-b-s.w4011-25177047232.33.4e5a3c0eSrwttP)；P2S 和 X2D 打印机需使用[四进一料管拓展口一代](https://detail.tmall.com/item.htm?abbucket=10&id=761478379121&pisk=gxQKjEYHpR23gAU_H2qGryDGnxVgilfUK95jrLvnVOBOeTK3aBXky3pOGHVFETj9eO69dTCzTQ95FTplxl4cT68yP-Y8orfEVNLSU9dBOCNWNQAQsHt9WpEvP-20ycc6YJY5t5ZgUGi6gdOIRH9Q6hOXwUOBdHN9CQd2F26WP5F9ZIMIdHTW1COyZUMBNHOsCBRrdXtBVFN9Zd9WPU6Wf5dyCLTWPjh4edGBE4I1cm1ZfWAEP4_99hZG9dw5bNOd9KCC54gSaBKph69TpJriBh1y2alryn1C0TRfdvwJUNC1Ri6bIDvCDQCc26aI5ebFOit5l8o5HeBJcwttNq1FOpY91ZNo0db9KT_pfS0vqF_DcesgbJxkJIB589h-Pt1Giw-Ny-H6UMA25QQzG0pJVgrhoZH91xvvZDNT60oyAC-09z8e90YC-Cp09znr4hPw6KVT60oyACR9nWF-40-a_&rn=a27d1c6d3ef887905d64d1771cba3506&skuId=5420062635266&spm=a1z10.3-b-s.w4011-25177047232.31.4e5a3c0eSrwttP)； 其他型号打印机可根据需求选购。

有关更换清洁刮片的教程请参考: [H2C 四进一料管拓展口料线清洁刮片 | Bambu Lab Wiki](../h2c/maintenance/replace-4in1-ptfe-adapter-filament-cleaning-pad.md)

## 安装示意图

### 情况一：连接更多的 AMS

> 该情况需确保料管拓展口安装在缓冲器与 AMS 之间。

以 H2C 为例，H2C 的缓冲器安装在打印机右上角，因此 1 个出口与缓冲器相连，而 4 个入口可连接 4 台 AMS，或连接额外的料管拓展口。

![](https://wiki.bambulab.com/part_acc/ptfe_adapter/h2c_4_in_1_ptfe.jpg)

以 P2S/X2D 为例，其缓冲器安装在背板中间位置，因此 1 个出口与缓冲器相连，而 4 个入口可连接 4 台 AMS，或连接额外的料管拓展口。

|  |  |
| --- | --- |
| P2S | X2D |

其他机型的连接方式可根据缓冲器安装位置进行选择。

### 情况二：连接更多的外挂耗材

**P2S / X2D / H 系列打印机**：

这些机型的缓冲器均集成了缠料检测功能，因此，需确保料管拓展口安装在**缓冲器与外挂料盘**间。使用多个耗材时，耗材需先经过料管拓展口，再进入缓冲器，最后进入机器内。故连接方式与**情况一**相同：料管拓展口的出口连接缓冲器，4 个入口连接外挂料盘，让耗材先经过料管拓展口，再进入缓冲器（具体可请参考情况一）。

- **若全部连接外挂料盘**：4 个入口分别接 4 个外挂料盘。
- **若需同时连接外挂料盘与 AMS**：将外挂料盘与 AMS 混接到 4 个入口即可，连接位置规则不变。  
  这样即可在使用外挂料盘时，依然保留缠料检测功能。

**X1 / P1 系列打印机**：

可以直接将料管拓展口安装在进料口上，P1P 设有螺丝孔位固定料管拓展口。

|  |  |
| --- | --- |
|  |  |

#### 示例

|  |  |  |
| --- | --- | --- |
| induction | 序号 | 耗材来源 |
| 1 | 料盘支架 ，临时的打印需求 |
| 2 | AMS （缓冲区或料线选通器） ，用于多色打印 |
| 3 | 干燥箱1（TPU）特殊材料打印 |
| 4 | 干燥箱2（PC）特殊材料打印 |

1. 使用 AMS 输送的耗材，在不打印时，会自动回收到 AMS 内，这时如果需要使用不存放于 AMS 内的耗材进行临时的打印，可以将耗材挂到料盘支架上，通过1号入口，完成手动上料，即可开始打印；

2. 如果需要使用保存条件要求较高的材料进行打印，在将料盘支架上的耗材回退出拓展口后，可以使用外置的干燥盒，通过3号或4号入口，完成手动上料，即可开始打印。

使用料管拓展口连接 AMS 时，请确保铁氟龙料管路径通畅无弯折，避免因料管扭曲而增加进料阻力。

有关各机型使用料管拓展口连接多个 AMS 的详细方法与示例，[请参考该wiki](../ams/manual/multi-model-AMS-compatibility-guide.md)。

## 结束语

> 我们希望这份指南为您提供了有效的信息，并真实地帮助了您。
>
> 如果您对本文中描述的过程有任何疑虑或疑问，您可以在开始操作前联系我们的客户服务团队。 我们随时准备为您提供帮助并回答您的任何问题。
