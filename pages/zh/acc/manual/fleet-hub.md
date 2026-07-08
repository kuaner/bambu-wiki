---
path: zh/acc/manual/fleet-hub
title: "Fleet Hub 产品介绍"
description: "本文介绍 Fleet Hub 的基本定位、硬件参数、使用协议、开发资源及集成接入方式。"
tags: []
created: 2026-05-13T11:03:48.092Z
updated: 2026-06-24T01:42:53.360Z
source: https://wiki.bambulab.com/zh/acc/manual/fleet-hub
---

FleetHub 是一款面向局域网内拓竹打印机接入与控制的集成设备。它基于安全软硬件设计和双向 TLS（mTLS）机制，提供 HTTP API 能力，适用于将打印机接入企业内部系统，或构建符合自身工作流、数据本地化和传输路径可控要求的打印管理系统。

![](https://wiki.bambulab.com/part_acc/fleet-hub/007.png)

FleetHub 通过有线网络接入局域网，最多支持管理同一网络下的 50 台打印机。打印机绑定至 FleetHub 后，将与 Bambu Cloud 服务断开连接；因此，绑定期间无法同时通过 Bambu Handy 使用该打印机。

![](https://wiki.bambulab.com/part_acc/fleet-hub/006.png)

> [Fleet Hub V01.01.00.00 固件版本说明](../../software/fleet-hub-firmware-release/v01-01-00-00.md)

## 硬件参数

|  |  |
| --- | --- |
|  |  |

| 参数 | 规格 |
| --- | --- |
| **尺寸（长 × 宽 × 高）** | 100 mm × 85 mm × 28 mm |
| **外壳材料** | 铝合金 |
| **处理器** | ARM |
| **内存** | 2GB |
| **存储** | 64GB eMMC，支持 USB 闪存驱动器、MicroSD 卡 |
| **网络** | RJ45，百兆全双工以太网 |
| **环境温度** | 工作温度：0°C 至 40°C |
| **电源要求** | 5V 3A |
| **典型功率** | 5W |
| **电源接口** | Type-C |

## 使用协议与隐私政策

无论你是 FleetHub 的实际开发者、基于 FleetHub 开发应用的开发者或集成商，还是设备的实际部署和使用者，在集成、部署或使用 FleetHub 前，均应仔细阅读以下文件：

[《FleetHub 终端用户使用协议（EULA）》](https://bambulab.cn/zh-cn/fleet-hub/developer/develop-agreement)：说明设备及相关软件功能的使用规则、许可范围、使用限制、版本更新、免责声明及合规要求。

[《FleetHub 隐私政策》](https://bambulab.cn/zh-cn/fleet-hub/developer/privacy-statement)：说明在激活、访问控制、运行和技术支持过程中涉及的信息与数据处理方式，以及接入应用程序相关的数据处理边界。

## 文档与开发资源

FleetHub 的技术资料统一通过开发者页面提供。你可以根据不同阶段的需求查阅相应文档，用于了解产品能力、评估接入方案，并完成设备激活、系统集成开发与部署。

您可以在开发者页面查看或获取以下资料：

- **技术白皮书**：介绍产品定位、部署方式、集成目标和整体能力。
- **安全白皮书**：介绍安全设计、访问控制机制、数据本地化方式、证书体系及安全合规背景。
- **API 文档**：说明接口能力、调用方式、认证机制、错误码及集成方法。
- **示例代码**：提供 API 调用方式、激活流程和基础接入方法。
- **最新固件版本：** 供最新固件版本的下载链接。

## 集成接入

如需使用 FleetHub 进行系统集成，请通过以下入口获取相关信息：

- **[FleetHub 开发者页面入口](https://bambulab.cn/zh-cn/fleet-hub)**：用于查看接入说明、API 文档、示例代码及其他开发资料，并完成开发者授权、Key 管理、客户端证书签发和设备激活等操作。
- **[FleetHub 官网产品页面入口](https://bambulab.cn/zh-cn/fleet-hub/developer)**：用于查看产品介绍及采购相关信息。设备可根据项目计划安排采购，也可先完成开发者授权后再进行采购。

完成开发者授权后，可参考快速入门文档配置 Key 与证书，并结合 API 文档与示例代码开展接口开发与系统集成。

## 结束语

> 感谢您关注并使用 Fleet Hub，如在开发、集成、部署或使用过程中遇到问题，欢迎联系 Bambu Lab 开发者团队；客户支持邮箱：**[devpartner@bambulab.com](mailto:devpartner@bambulab.com)**  
> 联系支持时，建议提供以下信息，以便我们更快定位和处理问题：
>
> - 企业名称或项目名称
> - 设备序列号
> - 固件版本
> - 问题描述
> - 错误信息或相关日志
> - 网络环境说明
