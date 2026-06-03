---
path: zh/knowledge-sharing/CMYK-color-lithophane-printing-instructions
title: "CMYK 透光浮雕打印指引"
description: "介绍如何使进行 CMYK 彩色打印"
tags: []
created: 2023-05-06T10:52:18.790Z
updated: 2026-03-30T06:47:44.013Z
source: https://wiki.bambulab.com/zh/knowledge-sharing/CMYK-color-lithophane-printing-instructions
---

![makemylitho-1.jpeg](https://wiki.bambulab.com/makerworld/makemylitho/makemylitho-1.jpeg)

购买链接：[天猫](https://detail.tmall.com/item.htm?abbucket=8&id=715351727644&rn=4757913396790a202d86e233290c7b70&spm=a1z10.5-b-s.w4011-25176969463.62.665d6f97fyI8Jr&skuId=5170951278326)

## 透光浮雕生成器

### 使用拓竹透光浮雕生成器

透光浮雕生成器是一款由拓竹自研的网页端软件，可用于创作单色或者彩色的透光浮雕。相对于其他同类型软件，透光浮雕生成器针对拓竹的 CMYK 耗材做了算法优化以确保生成的透光浮雕效果。

步骤 1：访问[透光浮雕生成器](https://makerworld.com.cn/makerlab/makeMyLithophane?from=wiki)并创建一个项目。

![makemylitho-1.jpeg](https://wiki.bambulab.com/makerworld/makemylitho/makemylitho-2.png)

步骤 2：选择与[拓竹 CMYK LED 背光板](https://detail.tmall.com/item.htm?id=715351727644&skuId=5216838867458)兼容的透光浮雕类型：**单色-单一尺寸相框**或**彩色-单一尺寸相框**。

![makemylitho-1.jpeg](https://wiki.bambulab.com/makerworld/makemylitho/makemylitho-3.png)

- **单色-单一尺寸相框**用于创建仅需 PLA Basic - 玉白色 的单色透光浮雕。
- **彩色-单一尺寸相框**用于创建需要 CMYK 四色组合套装 的彩色石版画。本文将使用此类型作为示例。点击**选择图片**导入您喜欢的图片。

![makemylitho-1.jpeg](https://wiki.bambulab.com/makerworld/makemylitho/makemylitho-4.png)

步骤 3：按需调整图片的方向、大小和角度。  
![makemylitho-1.jpeg](https://wiki.bambulab.com/makerworld/makemylitho/makemylitho-5.png)

步骤 4：按需调整图片的颜色与光照，可以在透光浮雕生成器中实时预览调整效果。

![makemylitho-1.jpeg](https://wiki.bambulab.com/makerworld/makemylitho/makemylitho-6.png)

步骤 5：点击左上角的**下载**按钮导出 3MF 文件。选择适合的打印机和喷嘴尺寸，建议使用 0.2mm 以获得更好的效果。

![makemylitho-1.jpeg](https://wiki.bambulab.com/makerworld/makemylitho/makemylitho-7.png)

生成 3MF 文件需要几分钟时间。生成的 3MF 文件可以直接打印，无需调整参数。

![makemylitho-1.jpeg](https://wiki.bambulab.com/makerworld/makemylitho/makemylitho-8.png)

您也可以在移动设备上使用透光浮雕生成器，通过最新版 Bambu Handy 中 MakerLab 入口访问相关功能。

|  |  |
| --- | --- |
| handy1.1.png | handy2.1.png |

  

### 使用第三方透光浮雕生成器

如果拓竹透光浮雕生成器无法满足您的需求，您也可以使用其他第三方浮雕生成器来生成透光浮雕。这里以 [Lithophane Makers](https://lithophanemaker.com/Color%20Lithophane.html?fbclid=IwAR0zbiYVOGT2kV0MY4LtLbNk5rrg_wOd_bEsA2kpnxebZCTbBNzPyFu8h7g) 为例。

步骤 1：生成 STL 文件。

1. 选取一张需要 3D 打印的彩色照片，确保照片格式为 jpg。使用 [Lithophane Makers](https://lithophanemaker.com/Color%20Lithophane.html?fbclid=IwAR0zbiYVOGT2kV0MY4LtLbNk5rrg_wOd_bEsA2kpnxebZCTbBNzPyFu8h7g) 进行文件格式调整。

- 选中 Crop（选择之后可自行调整 STL 长宽尺寸）。
- 首层高度建议 0.15 mm，长宽尺寸调整为：144\*108（**可兼容拓竹灯板、相框**）。
- 修改 X Shift 和 Y Shift，可调整打印照片的区域。

![makemylitho-1.jpeg](https://wiki.bambulab.com/makerworld/makemylitho/makemylitho-10.png)

2. 填写个人邮箱，点击 create .stl 之后，会下载一个压缩文件夹。

![makemylitho-1.jpeg](https://wiki.bambulab.com/makerworld/makemylitho/makemylitho-11.png)

3. 以上信息全部填写完成后，可通过网站提供的预览功能预览打印效果。

![makemylitho-1.jpeg](https://wiki.bambulab.com/makerworld/makemylitho/makemylitho-12.jpeg)

> 由于网站显示原因，预览功能仅供预览打印效果，具体以实际打印结果为准。

  

步骤 2：参数调整和切片。

1. 解压该压缩文件夹，将生成的五个 STL 文件拖入 Bambu Studio。提示是否将这些文件加载为一个多零件对象，选择**是**。
2. 增加耗材至 4 种颜色，分别为 PLA Basic 青色（Cyan #0086D6）、品红 (Magenta #EC008C)、黄色 (Yellow #F4EE2A)、白色 (White #FFFFFFF)；此处需要对应 AMS 四个槽位的料线摆放顺序。

![makemylitho-1.jpeg](https://wiki.bambulab.com/makerworld/makemylitho/makemylitho-13.png)

3. 在**对象**中根据文件名设置相应的颜色。

![makemylitho-1.jpeg](https://wiki.bambulab.com/makerworld/makemylitho/makemylitho-14.png)

4. 修改打印参数。

- 选择 0.2 mm 喷嘴。
- 修改首层层高至 0.15 mm。
- 顶部 & 底部壳体层数至 3。
- 填充改为直线 100% 填充。
- 开始切片（注：彩色透光浮雕文件切片时间较长，请耐心等待）。

## 参数调整和切片替换方案指南

您也可以下载示例 3MF 文件以快速获取上述步骤的切片参数配置。

1. 下载示例 3mf 文件（[下载链接](https://public-cdn.bambulab.com/wiki/model/Puppy-in-Flowers_v1.3mf)）- Labrador，并在 Bambu Studio 中打开。

![makemylitho-1.jpeg](https://wiki.bambulab.com/makerworld/makemylitho/makemylitho-15.png)

2. 根据您的需求调整打印机设置（它需要与 Bambu PLA Basic 兼容，推荐的床温度为 45 到 55 ℃）。

![makemylitho-1.jpeg](https://wiki.bambulab.com/makerworld/makemylitho/makemylitho-16.png)

3. 添加另一张盘并导入您想要打印的模型文件。

![makemylitho-1.jpeg](https://wiki.bambulab.com/makerworld/makemylitho/makemylitho-17.png)

![makemylitho-1.jpeg](https://wiki.bambulab.com/makerworld/makemylitho/makemylitho-18.png)

4. 将颜色设置为与上面一盘的 3mf 文件相同。

![makemylitho-1.jpeg](https://wiki.bambulab.com/makerworld/makemylitho/makemylitho-19.png)

5. 切片并等待完成。

![makemylitho-1.jpeg](https://wiki.bambulab.com/makerworld/makemylitho/makemylitho-20.png)

\*致谢: Puppy in the Flowers - 来自 @larissatondim; Sunflowers - 来自 Vincent van Gogh.

## AMS 上料打印

确保 AMS 中线材的放置顺序与 Bambu Studio 里设置的一致，否则将出现打印成品颜色错误。

![makemylitho-21.png](https://wiki.bambulab.com/makerworld/makemylitho/makemylitho--21.png)

## 相框 & 均光板模型

如果您使用了拓竹透光浮雕生成器，那么相框与均光板也会包含在生成的 3MF 文件中。您可以直接打印相框和均光板模型，无需额外修改配置。

![makemylitho-21.png](https://wiki.bambulab.com/makerworld/makemylitho/makemylitho--22.png)

如果您选择了生成适配 0.2mm 喷嘴的透光浮雕，我们也提供了使用 0.4mm 喷嘴配置的相框文件。

![makemylitho-21.png](https://wiki.bambulab.com/makerworld/makemylitho/makemylitho--23.png)

### 相框

3MF 文件 - [点击下载](https://wiki.bambulab.com/knowledge-sharing/cmyk-color-lithophane/cmyk_frame_x1c_v2.3mf) ：已经更改切片参数，下载后选择机型即可打印。  
STL 文件 - [点击下载](https://wiki.bambulab.com/knowledge-sharing/cmyk-color-lithophane/cmyk_frame_final_v2.stl)  
STP 文件 - [点击下载](https://wiki.bambulab.com/knowledge-sharing/cmyk-color-lithophane/cmyk_frame_final_v2.stp)

#### 切片参数

- 打印材料：大多数 PLA，最好使用深色耗材
- 墙层数：5
- 顶部壳体层数：5
- 底部壳体层数：3
- 填充密度：50%
- 支撑方式：树状（自动）
- 打印时长：5 小时 35 分钟
- 耗材重量：240 g

### 均光板

3MF 文件 - [点击下载](https://wiki.bambulab.com/knowledge-sharing/cmyk-color-lithophane/uniform_light_plate_x1c.3mf) ：已经更改切片参数，下载后选择机型即可打印。  
STL 文件 - [点击下载](https://wiki.bambulab.com/knowledge-sharing/cmyk-color-lithophane/uniform_light_plate(2).stl)

#### 切片参数

- 打印材料：PLA Basic 玉石白
- 墙层数：5
- 顶部壳体层数：5
- 底部壳体层数：5
- 打印时长：35 分钟
- 耗材重量：30 g

## 安装

视频安装指南。

  

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 为了确保您安全有效地进行操作，如果对指南中的任何步骤有疑虑或问题，请在开始操作前联系我们的客户服务团队，我们随时乐意为您解答疑问并提供支持。  
> [点击此处联系在线技术支持 （服务时间 9:00-21:00）](https://support.bambulab.cn/cn/im)
