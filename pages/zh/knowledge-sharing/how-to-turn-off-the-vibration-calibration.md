---
path: zh/knowledge-sharing/how-to-turn-off-the-vibration-calibration
title: "如何关闭准备阶段的振动校准过程"
description: "本文将介绍如何关闭打印机的准备阶段的振动校准"
tags: []
created: 2026-01-21T07:13:07.371Z
updated: 2026-06-29T09:31:16.962Z
source: https://wiki.bambulab.com/zh/knowledge-sharing/how-to-turn-off-the-vibration-calibration
---

## 快速振动补偿检查

快速振动检查会在打印前进行一次，打印机可快速判断皮带张力状态是否正常，避免影响打印过程。

## 何时使用

当您某次打印不希望设备进行快速的振动检查时，可以根据该指南关闭该功能。

> **关闭该功能会导致打印机无法检测皮带张力，长期可能影响打印质量，因此我们不建议关闭该功能。**

## 操作步骤

### 1. 编辑配置

在 Bambu Studio 软件中选择好对应机型，然后点击左上角的编辑按钮。

![进入打印机设置.jpg](https://wiki.bambulab.com/knowledge-sharing/how-to-turn-off-the-vibration-calibration/%E8%BF%9B%E5%85%A5%E6%89%93%E5%8D%B0%E6%9C%BA%E8%AE%BE%E7%BD%AE.jpg)

### 2. 找到 G-code

点击“打印机 G-code”，找到“打印机起始 G-code”栏目。

![进入gcode.jpeg](https://wiki.bambulab.com/knowledge-sharing/how-to-turn-off-the-vibration-calibration/%E8%BF%9B%E5%85%A5gcode.jpeg)

### 3. 修改 G-code

复制所有的 G-code。

![zh1.jpg](https://wiki.bambulab.com/knowledge-sharing/how-to-turn-off-the-vibration-calibration/zh1.jpg)

在桌面上建立一个新的文本文档，拷贝刚才复制的内容。

![txt.jpg](https://wiki.bambulab.com/knowledge-sharing/how-to-turn-off-the-vibration-calibration/txt.jpg)

按下“CTRL+F”，搜索关键字“mech mode”

![1.jpg](https://wiki.bambulab.com/knowledge-sharing/how-to-turn-off-the-vibration-calibration/1.jpg)

删除注释之间的 G-code 内容。

![2.jpg](https://wiki.bambulab.com/knowledge-sharing/how-to-turn-off-the-vibration-calibration/2.jpg)

将修改后的 G-code，重新复制并粘贴到 Bambu studio。

> 特别说明：A1mini 请参考下图删除。  
> ![a1mini.jpg](https://wiki.bambulab.com/knowledge-sharing/how-to-turn-off-the-vibration-calibration/a1mini.jpg)

### 4. 保存预设

保存并重命名为您需要的预设。  
![保存预设.jpeg](https://wiki.bambulab.com/knowledge-sharing/how-to-turn-off-the-vibration-calibration/%E4%BF%9D%E5%AD%98%E9%A2%84%E8%AE%BE.jpeg)

### 5. 启用预设

选择保存的预设，即可进行切片，并发起打印。

![用户预设.jpg](https://wiki.bambulab.com/knowledge-sharing/how-to-turn-off-the-vibration-calibration/%E7%94%A8%E6%88%B7%E9%A2%84%E8%AE%BE.jpg)

> 如您更改后想要开启该功能，只需重新选择**系统预设**。  
> ![系统预设.jpg](https://wiki.bambulab.com/knowledge-sharing/how-to-turn-off-the-vibration-calibration/%E7%B3%BB%E7%BB%9F%E9%A2%84%E8%AE%BE.jpg)

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
