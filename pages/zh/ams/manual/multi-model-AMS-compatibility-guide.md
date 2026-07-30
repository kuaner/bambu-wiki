---
path: zh/ams/manual/multi-model-AMS-compatibility-guide
title: "多机型 AMS 连接指南"
description: "本文主要介绍不同代 AMS 与不同打印机机型的兼容性和最大连接数量，以及带烘干功能的 AMS 对供电的要求。"
tags: []
created: 2025-03-25T15:14:57.250Z
updated: 2026-07-29T10:19:54.242Z
source: https://wiki.bambulab.com/zh/ams/manual/multi-model-AMS-compatibility-guide
---

## 使用 AMS 连接打印机

使用 AMS 与打印机连接时，需根据打印机机型，选用适配的 AMS 型号、缓冲器，并为多台 AMS 连接的场景匹配对应的料管拓展口。

### AMS

Bambu Lab AMS 分为一代 AMS、AMS 2 Pro、AMS HT 以及 A 系列专用的 AMS lite。

> **注意**：AMS 自带 6-pin 线缆台阶高度为 1.1 mm，AMS 2 Pro 自带 6-pin 线缆台阶高度为 2.5 mm。  
> ![image6.png](https://wiki.bambulab.com/ams-2-pro/troubleshooting/ams2pro-communication-anomalies/image6.png)

AMS、AMS 2 Pro 和 AMS-HT（后文统称 AMS）均为两级进料，由内部的上下料组件（#1）将耗材送入助力电机（#2）后，助力电机继续将耗材送入打印机的工具头。

由于工具头挤出机消耗的速度和助力电机送料的速度很难完全一致，因此 **AMS 连接打印机时必须通过缓冲器**。

![二级进料.png](https://wiki.bambulab.com/ams/multi-model-ams-compatibility-guide/%E4%BA%8C%E7%BA%A7%E8%BF%9B%E6%96%99.png)

而 AMS lite 为一级进料，耗材由上下料组件直接送入工具头，因此无需通过缓冲器。

![ams_lite1.jpg](https://wiki.bambulab.com/ams/multi-model-ams-compatibility-guide/ams_lite1.jpg)

> 注意：AMS lite 仅兼容 A 系列打印机，且单台 A 系列设备仅允许连接一台 AMS lite。

### 缓冲器

**介绍：** 缓冲器上滑块的滑行距离为耗材提供了一段缓冲长度，AMS 会根据滑块所处位置，及时助力送出耗材，并且不影响工具头挤出。

![](https://wiki.bambulab.com/ams/ams-function-introduction/ams%E5%8A%A9%E5%8A%9B.gif)

**类型：**

| 机型 | 缓冲器 | 购买链接 |
| --- | --- | --- |
| A 系列 |  | [A 系列料线选通器](https://detail.tmall.com/item.htm?abbucket=10&id=985298078348&pisk=gs4KjO0npOXnhJQ1HejgrwXCF31GnGVFKJPXrYDHVReTe8nhaX2oy0HTGDfUE8qteRwtd8FPTbM7F8HuxGb0TWurPt0RoZVFi5lVnJhWAh1SwXL5sDitWvIxPtXcyhAsY907ttg0HltsgAGBRDMC6cGxg4GIVU1tCbhqFewSP1CtgbKBV4MWf5Gq94OBPXi15XlWdLMIFC1taAMSP4wS51hrCYgSPjQ1eAOIEUE_cgfKq6DHPUat9csgOA9SbPGK5xFQSUTWaXnKhWMOp9SMBcNr2zRyymNQ08lbdp6-UPF_RowfIHDQDbF02W_B524UOoi7lT-7H2e-cyi9NENUOv0t1r1k0A4tK8aKfsYxqVamc2ZGb9moJje78JdJP-NgiyoaytpsUkcq5bUPG3H-Vgr3orpt1KDxZH1O63-rAfoc9auE930Q-fHc9aKy4c5Z6xfO63-rAfltn6CJ43oN_&rn=c76321134121994a8d760093406bd115&spm=a1z10.3-b-s.w4011-25177047232.26.495f3c0e9ef5Jd) |
| X1/P1 系列 | 单台 AMS：  多台 AMS： | [供料选通器](https://detail.tmall.com/item.htm?abbucket=10&id=694049363219&pisk=gqKImTfUAWVC8-kKwWkaCyOfl0SWPAoqd86JnLEUeMIdPgOwaySr-4Y1eCR54gJ-tQt56LYEKal3FFOHHwRWEvXRwQd5aeuZ0pvhqghVVmo2KPA5KNdCpkBteT6dwA7dKlAIUghqg0aaBwcF2plA7OMTWtfOpkQd9A_OhtjRp6I-C1B5n_EpwgHsCtB0p7Ed2NCOstyL2gC-X1BfETBLJQptCTfOwgQpwdH1E1C-MM2fF21HdYUB35DLFTvd1uEJv0bCGnUzVu9VpwtDp19wQh6CRsQ5saqDvCJJYHbiRyIkQEOWyIha86LfhC_2RjZBGBXJFTdIm-19ALt1-FPLJtsCOZKdR-kDQaL6fM-KZrvwC6QfbFuiTaSBOEfcJVcMNd1ewH_TOf5yud-d5IhafQbWyHS9vfnf4sEVGxATPR_0VO1qCAaurTcRqfRHT7xVJOXC7AM_9UbdIO1qCAaurwBGd1ksCWLl.&rn=31293cf0ffd658b59b3f384d64734474&spm=a1z10.3-b-s.w4011-25177047232.24.58d73c0ea3rbxh) [料线选通器](https://detail.tmall.com/item.htm?abbucket=10&id=693987695729&pisk=g7dsjEja1lq_KEutDluURR97F11Xh2lzfr_vrEFak1COhste0R5qIxvCkH-fgs8xjnOfv1BDQiSNcsTDV2orab8MSsfK40lzPhfuW_2TX5EVpXQVGNQICY22SsfxcyPxUbTMbSQForQAJ2_VoNF9DtedvMbb6iKAX9EdoZfADnKAvWQfuiET6GeLvMbzW5eTMked7aZOkRKvJ2_cviCABnLKRZjdDjHQPZM1jFgYCUqGomIeWMNYMChcCg_Q3SNf1NB6ZFIB8eRC5OsRhMX0ZCKekCRGKAwOieJWcKK-YRS9FatCUdi713tGkE_vfb45vCTXOOvUXRQ51G6J6OarreWvdB1w6m2k8esOF6JEKcWV1h9lqOHnxnTCbnd1pliF0L8e69t-YWtchKdN9CnKNgyYaggkv-aCES_C42gQn-bmDsmejhrDaOQh59uIRlpcBwbC42gQn-XO-NsER2Z9n&rn=af106227d1721bbedf4ffbbf9b7874f7&spm=a1z10.3-b-s.w4011-25177047232.22.a85c3c0eDs8o9F&skuId=4927627985197) |
| P2S |  | [P2S 供料缓冲器](https://detail.tmall.com/item.htm?abbucket=10&id=985866098141&pisk=ggPEX0Zie6CefRI0urcPQerML6cKibSfT7iSrz4oRDmhe9FrUrZGJaUoV7lzXlDuOXaQbeFa0QOCv9UkabGlci1fGyQKwbjb1whuwH3jk2fSEpvi946P8Z3VGyUK2e-llRffarL8A9voqucij4g-Z40HZNliz2cktYA3ScmtrbckZvDGsq0yZpDuq1Yil2vkEbvHSf0xzbmuqbbaSc3rZ0qoZNziMmU3rCujKwrPGpoPL4DEmymwgPFZ-cvL8c-pA5yILmAjbQAu_2zocMLegTi0HDMj4lf6TbzizlkbLiRU4z4YEAPyxwZ0j8roWRIyUmyuR-eoQwf37XoEE5ZMypGUEkFrpJ8RkPc3X-nxKOIt7WNjUmHwjM4_7DD4Uks9ZDw4Slkb1hOji-Eaaxcc4bx-SqLawJ-kUv0t7m_N714ocZKKDGJHeLHiMVofR29Jev0t7m_N7Lp-Iq3ZcwgC.&rn=ae53e1dfea39e67f80f5e1f19a04a948&spm=a1z10.3-b-s.w4011-25177047232.15.73923c0eJJYz8B) |
| H2 系列 | H2D/H2C： h2dbuffer.avif H2S： h2sbuffer.avif | [H2D/H2C 供料缓冲器](https://detail.tmall.com/item.htm?abbucket=10&id=900120058648&pisk=gWKi2fAc6F7sJ9FEqSSsJN4Pk7gKfGsfZIEAMiCq865IhA9tlokDMIQ4Dd3snxfHG1QOb1EcmKAXMZ-AMn26xQqYXfg63ojA0bh-20psCisqwRMKmXe1HtaauSCVLkSAnPT6ewJ6Ci14pSuJ8di0c-wjut5qKMWVnoSVutoEKtBYui5NuWJF365V0I5a86Wc3oWN0sPEKOBVgO7V0prFCTE4gISqKp5C3iWwgikHL66qisEVZn-BYbSqkaeDjNKhINfyK4Z4mk6Tw_vwzoqc9ObiWd530o-HuNwST1u7pssO1pXMG0Z1bZY2XM-ZTmSyPBxczg0xCNJD-Is9YxzNaFdOYh8u3oJhj6bAIwFit_-6L3sFJ0kkLHO9CHvY3mWpw6J6bimrFGjN_MXBDXZNie82XNsb_jfXxp-wogzb8z7Yao6EHHzblNWCK_3RjqA_v9CHlvD3PV_NdOh-Kv4blNWCK_HnKzN1796tw&rn=d895c4d15ea00645978239829e798c5d&spm=a1z10.3-b-s.w4011-25177047232.21.2bdd3c0eX0i1wm) [H2S 供料缓冲器](https://detail.tmall.com/item.htm?abbucket=10&id=1007207222201&pisk=gS0r2RD0vULyIPpi_f4e0_PDL6a8yyJsq2wQtXc3N82kv33UYfMDwBh3d2zEHxqnPzGS3JDsLWgSRXfUtxauv0wQFJzE9ARXCFTswbULod965ujYfAUOq_qldof0OyPl2Qc_SbUL-p5f-hTZwY_hldTutSA4OWFl-vqhos2YTaboK8qcnWFL-JDnKoc09WBhryqhiE2YTJ2hrkccnWPQtW43qIl0HW43Kvqkgj2Yty2nMchotZP_qQkeqOccBkrzIb2V7j34Z2S-a-7RPqo74Rb_3wbnu7l3CLCP7HwiX8Z_LxYfzyl0Txrs4d7rLXctxouFEQMinDk3MmpFYRonNcn30QYogzyzxqMc9garxY3U205p6j4oHceTqnpYg4g_YREVnLcjg8qZYY9A-8iZixrslt__ScHq8l4G40XLi5CqJ0WhYuVYgRO2gEc3CCB8BKSlvME0WSy6N7sdvuVYgRO2gMILm5F4CQN5.&rn=11ac6df76039049735f8476edd2a1dd4&spm=a1z10.3-b-s.w4011-25177047232.16.24aa3c0eitN4Js&skuId=6004151612379) |
| X2D | filament_buffer-x2d.png | [X2D 供料缓冲器](https://detail.tmall.com/item.htm?abbucket=16&id=1036114211654&pisk=gJjj2SAqcjcXRnyY6jyrFaHa7e-_U8rUhA9OKOnqBnKv5h1P_q-aoPbWB_56bhWTi1s6wOb4nFPmCa1cpE51I-v961C6_ZzzYtXDjhFefkrFn4xEIpfjDKH8Bd9xk88vn0fbQhFUTlZFntxMXt7PxXf-ypAJHmLvH8TJnp-9HILTFQp6KCnA6he7Fd9tDmpxXQdJCdx9Hhdxy3pwpdpvkdnJeQv9XCC9X8tJZdK961KtMPHBCrOchRCjC2A84QBvNcnODlYXOZ0Zfc1yHEsdHQ_Pzg9XlBLOdO_RD_WO0iYulqKGUw11W6FruIQBd_TFlWifOsvOCdCbxvORcOsWoalxkptXGeIvlvyhUFQ5VnSYs2XPFILB4azugF-fGwAHkzVl1TOV6iT-G7RN8TSvP6FrV1Y1Wi-RD7EC4HoeO1jS5YTnfLOUF8giSdV9j77kVVsMkLvXz8wSMNYvELOQF8gEJEpkhBe7FjQ5.&rn=b3cf8202fc9fa046aea076821fdfa0b4&spm=a1z10.3-b-s.w4011-25177047232.37.74773c0ey0Ca3X&skuId=6053876400264) |

### 料管拓展口

**介绍：** 料管拓展口为“四进一出”结构，目的是并联多个 AMS 的料管，满足更多耗材的使用需求。  
**类型：** 料管拓展口分为普通料管拓展口和 H2 系列专用料管拓展口。其中 **H2C 打印机需使用 H2 系列专用料管拓展口；P2S 和 X2D 需使用普通料管拓展口；** 其他型号打印机可根据需求选购。

| 类型 | 图片 | 购买链接 |
| --- | --- | --- |
| 料管拓展口 |  | [料管拓展口](https://detail.tmall.com/item.htm?abbucket=10&id=761478379121&pisk=gxQKjEYHpR23gAU_H2qGryDGnxVgilfUK95jrLvnVOBOeTK3aBXky3pOGHVFETj9eO69dTCzTQ95FTplxl4cT68yP-Y8orfEVNLSU9dBOCNWNQAQsHt9WpEvP-20ycc6YJY5t5ZgUGi6gdOIRH9Q6hOXwUOBdHN9CQd2F26WP5F9ZIMIdHTW1COyZUMBNHOsCBRrdXtBVFN9Zd9WPU6Wf5dyCLTWPjh4edGBE4I1cm1ZfWAEP4_99hZG9dw5bNOd9KCC54gSaBKph69TpJriBh1y2alryn1C0TRfdvwJUNC1Ri6bIDvCDQCc26aI5ebFOit5l8o5HeBJcwttNq1FOpY91ZNo0db9KT_pfS0vqF_DcesgbJxkJIB589h-Pt1Giw-Ny-H6UMA25QQzG0pJVgrhoZH91xvvZDNT60oyAC-09z8e90YC-Cp09znr4hPw6KVT60oyACR9nWF-40-a_&rn=a27d1c6d3ef887905d64d1771cba3506&spm=a1z10.3-b-s.w4011-25177047232.31.4e5a3c0eSrwttP&skuId=5420062635266) |
| H2 系列专用料管拓展口 |  | [H2 系列专用料管拓展口](https://detail.tmall.com/item.htm?abbucket=10&id=995777888055&pisk=gh5sj-xZ1cmsDk4TDczERA6shVAfcyPrfqTArZhZkCd9hIsF0AR4I-XBkMSXgI7Yji1XvCpcQn-wcI_cVyrza77GSIAL4uPyu9bGIQm9DIn2vpLXGFLQC8DVSIAYc2lYU7_GbjaFQqLvJyT2oFhODKnp9HYj6AIvXpnpoEAvDiIv9eLJrFKvDnQppHYsWAht6D3pSFKxBFIx9yTDvndvHiQLRExpDj3jPEw6jNaxCUKiG-8FWHGxM1FDK3OI3jlVBFp1NNKC8w5B5dtJhHvmZ1IFk15MKRM9iwW5ctI8YA-OFUsBUOZS1gsMkZTAf70Wv1_fOdXEXALW1h9R6dgzrwJAd6ON6oDl8wt9FBWUKlJ21G6kqde3xi_BbiC6pcZe0T7F6ps8YXsDhtCw91ELNgyxa3alvxgBEjTB4yaInxY0DIqFjGocadLH5pzQRcBDBeYB4yaInxv9-FtURyiOn&rn=a27d1c6d3ef887905d64d1771cba3506&spm=a1z10.3-b-s.w4011-25177047232.33.4e5a3c0eSrwttP) |

## H2 系列连接指南

- **最大连接数量**：最多支持**同时连接 4 台 AMS 2 Pro 和 8 台 AMS HT。**
- **多色打印支持**：由于 H2C/H2D 为双喷嘴打印机，且最极限的场景可以把所有连接的 AMS 2 Pro/HT 全部连接到同一个喷嘴上，另一个喷嘴使用外挂料盘进料，所以最多可以打印的颜色为 4\*4+8\*1+1（外挂料盘）=**25 色**。 H2S 为单喷嘴打印机，所以最多支持 **24 色**打印。
- **配件需求**：内置缓冲器，**无需额外购买**；部分场景需要购买 [料管拓展口](https://wiki.bambulab.com/zh/ams/manual/multi-model-AMS-compatibility-guide#%E6%96%99%E7%AE%A1%E6%8B%93%E5%B1%95%E5%8F%A3)。

> AMS 与 H2D/H2C 的连接方式相同，可根据需求进行调整，具体请参考：[H2C + 多台 AMS 连接指南](../../h2c/how-to-connect-ams.md)。

### 线缆连接

每台 AMS 背部都有两个 6-pin 口，能够串联起多台 AMS 设备，满足供电与通信需求。

![](https://wiki.bambulab.com/ams-2-pro/manual/6pin%E7%BA%BF%E7%BC%86.png)

> 注意：连接 AMS 2 Pro 或 AMS HT 时，请务必使用标配的新版本 6-pin 连接线，若使用上一代 AMS 的 6-pin 连接线可能导致 AMS 与打印机的通信不稳定，而上一代 AMS 可以兼容新版本的 6-pin 连接线。

### 料管连接

**H2D/H2C**：

- H2D/H2C 的缓冲器具备两个进料口，如果使用一台 AMS + 外挂料盘，或同时使用两台 AMS，可以直接连接在缓冲器上。

![](https://wiki.bambulab.com/ams/multi-model-ams-compatibility-guide/amspro&ht_22.jpg)

- 如需同时使用 2 台 AMS + 外挂料盘，或使用 3 台及以上数量的 AMS ，需要**使用料管拓展口**拓展。**打印机和每台 AMS 之间必须有缓冲器**；因此连接多台 AMS 时，料管拓展口需要连接在 AMS 与 缓冲器之间，请勿接反。

![料管拓展口](https://wiki.bambulab.com/ams/multi-model-ams-compatibility-guide/img_v3_00km_beb23ea0-305b-4dc9-8505-5c35d40b16dg.jpg)

> **注意：**：H2C 设备需要使用 **H2C 专用料管拓展口**。  
> ![](https://wiki.bambulab.com/ams/multi-model-ams-compatibility-guide/h2c_%E4%B8%93%E7%94%A8%E6%96%99%E7%AE%A1%E6%8B%93%E5%B1%95%E5%8F%A3.png)

- 最大连接数量：同时连接 4 台 AMS 2 Pro 和 8 台 AMS HT；

![](https://wiki.bambulab.com/ams-2-pro/manual/%E6%96%99%E7%AE%A1.png)

**H2S：**

- 由于 H2S 为单头打印机，因此 H2S 连接两台 AMS 时，也需使用料管拓展口。

![](https://wiki.bambulab.com/ams/multi-model-ams-compatibility-guide/3.jpg)

## X2D 打印机连接指南

- **最大连接数量**：最多支持**同时连接 4 台 AMS 2 Pro 和 8 台 AMS HT。**
- **多色打印支持**：由于 X2D 为双喷嘴打印机，且最极限的场景可以把所有连接的 AMS 2 Pro/HT 全部连接到同一个喷嘴上，另一个喷嘴使用外挂料盘进料，所以最多可以打印的颜色为 4\*4+8\*1+1（外挂料盘）=**25 色**。
- **配件需求**：超过两台 AMS 的连接场景需要购买[料管拓展口](https://wiki.bambulab.com/zh/ams/manual/multi-model-AMS-compatibility-guide#%E6%96%99%E7%AE%A1%E6%8B%93%E5%B1%95%E5%8F%A3)。

### 线缆连接

每台 AMS 背部都有两个 6-pin 口，能够串联起多台 AMS 设备，满足供电与通信需求。

![x2d-cable.jpg](https://wiki.bambulab.com/ams/multi-model-ams-compatibility-guide/x2d-cable1.jpg)

> 注意：
>
> - 连接 AMS 2 Pro 或 AMS HT 时，请务必使用标配的新版本 6-pin 连接线，若使用上一代 AMS 的 6-pin 连接线可能导致 AMS 与打印机的通信不稳定，而上一代 AMS 可以兼容新版本的 6-pin 连接线。
> - X2D 未连接外排风扇时，缓冲器的两个 6-pin 接口均可连接 AMS 设备。

### 料管连接

- 最大连接数量：4 台 AMS 2 Pro + 8 台 AMS HT + 外挂料盘；

![tube_connection.jpg](https://wiki.bambulab.com/ams/multi-model-ams-compatibility-guide/tube_connection.jpg)

- 仅使用一台 AMS + 外挂料盘，或同时使用两台 AMS 时，可直接连接在缓冲器上；

![ams-external-spool.jpg](https://wiki.bambulab.com/ams/multi-model-ams-compatibility-guide/ams-external-spool1.jpg)

- 使用 2 台 AMS + 外挂料盘，或使用 3 台及以上数量的 AMS 时，需使用**料管拓展口**。

![x2d-ams.jpg](https://wiki.bambulab.com/ams/multi-model-ams-compatibility-guide/x2d-ams.jpg)

> 注意：**打印机和每台 AMS 之间必须有缓冲器**。因此使用多台 AMS 时，料管拓展口需要连接在 AMS 与 缓冲器之间，请勿接反。  
> ![4-in-1-x2d.jpg](https://wiki.bambulab.com/ams/multi-model-ams-compatibility-guide/4-in-1-x2d.jpg)

## X1 /P1 系列打印机连接指南

- **最大连接数量**：X1/P1 最多支持同时连接4台 AMS 2 Pro **或** 4 台 AMS HT，一共4台。
- **配件需求**：

  - X1/P1 连接 1 台 AMS 时，需自行购买 [供料缓冲器，进料管接头，4-pin线](https://detail.tmall.com/item.htm?id=906162436922&pisk=ga-ocFAhwU77MNPqjWSSkanhEi0v2gsCtBEd9MCEus5XvUCKPDDhid7-FBdpo6A2i_JR9YtHoQ9NyBvIF95eTBfpyqn9FLsCYfInXcpWrL6MMQfUztkFLT4EHazRYdDNYfhtXreVPbIeexJlJEJVG9qPL9RUusWRg9WUYB5VuOWTaMSeTxjVKOazazrF0ZW1g85FLazVuO6Q887F8xvVG9XPYMRF0xXCg6SFYbsbY1xecnlNATRo96ZJ0Tbl_L5yeLK43aUWEsxBvnWkEwJzdkremTbkmLeAcgQJ8d_62do3cgpMuiWHAAzhtNYe2i-rgc7f8nRV3QHLRtYHLhs5jJoyngfl7n7Sxvdwnp8OonHZfgjPaeIWpRcJn3AJFnvLLrSl2EbMqGo_a6LvIHXHAXiDspJ68Zx3ZgWUuP7L_k6qpnzQRaWfn13Oq2A5ibg3bxD054_PhThtnx4QRaWfn1HmnPN5zt6-6&skuId=5766287773398&spm=pc_detail.30350276.guessitem.d1)。
  - X1/P1 连接多台 AMS 时，需要购买 [料线选通器](https://detail.tmall.com/item.htm?id=693987695729&pisk=gzhiYqi0XAy1dnSeZiP6pRd0SWvK-5NbmmCYDSE2LkrIMAEvCIY0x4y95mnxKomExluTDFGmKcgzBm0X5rrq0mqxBpd-5VNbg3FDwQ3sIVaovcXauy84oPXwJRWTg4Yzg3KJw9QUChFqWeu0jXuUArfauroVLkzTYrWagmrULzzRbSPq0eVUoz6NbO54TJz7Yt7abO7FYz4GQGyVQe0UArP40myw-2rQuSrqgg54qjlIT3Pb7cxYSMl8SRqr7lutWX7UpOgUxHxEtAca43Ehgsl3SqrJfiCkHuk7X8EmYBCgi2zmx8HMq1mmu4M4KjjwW0oEnmzIdnX0qxutFxyH7Cu3sl2q9D7fB5Dqfj2sIZTS85oIFuwwdHan6be0VJjeb233b8DmXH14XY0Ex8hdv_FrFDc0U7Sy49WzHg5b8EhFhtwaRyqJe5vmfkx6n_8H-T9_Qya92eYhhtwaRyqJ-eX5fRzQW3C..&spm=pc_detail.30350276.guessitem.d3&skuId=4927627985197)，[进料管接头](https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-25177047232.29.22ee3c0eBzRKFx&id=707575712100&rn=badc7578a26628b4999a1abad3488a03&abbucket=10&pisk=gRYx0x_cHYDDo0uSprmkSmjWLGhoq0A4yKRQSOX0fLpJBdIm_svGWGBJOic2IdxRBL9Rhrcq0G693TvgSIY94Pde_EcVSj72gN7sKv0HBIRV73rXT5YYP81DNr1150b7re2lNv0n-QdV7NMnKnmW0a1ltP_1ctO5NT5gh191cQO5U15_hN6jwQ6PFr11hO_5N11dGNaf58a5O6efGGsXNQ6P1N66CNGRPT515O915jnZBTNfIPKWY9AlnDfz5PTRMgikGTg6aU1vD9dXyPa__sIAdI6-HxouegONXFPaWMOXYd5Bh-MOQUdWlH9IEoXXv1dHXIgbPZY2GHs6RAr6pZpOAEs81yO2GtbRNeGgYTYRndTAVX4djaThAZto4xjGk6p6uKFT5pOktESyWve5QnfFP1LZOlBOfg5H-eeRNJXdsoG-wlrNc_SnMV7VMlbXo_BnMVEabglPw9c-wlrNc_5RKjhTblSra)，[4-pin线](https://detail.tmall.com/item.htm?id=694052067560&pisk=g7IZYIfHklEZVTPlUTx48xl27sK9GnP7QiOXntXDCCAgMRpD011Hom6_W-y2Tsd65hb6nm5BOsifCi7K0TBAfRKbBhB9DnV7Nu1VBOKxTjgGAGlnxd6HnjvgRHqchSc3NuZ5BPv9c9V55ybOxp9DmdAMo22eUKHMmEvGKJJDhf0mjsX3LBp2nfvijkDHhKiDmK0MK9vWhI0mjd0hKBpDmIfDmJ-H9KxDisxmgPBGnDJWSR5X3q7Iz7YJZOAEm0kJQF0Vpqir49JM7gAwTeTCYd8wZERpk2jGOtj1XeUZSnBCzs7cZWg6saJPTU_aac5P6KX2n1r-UBjN3M8ORf0MUhRwrGYZF8BBowSefGVxy96esU-CRyF6lh5NyQLgJWCVLC1cbecaOI_5dGYFZWiFME7cfHjgtuSr2jpHevSA7j02SppeNJyUxtA7eh2Xux3xkexJLQw6Cq3vSppeNJyEkqLHepR7Cd1..&spm=pc_detail.30350276.guessitem.d2&skuId=4926397845849)。
  - 部分场景需要购买 [料管拓展口](https://wiki.bambulab.com/zh/ams/manual/multi-model-AMS-compatibility-guide#%E6%96%99%E7%AE%A1%E6%8B%93%E5%B1%95%E5%8F%A3)。

### 连接 1 台 AMS

### 连接多台 AMS

## P2S 打印机连接指南

- **最大连接数量**：P2S 最多支持同时连接 4 台 AMS 2 Pro **和** 4 台 AMS HT，一共 8 台，合计 20 个槽位。
- **配件需求**：
  - P2S-Combo 自带缓冲器，**无需额外购买**；
  - P2S 单机 + AMS 单机时，还需要购买 [P2S 供料缓冲器](https://wiki.bambulab.com/zh/ams/manual/multi-model-AMS-compatibility-guide#%E7%BC%93%E5%86%B2%E5%99%A8)。
  - 部分场景需要购买 [料管拓展口](https://wiki.bambulab.com/zh/ams/manual/multi-model-AMS-compatibility-guide#%E6%96%99%E7%AE%A1%E6%8B%93%E5%B1%95%E5%8F%A3)。

### 线缆连接

缓冲器上有两个 6-pin 插口，可同时连接多台 AMS；AMS 背部也有两个 6-pin 插口，能够相互串联，满足多台 AMS 供电和通信。

![](https://public-cdn.bblmw.com/wiki/new/p2s/manual/diagram1compressed.png)

> 注意：
>
> - 连接 AMS 2 Pro 或 AMS HT 时，请务必使用标配的新版本 6-pin 连接线，若使用上一代 AMS 的 6-pin 连接线可能导致 AMS 与打印机的通信不稳定，而上一代 AMS 可以兼容新版本的 6-pin 连接线。
> - 不支持同时将两台 AMS 设备连接 P2S 缓冲器的两个 6-pin 接口，其中一个接口为备用口，用于为外设（如延时摄影套件）供电及通信扩展。

### 料管连接

- 连接 3 台以下数量的 AMS 时，可直接连接在缓冲器上。

![p2s_ht_ams_2.png](https://wiki.bambulab.com/ams/multi-model-ams-compatibility-guide/p2s_ht_ams_2.png)

- 连接 3 台及以上数量的 AMS 时，需要使用料管拓展口，实现“多进一出”的功能。

> **打印机和每台 AMS 之间必须有缓冲器**。因此使用多台 AMS 时，料管拓展口需要连接在 AMS 与 缓冲器之间，请勿接反。

|  |  |
| --- | --- |
|  |  |

## A1 系列连接指南

- **最大连接数量**：最多支持同时连接 4 台 AMS，可任意搭配（具体请参考：[A 系列 AMS 连接教程](../../a1/manual/ams-connection-guide.md)），或仅连接一台 AMS lite。

![a1-ams.png](https://wiki.bambulab.com/a1/ams-connection-guide/a1_ams.png)

- **配件需求**：需购买 [A 系列料线选通器](https://wiki.bambulab.com/zh/ams/manual/multi-model-AMS-compatibility-guide#%E7%BC%93%E5%86%B2%E5%99%A8)。

![img_v3_02q7_a49d9f49-25a8-49bb-b540-10798bbd15cg.jpg](https://wiki.bambulab.com/ams/multi-model-ams-compatibility-guide/img_v3_02q7_a49d9f49-25a8-49bb-b540-10798bbd15cg.jpg)

- **固件适配计划**： 请将打印机升级至 01.07.00.00 及以上版本。

> **注意：** 请勿使用 AMS 自带的缓冲器或 AMS Hub 连接 A 系列打印机至 AMS，否则会导致缓冲器或 AMS Hub 使用功能异常或损坏，在此种情况下，该缓冲器或 AMS Hub 将不予保修。因此，请您使用 **A 专用的料线选通器**连接 AMS。

## A2L 连接指南

- **最大连接数量**：最多支持同时连接 4 台 AMS 和 1 台 AMS lite，（具体请参考：[A2L AMS 连接指南](../../a2l/manual/a2l-ams-connection-guide.md)），最多可实现 19 色打印；

![image_(85).png](https://wiki.bambulab.com/ams/multi-model-ams-compatibility-guide/image_(85).png)

- **配件需求**：A2L 连接一台 AMS 时，无需额外购买任何配件，直接将打印机与 AMS 通过料管中继接头（工具盒内）连接即可；如需连接两台及以上 AMS，则需购买[料管拓展口](https://wiki.bambulab.com/zh/ams/manual/multi-model-AMS-compatibility-guide#%E6%96%99%E7%AE%A1%E6%8B%93%E5%B1%95%E5%8F%A3)。

### 线缆连接

打印机背部有 1 个 6-pin 插口，可直接连接 AMS 设备；AMS 背部有两个 6-pin 插口，可相互串联多台 AMS，满足多台 AMS 供电和通信。

![image_(86).png](https://wiki.bambulab.com/ams/multi-model-ams-compatibility-guide/image_(86).png)

### 料管连接

- 连接一台 AMS：可直接将 AMS 料管连接至料管中继接头；
- 连接多台 AMS：需用一段 70mm 左右的料管连接料管中继接头和料管拓展口，然后将多台 AMS 的料管连接至料管拓展口，可参考下图。

![料管连接.jpg](https://wiki.bambulab.com/ams/multi-model-ams-compatibility-guide/%E6%96%99%E7%AE%A1%E8%BF%9E%E6%8E%A5.jpg)

## AMS 烘干功能要求

有关 AMS 烘干功能的详细信息，请参考：[AMS 2 Pro 与 AMS HT 耗材烘干指南](../../../en/ams-2-pro/manual/drying-function.md)。

### AMS 2 Pro 烘干供电要求

- H2 系列/P2S 连接一台 AMS 2 Pro 时，可直接通过打印机取电进行烘干，无需额外配件；
- H2 系列/P2S 连接多台 AMS 2 Pro 时，仅其中 1 台可使用打印机供电，其余需通过**专用电源适配器（需单独购买）** 独立供电。

- X1/P1/A 系列使用 AMS 2 Pro 烘干,**每台** AMS 2 Pro 都**必须通过电源适配器**供电才能使用烘干功能。

> 注意：如果**打印机正在进料或者打印，且同时使用打印机供电给 AMS 2 Pro 进行烘干，为了优先确保打印功率，烘干功率自动会降低**，建议外接电源适配器以获得更好的烘干效果。

> **注意**：AMS 2 Pro 官方电源适配器规格为 24V 4A。为确保设备安全与正常使用，**请务必使用官方配件。使用第三方适配器可能会导致设备损坏，并影响保修权益**。

|  |  |
| --- | --- |
|  |  |

### AMS HT 烘干供电要求

无论连接什么型号的打印机，**每台 AMS HT 都需要外接电源才能启用烘干，不支持从打印机取电烘干（电源线标配，无需额外购买）。**

![](https://wiki.bambulab.com/ams/multi-model-ams-compatibility-guide/image-1.png)

### **烘干功能通信要求**

使用烘干功能的时候，**AMS 2 Pro/HT 必须通过 6-pin 连接线与打印机连接通信，不支持离线烘干模式。**

> 注意：请务必使用 AMS 2 Pro 和 AMS HT 标配的新版本 6-pin 连接线，若使用上一代 AMS 的 6-pin 连接线可能导致 AMS 与打印机的通信不稳定，而上一代 AMS 可以兼容新版本的 6-pin 连接线。

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
