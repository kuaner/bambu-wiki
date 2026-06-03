---
path: zh/software/bambu-studio/release/release-note-1-10-2
title: "Bambu Studio 1.10.2  Public Release 版本说明"
description: ""
tags: ["bambu connect", "bambu studio", "studio"]
created: 2025-02-11T08:22:23.581Z
updated: 2025-02-25T08:22:17.253Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/release/release-note-1-10-2
---

## 新功能

1. **首页内置Makerlab**：现在您可以在Studio中使用Makerlab了！

|  |
| --- |
|  |

2. **新增发送到拓竹农场管家功能**：安装[拓竹农场管家客户端](../../bambu-farm-manager.md)后，您可以在 Studio 中完成切片并直接发送至客户端

|  |
| --- |
|  |

## 改进

1. **新增授权和认证保护功能**：Bambu Studio会在打印机支持授权和认证保护功能的情况下，签名和加密发出到打印机的控制命令，由打印机判断是否可以执行。
2. A1 mini新增PLA Glow预设。
3. Bambu Lab打印机新增SUNLU耗材丝预设，感谢[@RikshaDriver](https://github.com/RikshaDriver)的贡献。

## Bug 修复

1. 修复了混合树和苗条树中可能出现的悬空支撑问题。([#5264](https://github.com/bambulab/BambuStudio/issues/5246))
2. 修复了巴西葡萄牙语在Linux中可能出现的加载失败的问题，感谢[@ronoaldo](https://github.com/ronoaldo)的贡献。([#5580](https://github.com/bambulab/BambuStudio/issues/5580))
3. 修复了Linux中下“丢弃或使用修改值”弹框中字体颜色显示的问题，感谢[@D0ot](https://github.com/D0ot)的贡献。([#2731](https://github.com/bambulab/BambuStudio/issues/2731))
4. 修复了部分情况下树状支撑未生成连续顶面支撑层的问题。([#5132](https://github.com/bambulab/BambuStudio/issues/5132))
5. 修复了混合支撑在部分情况下Top-Z参数失效的问题。([#5334](https://github.com/bambulab/BambuStudio/issues/5334))
6. 修复了 Mac 系统下部分场景下剩余打印时间显示异常的问题。([#5294](https://github.com/bambulab/BambuStudio/issues/5294) ,[#5280](https://github.com/bambulab/BambuStudio/issues/5280) , [#5378](https://github.com/bambulab/BambuStudio/issues/5378), [#5299](https://github.com/bambulab/BambuStudio/issues/5299))
7. 修复了部分情况下零件面片无法选择的问题。([#5343](https://github.com/bambulab/BambuStudio/issues/5343))
8. 更新了一些英文翻译内容，感谢[@ping-localhost](https://github.com/ping-localhost)的贡献。
9. 新增耗材丝供应商 LDO，感谢[@camerony](https://github.com/camerony)。
10. 修复了部分第三方打印机GCode导出失败的问题。 ([#5557](https://github.com/bambulab/BambuStudio/issues/5557),[#5614](https://github.com/bambulab/BambuStudio/issues/5614) ,[#5471](https://github.com/bambulab/BambuStudio/issues/5471))
11. 修复了 Fedora 系统中下拉菜单显示错误的问题，感谢[@gw0](https://github.com/gw0)的贡献。([#4201](https://github.com/bambulab/BambuStudio/issues/4201))
12. 修复了在 LAN 模式下打印机连接失败后 access code 可能被清除的问题，感谢[@crashkopf](https://github.com/crashkopf)的贡献。([#4713](https://github.com/bambulab/BambuStudio/issues/4713))
13. 一些编译问题的改进，再次感谢[@hadess](https://github.com/hadess)和[@crashkopf](https://github.com/crashkopf)。
14. 新增耗材供应商FusRock，感谢[@FusRock](https://github.com/FusRock)的支持。
15. 更新Docker构建依赖，感谢[@PatrickChenHZ](https://github.com/PatrickChenHZ)的支持。
16. 更新日语翻译，感谢[@do-gugan](https://github.com/do-gugan)的贡献。
17. 修复了MacOS中在线模型拖拽后的crash问题。([#5967](https://github.com/bambulab/BambuStudio/issues/5967))
