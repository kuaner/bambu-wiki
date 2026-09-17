---
path: zh/ams/manual/multi-model-AMS-compatibility-guide
title: "多机型 AMS 连接指南"
description: "本文主要介绍不同代 AMS 与不同打印机机型的兼容性和最大连接数量，以及带烘干功能的 AMS 对供电的要求。"
tags: []
created: 2025-03-25T15:14:57.250Z
updated: 2026-08-28T06:21:31.350Z
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

  

## AMS 连接指南

> 请点击下列按钮，选择您的打印机型号，以查看对应打印机的连接指南。

- H2 系列
- X2D
- X1 /P1 系列
- P2S
- A1 系列
- A2L
