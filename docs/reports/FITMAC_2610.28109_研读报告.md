---
title: FIT-MAC 多智能体闭环鲁棒 VLA 框架_研读报告
arxiv_id: "2610.28109"
date: 2026-10-22
subarea: vla
tags: [robotics, vla, multi-agent, robustness, perturbation, closed-loop, llm-agent, manipulation]
---

# FIT-MAC: A Closed-Loop Multi-Agent Framework for Robust Vision-Language-Action Models

> **作者**:Jiatong Li¹, Jisheng Dang¹, Qiangqiang Ma², Bimei Wang¹, Jingwen Zhao³, Wenjun Ma¹, Juncheng Li⁴, Hong Peng¹, Bin Hu⁵
> **机构**(**全文首页脚注原文照录**):**1** Lanzhou University(兰州大学) · **2** Northwest Normal University(西北师范大学) · **3** Sun Yat-sen University(中山大学) · **4** Zhejiang University(浙江大学) · **5** Beijing Institute of Technology(北京理工大学)。**共 5 家单位,署名结构为「兰大 4 人 + 西师大 1 + 中大 1 + 浙大 1 + 北理工 1」** —— 以高校联合体为主,⚠️ **全文未见任何企业署名**。
> **发表**:2026-10-20 · arXiv: 2610.28109v1 · cs.RO · License: arXiv.org perpetual non-exclusive license
> **会议 / 期刊**:⚠️ **论文正文未标注**(无投稿声明、无 camera-ready 标记、参考文献为 ACL/NAACL 风格但无投稿线索)。**本报告不推断。**
> **页数 / 篇幅**:⚠️ **论文正文未标注页码**(arXiv HTML 版无页码)。可核查的规模指标:**正文 5 章 + 附录 A/B/C 三部分,含 7 图、19 表**;附录含 2 张跨骨干完整表(5、6)、2 张多 seed 表(7、8)、2 张逐扰动消融表(9、10)、8 张超参敏感性表(11–18)、1 张运行时 trace 表(19)。
> **代码可得性**:🟡 **有项目页 + 有匿名 artifact 链接,但无公开仓库**。原文脚注给出:项目页 `https://fitmac-research.pages.dev/`;代码 `https://anonymous.4open.science/r/research-artifact-B431`。⚠️ 后者是 **anonymous.4open.science 匿名评审工件链接**(匿名投稿专用的临时托管),**不是 GitHub 仓库**,本报告**未联网核验其内容**(按任务约束不联网),因此按本项目 §11.2 口径属「**仅承诺发布 + 匿名链接不可核验**」档,不能按「有仓库」计。
> **本报告状态**:✅ **已获取 arXiv HTML 全文纯文本**(`drafts/arxiv_text/2610.28109v1.txt`,**101,490 字节 / 2,876 行**),正文 5 章 + 附录 A/B/C **全部读完**;Table 1–19 数字**逐格提取**;公式 (1)–(11) 全部定位。

---

## 元数据

