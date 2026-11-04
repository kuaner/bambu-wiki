---
path: zh/makerworld/makers_supply/ZC037/Watch_Movement_Design
title: "钟表机芯创作指南_ZC037"
description: ""
tags: ["zc037"]
created: 2026-10-29T02:30:30.525Z
updated: 2026-11-03T13:54:50.471Z
source: https://wiki.bambulab.com/zh/makerworld/makers_supply/ZC037/Watch_Movement_Design
---

# 钟表机芯创作指南

[![机芯创作指南概览 · 图 1](https://wiki.bambulab.com/makerworld/makersupply/zc037_%E5%88%9B%E4%BD%9C%E6%8C%87%E5%8D%97/zc037_design_01_re_movement_design_overview_cn.png)](https://wiki.bambulab.com/makerworld/makersupply/zc037_%E5%88%9B%E4%BD%9C%E6%8C%87%E5%8D%97/zc037_design_01_re_movement_design_overview_cn.png)

本指南面向使用机芯套件进行设计的设计师，介绍机芯固定、表盘间距与表冠安装的关键设计要点，帮助您将机芯集成到钟表项目中，并确保其稳定运行。

## 机芯的固定

考虑到 FDM 打印的尺寸精度与手工装配的精度限制，推荐采用侧面轮廓包裹的方式固定机芯。

[![TPU 机芯包裹结构 · 图 2](https://wiki.bambulab.com/makerworld/makersupply/zc037_%E5%88%9B%E4%BD%9C%E6%8C%87%E5%8D%97/zc037_design_02_re_tpu_movement_mount_cn.png)](https://wiki.bambulab.com/makerworld/makersupply/zc037_%E5%88%9B%E4%BD%9C%E6%8C%87%E5%8D%97/zc037_design_02_re_tpu_movement_mount_cn.png)

包裹结构的参考模型文件可在商品详情页获取。建议使用 TPU 材料打印包裹结构，以补偿打印尺寸公差并缓冲磕碰冲击，避免机芯受损。

- [TPU Cover.stp](https://wiki.bambulab.com/makerworld/makersupply/zc037_%E7%94%A8%E6%88%B7%E6%8C%87%E5%8D%97/application_instruction_of_40.5mm_diameter_watch_movement_kit_zc037.zip)

设计侧面包裹结构时，请注意以下要点：

### 避免尖锐部位划伤线圈

机芯上，钟表柄轴的对侧为驱动线圈，应避免包裹结构的尖锐部位接触或磕碰线圈，以免损坏机芯。建议在线圈一侧留出一段空隙，确保其他部位不与线圈接触。

|  |  |
| --- | --- |
| [包裹结构与驱动线圈的间隙 · 图 3](https://wiki.bambulab.com/makerworld/makersupply/zc037_%E5%88%9B%E4%BD%9C%E6%8C%87%E5%8D%97/zc037_design_03_re_coil_mount_clearance_cn.png) | [包裹结构与驱动线圈的间隙 · 图 4](https://wiki.bambulab.com/makerworld/makersupply/zc037_%E5%88%9B%E4%BD%9C%E6%8C%87%E5%8D%97/zc037_design_04_re_coil_mount_clearance_cn.png) |

### 避开柄轴孔

机芯椭圆短轴一侧设有柄轴孔，包裹结构需在柄轴孔对应的位置留出空间，以便安装柄轴。参考尺寸如下：柄轴孔直径为1.0 mm，孔中心位于机芯横向正中央，距离机芯底面 1.1 mm。

[![机芯柄轴孔尺寸 · 图 5](https://wiki.bambulab.com/makerworld/makersupply/zc037_%E5%88%9B%E4%BD%9C%E6%8C%87%E5%8D%97/zc037_design_05_re_stem_hole_dimensions_cn.png)](https://wiki.bambulab.com/makerworld/makersupply/zc037_%E5%88%9B%E4%BD%9C%E6%8C%87%E5%8D%97/zc037_design_05_re_stem_hole_dimensions_cn.png)

更多尺寸信息，请下载并查阅所附图纸。

### 为柄轴留出拆卸空间

如果无法在装有柄轴的情况下取出机芯，请确保安装座内留有足够的操作空间，便于用镊子夹取柄轴。这样就可以先取下柄轴，再小心地取出机芯。

|  |  |
| --- | --- |
| [预留柄轴拆卸操作空间 · 图 6](https://wiki.bambulab.com/makerworld/makersupply/zc037_%E5%88%9B%E4%BD%9C%E6%8C%87%E5%8D%97/zc037_design_06_re_stem_removal_clearance_cn.png) | [预留柄轴拆卸操作空间 · 图 7](https://wiki.bambulab.com/makerworld/makersupply/zc037_%E5%88%9B%E4%BD%9C%E6%8C%87%E5%8D%97/zc037_design_07_re_stem_removal_clearance_cn.png) |

### 按先后顺序安装两端台阶

建议先将机芯装入表壳，使指针轴穿过表盘，再安装外侧包裹结构。指针轴与机芯主体形成阶梯状结构，轴的长度与机芯主体的厚度大致相当。

如果同时将这两个部分装入安装座，机芯容易移位或倾斜，导致指针轴难以对准。分步安装这两个部分，可以让装配更轻松、更可靠。

|  |  |  |
| --- | --- | --- |
| [按先后顺序安装两端台阶 · 图 8](https://wiki.bambulab.com/makerworld/makersupply/zc037_%E5%88%9B%E4%BD%9C%E6%8C%87%E5%8D%97/zc037_design_08_re_stepped_movement_mounting_cn.png) | [按先后顺序安装两端台阶 · 图 9](https://wiki.bambulab.com/makerworld/makersupply/zc037_%E5%88%9B%E4%BD%9C%E6%8C%87%E5%8D%97/zc037_design_09_re_stepped_movement_mounting_cn.png) | [按先后顺序安装两端台阶 · 图 10](https://wiki.bambulab.com/makerworld/makersupply/zc037_%E5%88%9B%E4%BD%9C%E6%8C%87%E5%8D%97/zc037_design_10_re_stepped_movement_mounting_cn.png) |

## 机芯与表盘的间距

1. 机芯与表盘背面的间距

   为避免指针轴上的钟表齿轮与表盘背面发生干涉、造成走时卡顿，套件内附带两片薄的钟表垫片，用于隔开齿轮与表盘，防止两者直接接触。

   此外，建议在设计固定位时，为机芯与表盘背面之间预留 0.4 mm 的高度间隙，以避免两者接触产生摩擦。

   [![机芯与表盘背面的间距 · 图 11](https://wiki.bambulab.com/makerworld/makersupply/zc037_%E5%88%9B%E4%BD%9C%E6%8C%87%E5%8D%97/zc037_design_11_re_dial_movement_gap_cn.png)](https://wiki.bambulab.com/makerworld/makersupply/zc037_%E5%88%9B%E4%BD%9C%E6%8C%87%E5%8D%97/zc037_design_11_re_dial_movement_gap_cn.png)
2. 表盘中央指针轴孔的尺寸建议

   为避免指针轴碰到表盘孔，建议将表盘中央孔直径设为 1.8 mm。

   [![表盘中央指针轴孔尺寸 · 图 12](https://wiki.bambulab.com/makerworld/makersupply/zc037_%E5%88%9B%E4%BD%9C%E6%8C%87%E5%8D%97/zc037_design_12_re_dial_shaft_hole_dimensions_cn.png)](https://wiki.bambulab.com/makerworld/makersupply/zc037_%E5%88%9B%E4%BD%9C%E6%8C%87%E5%8D%97/zc037_design_12_re_dial_shaft_hole_dimensions_cn.png)

## 表冠与柄轴的固定

1. 表冠柄轴孔的尺寸

   为适配柄轴螺纹，避免孔径过小造成安装困难、或孔径过大导致调时过程中脱落，建议按喷嘴直径设置孔径。使用 0.2 mm 喷嘴时，建议将孔径设为 0.9 mm，使用 0.4 mm 喷嘴时，建议将孔径设为 1.1 mm。

   [![表冠柄轴孔尺寸 · 图 13](https://wiki.bambulab.com/makerworld/makersupply/zc037_%E5%88%9B%E4%BD%9C%E6%8C%87%E5%8D%97/zc037_design_13_re_crown_stem_hole_dimensions_cn.png)](https://wiki.bambulab.com/makerworld/makersupply/zc037_%E5%88%9B%E4%BD%9C%E6%8C%87%E5%8D%97/zc037_design_13_re_crown_stem_hole_dimensions_cn.png)
2. 表冠柄轴孔的深度

   由于螺纹啮合长度较短，柄轴在拧入过程中可能穿透表冠的底面，导致柄轴有效长度不足，进而使表冠与表盘接触，影响正常运动。

   建议在设计时配套设计对照件，用于控制拧入深度。对照件应带有凹槽，且长度合适。操作时，先将柄轴光轴段与凹槽对齐，再拧入表冠，直至表冠的端面与凹槽的指定边缘平齐。

   [![表冠拧入深度对照件 · 图 14](https://wiki.bambulab.com/makerworld/makersupply/zc037_%E5%88%9B%E4%BD%9C%E6%8C%87%E5%8D%97/zc037_design_14_re_crown_insertion_depth_guide_cn.png)](https://wiki.bambulab.com/makerworld/makersupply/zc037_%E5%88%9B%E4%BD%9C%E6%8C%87%E5%8D%97/zc037_design_14_re_crown_insertion_depth_guide_cn.png)
3. 在碰撞与挤压中保护柄轴

   柄轴直径较细，使用过程中若表冠受到意外碰撞，可能导致柄轴损坏。

   建议固定表冠后，沿其下轮廓用表壳设置一圈承托结构。发生碰撞时，表冠所受的力可传递该结构，从而保护柄轴。

   [![保护柄轴的表冠承托结构 · 图 15](https://wiki.bambulab.com/makerworld/makersupply/zc037_%E5%88%9B%E4%BD%9C%E6%8C%87%E5%8D%97/zc037_design_15_re_crown_impact_support_cn.png)](https://wiki.bambulab.com/makerworld/makersupply/zc037_%E5%88%9B%E4%BD%9C%E6%8C%87%E5%8D%97/zc037_design_15_re_crown_impact_support_cn.png)
