---
path: zh/software/bambu-studio/release/release-note-1-7-2
title: "Bambu Studio 1.7.2 版本说明"
description: ""
tags: ["bambu studio", "studio"]
created: 2023-08-04T13:16:33.381Z
updated: 2024-05-28T10:52:42.859Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/release/release-note-1-7-2
---

此版本是 [V1.7.1.62](release-note-1-7.md) 的热修复版本

## 改进

### 提升切片15%阶段的速度

从1.7.1版本开始，默认的墙生成器已经切换为可变线宽的Arachne。与经典的墙生成器相比，Arachne更复杂。许多用户反馈，在切片复杂模型时，15%切片阶段的处理时间显著增加。因此，我们优化了同时使用Arachne和悬垂减速功能场景的切片速度。

下方是对同一个 [3mf](https://wiki.bambulab.com/1-7-1-studio-hotfix/test_slicing_speed.3mf) 切片的速度对比：

|  |  |
| --- | --- |
|  |  |

然而，如果模型极其复杂（例如，在切浮雕的时候）切片速度过慢，我们建议切换到经典壁层生成器或禁用悬垂减速功能。请参考以下的例子：

![](https://wiki.bambulab.com/1-7-1-studio-hotfix/screenshot-20230804-211218.png)

性能问题并非总是能在短时间内解决，但我们会像往常一样继续优化。

如果你遇到任何问题或有什么意见，请不要犹豫向我们提出，我们非常欢迎用户提供的所有建设性反馈和建议！

### 支持arachne同时使用顶面单层墙或最顶面单层墙

顶面单层墙选项对于提高顶面质量非常重要。自从在V1.7.0公开测试版中将默认的壁层生成器切换到Arachne后，用户反馈顶面质量变差，因为原始的Arachne不能同时和顶面单层墙一起使用。

我们之前测试过这个选项，发现和Arachne同时使用会导致很多模型切片过程太慢。然而，我们找到了初步解决方案，现在这个选项已经在发布版本中可用。

现在你可以使用Arachne墙生成器的同时，使用“仅最顶面单层墙”或"所有顶面单层墙"选项。"仅最顶面"选项只能让最顶层成为单壁层，但是当模型非常复杂时，它的切片速度比"全部顶面"快得多。

请查看下面的对比：

![](https://wiki.bambulab.com/1-7-1-studio-hotfix/20230804-205405.jpg)

## Bug 修复

1. 修复Studio和打印机之间同步出错导致的一些动态流量校准出错的问题。
2. 修复流量比例校准结果显示错误的问题。
3. 修复保存校准结果为中文名时崩溃的问题。
4. 修复翻译问题和校准图片显示问题。
5. 改善一些第三方打印机预设，感谢来自 @OrcaSlicer 的贡献，感谢 SoftFever 的提交。
6. 修复无AMS时，进退料按钮消失的问题 <https://github.com/bambulab/BambuStudio/issues/2145>
7. 修复Windows版本网络插件安装问题。
8. 修复当盘名太长时，发送打印失败的问题。
9. 修复Linux版本无法切换盘视图的问题 <https://github.com/bambulab/BambuStudio/issues/2140>