- **arXiv ID**:[2610.28109v1](https://arxiv.org/abs/2610.28109v1)(注意:本篇 ID 为 `2610.28109v1`,与本项目已收录的 `2610.23438` / `2610.23288` 等同批次)
- **作者**:Jiatong Li, Jisheng Dang, Qiangqiang Ma, Bimei Wang, Jingwen Zhao, Wenjun Ma, Juncheng Li, Hong Peng, Bin Hu
- **机构**:兰州大学 · 西北师范大学 · 中山大学 · 浙江大学 · 北京理工大学
- **发表时间**:2026-10-20
- **会议 / 期刊**:论文正文未标注
- **项目页**:`https://fitmac-research.pages.dev/`(论文脚注给出,本报告未联网核验)
- **代码**:`https://anonymous.4open.science/r/research-artifact-B431`(匿名 artifact,非公开仓库,未核验)
- **PDF**:<https://arxiv.org/pdf/2610.28109v1>
- **代码可得性判定**:🟡 **无公开 GitHub 仓库**;有项目页 + 匿名 artifact 链接。按本项目 §11.2 的三档口径 → **(b) 仅承诺发布**,且其链接形态是匿名工件(评审期托管,通常不长期保留),**实际可用性低于典型「仅承诺发布」**。

### 评测栈与基准设置(全文 §4.1 / 附录 A.1 可考)

| 项 | 值(全部出自全文) |
|---|---|
| 基准 | **LIBERO-Object** + **LIBERO-Spatial**(Liu et al. 2023),遵循 **LIBERO-PRO** 扰动协议(Zhou et al. 2025) |
| 扰动类型 | **5 类**:`Pos`(物体位置)、`Task`(任务指令)、`Env`(环境)、`Obj`(物体同一性)、`Sem`(语义绑定) |
| 扰动强度 | ⚠️ **论文未给出任何强度分级** —— 每类扰动只有 LIBERO-PRO 的单一固定设定,论文未引入强度参数,也未报告扰动幅值 |
| 基座 VLA | **OpenVLA**(Kim et al. 2024)、**π0**(Black et al. 2024)、**π0.5**(Intelligence et al. 2025),**全部冻结,不修改参数** |
| 主实验预算 | **每任务 50 episodes**;消融 **每任务 10 episodes**;多 seed:5 个种子 {7, 11, 13, 17, 23} × 每任务每 seed 10 episodes → **每条件每套件 100 episodes** |
| 任务数 | ⚠️ **论文未给出任务数**。LIBERO-Object / LIBERO-Spatial 标准划分为各 10 任务(属公开信息量级,非论文给出) |
| 指标 | **SR**(成功率)、**IR**(干预率)、**RSR**(被干预回合中的成功率) |
| 感知栈 | **Grounding DINO**(开放词检测)+ **VLM resolver**(候选歧义时) |
| 训练 | **完全免训练** —— 推理期控制层,基座 VLA 冻结 |
| 仿真 / 真机 | ⚠️ **仅 LIBERO 仿真**;**全文无真机实验、无仿真器名称、无硬件平台描述** |

---

## 核心问题

### 1. 失败形态:不是「掉点」,是**归零**

论文的立论起点不是「VLA 精度不够」,而是一个更尖锐的观察:**在扰动下,VLA 不是性能退化,而是整类任务彻底归零。**

Table 1 里 OpenVLA 的原始成绩直接给出了这个形态:

| 基准 | Obj | Pos | Sem | Task | Env |
|---|---:|---:|---:|---:|---:|
| LIBERO-Object | 98.0 | **0.0** | 98.0 | **0.0** | **0.0** |
| LIBERO-Spatial | 97.0 | **0.0** | 77.0 | **0.0** | 89.0 |

**10 个条件里有 5 个是精确的 0.0%**。这与「置信度掉了 10 个点」是完全不同的问题:归零意味着**没有可恢复的中间状态** —— 策略不是做错了,而是从第一步起就走进了另一条与任务无关的轨迹。

### 2. 根因诊断:两类失败被**混成了一种**

论文的关键观察(§1 原文口径)是**「扰动诱发不同的失败类型」**:

- **Target failure(目标绑定错误)**:指令指代的对象或空间关系被错误 grounding —— 策略在**抓之前**就对准了错误的实例。这类失败的表征是 **empty grasp / 抓了错的碗**。
- **Execution failure(局部执行失败)**:目标**识别正确**,但抓取、搬运、放置阶段的局部控制失稳 —— 表征是 **failed lift / unstable release / stalled execution**。

> **为什么这个区分是全部方法论的地基?** 因为两类失败的**恢复动作互斥**:目标绑错的正确恢复是「换绑定」(重跑 grounding),而执行失败的正确恢复是「换控制器」(上局部几何抓放)。**对目标绑定错误做执行重试,等于用错误的绑定再抓一次 —— 必然再错。** 论文附录 B.3 的失败案例正是这个机制的直接证据:*「Completing the grasp therefore does not resolve the upstream grounding error.」*(抓成功了也没解决上游的 grounding 错误)。**这句话是全文最有工程价值的一句。**

### 3. 为什么现有显式检测 / 回退方案不够

论文的表述是:*「Existing VLA policies generally lack an explicit runtime mechanism for distinguishing these failure modes and selecting an appropriate recovery strategy.」* —— **缺的不是「检测」,是「区分 + 路由」**。本报告把它拆成三条(前两条是论文口径的展开,第三条是本报告的读解):

- **置信度阈值 / OOD 检测**只能回答「我现在是不是在分布外」,不能回答「我现在是**抓错了对象**还是**抓滑了**」。前者需要改变**语义绑定**,后者需要改变**控制**;阈值信号对这两者给出的响应是同一个。
- **重试(retry)是无差别动作**,而恢复动作的选择**依赖于失败类型**。在目标绑定错误上重试 = 重复同一个错误绑定(论文 B.3 案例)。
- 🔑 **本报告的读解:多智能体的价值不在「多个 LLM 投票」,而在「把诊断与恢复解耦」**。FIT-MAC 的核心资产是**一个显式的、可检视的失败分类器 + 一张失败类型 → 恢复机制的路由表**,LLM 只是可选的辅助证据源(见下文方法论第 3 节)。**这一点对产业极其重要,后面行业映射会展开。**

### 4. 论文的「感知-动作绑定 / 闭环」视角

FIT-MAC 的核心结构改动是:**把「指令指代 → 视觉实例」这个绑定从动作生成内部外提成一个显式状态对象 $g_t$(grounding record)**,并给它三个新属性:

1. **可写**(target correction 可以改写它,改完后重建 grounded prompt 交给 VLA);
2. **可检视**(Verifier Agent 可以检查它是否与当前观测一致);
3. **可锁存**(target-instance lock 跨 policy query 持久化,避免每步重新 grounding 导致的漂移)。

闭环闭合在 **policy-query 边界**而非每个控制步:每个查询边界上跑一次「监控 → 诊断 → 门控 → 路由」,不需要干预时**原 VLA 仍是默认动作生成器**。**这是一个「监督式闭环」而不是「控制式闭环」** —— 它管的是「该不该继续往这条轨迹走」,不是「这一帧该输出什么」。

> **结论先行的一句话判断**:这篇论文的**工程价值远大于方法论新意**。它没有提出新的 VLA、没有新的训练目标、没有新的损失函数,它的贡献是**把「VLA 跑飞了怎么办」这件事从一个学术空白变成一个可实现的运行时状态机**。而它恰好也是本项目 2026-10-20 收录的 CoEvolve(编排层归基础模型)在**单机器人 VLA 侧**的对应物 —— 两者都在说同一件事:**编排 / 监控层是一个独立于策略的、可以被工程化交付的层。**

---

## 方法论与核心思路

### 3.1 整体架构:四个 agent + 一个共享执行状态

FIT-MAC 在冻结的 VLA $\pi_{\mathrm{VLA}}$ 外挂一层**推理期控制层**(§3.1 原文结构):

```
┌──────────────── 指令 x, 观测 I_t, 低维状态 o_t ────────────────┐
│                                                                │
│  ┌──────────────┐   结构化任务规格    ┌──────────────────┐      │
│  │ Planner Agent│ ─────────────────▶ │  Grounder Agent  │      │
│  │  解析指令     │  (目标/源/目的/     │ Grounding DINO   │      │
│  │  分解子任务   │   空间关系)         │ + VLM resolver   │      │
│  └──────────────┘                    └────────┬─────────┘      │
│                                              │ g_t(grounding record)
│                                              │ 「目标实例锁」
│  ┌───────────────────────────────────────────▼──────────────┐   │
│  │            共享执行状态  S(子任务索引 k_t, 相位 φ_t,      │   │
│  │              诊断历史 H, 纠正状态 R, 动作队列 Q)         │   │
│  └───────────────┬──────────────────────────────▲──────────┘   │
│                  │ 诊断 d_t                     │ 门控 Γ        │
│           ┌──────▼─────────┐         ┌──────────┴──────────┐   │
│           │ Verifier Agent │         │  Correction Agent   │   │
│           │ 相位化进度监控  │ ──────▶ │  路由:重绑定 / 局部 │   │
│           │ target/pick/place│  门控 Γ │  抓放恢复 / 交还   │   │
│           │ 失败分类        │         └──────────┬──────────┘   │
│           └────────────────┘                    │              │
│                                                 ▼              │
│                        ┌──────────────────────────────────┐   │
│                        │  冻结的 π_VLA(默认动作生成器)     │   │
│                        │  A ← π(ℓ, o_t),ℓ = grounded prompt│  │
│                        └──────────────────────────────────┘   │
└────────────────────────────────────────────────────────────────┘
```

**数据流要点(§3.1 + 附录 C.1 Algorithm 1):**

- **Planner Agent**(§3.2):把指令转成结构化任务规格 —— 目标物体、源描述、目的描述、空间关系、参考物体;多步指令组织成**有序子任务序列**。附录 C.3.1 明确:**「保持指令本身的粒度」**,不把简单 pick-and-place 拆成 locate/grasp/move/release 四个子任务;**规则化 planner 提供 fallback,可选的本地语言模型产出同样的结构化接口**。
- **Grounder Agent**(§3.3):每个子任务开始前用 **Grounding DINO** 检出候选目标 / 目的地 / 参考物;**检测不确定或歧义时,由 VLM resolver 选出最匹配任务规格的候选**;选中目标与目的地写入 grounding state $g_t$,并据此构造 grounded prompt $\tilde{x}_{k_t}$ 交给 VLA。**关键设计:几何证据只在语义兼容的候选集内作为 tie-break,不允许几何邻近压过语义兼容。**
- **Verifier Agent**(§3.4):监控目标接近、夹爪闭合、物体-夹爪运动、目的地接近、释放后稳定性;输出**相位化进度指标**与**失败分类 $d_t$**。
- **Correction Agent**(§3.5):按 $d_t$ 路由 —— target failure → 回调 Grounder 重绑定并重建 grounded prompt;execution failure → 保留绑定,调用**有界局部控制器** $\pi_{\mathrm{pick}} / \pi_{\mathrm{place}}$;无异常 → **VLA 继续作为默认动作生成器**。

**执行相位模型**:$k_t$ = 当前子任务索引,$\phi_t$ = 当前操作相位,相位属于 $\Phi_{\mathrm{pick}}$ 或 $\Phi_{\mathrm{place}}$ 两集合之一。**「pick 相位」= 接近 / 抓取 / 抬起;「place 相位」= 搬运 / 放置 / 释放 / 释放后稳定。** 这两套判据的不同,正是后面「相位化阈值」的意义所在。

### 3.2 关键模块 1:失败检测 —— **用几何与运动信号,而不是用 LLM 的「感觉」**

这是全文最值得学的一点,也是最容易被误读的一点。

**检测信号(§3.4 + 附录 C.3.3 原文):**

| 证据类型 | 具体信号 | 用途 |
|---|---|---|
| 目标绑定 | 目标锁置信度 $\kappa_t$、与当前观测的一致性 $\mathrm{Inconsistent}(g_t, I_t)$、**target-probe mismatch**、目标歧义 | 判 target failure |
| 抓取 | 夹爪闭合、物体随夹爪抬起(**object lift**) | 判 pick 是否完成 |
| 进度 | 末端-目标距离 $d_t^{\mathrm{tgt}}$、物体-目的地距离 $d_t^{\mathrm{dst}}$、$\Delta$ 步内的距离缩减与位移量 | 判 stall |
| 放置 | 释放后稳定性、物体-目的地对齐 | 判 place 是否完成 |

**判据(式 2–5):**

$$\chi_t^{\mathrm{prog}}=\begin{cases}\mathbf{1}\!\left[\Delta d_t^{\mathrm{tgt}}>\tau_{\mathrm{tgt}}\ \lor\ \|\Delta p_t^{\mathrm{ee}}\|_2>\tau_{\mathrm{ee}}\right],&\phi_t\in\Phi_{\mathrm{pick}},\\[4pt]\mathbf{1}\!\left[\Delta d_t^{\mathrm{dst}}>\tau_{\mathrm{dst}}\ \lor\ \|\Delta p_t^{\mathrm{obj}}\|_2>\tau_{\mathrm{obj}}\right],&\phi_t\in\Phi_{\mathrm{place}},\end{cases}\qquad
\chi_t^{\mathrm{stall}}=\mathbf{1}\!\left[\sum_{\tau=t-W_{\phi_t}+1}^{t}\chi_\tau^{\mathrm{prog}}=0\right]$$

> **这里有一个非常关键的设计选择,论文写得很轻但含义很重**:进度判据是「**距离缩短**」**或**「有位移」—— 是**几何 + 运动**的确定性信号,**不是**「VLM 觉得画面在动」。
>
> 附录 C.3.3 明确写着:*「An optional language-model assessment supplements the rule-based diagnosis. Its output is normalized, its confidence is clamped, and its evidence is merged with the deterministic checks before intervention gating and correction routing.」* —— **LLM 评估是「补充」,不是「主导」**,且其输出还要被归一化 + 置信度截断(clamp)后再与确定性检查**合并**。
>
> 🔑 **本报告的判断:这实际上把「多智能体系统依赖闭源 LLM」的复现风险,大幅削减了。** 论文标题里的 "Multi-Agent" 在**诊断环节**其实是**规则化的确定性状态机**,LLM 只是在(可选的)证据位上补一刀。**但论文没有说明主表(1–3)跑的是「开 LLM」还是「关 LLM」配置** —— 这是本文最关键的一个未声明项(见「局限性」)。

**自适应干预门(Adaptive Intervention Gate,附录 C.1)—— 第二个被低估的设计:**

> *「Failure detection does not automatically trigger correction.」* —— **检测到失败 ≠ 触发纠正。**

门控还要求:同类失败**连续出现 N 次**(参数 `multi-agent-adaptive-intervention-failures`,默认 **3**;取值 2/3/4)、**足够长的目标高置信观测序列**、以及(对 Obj / Sem / Env 路由)**额外的进度守卫** —— 若 VLA 仍在被识别为「有进展」,则继续执行,除非出现更强的目标绑定错误或局部执行失败证据。

> **这一条是全文对「鲁棒性 = 不扰动正常行为」这个命题最认真的回答。** 论文明确:*「FIT-MAC can record a failure while continuing to monitor the pretrained VLA when the evidence is insufficient to justify correction.」* —— **记录失败但不下手**,这正是它能在 Obj / Sem / Env 上做到 IR 只有 21.2%–50.4% 的机制。

### 3.3 关键模块 2:多智能体之间的通信与仲裁

**必须说清楚:这不是「LLM 之间投票」。** 通信机制是**共享执行状态 + 确定性路由**:

| 通信通道 | 内容 | 载体 |
|---|---|---|
| Planner → Grounder / Verifier / Correction | 结构化任务规格(目标、源、目的、空间关系、参考物、置信度) | **JSON 接口**(附录 C.3.1 明确「Output JSON only」) |
| Grounder → Verifier / Correction | grounding record $g_t$(选中目标、置信度证据、**目标实例锁**、图像位置、目的引用) | 持久化记录 |
| Verifier → Correction | 诊断 $d_t$ + 证据标签 + 门控许可 $\Gamma$ | JSON(附录 C.3.3 的 snapshot 字段共 **19 个**,含 `failure_type` / `reason` / `confidence` / `evidence_tags`) |
| Correction → 全体 | 路由结果(pretrained VLA / target correction / execution correction)+ 落地的纠正动作与状态 | 接口约定 |

**仲裁规则的三层结构(附录 C.1 Algorithm 1 第 18–25 行):**

1. **pending execution correction 优先**(在途的局部恢复有最高路由优先级,不允许被打断);
2. 否则若 $\Gamma.\mathrm{allow\_target\_correction}$ → target correction;
3. 否则若 $\Gamma.\mathrm{allow\_execution\_correction}$ → execution correction;
4. 否则 → base policy(原 VLA)。

**失败类型优先级**(式 6):**target-failure 优先于 pick/place-failure** —— 即使当前相位是 pick 且已检测到 stall,只要目标绑定不可信,先修绑定。**这个顺序是对的**:对一个绑错对象的轨迹做局部抓取恢复,等于把错误的对象抓得更稳。

**⚠️ 一条未声明的信息**:论文**没有说明主结果(表 1–3)所用配置中,Verifier 的「optional language-model assessment」是否启用、Planner 用的是规则 fallback 还是 LLM**。附录 C.3.1 说「a rule-based planner provides a fallback, while an optional local language model produces the same structured interface」——**两句并列,没给主表用的是哪个**。这直接影响 token 成本与延迟的估计,故本报告在「复现线索」中把它列为**未知项**。

### 3.4 关键模块 3:恢复 / 重试策略

**路线 A —— Target correction(重绑定):**
调用 Grounder Agent 重跑检测与匹配 → 更新 $g_t$ → 重建 grounded prompt $\tilde{x}_{k_t}$ → **原 VLA 用修正后的绑定继续动作生成**。
**关键点:「This intervention changes the instance on which the policy acts without modifying the policy itself.」** —— 不改权重、不改架构,只改「策略在看哪个对象」。

**路线 B —— Execution correction(有界局部恢复):**
保留目标锁,调用 $\pi_{\mathrm{pick}}$ 或 $\pi_{\mathrm{place}}$。**阶段专属的 waypoint $p_t^*$**:

| 相位 | waypoint |
|---|---|
| 接近(approach) | **hover 点** |
| 抓取与抬起 | **grounded target** |
| 搬运与放置 | **grounded destination** |
| 释放 | **retreat 点** |

**恢复动作(式 7–8)—— 这一步值得单独看,因为它是整个框架里最「传统机器人学」的部分:**

$$u_t^{\mathrm{rec}}=\operatorname{clip}\!\left((p_t^{*}-p_t^{\mathrm{ee}})\oslash\bm{s},\,-1,\,1\right),\qquad a_t^{\mathrm{rec}}=\left[\left(u_t^{\mathrm{rec}}\right)^{\top},\ \mathbf{0}_{3}^{\top},\ a_t^{\mathrm{grip}}\right]^{\top}$$

$\bm{s}=(s_x,s_y,s_z)$ 是**逐轴位移缩放**(即一个手写的 P 控制器 + 饱和限幅),旋转命令恒为零。**注意 $\mathbf{0}_3$ —— 恢复器完全不做旋转补偿。** 这是一个**姿态无关的直线插值抓放器**。

**恢复器的完整动作序列(附录 C.1):**

- **pick-correction**:接近目标 → 下降 → 闭合夹爪 → **验证物体是否被抬起** → 若抬起验证失败,允许**重开夹爪并再走一次受控下降** → 确认搬运中后移交 place 流程;
- **place-correction**:验证物体被携带 → 解析有效目的地锚点 → 抬起 → 搬运到目的地上方 → **调整物体-目的地对齐** → 下降 → 释放 → 后退;释放后有**可选 settling routine**(夹爪保持张开 + 小幅上移若干次查询),以降低「夹爪仍在接触 / 立即扰动」的风险;
- **取消条件**:有效性条件失败 / 当前尝试进入不兼容相位 / **纠正查询预算耗尽** → 控制器返回 $\bot$ → **控制权交还 VLA**。

> 🔑 **诚实指出一条重要限制:论文自己写了**「*Geometric placement control applies only when the destination can be represented by a direct anchor. Instructions requiring more complex destination relations remain under pretrained VLA control.*」—— **恢复器只支持「能表达为直接锚点」的目的地**,复杂空间关系的目的地直接放弃恢复、还给 VLA。这直接解释了为什么 Sem(语义绑定)扰动下 FIT-MAC **不排第一**(Object 98.8 输给 AtomVLA 99.0,Spatial 86.8 输给 X-VLA 96.0)—— **语义扰动打的正是这个补丁的软肋**。

### 3.5 训练 / 推理流程与延迟开销

**训练:❌ 完全不需要训练。** 基座 VLA 全程冻结,无任何梯度更新、无新参数、无微调。这是本文**在复现门槛上最大的优势**(见「复现线索」)。

**推理流程(附录 C.1 Algorithm 1):**
每个 policy-query 边界:观测 → 选活跃子任务 → (必要时)grounding → 监控本次尝试 → 诊断 → 门控 → 路由 → 生成动作块 → **截断到 $H_{\mathrm{eff}}$** → 入队执行。

**反馈频率由一个参数控制(式 11):**

$$H_{\mathrm{eff}}=\min\!\left(H_{\mathrm{open\text{-}loop}},\ H_{\mathrm{exec}}\right)$$

$H_{\mathrm{exec}}$ 即配置项 `multi-agent-exec-horizon`。附录 A.5.4 给出该参数取值 **{1, 2, 3, 4}** 分别对应 **{11, 22, 33, 44}** 个执行步;**默认 = 2(即 22 步)**。

> ⚠️ **但这里有一个论文未讲清、却直接决定「延迟」能不能算出来的关键缺口:$H_{\mathrm{open\text{-}loop}}$ 的具体取值全文未给。** 而附录 C.2 的运行时 trace 显示 base policy 单次是「an **eight-action chunk**」—— 即 8。若 $H_{\mathrm{open\text{-}loop}}=8$,则 $H_{\mathrm{eff}}=\min(8,22)=8$,**$H_{\mathrm{exec}}$ 永远不会成为约束**,这与 A.5.4 中「horizon 从 11 调到 22 使 LIBERO-Object 的 Task SR 从 36.0% 跃到 86.0%」的强敏感性直接矛盾。**因此读者无法从论文反推真实的 policy query 频率与端到端延迟。** 这是本文在工程侧最实质的一处空白。

**每步延迟 / token 成本 / 推理开销:⚠️ 论文完全未给出。** 全文检索 `latency` / `token` / `Hz` / `second` / `cost` / `API` / `GPU` **均无实质命中**(唯一命中是 §5 结论里的 "reducing intervention overhead" 这一句未来工作表述)。**这是本报告强调的一个关键负面信息:一篇把「推理期闭环」作为核心贡献的工作,完全没有报告推理期开销。**

论文给出的**唯一**与开销相关的量化替代物是 **IR(干预率)** —— 它是**回合级**的(「至少接受过一次纠正动作的回合占比」),**不是**调用次数、不是 token 数、不是延迟。下文会说明为什么 IR 可以作为开销的**下界代理**,但它**不能**替代延迟。

### 3.6 扰动类型:分类清晰,但**没有强度分级**

| 代号 | 全名 | 论文给出的语义 | FIT-MAC 的表现(OpenVLA) |
|---|---|---|---|
| **Obj** | object identity | 物体同一性变化 | Object 99.0 / Spatial 97.2 —— **几乎不受影响** |
| **Pos** | object position | 物体位置变化 | Object 93.4 / Spatial 40.2 —— **恢复收益最大处** |
| **Sem** | semantic binding | 语义绑定变化 | Object 98.8 / Spatial 86.8 —— **不排第一** |
| **Task** | task instruction | 任务指令变化 | Object 87.2 / Spatial 37.8 —— **恢复收益最大处** |
| **Env** | environment | 环境变化 | Object 48.8 / Spatial 97.8 —— **两套件天壤之别** |

> **关于「强度分级」,必须明确写:论文没有。** LIBERO-PRO 的五类扰动在论文中**只有单一设定**,论文未引入强度参数、未做强度扫描、未报告扰动幅值。这与「鲁棒性」类论文的通常做法(至少给出 mild / medium / severe 三档)不同 —— **因此本文的「鲁棒性」结论严格来说是「对这五类特定扰动的鲁棒性」,而不是「对扰动强度的鲁棒性」。**

---

## 核心公式提取

### (F1) 候选打分的几何先验(式 1)—— 「语义优先,几何兜底」

$$S_t(c)=\left\|p_{t,\mathrm{xy}}^{c}-p_{t,\mathrm{xy}}^{\mathrm{ee}}\right\|_{2}+\lambda_{z}\left|p_{t,z}^{c}-p_{t,z}^{\mathrm{ee}}\right|,\qquad \hat{c}_t=\arg\min_{c\in\mathcal{C}_t^{\mathrm{sem}}}S_t(c)$$

**符号解释**:
- $c$ —— Grounding DINO 检出的候选实例;$\mathcal{C}_t^{\mathrm{sem}}$ —— **与指令语义兼容的候选子集**(关键约束)
- $p_{t,\mathrm{xy}}^{c}$ / $p_{t,\mathrm{xy}}^{\mathrm{ee}}$ —— 候选与末端执行器的平面坐标;$p_{t,z}$ —— 竖直坐标
- $\lambda_z$ —— 竖直距离权重;$\odot$ —— 元素除(式 7 中同义)
- $S_t(c)$ —— 打分,越小越优;$\hat{c}_t$ —— 最终选中的目标实例

**本报告的读解**:**这个式子的全部工程意义在 $\mathcal{C}_t^{\mathrm{sem}}$ 这个下标**。若不加这个约束,几何最近者永远赢 → 策略会去抓「离手最近的碗」,这恰恰是 Figure 3 上排那个失败案例(抓了盘子与ramekin之间的碗)。**先语义过滤、再几何排序,是一个正确的优先级设计**,论文对此有一句明写:*「Restricting this comparison to instruction-compatible candidates ensures that geometric proximity does not override semantic compatibility.」*

### (F2) 相位化进度 + 停滞检测(式 2–5)

$$d_t^{\mathrm{tgt}}=\left\|p_t^{\mathrm{ee}}-p_t^{\mathrm{tgt}}\right\|_2,\qquad d_t^{\mathrm{dst}}=\left\|p_t^{\mathrm{obj}}-p_t^{\mathrm{dst}}\right\|_2$$
$$\Delta d_t^{\mathrm{tgt}}=d_{t-\Delta}^{\mathrm{tgt}}-d_t^{\mathrm{tgt}},\qquad \Delta d_t^{\mathrm{dst}}=d_{t-\Delta}^{\mathrm{dst}}-d_t^{\mathrm{dst}}$$

**符号解释**:$p_t^{\mathrm{ee}}$ 末端执行器;$p_t^{\mathrm{tgt}}$ 已绑定目标;$p_t^{\mathrm{obj}}$ 被操作物体;$p_t^{\mathrm{dst}}$ 目的地;$\Delta$ —— 回看窗口的控制步数;$\Delta d>0$ 表示**距离在缩短**;$\|\Delta p_t^{\mathrm{ee}}\|_2$ / $\|\Delta p_t^{\mathrm{obj}}\|_2$ —— 末端 / 物体在 $\Delta$ 步内的位移量;$\tau_{\cdot}$ —— 各相位的最小位移/缩减阈值;$W_{\phi_t}$ —— 相位**耐心窗口**(patience window);$n_t^{\mathrm{phase}}$ / $T_{\phi_t}$ —— 相位已用时长 / 相位时限(超时判据 $\chi_t^{\mathrm{timeout}}=\mathbf{1}[n_t^{\mathrm{phase}}>T_{\phi_t}]$)。

> **注意「进展」的判据是析取(∨)**:距离没缩短**但**末端还在动 → 仍算进展。**这是为了容忍「绕行接近」「抓取前的微调」这类不朝目标直线推进但仍在推进的合法行为。** 相应地,只有当**整个耐心窗口内既无距离缩减、又无任何位移**时 ($\sum \chi^{\mathrm{prog}}=0$) 才判 stall。

### (F3) 失败分类与路由(式 6)—— 全文的枢纽

$$d_t=\begin{cases}\text{target-failure},&\kappa_t<\tau_{\kappa}\ \lor\ \mathrm{Inconsistent}(g_t,I_t),\\[2pt]\text{pick-failure},&\phi_t\in\Phi_{\mathrm{pick}}\land\left(\chi_t^{\mathrm{stall}}=1\lor\chi_t^{\mathrm{timeout}}=1\right),\\[2pt]\text{place-failure},&\phi_t\in\Phi_{\mathrm{place}}\land\left(\chi_t^{\mathrm{stall}}=1\lor\chi_t^{\mathrm{timeout}}=1\right),\\[2pt]\text{none},&\text{otherwise}.\end{cases}$$

**符号解释**:$d_t$ —— 本次诊断;$\kappa_t$ —— 活跃目标锁的置信度;$\tau_\kappa$ —— 置信度门限(默认 **0.12**,敏感性取值 0.10/0.12/0.18);$\mathrm{Inconsistent}(g_t,I_t)$ —— 已锁定的实例与当前观测或指令空间关系不再一致;$\phi_t\in\{\Phi_{\mathrm{pick}},\Phi_{\mathrm{place}}\}$ —— 相位归属。

> **这个式子的三个可迁移设计:**
> 1. **目标绑定错误享有最高优先级** —— 即使在 pick 相位已判 stall,先修绑定;
> 2. **绑定判据是「或」** —— 低置信 **或** 与观测不一致,任一成立即触发;这让「VLM 自认为很确定但选错了」这种最危险的情形也能被抓住;
> 3. **分类与「是否干预」被分成两步**(诊断 $d_t$ vs 门控 $\Gamma$)—— 这正是 3.2 节说的「记录失败但不下手」的实现基础。

### (F4) 有界局部恢复控制律(式 7–8)

$$u_t^{\mathrm{rec}}=\operatorname{clip}\!\left((p_t^{*}-p_t^{\mathrm{ee}})\oslash\bm{s},\,-1,\,1\right),\qquad a_t^{\mathrm{rec}}=\left[\left(u_t^{\mathrm{rec}}\right)^{\top},\ \mathbf{0}_{3}^{\top},\ a_t^{\mathrm{grip}}\right]^{\top}$$

**符号解释**:$p_t^{*}$ —— 相位专属 waypoint(hover / target / destination / retreat);$p_t^{\mathrm{ee}}$ —— 当前末端位姿;$\bm{s}=(s_x,s_y,s_z)$ —— **逐轴位移缩放**(P 控制器增益);$\operatorname{clip}(\cdot,-1,1)$ —— 归一化动作限幅;$a_t^{\mathrm{grip}}$ —— 夹爪命令;$\mathbf{0}_3$ —— **旋转命令恒为零**。

> **本报告必须点破的一点:这个控制律是一个「手写的几何 P 控制器」,不含任何学习成分,也不做旋转补偿。** 它之所以能工作,是因为 LIBERO 的 pick-place 任务里「移动到某个 3D 点」是够用的。**在需要旋转对齐、需要处理物体姿态、需要柔性接触的任务上,这个恢复器是不可用的。** 这是理解本文全部实验结果的关键(见「关键成果」中「增益的主要来源」分析)。

### (F5) 干预与恢复的指标(式 9)—— 本文最值得其他论文抄的一个设计

$$\mathrm{IR}=\frac{N_{\mathrm{int}}}{N_{\mathrm{all}}},\qquad \mathrm{RSR}=\frac{N_{\mathrm{succ,int}}}{N_{\mathrm{int}}}$$

**符号解释**:$N_{\mathrm{all}}$ —— 评估回合总数;$N_{\mathrm{int}}$ —— **至少接受过一次纠正动作**的回合数;$N_{\mathrm{succ,int}}$ —— 其中成功的回合数;IR —— 干预率(需干预的回合占比);RSR —— 被干预回合中的成功率。

> 🔑 **为什么这三个指标必须一起看(这是本报告对本文方法论的最高评价):**
>
> **单看 SR 无法区分「方法很强」与「方法在每一步都插手」。** 一个把每个回合都接管 100% 的系统,SR 一样可以是 93.4%。IR 告诉你**干预有多频繁**(Pos 扰动下 OpenVLA 是 **99.5%** 的回合都被干预),RSR 告诉你**干预之后到底救回来没有**(Pos 下 **93.8%**)。
>
> **IR + RSR + SR 三元组把「鲁棒性」变成了一个可分解的量**:
> $$\mathrm{SR} \approx (1-\mathrm{IR})\cdot \mathrm{SR}_{\mathrm{nominal}} + \mathrm{IR}\cdot\mathrm{RSR}$$
>
> **本项目已收录论文中,明确把「方法开销」与「方法效果」分开报告的极少** —— Spark-0 报 token 消耗(§12.3),FastVLA 报预算匹配,本文报 IR/RSR。**这三个是本项目迄今见到的「开销-效果分离」最完整的报告范式,建议固化为常设核查项。**

---

## 关键成果与贡献

### 证据强度评级:⭐⭐⭐(3 / 4)—— 方法学证据中等偏强,工程与成本证据弱

| 子结论 | 评级 | 理由 |
|---|---|---|
| 「同 seed / 同 episode 预算下 FIT-MAC > OpenVLA」 | ⭐⭐⭐⭐ | 变量控制严格:同任务分配、同 episode 预算、同随机种子;5 seed × 100 episode 的逐 seed 表全给;**本项目 §12.3「变量控制」维度上属干净的一档** |
| 「IR/RSR 把开销与效果分离」 | ⭐⭐⭐⭐ | 指标设计本身是本篇最硬的贡献,且逐格给全 |
| 「跨骨干可迁移(OpenVLA / π0 / π0.5)」 | ⭐⭐⭐ | 三骨干全覆盖是真加分项,但 π0 / π0.5 的 LIBERO 适配方式(fine-tune? zero-shot? 具体 checkpoint)**论文未给** |
| 「增益主要来自 execution correction」 | ⭐⭐⭐⭐ | 消融是**同骨干、同 seed、同其余组件**的受控对照(附录 A.4 明确:「keeps the backbone, prompts, evaluation seeds, perturbation settings, and remaining components unchanged」)——**单变量归因成立** |
| 「SOTA(10 个条件中 8 个第一)」 | ⭐⭐⭐ | 数字可核(下表逐格验算通过),但**基线含大量缺失值(「–」)**,且若干基线成绩是「published benchmark results」(论文原话),非同口径重跑 |
| 「工业可部署性 / 实时性」 | ⭐ | **论文零数据**:无延迟、无 token、无 GPU、无真机、无安全讨论 |
| 「可复现性」 | ⭐⭐ | 无公开仓库(仅匿名 artifact 链接);VLM/LLM 型号未披露;$H_{\mathrm{open\text{-}loop}}$ 未给;主表配置(LLM 开/关)未声明 |

**总体 ⭐⭐⭐(3/4)**:**方法学与实验设计的可信度明显高于其工程可迁移性的可信度。** 论文把「失败检测 + 分类 + 路由」这件工程上最脏的活做成了一个可实现的确定性状态机,并用 IR/RSR 把自己的开销暴露出来 —— **这是一篇「方法诚实度」高于「工程完备度」的论文。** 依赖未披露模型 + 零延迟数据 + 零真机,三重因素共同压低了评级(对照本项目 §12.1「算力充裕设定下成立的方法对产业无意义」的判据,**本篇恰恰没有回答「它在部署算力下是否成立」这个最关键的问题**)。

### 主结果:Table 1(SR %,与 SOTA 对比)

| 方法 | O-Obj | O-Pos | O-Sem | O-Task | O-Env | S-Obj | S-Pos | S-Sem | S-Task | S-Env | Avg |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| MolmoAct (Lee+ 2025) | 92.0 | 6.0 | 96.0 | 0.0 | – | 90.0 | 0.0 | 88.0 | 0.0 | – | – |
| NORA (Hung+ 2025) | 86.0 | 0.0 | 92.0 | 0.0 | – | 92.0 | 0.0 | 91.0 | 0.0 | – | – |
| X-VLA (Zheng+ 2026) | 89.0 | 2.0 | 98.0 | 8.0 | – | 97.0 | 0.0 | 96.0 | 0.0 | – | – |
| AtomVLA (Sun+ 2026) | 93.0 | 10.0 | 99.0 | 0.0 | – | 95.0 | 16.0 | 95.0 | 1.0 | – | – |
| CaP-Agent0 (Fu+ 2026) | – | 22.0 | – | 18.0 | – | – | 12.0 | – | 14.0 | – | – |
| RATs (Zhang+ 2026a) | – | **61.0** | – | **63.0** | – | – | **29.0** | – | **31.0** | – | – |
| OpenVLA (Kim+ 2024) | 98.0 | 0.0 | 98.0 | 0.0 | 0.0 | 97.0 | 0.0 | 77.0 | 0.0 | 89.0 | 45.9 |
| **FIT-MAC(本文)** | **99.0** | **93.4** | 98.8 | **87.2** | **48.8** | **97.2** | **40.2** | 86.8 | **37.8** | **97.8** | **78.7** |

**逐格验算(本报告独立核算,确认论文无误):**
- OpenVLA 平均 = (98+0+98+0+0+97+0+77+0+89)/10 = **45.9** ✅ 与论文一致;
- FIT-MAC 平均 = (99.0+93.4+98.8+87.2+48.8+97.2+40.2+86.8+37.8+97.8)/10 = **78.7** ✅;
- 相对 OpenVLA 提升 = 78.7 − 45.9 = **+32.8 点** ✅(论文原话「exceeding OpenVLA by 32.8%」,严格说是**百分点**);
- LIBERO-Object Pos 相对最强对手 RATs:93.4 − 61.0 = **+32.4 点** ✅;Task:87.2 − 63.0 = **+24.2 点** ✅;
- 「8 / 10 条件第一」独立核对:输掉的两个是 **O-Sem(98.8 vs AtomVLA 99.0)** 与 **S-Sem(86.8 vs X-VLA 96.0)** —— 其余 8 项 FIT-MAC 均为该列最高 ✅。

### 干预行为:Table 2(SR / IR / RSR,%)

| 扰动 | O-SR | O-IR | O-RSR | S-SR | S-IR | S-RSR |
|---|---:|---:|---:|---:|---:|---:|
| Obj | 99.0 | 99.8 | 99.3 | 97.2 | 37.8 | 97.9 |
| Pos | 93.4 | 99.5 | 93.8 | 40.2 | 87.6 | 41.3 |
| Sem | 98.8 | 98.9 | 99.6 | 86.8 | 42.8 | 98.6 |
| Task | 87.2 | 100.0 | 87.1 | 37.8 | 90.6 | 35.5 |
| Env | 48.8 | 50.4 | 97.5 | 97.8 | 21.2 | 99.1 |

**本报告从这张表读出的三条(论文没写,但数据摆在那里):**

1. **IR 出现了「反直觉的双峰」:越难的扰动,干预越少。** LIBERO-Spatial 上:Env(OpenVLA 已 89.0%)→ IR **21.2%**;Obj(97.0%)→ IR **37.8%**;Sem(77.0%)→ IR **42.8%**;而 Pos(0.0%)→ IR **87.6%**、Task(0.0%)→ IR **90.6%**。
   > **解释:IR 是「基线已经好」的反向指标。** 门控要求「持续失败证据」,而基线越强,越难积累到触发阈值 —— 所以 **IR 高 ⇔ 基线在该条件下几乎全败**。这实际上是**门控在按需介入**的证据,而不是「乱插手」。
2. **RSR 暴露了「恢复了但没救回来」的真相。** LIBERO-Spatial 的 Pos:SR 40.2 / IR 87.6 / **RSR 41.3** —— **87.6% 的回合被干预,但干预后只有 41.3% 成功**。这意味着 **近 60% 的被干预回合是「干预了也没救回来」**。Task 更极端:IR 90.6% / RSR 35.5%。
   > 🔑 **这直接推翻了「装了 FIT-MAC 就等于鲁棒」的直觉。** 在 Spatial 的 Pos / Task 上,装了框架的净收益是 0.0% → 40.2%,但**仍有约六成被干预回合彻底失败**。**真正的瓶颈是「干预之后仍救不回来」,而不是「检测不到」** —— 这与论文自己的失败案例 B.3 完全吻合(*「the gripper repeatedly fails to grasp it after approaching」* —— 目标识别对了,抓取就是抓不住)。
3. **Object 的 Env 条件是全文最刺眼的一格:SR 48.8 / IR 50.4 / RSR 97.5。** 即 **被干预的回合 97.5% 成功了,但整体只有 48.8%** —— 说明**另外 49.6% 的回合根本没触发干预,于是基线直接失败**。**门控在这里「过于保守」了。** 这是本报告认为**门控参数(尤其 failure threshold)存在明显可调空间**的直接证据 —— 而 Table 4 显示 failure threshold 从 2 调到 4 时 LIBERO-Object 的 SR **纹丝不动地停在 85.4%**,说明**调这个阈值救不回 Env 这一格**。

### 跨骨干泛化:Table 6(五扰动平均 SR,%)

| 基准 | 方法 | OpenVLA | π0 | π0.5 |
|---|---|---:|---:|---:|
| LIBERO-Object | 仅基座 | 39.2 | 42.6 | 57.0 |
| | **+ FIT-MAC** | **85.4** | **78.4** | **79.4** |
| | **Δ** | **+46.2** | **+35.8** | **+22.4** |
| LIBERO-Spatial | 仅基座 | 52.6 | 50.8 | 52.2 |
| | **+ FIT-MAC** | **72.0** | **67.4** | **69.2** |
| | **Δ** | **+19.4** | **+16.6** | **+17.0** |

**Table 5 完整逐条件(SR/IR/RSR,%)** —— 摘取最关键的几行:

| 基准 | 条件 | OpenVLA | +FIT-MAC | π0 | +FIT-MAC | π0.5 | +FIT-MAC |
|---|---|---|---|---|---|---|---|
| Object | Task | 0.0/–/– | 87.3/100.0/87.1 | 0.0/–/– | 84.0/98.0/85.7 | 1.0/–/– | 80.0/100.0/80.0 |
| Object | Pos | 0.0/–/– | 93.1/99.5/93.8 | 0.0/–/– | 67.0/100.0/67.0 | 17.0/–/– | 67.0/99.0/67.7 |
| Object | Env | 0.0/–/– | 48.8/50.4/97.5 | 29.0/–/– | 65.0/78.0/82.1 | 73.0/–/– | 69.0/79.0/86.1 |
| Spatial | Pos | 0.0/–/– | 40.2/87.6/41.3 | 0.0/–/– | 36.0/98.0/34.7 | 20.0/–/– | 37.0/98.0/37.8 |
| Spatial | Task | 0.0/–/– | 37.8/90.6/35.5 | 0.0/–/– | 27.0/100.0/27.0 | 1.0/–/– | 25.0/100.0/25.0 |
| Spatial | Sem | 77.0/–/– | 86.8/42.8/98.6 | 97.0/–/– | 83.0/60.0/81.7 | 97.0/–/– | 93.0/63.0/88.9 |

> **一处必须指出的「负增益」:π0.5 在 LIBERO-Spatial 的 Sem 条件下,加 FIT-MAC 反而从 97.0 掉到 93.0;Object 的 Env 从 73.0 掉到 69.0。** 论文正文强调「consistently improves」,但**表格里有 2 处下降**。这与下一节的消融发现是同一件事的不同侧面。

### 消融:Table 3(OpenVLA,五扰动平均 SR,%)

| 配置 | Object | Spatial | Avg | ΔSR(Object) | ΔSR(Spatial) |
|---|---:|---:|---:|---:|---:|
| **FIT-MAC(完整)** | **85.4** | **72.0** | **78.7** | 0.0 | 0.0 |
| w/o target correction | 77.2 | 69.8 | 73.5 | −8.2 | −2.2 |
| **w/o execution correction** | **47.0** | 62.4 | **54.7** | **−38.4** | **−9.6** |
| w/o hard pick | 50.2 | 70.0 | 60.1 | −35.2 | −2.0 |
| w/o hard place | 63.2 | 64.0 | 63.6 | −22.2 | −8.0 |

**三条必须写下来的结论:**

1. 🔑 **增益的主要来源是「执行纠正」,不是「多智能体推理」。** 去掉 execution correction → 平均 SR 从 **78.7% 掉到 54.7%**(**−38.4 点**,Object 上更是 −38.4)。而 target correction 只有 −8.2。
   > **本报告的读解:「执行纠正」= 手写的几何抓放控制器(式 7–8)+ hard pick / hard place 两条流程。** 也就是说,**框架增益的主体是一个「传统模块化抓放栈」在 VLA 跑飞时的兜底**,而不是 LLM 智能体对失败的理解能力。**这既是本文最强的工程结论,也是它最强的对照缺口 —— Table 1 里没有任何一个「VLA + 传统抓放兜底」的非本文基线。** 一个审稿人完全可以问:*「你的 gain 是不是主要来自那个 P 控制器?」* 论文没有回答,也没有做这个对照。
2. **hard pick 高度偏向 LIBERO-Object(−35.2 vs −2.0),hard place 偏向两侧(−22.2 / −8.0)。** 论文的解释:*「Hard pick primarily benefits LIBERO-Object」*。
3. ⚠️ **消融表内部存在反例,论文自己承认了(*「some ablated variants outperform full FIT-MAC in individual settings」*)。** 附录 A.4 / Table 10 里,π0.5 在 LIBERO-Spatial 上:
   - 去掉 **target corrector**:Task **25.0 → 27.0**(更好);
   - 去掉 **execution corrector**:Task **25.0 → 47.0**(**大幅更好!**)、Pos 37.0 → 35.0(更差);
   - 去掉 **hard pick**:Task **25.0 → 45.0**、Pos **37.0 → 55.0**(**大幅更好!**)。
   > 🔑 **这是本报告认为全文最重要的一个未被充分强调的负面结果:在 π0.5 + LIBERO-Spatial 上,「少加组件」比「全加」更好,去掉 hard pick 能让 Pos SR 从 37.0 涨到 55.0(+18 点)。** 论文的措辞是「收益依赖骨干与扰动」,但表格显示的是**框架组件在最弱的那个组合上会主动伤害性能**。合理的机制猜测:π0.5 的空间 grounding 本来就比 OpenVLA 强,重绑定反而把它拽向错误实例(对应 B.3 的「VLM 选了错误的碗」失败模式)。**这意味着「多智能体闭环」在强基座上可能是有害的 —— 这是一个反直觉且对产业重要的判断。**

### 超参敏感性:Table 4(OpenVLA)

| 参数 | 取值 | Object | Spatial | Avg | 默认 |
|---|---|---|---|---|---|
| Failure threshold | 2 / 3 / 4 | 85.4 / 85.4 / 85.4 | 70.8 / 70.6 / 70.6 | 78.1 / 78.0 / 78.0 | **3** |
| Confidence threshold | 0.10 / 0.12 / 0.18 | 85.4 / 85.4 / 85.4 | 71.0 / 70.6 / 71.0 | 78.2 / 78.0 / 78.2 | **0.12** |
| Minimum rescue step | 8 / 12 / 16 | 85.4 / 85.4 / 85.4 | 71.2 / 70.6 / 71.0 | 78.3 / 78.0 / 78.2 | **12** |
| **Execution horizon** | **1 / 2 / 3** | **68.0 / 85.4 / 87.4** | **72.0 / 70.0 / 69.8** | **70.0 / 77.7 / 78.6** | **2** |

**读法:**
- **前三个参数几乎不敏感**(Avg 变动 ≤ 0.3 点)—— **这是好消息:门限不需精调,说明框架的鲁棒性不靠手调阈值撑着。** 这一点对产业落地很关键(§5 里我把它列进「量产壁垒:可缓解」)。
- **执行 horizon 是唯一有实质影响的参数**,且**方向是反直觉的**:horizon 越大(1→2,即 11→22 步)平均 SR 从 70.0% 升到 77.7%,**主要收益在 LIBERO-Object**。附录 A.5.4 给了细节:horizon 11→22 使 LIBERO-Object 的 Task SR 从 **36.0% → 86.0%**、Pos 从 **58.0% → 94.0%**;但 **44 反而下降**(Task 77.0 / Pos 79.0);而 LIBERO-Spatial 上 22→33 会让 Pos 从 41.0 降到 39.0、Env 从 99.0 降到 97.0。
  > **机制**:horizon 越长 → 反馈越稀疏 → **故障持续更久才被察觉**;horizon 越短 → 反馈越密 → 但**每次反馈都要跑一次监控 + 诊断(+ 可能一次 VLM 查询),算力开销上升**,且过密的干预会打断 VLA 正在进行的有效动作。**论文选了 22 作为「跨扰动更均衡」的折中。** 这条曲线本身就是「**反馈频率 ↔ 效果 ↔ 开销**」三者权衡的实证,可惜论文**只报告了效果,没有报告开销那一维**。
- ⚠️ **一处论文未解释的数字不一致**:Table 3 的完整 FIT-MAC 平均是 **78.7**(Object 85.4 / Spatial 72.0),而 Table 4 中**默认值行**(horizon = 2)给出的是 **77.7**(Object 85.4 / **Spatial 70.0**)。**Spatial 上差 2.0 点、Avg 差 1.0 点,论文未给解释。**
  > **本报告的推测(标注为推测)**:Table 3 的 FIT-MAC 行来自主实验(**每任务 50 episodes**),而 Table 4 / Table 9 / Table 10 的逐条件数据来自消融协议(**每任务 10 episodes**,附录 A.1 明确区分)。可交叉验证:Table 9 的 OpenVLA Full FIT-MAC 逐条件 = 86.0 / 94.0 / 100.0 / 98.0 / 49.0,平均 = 85.4;而 Table 1 主实验 = 87.2 / 93.4 / 99.0 / 98.8 / 48.8,平均 = 85.44 ≈ 85.4 —— **两者平均相同、逐条件不同**,与「同均值不同样本」的解读一致。**这不是错误,但论文没有标注,读者极易误读为同一个实验。**

### 多 seed 稳定性:Table 7 / 8(OpenVLA + FIT-MAC)

- **LIBERO-Object**:平均 SR **85.4%**,**总体标准差 0.1%**;
- **LIBERO-Spatial**:平均 SR **71.7%**,**总体标准差 0.9%**;
- **条件级最大波动**:LIBERO-Spatial 的 **Pos**:均值 **38.0%**,**σ = 2.8%**;
- **最稳的一格**:LIBERO-Object 的 **Obj**:**所有 5 个 seed 都是 100.0%**。

> **本报告的评价:这是本文实验设计最好的部分,也是它敢下「consistent gains」这句话的底气。** 5 个 seed × 每条件每套件 100 episodes,逐 seed 的 SR/IR/RSR 全表公开,统计量用**总体标准差**(population σ,公式 10)并明确写了 $N=5$。
> ⚠️ **但要注意口径**:σ = 0.1% / 0.9% 是**跨 5 个扰动条件平均后的套件级**统计量,不是条件级。条件级的真实波动要差得多 —— 论文自己给出最差的一格是 Spatial Pos 的 **σ = 2.8%**。**读者若只看「σ = 0.1%」会严重高估稳定性。**

### 延迟 / 推理开销 / token 成本

⚠️⚠️ **论文未给出 —— 任何一项都没有。**

| 项 | 论文是否给出 |
|---|---|
| 端到端延迟 / 控制频率(Hz) | ❌ **论文未给出** |
| 每步推理耗时 | ❌ **论文未给出** |
| LLM / VLM 调用次数(每回合 / 每步) | ❌ **论文未给出** |
| token 消耗 | ❌ **论文未给出** |
| API 成本 | ❌ **论文未给出** |
| GPU 型号 / 显存 / 训练时长 | ❌ **论文未给出**(且**无需训练**) |
| 唯一的开销代理指标 | ✅ **IR(回合级干预率)** |
| 唯一与开销相关的定性表述 | ✅ §5:*「Future work will focus on reducing intervention overhead」* |

> **本报告的判断:这是本文最刺眼的缺失,也是它与本项目 §12.1「实时正在从加分项变成准入门槛」这条产业判据之间的最大张力。** 一篇把「推理期闭环」当核心卖点的工作,必须回答:**加了四个 agent 之后,一次 pick-place 从多少毫秒变成多少毫秒?** 论文没答。
>
> **可用的间接推断(本报告的估计,非论文给出)**:IR 在 Pos / Task 条件下是 **87.6%–100%**,即**几乎每个回合都至少触发一次纠正**;而 target correction 必然包含一次 Grounding DINO 检出 + 至少一次 VLM 候选选择(runtime trace 记录了 *「VLM confidence 0.95」*),execution correction 则包含每个 policy-query 边界的一次监控 + 诊断。**因此每回合的 VLM 查询次数至少是 1~2 次量级,再加上执行 horizon 缩短带来的 VLA 重查询次数上升。** ⚠️ **这是一个结构性推断,不是延迟数字。**

### 失败案例分析(附录 B.3,论文给了两个定性案例)

| 案例 | 现象 | 根因 | 论文自己的定性 |
|---|---|---|---|
| **左:target rebinding error** | 指令要求「cookie box 旁边的碗」,但 VLM 在 Grounding DINO 的候选中选了「ramekin 旁边的碗」 | **空间关系理解错误** —— VLM 的选择违反了指令的空间关系 | *「This failure originates in target selection rather than low-level control. Completing the grasp therefore does not resolve the upstream grounding error.」* |
| **右:pick stall** | 指令要求「ramekin 旁边的碗」,VLM 选对了,但**夹爪反复抓不住** | **抓取执行失败** —— 目标正确,控制不行 | *「correct grounding alone does not ensure successful manipulation」* |

> 🔑 **这两个案例合起来构成了本文最诚实、也最有价值的一段自我否定:**
> - **左案例暴露了 target corrector 自身的脆弱性** —— 它是框架里负责「修正错误绑定」的组件,但它自己就是那个会被空间关系骗过的 VLM。**用一个不可靠的组件去修另一个不可靠的组件,净收益取决于谁更准。** 这正好解释了 π0.5 + Spatial 上「去掉 target corrector 反而更好」的消融反例。
> - **右案例暴露了框架的能力天花板** —— **目标对了、抓不住,系统就没救了**。恢复器能做的只是「重开夹爪 + 再走一次受控下降」,**它不能改变抓取的物理可行性**。**这解释了 RSR 在 Spatial Pos / Task 上只有 41.3% / 35.5% 的现象。**
> - **附录 B 明确列出了「剩余局限在空间 grounding 与抓取执行」** —— 论文的结论段也写了未来方向是 *「improving semantic and spatial grounding to support reliable long-horizon execution」*。

---

## 局限性与未来展望

### ① 论文自述的局限与未来方向

- **§5 结论**明确列出的两条未来工作:(a) **降低干预开销**(reducing intervention overhead);(b) **改进语义与空间 grounding**,以支撑可靠的长时程执行。
- **§C.1 的实现边界自述**:
  - 几何放置控制**仅在目的地可表达为「直接锚点」时可用**;需要更复杂目的地关系时**仍由预训练 VLA 控制**(即放弃恢复);
  - 纠正会被**取消**的三种情况:有效性条件失败 / 当前尝试进入不兼容相位 / **纠正查询预算耗尽**;
  - 候选缺失或不可靠时,额外的语言模型查询**受配置的查询预算约束**;
  - 对 Obj / Sem / Env 路由,门控**额外要求进度守卫**;
- **附录 B.3 自述的两类残余失败**:空间 grounding 错误、抓取执行失败。

### ② 本报告在阅读中发现的额外问题(按严重性排序)

1. 🔴 **零延迟 / 零成本数据,是全文最严重的缺失。** 一篇以「推理期闭环」为卖点的论文,**不报告延迟、不报告 token、不报告调用次数**,等于**无法回答「这套东西能不能上机器人」**。对照本项目 §12.1 ——「实时正在从加分项变成准入门槛,而门槛按部署算力划线」—— **本篇恰好落在它自己的盲区里**。(评级影响:工程结论从 ⭐⭐⭐⭐ 降到 ⭐)
2. 🔴 **缺少「最直接的对照基线」。** Table 1 的对比对象是别的 VLA 论文(且多为「published benchmark results」,非同口径重跑),**没有一个「VLA + 传统脚本抓放兜底」的基线**。而消融显示:**去掉 execution correction 掉 38.4 点** —— 这**在逻辑上等价于**说「增益的主体来自那个手写几何抓放器」。**论文的对比框架让「多智能体」承担了本该由「传统兜底」承担的功劳。** 补上这个基线是本文最应该做但没做的事。
3. 🔴 **基线太弱,放大了效应量。** OpenVLA 在 **10 个条件中的 5 个是精确的 0.0%**。与 0.0% 比 +93.4 点的说服力,远弱于与一个 60% 的基线比 +33 点。论文未说明用的是哪个 OpenVLA 变体(原始权重? LIBERO 微调?)、也未说明 π0 / π0.5 在 LIBERO 上是 zero-shot 还是微调 —— **这直接影响「+46.2 点」这个数字的可比性**。
4. 🟠 **「多智能体」的三个 agent 中,LLM 是可选的 —— 但论文没说主表用的是哪个配置。** Planner 有规则 fallback,Verifier 的语言模型评估是 optional。**如果主表是纯规则配置,那本文的贡献其实是「一个精心设计的确定性运行时状态机」,与 LLM agent 关系不大;如果是 LLM 配置,则复现门槛与成本问题立刻出现。** 这个二义性贯穿全文且从未被澄清。**这是本文对读者最不友好的一处。**
5. 🟠 **组件在最弱组合上会主动伤害性能(已由论文自己的表格证明)。** π0.5 + LIBERO-Spatial:去掉 hard pick → Pos SR **37.0 → 55.0**(+18);去掉 execution corrector → Task SR **25.0 → 47.0**(+22)。**「多智能体闭环对强基座可能有害」这一结论论文只写了一句轻描淡写的话,本报告认为它应当被当作一个独立的发现来报告。**
6. 🟠 **没有真机实验,没有仿真器说明。** 全文无真机、无 MuJoCo / Isaac 提及、无机器人型号、无控制频率。**LIBERO 的「Env 扰动」是仿真里的环境扰动,与真实光照 / 材质 / 相机畸变的差距极大**,而 Env 恰好是 Object 套件上 SR 最低的一格(48.8)。
7. 🟠 **统计口径混乱:主实验 50 eps/task、消融 10 eps/task、逐条件表跨两套协议。** Table 1 的 Object Pos = 93.4,而 Table 9 的 Full FIT-MAC Pos = 94.0;Spatial Env = 97.8 vs 99.0(差 1.2 点)。**同一篇论文里同一配置的数字有两个版本,论文未加区分标注。**
8. 🟡 **Table 3 与 Table 4 的默认值不自洽(78.7 vs 77.7),论文未解释**(本报告的推测见「关键成果」)。
9. 🟡 **扰动强度无分级。** 五类扰动各只有单一设定,无法判断「严重扰动下是否仍有效」。**一篇主打鲁棒性的论文不做强度扫描,是硬伤。**
10. 🟡 **恢复器的能力边界窄。** 式 7–8 的旋转命令恒为 $\mathbf{0}_3$、只支持「直接锚点」目的地、只覆盖 pick / place 两个相位。**装配、工具使用、铰接、柔性物体、多步长任务全部不在覆盖范围内** —— 而论文的贡献声明里是笼统的「long-horizon execution」。
11. 🟡 **安全 / 认证零讨论。** 恢复器会在「机器人已经抓歪」时接管并直接下压 —— 论文完全未讨论力限、碰撞、夹伤风险。**对照本项目 §4:ISO 10218 / ISO/TS 15066 / 欧盟 AI Act,这套系统的可认证性是空白。**
12. 🟡 **可复现性材料缺失:**$H_{\mathrm{open\text{-}loop}}$ 未给、$\lambda_z$ / $\tau_{\cdot}$ / $W_{\phi_t}$ / $T_{\phi_t}$ / $\bm{s}$ 的具体值未给(附录只给了敏感性扫描的几个超参)、**所选 VLM / LLM 型号未给**、匿名 artifact 链接不可核验。

### ③ 未来方向(论文提的 + 本报告推断的)

**论文提的**:降低干预开销;改进语义与空间 grounding;支撑长时程执行。

**本报告推断的(基于上表的缺口):**
- **补「VLA + 传统脚本兜底」基线**,并把「多智能体净贡献」与「兜底净贡献」分开计价 —— **这是本文结论能否成立的关键**;
- **把恢复器从「手写 P 控制器」升级为「可学习的恢复策略」(类似论文自己引用的 RACER:用自动生成的恢复轨迹训练一个 recovery policy)**,这能直接压低 Spatial Pos / Task 上只有 35.5%–41.3% 的 RSR;
- **把 LLM 角色从「诊断」退回「候选消歧」** —— 论文其实已经这么做了(诊断是确定性的),但标题与叙事仍是 "Multi-Agent";**叙事与实现的错位会误导读者对成本与延迟的预期**;
- **真机验证是必需的下一步**:本文的整套逻辑建立在「几何信号足够可靠」之上,而真实抓取的接触噪声、遮挡、标定漂移都会直接打到这套规则式检测器 —— **这恰恰是本项目 Spark-0 / BlindBaoding 两篇所覆盖的领域,应当交叉追踪**。

---

## 复现线索

- **代码**:🟡 **无公开仓库**。论文脚注给出 `https://anonymous.4open.science/r/research-artifact-B431`(**匿名评审工件链接,非 GitHub**)与项目页 `https://fitmac-research.pages.dev/`。⚠️ **本报告按任务约束未联网核验其内容**。按本项目 §11.2 口径 → **(b) 仅承诺发布**,且形态比典型「仅承诺发布」更弱。**若要做严格复现,应假定「无可用代码」。**
- **数据**:**无需新采集数据**。评测用 **LIBERO-Object + LIBERO-Spatial**(Liu et al. 2023)的 **LIBERO-PRO** 扰动协议(Zhou et al. 2025)。⚠️ **论文未给出任务数**(标准划分为各 10 任务,属公开信息量级)。
- **是否需要训练**:❌ **完全不需要训练**。基座 VLA 冻结,框架是纯推理期控制层。**这是本篇相对本项目已收录多数论文(Spark-0 需 96 GPU × 400k 步)的最大优势。**
- **依赖基座 VLA**(三选一即可,**全部冻结**):
  - **OpenVLA**(Kim et al. 2024)—— 开源自回归基座,**论文未给具体 checkpoint / 是否 LIBERO 微调**;
  - **π0**(Black et al. 2024)—— 需 Physical Intelligence 的 openpi 实现;
  - **π0.5**(Intelligence et al. 2025)—— 同上;⚠️ **论文未给 LIBERO 上的适配方式**。
- **依赖的感知 / 推理组件**:
  - **Grounding DINO**(开放词检测,开源);
  - **VLM 候选选择器** —— ⚠️ **型号未披露**;
  - **Planner 的语言模型** —— ⚠️ **型号未披露**,且论文写明有**规则化 fallback**;
  - **Verifier 的语言模型评估** —— ⚠️ **型号未披露**,且论文写明是 **optional**。
- **依赖的闭源 LLM API 与其调用成本**:⚠️ **无法从论文确定**。论文**未点名任何 LLM/VLM 型号**(全文检索 GPT / Claude / Gemini / Qwen / LLaVA / InternVL / DeepSeek **均无命中**),因此 **token 单价、调用次数、单回合成本均无法计算**。
  > 📌 **本报告的处理方式**:遵守「禁止编造 API 单价」,**不给出任何具体单价数字**。可确定的只有**调用次数的结构性下界**:IR 在 Pos / Task 条件下为 87.6%–100% → **几乎每个回合至少一次 VLM 查询(候选歧义时)+ 每个 policy-query 边界一次监控诊断**;外加 execution horizon 从开环缩短带来的 **VLA 重查询次数上升**。⚠️ **以上为结构性推断,非论文数据。**
- **硬件 / 算力**:⚠️ **论文未给 GPU 型号、显存、训练时长**(训练本身不需要)。复现所需的**推理侧**算力至少要同时容纳:冻结的 7B 级 VLA(OpenVLA)+ Grounding DINO + 一个 VLM。**论文未指明 VLM 是本地部署还是 API 调用** —— 这直接决定能不能塞进 Jetson 级别边缘算力。
- **评测配置(必须复现的协议)**:
  | 项 | 值 |
  |---|---|
  | 主实验 | 每任务 **50 episodes** |
  | 消融 | 每任务 **10 episodes** |
  | 多 seed | **{7, 11, 13, 17, 23}**,每任务每 seed 10 episodes → 每条件每套件 **100 episodes** |
  | 统计 | 跨 seed 的**总体标准差**(公式 10,$N=5$) |
  | 超参默认值 | failure threshold **3**;confidence threshold **0.12**;min rescue step **12**;exec horizon **2**(≈22 步) |
- **复现难度评估**:🟠 **中高(算法侧中,数据侧低,工程侧高)**。
  - **算法侧 🟡 中**:四个 agent 的**接口是清楚的**(附录 C.3 给了全部 4 段 system prompt + JSON schema),诊断逻辑是**公式化的**(式 1–8)—— **这是本篇对复现最大的善意:它把自己的决策逻辑写成了可实现的公式,而不是留给读者猜。**
  - **数据/训练侧 🟢 低**:无训练、无新数据,benchmark 是公开的。
  - **工程侧 🔴 高**:① **VLM/LLM 型号未披露** → 无法复现「ambiguous 候选」的判定行为,而这恰恰是 target failure 的核心检测环节;② **$H_{\mathrm{open\text{-}loop}}$ 未给** → 无法确定反馈频率,也就无法对齐 horizon 消融;③ **阈值族**($\tau_{\mathrm{tgt}},\tau_{\mathrm{ee}},\tau_{\mathrm{dst}},\tau_{\mathrm{obj}},W_{\phi_t},T_{\phi_t},\lambda_z,\bm{s}$)**的具体值全部未给**,而附录只做了 4 个超参的敏感性扫描,**这 8 个常数才是真正的自由度所在**;④ 无代码。
  - **一句话估计**:**有经验的多智能体 / 机器人团队约需 2–4 周**能把框架跑通并复现「趋势」;但**要复现具体数字(尤其 40.2 / 37.8 这类低位数字)需要逐一调这 8 个未公开常数,可能需要数月**。

---

## 应用与行业映射(本项目强制要求)

### 1. 应用方向

**先说结论:受益最大的不是「最需要智能」的场景,而是「任务结构固定但输入会漂移」的场景。** 原因是本文框架的能力边界非常明确 —— 恢复器只覆盖 **pick / place 两个相位**、只支持**直接锚点**目的地、**不做旋转补偿**。

| 场景 | 受益度 | 判断依据(来自论文) |
|---|:---:|---|
| **仓储 / 物流分拣** | ⭐⭐⭐⭐ | **物体位置漂移是仓储常态**(料箱、传送带上件、堆垛误差)。FIT-MAC 在 Pos 扰动下收益最大(Object **93.4%**、Spatial **40.2%**),恢复流程正是「找到正确实例 + 抓起来 + 放到正确位置」 |
| **服务场景(酒店 / 医院 / 前台)** | ⭐⭐⭐⭐ | **指令改写 + 物品摆放随机** = Task + Pos 双扰动,而这正是基线归零(0.0%)而 FIT-MAC 拉回到 87.2% / 37.8% 的两类。恢复器是纯几何抓放,与语言无关,**鲁棒性不依赖更强的 LLM** |
| **工业装配 / 上下料** | ⭐⭐⭐ | 受益于「物品来料位置不定」;但 ⚠️ **装配本身(插入、对准、旋拧)不在恢复器覆盖范围** —— 只覆盖「取件 + 放置」段 |
| **特种 / 半结构化环境** | ⭐⭐ | 位置漂移收益真实存在;但 **Env 扰动在 Object 套件上只有 48.8%**,且**零真机验证** —— 特种场景恰恰最需要真机证据 |
| **家庭 / 长时程整理** | ⭐⭐ | 论文自己把「long-horizon」列为**未来工作**;恢复器每次只处理一个子任务,**长时程 = 恢复器被反复调用的累积可靠性问题,论文未测** |
| **医疗 / 精密操作** | ⭐ | **不适合**。旋转命令恒为 0、无力控、无接触检测、零安全讨论 |
| ❌ **不适用** | — | 需要旋转对齐 / 工具使用 / 铰接 / 柔性物体 / 多步长语义任务的场景 |

**「谁会因为这套框架受益」的直接回答**:
- **最直接受益的是 VLA 基座的使用者**,而不是 VLA 的开发者。FIT-MAC 明确「不修改基座」,所以一个已经训好 / 选好 OpenVLA / π0 的团队,**可以零训练加一层运行时加固**。这降低了「要不要换底座」的决策成本。
- **最直接的受益者是「基线会归零」的场景主**。Table 1 里 5 个 0.0% 的格子意味着:**在这些条件下,今天最主流的开源 VLA 方案是不可用的**,而 FIT-MAC 把其中几个拉回到 87%–93%。**这是「从不可用变成可用」的跨越,而不是「从 90% 变成 95%」的精修。**

### 2. 行业玩家

| 公司 | 对应产品线 | 与本文的关系 | 谁会受益 / 谁会用 |
|---|---|---|---|
| **Physical Intelligence** | **π0 / π0.5** | **本文两个受测 backbone 之一** —— 论文直接证明「运行时加固层」可插在 π 系列之上而不改权重 | 🔑 **最可能的商业形态:把 FIT-MAC 类运行时层做成 π 的授权增值模块**。PI 的商业模式本就是「π 基础模型授权」,**一个不改动模型、只增强鲁棒性的插件层,是它最自然的收费位** |
| **NVIDIA** | **Isaac Lab / GR00T / Jetson–Orin** | ⚠️ **同时是基座供应方、仿真平台方、边缘算力方** —— 本项目 §11.2 已把 NVIDIA 列为「最需要交叉验证的一家」 | 🟡 **受益方也是约束方**:多智能体运行时把推理算力需求从「1 个 VLA」抬到「VLA + 检测器 + VLM」,**能否塞进 Orin 级别边缘模组,是这套方案唯一的生死线,而论文没测延迟** |
| **Unitree(宇树)** | **G1 / H1** | 本项目 §13.2 已把宇树记为「多机器人协作赛道的默认科研载体」;G1 的成本结构使「加一层加固」的边际成本很低 | 🟢 **最可能的第一批真实用户**:本体便宜、量已成规模、学术界拿来做通用操控底座。**但 G1 的算力余量能否同时跑 VLA + Grounding DINO + VLM,需实测** |
| **AgiBot(智元)/ Fourier(傅利叶)** | 智元 A2 / GR-2 等国产人形 | 走「全栈自研」路线(本项目 §1.1) | 🟡 **最可能自建同类层,而不是采购第三方**。对它们而言,FIT-MAC 的价值更多是**方法论参照**而不是产品组件 |
| **Figure AI** | **Figure 02 / Helix VLA** | 走「自研 VLA + 自研全栈」 | 🔴 **最不可能直接采用**。**但 Figure 面对的问题和本文一模一样** —— Helix 跑飞了怎么办?因此本文对 Figure 的价值是**问题定义的参照**,而非可采购的组件 |
| *(参照)* **Skild AI** | Skild Brain | 定位「通用机器人大脑」 | 🟡 **边界竞争者**:若「大脑」定位包含运行时监督,FIT-MAC 式的监控层就是其职责范围的一部分 |

> 📌 **与本项目 §13.2「编排层归基础模型,技能层归电机策略」的对齐判断**:FIT-MAC 是**单机器人 VLA 场景下**的同一个分层逻辑 —— **编排 / 监控层可以独立于技能层(VLA)交付**。本文的「execution correction」正好落在技能层(手写几何抓放),「target correction」落在编排层(语义 grounding)。**分层结论在两个场景(多机协作 / 单机 VLA)上得到一致印证,这是本报告认为本文除数字外最值得记录的行业价值。**

### 3. 替代方案

| 方案 | 成本量级 | 性能特征 | 与 FIT-MAC 的对比 |
|---|---|---|---|
| **传统模块化感知-规划栈**(Grounding DINO / SAM + 位姿估计 + 规划 + 抓取控制,全手写规则) | **软件零采购成本 + 已有工控算力**;工时成本高 | 确定性强、可解释、**可过安全认证**;但**不处理语义歧义**(「不是盘子和小碗之间的那个碗」要靠规则硬写) | 🔴 **这是最危险的对照,而论文没做。** 本报告的读解是:**FIT-MAC 的增益主体(去掉 execution correction 掉 38.4 点)本质上就是「一个手写几何抓放兜底」**,而传统栈能提供同样的兜底且**零 LLM 成本、零延迟开销、确定性可认证**。**FIT-MAC 相对传统栈的净增量,论文未测。** |
| **扰动鲁棒训练 / 后训练**(论文引用的 Guo+ 2026、Zhang+ 2025a、Islam+ 2026、Sun+ 2026 路线) | **训练算力高**(本项目已收录 Spark-0 为 96 GPU × 400k 步量级 ⚠️ 该数字来自本项目行业格局 §12.1,非本文) | 部署期**零额外开销**;但每种新扰动都要重训,**组合爆炸** | 🟢 **部署成本优于 FIT-MAC**。FIT-MAC 的优势是「不重训就能应对没见过的扰动组合」;劣势是**每次执行都要付运行时开销** |
| **控制器兜底**(阻抗 / 力控 + 固定重试) | 增量硬件(力矩或电流传感)+ 调参工时 | **只能解决 execution failure,解决不了 target-binding 错误** | 🔴 **这正是论文论证的靶心** —— 论文的核心贡献就是证明「只会兜底执行失败」不够 |
| **置信度阈值 / OOD 检测 + 统一重试** | 几乎零 | 知道「不在分布内」,**但不知道是哪类失败** | 🔴 **论文的立论直接针对这一类**:统一重试在目标绑定错误上必然重复错误绑定(附录 B.3 左案例) |
| **人工接管 / 遥操作** | **人力工时成本,量级远高于以上全部** ⚠️ **论文未给出,此为基于公开量级的估计** | 能解决一切(人能看到一切),但**不可规模化** | 🔴 **在 Spatial 的 Task 扰动上,基线 0.0% 意味着 100% 的回合都需要人 —— 这正是本文试图消除的成本项** |
| **VLA + 只做 grounding 重绑定(不做执行恢复)** | 中等(一次 VLM 查询) | 对应消融「w/o execution correction」:**平均 54.7%**(Object 47.0 / Spatial 62.4) | 🟡 **一个折中方案**:放弃最贵的那部分,只保留语义修正。**这可能是性价比最高的工业落点**,论文的消融数据恰好给了这个选择的量化依据 |

> **成本小结(诚实版)**:FIT-MAC 的**增量硬件成本为零**(无新传感器),**增量软件成本 = Grounding DINO + 一个 VLM + 运行时状态机**;**但增量算力与延迟成本未知(论文未给出)**。相对「扰动鲁棒训练」路线的核心优势是**免训练**;相对「传统模块化栈」的核心劣势是**多了一个不可预测时延的 VLM 调用与一个不可验证的 LLM 决策**。

### 4. 量产壁垒

| 环节 | 状态 | 卡点 |
|---|---|---|
| **硬件成本** | ✅ **零增量** | 无新传感器、无新执行器。**这是本框架相对「加传感器」路线的最大优势** |
| **训练数据** | ✅ **零需求** | 完全免训练,基座冻结。**这是本框架相对扰动鲁棒训练路线的最大优势** |
| **可靠性** | 🔴 **硬卡点** | **Spatial Pos / Task 的 RSR 仅 41.3% / 35.5%** —— 即**被干预的回合里,近六成仍然失败**。**装上框架 ≠ 变可靠。** 附录 B.3 右案例直接说明:**目标对了但抓不住,系统无解** —— 恢复器只能重试抓取,改变不了抓取的物理可行性。**量产需要的是「连续 10 万次不掉球」,本文离这个量级有几个数量级** |
| **推理算力与延迟** | 🔴 **最硬的未知** | **论文零数据**。VLA + Grounding DINO + VLM 三件套能否同框部署在 Jetson Orin 级别边缘模组上,取决于 VLM 尺寸 —— **而论文没说是本地 VLM 还是 API**。⚠️ **若走 API,则引入网络依赖 + 延迟抖动 + token 成本 + 数据外传合规问题(工厂场景尤其敏感)**。对照本项目 §12.1:「实时已是准入门槛,门槛按部署算力划线」—— **本篇没有跨过这条线** |
| **安全认证** | 🔴 **空白** | 恢复器会在「已经抓歪」时接管并**直接下压**($a_t^{\mathrm{rec}}$ 只有位置命令 + 夹爪命令,**无力度上限**),且**旋转恒为 0**(意味着侧向碰撞时不会调整姿态)。论文**完全没有安全章节**。⚠️ **对照本项目 §4 的 ISO 10218 / ISO/TS 15066 / 欧盟 AI Act:一个含 LLM 决策、时延未知、力度无上限的运行时层,目前不具备可认证性。** |
| **标定 / 产线一致性** | 🟠 **可缓解但非零** | 论文的 4 个超参敏感性极低(Avg 变动 ≤ 0.3 点)—— **这是好消息**;但 8 个未公开的检测阈值常数($\tau_{\cdot}, W_{\cdot}, T_{\cdot}, \lambda_z, \bm{s}$)需逐产线/逐任务调。**好在它们数量有限,且论文证明了对这 4 个主超参不敏感** |
| **可维护性** | 🟡 **未讨论** | 依赖 Grounding DINO + VLM 两个外部组件的版本稳定性;**VLM 换版本就可能改变 target failure 的判定** —— 这是一个**没有回归测试基座就无法管理的依赖** |
| **⚖️ 最卡的那一环** | —— | 🔴 **不是算法,是「延迟与成本的未知」+「RSR 只有 35%–41%」。** 即使这两个问题都解决,本文的恢复器也只覆盖 pick-place,**离通用的长时程执行还差一个数量级** |

### 5. 时间窗估计

- **1 年内(2026-10 → 2027-10)**:🟡 **技术验证可行,产品化不可行**。
  - **可落地的形态**:**(a) 高校与研究机构的鲁棒性评测工具** —— LIBERO-PRO 已开源、OpenVLA 已开源、框架零训练,一个团队完全能自己复现趋势;**(b) OpenVLA 生态的「鲁棒性插件」实验分支**;**(c) 固定 pick-place 任务的夜间批处理作业**(不要求交互实时性,是延迟约束最松的场景)。
  - **不可落地**:任何有实时性要求的客户场景 —— **因为延迟数据都不存在,没人能承诺 SLA**。
  - **触发条件(可核查)**:① 出现一个**公开可核验的仓库**(当前的匿名 artifact 链接不算);② **论文或后续工作给出端到端延迟与每回合 VLM 调用数**;③ 出现 ≥1 次**真机**验证。

- **3 年内(2027-10 → 2029-10)**:🟡 **窄场景可试点,但需要一次关键的范式转换**。
  - **最可能的第一个商业场景**:🔵 **仓储 / 物流的「来料位置不定」的分拣与上下料** —— 理由:(a) **Pos 扰动是仓储的常态而非扰动**;(b) 恢复流程(找到正确实例 → 抓 → 放到正确位置)**与仓储任务天然同构**;(c) 该场景的 ROI 模型简单(减少人工干预次数)。
  - **但必须先完成三件事**:① **把 VLM 蒸馏/降级成边缘可跑的轻量判别器**(这几乎必然会发生 —— LLM 不会进 Orin);② **把「VLA + 脚本兜底」的对照做实,证明多智能体净贡献 > 0**;③ **RSR 从 35%–41% 提到 90%+**(否则收益不足以覆盖系统的复杂度)。
  - **价格预期**:⚠️ **论文未给出,本报告也不做金额预测**。**可预期的是成本结构而非价格** —— 增量硬件为零,增量成本落在**边缘算力(VLM 的尺寸决定)+ 集成工程**;⚠️ **若最终形态是「边缘 VLM + 确定性状态机」,它的成本结构会非常像今天的机器视觉方案(一次性 NRE + 单机 BOM 增量)**,而不是像 SaaS 式的持续 token 成本。

- **5 年内(2029-10 → 2031-10)**:🟢 **「多智能体 LLM 闭环」会退场,「确定性运行时监督层」会留下**。
  - **本报告的判断(明确标注为本报告推断)**:五年后,产业上留下的**不会是四个 LLM agent 在环**,而会是一套**确定性的运行时监督层**:硬编码的失效检测 + 一个小型视觉判别器 + 一张恢复策略表。**理由有三**:
    1. **延迟与可认证性**:LLM 在安全关键路径上无法过认证(不可预测时延 + 不可复现输出);
    2. **成本结构**:按 token 计费的开销无法与「一次性 NRE + 边缘算力」竞争;
    3. **本文自身的实现已经指向这个方向** —— 诊断是确定性的(式 2–6)、LLM 在 Planner/Verifier 中是 optional、恢复器是无学习的几何 P 控制器。**本文的「多智能体」是壳,「确定性状态机 + VLM 消歧」是核。**
  - **真正的产业影响不在这篇论文的数字,而在它给出的问题定义**:**「VLA 跑飞了怎么办」会被行业当作一个独立的、可采购的、跨基座可插拔的层来做。** 这与本项目已收录的 CoEvolve(编排层归基础模型)、TANDEM、GTA-VLA 等构成**同一条产业线索**。
  - **潜在颠覆性**:🟡 **有限**。这一层提高的是**可用性下限**(把 0% 拉到 40%–90%),不是**能力上限**;它不会让机器人做更难的事,只会让它们**在已经接近的条件下不掉链子**。**真正的颠覆仍然要靠更好的基座 VLA 和更好的数据,而不是靠运行时打补丁。**

---

## 横向对比:同项目已收录 VLA / 运行时鲁棒性路线

| 方法 | 核心思路 | 是否需训练 | 推理开销是否报告 | 开源 / 可核验 | 与 FIT-MAC 的关系 |
|---|---|---|---|---|---|
| **FIT-MAC(本文)** | 冻结 VLA + 四 agent 运行时闭环(目标重绑定 / 有界几何抓放恢复) | ❌ **免训练** | ❌ **完全未报告** | 🟡 匿名 artifact 链接 | — |
| [[CoEvolve_2610.23288_研读报告\|CoEvolve]](2610.23288) | 多机器人协作的编排层 / 技能层分离 | — | — | 🔴 仓库 404(本项目 §13.4 实测) | **同一分层逻辑的多机版本**;本文的「编排层可独立交付」结论与之互证 |
| [[FastVLA_2610.22146_研读报告\|FastVLA]](2610.22146) | 推理加速 / 自适应 token 预算 | — | ✅ **报 token 消耗与预算匹配对照** | ✅ 有真代码 | **方法论对照面**:FastVLA 证明「报告开销」可行,FIT-MAC 却完全没报 —— **同一项目内两种报告文化的对比** |
| [[Spark0_2610.22342_研读报告\|Spark-0]](2610.22342) | 大规模触觉预训练 + 视觉蒸馏 | ✅ 96 GPU × 400k 步 | — | ✅ | **互补面**:Spark-0 提高「抓得住」的物理能力,FIT-MAC 解决「跑飞了怎么办」—— **本文 RSR 只有 35%–41% 的根因,正是 Spark-0 那一侧的问题** |
| [[BlindBaoding_2610.23438_研读报告\|BlindBaoding]](2610.23438) | 触觉 + 域随机化,零样本真机迁移 | ✅ 需 Isaac Lab 训练 | — | 🔴 无仓库 | **交叉点**:FIT-MAC 的检测器全靠视觉几何,**在遮挡 / 接触密集场景会失效**;触觉正是那个缺失的信号 |
| [[TANDEM_2610.28314_研读报告\|TANDEM]](2610.28314) | 层级推理 + 全局-局部恢复 | — | — | — | **同类问题**(长时程恢复),但走的是「策略内部」路线,FIT-MAC 走「策略外部」路线 |

---

## 概念关联

- 本项目「VLA 鲁棒性 / 失败恢复」概念线 —— 本文是该线上**第一篇把「失败类型」显式分类并据此路由恢复**的论文(此前收录的 RACER / COME-robot / TCoT / SAFE 均以论文引用的形式出现,本文是本项目首次收录一篇以「**目标绑定错误 vs 局部执行失败**」为轴的)。**建议把「失败分类学」作为一条独立概念线建立。**
- 本项目「推理开销-效果分离」维度 —— 本文给出 IR / RSR 三元组,与 FastVLA 的 token 预算、Spark-0 的算力档位构成**三种不同形式的同维度披露**。📌 **建议固化为常设核查项:任何声称「推理期增强」的方法,必须同时报告「增强的开销」** —— 本文是这条规则的反面样本(自己开了先例却没执行)。
- 本项目 §13.2「编排层归基础模型,技能层归电机策略」 —— 本文在**单机 VLA 场景**给出同构证据:**编排层(grounding / 诊断 / 路由)可独立于技能层(VLA + 几何恢复)交付**。**两个场景指向同一结论,证据强度上升。**
- 本项目 §12.1「实时是准入门槛,按部署算力划线」 —— 本文是这条判据的**反例样本**:把「推理期闭环」当核心贡献,却完全没有部署算力与延迟数据。**建议把「延迟/算力缺失」单列为一条负向观察维度。**
- arXiv:<https://arxiv.org/abs/2610.28109v1>
- ⚠️ **代码可用性**:项目页 `https://fitmac-research.pages.dev/` + 匿名 artifact `https://anonymous.4open.science/r/research-artifact-B431`(**非公开 GitHub,本报告未联网核验**)。
- ⚠️ **全文本报告中唯一未定的关键项**:**主表(1–3)所用配置中,Verifier 的 optional 语言模型评估是否启用、Planner 用规则 fallback 还是 LLM** —— 论文未声明,直接影响成本与延迟的估计。
