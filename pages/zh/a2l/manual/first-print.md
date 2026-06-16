---
path: zh/a2l/manual/first-print
title: "A2L 首次打印"
description: "本文介绍了 A2L AMS 套装及单机的首次打印方法。引导您使用 AMS lite 或外挂料盘装载耗材并完成进料，通过打印机屏幕、Bambu Handy 和 Bambu Studio 软件发起打印任务。"
tags: []
created: 2026-06-01T13:02:09.025Z
updated: 2026-06-02T03:55:35.447Z
source: https://wiki.bambulab.com/zh/a2l/manual/first-print
---

## 视频指南

## 打印流程概览

- 根据您所购买的版本（[AMS 套装](#a2l-ams-%E5%A5%97%E8%A3%85%E8%BF%9E%E6%8E%A5%E6%96%B9%E5%BC%8F)/[单机](#a2l-%E5%8D%95%E6%9C%BA%E8%BF%9E%E6%8E%A5%E6%96%B9%E5%BC%8F)），将 AMS lite 或外挂料盘连接至打印机，装载耗材并完成进料。
- 打印前，先[检查热床](#%E6%A3%80%E6%9F%A5%E7%83%AD%E5%BA%8A)和[清洁打印板](#%E6%B8%85%E6%B4%81%E6%89%93%E5%8D%B0%E6%9D%BF)的状态，再[发起打印](#%E4%B8%89%E3%80%81%E5%BC%80%E5%A7%8B%E6%89%93%E5%8D%B0)任务。
- 打印结束后，等待模型冷却至室温后再[取下模型](#%E5%9B%9B%E3%80%81%E5%8F%96%E4%B8%8B%E6%A8%A1%E5%9E%8B)。如需更换耗材或长期不使用，请将[耗材退出](#%E4%BA%94%E3%80%81%E9%80%80%E6%96%99)打印机。

## 一、打印前准备

请先根据开箱指南完成组装，并将打印机放置在稳定平面上。

### 1. 正确安装

#### A2L AMS 套装连接方式

详细操作说明请参见 [A2L 套装开箱指南](unboxing-a2l-combo.md)。

![a2l-first-print-001-s01-setup-ams-combo-connection-v2.png](https://public-cdn.bblmw.com/wiki/new/a2l/manual/first-print/a2l-first-print-001-s01-setup-ams-combo-connection-v2.png)

#### A2L 单机连接方式

详细操作说明请参见 [A2L 单机开箱指南](unboxing-a2l.md)。

![a2l-first-print-002-s01-setup-standalone-connection-v2.png](https://public-cdn.bblmw.com/wiki/new/a2l/manual/first-print/a2l-first-print-002-s01-setup-standalone-connection-v2.png)

### 2. 开机和初始化

插入电源线，打开电源开关，并根据屏幕提示完成初始化校准。

![a2l-first-print-003-s02-power-on-initial-calibration-v2.png](https://public-cdn.bblmw.com/wiki/new/a2l/manual/first-print/a2l-first-print-003-s02-power-on-initial-calibration-v2.png)

### 3. 检查热床

在放置打印板前，请检查并清洁热床表面，确保无异物残留。若存在异物，加热过程中可能会损伤热床软磁铁表面。

![a2l-first-print-004-s03-check-clean-heatbed-v2.png](https://public-cdn.bblmw.com/wiki/new/a2l/manual/first-print/a2l-first-print-004-s03-check-clean-heatbed-v2.png)

### 4. 清洁打印板

请避免在开箱或操作过程中直接用手接触打印板表面，以免油污影响打印附着力。

如不慎触碰，请按以下步骤清洁：

1. 取出打印板，用温水和洗洁精清洗表面；
2. 使用干净的纸巾或无纺布将其擦干；
3. 确认表面清洁后，将打印板放回热床。

## 二、进料

首次打印时，请根据实际连接方式选择一种进料方式。

如需同时连接 AMS lite 和外挂料盘，或在打印中切换耗材来源，详细操作说明请参见 [A2L AMS 连接指南](a2l-ams-connection-guide.md)。

### 方式 1：AMS lite 进料

根据耗材绕线方向，将料盘安装到 AMS lite 的料盘转轴上，直至卡紧。

![a2l-first-print-005-s04-ams-feed-install-spool-v2.png](https://public-cdn.bblmw.com/wiki/new/a2l/manual/first-print/a2l-first-print-005-s04-ams-feed-install-spool-v2.png)

> **提示**：AMS lite 支持宽度为 40–68 mm、内径为 53–58 mm 的料盘。

> **注意**：请避免使用 AMS lite 来打印柔性材料，包括 TPU（AMS 专用 TPU 除外）、TPE 或潮湿的水溶性耗材 PVA。请避免使用太硬（即模量过高）或太脆（即韧性不足）的材料，包括第三方纤维增强材料，如 PA-CF/GF、PET-CF/GF 和 PLA-CF/GF 等。请使用外挂料盘的方式来打印这些耗材。

确认料盘安装到位后，按压释放按钮，并手动将耗材送入进料口，直至 AMS lite 自动拉入耗材。

![a2l-first-print-006-s04-ams-feed-insert-filament-v2.png](https://public-cdn.bblmw.com/wiki/new/a2l/manual/first-print/a2l-first-print-006-s04-ams-feed-insert-filament-v2.png)

> **提示**：如果耗材在进入挤出机前卡住，按下释放按钮可拔出耗材。

### 方式 2：外挂料盘进料

请先确认耗材类型和颜色，以便在屏幕上完成耗材信息设置。

![a2l-first-print-007-s05-external-feed-check-filament-type-color-v2.png](https://public-cdn.bblmw.com/wiki/new/a2l/manual/first-print/a2l-first-print-007-s05-external-feed-check-filament-type-color-v2.png)

在打印机屏幕上，点击**耗材 > Ext（外挂料盘） > 编辑**，选择耗材的类型和颜色后，点击**确认**，设置耗材信息。

![a2l-first-print-008-s05-external-feed-open-ext-edit-v2.png](https://public-cdn.bblmw.com/wiki/new/a2l/manual/first-print/a2l-first-print-008-s05-external-feed-open-ext-edit-v2.png)

![a2l-first-print-010-s05-external-feed-select-filament-color-v2.png](https://public-cdn.bblmw.com/wiki/new/a2l/manual/first-print/a2l-first-print-010-s05-external-feed-select-filament-color-v2.png)

按照耗材的绕线方向，将料盘放置到料盘支架上。

![a2l-first-print-012-s05-external-feed-place-spool-on-holder-v2.png](https://public-cdn.bblmw.com/wiki/new/a2l/manual/first-print/a2l-first-print-012-s05-external-feed-place-spool-on-holder-v2.png)

将耗材的一端插入料管，向工具头方向推送耗材，直至无法继续前进。此时，打印机屏幕上的工具头处会出现小绿灯，表示检测到耗材进入。

![a2l-first-print-013-s05-external-feed-insert-filament-into-tube-v2.png](https://public-cdn.bblmw.com/wiki/new/a2l/manual/first-print/a2l-first-print-013-s05-external-feed-insert-filament-into-tube-v2.png)

在屏幕上点击**进料**，等待喷嘴加热。

![a2l-first-print-015-s05-external-feed-tap-feed-v2.png](https://public-cdn.bblmw.com/wiki/new/a2l/manual/first-print/a2l-first-print-015-s05-external-feed-tap-feed-v2.png)

期间再次手动推动耗材，确保耗材仍然留在挤出机内。

![a2l-first-print-017-s05-external-feed-push-filament-during-heating-v2.png](https://public-cdn.bblmw.com/wiki/new/a2l/manual/first-print/a2l-first-print-017-s05-external-feed-push-filament-during-heating-v2.png)

观察喷嘴，根据屏幕提示完成后续操作。

![a2l-first-print-018-s05-external-feed-observe-nozzle-v2.png](https://public-cdn.bblmw.com/wiki/new/a2l/manual/first-print/a2l-first-print-018-s05-external-feed-observe-nozzle-v2.png)

## 三、开始打印

### 1. 选择模型

在首页点击**打印文件**，然后选择要打印的模型。以下以小船模型为例。

根据机型特点，打印机内置了多款实用模型（打印板保护套、热床保护架等），您可以按需选择打印。这些内置模型的详细使用指南，请参见 [A2L 配件模型介绍](internal-print-files.md)。

![a2l-first-print-020-s06-print-select-print-files-v2.png](https://public-cdn.bblmw.com/wiki/new/a2l/manual/first-print/a2l-first-print-020-s06-print-select-print-files-v2.png)

### 2. 确认配置

如需记录延时摄影视频，打开**延时摄影**功能。

根据需要在**高级设置**中开启或关闭其他选项。

![a2l-first-print-022-s07-print-enable-timelapse-v2.png](https://public-cdn.bblmw.com/wiki/new/a2l/manual/first-print/a2l-first-print-022-s07-print-enable-timelapse-v2.png)

确认要使用的耗材后，点击**打印**。

![a2l-first-print-024-s07-print-confirm-filament-v2.png](https://public-cdn.bblmw.com/wiki/new/a2l/manual/first-print/a2l-first-print-024-s07-print-confirm-filament-v2.png)

> 提示：打印机内置模型为已切片文件，请选择文件要求的耗材类型进行打印。

### 其他打印方式

#### 方法 1：从 Bambu Studio 发起打印

1. 参考[打印机账号绑定指南](../../knowledge-sharing/printer-account-binding-guide.md)连接 Wi-Fi。
2. 参考 [Bambu Studio 快速上手教程](../../software/bambu-studio/studio-quick-start.md) 安装软件，连接打印机。
3. 进入 Bambu Studio 主页，挑选想要打印的模型，选择打印配置后点击**下载并打开**。
4. 选择对应的打印机型号和打印板类型，点击**切片单盘**。
5. 点击**打印单盘**，按需设置高级选项，点击**发送**。

#### 方法 2：从 Bambu Handy 发起打印

1. 参考[打印机账号绑定指南](../../knowledge-sharing/printer-account-binding-guide.md)连接 Wi-Fi。
2. 参考 [Bambu Handy 快速入门指南](../../studio-handy/handy/bambu-handy-quick-start.md)安装软件，连接打印机。
3. 在 Bambu Handy 中选择想要打印的模型，点击**准备打印**，选择打印配置，确认打印信息，再点击**开始打印**即可将打印任务发送给打印机。

## 四、取下模型

1. 打印结束后，等待热床和模型冷却至室温后，取下打印板。轻轻弯折打印板以取下模型和擦拭塔（如有）。  
   ![a2l-first-print-026-s08-remove-model-take-off-print-plate-v2.png](https://public-cdn.bblmw.com/wiki/new/a2l/manual/first-print/a2l-first-print-026-s08-remove-model-take-off-print-plate-v2.png)
2. 使用刮刀清除打印板上的预挤出线，再将打印板重新放回热床，以便下次打印。  
   ![a2l-first-print-028-s08-remove-model-scrape-purge-line-v2.png](https://public-cdn.bblmw.com/wiki/new/a2l/manual/first-print/a2l-first-print-028-s08-remove-model-scrape-purge-line-v2.png)

> **提示**：由于固件版本不同，预挤出线可能出现在打印板前端或后端，均属正常现象。

## 五、退料

### 方式 1：AMS lite 退料

在打印任务正常完成后，AMS lite 料盘转轴回转，耗材会自动退出挤出机。

**如果打印任务在中途被取消或中断**，可以在屏幕上选择对应耗材，点击**退料**，打印机将开始自动加热热端，并切断耗材。

![a2l-first-print-030-s09-ams-unload-select-filament-unload-v2.png](https://public-cdn.bblmw.com/wiki/new/a2l/manual/first-print/a2l-first-print-030-s09-ams-unload-select-filament-unload-v2.png)

如需更换料盘，请按以下步骤操作。

在耗材退出工具头后，按住释放按钮，同时旋转料盘，将耗材收回。当耗材末端接近进料口时，用手接住耗材末端，并将耗材末端塞进料盘的孔洞中。

![a2l-first-print-031-s09-ams-unload-hold-release-button-v2.png](https://public-cdn.bblmw.com/wiki/new/a2l/manual/first-print/a2l-first-print-031-s09-ams-unload-hold-release-button-v2.png)

![a2l-first-print-033-s09-ams-unload-catch-filament-end-v2.png](https://public-cdn.bblmw.com/wiki/new/a2l/manual/first-print/a2l-first-print-033-s09-ams-unload-catch-filament-end-v2.png)

握住料盘，向料盘转轴中心方向轻推，然后向外取下料盘。

![a2l-first-print-035-s09-ams-unload-remove-spool-v2.png](https://public-cdn.bblmw.com/wiki/new/a2l/manual/first-print/a2l-first-print-035-s09-ams-unload-remove-spool-v2.png)

### 方式 2：外挂料盘退料

在屏幕上选择对应耗材，点击**退料**，打印机将开始自动加热热端，并切断耗材。

![a2l-first-print-036-s10-external-unload-select-filament-unload-v2.png](https://public-cdn.bblmw.com/wiki/new/a2l/manual/first-print/a2l-first-print-036-s10-external-unload-select-filament-unload-v2.png)

根据屏幕提示，手动旋转料盘，将耗材从铁氟龙料管中抽出。

![a2l-first-print-038-s10-external-unload-rotate-spool-v2.png](https://public-cdn.bblmw.com/wiki/new/a2l/manual/first-print/a2l-first-print-038-s10-external-unload-rotate-spool-v2.png)

## 结束语

> 我们希望本指南可以为您提供清晰实用的帮助。  
> 如果问题仍未解决，请提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)并附上您近期的打印机日志，以及相关的照片或其他详细信息，我们的技术团队将随时为您答疑解惑并提供支持。  
> 您也可以访问 [Bambu AI](https://support.bambulab.cn/cn)，它能够即时解答常见问题，并为您提供操作指导。
