---
path: zh/software/bambu-studio/release/release-note-2-3-0
title: "Bambu Studio 2.3.0 版本说明"
description: ""
tags: []
created: 2025-10-14T11:22:49.276Z
updated: 2025-10-14T14:30:45.980Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/release/release-note-2-3-0
---

V2.3.0新增支持[Bambu Lab P2S](https://bambulab.com/zh/p2s)，并包含若干新功能与问题修复。

![](https://wiki.bambulab.com/bambu-studio/release-note-2-3-0/image.png)

  

## 新功能

### “跳过零件”时跳过无用的换色冲刷

原先跳过单个零件时，仅可跳过某个零件主体的打印，与该零件有关的换料冲刷浪费依然存在。引入该改动后，与该零件相关的无效换色冲刷与在料塔上的无效走线将一并跳过，可有效缩短打印时间、减少材料浪费。目前支持**H2S**和**P2S**。

![](https://wiki.bambulab.com/bambu-studio/release-note-2-3-0/image-1.png)

如果蓝色零件A和黑色零件B打印时跳过黑色零件B，修改前的版本会有黑色的冲刷，以及在料塔上尝试打印黑色耗材。

修改后的版本在跳过黑色零件 B 后，不再出现黑色耗材的冲刷与料塔走线（该场景下新老版本对比，打印时间从约3.5h降为22min，不必要的冲刷从约60g降为0g）。

> ⚠注意：目前该功能**仅支持H2S、P2S**。

  

### **A1/A1 mini支持AMS、AMS HT、AMS 2 Pro**

新增 A1 / A1 mini对 AMS、AMS HT、AMS 2 Pro的支持（需配合专用AMS缓冲器）。切换AMS Lite与AMS/AMS 2 Pro/AMS HT时，请在打印机屏幕或 Studio 的 AMS 设置中同步切换类型。

> **⚠**注意：
>
> - 如需A1/A1 mini搭配AMS使用，请确保Studio版本不低于V2.3.0.70。
> - 最低支持固件版本（A1/A1 mini）：01.06.10.33

|  |  |
| --- | --- |
|  |  |

  

### 布尔工具升级（支持对象级别+多零件输入）

无需额外“组合”步骤，即可在**对象级别**直接进行布尔运算；对象与零件级别均**支持多零件输入**，编辑模型流程更高效。

![2025.gif](https://wiki.bambulab.com/bambu-studio/release-note-2-3-0/2025.gif)

  

### **避免跨越外墙功能优化**

- 优化了层间空驶路径，层间空驶也会避开跨越外墙。

![](https://wiki.bambulab.com/bambu-studio/release-note-2-3-0/image-4.png)

- 新增“避免跨越外墙-包含支撑”选项，启用后空驶路径在计算绕行时将同时考虑支撑分布，进一步降低拉丝风险。该选项尤其适用于鞋打印场景。

![](https://wiki.bambulab.com/bambu-studio/release-note-2-3-0/image-5.png)

  

### **悬垂分段方式优化**

更新了悬垂分段算法，避免因悬垂度突变造成的表面质量波动，提升悬垂区域的稳定性与一致性。

|  |  |
| --- | --- |
|  |  |

  

### **全新使用引导页**

优化了原有使用引导页：可快速访问拓竹学院（Bambu Academy）、Bambu官方耗材指南与更多Bambu Wiki 页面；顶部提供快速搜索 Wiki 的入口。

![](https://wiki.bambulab.com/bambu-studio/release-note-2-3-0/image-8.png)

  

### **H2D/H2D Pro远程自动识别喷嘴**

在“**设备“-“打印机零件”**中点击刷新按钮，可触发H2D/H2D Pro对喷嘴信息的自动识别。识别过程中打印机会短暂运动，请等待30s后喷嘴信息刷新。

![](https://wiki.bambulab.com/bambu-studio/release-note-2-3-0/image-9.png)

  

### 支持外墙不减速

开启后，外墙不会因最小层时间而被强制减速。在Silk/Glossy等材料的特定场景中，可能获得更好的表面一致性效果。

![](https://wiki.bambulab.com/bambu-studio/release-note-2-3-0/image-10.png)

  

### **增加"额外回填长度“**

启用后，在空驶结束后挤出时，会在原回填长度基础上额外增加一段指定长度。该选项仅建议用于部分发泡类材料（如 **Aero**）。

![](https://wiki.bambulab.com/bambu-studio/release-note-2-3-0/image-11.png)

  

### **支撑增加“Z覆盖XY”效果**

开启后，当Top Z覆盖与模型/支撑间距冲突时，算法将优先保证支撑生成在悬垂下方，并在模型与支撑间保留与Top Z一致的间距。可显著改善斜面处的支撑贴合与拆卸体验（尤其适用于采用专用支撑料的场景）。

![](https://wiki.bambulab.com/bambu-studio/release-note-2-3-0/image-12.png)

  

## 优化

1. **修改器支持墙打印调整**：局部可更自由的调整墙顺序，其中修改器、高度范围修改器等均支持。

![](https://wiki.bambulab.com/bambu-studio/release-note-2-3-0/image-13.png)

2. **（Windows平台）支持关闭账户信息自动填充**：为公共场所登录场景提供更好的隐私保护（默认开启）。

![](https://wiki.bambulab.com/bambu-studio/release-note-2-3-0/image-14.png)

3. **冲刷值被修改时显示优化**：当冲刷值偏离默认值时提供更清晰的显示，同时当冲刷值被设为0时提供警告，避免常见的冲刷值配置错误导致的换色质量问题。

![](https://wiki.bambulab.com/bambu-studio/release-note-2-3-0/image-15.png)

4. **新增打印板预设**：H2D/H2D Pro增加**低温增稳打印板**和**工程材料打印板**。

![](https://wiki.bambulab.com/bambu-studio/release-note-2-3-0/image-16.png)

> ⚠注意：H2D将在**后续版本**中支持这两种打印板。

5. 优化了X系列的挤出补偿pattern，避免跟模型重叠。([#5682](https://github.com/bambulab/BambuStudio/issues/5682))

![](https://wiki.bambulab.com/bambu-studio/release-note-2-3-0/image-17.png)

6. 修复Fuzzy Skin绘制无法设置点距和厚度的问题。新增 Disabled档，将原None档与“Fuzzy Skin绘制”逻辑统一。

![](https://wiki.bambulab.com/bambu-studio/release-note-2-3-0/image-18.png)

7. CrossZag 优化：改进顶/底面 Skin 闭合，纹理过渡更自然。

## Bug修复

1. 修复AMS中包含支撑料时，AMS Sync的“覆盖模式”可能导致的崩溃。 ([#7997](https://github.com/bambulab/BambuStudio/issues/7997), [#8204](https://github.com/bambulab/BambuStudio/issues/8024))
2. 修复Arachne模式下精准墙移动方向错误。([#8030](https://github.com/bambulab/BambuStudio/issues/8030))
3. 修复特定移动操作触发的崩溃。([#8094](https://github.com/bambulab/BambuStudio/issues/8094))
4. 修复H2S发送打印文件在低概率情况下失败的问题。([#8091](https://github.com/bambulab/BambuStudio/issues/8091))
5. 修复更新Note时无法保存的错误。([#8081](https://github.com/bambulab/BambuStudio/issues/8081))
6. 修复文字工具部分字体加粗与旧版本不一致的问题。([#8106](https://github.com/bambulab/BambuStudio/issues/8106))
7. 修复 macOS 15在任务结束时的低概率崩溃。([#8174](https://github.com/bambulab/BambuStudio/issues/8174))
8. 优化深色模式下的装配图标显示。([#8170](https://github.com/bambulab/BambuStudio/issues/8170))
9. 修复了AMS在部分场景下排序错误。([#8064](https://github.com/bambulab/BambuStudio/issues/8064))
10. 纠正稀疏填充部分描述错误。([#8202](https://github.com/bambulab/BambuStudio/issues/8202))
11. 修复文字添加后无法居中的问题。([#8224](https://github.com/bambulab/BambuStudio/issues/8224))
12. 修复首层流量比例未能应用于所有零件的问题。([#8249](https://github.com/bambulab/BambuStudio/issues/8249))
13. 修复“仅在打印板上生成”时，个别模型内孔错误生成支撑的问题。([#7826](https://github.com/bambulab/BambuStudio/issues/7826))
14. 加载网络库时校验其数字签名，防止库被篡改并降低安全风险。([#7405](https://github.com/bambulab/BambuStudio/issues/7405))

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
