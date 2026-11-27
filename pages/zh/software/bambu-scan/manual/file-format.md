---
path: zh/software/bambu-scan/manual/file-format
title: "文件格式"
description: "Bambu Scan 支持以下文件格式。"
tags: []
created: 2026-11-26T14:02:06.220Z
updated: 2026-11-27T02:37:51.988Z
source: https://wiki.bambulab.com/zh/software/bambu-scan/manual/file-format
---

Bambu Scan 支持以下文件格式。

|  | 格式 | 类型 | 说明 | 支持导入 | 支持导出 |
| --- | --- | --- | --- | --- | --- |
| Bambu Scan专用格式 | \*.bspr(z) | 项目（索引）文件 | *.bspr为Bambu Scan项目索引文件。项目以文件夹形式保存，包含该项目下的所有子项目。* .bsprz为Bambu Scan 压缩项目格式，便于项目备份与分享。 关于项目文件和子项目更多说明，参考[项目系统部分](project-system.md)。 | √ | √ |
|  | \*.bssub | 子项目文件 | 包含单次扫描的帧数据、点云、网格及后处理数据。 | √ | √ |
|  | \*.bspreset | 预设文件 | Bambu Scan扫描预设或者封装预设的存储格式。 | √ | √ |
| 通用格式 | \*.stl | 网格文件 | 常见的三角网格格式，通常不包含颜色信息，可导入Bambu Studio 进行切片打印。 | √ | √ |
|  | \*.ply | 网格文件 | 常见网格格式。 | √ | √ |
|  | \*.obj | 网格文件 | 常见的网格格式，可通过关联材质及纹理文件保存颜色信息。可导入Bambu Studio 进行切片打印。 | √ | √ |
|  | \*.asc | 点云文件 | 文本格式的点云文件，用于保存点的三维坐标等信息。 | √ | √ |
|  | \*.stp | CAD文件 | STEP 格式的 CAD 模型文件，用于高级编辑中测量模块使用。 | √ |  |

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
