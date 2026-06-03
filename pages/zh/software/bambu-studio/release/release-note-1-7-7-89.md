---
path: zh/software/bambu-studio/release/release-note-1-7-7-89
title: "Bambu Studio 1.7.7.89 版本说明"
description: ""
tags: ["bambu studio", "studio"]
created: 2023-10-12T09:45:42.108Z
updated: 2024-09-04T13:14:22.521Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/release/release-note-1-7-7-89
---

这是一个基于1.7.7.88的Bambu Studio增强版本, 包括一些功能优化和错误修复。

# 优化

1. 将开门打印的提示从发起打印界面转移到每日tips。  
   在封闭机箱内使用PEI热床打印时，由于热床温度较高，腔温在打印过程中会逐步升高造成耗材阻塞挤出机，详细说明见[wiki](../../../filament-acc/filament/heat-creep.md)。  
   在前一个版本中，发起打印时会对gcode中热床温度的检查，并在gcode热床温度较高时提示用户打开机箱进行打印。  
   然而大量用户反馈每次发送打印都有相关提示过于繁琐，因此这个版本我们将这个提示放到每日tips中，用户发起打印时不再提示。  
   ![20231013-103619.jpg](https://wiki.bambulab.com/1-7-8-studio-version/20231013-103619.jpg)  
   请用户自行阅读[wiki](../../../filament-acc/filament/heat-creep.md)，打印前决定是否打开箱门和顶盖，以预防打印过程中堵头。

# 修复

1. 修复P1P逐件打印模式下摆盘异常的问题
2. 修复A1 mini切片预览时，统计的耗材冲刷量不对的问题
3. 修复德语下PA校准K值不显示的问题https://github.com/bambulab/BambuStudio/issues/2689
