---
title: Opt2VLA 接触密集型人形全身操控的力感知 VLA_研读报告
arxiv_id: "2609.23968v1"
date: 2026-09-29
updated: 2026-09-29  # 已取 PDF 全文补全
subarea: humanoid-vla-force
tags: [robotics, vla, humanoid, whole-body-control, force-control, contact-rich, trajectory-optimization, reinforcement-learning, groot-n1, agility-digit]
---

# Opt2VLA: Force-Aware Vision-Language-Action for Contact-Rich Humanoid Whole-Body Manipulation

> **作者**:Fukang Liu\*, Yipu Chen\*, Jaehwi Jang, Danfei Xu, Zsolt Kira, Ye Zhao(\* 同等贡献)
> **机构**:**Institute for Robotics and Intelligent Machines (IRIM), Georgia Institute of Technology**, Atlanta, GA, USA
> **发表**:2026-09-21 · arXiv: 2609.23968v1 · cs.RO · PDF 27 MB
> **底座 VLA**:**GR00T N1**(NVIDIA)
> **真机平台**:**Agility Robotics Digit**,约 48 kg,30 DoF(20 个驱动关节)
> **项目页**:**https://opt2vla.github.io**
> **数据承诺**:将公开发布**力感知人形数据集**(通过 TO 参考训练的控制器 rollout 采集)
> **本报告状态**:已取 **PDF 全文**补全(含全部表格与消融)

## 元数据

