---
path: zh/p2s/manual/first-print
title: "P2S 首次打印"
description: "本文介绍了 P2S 套装版及单机版的首次打印方法。引导您使用 AMS 2 Pro 或外挂料盘装载耗材并完成进料，通过打印机屏幕、Bambu Handy 和 Bambu Studio 软件发起打印任务。"
tags: ["p2s"]
created: 2025-10-14T13:53:43.380Z
updated: 2026-01-07T11:53:38.442Z
source: https://wiki.bambulab.com/zh/p2s/manual/first-print
---

### 打印流程概览

- 根据您所购买的版本（套装版/单机版），将 [AMS 2 Pro](https://wiki.bambulab.com/zh/p2s/manual/first-print#%E5%A5%97%E8%A3%85%E7%89%88%E9%80%9A%E8%BF%87-ams-2-pro-%E8%BF%9B%E6%96%99) 或[外挂料盘](https://wiki.bambulab.com/zh/p2s/manual/first-print#%E5%8D%95%E6%9C%BA%E7%89%88%E9%80%9A%E8%BF%87%E5%A4%96%E6%8C%82%E6%96%99%E7%9B%98%E8%BF%9B%E6%96%99)连接至打印机，装载耗材并完成进料。
- 打印前，先[检查打印板和热床](https://wiki.bambulab.com/zh/p2s/manual/first-print#%E6%AD%A5%E9%AA%A4-1%E6%89%93%E5%8D%B0%E5%89%8D%E5%87%86%E5%A4%87)的状态，再发起[打印任务](https://wiki.bambulab.com/zh/p2s/manual/first-print#%E6%AD%A5%E9%AA%A4-2%E5%BC%80%E5%A7%8B%E6%89%93%E5%8D%B0)。
- 打印结束后，等待模型冷却至室温后再[取下模型](https://wiki.bambulab.com/zh/p2s/manual/first-print#%E6%AD%A5%E9%AA%A4-3%E5%8F%96%E4%B8%8B%E6%A8%A1%E5%9E%8B)，并将[耗材退出打印机](https://wiki.bambulab.com/zh/p2s/manual/first-print#%E6%AD%A5%E9%AA%A4-4%E9%80%80%E5%87%BA%E8%80%97%E6%9D%90)，以便下次使用。

## 视频教程

## 套装版：通过 AMS 2 Pro 进料

### 注意事项

- P2S 套装版（P2S Combo）已包含 AMS 2 Pro 和外挂料盘支架，推荐您优先使用 AMS 设备来装载耗材。
- 若耗材料盘过大，或打印 AMS 不兼容的耗材时，请参见[外挂料盘安装步骤](https://wiki.bambulab.com/zh/p2s/manual/first-print#%E5%8D%95%E6%9C%BA%E7%89%88%E9%80%9A%E8%BF%87%E5%A4%96%E6%8C%82%E6%96%99%E7%9B%98%E8%BF%9B%E6%96%99)操作。

### 连接 AMS

将 AMS 2 Pro 放置在打印机顶部，连接 6-pin 线和铁氟龙料管。详细操作说明请参见 [P2S 开箱指南](unboxing-p2s.md)。

![1-connect-ams.jpeg](https://public-cdn.bblmw.com/wiki/new/p2s/manual/first-print/1-connect-ams.jpeg)

> 如需更换料管的插入位置，请先按压黑色的气动接头，再向外轻拉料管即可拔出。  
> ![release-tube-from-buffer.webp](https://wiki.bambulab.com/p2s/manual/first-print/release-tube-from-buffer.webp)

### AMS 进料

1. 打开电源开关。  
   ![50-power-on-2.jpg](https://public-cdn.bblmw.com/wiki/new/p2s/manual/p2s-unboxing/50-power-on-2.jpg)
2. 将打印所需耗材放入 AMS 2 Pro 料槽，轻推进料口，然后将耗材插入约 2 cm，AMS 将检测到耗材并自动送料。  
   ![2-load-fila-with-ams.png](https://public-cdn.bblmw.com/wiki/new/p2s/manual/first-print/2-load-fila-with-ams.png)

## 单机版：通过外挂料盘进料

### 注意事项

打印机背面共预留 3 个外挂料盘支架底座安装位置，出厂时已将底座预装在官方推荐位置。**对于购买 P2S Combo 的用户，如需使用外挂料盘，请注意料盘支架的安装位置及进料方式：**

- **使用过大尺寸的耗材料盘时**，直接在预装底座上安装料盘支架，并装载耗材。推荐将支架料管接入缓冲器左侧任一进料口，打印机将支持缠料检测功能。
- **使用 AMS 不兼容的耗材（请在[此处](https://bambulab.cn/zh-cn/filament-guide)查询）时**，一般不推荐从缓冲器进入。请拆下底座（使用工具盒随附的 H2.0 内六角扳手），将其安装在 P2S 单机版的预装位置，并确保支架料管直接接入机箱进料口，不经过缓冲器。

> 拆装过程中，如需更换料盘支架的方向，请用力将料盘支架分离（首次操作较为费力），建议先上下晃动支架，再顺势向外拔出。  
> ![10月21日.webp](https://wiki.bambulab.com/p2s/manual/10%E6%9C%8821%E6%97%A5.webp)

### 安装料盘支架组件

根据打印机预留的支架底座位置，安装料盘支架并插入铁氟龙料管：

- [P2S Combo 外挂料盘安装方式](https://wiki.bambulab.com/zh/p2s/manual/unboxing-p2s#%E6%AD%A5%E9%AA%A46%E5%AE%89%E8%A3%85%E6%96%99%E7%9B%98%E6%94%AF%E6%9E%B6%E7%BB%84%E4%BB%B6)（外挂耗材从缓冲器送入）
- [P2S 单机版外挂料盘安装方式](https://wiki.bambulab.com/zh/p2s/manual/unboxing-p2s#%E6%AD%A5%E9%AA%A45%E5%AE%89%E8%A3%85%E6%96%99%E7%9B%98%E6%94%AF%E6%9E%B6%E7%BB%84%E4%BB%B6)（外挂耗材从机箱进料口送入）

|  |  |  |  |
| --- | --- | --- | --- |
| P2S Combo 支架安装位置 |  | P2S 单机版支架安装位置 |  |
|

根据支架的实际安装位置，可以同步调整或修剪料管长度（参见下方图示及说明）。务必确保料管长度适中，料管过长可能影响进料。

|  |
| --- |
| ① AMS 到缓冲器：约 600 mm ② 左上外挂料盘到缓冲器：约 350 mm |

|  |  |
| --- | --- |
| ③ 左下外挂料盘到缓冲器：约 280 mm | ④ 右侧外挂料盘到机箱进料口：约 180 mm |

### 外挂料盘进料

1. 在进料前，请记下耗材类型和颜色，然后根据耗材绕线的方向，将料盘放置在料盘支架上。  
   ![8-fila-info.png](https://public-cdn.bblmw.com/wiki/new/p2s/manual/first-print/8-fila-info.png)
2. 在屏幕上点击“编辑”，选择耗材的类型和颜色后，点击“确认”。

|  |  |
| --- | --- |
|  |  |

3. 将耗材插入料管，持续推送直至无法前进。此时，打印机屏幕上的工具头会显示耗材颜色，表示挤出机检测到耗材进入。

|  |  |
| --- | --- |
|  |  |

4. 在屏幕上点击“进料”，等待喷嘴加热，期间再次手动推动耗材，确保耗材仍然留在挤出机内。  
   ![13-load-fila-with-external-spool.png](https://public-cdn.bblmw.com/wiki/new/p2s/manual/first-print/13-load-fila-with-external-spool.png)
5. 根据打印机提示观察喷嘴，看见喷嘴顺利挤出耗材后，在屏幕上点击“耗材已挤出，继续”；如果耗材没有被挤出，选择“耗材未挤出，重试”，然后重复推入耗材的动作。

|  |  |
| --- | --- |
|  |  |

## 步骤 1：打印前准备

### 检查热床

在放置打印板前，请检查并清洁热床表面，确保无异物残留。若存在异物，在加热过程中可能对软磁贴表面造成不可逆损伤。

![16-check-heatbed.jpeg](https://public-cdn.bblmw.com/wiki/new/p2s/manual/first-print/16-check-heatbed.jpeg)

### 清洁打印板

请避免在开箱或操作过程中直接用手接触打印板表面，以免油污影响打印附着力。  
如不慎触碰，请按以下步骤清洁：

1. 取出打印板，用温水和洗洁精清洗表面；
2. 使用干净的纸巾或无纺布将其擦干；
3. 确认表面清洁后，放回打印板。

## 步骤 2：开始打印

> - 本步骤支持通过打印机屏幕、Bambu Studio 或 Bambu Handy 进行操作，以下使用屏幕作为展示。您也可以在[其他打印方式](https://wiki.bambulab.com/zh/p2s/manual/first-print#%E5%85%B6%E4%BB%96%E6%89%93%E5%8D%B0%E6%96%B9%E5%BC%8F)，学习如何通过 Bambu Studio 和 Bambu Handy 进行操作。
> - 建议自行准备一个 U 盘并插入打印机，用于保存工作录像和历史打印缓存。  
>   ![17-insert-usb-drive.png](https://public-cdn.bblmw.com/wiki/new/p2s/manual/first-print/17-insert-usb-drive.png)

### 选择模型

在首页上点击“打印文件”，选择想要打印的模型。

|  |  |
| --- | --- |
|  |  |

### 确认配置

确认使用的打印板和喷嘴配置正确，并根据需要设置延时摄影和高级选项（默认为自动模式），然后点击“下一步”。

![20-advanced-settings.png](https://public-cdn.bblmw.com/wiki/new/p2s/manual/first-print/20-advanced-settings.png)

### 匹配耗材

在 AMS 或外挂料中，选择识别到的耗材，点击“打印”。

|  |  |
| --- | --- |
|  |  |

### 其他打印方式

#### 从 Bambu Studio 发起打印

1. 参考[打印机账号绑定指南](../../knowledge-sharing/printer-account-binding-guide.md)连接 Wi-Fi。
2. 参考 [Bambu Studio 快速上手教程](../../software/bambu-studio/studio-quick-start.md) 安装软件，连接打印机。
3. 进入 Bambu Studio 主页，选中打开想要打印的模型，修改打印配置后点击“下载并打开”。  
   ![print-from-studio-select-model-cn.png](https://wiki.bambulab.com/p2s/manual/first-print/print-from-studio-select-model-cn.png)
4. 点击“切片单盘”，再点击“打印单盘”，确认打印机和耗材无误，点击“发送”即可将打印任务发送给打印机。  
   ![print-from-studio-send-task-cn.png](https://wiki.bambulab.com/p2s/manual/first-print/print-from-studio-send-task-cn.png)

#### 从 Bambu Handy 发起打印

1. 参考[打印机账号绑定指南](../../knowledge-sharing/printer-account-binding-guide.md)连接 Wi-Fi。
2. 参考 [Bambu Handy 快速入门指南](../../studio-handy/handy/bambu-handy-quick-start.md)安装软件，连接打印机。
3. 在 Bambu Handy 中选择想要打印的模型，点击“准备打印”，选择打印配置，确认打印信息，再点击“开始打印”即可将打印任务发送给打印机。  
   ![print-from-handy-cn.png](https://wiki.bambulab.com/p2s/manual/first-print/print-from-handy-cn.png)

您可前往 [Bambu Lab 软件页](../../software.md) 获取更多软件使用教程。

## 步骤 3：取下模型

1. 打印结束后，请等待热床和模型冷却至室温。随后取下打印板，轻轻弯折打印板以取下模型和擦拭塔（如有）。  
   ![23-remove-model.png](https://public-cdn.bblmw.com/wiki/new/p2s/manual/first-print/23-remove-model.png)

> 注意：过早取件可能导致模型变形或损坏打印板。

2. 使用刮刀将打印板上的预挤出线清除后，再将打印板重新放回热床。  
   ![24-remove-cali-line.png](https://public-cdn.bblmw.com/wiki/new/p2s/manual/first-print/24-remove-cali-line.png)

## 步骤 4：退出耗材

### AMS 2 Pro 退料

在打印任务正常完成后，耗材会自动退回到 AMS 2 Pro。如果打印任务在中途被取消，您可以在屏幕上点击"退料"，以便让被挤出机咬合的耗材退回到 AMS 2 Pro。

![25-unload-ams-fila.png](https://public-cdn.bblmw.com/wiki/new/p2s/manual/first-print/25-unload-ams-fila.png)

### 外挂料盘退料

如近期不再使用外挂料盘上的耗材，可以将耗材退出挤出机后存储收纳。

1. 在屏幕上点击“退料”。  
   ![26-unload-external-fila.png](https://public-cdn.bblmw.com/wiki/new/p2s/manual/first-print/26-unload-external-fila.png)
2. 根据打印机提示，在耗材退出工具头后边旋转料盘，边拉回耗材。  
   当耗材接近气动接头时，用手接住耗材，并将其插入料盘上的孔洞固定。完成后，在屏幕点击“已完成，继续”。

|  |  |
| --- | --- |
|  |  |

> 如使用 P2S Combo，可将外挂料盘耗材退到缓冲器以外，无需完全拉出，便于下次继续使用。  
> ![29-unload-out-of-buffer-v2.jpg](https://public-cdn.bblmw.com/wiki/new/p2s/manual/first-print/29-unload-out-of-buffer-v2.jpg)

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)，点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
