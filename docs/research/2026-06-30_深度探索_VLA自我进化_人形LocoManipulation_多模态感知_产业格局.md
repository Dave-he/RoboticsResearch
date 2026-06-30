# 2026 年机器人研究前沿深度探索:VLA 自我进化 · 人形 Loco-Manipulation · 多模态感知 · 产业格局

*生成日期: 2026-06-30 | 来源数: 20+ | 置信度: 高*

## 执行摘要

2026 年上半年,机器人学研究在四个方向上出现重大突破:(1) VLA 模型的测试时自我改进从概念走向多路线并行发展,以 T2VLA、TT-VLA、RISE 为代表;(2) 人形机器人 loco-manipulation 系统从单一平台验证迈向跨平台通用化,Calvert 博士论文在 6 种机器人上部署、WholeBodyVLA 统一潜在空间框架;(3) 多模态感知 VLA 从 RGB-only 扩展到 IR/雷达/声学等异构传感器融合,MuseVLA 和 OmniVLA 代表两种技术路线;(4) 全球人形机器人产业进入量产验证期,2025 年出货约 18000 台、市场规模约 $440M,中国占据 85% 产量份额。

---

## 1. VLA 测试时自我进化:从外部奖励到内部置信度

### 1.1 研究趋势概览

ICLR 2026 收到 **164 篇 VLA 相关论文**,较 ICLR 2025 的 9 篇增长 18 倍,预计 ICLR 2027 将突破 1000 篇。其中 RL for VLAs 被列为七大趋势之一,测试时 RL(test-time RL)是增长最快的细分方向。

当前的 VLA RL 方法可分为三大范式:

| 范式 | 代表方法 | 奖励来源 | 环境交互 | 核心优势 |
|---|---|---|---|---|
| 在线 RL | VLA-RL, RobustVLA | 外部环境 | 是 | 接近 oracle 性能 |
| 离线 RL | ActionX, BORA | 预训练数据 | 否 | 无需在线交互 |
| **测试时 RL** | **T2VLA, TT-VLA, RISE** | **内部信号/世界模型** | **否或想象空间** | **部署后持续改进** |

### 1.2 T2VLA:置信度驱动的自我引导(本项目研读论文)

T2VLA (arXiv: 2606.29892) 的核心发现是:**离散动作 VLA 的生成置信度与任务成功正相关**。基于此,论文提出:
- 利用轨迹与高置信度专家演示的相似度作为内在奖励
- 双专家引导机制(Local Pseudo-Expert + Global Expert Pool)平衡探索与稳定性
- 在 LIBERO 和 RoboTwin 上接近 Oracle RL 性能
- 架构无关:在 OpenVLA-OFT 和 pi 系列上均有效

### 1.3 TT-VLA:密集逐步奖励信号(前驱工作)

TT-VLA (arXiv: 2601.06748, 2026年1月)是测试时 RL 的先行者,采用**环境衍生的密集逐步任务进度信号**作为奖励:
- 与 T2VLA 的区别:TT-VLA 依赖环境信号(任务进度代理),T2VLA 完全依赖模型内部置信度
- TT-VLA 保留了 SFT/RL 训练的先验,作为补充而非替代
- 在仿真和真实机器人上均验证有效性

### 1.4 RISE:基于世界模型的想象空间自我改进(RSS 2026)

