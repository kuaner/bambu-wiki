---
path: zh/software/bambu-studio/release/release-note-1-7-7
title: "Bambu Studio 1.7.7 版本说明"
description: ""
tags: ["bambu studio", "studio"]
created: 2023-10-09T07:12:06.062Z
updated: 2024-05-28T10:59:40.929Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/release/release-note-1-7-7
---

这是一个基于[1.7.6.92](https://github.com/bambulab/BambuStudio/releases/tag/v01.07.06.92)的Bambu Studio版本, 支持Bambu Lab X1E，以及包括一些改进和错误修复。

# 新增功能

1. 支持Bambu Lab X1E  
   ![](https://wiki.bambulab.com/software/bambu-studio/release-note/v1_7_7/x1e.png)

# 优化

1. 支持在打印完成后对MakerWorld中的模型进行评分  
   ![](https://wiki.bambulab.com/software/bambu-studio/release-note/v1_7_7/ratings.png)
2. 调整诸如PLA、PVA、TPU、PETG-CF等材料的软化温度，并优化了在热床温度达到材料软化温度时的打印提示  
   ![](https://wiki.bambulab.com/software/bambu-studio/release-note/v1_7_7/soften_temperature1.png)
3. 更新A1 mini的启动G-code，缩短启动时的原料线长度，并更改X轴频率扫描
4. 在A1 Mini上使用纹理PEI打印板时，去除“动态流程校准”的提示.
5. 将PolyLite PETG的最大体积流量设置为11.5 mm^3/s

# 修复

1. 修复了在创建和删除盘之后出现的内存泄漏问题;
2. 修复在动态流量校准页面下，“动态流量校准结果”窗口在没有历史值时出现的闪烁问题；
3. 修复 [问题 2589](https://github.com/bambulab/BambuStudio/issues/2589): 手动流量比例校准在德语语言中报告了无效的 K 值；
4. 修复 [问题 2473](https://github.com/bambulab/BambuStudio/issues/2473): 当进行流量比例校准时报告错误信息："未处理的未知异常，终止应用程序"；
5. 修复 [问题 2582](https://github.com/bambulab/BambuStudio/issues/2582): 将Kobra Max打印机的更换材料G代码从M600修改为M601，以防止在打印过程中发生某些崩溃；
6. 修复 [问题 2346](https://github.com/bambulab/BambuStudio/issues/2346): 加载材料时按钮文字不正确；
7. 修复 [问题 2533](https://github.com/bambulab/BambuStudio/issues/2533): 无法使用AMS打印PLA Aero；
8. 修复 [问题 2633](https://github.com/bambulab/BambuStudio/issues/2633): 在访问SD卡窗口时崩溃；
9. 修复 [问题 2573](https://github.com/bambulab/BambuStudio/issues/2573): 在Mac OS启动时出现随机崩溃；
