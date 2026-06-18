---
title: WireCraft 工业 DLO 操控仿真基准_研读报告
arxiv_id: "2606.18097v1"
date: 2026-06-18
subarea: simulation
tags: [robotics, deformable-linear-objects, benchmark, industrial-assembly, sim2real, ur5, rl, vla, insertion]
---

# WireCraft: A Simulation Benchmark for Industrial DLO Manipulation

> **作者**:Chongyu Zhu, Ramy ElMallah, Hyegang Kim, Zachary Tang, Jiachen Rao, Artem Arutyunov, Seungyeon Ha, Chi-Guhn Lee
> **机构**:**University of Toronto**(MIE + CS) · **CREFLE Inc.**(Seongnam, Republic of Korea)
> **通讯作者**:cyzhu@mie.utoronto.ca
> **发表**:2026-06-16 · arXiv: 2606.18097v1 · cs.RO
> **本报告状态**:首次入册,基于摘要 + HTML 全文(arxiv.org/html/2606.18097)的深度整理

## 元数据

- **arXiv ID**:[2606.18097v1](https://arxiv.org/abs/2606.18097v1)
- **作者**:Chongyu Zhu, Ramy ElMallah, Hyegang Kim, Zachary Tang, Jiachen Rao, Artem Arutyunov, Seungyeon Ha, Chi-Guhn Lee
- **机构**:University of Toronto(Department of Mechanical and Industrial Engineering + Department of Computer Science) · CREFLE Inc.(Seongnam, Republic of Korea)
- **发表时间**:2026-06-16
- **会议 / 期刊**:预印本(待投递)
- **PDF**:[link](https://arxiv.org/pdf/2606.18097v1)
- **代码 / 基准**:作者承诺"upon acceptance"开源(目前未发布)

## 核心问题

**DLO(Deformable Linear Objects,线缆 / 绳 / 线状柔性物体)**是工业装配的核心对象,但**没有统一的基准**来评估操控策略:

1. **状态空间无限维**:刚体只需要 6-DoF 位姿,DLO 的状态是无限维的(整条线的形状 = 无数个点的位置)
2. **与 fixtures(夹具 / 障碍)持续接触**:DLO 一直被各种夹具挤压、形变
3. **现有基准太散**:
   - 部分基准绑定特定硬件 → 不能跨平台比较
   - 部分基准任务太通用(generic deformable)→ 跟工业实际场景差太远
   - 几乎没有"sim + 真实 + 共享评估协议"三位一体的基准
4. **关键子任务没覆盖**:**connector insertion(连接器插接)**、**clip routing(线缆卡扣穿引)**、**channel seating(线缆沿通道布置)**—— 工业 80% 装配工作都是这三种

**根因诊断**:学界 DLO 评测**碎片化** —— 一篇论文一个任务、一套评估方式,无法横向比较,也无法追踪 SOTA 进步。

**核心视角**:把"工业 DLO 操控"作为**通用灵巧操控的核心试金石** —— 如果一个方法在 DLO 上成功,基本就能推广到一般接触丰富任务。

## 方法论与核心思路

### 整体框架

WireCraft = 一个**模块化、可配置难度、跨 sim/real 的 DLO 操控基准**。

```
+---------------------------------------+
|        WireCraft Benchmark            |
+---------------------------------------+
|                                       |
|   3 Task Families:                    |
|     A. Connector Insertion  (5 形状)  |
|     B. Clip Routing         (1/2/3 卡)|
|     C. Channel Seating      (5 段)   |
|                                       |
|   2 DLO Physics Models:               |
|     - Articulated (铰接链)            |
|     - Deformable (连续形变)          |
|                                       |
|   Sim + Real (UR5) with shared schema |
|     - LeRobot-compatible              |
|     - 7D state / 7D action            |
|     - Wrist + 3rd-person RGB          |
|     - Language instruction            |
|                                       |
|   Benchmarked Policies:               |
|     - RL  (PPO, SACfD)                |
|     - IL  (ACT)                        |
|     - VLA (π0.5)                       |
+---------------------------------------+
```

### 关键创新点 1:三任务族 + 难度轴

**A. Connector Insertion(连接器插接)**
- 5 种几何形状,沿"难度轴"展开:
  - 圆柱(rotation-invariant,最易)
  - 立方体
  - Ethernet 网线
  - DisplayPort
  - USB-A(orientation-sensitive,最难)
- **典型应用**:服务器线缆、显示器连接、消费电子

**B. Clip Routing(线缆卡扣穿引)**
- 1-clip → 2-clip → 3-clip 序列
- 难度由"clip 数量"和"随机 yaw"控制
- **典型应用**:汽车线束、机箱内部走线

**C. Channel Seating(线缆沿通道布置)**
- 5 段 channel,每段弯曲角 0° / ±20°
- 难度由"每段弯曲度"控制
- **典型应用**:电动车电池包布线、航空航天线缆

### 关键创新点 2:双 DLO 物理模型

| 模型 | 适用 | 优势 | 限制 |
|---|---|---|---|
| **Articulated(铰接)** | 线束/线缆/工业装配 | 仿真快(可扩到 8K 并行环境) | 真实感差(无法模拟细线弯曲) |
| **Deformable(连续形变)** | 真实线缆/绳/电线 | 物理真实 | 仿真慢(只能 2K 并行,4K 崩) |

这种"难度/真实度"的二维选择空间是 WireCraft 最有价值的工程设计。

### 关键创新点 3:统一 Sim + Real Schema

完全兼容 **LeRobot**(业界最常用的机器人数据 schema),包含:
- **状态**:7-DoF 关节位姿
- **动作**:7-DoF 关节目标
- **视觉**:腕部 + 第三人称 RGB 同步
- **语言**:自然语言指令

**好处**:sim 训出来的策略可以**直接**用 LeRobot 工具链在 UR5 真实环境部署,无需重新对齐数据格式。

### 训练 / 评估流程

1. **Sim 训练**:在 WireCraft sim 中用 PPO / SACfD / ACT 训策略
2. **Sim 评测**:在 WireCraft sim 中按"shared metrics"(成功率、路径长度、接触力)评估
3. **Real 验证**:把 sim 训好的策略零样本部署到 UR5(或 fine-tune on real)
4. **跨平台比较**:不同论文用同一基准,横向比较

### 与已有方法的本质区别

| 基准 | 任务族 | 物理模型 | 真实硬件 | 行业相关性 |
|---|---|---|---|---|
| SoftGym | 通用 deformable | 连续 | 无 | 低 |
| DiPCo | 线缆 | 连续 | 无 | 中 |
| Factory | 工业 | 混合 | 无 | 中(但任务泛) |
| ManiSkill | 通用 manipulation | 刚体为主 | 无 | 中 |
| **WireCraft** | **工业 DLO 三件套** | **铰接 + 连续** | **UR5** | **高(3C / 汽车 / 航空)** |

## 核心公式提取

> 基于 HTML 全文整理

**Privileged PPO 的 reach → insert 成功概率分解**:

$$
P(\text{task success}) = P(\text{reach}) \cdot P(\text{insert} \mid \text{reach})
$$

- 任务成功 = 必须先 reach(到达插座)再 insert(接触丰富插接)
- 这个分解揭示了 WireCraft 论文的关键诊断:**vision policy 卡在 reach 阶段**,而非 insert 阶段

**铰接链 DLO 状态(简化)**:

$$
q_t = (p_0, p_1, \ldots, p_N) \in \mathbb{R}^{3 \times (N+1)}
$$

- $q_t$ —— 整条 DLO 的状态(N+1 个 3D 关节位置)
- N —— 链节数(典型 30-50)
- 对比刚体 $q_t \in \mathbb{R}^6$,DLO 状态空间大 **5-15 倍**

**变形 DLO 状态(更复杂)**:

$$
q_t = \phi(x, t), \quad x \in [0, L], \quad \phi \in \mathbb{R}^3
$$

- 状态是一个连续函数(沿弧长 x 的位置)
- **无限维** → 仿真要用 FEM(有限元)或 PBD(Position-Based Dynamics)
- **无解析解**,只能用数值积分

## 关键成果与贡献

### Connector Insertion(3mm 间隙,deformable 线缆)

| 方法 | 圆柱 | 立方体 | Ethernet | DisplayPort | USB-A |
|---|---:|---:|---:|---:|---:|
| **State PPO(特权信息)** | 93.75±1.25% | 95.00±3.75% | 95.86±1.93% | 92.92±3.15% | n/a |
| SACfD(特权 SAC) | 85.55±8.68% | 93.06±6.46% | 92.40±5.91% | 77.43±6.17% | n/a |
| **Vision PPO(仅视觉)** | 41.49±1.32% | 6.25±3.31% | 17.74±1.21% | 3.32±1.45% | n/a |

### Reach / Insert 拆解(Ethernet 任务,Figure 4)

| 方法 | Reach SR | Insert SR | 任务 SR |
|---|---:|---:|---:|
| Privileged PPO | ~99% | ~95% | ~95% |
| SACfD | ~99% | ~92% | ~92% |
| Vision PPO | ~52% | ~33% | ~17% |
| π0.5 | ~6% | ~0% | ~0% |

**核心诊断**:
- Privileged → task 95%,**任务设计良好**(well-posed)
- Vision PPO → task 17%,**主要死在 reach 阶段**(51.6% reach)
- π0.5 → task ~0%,**VLA 现阶段完全无法处理 DLO 工业任务**

### 其他任务族结果(State PPO)

| 任务 | 成功率 |
|---|---:|
| 1-clip routing | 95.32±0.93% |
| 3-clip routing(估计) | < 95%(任务更难) |
| 直线 channel seating | 82.33±0.31% |
| 弯曲 channel seating(±20°) | 待补充 |

### 真实 UR5 实验(Ethernet 插接,ACT,10 次)

| 数据组合 | Reach | Insert |
|---|---:|---:|
| R(实) | 0/10 | 0/10 |
| S(sim) | 0/10 | 0/10 |
| P(sim privileged) | 0/10 | 0/10 |
| R + S | **5/10** | **4/10** |
| R + S + P | 4/10 | 1/10 |

**最关键的发现**:
- **任何单一数据源(R/S/P)零样本 sim2real 都失败** — Sim2Real gap 极大
- **R + S 混合最有效** — 真实 + 仿真协同,真实数据提供动力学、仿真提供多样性
- **R + S + P 反不如 R + S** — Privileged 信息反而有害(可能因为 sim privileged 与 real sensor 分布差异)

### 计算扩展性(RTX A4000)

| DLO 模型 | 最大并行环境数 |
|---|---:|
| Articulated | 8,192 ✓ |
| Deformable | 2,048 ✓(4,096 失败) |

## 局限性与未来展望

### 论文自述局限(从 HTML 全文整理)

1. **VLA 表现灾难性** — π0.5 在 Ethernet 任务 0% 成功率。论文没有解释为什么 VLA 完全失败(可能是训练数据没覆盖 DLO、动作空间不匹配、视觉编码器对细线不敏感)
2. **Sim2Real gap 巨大** — 真实部署从 sim 100% → 真实 40%。**工业级 sim2real 仍是大挑战**
3. **Privileged 信息是 hack** — 现实中没有"完美状态",benchmark 用它只是验证任务 well-posed
4. **单平台(UR5)** — 没有在双臂、人形上验证
5. **只测了插接** — channel seating 的真实部署未做
6. **Deformable 仿真慢** — 2K 并行是天花板,大规模 RL 训练受限

### 我们发现的潜在问题

1. **基线不完整**:
   - 没有测 OpenVLA、Octo、RDT-1B、GR-2(只测了 π0.5)
   - 没有测带力矩/触觉的 VLA
   - 没有测模仿学习(只有 ACT 训 40k step,数据量太小)
2. **真实数据规模小** — 10 次 rollout 算 95% 置信区间很宽,**应做 30-50 次**
3. **奖励函数未公开** — State PPO 95% 是因为 sim 奖励 + privileged 信息,不能直接迁移到真实
4. **task diversity 限制** — 5 种插接器、3 种 clip 数量、5 段 channel,工业线缆类型远不止这些

### 未来方向

- **VLA + 力矩 / 触觉** — WireCraft 是 VLA 失败的硬骨头,需要新方法
- **跨平台 DLO 基准** — 推广到双臂、人形、线外
- **真实世界 RL** — 直接在真实 UR5 上 fine-tune(sim 启航 + real fine-tune)
- **DLO foundation model** — 一个模型覆盖所有 3 任务族
- **DLO 数字孪生** — 用 NeRF / 3DGS 实时重建 DLO 形状

## 复现线索

- **代码 / 基准**:**未开源**(作者承诺"upon acceptance"开源)
- **数据**:
  - Sim 数据:作者在 benchmark 内自动生成
  - Real 数据:UR5 + LeRobot schema,估计几百条 demo
- **硬件**:
  - **训练**:RTX A4000(论文实测),A100/H100 也可以
  - **部署**:UR5 + Realsense 腕部相机 + 第三人称 RGB
- **依赖**:Isaac Sim / MuJoCo(物理 sim) + LeRobot(数据 schema) + ROS 2
- **复现难度评估**:**中**
  - 利好:论文详尽、数据格式标准、UR5 通用
  - 卡点:benchmark 未开源、deformable 仿真慢、UR5 + 多相机 + 力矩需要数万到十万元设备

## 应用与行业映射(本项目强制要求)

### 1. 应用方向

- **3C 电子装配**:手机排线、笔记本铰链线缆、显示器接插
- **汽车制造**:线束装配(动力 + 信号 + 通信)、传感器布线
- **航空航天**:航电系统布线、卫星太阳能板线缆
- **数据中心**:服务器机柜内部线缆、交换机堆叠
- **医疗设备**:内窥镜线缆、手术机器人
- **家电**:洗衣机、空调、冰箱内部走线
- **物流仓储**:线缆类 SKU 的拣选和包装

### 2. 行业玩家

| 公司 | 主营业务 | 部署状态 |
|---|---|---|
| **MUJIN**(日本) | 工业 3D 视觉 + 路径规划,擅长线缆 | 已有线缆 demo |
| **Plus One Robotics** | 仓储 + 物流,通用机械臂 | 主要刚体 |
| **Covariant / Cohere?** | 通用 manipulation | 通用 |
| **国内:节卡机器人** | 协作臂 | 已有汽车线束 demo |
| **国内:越疆科技(Dobot)** | 协作臂 | 部分线缆 |
| **国内:非夕科技(Flexiv)** | 复合机器人 | 已有线缆 demo |
| **国内:大族机器人** | 协作臂 | 部分线缆 |
| **国外:Universal Robots(UR5 母公司)** | 协作臂 | WireCraft 用了 UR5 |

### 3. 替代方案

| 方案 | 适用 | 成本 | 灵活度 | 成功率 |
|---|---|---|---|---|
| 人工 | 全场景 | 极高(人力) | 高 | 99% |
| 专用治具 + 人工引导 | 大批量同款 | 中(治具) | 低 | 90% |
| 纯刚体 RL/IL(VLA) | 刚体件 | 中 | 高(已成熟) | 80-95% |
| **DLO 专用 sim 训练 + sim2real** | **DLO 类** | **中** | **中** | **< 50%(WireCraft 实测)** |
| 强示教 + 简单 RL | 单任务 | 高(示教) | 低 | 70-85% |

### 4. 量产壁垒

- **Sim2Real 真实差距**:**最大卡点**,WireCraft 实测 sim→real 掉 50%+ 性能
- **DLO 仿真物理参数标定** — 不同材质(铜、铝、光纤、橡胶)需要不同摩擦/硬度参数,标定工作量大
- **DLO 视觉感知** — 细线在低对比场景下分割困难,需要专门视觉模型
- **触觉 / 力矩融合** — DLO 操控对力反馈极敏感,目前 VLA 不擅长
- **多品种小批量** — 工业实际每批线缆规格不同,基准再通用也不能穷举
- **VLA 灾难性失败** — π0.5 在 WireCraft 上 0% 成功率,**说明当前 SOTA VLA 完全不适合 DLO 工业**
- **认证 / 安全** — 工业装配对可靠性要求 99.9%+,目前 DLO 操控还差几个数量级

### 5. 时间窗估计

- **1 年内(2026)**:
  - 实验室演示级 sim2real(< 5 种线缆)
  - 3C 大厂(苹果、华为)内部 R&D 项目
  - WireCraft 基准成为标准对照工具
- **3 年内(2028)**:
  - **汽车线束**率先量产(标准化、量最大)
  - 单任务 DLO 操控产线部署
  - VLA + 力矩的初版可能解决 50-70% DLO 任务
- **5 年内(2030)**:
  - **3C 电子装配**广泛部署(线缆成本占比高、人力贵)
  - 通用 DLO 操控成为具身智能的"奥赛题"
  - WireCraft / 后续基准成为行业入门门槛

## 横向对比

| 基准 | 任务族 | 物理 | 真实硬件 | 行业相关性 | 维护者 |
|---|---|---|---|---|---|
| SoftGym | 通用 deformable | 连续 | 无 | 低 | Berkeley |
| DiPCo | 线缆插接 | 连续 | 无 | 中 | Berkeley |
| ManiSkill | 通用 manip | 刚体为主 | 无 | 中 | UCSD |
| Factory | 工业 | 混合 | 无 | 中 | Stanford |
| **WireCraft** | **3 工业 DLO** | **铰接 + 连续** | **UR5** | **高(3C/汽车)** | **UofT + CREFLE** |

| 策略类型 | Reach | Insert | 适用 |
|---|---:|---:|---|
| Privileged PPO | ~99% | ~95% | 仅 sim benchmark(upper bound) |
| Vision PPO | ~52% | ~33% | sim 训练,real 失败 |
| ACT(IL, real 40k) | 0-50% | 0-40% | 真实小数据 |
| **π0.5 VLA** | **~6%** | **~0%** | **完全失败** |

## 概念关联

- [[DLO 操控]]:DLO = 无限维状态空间的子领域
- [[Sim2Real]]:WireCraft 是 sim2real 差距的"压力测试"
- [[LeRobot schema]]:工业数据标准的代表
- [[VLA 局限]]:π0.5 在 WireCraft 0% 提示 VLA 通用性边界
- [[工业装配]]:三大应用方向(3C、汽车、航空)都是高价值场景
- [[UR5 平台]]:协作臂的事实标准

## 引用 & 链接

- arXiv:[2606.18097v1](https://arxiv.org/abs/2606.18097v1)
- HTML 全文:[arxiv.org/html/2606.18097](https://arxiv.org/html/2606.18097)
- 论文 PDF:[arxiv.org/pdf/2606.18097v1](https://arxiv.org/pdf/2606.18097v1)
- 通讯作者:cyzhu@mie.utoronto.ca
- 合作机构:University of Toronto + CREFLE Inc.
