---
path: zh/software/bambu-studio/release/release-note-1-7-3
title: "Bambu Studio 1.7.3版本说明"
description: ""
tags: ["bambu studio", "studio"]
created: 2023-08-08T07:42:29.539Z
updated: 2024-05-28T10:52:54.986Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/release/release-note-1-7-3
---

此版本是 [1.7.2.51](release-note-1-7-2.md)的热修复版本

---

## Bug 修复

1. 在之前的热修复版本 1.7.2.51 和版本 1.7.1.62 中，我们将默认的墙壁生成器切换为Arachne可变线宽。但是，由于一些问题，我们决定在这次热修复中退回Classic墙生成器，并撤销悬垂检测的优化。

在发布1.7版本后，有用户报告在Arachne模式下进行悬垂计算时切片时间变得非常慢。而我们尝试在1.7.2.51中使用一种方法来解决这个问题，但不幸的是，这导致了一些悬垂检测错误。以下是一些生成错误的例子：

![Image 1](https://wiki.bambulab.com/1-7-1-studio-hotfix/1-7-3-studio-hotfix/arachne_1.png)
![Image 2](https://wiki.bambulab.com/1-7-1-studio-hotfix/1-7-3-studio-hotfix/arachne_2.png)

看起来我们最近的悬垂检测方法并不如我们所希望的那样完善。为了确保可靠性和速度，我们已经回到了Classic墙壁生成器。我们正在努力完善Arachne，并将在其性能和稳定性足够好时重新推出这个功能。

对于用户在使用我们最近的更新的软件中遇到的这些问题，我们深感抱歉。您的反馈对我们至关重要，我们真诚地感谢您的耐心和宝贵意见。

2. 修复了在Arachne墙壁生成器中墙顺序不正确的问题。 <https://github.com/bambulab/BambuStudio/issues/2195>
3. 修复了回放界面下点击停止回放引起的UI卡顿问题。
4. 更新 Bambu Cube V2R1。 <https://github.com/bambulab/BambuStudio/issues/2193>
5. 修复树桩支撑在孔洞内生成不正确的问题。

![Image 1](https://wiki.bambulab.com/1-7-1-studio-hotfix/1-7-3-studio-hotfix/tree_support_1.png)
![Image 2](https://wiki.bambulab.com/1-7-1-studio-hotfix/1-7-3-studio-hotfix/tree_support_2.png)

7. 修复将保存流速标定结果时，使用中文名导致崩溃的问题。
