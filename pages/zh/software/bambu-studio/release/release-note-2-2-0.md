---
path: zh/software/bambu-studio/release/release-note-2-2-0
title: "Bambu Studio 2.2.0 版本说明"
description: ""
tags: ["bambu studio"]
created: 2025-07-18T04:11:16.583Z
updated: 2025-08-13T07:16:20.387Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/release/release-note-2-2-0
---

## 新功能

### Helio Addictive仿真功能集成（Beta）

从这个Public Release开始，我们很高兴将**Helio Additive**的仿真功能引入Bambu Studio。[Helio Additive](https://www.helioadditive.com)是一家专注于G-code仿真与优化的技术提供商。其仿真引擎可在打印开始前预测温度相关问题，如翘曲、粘结不良或下垂。

> 📓**意义**：在打印前及时发现过热或冷却不足的问题——无需反复试错即可提升强度、精度与可靠性。

**使用方法**：

1. 在 **“偏好设置” > “Helio 选项”** 中勾选 **”开启Helio”** 。启用此选项即表示您同意 Helio 隐私政策。

![](https://wiki.bambulab.com/software/bambu-studio/release-note/v2_2_0/helio_.png)

2. 正常对模型进行切片。
3. 点击右上方工具栏中的 **Helio Action** 按钮。
4. 输入预计的腔体温度范围（如已知真实腔体温度，使用真实值可获得更佳效果）。

![](https://wiki.bambulab.com/software/bambu-studio/release-note/v2_2_0/helio_1.png)

5. 点击 **”确认”** 并等待仿真运行完成。
6. 仿真完成后，可在已切片模型上叠加查看热仿真结果。

![](https://wiki.bambulab.com/software/bambu-studio/release-note/v2_2_0/helio_2.png)

**仿真结果基于热力指数值：**• **-100 → 过冷**：拉伸强度可能下降约 50%（基于 ASTM D638 试验）。  
• **0 → 理想**：强度与尺寸精度最佳。  
• **+100 → 过热**：层间保持熔融时间过长，容易导致下垂或塌陷。  
  
建议尽量让零件的大部分区域接近 0，以获得最佳机械性能。

**⚠ 当前限制与支持配置**

- **支持的打印机**：Bambu Lab X1/X1C/X1E、H2D
- **支持的耗材**：Bambu PLA Basic、PLA Lite、PLA Matte、PLA Silk+、Bambu ABS、PC、PETG HF、TPU 95A HF
- **G-code要求**：G-code 必须为**单色逐层**顺序切片（暂不支持多色或多材料）。
- **功能范围**：当前版本仅支持热仿真功能，G-code优化将在后续版本中推出。
- **功能Beta期间免费使用**：在该期间，您可通过领取**限量免费密钥**免费使用Helio（1000个）。密钥发放完毕后，Helio将暂停并在下一阶段释放更多名额。

如需了解详情或获取更多帮助, 加入[Helio Additive Discord](https://discord.com/invite/EjQXDJP9kS).

  

### Bambu Studio支持远程零件跳过

您现在可以在打印过程中，直接通过Bambu Studio远程跳过零件，实现与H2D和X系列打印机屏幕相同的功能。这使您无需停留在打印机旁，就能停止打印特定零件。  
**使用方法**：

- 打印过程中，点击打印机状态栏中的 “跳过” 按钮。
- 将打开零件跳过界面，您可以手动选择要跳过的对象。

![](https://wiki.bambulab.com/studio_releasenote/2_2_0_public/cn-1.png)

![](https://wiki.bambulab.com/studio_releasenote/2_2_0_public/cn-2.gif)

**最低支持固件版本**：

- X1C：01.09.02.12
- H2D：01.02.00.00
- 其他机型：将在后续固件中逐步支持

> ⚠️ 请确保您的打印机固件已更新至最新版本，以使用此功能。

  

### Fuzzy Skin绘制功能

Bambu Studio 新增了**FuzzySkin绘制工具**，让您对打印效果拥有更好的控制。该工具可像涂色模块一样，在模型表面指定FuzzySkin生效的区域。您可以为模型的侧面添加FuzzySkin（不包含顶部与底部表面）。

![](https://wiki.bambulab.com/software/bambu-studio/release-note/v2_2_0/fuzzy_1.png)

![](https://wiki.bambulab.com/studio_releasenote/2_2_0_public/cn-3.gif)

🙌 感谢
[@hejllukas](https://github.com/hejllukas)
对该功能的贡献。

  

### 耗材颜色选择优化

该优化为耗材颜色选择流程带来两项改进，聚焦色觉障碍用户以及使用官方Bambu耗材的用户使用体验提升。

- **官方颜色表集成**：  
  当选择耗材颜色时，会显示当前耗材类型支持的**官方颜色表**。该颜色表包含已知的**Bambu官方颜色名**及其**Filament Code**，这有助于更快速方便的选择到对应的耗材。如果想要的颜色不在官方颜色表中，点击“**其他颜色**”来使用原系统调色盘。

|  |  |
| --- | --- |

- **AMS颜色显示优化**  
  在**AMS材料设置**中，如果使用的是**带RFID的Bambu官方耗材**，它的官方颜色名同样会显示在界面中。

  

### 支持外挂料盘实现无AMS下的换料

对于多个耗材映射到同一个外挂的场景，（配合支持该功能的固件）在**发送打印任务窗口**中勾选此选项后，即可实现手动换料打印。当需要进行换料时，打印机会自动暂停并提醒客户进行换料。该功能适合于**没有AMS场景下的多色打印**。

![](https://wiki.bambulab.com/studio_releasenote/2_2_0_public/cn-6.png)

> ⚠️ 注意：该功能需配合**后续固件**更新使用。

  

### Seam避开悬垂（实验性功能）

Seam出现在悬垂位置时会导致低附着力和不稳定性，进而引起打印失败。此实验性功能旨在使Seam尽可能避开悬垂区域，以提升打印成功率。

|  |  |
| --- | --- |

🧪 特别鸣谢 @Onkelsam 提供的测试模型帮助验证了该问题。

  

### 支持按高度线性降低速度/加速度上限

现可在**零件/修改器**级别设置**速度和加速度上限**，此上限可以在**指定高度区间内线性变化**，有效降低**高瘦模型**的失败风险。

|  |  |
| --- | --- |

  

### 用户预设批量管理器

通过“**文件-批量预设管理**”打开后，可查看当**前预设数量**及**云端存储上限**，支持**批量删除打印机、耗材与工艺预设**。如果你频繁被预设超过云端上限困扰，希望这个功能可以有效的帮助到你。

|  |  |
| --- | --- |

  

### Bambu打印机支持第三方打印机的校准功能（开发者模式）

支持在**开发者模式**下，对Bambu打印机（不包含H2D）中**运行原第三方打印机的多种流量校准模型**。  
具体模型及操作方式参考[Bambu Wiki](../../../bambu-studio/Calibration.md)。感谢[@logikal](https://github.com/logikal)的贡献。

![](https://wiki.bambulab.com/software/bambu-studio/release-note/v2_2_0/disanfang.png)

> ⚠️ 注意，Bambulab无法为这些校准功能提供支持。我们仍然建议使用Bambu Studio中提供的默认校准选项。

  

### 涂色工具优化

填充功能增加了新模式“连接相同颜色”选项，支持对一个颜色联通的区域全部填充为目标颜色。

|  |  |
| --- | --- |

  

### H2D机型AI检测新增各子功能开关

针对H2D提供了更详尽的AI检测子功能设置，你可以更精准的控制AI检测的范围和灵敏度。

![](https://wiki.bambulab.com/software/bambu-studio/release-note/v2_2_0/ai_dect.png)

  

## 改进

### 新增裹头检测功能：

为了解决H2D打印过程中的裹头问题，我们在工艺预设中新增了“**启用触碰裹头检测**”选项（**默认关闭**）。启用该功能后，Studio会在打印板顶端添加一个不可打印区域，用于配合固件进行裹头检测。同时根据打印板上零件类型对料塔进行调整：

- **打印单色模型时**：额外生成一个高度为20层的料塔；若零件本身不足20层，则料塔与零件等高。
- **打印多色模型时**：若已有料塔高度大于20层，保留原结构；若不足20层，则自动补齐至20层。

**最低支持固件版本**：H2D 01.01.30.00 Public Beta及以后。

> ⚠️ 注意：该功能依赖对应版本的固件支持。

![](https://wiki.bambulab.com/software/bambu-studio/release-note/v2_2_0/guo_tou_jian_ce.png)

  

### 文字工具更新

支持更多字体库、提升了拖动文字的交互性能、新增文字环绕投影模式，并可将文字直接设置为负零件或修改器。另外，我们新增了备用字体的功能，即字符串中包含当前字体不支持的字符时，会使用备用字体进行替代。([#7322](https://github.com/bambulab/BambuStudio/issues/7322), [#5578](https://github.com/bambulab/BambuStudio/issues/5578)).

![](https://wiki.bambulab.com/studio-print-all/pixpin_2025-08-13_15-12-57.png)

> **注意：** 旧版本项目导入后，对原项目中文字编辑时，可能在字体大小及加粗效果有细微差别，可手动调整。

🙌 感谢
[@Jony01](https://github.com/Jony01)
和
[@Noisyfox](https://github.com/Noisyfox)
对该功能的贡献。

  

### 优化速度平滑功能

对过渡区域中的速度突变问题进行了修复，速度过渡更加平滑。

|  |  |
| --- | --- |

  

### 首页布局优化

对主页侧边栏的分类与整体布局重新调整，以提供更简洁、更直观的用户体验。

![](https://wiki.bambulab.com/studio_releasenote/2_2_0_public/cn-20.png)

  

### Gizmo工具栏自动折叠：

该功能主要针对小窗口与低分辨率屏幕进行显示优化，画布长度不足时自动将工具折叠至Gizmo尾部。可在偏好设置的“3D设置-工具栏风格”中关闭该功能。

|  |  |
| --- | --- |

  

### Scarf Seam 选项添加至工艺选项卡：可覆盖耗材设置中 Scarf Seam 的选项。

在工艺选项卡中增加了Scarf Seam覆盖选项，该选项开启后，工艺选项中的Scarf Seam参数可覆盖当前耗材设置中Scarf Seam参数。([#5287](https://github.com/bambulab/BambuStudio/issues/5287)).

![](https://wiki.bambulab.com/software/bambu-studio/release-note/v2_2_0/scarf_seam.png)

  

### 优化H2D耗材预设配置

针对H2D的Bambu ABS/ASA/PLA Basic/PLA Matte/PETG HF和PC增加单独的0.6mm喷嘴与0.8mm喷嘴预设，并适当提高体积流量参数，在保证质量的前提下提高打印速度。  
优化Bambu ABS的冷却参数，避免ABS材料在打印过程中出现散热不足问题。

  

### 切割工具性能优化

优化了进入切割工具时的性能，在多面片场景下明显提升模型的加载速度。

![](https://wiki.bambulab.com/software/bambu-studio/release-note/v2_2_0/qiege.gif)

🙌 感谢@Wholeheartedness的模型。

  

### 侧边栏宽度可调整

现在支持通过拖动侧边栏边缘来调整其宽度。([#7377](https://github.com/bambulab/BambuStudio/issues/7377), [#7300](https://github.com/bambulab/BambuStudio/issues/7300), [#7313](https://github.com/bambulab/BambuStudio/issues/7313), [#7454](https://github.com/bambulab/BambuStudio/issues/7454), [#7221](https://github.com/bambulab/BambuStudio/issues/7221), [#7238](https://github.com/bambulab/BambuStudio/issues/7238))

![](https://wiki.bambulab.com/software/bambu-studio/release-note/v2_2_0/cebian.gif)

> 注意：首次在扩展显示屏中运行可能因覆盖安装不生效，重启软件后按 Ctrl+W 重置即可继续调整侧边栏宽度。

  

### 其他改进

1. 兼容MacOS15编译：更新了Boost与JPEG库依赖项。
2. Locked Zag的表皮和骨架提供纹理选择入口。用户可以自行选择不同纹理改善强度，拼接不同的外观花纹。

![](https://wiki.bambulab.com/software/bambu-studio/release-note/v2_2_0/locked_zag.png)

3. H2D 0.2mm预设中禁用**PLA Glow**和**PVA**材料以防止堵头。
4. 优化部分UI：包含Locked Zag子参数UI优化、切片模式增加UI提示说明和打印机零件框中的Wiki入口。

|  |  |
| --- | --- |

![](https://wiki.bambulab.com/software/bambu-studio/release-note/v2_2_0/locked_zag_1_3.png)

5. 优化了测量工具的值复制功能。([#7426](https://github.com/bambulab/BambuStudio/issues/7426))
6. MacOS增加 **Command + Shift + Z (⌘ + ⇧ + Z)** 为重做快捷键，感谢@coreyward的贡献。
7. 更新了部分土耳其语翻译，感谢@fatih5228的贡献。

  

## Bug 修复

1. 优化了最小冲刷值显示的问题。([#7423](https://github.com/bambulab/BambuStudio/issues/7423), [#7455](https://github.com/bambulab/BambuStudio/issues/7455))
2. 修复了部分风扇值显示错误的问题。 ([#7440](https://github.com/bambulab/BambuStudio/issues/7440))
3. 修复了登录页空白的问题。([#7353](https://github.com/bambulab/BambuStudio/issues/7353), [#7469](https://github.com/bambulab/BambuStudio/issues/7469), [#7304](https://github.com/bambulab/BambuStudio/issues/7304), [#7329](https://github.com/bambulab/BambuStudio/issues/7329), [#7344](https://github.com/bambulab/BambuStudio/issues/7344), [#7230](https://github.com/bambulab/BambuStudio/issues/7230), [#7315](https://github.com/bambulab/BambuStudio/issues/7315), [#7403](https://github.com/bambulab/BambuStudio/issues/7403), [#7529](https://github.com/bambulab/BambuStudio/issues/7529))
4. 修复了部分条件下Finish Time不显示的问题。([#7401](https://github.com/bambulab/BambuStudio/issues/7401), [#7237](https://github.com/bambulab/BambuStudio/issues/7237))
5. 修复了Linux Wayland平台下Canvas3D无法正确渲染的问题。([#7343](https://github.com/bambulab/BambuStudio/issues/7343), [#6632](https://github.com/bambulab/BambuStudio/issues/6632), [#6985](https://github.com/bambulab/BambuStudio/issues/6985), [#6215](https://github.com/bambulab/BambuStudio/issues/6215))
6. 修复了部分情况下料塔切片crash的问题。([#7064](https://github.com/bambulab/BambuStudio/issues/7064))
7. 修复了部分模型中跨越外墙导致的模型质量下降。([#7452](https://github.com/bambulab/BambuStudio/issues/7452), [#7240](https://github.com/bambulab/BambuStudio/issues/7240))
8. 修复了P1P使用升级套件后同步打印机信息可能出现的报错问题。([#7395](https://github.com/bambulab/BambuStudio/issues/7395))
9. 修复了MacOS 26可能出现的Crash问题。([#7367](https://github.com/bambulab/BambuStudio/issues/7367), [#7424](https://github.com/bambulab/BambuStudio/issues/7424), [#7422](https://github.com/bambulab/BambuStudio/issues/7422), [#7540](https://github.com/bambulab/BambuStudio/issues/7540))
10. 修复了MacOS中生成的GCode可能导致的擦料塔碰撞错误。([#7437](https://github.com/bambulab/BambuStudio/issues/7437))
11. 修复了Mac休眠后唤醒可能导致的崩溃问题。  
    ([#7432](https://github.com/bambulab/BambuStudio/issues/7432), [#7291](https://github.com/bambulab/BambuStudio/issues/7291), [#7203](https://github.com/bambulab/BambuStudio/issues/7203), [#7179](https://github.com/bambulab/BambuStudio/issues/7179), [#7207](https://github.com/bambulab/BambuStudio/issues/7207), [#7239](https://github.com/bambulab/BambuStudio/issues/7239), [#7254](https://github.com/bambulab/BambuStudio/issues/7254))
12. 修复了部分3mf中因包含“Extra length on restart”而导致的回抽计算错误。([#7222](https://github.com/bambulab/BambuStudio/issues/7222))
13. 修复了若干拼写错误，感谢[@eried](https://github.com/eried)的贡献。
14. 修复了创建耗材预设对话框无法正确缩放的问题，感谢[@gunlock](https://github.com/gunlock)的贡献。
15. 修复了部分第三方机型发送打印后crash的问题。([#7295](https://github.com/bambulab/BambuStudio/issues/7295), [#7392](https://github.com/bambulab/BambuStudio/issues/7392))
16. 修复了Obj导入后耗材重复添加的问题。([#7682](https://github.com/bambulab/BambuStudio/issues/7682))
17. 修复了H2D左右喷嘴直径不一致时无法发起校准的问题。([#7543](https://github.com/bambulab/BambuStudio/issues/7543))
18. “偏好设置-3D设置”中增记忆颜色方案的选项，打开后会在重启Studio时记忆上次关闭Studio的颜色方案。([#7252](https://github.com/bambulab/BambuStudio/issues/7252))

![](https://wiki.bambulab.com/software/bambu-studio/release-note/v2_2_0/studio.png)

19. 修复了偏好设置中关闭在线模型选项失效的问题。([#7719](https://github.com/bambulab/BambuStudio/issues/7719))
20. 修复了H2D G-Code在层高/流量预览时的显示错误。([#7750](https://github.com/bambulab/BambuStudio/issues/7750))
21. 修复了删除耗材预设时可能造成的支撑筏层设置不生效的错误。([#7704](https://github.com/bambulab/BambuStudio/issues/7704))
22. 修复了支撑料菜单不显示耗材数字和颜色的错误。([#7637](https://github.com/bambulab/BambuStudio/issues/7637))
23. 修复了因复制零件导致的可变层高打印对象切片错误。([#7583](https://github.com/bambulab/BambuStudio/issues/7583))
24. 修复了部分flathub的编译问题，感谢[@hadess](https://github.com/hadess)的贡献。