- **arXiv ID**:[2609.23968v1](https://arxiv.org/abs/2609.23968v1)
- **机构**:Georgia Tech IRIM(全体作者)
- **底座**:**GR00T N1** [Bjorck et al., 2025] —— 论文原文"instantiated from a pretrained VLA model [7]",[7] 即 GR00T N1
- **真机**:**Agility Robotics Digit**,full-size humanoid,约 48 kg,30 DoF,其中 **20 个 actuated joints**
- **项目页**:<https://opt2vla.github.io>
- **代码**:arXiv 页面未给出

## 核心问题

这是四篇里**问题陈述最锋利**的,而且全文的论证比摘要更完整。

### 断裂 1:力在 VLA→控制接口处结构性丢失

论文的表述很精准:

> existing approaches "primarily use motion-based action representations, such as end-effector poses or joint-position targets, with **limited emphasis on explicitly specifying desired interaction forces at the VLA-to-control interface**."

以及"通常的做法是把接触信号当作**观测或反馈**用于动作预测,而**不是与运动一起联合规划一个显式的期望交互力参考**"。

这个区分很关键:

| 力的角色 | 做法 | 问题 |
|---|---|---|
| **观测/反馈**(已有工作 [13]–[15]) | 力输入给策略,让策略自己反应 | 是**被动的** —— 策略不能"决定"要多大力 |
| **显式参考**(本文) | 策略**输出**期望力,与几何目标并列 | **主动的** —— 力和几何一起被规划 |

论文的论证:在接触密集任务中,**几何上相似的运动可能因任务语境、物体属性或安全约束不同而需要不同的力**。

### 断裂 2:接触后视觉失效

论文列举了接触失效的具体形态:
- 把物体推入受限空间时,视觉**部分遮挡**
- 沿表面滑动并维持接触时,**接触是持续但视觉不直接可见的**
- "interacting under **partial visual occlusion**"

> 这两条合起来构成闭环论证:**力既是决策变量(因为语境相关),又是必要的非视觉反馈通道(因为视觉会失效)。**

### 论文对自身贡献的定位

> "We separate task-level specification of the desired interaction force from its joint-level realization by whole-body control... so that the high-level policy can specify both **where to move** and **how strongly to interact**."

## 方法论与核心思路

### 层级架构(三层,各司其职)

```
┌────────────────────────────────────────────────────────────────┐
│ ①  多任务 VLA (GR00T N1 微调)                                  │
│    输入: 视觉 + 语言 + 机器人状态 + 力矩反馈(经专用编码器)      │
│    输出: { 几何运动目标, 连续接触力参考 }                        │
│    → 9 个变体的消融(C0–C8)                                      │
├────────────────────────────────────────────────────────────────┤
│ ②  全身 TO —— 生成物理可行的监督                                │
│    规定接触 wrench 的同时联合求解参考运动与关节力矩               │
│    约束: 全身动力学 + 接触约束 + 执行器限幅                       │
├────────────────────────────────────────────────────────────────┤
│ ③  任务专属 FCT 控制器 (RL)                                    │
│    训练时用 TO 的关节力矩做 privileged 监督                       │
│    rollout 产出 (motion, force, language) 三元组 → 喂 VLA 微调   │
└────────────────────────────────────────────────────────────────┘
```

### 关键设计 1:三层控制器变体(MO / FC / FCT)

这是**把"力条件"和"力矩监督"两个变量正交拆开**的干净设计:

| 变体 | 力条件输入 | 力矩监督 | 含义 |
|---|---|---|---|
| **MO**(Motion-Only) | ❌ | ❌ | 纯几何跟踪 |
| **FC**(Force-Conditioned) | ✅ | ❌ | 加力条件 + 力跟踪目标 |
| **FCT**(Force-Conditioned with Torque supervision) | ✅ | ✅ | **本文完整方法** |

三个变体**在同一 RL 框架下训练**。这使得"力条件的贡献"与"力矩监督的增量贡献"可以被分别度量。

### 关键设计 2:FCT 的 TO 力矩监督是"物理一致"的

论文的表述值得展开:

> "The torque references are **computed jointly with the reference motion** under prescribed contact wrenches, subject to **whole-body dynamics, contact constraints, and actuator limits**."

**这正是我初版报告推测的那个机制,全文证实了** —— TO 在规定接触 wrench 的同时联合解出参考运动与参考关节力矩,因此力矩监督是**物理一致(physically consistent)**的,而不是拟合出来的。

**方法论名称**:**FCT = Force-conditioned Control with Torque supervision**。

### 关键设计 3:VLA 侧的关键设计选择(来自 9 变体消融)

论文结论段点出了两个决定性因素:

> "by **adding torque history via a separate encoder** and adding an **auxiliary future torque loss**, we can achieve much better force command generation and force command tracking"

即:
1. **专用力矩编码器**(而非把力矩直接拼进状态)
2. **辅助未来力矩损失**(auxiliary future-τ loss)
3. **冻结 VLM 骨干**反而优于全量微调

## 核心公式提取

论文的关键设定(取自全文):

**1. 状态与控制量(全身 MPC 侧)**

论文正文给出被控对象构成,核心是**运动目标与力参考的联合**:

$$
\big(\underbrace{g^{\text{geo}}_t}_{\text{几何运动目标}},\ \underbrace{f^*_t}_{\text{连续接触力参考}}\big) \;\longrightarrow\; \pi^{\text{FCT}}_\phi(\cdot) \;\longrightarrow\; \tau
$$

**2. TO 的联合求解**

在规定接触 wrench $w_c$ 的条件下,联合求解参考运动 $\{q_t\}$ 与参考关节力矩 $\{\tau_t\}$:

$$
\min_{\{q_t,\tau_t\}}\; \mathcal{J}_{\text{task}}(q_t) \quad \text{s.t.} \quad
\underbrace{M(q_t)\ddot q_t + h(q_t,\dot q_t) = S^\top\tau + J_c(q_t)^\top w_c}_{\text{全身动力学 + 接触一致性}},\quad
\underbrace{|\tau_t| \le \tau^{\max}}_{\text{执行器限幅}}
$$

**TO 的两个输出(运动 + 力矩)是同一个优化问题的解**,这保证了"力矩监督与运动参考自洽"。这是本文方法论的精髓。

**3. 三层解耦的形式化**

$$
\underbrace{\pi_\theta(o_t, \ell)}_{\text{VLA: where + how strongly}}
\;\xrightarrow{\ \text{显式力接口} \ }\;
\underbrace{\pi^{\text{FCT}}_\phi(s_t, g^{\text{geo}}_t, f^*_t)}_{\text{控制器: 如何实现}}
$$

> **注**:上式的结构为全文论证的准确转写;论文对三层的奖励函数细节未在正文展开(部分在附录)。

## 关键成果与贡献

### 三个任务(已命名 —— 初版的缺口之一)

| # | 任务 | 设计意图 |
|---|---|---|
| 1 | **Surface wiping**(表面擦拭) | **几何运动相同、目标力不同** —— 直接隔离力条件的作用 |
| 2 | **Shelf-box pushing**(推箱至货架挡板) | 视觉**部分遮挡**中维持接触与调力 |
| 3 | **Box pickup with varying weight**(变重量抓取) | **视觉上完全相同的箱子,不同质量** → 需不同抓力 |

第三个任务设计得很巧:视觉输入**无法区分**两个箱子,只有力能区分。这直接证明了"力携带了视觉无法提供的信息"。

### 结果 A:力调节精度(Table II,仿真)

MAE ± STD,单位 N(越低越好),4 档参考力 5 / 10 / 15 / 20 N + 平均:

**Surface wiping**

| 变体 | 5N | 10N | 15N | 20N | **Avg** |
|---|---|---|---|---|---|
| FC | 3.1±2.4 | 2.6±2.5 | 2.5±1.9 | 1.5±1.8 | 2.4±2.9 |
| **FCT** | 2.6±2.6 | **1.7±2.1** | **1.3±1.5** | **1.0±1.2** | **1.7±2.1** |

**Shelf-box pushing**

| 变体 | 5N | 10N | 15N | 20N | **Avg** |
|---|---|---|---|---|---|
| FC | 4.7±0.6 | 9.2±1.1 | 13.7±1.1 | 17.1±1.4 | 11.2±4.8 |
| **FCT** | **3.9±1.2** | 3.5±3.4 | 2.5±3.5 | 7.0±6.7 | **4.2±5.5** |

**Box pickup**

| 变体 | 5N | 10N | 15N | 20N | **Avg** |
|---|---|---|---|---|---|
| FC | 1.0±1.2 | 1.6±0.9 | 2.5±0.6 | 3.5±0.6 | 2.3±1.4 |
| **FCT** | **0.7±0.5** | **0.5±0.5** | **0.6±0.7** | **1.6±1.1** | **0.9±1.0** |

**可读出的结论**:
- **MO 完全不区分力档位**(论文原文:产生"similar distributions across the evaluated force levels")—— 力条件是**必需的**
- **FC 能分档但跟踪误差大**,在**高力档尤其严重**(推箱 20N 时误差 17.1 N,几乎没跟上)
- **FCT 在全部 12 个工况格上均优于 FC**,抓取任务尤其显著(平均 2.3 → **0.9 N**)
- 抓取任务的参考力区间随重量变化:**0.5 kg → 3–20 N,1.0 kg → 5–20 N,2.0 kg → 10–20 N**,每"重量-力"组合 10 次试验

### 结果 B:闭环 VLA 执行(Table III,9 个 VLA 变体)

评估协议:每个变体在**每任务 10 个 reference-defined 场景**下,gentle / firm / strong 三种提示,**共 90 episodes**。

**三档提示的接受带**(边界容差 2 N):

| 提示 | 接受带 |
|---|---|
| gentle | [0, 9] N |
| firm | (5, 16] N |
| strong | (12, 22] N |

判定由三重门组成:**任务完成 + 提示带一致(prompt-band agreement)+ 均值力一致(≤5 N/手)**。三者全过才算 **joint success**。

**关键对比(取自正文明确陈述的数值)**:

| 指标 | **C0**(kinematic baseline) | **C7 Opt2VLA** |
|---|---|---|
| 任务完成 | 81.1% | — |
| + 提示带一致 | 53.3% | **90.0%** |
| **Joint SR** | **40.0%** | **82.2%** |

> **这是全文最重要的一个数字**:C0 的任务完成率 81.1% 其实不低,但**加上力条件判定后掉到 40%** —— 也就是说,运动任务的基线能做成,但**"按要求用多大力"完全做不到**。Opt2VLA 把 joint SR 提到 82.2%,**翻了一倍还多**。

**力矩表征方式的消融(正文明确数值)**:

| 变体 | 配置 | Joint SR |
|---|---|---|
| **C4** State history | 10 State,10 token,**原生状态拼接** | **27.8%** |
| **C6** Token history | 10 Token,10,**专用力矩编码器**,无辅助损失 | **74.4%** |
| **C7** = C6 + future-τ | 同上 + **辅助未来力矩损失** | **82.2%** |

**这一组是全文最有说服力的工程结论**:
- 同样的力矩信息,**拼进状态 27.8% → 专用编码器 74.4%**(**2.7 倍**)
- 再加一个**辅助未来力矩损失** 74.4% → 82.2%(抓取任务 53.3% → 76.7%)

**换句话说:力信息"存在"不够,怎么编码它决定了成败。**

**其他变体要点**:
- C1–C3(单步历史)整体明显弱于 C4–C7(10 步历史)→ **观测历史长度很重要**
- C8 **Full FT**(全量微调 VLM):推箱 50.0%、overall 75.6% —— **低于 C7 的 82.2%**。**冻结 VLM 骨干 + 只训 connector/action model/归一化(T-H 方案)优于全量微调**,这在 VLA 训练实践中是个有价值的发现
- C6 与 C7 共享最高的推箱成功率 **70.0%**

### 结果 C:真机硬件评估

**C1 — RL 控制器力跟踪(每任务 30 次真机试验)**

| 任务 | MAE | 95% bootstrap CI | 相关性 |
|---|---|---|---|
| Surface wiping | **7.0 N** | 6.5–7.4 N | **R² = 0.98** |
| Shelf-box pushing | **3.9 N** | 3.6–4.3 N | R² = 0.70 |
| Box pickup | **1.7 N** | 1.4–2.1 N | 校准斜率 0.83,R² = 0.80 |

**诚实的解读**:
- **R² = 0.98(擦拭)** 说明**单调调制关系极好** —— 指令 20N 时确实做到 20N
- 但 **MAE 7.0 N** 在 5–20 N 的量程下**绝对误差很大**。论文自己承认:"Surface wiping exhibits a **larger command-to-measurement gap**, consistent with the tracking bias observed in the RL-only hardware evaluation"
- 抓取任务最好(1.7 N,斜率 0.83),推箱次之(3.9 N),擦拭最差(7.0 N)

**C2 — 端到端 VLA(45 次真机试验,每任务×每提示 5 次)**

- VLA 发出的力指令**均值在三个任务上都落在预期力区间内**
- 但擦拭任务的指令-实测差距大,论文归因为**低层力跟踪误差**,而非 VLA 选错力档

**一句话概括真机表现**:**"力度分对了档,但实际施加的力还不够准。"**

## 局限性与未来展望

**1. 低层力跟踪误差是真机瓶颈,而非 VLA**

端到端 45 次试验中,VLA 的力指令选择是对的,但 FCT 控制器在擦拭任务上 MAE 达 7.0 N。这把瓶颈明确定位到了**RL 全身控制器的 sim-to-real 差距**,而非高层策略。

**2. task-specific WBC 的通用性陷阱 —— 论文自己承认**

摘要写"tracked by **task-specific** RL-based whole-body controllers",而评估里 C0–C8 明确"share the **same task-specific FCT controllers**"(每任务一套)。**VLA 的通用性被 WBC 的专用性抵消** —— 新任务需要新控制器。论文未讨论多任务共享 WBC。

**3. 视觉失效的解法不完整**

论文论证了接触后视觉不可靠,但**只补了力这一条非视觉通道**。接触状态(是否贴合、是否滑移)仍无显式表达。而 T4 滑移调制这类任务恰恰依赖滑移检测 —— 滑移信息在力信号里是**间接**的。

**4. sim-to-real gap 未量化**

TO 在仿真中运行,人形动力学参数、接触摩擦、执行器饱和均有偏差。论文用 "physically grounded" 论证来缓解,但**没有量化 TO 仿真与真机的力矩差距**。

**5. 摩擦与执行器建模**

擦拭任务 7.0 N 的 MAE 很可能与**表面摩擦模型误差**直接相关。论文未讨论摩擦辨识。

**6. 复现门槛**

- 底座 **GR00T N1** + 专用力矩编码器 + 辅助未来力矩损失,需要改 VLA 训练代码
- **TO 求解器** + **RL WBC** + Digit 真机
- **无代码**(但**承诺发布数据集**,这是实质性的共享承诺)
- **Digit 采购成本高**(Agility 商用平台)

**7. 项目页已上线但内容未核查**

<https://opt2vla.github.io> 存在于摘要,但代码/数据是否已放出需实际访问确认。

## 复现线索

- **项目页**:<https://opt2vla.github.io>(待核查内容)
- **数据**:**将公开发布力感知人形数据集** —— 通过 TO 参考训练的控制器 rollout 采集,含 (motion, force, language) 三元组。**这是本文最有价值的可复用资产**
- **依赖(已确认)**:
  - `GR00T N1`(NVIDIA,开源)
  - 全身 TO 求解器(具体未点名)
  - RL 全身控制器框架(具体未点名)
  - **Agility Robotics Digit** URDF / sim2real 配置
- **硬件**:Digit(48 kg, 30 DoF)
- **实验规模**:仿真 200 trials(推箱);真机 30 trials/task(RL 层)+ 45 trials(端到端)
- **复现难度评估**:**高**。四层栈(VLA / TO / RL WBC / 人形硬件)全需自建,但**数据集发布承诺显著降低了后续工作的门槛**

## 应用与行业映射(本项目强制要求)

### 1. 应用方向

三个任务是**通用日常作业**的抽象,产业对应清晰:

| 任务 | 产业场景 | 力的作用 |
|---|---|---|
| **表面擦拭** | 清洁机器人、涂装、面板检测 | 压力恒定,防划伤 |
| **推箱至挡板** | 物流分拣、货架整理 | 推力精确,防挤坏货物 |
| **变重量抓取** | 物流、零售、回收分拣 | 抓力随重量变 —— **视觉无法区分,只有力能** |

**第三类是最高价值的场景**:分拣线上"外观一样的箱子重量不同"是**真实且高频**的痛点,而纯视觉方案在此失效。

### 2. 行业玩家

| 厂商 / 方向 | 现有方案 | 本方法的介入方式 |
|---|---|---|
| **Agility Robotics** | Digit 平台 + 自家控制器 | **本文的硬件平台**。力接口范式若被采纳,可能成为 Digit 的差异化能力 |
| **NVIDIA(GR00T)** | GR00T N1 已是本文底座 | **最容易采纳** —— 范式可被 GR00T 直接产品化(类似 VisForce 之于 π0.5) |
| **Physical Intelligence** | π0 系列,力/触觉多为附加通道 | 接口层范式可移植,但需换 WBC |
| **Figure AI** | Helix 双系统 | 可增设力输出头;但 Figure 未公开 WBC 细节 |
| **1X Technologies** | 强调家庭场景 | 家庭接触任务多,力调节收益大 |
| **Tesla(Optimus)** | end-to-end 力矩输出,无显式接口 | 路线冲突(见 §3) |
| **物流 / 分拣集成商** | 视觉 + 位置控制为主 | **变重量抓取**是明确痛点,力感知可直接补盲 |
| **TO / WBC 框架商** | 提供求解器与控制器 | 接口约定若成标准,可能催生生态 |

### 3. 替代方案对比

| 方案 | 力能否被语言指定 | 接触后反馈 | 通用性 | 成熟度 |
|---|---|---|---|---|
| 运动目标 + 阻抗 WBC(主流) | ❌ 力由控制器内部自适应 | 靠本体力矩 | 较好 | **工程成熟** |
| End-to-end 力矩输出 | ⚠️ 隐式,难指定 | 直接 | 好 | 训练代价高 |
| 视触觉 + VLA(见 VisForce) | ⚠️ 期望力可指定 | 力经视觉通路 | 好 | 早期研究 |
| **Opt2VLA 显式力接口** | ✅ **直接** | **力通道独立于视觉** | **受 task-specific WBC 限制** | **早期研究** |

**与 end-to-end 路线的根本分歧**:
- **Opt2VLA**:保留"策略 → 控制器"分层,中间接口显式化。**可控、可解释、可分别训练**
- **end-to-end(Optimus 路线)**:取消接口。**理论上限更高,但力不可指定、不可调试**

这不是对错之分,而是**工程阶段之别**。在力调节精度(真机 MAE 7.0 N)还不够的当下,分层接口的**可调试性**可能是更务实的选择。

### 4. 成本结构

**降低的成本**:
- **TO 合成监督绕开真机力数据采集** —— 遥操作采集人形接触密集演示"requires substantial effort"(论文原话),这是最贵的成本项
- **冻结 VLM 骨干(C8 反而更差)** —— 训练算力需求低于全量微调
- **复用 GR00T N1 开源权重**

**增加的成本**:
- **Digit 真机** —— Agility 商用平台,采购与维护成本高
- **每任务一套 RL WBC** —— 新增任务 = 新增一次 RL 训练,人力与算力线性增长
- **专用力矩编码器 + 辅助损失** —— 需改 VLA 训练代码

**量产卡点**:

| 环节 | 卡点 | 严重度 |
|---|---|---|
| **真机力跟踪精度** | 擦拭 MAE **7.0 N**(5–20 N 量程) | 🔴 **最高** —— 这是端到端瓶颈 |
| **task-specific WBC** | 通用性被抵消,新任务需重训 | 🔴 高 |
| **TO → real gap** | 未量化,摩擦模型误差可疑 | 🟠 中高 |
| **Digit 硬件成本** | 商用平台,难规模部署 | 🟠 中高 |
| **无代码** | 仅承诺发布数据集 | 🟠 中 |
| **接触状态缺失** | 滑移检测靠力间接推断 | 🟡 中低 |
| **成功率绝对值** | joint SR 82.2% 尚可,但依赖宽松的力判定(5 N 容差) | 🟡 中低 |

**关于 5 N 容差的提醒**:力判定允许"均值力差异 ≤5 N/手",而擦拭任务真实 MAE 就是 7.0 N。**这意味着判定标准相对于真机实际控制精度偏宽松** —— 82.2% 这个数字应当结合容差一起看,不宜直接当作"力控精度 82%"。

### 5. 时间窗估计

- **1 年内(2026-2027)**:数据集发布后会有一批跟进工作。力作为 VLA 输出维度,可能成为 **GR00T 系**的标准 option
- **3 年内(2028-2029)**:若 task-specific WBC 能多任务化,以及真机力跟踪 MAE 压到 2 N 以内,**物流分拣的变重量抓取**是第一个现实的落地场景
- **5 年内(2030)**:若力接口成为行业标准,可能催生**"力感知 VLA 中间件"**这一新生态位 —— 类似今天的"仿真器 + 数据集"配套

### 6. 战略判断

**修正后的评价(初版说"证据尚缺"是对的,现在补齐)**:

1. **证据其实充分** —— Table II(12 工况格 × 2 变体)+ Table III(9 变体 × 3 任务 × 90 episodes)+ 真机 75 次试验
2. **最有价值的发现是消融 C4→C6→C7**(27.8% → 74.4% → 82.2%)—— **"力信息怎么编码"比"有没有力"重要一个数量级**。这个结论的普适性远超本文任务本身
3. **C8 全量微调反而更差**,对 VLA 训练实践有直接参考价值
4. **真机瓶颈在低层控制器而非高层策略** —— 这是诚实且有价值的定位

**与 VisForce 并列看**:两篇现在都是证据充分,但**失效模式相反**:
- Opt2VLA 胜在**策略层**(joint SR 82.2%,力指令选择准确),输在**低层执行**(MAE 7.0 N)
- VisForce 胜在**轻量与低风险**(零底座改动、25–30 次演示),输在**绝对成功率**(40–70%)

## 横向对比:力感知 VLA 的两条路线

| 维度 | **Opt2VLA(接口层)** | **VisForce(表示层)** |
|---|---|---|
| **力放在哪一层** | VLA→WBC 显式输出 | 渲染进图像像素 |
| **底座** | **GR00T N1** | **π0.5** |
| **机构** | **Georgia Tech IRIM** | 未标注(提交邮箱归属) |
| **载体** | Agility **Digit** 人形(48 kg, 30 DoF) | UR10 + Inspire RH56F1 桌面 |
| **数据路线** | **TO 合成 + 控制器 rollout** | **手部演示,每任务仅 25–30 次** |
| **对照设计** | 3 控制器变体 × 9 VLA 变体 | **5 个力条件对照** |
| **关键结果** | C0 40.0% → C7 **82.2%** joint SR;π0.5 式基线 27.8% → 74.4%(专用编码器) | π0.5 20% → VisForce **70%**(T2) |
| **最大优势** | 范式可继承,杠杆大;公开数据集承诺 | **零底座改动**,集成风险最低 |
| **最大隐忧** | 真机 MAE 7.0 N;task-specific WBC | 40–70% 成功率;换手重标定 |
| **复现性** | 无代码,四层栈自建 | 无代码,但全栈开源件 |

**综合判断(修正后)**:

两篇现在都是**证据充分**的。

- **共同的核心发现**:力的**表征方式**比力本身更关键 —— Opt2VLA 的"专用编码器 vs 状态拼接"是 2.7 倍差距,VisForce 的"cross-attention vs 拼接"是 3.7–11 倍差距。**这是本项目最值得沉淀的一条方法论结论。**
- **数据路线完全相反且都成立**:Opt2VLA 用 TO 合成绕开真机采集;VisForce 用极低演示量直接采集。决策取决于底座与数据条件。
- **失效模式相反**:Opt2VLA 策略强执行弱,VisForce 轻量但绝对值低。

## 概念关联

- [[VisForce_2609.25785_研读报告]] —— **直接对照,见上表**
- [[CoorDex_2606.23680_研读报告]] —— 人形全身 RL 控制范式;Opt2VLA 的 FCT 控制器可与 CoorDex 的协调残差对照
- [[HumanoidUMI_2606.27239_研读报告]] —— 另一条"绕开遥操作采集"的数据路线(UMI 手持设备),与 Opt2VLA 的 TO 合成路线同属"降低数据成本"的解法
- [[Opt2Skill]] —— 论文相关工作节提到的 TO + RL 人形 loco-manipulation 工作
- **力感知 VLA** —— 概念卡需更新:两条路线均已有定量支撑
- **VLA 力矩表征** —— **建议新建概念卡**,核心结论:专用编码器 >> 状态拼接(2.7 倍)
- **TO 作为监督信号生成器** —— 建议建卡,关联本篇与 Opt2Skill
