---
title: 人形机器人快速弹性可适配 loco-manipulation 行为系统_研读报告
arxiv_id: "2606.26425v1"
date: 2026-06-30
subarea: humanoid
tags: [robotics, humanoid, loco-manipulation, behavior-tree, affordance-template, whole-body-control, coactive-design]
---

# A System for Fast, Resilient, and Adaptable Loco-Manipulation Behaviors on Humanoid Robots

> **作者**: Duncan William Calvert (单人作者,博士论文)
> **机构**: University of West Florida, Department of Intelligent Systems and Robotics
> **发表**: 2026-06-24 · arXiv: 2606.26425v1
> **文档类型**: PhD 论文,331 页
> **本报告状态**:基于 arXiv 摘要 + 论文结构描述;完整实验数字需 PDF 验证

## 元数据

- **arXiv ID**: [2606.26425v1](https://arxiv.org/abs/2606.26425v1)
- **作者**: Duncan William Calvert
- **机构**: University of West Florida (UWF), Department of Intelligent Systems and Robotics
- **发表时间**: 2026-06-24
- **文档类型**: 博士论文(PhD dissertation), 331 页
- **视频演示**: [YouTube playlist](https://www.youtube.com/playlist?list=PLJK5CTyotYqsfgfnXb-09YNFeBose6uEY)
- **代码**: 摘要未提及开源代码
- **PDF**: [link](https://arxiv.org/pdf/2606.26425v1)
- **DOI**: 10.48550/arXiv.2606.26425

## 核心问题

人形机器人要在人类设计的工作空间中承担物理 demanding、危险和重复性工作,但**现有系统在实时协调 locomotion + manipulation + perception + operator supervision 方面存在系统性缺陷**:

1. **现有方法卡在哪**:人形机器人的行为系统通常要么是预设的硬编码序列(不可适配),要么是端到端学习方法(不可解释、不可在线修复),缺少一种"runtime 可编辑 + 可观测 + 可干预"的中间层
2. **论文认为根因是什么**:DARPA Robotics Challenge 期间发展出的 Coactive Design 原则(人机协作设计)虽然提供了正确的方向,但缺乏一个完整的工程系统将这些原则落地为可复用的行为架构
3. **论文提出的新视角**:把行为系统设计为"robot-local, runtime-editable behavior authoring and runtime system"——一个运行时可编辑的行为创作和执行系统,融合 Affordance Templates(对象中心)、Behavior Trees(逻辑组织)和 runtime-editable perception(可编辑感知)

## 方法论与核心思路

**整体框架**:系统由四个核心模块组成,形成一个从操作员到机器人执行的完整闭环:

1. **Operator Interface(操作员界面)**:持续与机器人同步,支持 runtime authoring(运行时创作)、monitoring(监控)和 repair(修复)
2. **Behavior Architecture(行为架构)**:融合三种范式
   - **Affordance Templates**:对象中心的行为模板,定义"在某个对象上能做什么 + 怎么做"
   - **Behavior Trees**:组织逻辑和执行流,提供分支、循环、优先级等控制结构
   - **Behavior Scene + Primitive Scene Actions**:运行时可编辑的感知层
3. **Action Primitives(动作原语)**:基于 whole-body controller,支持**边走边操作**(arms moving while walking)
4. **Concurrent Action Layering(并发动作分层算法)**:允许多个动作原语并行执行,提升速度

**关键创新点 1:Coactive Design 原则的工程化落地**

Coactive Design 是 DARPA Robotics Challenge 期间发展出的人机协作设计理念,强调:
- **Observable**:操作员能完整观察机器人状态
- **Predictable**:行为可预测,无意外
- **Directable**:操作员可随时干预和调整

本论文的独特贡献是将这些原则从一个设计理念落地为完整的工程系统——包含接口、架构、库和评估方法。

**关键创新点 2:三范式融合的行为架构**

不同于纯 BT(Behavior Tree)或纯端到端学习,论文提出:
- Affordance Templates 提供"对象 → 动作"的语义映射
- BT 提供执行逻辑的可组合性
- Runtime-editable perception 让感知参数(如目标位置、物体属性)可以在执行过程中修改

**关键创新点 3:Concurrent Action Layering(并发动作分层)**

传统方法通常串行执行动作原语(先走到位置 → 再抓取 → 再放下),论文提出并发分层算法:
- 多个动作原语可以同时激活
- 不同原语控制不同的 body part(手臂、躯干、底盘)
- 系统自动处理冲突和优先级

**训练 / 推理流程**:

```
[操作员指令] --> Operator Interface
                      |
                      v
              Behavior Architecture
              |-- Behavior Tree (逻辑组织)
              |-- Affordance Templates (对象-动作映射)
              |-- Behavior Scene (感知状态)
                      |
                      v
              Action Primitives
              |-- Whole-body Controller (手臂+行走协调)
              |-- Concurrent Action Layering (并行执行)
                      |
                      v
              [机器人执行] <---> [操作员实时监控/修复]
```

**与已有方法的本质区别**:

| 方法 | 范式 | 可编辑性 | 可观测性 | 人机协作 |
|---|---|---|---|---|
| 硬编码序列 | 预设 | 低 | 中 | 低 |
| 纯端到端学习 | 学习 | 极低 | 极低 | 极低 |
| 纯 Behavior Tree | 规则 | 中 | 高 | 中 |
| Coactive Design(概念） | 理念 | - | - | 高 |
| **本论文** | **融合** | **高(runtime)** | **高** | **高** |

## 核心公式提取

> 本论文是系统/工程论文,核心贡献在架构设计而非数学公式。以下为从摘要推断的关键概念形式化:

**并发动作分层**(概念公式):

$$
\mathbf{a}_t = \sum_{i \in \text{active}} w_i \cdot \pi_i(\mathbf{s}_t, \mathbf{g}_i)
$$

**符号解释**:
- $\mathbf{a}_t$ —— 时间 t 的合成动作(whole-body)
- $\pi_i$ —— 第 i 个激活的 action primitive
- $w_i$ —— 权重/优先级
- $\mathbf{s}_t$ —— 机器人当前状态
- $\mathbf{g}_i$ —— 第 i 个 primitive 的目标

**Affordance Template 执行**(概念):

$$
\text{Behavior} = \text{BT}(\{\text{AT}_1, \text{AT}_2, \ldots, \text{AT}_n\}, \text{Scene})
$$

**符号解释**:
- $\text{BT}$ —— Behavior Tree 组合逻辑
- $\text{AT}_i$ —— 第 i 个 Affordance Template
- $\text{Scene}$ —— 当前行为场景(可运行时编辑)

## 关键成果与贡献

**部署规模**:已在 **6 种不同人形机器人**上部署:
1. Boston Dynamics' DRC Atlas
2. NASA's Valkyrie
3. IHMC and Boardwalk Robotics' Nadia
4. Unitree's H1-2
5. IHMC's Alex
6. (暗示还有更多平台)

**行为库**:覆盖 **20+ 种真实机器人任务变体**:
- 推拉门(旋钮、push-bar、lever-handle 三种机构)
- 多步探索序列
- 障碍清除
- 响应式 table-to-table 操控

**效率指标**:
- 现有行为的适配、扩展、组合可在**分钟到小时级**完成新 loco-manipulation 行为
- 支持边走边操作(arms moving while walking)

**评估维度**:从 5 个维度系统评估:
1. Capability(能力)
2. Speed(速度)
3. Reliability(可靠性)
4. Speed of behavior creation(行为创作速度)
5. Adaptation, extension, combination(适配、扩展、组合能力)

**核心贡献**:
1. 提出并实现了完整的 runtime-editable behavior authoring 系统
2. 证明 Coactive Design 原则可以在工程系统中落地
3. 在 6 种不同机器人上验证泛化性,证明架构的平台无关性
4. 建立了 20+ 任务的公开行为库

## 局限性与未来展望

**论文自述的局限**(基于摘要推断):
- 作为博士论文,可能侧重系统设计而非大规模定量评估
- 行为库虽然覆盖 20+ 任务,但与端到端学习方法的任务多样性相比仍有限
- 操作员依赖:系统设计强调人机协作,可能不适合全自主场景
- 硬件依赖:虽然部署在 6 种机器人上,但都是传统液压/电动人形,未涵盖新型柔性/软体设计

**我们阅读时发现的潜在问题**:
1. **可量化对比不足**:论文是系统论文,缺少与端到端学习方法(如 pi0、RT-2)在同一任务集上的直接对比
2. **自主性边界模糊**:系统强调操作员协作,但在操作员不可用时的退化行为(autonomy fallback)未充分讨论
3. **学习模块缺失**:行为模板是手工设计的;如何用学习方法自动生成 Affordance Templates 是一个开放问题
4. **感知系统鲁棒性**:runtime-editable perception 在光照/遮挡/动态环境下的鲁棒性
5. **开源可得性**:没有提到代码开源,复现困难

**未来方向**:
- 论文方向:将行为模板与学习方法结合,实现半自动化的行为创作
- 我们的推断:可作为 VLA 模型的"执行层"——VLA 负责高层决策,本系统负责低层执行和安全管理
- 另一推断:与 LLM-based planning 结合,实现"自然语言 -> 行为树 -> Affordance Templates"的自动转换

## 复现线索

- **代码**:未提及开源
- **数据**:不依赖训练数据(系统论文)
- **硬件**:需要人形机器人平台(至少 H1-2 级别)
- **依赖**:ROS / ROS2(推断)、whole-body controller(推断基于 IHMC 的开源 Java 框架)
- **复现难度评估**:**极高**。需要人形机器人硬件 + 完整的软件栈 + 操作员培训;但部分模块(行为树、Affordance Templates)可单独复现

## 应用与行业映射(本项目强制要求)

### 1. 应用方向

- **工业 / 制造业**:在人类设计的工厂空间执行搬运、开门、清理障碍等任务
- **核电站 / 化工厂**:危险环境下的远程操作任务,操作员可通过界面远程创作和修复行为
- **灾难救援**:DARPA Robotics Challenge 场景的直接延续——废墟中的多步操作
- **航空航天**:NASA Valkyrie 的部署暗示太空/星际场景
- **家庭服务**:虽然当前定位是工业,但行为库的 table-to-table 操作可迁移到家庭
- **物流仓储**:开门、探索、搬运等行为在仓储环境中直接可用

### 2. 行业玩家

| 公司 | 关联产品 / 平台 | 受益逻辑 |
|---|---|---|
| **Boston Dynamics** | Atlas 系列 | 直接相关——论文在 DRC Atlas 上验证 |
| **NASA** | Valkyrie | 直接相关——论文在 Valkyrie 上部署 |
| **IHMC + Boardwalk Robotics** | Nadia, Alex | 直接相关——论文作者与 IHMC 有深度合作 |
| **Unitree** | H1-2 | 直接相关——论文在 H1-2 上部署;降低人形机器人行为开发门槛 |
| **Figure AI** | Figure 02 + Helix | 间接受益——行为系统架构可参考;但 Figure 更偏端到端 |
| **Tesla Optimus** | 自研平台 | 间接受益——工厂场景的行为模板设计可参考 |
| **1X Technologies** | Neo Beta | 间接——家庭场景需要 runtime-editable 行为 |
| **Apptronik** | Apollo | 间接——工业场景受益 |
| **国内: 宇树(Unitree)** | H1-2 / G1 / H1 | **直接受益**——论文已在 H1-2 上验证,可直接使用 |
| **国内: 优必选 / 傅利叶 / 智元** | 人形平台 | 受益——需要行为系统软件栈 |

### 3. 替代方案

- **现状 1:端到端 VLA(pi0 / OpenVLA)**:直接从感知到动作的学习方法;**问题**:不可解释、不可在线修复、需要大量数据
- **现状 2:传统 motion planning + task planning**:分层规划方法;**问题**:缺乏 runtime 可编辑性,人机协作能力弱
- **现状 3:纯 teleoperation**:全手动远程操作;**问题**:操作员负载高、不可扩展
- **成本对比**:
  - 本论文方法:人形机器人($20K-200K) + 行为系统软件 + 操作员培训
  - 端到端 VLA:人形机器人 + GPU 集群 + 大量训练数据
  - 全遥操作:人形机器人 + 高带宽通信 + 全职操作员

### 4. 量产壁垒

1. **硬件成本**:人形机器人本身成本高($20K-200K),即使 Unitree H1-2 也需 $20K+
2. **操作员培训**:Coactive Design 要求操作员理解行为系统,培训成本高
3. **行为库覆盖**:20+ 任务变体对于工业部署仍显不足,需要持续扩展
4. **感知鲁棒性**:runtime-editable perception 依赖感知系统稳定,在恶劣环境下(粉尘、光照变化)可能退化
5. **全自主能力**:系统设计强调人机协作,量产场景需要更高的自主性
6. **开源生态**:没有开源代码,行业采用门槛高

### 5. 时间窗估计

- **1 年内(2026-2027)**:系统论文的方法和架构被**人形机器人公司**作为软件栈参考;IHMC 相关技术可能通过 Boardwalk Robotics 商业化
- **3 年内(2027-2029)**:行为系统成为人形机器人**标配软件层**之一,类似 ROS 在移动机器人中的地位;Unitree 等公司可能采用类似架构
- **5 年内(2029-2031)**:runtime-editable behavior 理念与 VLA 融合,形成**"VLA 决策 + Coactive 执行"**的混合架构,成为人形机器人的标准范式

## 横向对比

| 方法 | 范式 | 平台覆盖 | Runtime 可编辑 | 人机协作 | 行为库 |
|---|---|---|---|---|---|
| 本论文 (Calvert) | Coactive + BT + AT | 6 种人形 | 是 | 是 | 20+ |
| pi0 (PI) | 端到端 VLA | 1-2 种 | 否 | 否 | 学习 |
| RT-2 (Google) | 端到端 VLA | 1 种 | 否 | 否 | 学习 |
| Hi5 / G1 (Unitree) | 遥操作 + 学习 | 1 种 | 部分 | 部分 | 小 |
| NaDIO (Nadia) | 行为系统 | 1 种 | 部分 | 部分 | 小 |

## 概念关联

- [[../concepts/Coactive_Design.md|Coactive Design]] — 核心设计理念
- [[../concepts/Behavior_Tree.md|Behavior Tree]] — 逻辑组织工具
- [[../concepts/Affordance_Template.md|Affordance Template]] — 对象-动作映射
- [[../concepts/whole_body_control.md|Whole-body Control]] — 底层控制基础
- [[../concepts/loco_manipulation.md|Loco-manipulation]] — 目标任务范式

## 待补充(打开 PDF 后)

- [ ] 6 种机器人的具体部署细节和对比
- [ ] 20+ 任务变体的完整列表和成功率
- [ ] Concurrent Action Layering 算法的详细伪代码
- [ ] Whole-body controller 的具体实现
- [ ] Operator interface 的设计细节和交互方式
- [ ] 与端到端学习方法的定量对比(如有)
- [ ] Behavior Scene 和 Primitive Scene Actions 的详细机制
