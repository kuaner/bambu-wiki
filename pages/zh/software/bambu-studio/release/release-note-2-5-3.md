---
path: zh/software/bambu-studio/release/release-note-2-5-3
title: "Bambu Studio 2.5.3 版本说明"
description: ""
tags: []
created: 2026-04-14T10:45:07.999Z
updated: 2026-07-03T04:27:21.613Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/release/release-note-2-5-3
---

V2.5.3版本新增对Bambu Lab X2D的支持，同时包含了若干新功能、改进与Bug修复。

![x2d.png](https://wiki.bambulab.com/software/bambu-studio/release-note/v2_5_3/x2d.png)

## 新功能

### 混色打印（实验性功能）

混色打印功能现已上线。在耗材项目列表中底部点击“添加混色耗材”后，可在弹窗中配置混色耗材。

了解更详细的使用方法，请参阅这篇 wiki：[**混色打印**](../../../bambu-studio/color-mixing.md)。

![小船.jpeg](https://wiki.bambulab.com/software/bambu-studio/release-note/v2_5_3/%E5%B0%8F%E8%88%B9.jpeg)

- 支持2种或3种同类型耗材进行混色。
- 混色模式介绍：  
  1.普通模式：双色或者三色可使用比例框中的色盘条或者色盘三角形来进行调整，或直接从下方推荐颜色中选择。搭配拓竹 CMYK 耗材套装，即可呈现多种颜色效果，如左图所有小船均为使用拓竹CMYK耗材套装在单盘中打印。  
  2.渐变模式：基于双色的渐变色彩效果，可实现丰富的过渡色打印效果，如右图所示的双色上下渐变过渡效果。

颜色预测部分参考了@ratdoux在OrcaSlicer-FullSpectrum 中的方案，感谢他的出色工作。 其余部分均由 Bambu Studio 团队独立开发完成。

![混色1.png](https://wiki.bambulab.com/software/bambu-studio/release-note/v2_5_3/%E6%B7%B7%E8%89%B21.png)

---

![混色2.png](https://wiki.bambulab.com/software/bambu-studio/release-note/v2_5_3/%E6%B7%B7%E8%89%B22.png)

> ⚠️注意：
>
> 1. 本功能为实验功能，含混色耗材的3mf暂不支持上传至MakerWorld。
> 2. 该功能仅适用于接近垂直的墙，不适合用于斜坡和顶面/底面的叠色；
> 3. 不建议单头打印机使用（换色频繁、耗材浪费），推荐使用多头打印机获取更好效果；
> 4. 0.4mm喷嘴条件下，固定层高建议使用0.12mm、叠层层高建议使用0.2mm来获得较为均匀的混色效果。应避免使用极端叠层比例，避免过小层高触发熔体破裂导致打印质量下降；
> 5. 叠层颜色的预估模型尚不够准确，对颜色要求高的用户建议提前打印小测试块观察结果精调。

### 支持耗材变轨器

耗材变轨器支持将 AMS 中的耗材同时送入多挤出机设备（H2C/X2D）的左右喷嘴，此时切片允许单个耗材使用不同喷嘴打印。

![变轨器2.png](https://wiki.bambulab.com/software/bambu-studio/release-note/v2_5_3/%E5%8F%98%E8%BD%A8%E5%99%A82.png)

耗材变轨器有效减少不必要的冲刷次数，提升了使用AMS打印的便捷性。

![变轨器1.png](https://wiki.bambulab.com/software/bambu-studio/release-note/v2_5_3/%E5%8F%98%E8%BD%A8%E5%99%A81.png)

软件 UI 显示：

|  |  |
| --- | --- |
| 变轨器3.png | 变轨器4.png |

> ℹ️Tip：仅在通过同步按钮同步已安装耗材变轨器的设备后，才会在打印机预设和设备页面中显示，并在切片模式中启用智能分配模式。  
> ![变轨器5.png](https://wiki.bambulab.com/software/bambu-studio/release-note/v2_5_3/%E5%8F%98%E8%BD%A8%E5%99%A85.png)  
> ⚠️固件最低支持版本：01.02.00.00（H2C）、01.01.00.00（X2D）

### 风扇速度支持线性过渡控制

现在支持对部件及辅助风扇的转速进行更精准的逐层控制，风扇转速将从起始层数的设定值线性过渡至目标速度。可改善首层附近的散热条件，降低因骤冷导致的翘边或首层失败概率。

|  |  |
| --- | --- |
| 风扇2.png | 线性.png |

### H2D/H2C/X2D 新增参数“开启料塔接触层优化”(开发者模式)

启用后，对料塔接触层单独设置温度、预挤出和冲刷参数，提升多材料切换时的打印质量，并有效降低耗材粘性差异较大时的料塔倒塌风险。

![擦料塔优化.png](https://wiki.bambulab.com/software/bambu-studio/release-note/v2_5_3/%E6%93%A6%E6%96%99%E5%A1%94%E4%BC%98%E5%8C%96.png)

### 装配预览功能

新增装配预览功能，支持用户在更改配色或涂色后实时查看整体装配效果。可通过视图中的视角按钮调整预览角度。可在“偏好设置”-“3D设置”中对该功能进行开启或关闭。更多详情参考[整体视图](../../../bambu-studio/assembly-view.md)。

|  |  |
| --- | --- |
| 装配1.png | 装配2.png |

> ℹ️Tip：为获得最佳装配预览效果，建议创作者导入完整的整体模型文件，而非分散的单独零件。

### 降低打印过程中的倒塌风险

本次从支撑和料塔角度进行优化，降低打印过程中的倒塌概率：

- P2S机型现默认启用擦料塔熨烫功能： 在多材料混打场景中，可有效提升擦料塔层间粘附力，降低擦料塔倒塌风险。
- 树状支撑底部新增倒角设计（从 2mm 的高度处向外扩），有效降低支撑倒塌风险。同时优化了支撑节点合并时的半径计算逻辑，提升支撑形态的一致性与准确性。

![支撑1.png](https://wiki.bambulab.com/software/bambu-studio/release-note/v2_5_3/%E6%94%AF%E6%92%911.png)

---

![支撑2.png](https://wiki.bambulab.com/software/bambu-studio/release-note/v2_5_3/%E6%94%AF%E6%92%912.png)

### Liveview 连接或切换设备时展示静态预览帧

在云端或 LAN 模式下，Liveview 未自动播放时，设备页Liveview页面显示当前设备的静态预览帧。

![预览帧1.png](https://wiki.bambulab.com/software/bambu-studio/release-note/v2_5_3/%E9%A2%84%E8%A7%88%E5%B8%A71.png)

> ⚠️固件最低支持版本：01.02.00.00（P2S），01.01.00.00（X2D）

### 模糊皮肤功能支持新噪声类型和生成器模式

除经典（Classic）模式外，Fuzzy Skin新增以下4种噪声类型（Noise Type）：

- Perlin（柏林噪声）
- Billow（云状噪声）
- Ridged Multifractal（脊状多重分形）
- Voronoi（维诺图）  
  同时新增绒毛表面生成器模式：
- 位移:通过让喷嘴相对原始路径左右偏移形成纹理。
- 挤出:通过改变挤出量形成纹理(喷嘴走线保持平直)。
- 组合:位移+挤出。观感接近位移模式,且能填补圈与圆之间的间隙

> ℹ️Tip：挤出与组合模式仅在Arachne（可变线宽）模式时，“绒毛表面厚度”不大于“实际打印线宽”的场景下生效。

感谢[@Arachnid](https://github.com/Arachnid) 的贡献。

![模糊皮肤.png](https://wiki.bambulab.com/software/bambu-studio/release-note/v2_5_3/%E6%A8%A1%E7%B3%8A%E7%9A%AE%E8%82%A4.png)

### 新增熨烫风扇速度控制

可单独配置熨烫过程中的风扇转速, 将此参数调低时可降低因低体积流量导致的喷嘴堵塞风险，使熨烫表面更加平滑（默认设为 -1 时不启用）。  
感谢[@Noisyfox](https://github.com/Noisyfox)的贡献。

![熨烫风扇.png](https://wiki.bambulab.com/software/bambu-studio/release-note/v2_5_3/%E7%86%A8%E7%83%AB%E9%A3%8E%E6%89%87.png)

### Helio 功能更新

对 Helio 集成进行了全面升级，涵盖性能大幅提升、结果展示与引导更清晰、兼容性处理扩展，以及工作流稳定性改进。

> 适用范围与限制：
>
> - Helio 目前支持除X2D外的所有 Bambu Lab 打印机。
> - 如需了解受支持的打印机与材料详情，请访问 [https://wiki.helioadditive.com/en/supportedprinters。](https://wiki.helioadditive.com/en/supportedprinters%E3%80%82)

#### 产品与定价更新（Alpha → Beta）

- Helio 正式从 Alpha 升级至 Beta，定价方案全面简化，在[合理使用范围](https://wiki.helioadditive.com/zh/policies/fair)内，Assess/Enhance 功能近乎无限量使用。原配额/Token 计费体系已停用。
- 新用户可享受 2 周免费试用，试用期内可使用全部功能。
- 产品命名更加清晰：
  - Assess（原 Simulation）：在打印前预测可能出现的失败点。
  - Enhance（原 Optimization）：自动修复并生成优化速度方案，可针对打印速度、强度、可靠性及表面光泽度进行自动优化。
- 改进了激活流程。

#### 性能提升

Helio 的 Assess 与 Enhance 均已支持 GPU 加速，相较于之前版本运行时间显著缩短（在支持的场景下最高可提速约 5 倍）。

#### 兼容性处理与安全机制

- 多材料检测： 现可自动识别包含多种材料的任务，并提供操作引导，帮助用户安全进行后续操作。
- 检测到不支持的材料时，将提示用户：
  - 选择参考材料进行模拟，或切换至受支持的材料配置文件。不再允许静默匹配不符的情况。
- 自定义材料与打印机的匹配优化：
  - 使用基于 Token 的模糊匹配来识别最接近的受支持配置文件。
  - 新增材料类型回退机制与确认提示。

#### 结果展示更清晰、更具可操作性

Assess 结果现在能更清晰地说明问题产生的原因，以及哪些参数或设置会带来相关风险。

- 修复建议更易定位和执行。
- 可打印性报告已优化，减少了歧义表达。
- 评估引导与具体目标更紧密关联，例如提升可靠性、降低失败风险、提高打印速度等。

#### 新增 Helio 历史记录

- 可查看最近 10 次 Assess 与 Enhance 的运行记录。
- 支持回顾历史结果，并可下载已生成的 G-code 进行对比。
- 网络中断后可恢复最近的运行结果。

#### 稳定性改进与 Bug 修复

- 改进了 G-code 轮询过程中的错误检测机制。
- 后端错误信息现在将直接显示在失败对话框中，提供更清晰的诊断信息。

## 改进

### P2S支持手动停止空气净化与异物检测

![p2s风扇.png](https://wiki.bambulab.com/software/bambu-studio/release-note/v2_5_3/p2s%E9%A3%8E%E6%89%87.png)

### 逐件打印优化

- 交互改进：开启逐件打印后，界面自动显示打印顺序并在右下角弹出提示，支持手动关闭打印顺序标签。
- 支持为每个零件单独生成裙边（skirt）。

> ⚠️注意：启用该功能后，建议在碰撞检测安全距离之外，额外预留一个Skirt Distance的间距，以避免碰撞风险。

|  |  |
| --- | --- |
| 逐件1.png | 逐件2.png |

### H2C 机型喷嘴信息弹窗中新增累计打印时长显示

⚠️固件最低支持版本：01.02.00.00（H2C）

![h2c喷嘴.png](https://wiki.bambulab.com/software/bambu-studio/release-note/v2_5_3/h2c%E5%96%B7%E5%98%B4.png)

### H2C喷嘴信息状态弹窗同步优化

H2C打印机同步后，切换页面、设备或重启后返回准备页面，不再重复弹出喷嘴信息同步弹窗。

### 扩展“减小填充回抽”模式

新增“自动”选项。默认情况下，大多数耗材会启用该功能以节省打印时间；对于粘性较高的耗材（PETG），则默认关闭，以降低耗材碎屑粘附喷嘴并造成瑕疵的风险。“开启”和“关闭”模式的行为保持不变，仍分别表示始终开启或始终关闭。

![减小回抽.png](https://wiki.bambulab.com/software/bambu-studio/release-note/v2_5_3/%E5%87%8F%E5%B0%8F%E5%9B%9E%E6%8A%BD.png)

### 其他改进

1. 曲线规划增强功能同步优化：同步支持曲线规划增强的打印机后，Studio 将自动关闭切片圆弧拟合，以确保该功能正常生效。  
   ⚠️固件最低支持版本：01.02.00.00（H2C）
2. 高收缩率耗材切片时新增提示。

![高收缩.png](https://wiki.bambulab.com/software/bambu-studio/release-note/v2_5_3/%E9%AB%98%E6%94%B6%E7%BC%A9.png)

3. H2C喷嘴信息状态弹窗同步优化：H2C打印机同步后，切换页面、设备或重启后返回准备页面，不再重复弹出喷嘴信息同步弹窗。
4. H2S/H2C/P2S支持AMS 2 PRO与AMS HT的远程烘干与边烘边打功能。  
   ⚠️固件最低支持版本：01.01.40.00（H2S）、01.02.00.00（H2C）、01.02.00.00（P2S）。
5. H2C左头支持TPU材料打印（TPU 90A/95A/95A HF）。  
   ⚠️固件最低支持版本：01.02.00.00(H2C)
6. H2S机型增加裹头检测和裹头检测校准功能。  
   ⚠️固件最低支持版本：01.01.40.00（H2S）
7. 全部机型现支持进退料停止功能。  
   ⚠️注意：固件最低支持版本：01.01.40.00（H2S）、01.02.00.00（H2C）、01.01.50.40（P2S）、01.09.01.00（P1S）、01.07.01.00（A1）
8. 将"更改类型"（Change Type）改为带勾选标记的子菜单，提升操作便捷性。感谢[@jomixlaf](https://github.com/jomixlaf)的贡献。
9. 在Unix系统的支持MIME类型列表中新增model/step。感谢@hadess的贡献。
10. 新增winget更新器GitHub Action，优化打包与分发工作流。感谢@LightDestory的贡献。
11. 将macOS CI环境从macos-13升级至macos-15-intel。感谢@raulp的贡献。
12. 升级GitHub Actions，感谢@salmanmkc的贡献。

## Bug修复

1. 修复了部分场景下P2S的liveview丢帧的问题。
2. 修复了部分场景下跨多屏幕界面显示异常的问题。([#9627](https://github.com/bambulab/BambuStudio/issues/9627))
3. 修复了H2C切换喷嘴类型后重新切片，速度参数未正确跟随所选喷嘴更新的问题。([#9807](https://github.com/bambulab/BambuStudio/issues/9807))
4. 修复了部分场景下FuzzySkin涂抹与避免跨越外墙同时启用产生的走线错误。([#9837](https://github.com/bambulab/BambuStudio/issues/9837))
5. 修复了部分场景下顶面流量比例重置错误的问题。([#9563](https://github.com/bambulab/BambuStudio/issues/9563))
6. 优化了跨机型同喷嘴类型工艺预设的迁移适配逻辑。([#9105](https://github.com/bambulab/BambuStudio/issues/9105))
7. 修复了在启用擦料塔外墙间隙后，部分场景下可能导致外墙缺失的问题。
8. 修复了web目录下用户程序相关的冲突问题。感谢@Bambu-Pomfret 的贡献。
9. 自本Beta版本起，Beta更新通知默认开启，可在偏好设置中关闭。
10. 修复了重新选择对象后，对象设置中顶面流量比例可能被重置的问题。(#9563)
11. 修复了XWayland/Intel平台上3D视图中浮层元素显示不可读的问题。感谢@pedrosland的贡献。
12. 修复了当SwitchBoard控件显示在左侧副显示器时，无法正确响应鼠标左键点击的问题。感谢@mpaperno的贡献。
13. 修复了一处除以零的异常。感谢@mpaperno的贡献。
14. 修复了CLI段错误导致命令行模型工作流无法使用的问题。感谢@niccolodevries的贡献。
15. 修复了绒毛表面（Fuzzy Skin）点距设置为0mm时切片可能崩溃的问题。
16. 修复了因已分配但未清除的对象实例导致的内存泄漏问题。感谢@mpaperno的贡献。
17. 新增局部切割功能支持。感谢@StateoftheeArt的贡献。
18. 重构了GUI参数输入验证逻辑，支持浮点数最小值与最大值，不再仅限于整数。感谢@mpaperno的贡献。
19. 修复了Windows下窗口拖动卡顿的问题。感谢@4RH1T3CT0R7的贡献。
20. 修复了P2S加速度设置可能影响空走移动的问题。

## 已知问题

受MacOS Tahoe 26系统变更影响，默认下载路径可能被修改为无写入权限的系统目录，导致 Makerworld 文件下载失败。如遇此问题，请前往偏好设置重新指定存储路径即可解决。

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
