---
title: MuseVLA 自适应多模态感知 VLA 模型_研读报告
arxiv_id: "2606.17598v1"
date: 2026-06-17
subarea: vla
tags: [robotics, vla, multimodal-sensing, dexterous-hand, tool-call, sensor-fusion]
---

# MuseVLA: An Adaptive Multimodal Sensing Vision-Language-Action Model for Robotic Manipulation

> **作者**:Xingyuming Liu, Ruichun Ma, Heyu Guo, Qixiu Li, Qingwen Yang, Lin Luo, Shiqi Jiang, Chenren Xu, Jiaolong Yang, Baining Guo
> **发表**:2026-06-16 · arXiv: 2606.17598v1
> **摘要长度**:完整 arXiv 摘要
> **本报告状态**:首次入册,基于摘要+标题深度推理;完整公式与实验数字需要 PDF 验证

## 元数据

- **arXiv ID**: [2606.17598v1](https://arxiv.org/abs/2606.17598v1)
- **作者**:Xingyuming Liu, Ruichun Ma, Heyu Guo, Qixiu Li, Qingwen Yang, Lin Luo, Shiqi Jiang, Chenren Xu, Jiaolong Yang, Baining Guo
- **机构推断**:从作者列表判断 — 团队混合了 **北京大学(Chenren Xu 长期在 PKU)** 与 **微软亚洲研究院 / 微软研究院(MSRA, Jiaolong Yang、Baining Guo 均为 MSRA 资深学者)** 的可能组合;Lin Luo、Shiqi Jiang 等也与 MSRA 强关联。**待 PDF 确认**。
- **发表时间**:2026-06-16
- **代码**:摘要未提及(待 PDF 确认)
- **项目页**:摘要未提及(待 PDF 确认)
- **PDF**:[link](https://arxiv.org/pdf/2606.17598v1)

## 核心问题

当前 VLA(RT-2 / OpenVLA / Octo / π0)模型的**单模态瓶颈**:

1. **现有方法只用 RGB**:几乎所有主流 VLA 都假设输入是 RGB 图像,把"温度 / 声音 / 雷达反射 / 深度 / 力矩"这类**无法从 RGB 反推的物理属性**全部放弃
2. **任务不可达**:大量真实操控任务在纯视觉下根本不可解 — 例如"把温度高于 60°C 的零件挑出来"、"听到玻璃破碎声就去找"、"隔着墙探测金属物体"等
3. **多模态整合代价高**:传统做法是把所有传感器 raw 数据塞进模型,导致输入维度爆炸 + 训练数据稀缺的"双重灾难"

论文的根因诊断:**VLA 不应该"被迫"接受所有模态,而应该像 LLM 一样按需调用** —— 这是论文最核心的视角切换。论文把"多模态感知"问题重新定义为**工具调用(tool call)**问题。

## 方法论与核心思路

**整体框架**:MuseVLA = Multimodal Sensor VLA,核心是把"调用哪个传感器 + 关注什么"做成可学习的"工具调用"。

**三阶段流程**:

1. **任务理解 + 工具选择**:给定任务指令与视觉上下文,VLA 先生成
   - **sensor token** —— 选择调用哪个传感器(温度 / 麦克风 / 雷达 / ... 中的一个)
   - **target description** —— 描述"传感器应该关注哪个区域 / 对象 / 属性"
   - 这一步类比 LLM 的 `function_call(name="temperature_sensor", args={"region": "mug_handle"})`
2. **传感器测量 → grounded sensor image**:把异构传感器读数(温度值 / 频谱 / 雷达散射)转换为**统一的中间表示 —— grounded sensor image**(传感器读数被"贴回"原图的对应空间位置)
3. **多模态融合 + 动作生成**:grounded sensor image 与 RGB 一起送入 VLA backbone,生成操控动作

**关键创新点 1:sensor token 工具调用机制**

把传感器选择建模为离散 token(类似 LLM tool call),而不是连续条件输入,带来 3 个收益:
- **离散决策**:传感器选择变得可解释、可审计、可调试
- **稀疏激活**:不需要每帧调用所有传感器,只在需要时调用,降低硬件成本和延迟
- **自然泛化**:新增传感器只需扩充 token 词表,backbone 不需要重新训练

**关键创新点 2:grounded sensor image 作为统一中间表示**

这是论文最巧妙的工程抽象:
- 温度传感器的 1D 数值 → 贴回图像,变成"温度图"
- 麦克风的频谱 → 时间窗口切片后贴回图像,变成"声音热力图"
- 雷达散射 → 投影到图像平面,变成"雷达叠加图"

这种设计**解耦了"传感器数据处理"与"VLA 主干"**,VLA backbone 永远只接收图像格式的输入,backbone 完全无感于"这张图来自什么传感器"。

**关键创新点 3:数据合成 pipeline**

为了让模型学会 grounded sensor image,VLA 不需要真实多模态数据集(成本极高),而是:
- 在现有 RGB 视频数据集上,**用仿真 / 物理模型合成**对应传感器的"grounded 图像"
- 例如:对一个 RGB 视频,根据场景物理属性合成"温度场"图像
- 训练时 VLA 见到的是合成的 grounded image,推理时是真实传感器读数

**与已有方法的本质区别**:

| 方法 | 模态 | 架构 | 数据 |
|---|---|---|---|
| RT-2 / OpenVLA / Octo | 仅 RGB | 单流 VLA | OpenX-Embodiment |
| π0 | RGB + 力矩 | 双流 + 早期融合 | 多机厂数据 |
| 3D Diffusion Policy (DP3) | RGB + 点云 | 3D 表征 | 仿真 + 真实 |
| 通用多模态 LLM(LLaVA) | RGB + 文本 | 视觉编码 + LLM | 图像文本对 |
| **MuseVLA** | **RGB + 按需异构传感器** | **tool call + grounded image** | **合成增广** |

**架构图(基于摘要描述的模块流)**:

```
[任务指令] ──┐
             ├─→ VLA Backbone ──→ sensor token + target description
[RGB 图像] ──┘                              │
                                            ▼
                                 [选定传感器] [被激活,采集]
                                            │
                                            ▼
                                  grounded sensor image
                                            │
                                            ▼
                          VLA Backbone(融合 RGB + grounded image)
                                            │
                                            ▼
                                        [动作输出]
```

## 核心公式提取

> 基于摘要推断;待 PDF 验证

**工具调用决策**(离散化 sensor token):

$$
p(s_t \mid \text{task}, \text{rgb}_t) = \text{Softmax}\big( W_s \cdot \text{VLA}_\phi(\text{task}, \text{rgb}_t) \big)
$$

**符号解释**:
- $s_t$ —— 第 t 步选定的传感器类型(温度 / 麦克风 / 雷达 / 不调用)
- $W_s$ —— 传感器选择 head 的参数
- $\text{VLA}_\phi$ —— 共享的 VLA 表征

**grounded sensor image 转换**(异构 → 统一):

$$
I^{\text{grounded}}_t = \mathcal{T}\big( \text{sensor\_reading}_t, \text{RGB}_t, \text{pose}_t \big)
$$

**符号解释**:
- $\mathcal{T}$ —— 传感器标定 + 空间投影函数(类似 NeRF 的 pose-conditioned rendering)
- 关键:**输出格式是图像**,VLA backbone 看到的输入空间不变

**总训练目标**(多任务联合):

$$
\mathcal{L} = \mathcal{L}_{\text{action}} + \lambda_1 \mathcal{L}_{\text{sensor\_select}} + \lambda_2 \mathcal{L}_{\text{target\_desc}} + \lambda_3 \mathcal{L}_{\text{synth\_align}}
$$

**符号解释**:
- $\mathcal{L}_{\text{action}}$ —— 动作预测损失
- $\mathcal{L}_{\text{sensor\_select}}$ —— 传感器选择监督
- $\mathcal{L}_{\text{target\_desc}}$ —— target description 生成监督
- $\mathcal{L}_{\text{synth\_align}}$ —— 合成的 grounded image 与真实传感器读数的一致性损失(用于 sim-to-real 桥接)
- $\lambda_i$ —— 平衡项

## 关键成果与贡献

**核心数字**(摘要中明确):
- 真实机器人平台 **80.6% 平均成功率**
- 显著优于 RGB-only baseline 与 multisensory VLA baseline
- 在**未见任务**上展现强 zero-shot 能力

**三类典型任务**:
1. **温度引导的 pick-and-place**:把"高温零件"挑出来放在指定位置
2. **声音驱动的物体搜索**:听到声音,定位声源物体并抓取
3. **雷达辅助的隐藏物体检索**:隔着遮挡找到金属物体

**核心贡献**:
1. 提出 **"VLA = 工具调用者"** 的新范式 — 改变了 VLA 与传感器的关系,从"被迫全吃"到"按需调用"
2. 提出 **grounded sensor image** 统一中间表示 — 让异构传感器复用同一 backbone
3. 提出 **数据合成 pipeline** — 把多模态 VLA 训练从"必须有真机多传感器数据"解放为"RGB + 物理仿真"
4. 在灵巧手任务上验证 80.6% 成功率,显著超越 RGB-only baseline

## 局限性与未来展望

**论文自述的局限**(待 PDF 验证):
- 工具调用 sensor token 的词表大小:目前支持几种传感器?是否能扩展到几十种?
- 数据合成的物理可信度:合成 grounded image 在多大程度上能替代真实传感器读数
- 推理时延:传感器调用 + VLA 推理 + 动作生成的总延迟是否满足实时控制
- 任务泛化:zero-shot 到完全未见任务的成功率具体多少

**我们阅读时发现的潜在问题**:
1. **sensor token 选错的级联效应**:选错传感器 → 错的 grounded image → 错的动作;错误是否会累积?
2. **"按需调用"的边界**:在某些任务里多个传感器同时需要(温度 + 雷达),单 token 设计如何处理并发调用
3. **数据合成的领域鸿沟**:合成温度图 vs 真实热成像的差距在工业 / 户外 / 高速运动场景下是否可接受
4. **calibration 漂移**:grounded sensor image 依赖精确的空间标定;长时间运行后传感器偏移如何处理
5. **传感器硬件门槛**:工业级热像仪 / 麦克风阵列 / 毫米波雷达的 BOM 成本

**未来方向**(论文提的 + 我们的推断):
- 论文方向:更多传感器类型(嗅觉 / 触觉 / 近红外 / ToF)、更多任务域(医疗 / 农业 / 安防)
- 我们的推断:可与 VLA π0 系列的"通用基础模型"路线结合 — π0 负责高层指令理解,MuseVLA 负责多模态感知落地
- 另一推断:可与 **触觉基础模型**(项目目前 5 个 sub-area 之外的子领域)整合,实现"视觉 + 听觉 + 触觉"三模态 VLA

## 复现线索

- **代码**:待 PDF 确认(摘要未提)
- **数据**:可能依赖 DROID / Bridge / Open X-Embodiment + 自建多模态数据集;数据合成 pipeline 是核心依赖
- **硬件**:多模态传感器(热像仪 / 麦克风阵列 / 毫米波雷达)+ 灵巧手;真实机器人平台
- **依赖**:PyTorch + VLA backbone(可能基于 OpenVLA 或自研)
- **复现难度评估**:**高**。数据合成 pipeline + 多传感器 calibration 是核心门槛;VLA 主干训练本身门槛中等

## 应用与行业映射(本项目强制要求)

### 1. 应用方向

- **特种作业**:核电站温度监控(挑出"热"管道 / "冷"容器)、化工厂气体泄漏检测
- **工业制造**:芯片工厂的晶圆温度监测、汽车涂装车间漆膜厚度雷达检测
- **物流仓储**:冷链仓库按温度分拣、夜间通过声音定位跌落包裹
- **家庭服务**:听声定位 + 视觉确认(找打翻的玻璃杯)、过热报警关火
- **医疗**:超声辅助手术、近红外血氧检测
- **应急救援**:烟雾 / 瓦砾中通过声学 + 雷达定位受困者

### 2. 行业玩家

| 公司 | 关联产品 / 模型 | 受益逻辑 |
|---|---|---|
| **Physical Intelligence (PI)** | π0 系列 | 直接受益 — π0 当前只用 RGB + 力矩,接入 MuseVLA 的 sensor token 范式可扩展到温度 / 声音 |
| **Figure AI** | Figure 02 + Helix | 受益 — Helix 工厂场景多温度,加温度传感器可解决"挑出热工件"等任务 |
| **1X Technologies** | Neo Beta | 受益 — 家庭场景中声音驱动(寻找跌落物品)是关键需求 |
| **Apptronik** | Apollo + Google DeepMind Gemini Robotics | 受益 — DeepMind 路线可能向多模态扩展 |
| **Tesla Optimus** | 自研 + FSD 视觉栈 | 受益 — 自动驾驶的多传感器融合经验可迁移 |
| **Boston Dynamics** | Atlas + RL 控制栈 | 受益 — 工业场景多模态需求强 |
| **Sanctuary AI** | Phoenix + Carbon | 受益 — Carbon 通用大脑路线契合 tool call 范式 |
| **国内**:宇树(Unitree) / 智元(AgiBot) / 傅利叶 / 优必选 | 人形机器人 | 直接受益 — 多模态传感器集成是产品差异化点 |
| **传感器 OEM**:FLIR(热像仪) / Velodyne(雷达) / 歌尔(声学) | 硬件供应 | **直接受益** — 多模态 VLA 拉动传感器 BOM |

### 3. 替代方案

- **现状 1:多模态 LLM 端到端**:LLaVA-NeXT / Qwen-VL 等直接吃多张图;**问题**:不支持工具调用、无法选传感器、训练数据极贵
- **现状 2:任务专用传感器 + 硬编码策略**:为每个任务写专用代码;**问题**:不可扩展,每次新增传感器需要重写
- **现状 3:多模态融合 + 早期融合 VLA**:把所有传感器数据 concat 进 backbone;**问题**:输入维度爆炸、训练数据稀缺
- **成本对比**(估算):
  - MuseVLA 风格(按需传感器):1-2 个传感器($500-3000) + VLA 主干
  - 多模态早期融合:5-10 个传感器($3000-10000) + 大模型

### 4. 量产壁垒

1. **多传感器标定**:grounded sensor image 依赖精确外参;量产现场标定成本高
2. **传感器可靠性**:工业级热像仪 / 雷达的 MTBF 与成本量级
3. **训练数据**:真实多模态数据仍然稀缺(论文用合成弥补,但工业场景物理模型不准)
4. **延迟**:多传感器调用 + VLA 推理 + 控制的端到端延迟需要 < 100ms
5. **安全认证**:UL 3300 / 欧盟 AI Act 对家庭场景的多传感器融合(尤其是声学)隐私有严格要求
6. **API / 标准化**:sensor token 词表需要行业共识,否则不同 VLA 间不兼容

### 5. 时间窗估计

- **1 年内(2026-2027)**:论文方法进入 **PI / Skild / Figure** 等头部 VLA 公司的研究路线;开源版本可能激发 PoC
- **3 年内(2027-2029)**:成为 **"多模态 VLA 训练"的标配**;类似 2024 年 3D 点云被纳入主流 VLA 的节奏
- **5 年内(2029-2031)**:sensor token 范式可能成为 **VLA 行业标准**的一部分,类似 LLM 的 function call;**消费级家庭机器人**因多模态受益显著

## 横向对比(可选)

| 方法 | 模态 | 工具调用 | 数据合成 | 灵巧手任务 |
|---|---|---|---|---|
| RT-2 | 仅 RGB | ❌ | ❌ | 一般 |
| OpenVLA | 仅 RGB | ❌ | ❌ | 一般 |
| π0 | RGB + 力矩 | ❌ | ❌ | ✅ |
| 3D Diffusion Policy | RGB + 点云 | ❌ | ✅ | 部分 |
| Octo | 仅 RGB | ❌ | ❌ | 部分 |
| **MuseVLA** | **RGB + 按需异构** | **✅** | **✅** | **✅ 80.6%** |

## 概念关联

- [[../concepts/VLA.md|VLA 范式]] — 上游决策层
- [[../concepts/multimodal_fusion.md|多模态融合]] — 方法论父概念
- [[../concepts/tool_calling.md|Tool Calling 范式]] — 来自 LLM 的范式迁移
- [[../concepts/dexterous_hand_cost.md|灵巧手成本结构]] — 硬件约束
- [[../concepts/sim2real_gap.md|sim2real]] — 数据合成 pipeline 的理论基础

## 待补充(打开 PDF 后)

- [ ] 具体的实验数字(每个任务的成功率、与 baseline 的差距)
- [ ] sensor token 词表大小
- [ ] 数据合成 pipeline 的细节(物理模型、可信度)
- [ ] grounded sensor image 的具体形式
- [ ] 真实机器人平台的硬件规格
- [ ] 作者机构与产业链关系
- [ ] zero-shot 任务的完整列表
- [ ] 推理延迟与硬件 BOM
