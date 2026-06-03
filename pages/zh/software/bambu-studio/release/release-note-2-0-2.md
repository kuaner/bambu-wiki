---
path: zh/software/bambu-studio/release/release-note-2-0-2
title: "Bambu Studio 2.0.2 版本说明"
description: ""
tags: ["bambu studio", "studio"]
created: 2025-04-15T12:27:48.633Z
updated: 2025-04-16T07:14:54.161Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/release/release-note-2-0-2
---

## Improvements

1. Studio设备页面支持 P1 系列／X1系列（不包含X1E） 打印机在连接AMS 2 Pro和AMS HT场景下的耗材设置。

- X1 系列固件版本不低于 01.09.00.00。
- P1 系列固件版本不低于 01.08.00.00。

2. 支持在Studio上通过子网绑定方式连接X1系列打印机（X1 系列固件版本不低于 01.09.00.00）。

|  |
| --- |
|  |

3. 根据用户反馈优化了“发送打印“页面。

- 打印选项从可折叠隐藏改为常显示。
- 打印选项相关介绍从常显示改为悬浮提示。
- 各机型自动记忆上次打印选项设置。
- 重构AMS映射界面，取消X1 系列、P1 系列、A1 以及 A1 mini 的"启用AMS" 选项。当用户需要使用外部料盘打印时，可通过在映射框选中外部料盘实现。

|  |  |
| --- | --- |
|  |  |

4. 更新了11种语言的翻译，同时感谢[@fatih5228](https://github.com/fatih5228)贡献的土耳其语翻译。

## Bugs Fixed

1. 修复windows arm平台下载网络插件后程序崩溃的问题。([#6360](https://github.com/bambulab/BambuStudio/issues/6336), [#6171](https://github.com/bambulab/BambuStudio/issues/6171), [#6283](https://github.com/bambulab/BambuStudio/issues/6283), [#6295](https://github.com/bambulab/BambuStudio/issues/6295), [#6117](https://github.com/bambulab/BambuStudio/issues/6117), [#6063](https://github.com/bambulab/BambuStudio/issues/6063), [#6014](https://github.com/bambulab/BambuStudio/issues/6063))
2. 修复了第三方3mf导入后可能出现的错误提示。([#6336](https://github.com/bambulab/BambuStudio/issues/6336))
3. 修复了”切片所有盘”未跳过空盘继续切片的问题。([#6276](https://github.com/bambulab/BambuStudio/issues/6276))
4. 修复了 GCode 在 Mac 上部分情况下无法正确打开的问题。([#6231](https://github.com/bambulab/BambuStudio/issues/6231))
5. 修复了Mac上文字功能部分字母无法输入的问题。([#6222](https://github.com/bambulab/BambuStudio/issues/6222))
6. 修复了切割时旋转平面无法正确调整的问题。([#6300](https://github.com/bambulab/BambuStudio/issues/6300))
7. 修复了小键盘Enter键输入失效的问题。([#6167](https://github.com/bambulab/BambuStudio/issues/6167))
8. 修复了部分3mf导入后Scarf Seam不生效的问题。([#6320](https://github.com/bambulab/BambuStudio/issues/6320))
9. 修复了MakerWorld中Image-to-3D生成的OBJ导入Studio后崩溃的问题。([#6333](https://github.com/bambulab/BambuStudio/issues/6333))
10. 修复了流量校准结果无法修改的问题。([#6274](https://github.com/bambulab/BambuStudio/issues/6274))
11. 修复了预设选择时tooltip的显示错误。([#6380](https://github.com/bambulab/BambuStudio/issues/6380))
12. 修复了可能出现的Mac插件替换错误。([#6340](https://github.com/bambulab/BambuStudio/issues/6340))
13. 优化了尖尾情况下树状支撑的形态以保证打印质量。([#6371](https://github.com/bambulab/BambuStudio/issues/6371))
14. 为保证打印质量，我们关闭了除H2D的PLA、PETG以外耗材的风扇提前开启功能。([#6177](https://github.com/bambulab/BambuStudio/issues/6177))
15. 修复了部分step文件导入后crash的问题。([#6079](https://github.com/bambulab/BambuStudio/issues/6079))
16. 修复了发送失败后，不能点击取消再发送的错误。([#6216](https://github.com/bambulab/BambuStudio/issues/6216))
17. 修复了部分情况下Mac电脑休眠唤醒后打印机未自动重连的问题。([#6311](https://github.com/bambulab/BambuStudio/issues/6311))
18. 修复了俄罗斯语下冲刷体积窗口显示错误的问题。([#6483](https://github.com/bambulab/BambuStudio/issues/6483))
19. 修复了Brim绘制功能的内存泄露问题，感谢[@Noisyfox](https://github.com/Noisyfox)的贡献。
