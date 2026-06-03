---
path: zh/software/bambu-studio/use-ams-on-bambu-studio
title: "在 Bambu Studio 中使用 AMS"
description: "介绍如何在 bambu studio 中使用 AMS，包括 AMS 映射和 AMS 操作与设置。"
tags: ["ams", "bambu studio"]
created: 2024-09-18T07:35:53.623Z
updated: 2025-02-20T06:31:56.057Z
source: https://wiki.bambulab.com/zh/software/bambu-studio/use-ams-on-bambu-studio
---

本指南用于在 Bambu Studio 上使用 AMS，包括 AMS 操作、控制界面和 AMS 映射。

> 如需了解多色打印，请点击[这里](multi-color-printing.md)查看 Bambu Studio 多色打印指南。

## AMS 操作

### 进料

选择要装入耗材的槽。当指示灯开始闪烁时，向前按下按钮并插入耗材，直到耗材自动拉入。  
![screenshot-20240918-172704.png](https://wiki.bambulab.com/studio-ams/screenshot-20240918-172704.png)

### LED 灯状态

- **白灯亮**  
  有料插入该槽且处于空闲状态。耗材可以拉出。(如果感觉槽内堵塞堵塞，请按下按钮释放耗材）。
- **白灯呼吸**  
  料槽繁忙，请勿拉出耗材。
- **红灯**  
  错误状态。 请检查错误信息或联系技术服务。

![20240919-153626.jpg](https://wiki.bambulab.com/studio-ams/20240919-153626.jpg)

## 耗材控制界面

图标说明：

- RFID 读取按钮和指示灯
- 耗材颜色和类型
- 编辑或查看耗材信息

![20240919-153621.jpg](https://wiki.bambulab.com/studio-ams/20240919-153621.jpg)

## AMS 映射

- **在 AMS 中查看耗材类型和颜色**  
  ![screenshot-20240918-172704.png](https://wiki.bambulab.com/studio-ams/screenshot-20240918-172704.png)
- **点击编辑图标设置耗材类型和颜色**  
  ![动画_颜色.gif](https://wiki.bambulab.com/studio-ams/%E5%8A%A8%E7%94%BB_%E9%A2%9C%E8%89%B2.gif)
- **Bambu Studio AMS 映射**  
  Bambu Studio 将对当前打印作业进行 AMS 映射（匹配耗材类型和颜色）。AMS 映射部件的上半部分是当前项目的源颜色和类型，下半部分是 AMS 料槽的目标索引和颜色。  
  ![颜色对应.png](https://wiki.bambulab.com/studio-ams/%E9%A2%9C%E8%89%B2%E5%AF%B9%E5%BA%94.png)

> **注意**：
>
> - 可在**设备**中选择要使用的打印机，然后在**准备**界面单击**从AMS同步材料列表**图标，再单击**重新同步**。
>
> |  |  |
> | --- | --- |
> |  |  |
>
> - 开启**多设备管理**可能会出现无法同步耗材丝的问题。可点击**多设备**界面中要使用的打印机**视图**，切换到指定设备界面，然后再回到**准备**页面同步，即可成功。
>
> |  |  |  |
> | --- | --- | --- |
> |  |  |  |

- **如下所示手动调整映射**  
  ![动画_mapping.apng](https://wiki.bambulab.com/studio-ams/%E5%8A%A8%E7%94%BB_mapping.apng)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。
>
> 我们希望能确保您安全有效地进行操作。如果您对本指南描述的过程有任何疑虑或问题，建议您在开始操作前联系我们的客户服务团队。我们随时准备为您解答疑问并提供帮助。  
> [点击此处联系在线技术支持 （服务时间 9:00-21:00）](https://support.bambulab.cn/cn/im)
