---
path: zh/s1/manual/calibration
title: "S1 设备校准"
description: ""
tags: []
created: 2026-11-26T14:00:36.618Z
updated: 2026-11-26T14:00:36.618Z
source: https://wiki.bambulab.com/zh/s1/manual/calibration
---

## 标定板

标定板上的反光点分布与背后二维码绑定，使用过程中若标定板上的反光点脱落，则需要更换新的标定板。

![001.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/calibration/zh/001.png)

如使用随设备的标定板进行校准，出厂时已绑定对应标定板信息，可直接按照屏幕提示进行校准。

如有新的标定板，需先扫描背后的二维码进行绑定，再进行校准。

![002.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/calibration/zh/002.png)

## 安全提示

> 本设备采用红外散斑与蓝色激光双光源进行三维扫描。其中，**红外散斑及平行线模式下的蓝色激光处于安全水平**，在对应模式下扫描人体或人脸时无需闭眼或做特别防护。  
> 其余蓝色激光模式符合 **Class 2（Ⅱ类）** 激光安全标准，强烈建议**避免长时间刻意直视激光束或其镜面反射光，同时避免或直接扫描人体**。  
> 扫描过程中投射的激光图案可能呈现闪烁或移动效果。患有光敏性癫痫或相关疾病、或对闪烁光敏感的用户，**建议避免注视扫描光束及其投射图案**，并在使用前咨询医生。若使用过程中感到头晕、视觉不适，请立即停止扫描并离开光照区域。

## 使用注意事项

1. 请勿在扫描时将标定板作为背景扫描使用。
2. 请勿在标定板上粘贴标记点，否则会干扰正常标定动作。
3. 请保持标点板标定面干净整洁。

## 校准周期

1. **首次使用时强烈推荐校准**。
2. 环境发生明显变化时，推荐校准。

> 通常温度变化过大或者长时间未校准，可能会影响扫描仪的精度。我们推荐在**超过两周未校准**或者**当前使用温度和最后一次校准相差超过 10℃ 时**进行校准。

3. 长时间未使用时，推荐校准。

![003.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/calibration/zh/003.png)

## 操作过程

在软件中选择“校准”。

![004.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/calibration/zh/004.png)

### 设备校准

首次使用时，请根据提示撕下设备上的保护膜。

![005.gif](https://public-cdn.bblmw.com/wiki/new/s1/manual/calibration/zh/005.gif)

将标定板按照正确方向放在桌面上，箭头朝前。

![006.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/calibration/zh/006.png)

请根据校准页面的教程提示，将**扫描仪移至标定板上方，向前微微倾斜扫描仪，确保相机与标定板平行。**

![007.gif](https://public-cdn.bblmw.com/wiki/new/s1/manual/calibration/zh/007.gif)

当扫描仪镜头和标定板几乎平行时，开始校准。

![008.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/calibration/zh/008.png)

校准时，请根据球形指示器进行操作，其中：

- 白色小球：代表当前步骤的目标位姿。

校准时需要控制橙色小球与白色小球重叠，在这个过程中通常需要先调整角度（对齐文字），再拉远拉仅调整距离（对齐球形指示器的大小）。当位置对准后，橙色球会变为绿色，保持约0.5后即可完成该步骤的校准。随后继续垂直上拉扫描仪完成后续步骤校准。

- 橙色小球：代表当前扫描仪的位姿。其数字部分反映了当前扫描仪的姿态（俯仰和横滚角度），大小反映距离标定板的距离。

1. 俯仰和横滚姿态：

![009.webp](https://public-cdn.bblmw.com/wiki/new/s1/manual/calibration/zh/009.webp)

2. 距离变化：

![010.webp](https://public-cdn.bblmw.com/wiki/new/s1/manual/calibration/zh/010.webp)

---

开始扫描后，若屏幕中心的小球变为橙色，说明距离过近或过远，需移动扫描仪。小球变为绿色时，说明距离合适，若未能进入下一步，可小幅度上下移动。

![011.webp](https://public-cdn.bblmw.com/wiki/new/s1/manual/calibration/zh/011.webp)

第 12 步根据屏幕提示,向下对准最后一个小球,完成整个校准流程。

![012.webp](https://public-cdn.bblmw.com/wiki/new/s1/manual/calibration/zh/012.webp)

### 激光平面校准

只需对准白色平面就能发起该项校准，可对准白色墙面（或白色桌面），由近到远，缓慢移动扫描仪。

|  |  |
| --- | --- |
| 013.png | 014.png |

## 标定失败的可能原因

通常有三种常见错误场景：

- **未撕保护膜**：请在首次校准前，检查镜头模组前全部保护膜是否移除。

![015.gif](https://public-cdn.bblmw.com/wiki/new/s1/manual/calibration/zh/015.gif)

- **对准标定板后无法显示后续的距离指示器**：可能是使用了错误的标定板进行扫描，请点击右下角按钮，重新扫描标定板的二维码信息后重试。

![016.png](https://public-cdn.bblmw.com/wiki/new/s1/manual/calibration/zh/016.png)

- **第一步或者后续校准无法通过**：通常为镜头模组没有对准校准版，请调整镜头（通常需要向前倾斜一定角度），保证镜头模组所在的平面对齐标定板，或者依据球形指示器调整姿态。

![017.gif](https://public-cdn.bblmw.com/wiki/new/s1/manual/calibration/zh/017.gif)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果本指南未解决您的问题，[请联系在线技术支持（服务时间 9:00-21:00）](https://support.bambulab.cn/liveChat/?from=5)，我们随时准备为您解答疑问并提供帮助。  
> 如果您对本篇 Wiki 有任何建议或反馈，欢迎在评论区留言，感谢您的支持与关注！
