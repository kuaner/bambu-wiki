---
path: zh/studio-handy/bambu-studio/PLA/PETG-with-bambu-bool-plate-supertack
title: "如何使用拓竹低温增稳打印板打印 Support for PLA/PETG"
description: "本文介绍了如何使用拓竹低温增稳打印板打印 Support for PLA/PETG"
tags: ["bambu studio"]
created: 2024-11-08T10:28:22.009Z
updated: 2024-11-14T09:43:06.792Z
source: https://wiki.bambulab.com/zh/studio-handy/bambu-studio/PLA/PETG-with-bambu-bool-plate-supertack
---

拓竹低温增稳打印板首层不兼容 Support for PLA/PETG，直接在打印板表面打印 Support for PLA/PETG 会损坏打印板，故 Bambu Studio 在切片完成检测到有首层存在 Support forPLA/PETG 时会出现错误提示并禁止打印。

## 打印建议

1.建议在使用 Support for PLA/PETG 时按如下方式选择仅在支撑界面使用支撑材料。

![20241108-182318.jpg](https://wiki.bambulab.com/bambu-studio/pla-petg/20241108-182318.jpg)

2.当打印的模型无法避免在首层使用支撑材料时，可以通过增加阀层（阀层数不小于 2）来避免 Support for PLA/PETG直接打印在打印板上。

![20241108-182336.jpg](https://wiki.bambulab.com/bambu-studio/pla-petg/20241108-182336.jpg)