RISE (arXiv: 2602.11075, RSS 2026) 提出了**完全不同的路线**:通过组合式世界模型在想象空间中自我改进,无需物理交互:
- 组合式世界模型 = 可控动力学模型(预测多视角未来) + 进度价值模型(评估想象结果)
- 闭环自我改进:想象 rollout -> 估计优势 -> 更新策略,全部在想象空间完成
- 三个真实世界任务:动态砖块分拣(+35%)、背包打包(+45%)、箱子封口(+35%)
- **开源**: [GitHub](https://github.com/OpenDriveLab/RISE)

### 1.5 三种路线对比

| 方法 | 奖励来源 | 需要环境 | 需要世界模型 | 安全性 | 性能提升 |
|---|---|---|---|---|---|
| TT-VLA | 环境进度代理 | 是 | 否 | 中 | 显著 |
| T2VLA | 模型内部置信度 | **否** | 否 | 高 | 接近 Oracle |
| RISE | 想象空间价值估计 | **否** | **是** | **最高** | +35-45% |

**关键洞察**:测试时 RL 正在从"需要环境反馈"向"完全自我引导"演进,T2VLA 代表了去外部依赖的极端,RISE 代表了通过世界模型实现安全想象空间的路线。

---

## 2. 人形 Loco-Manipulation 系统:从单一平台到跨平台通用化

### 2.1 当前格局

2026 年人形 loco-manipulation 研究呈现两条技术路线并行发展的态势:

**路线 A:结构化行为系统(Calvert 论文)**
- 代表:Calvert 博士论文(arXiv: 2606.26425),UWF/IHMC
- 核心思想:Coactive Design + Behavior Trees + Affordance Templates
- 部署平台:6 种人形机器人(DRC Atlas, Valkyrie, Nadia, H1-2, Alex 等)
- 行为库:20+ 任务变体,分钟到小时级适配
- 特点:可解释、可在线修复,但依赖操作员协作

**路线 B:端到端学习型 VLA**
- 代表:WholeBodyVLA(ICLR 2026),CoorDex,HumanoidUMI
- 核心思想:统一潜在动作空间,从无动作示教中学习全身协调
- 特点:数据驱动、可泛化,但可解释性弱

### 2.2 WholeBodyVLA:统一潜在空间框架(ICLR 2026)

WholeBodyVLA 来自 OpenDriveLab(ICLR 2026),提出统一的 Vision-Language-Action 框架:
- 面向大空间人形 loco-manipulation
- 从无动作(action-free)的示教数据中学习统一的潜在动作
- 解决跨形态迁移问题:不同机器人的动作空间差异通过潜在空间统一

### 2.3 Expert-Guided Imitation:专家引导的 loco-manipulation

AIST 的研究(arXiv: 2026, IEEE/ICRA 2026)提出专家引导模仿学习:
- 通过 BC(Behavior Cloning)目标实现腿部运动约束
- 确保运动符合人形机器人的动力学和运动学约束
- 在真实人形机器人上验证

### 2.4 HWC-Loco:分层全身控制

HWC-Loco(OpenReview, 被引 5 次)提出分层全身控制算法:
- 专门针对人形运动任务设计
- 已在 Unitree 平台上部署验证

### 2.5 ICRA 2026 安全全身 Loco-Manipulation

Mitsubishi Electric Research Labs (MERL) 在 ICRA 2026 发表安全全身 loco-manipulation 论文,强调:
- 在执行 loco-manipulation 时的安全约束
- 面向工业应用的安全保障

**关键洞察**:Calvert 的结构化系统路线和 VLA 端到端路线正在**走向融合**。Calvert 论文本身指出,未来方向是将行为模板与学习方法结合,而 VLA 研究者也开始意识到需要结构化的执行层来保障安全。

---

## 3. 多模态感知 VLA:从 RGB-only 到异构传感器融合

### 3.1 两条技术路线

2026 年多模态 VLA 出现两种代表性方案:

| 方面 | MuseVLA (本项目研读) | OmniVLA |
|---|---|---|
| arXiv | 2606.17598 (2026-06) | 2511.01210 (2025-11, v3 2026-03) |
| 核心思想 | 传感器作为**工具调用**(tool call) | 传感器数据**空间叠加**(sensor-masked image) |
| 传感器类型 | 温度/麦克风/雷达(按需调用) | IR/mmWave 雷达/麦克风阵列(并行融合) |
| 统一表示 | grounded sensor image | sensor-masked image |
| 架构 | VLA backbone + sensor token | 冻结视觉编码器 + per-sensor 投影层 + LLM + diffusion 动作专家 |
| 数据策略 | 合成增广(物理模型生成 grounded image) | Grounded SAM 语义分割 + 传感器叠加 |
| 平均成功率 | 80.6% | 84% |
| RGB-only 基线 | 显著超越 | 25% -> 84%(+59%) |
| 开源 | 未提及 | **是** (CC BY-SA 4.0) |

### 3.2 技术路线对比分析

**MuseVLA 优势**:
- 工具调用范式更灵活,传感器按需激活,降低延迟和硬件成本
- 合成增广 pipeline 减少对真实多模态数据集的依赖
- 新增传感器只需扩充 token 词表,backbone 不需要重新训练

**OmniVLA 优势**:
- 开源,可复现
- 传感器并行融合,适合多传感器同时需要的场景
- 数据效率高:仅用 50% 训练数据即可达到 raw-sensor 基线的全部性能
- 在三个未见任务上泛化性验证更充分(+59% / +28%)

### 3.3 触觉/力觉 VLA 趋势

GitHub 上的 [Awesome-Force-Tactile-VLA](https://github.com/OpenHelix-Team/Awesome-Force-Tactile-VLA) 论文列表显示,力觉/触觉 VLA 正在成为独立子领域:
- ForceVLA:增强 VLA 模型的力觉感知
- Tactile-Force Alignment:触觉-力觉对齐在 VLA 中的应用
- 与 MuseVLA/OmniVLA 的差异:触觉/力觉更关注**接触动力学**,而 MuseVLA/OmniVLA 更关注**环境感知**

### 3.4 多模态融合综述(2026)

Elsevier 综述论文(Multimodal fusion with VLA models for robotic manipulation)系统梳理了多模态 VLA 融合策略:
- **融合不仅仅是"一起使用多个传感器"**:需要架构级的设计
- 早期融合 vs 晚期融合 vs 中间融合各有适用场景
- 关键挑战:异构传感器的时间对齐、空间标定、数据稀缺

**关键洞察**:MuseVLA 的"工具调用"范式和 OmniVLA 的"空间叠加"范式代表了两条互补路线。工具调用适合**稀疏按需感知**(如偶尔需要温度检测),空间叠加适合**持续多模态监控**(如同时需要视觉+雷达+声学)。未来可能融合:用工具调用决定"何时用哪种传感器",用空间叠加决定"如何融合数据"。

---

## 4. 全球人形机器人产业格局:量产验证期

### 4.1 市场规模与出货量

| 指标 | 2025 年 | 2026 年(预测) | 来源 |
|---|---|---|---|
| 全球出货量 | ~18,000 台 | ~28,000 台(中国)/ 全球更高 | IDC, Morgan Stanley |
| 市场规模 | ~$440M | - | IDC |
| 全球机器人市场(含工业) | - | $38B (+34% YoY) | Robotics Center |
| 风险投资 | $9.4B (2025, +41% YoY) | - | Robotics Center |
| 商业人形平台数 | 3 (2024) -> 12 (2026) | - | Robotics Center |
| 价格区间 | - | $28K (躯干) - $245K (全身) | Robotics Center |

### 4.2 中国:全球制造中心

来自 Fortune 杂志(2026年6月)和 Morgan Stanley 的关键发现:

- **中国占全球人形机器人产量 85%**(2025,Barclays 数据)
- 超过 **140 家中国制造商**和 **330 种机型**(工信部 2025)
- 龙头企业:
  - **AGIBOT(智元)** 和 **Unitree(宇树)** 各出货超 5,000 台(2025)
  - **Matrix Robotics(上海)**:MATRIX-3,~$99,000/台,已获约 1,000 台咖啡连锁和酒店订单
  - **EngineAI(深圳)**:全身人形约 $26,600(基础版)
  - **RoboScience**:前苹果工程师叶田创立,专注 AI 系统
- 成本优势:中国制造的机器人比外国品牌**便宜 20%+**(Morgan Stanley)
- Unitree 2025 年营收 17 亿元(~$250M),利润 2.78 亿元(~$41M),**已实现盈利**
- 政府"十四五"规划(2026-2030)将人形机器人列为前沿技术重点
- 2025 年来自国企订单超 20 亿元(~$295M),主要用于电站、数据中心、娱乐

### 4.3 美国:AI 大脑优势

- **Figure AI**:Figure 03 机器人,40 台车队已部署
- **Tesla Optimus**:Gen 3,目标 2026 年产 5-10 万台(Musk 表态)
- **Boston Dynamics**:Atlas 系列持续迭代
- 美国在 AI"大脑"和高层计算能力方面保持优势
- 在出货量上:Figure 和 Tesla 2025 年各仅"数百台"

### 4.4 量产成本结构

来自多个来源的成本数据:

| 机器人型号/类型 | 价格 | 来源 |
|---|---|---|
| Unitree G1 (Amazon) | $17,990 | Lumichats |
| Unitree R1 | ~$5,500 | Recorded Future |
| EngineAI 全身基础版 | ~$26,600 | Fortune |
| Matrix Robotics MATRIX-3 | ~$99,000 | Fortune |
| 企业级人形 | $100K-$320K | Robozaps |
| 全球均价(2025) | ~$46,000 | Fortune/Morgan Stanley |
| 预测均价(2050) | ~$21,000 | Fortune/Morgan Stanley |

**成本下降趋势**:2025->2026 制造成本持续下降,驱动力为:
1. 本地化零部件(中国供应商降低 BOM 20%+)
2. 产量爬坡带来规模效应
3. 关键零部件(伺服电机、减速器、力矩传感器)国产替代

### 4.5 部署行业分布

Robotics Center 2026 报告的行业部署量:

| 行业 | 部署量(台) | 增长率 |
|---|---|---|
| 物流/仓储 | 41,000 | - |
| 半导体制造 | 22,500 | - |
| 餐饮服务 | 8,200 | +61% YoY(增长最快) |
| **以上三个占全部商业部署的 64%** | | |

**关键洞察**:2026 年是人形机器人从"量产元年"(2025)进入"规模化验证期"的关键节点。中国凭借制造成本优势和供应链密度占据出货量主导,但美国在 AI"大脑"(VLA 模型)方面领先。**真正的瓶颈不在产能,而在需求端**——"没有需求和市场规模化,这些公司无法真正进入量产"(风投 Chibo Tang)。

---

## 5. VLA 研究的 Benchmark 现实

### 5.1 ICLR 2026 的 Benchmark 警示

ICLR 2026 的 VLA 综述分析揭示了一个**严峻的 benchmark 现实**:

| Benchmark | 状态 | 含义 |
|---|---|---|
| LIBERO | "基本已解决"(95-98%) | 无法区分模型优劣 |
| CALVIN | "接近饱和"(ABC >4, D >3.75) | 接近天花板 |
| SIMPLER | 40-99% 跨论文差异大 | "跨论文比较噪声大" |
| RLBench | VLA 远不如 3D SOTA | "大多数 VLA 回避与 3D 基线比较" |

### 5.2 "前沿差距"

ICLR 2026 综述作者指出:
- **"大多数 VLA 在零样本泛化上仍然困难"**
- 大型 VLA(7B+ 参数)"非常擅长在 benchmark 上过拟合"
- **"sim-only 结果难以信任"**——真实世界验证是必需的
- 存在**前沿实验室与学术实验室之间的"隐藏差距"**——仅读论文看不到

### 5.3 对本项目的启示

1. **关注真实世界验证**:本项目的研读报告应优先选择有真机实验的论文
2. **Benchmark 数字需谨慎**:LIBERO 95%+ 不再是区分度指标
3. **跟踪前沿实验室**:PI、Google DeepMind、Figure AI 等的内部进展可能领先公开论文 6-12 个月

---

## 6. 关键发现与项目建议

### 6.1 技术融合趋势

2026 年上半年的研究呈现三条融合轴线:

1. **VLA 决策 + 结构化执行**:T2VLA/MuseVLA 负责"做什么",Calvert 系统负责"怎么做"
2. **多模态感知 + 自我改进**:MuseVLA 的传感器置信度可增强 T2VLA 的自我评估准确性
3. **想象空间 + 真实部署**:RISE 的世界模型想象 + Calvert 的真机执行 = 安全的闭环自我改进

### 6.2 对本项目的具体建议

1. **关键词迭代**:在 `configs/keywords.yaml` 中新增:
   - `test-time RL`, `self-bootstrapping`, `world model imagination`
   - `WholeBodyVLA`, `OmniVLA`, `sensor-masked image`
   - `tool call VLA`, `grounded sensor image`

2. **研读报告优先级调整**:
   - 优先选择有**真实机器人实验**的论文
   - 对 LIBERO-only 的论文降低优先级(benchmark 饱和)
   - 关注 RLBench 和 RoboTwin 上的表现

3. **行业映射更新**:
   - 新增:AGIBOT(智元)、Matrix Robotics、EngineAI、RoboScience
   - 更新成本量级:Unitree G1 已降至 $17,990;中国制造均价比外国低 20%+
   - 新增部署行业:餐饮服务(+61% YoY)是增长最快的意外赛道

4. **概念笔记扩展**:
   - `test_time_rl.md` — 三种路线对比(T2VLA/TT-VLA/RISE)
   - `multimodal_vla_paradigms.md` — 工具调用 vs 空间叠加
   - `humanoid_production_economics.md` — 量产成本与供应链

---

## 来源

1. [State of VLA Research at ICLR 2026](https://mbreuss.github.io/blog_post_iclr_26_vla.html) — 164 篇 VLA 论文综合分析,七大趋势
2. [State of Robotics 2026 Report](https://www.roboticscenter.ai/state-of-robotics-2026) — $38B 市场,12 种商业人形平台
3. [T2VLA: Confidence-Driven Test-Time RL](https://arxiv.org/abs/2606.29892v1) — 本项目研读论文
4. [TT-VLA: On-the-Fly VLA Adaptation](https://arxiv.org/html/2601.06748v2) — 测试时 RL 前驱工作
5. [RISE: Self-Improving Robot Policy](https://arxiv.org/abs/2602.11075) — RSS 2026,组合式世界模型
6. [Calvert: Loco-Manipulation Behavior System](https://arxiv.org/abs/2606.26425) — 本项目研读论文
7. [WholeBodyVLA](https://github.com/OpenDriveLab/WholebodyVLA) — ICLR 2026,统一潜在空间
8. [OmniVLA: Physically-Grounded Multimodal VLA](https://arxiv.org/html/2511.01210v3) — 多模态传感器融合,84% 成功率
9. [MuseVLA](https://arxiv.org/abs/2606.17598) — 本项目研读论文,工具调用范式
10. [China builds 85% of world's humanoids](https://fortune.com/2026/06/09/china-builds-85-percent-worlds-humanoids-robots-cheap/) — 中国人形机器人产业分析
11. [Humanoid Robot Market Size $38B by 2035](https://blog.robozaps.com/b/market-size-for-humanoid-robots) — 市场规模预测
12. [Awesome RL-VLA](https://github.com/Denghaoyuan123/Awesome-RL-VLA) — VLA RL 论文列表
13. [Awesome VLA-WAM](https://github.com/DravenALG/awesome-vla-wam) — VLA 与世界动作模型综合列表
14. [Expert-Guided Imitation for Humanoid Loco-Manipulation](https://ieeexplore.ieee.org/document/11404507/) — ICRA 2026
15. [HWC-Loco: Hierarchical Whole-Body Control](https://openreview.net/forum?id=3UE3Aatcjy) — 分层全身控制
16. [ICRA 2026 Safe Whole-Body Loco-Manipulation](https://www.youtube.com/watch?v=3HwqI6DK-7k) — MERL 安全约束
17. [Multimodal fusion with VLA models](https://www.sciencedirect.com/science/article/pii/S1566253525011248) — Elsevier 综述
18. [Awesome Force-Tactile-VLA](https://github.com/OpenHelix-Team/Awesome-Force-Tactile-VLA) — 触觉/力觉 VLA 论文列表
19. [VLA Survey](https://vla-survey.github.io/) — VLA 综述论文
20. [2026 Humanoid Robot Industry Outlook](https://en.eeworld.com.cn/news/robot/eic717058.html) — 10 万级量产将至
21. [中国人形机器人产业格局](https://finance.sina.com.cn/stock/relnews/cn/2026-02-09/doc-inhmfcpk2210749.shtml) — 2025 量产元年分析
22. [国产化率超 90%](https://t.qianzhan.com/caijing/detail/260129-21db9065.html) — 中国人形机器人产业链分析

## 方法论

搜索了 16 个查询(Google Search),覆盖 4 个子主题。深度阅读了 8 个关键来源(T2VLA 论文页、TT-VLA 论文、RISE 论文、OmniVLA 论文、ICLR 2026 VLA 综述、Robotics Center 2026 报告、Fortune 中国人形机器人报道、WholeBodyVLA GitHub)。

子问题:
1. VLA 测试时自我改进的最新进展(2026)
2. 人形 loco-manipulation 系统的前沿方法
3. 多模态感知 VLA 的产业落地路线
4. 2026 年人形机器人竞争格局与产业链
