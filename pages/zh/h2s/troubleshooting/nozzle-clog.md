---
path: zh/h2s/troubleshooting/nozzle-clog
title: "H2S 喷嘴/热端堵塞清理"
description: "本文将系统介绍 H2S 热端堵塞时的故障排除方法及详细操作步骤。"
tags: []
created: 2025-08-26T02:19:58.844Z
updated: 2025-09-22T09:01:11.955Z
source: https://wiki.bambulab.com/zh/h2s/troubleshooting/nozzle-clog
---

热端堵塞是 3D 打印领域内的一个常见的现象，时常会遇到这个问题。堵塞的发生有各种不同的原因，例如，热端的温度不够高，不能确保耗材在挤压时足够快地融化；或者可能你使用的耗材可能有微小颗粒(如木质的耗材或其他耗材)，这些颗粒会聚集在喷嘴的尖端，限制流动。这些现象很容易判断，会通过以下方式表现出来：

- 挤出不足（挤压出的耗材不够，导致打印模型周围有间隙）
- 没有挤出 （打印机运行正常，但没有耗材从喷头中出来）

## 所需工具

为了解决大部分的堵塞问题，你可能会用到以下工具：

- 通针
- 钳子
- 防烫手套
- 耗材
- H1.5和H2.0内六角扳手

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/troubleshooting/nozzle-clog/image.png)

## 操作前的注意事项及机器状态

> 请注意本指南中的一些涉及高温打印头的操作有一定危险性。在执行这些操作时，请采取所有必要的预防措施。对于其中的一些操作，请关闭机器并等待热端完全冷却。
>
> 在需要手持热端的时候，请您带好防烫手套。

## 操作指南

### 1. 手动挤出堵塞物

这是清理热端堵塞最简单的方法，在屏幕上将热端温度提高到略高于耗材要求的温度，然后通过屏幕菜单点击进料来挤出耗材。

#### 步骤 1. 加热热端

将热端温度提高到略高于耗材要求的温度（以PLA为例，设置热端温度为250℃）

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/troubleshooting/nozzle-clog/image-1.png)

#### 步骤 2. 手动挤出

通过点击屏幕上的进料按钮挤出耗材，观察喷嘴能否正常挤出。

|  |  |
| --- | --- |
|  |  |

### 2. 冷拔

如果无法手动挤出，打印机提供了喷嘴冷拔维护功能，帮助您完成冷拔操作。本文以PLA进行冷拔为例。

#### 步骤 1. 点击“设置”-“工具箱”

进入工具箱页面，点击“喷嘴冷拔维护”，再点击下一步。

![屏幕_冷拔.png](https://wiki.bambulab.com/h2s/%E5%B1%8F%E5%B9%95_%E5%86%B7%E6%8B%94.png)

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/troubleshooting/nozzle-clog/image-5.png)

#### 步骤 2. 修改冷拔参数

根据喷嘴尺寸、喷嘴中残留的耗材类型来选择冷拔参数。本例中喷嘴尺寸为0.4mm，冷拔耗材PLA，喷嘴中残留的耗材为PLA。确定冷拔参数后，点击开始。

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/troubleshooting/nozzle-clog/image-6.png)

#### 步骤 3. 开始冷拔

接下来打印机会自动执行冷拔流程，请按照打印机的提醒操作。

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/troubleshooting/nozzle-clog/image-7.png)

根据提示，按下黑色气动接口，拔下PTFE管。然后点击“已完成，继续”

|  |  |
| --- | --- |
|  |  |

下一步是向挤出机内插入耗材，直到推不动为止。

|  |  |
| --- | --- |
|  |  |

打印机会自动咬合耗材，加热喷嘴并开始冲刷。

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/troubleshooting/nozzle-clog/image-12.png)

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/troubleshooting/nozzle-clog/image-13.png)

等到挤出的耗材完全变成了新加载的耗材，喷嘴开始冷却。

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/troubleshooting/nozzle-clog/image-14.png)

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/troubleshooting/nozzle-clog/image-15.png)

喷嘴冷却完毕后，根据打印机提示，一只手按压从动轮支架，另一只手缓慢拉出耗材。

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/troubleshooting/nozzle-clog/image-16.png)

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/troubleshooting/nozzle-clog/image-17.png)

在已拉出的耗材末端上检查是否有杂质残留，我们强烈建议您多次重复冷拔直至拔出的耗材丝达到表面洁净无异常物质残留。若冷拔质量已经达到要求，则可以点击“完成”。

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/troubleshooting/nozzle-clog/image-18.png)

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/troubleshooting/nozzle-clog/image-19.png)

维护完成后，重新插入PTFE管。

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/troubleshooting/nozzle-clog/image-20.png)

![](https://public-cdn.bblmw.com/wiki/new/aether/h2s/troubleshooting/nozzle-clog/image-21.png)

### 3. 使用通针疏通

> 通针疏通时会释放热端内部压力，喷嘴可能突然喷出高温杂质，因此务必佩戴手套，且清理时禁止将头深入机箱观察。

如果耗材无法从喷嘴中挤出，或从喷嘴挤出的耗材没有完全变成新加载的耗材，则需要使用通针来疏通热端，并重新手动挤出耗材（循环通针疏通与挤出这一过程）。

将热端加热到220℃，等待热端达到指定温度后，将通针伸入喷嘴并上下疏通多次。

|  |  |
| --- | --- |
|  |  |

## 验证喷嘴是否正常

重新安装喷嘴，连接 PTFE 管，并重新装入耗材测试挤出效果，如果仍然堵塞或挤出不足，还需要反复多次尝试清理热端。

虽然上述方法往往能清除 99% 的堵塞物，但在有些情况下，由于喷嘴可能已经损坏，所以只需更换喷嘴。如果做完这些后，您的机器能正常打印，那么您就成功地疏通了您的喷嘴。

## 注意

0.2 mm 的喷嘴更难清除堵塞物，可能需要多次进行上述步骤。另一方面，大于 0.4 mm 的喷嘴往往比 0.4 mm 的喷嘴更少堵塞，因为喷嘴的口径开口允许更大的颗粒通过。

## 结束语

> 我们希望本指南能为您提供有用的信息，帮助您解决问题。  
> 如果您对本文有任何疑问，请联系客户服务团队，我们随时为您解答疑问并提供帮助！  
> 点击此处进入 [Bambu AI](https://support.bambulab.cn/cn)，点击此处提交[服务工单](https://bambulab.cn/zh-cn/my/support/tickets/create?from=5)。
