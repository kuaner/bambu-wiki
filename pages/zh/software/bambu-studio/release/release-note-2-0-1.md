---
path: zh/software/bambu-studio/release/release-note-2-0-1
title: "Bambu Studio 2.0.1 版本说明"
description: ""
tags: []
created: 2025-03-28T09:27:54.491Z
updated: 2025-03-28T13:23:52.422Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/release/release-note-2-0-1
---

该版本基于2.0.0 Public Release。

## Bugs Fixed

1. 修复了Mac上AMS无法进行手动映射的问题。([#6146](https://github.com/bambulab/BambuStudio/issues/6146), [#6157](https://github.com/bambulab/BambuStudio/issues/6157), [#6163](https://github.com/bambulab/BambuStudio/issues/6163), [#6185](https://github.com/bambulab/BambuStudio/issues/6185), [#6191](https://github.com/bambulab/BambuStudio/issues/6191), [#6195](https://github.com/bambulab/BambuStudio/issues/6195), [#6202](https://github.com/bambulab/BambuStudio/issues/6202), [#6205](https://github.com/bambulab/BambuStudio/issues/6205), [#6217](https://github.com/bambulab/BambuStudio/issues/6217), [#6230](https://github.com/bambulab/BambuStudio/issues/6230), [#6237](https://github.com/bambulab/BambuStudio/issues/6237), [#6246](https://github.com/bambulab/BambuStudio/issues/6246), [#6250](https://github.com/bambulab/BambuStudio/issues/6250))
2. 修复了耗材丝同步功能中在P1S预设下不支持已安装升级套件的P1P的问题。([#6148](https://github.com/bambulab/BambuStudio/issues/6148), [#6149](https://github.com/bambulab/BambuStudio/issues/6149), [#6181](https://github.com/bambulab/BambuStudio/issues/6181), [#6204](https://github.com/bambulab/BambuStudio/issues/6204), [#6208](https://github.com/bambulab/BambuStudio/issues/6208))
3. 修复了校准页面中未显示AMS耗材丝的问题。([#6150](https://github.com/bambulab/BambuStudio/issues/6150), [#6156](https://github.com/bambulab/BambuStudio/issues/6156), [#6182](https://github.com/bambulab/BambuStudio/issues/6182), [#6210](https://github.com/bambulab/BambuStudio/issues/6210), [#6211](https://github.com/bambulab/BambuStudio/issues/6211), [#6218](https://github.com/bambulab/BambuStudio/issues/6218), [#6232](https://github.com/bambulab/BambuStudio/issues/6232), [#6243](https://github.com/bambulab/BambuStudio/issues/6243))
4. 尝试修复Windows上可能出现的安装后Bambu Lab打印机预设消失的问题。([#6166](https://github.com/bambulab/BambuStudio/issues/6166))
5. 优化了发送打印界面中的单喷嘴打印机AMS使用的相关逻辑。当映射至外挂料时点击发送打印，“使用AMS”选项会自动设置为Off。([#6179](https://github.com/bambulab/BambuStudio/issues/6179), [#6203](https://github.com/bambulab/BambuStudio/issues/6203))
6. 优化了部分模型切片时间过长的问题。([#6186](https://github.com/bambulab/BambuStudio/issues/6186))
7. 修复了在部分语言下，自定义耗材名称无法正确显示的问题。([#6190](https://github.com/bambulab/BambuStudio/issues/6190))
8. 修复冲刷乘数不为1时，H2D耗材丝节省量计算错误的问题。([#6214](https://github.com/bambulab/BambuStudio/issues/6214))
9. 修复了H2D 0.12mm层高配置文件中参数错误的问题。([#6169](https://github.com/bambulab/BambuStudio/issues/6169))
10. 修复了Flatpak上部分编译问题，感谢[@hadess](https://github.com/hadess)的贡献。
