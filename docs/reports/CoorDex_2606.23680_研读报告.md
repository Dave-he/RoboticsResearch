---
title: CoorDex 协调身体与手部先验的人形连续灵巧 loco-manipulation_研读报告
arxiv_id: "2606.23680v1"
date: 2026-06-26
subarea: humanoid
tags: [robotics, humanoid, dexterous-manipulation, loco-manipulation, residual-rl, latent-prior, sim-to-real, unitree-g1, wuji-hand]
---

# CoorDex: Coordinating Body and Hand Priors for Continuous Dexterous Humanoid Loco-Manipulation

> **作者**:Sikai Li, Shuning Li, Zhenyu Wei, Yunchao Yao, Chenran Li, Mingyu Ding
> **机构**:**UNC Chapel Hill** · **UC Berkeley**(Sikai Li 同时属二)
> **通讯作者 / 一作**:Sikai Li(`skevinci`);Mingyu Ding 教授组
> **发表**:2026-06-22 · arXiv: 2606.23680v1 · cs.RO, cs.AI, cs.LG
> **本报告状态**:首次入册,基于摘要 + 项目页 `https://skevinci.github.io/coordex/` 整理(项目页有真实与仿真视频)

## 元数据

- **arXiv ID**:[2606.23680v1](https://arxiv.org/abs/2606.23680v1)
- **作者**:Sikai Li(UNC + UC Berkeley), Shuning Li, Zhenyu Wei, Yunchao Yao, Chenran Li, Mingyu Ding(UNC Chapel Hill)
- **机构**:UNC Chapel Hill(Department of Computer Science) · UC Berkeley
- **发表时间**:2026-06-22
- **会议 / 期刊**:预印本(待投 RSS / ICRA / CoRL)
- **项目页**:<https://skevinci.github.io/coordex/>
- **代码**:<https://github.com/Skevinci/CoorDex>(已公开)
- **PDF**:[link](https://arxiv.org/pdf/2606.23680v1)
- **仿真平台**:Isaac Lab(NVIDIA)

## 核心问题

**人形机器人的"locomotion + 灵巧操控"耦合**是行业最关心、也最难落地的一类任务。当前两条主流路线都有结构性问题:

1. **"stop-and-go"范式**:人形走到目标前停下来 → 操控 → 再继续走。问题在于真实环境(工厂、超市、家居)**根本不允许"停下来"**——一辆 8 km/h 的传送带不会等你。
2. **"低自由度夹爪当末端"范式**:把人手型灵巧手换成 1-DoF 开合夹爪,虽然控制简单,但 80% 的"开柜门 / 拧瓶盖 / 插软管"等接触丰富任务被直接排除。

**根因诊断**:学界此前的工作普遍把**全身控制和手部控制当成两个独立模块**分别训练(上半身 PPO + 下半身 PPO + 手部模仿学习),但在**运动中操控(moving while manipulating)**这一场景下,身体与手的耦合动力学(手臂摆动对手指接触的扰动、CoM 偏移对手指定位的影响)**让这种解耦方式学不到可部署的策略**。

**核心视角**:**身体和手部必须共享一个"任务上下文"** —— 不是独立学两套策略,而是学一个**协调式残差(coordinated residual)**叠加在**解耦先验(latent prior)**之上。先验负责"会走路 + 会抓握",残差负责"在走路中调整手指以保持接触"。

## 方法论与核心思路

### 整体框架

```
+--------------------------------------------------+
|              Stage 1 · Teacher Policy            |
|  Whole-body motion tracking teacher (privileged) |
|  + Hand motion tracking teacher (privileged)     |
|         ↓ 蒸馏 (privileged info → proprio only) |
+--------------------------------------------------+
|              Stage 2 · Latent Prior               |
|  Frozen body decoder + frozen hand decoder       |
|  (proprioception → latent → joint targets)       |
+--------------------------------------------------+
|              Stage 3 · Residual RL (PPO)          |
|  Shared task context  →  body residual head      |
|                      →  hand residual head       |
|         ↓ on top of frozen prior (composition)   |
+--------------------------------------------------+
|     Hardware: Unitree G1 + 7-DoF Dex3-1 (real)    |
|               G1 + 20-DoF Wuji (sim, Isaac Lab)  |
+--------------------------------------------------+
```

### 关键创新点 1:Latent-Prior Interface(先验作为动作空间)

不直接把 joint-space PPO 用在 30+ 个关节上(维度爆炸),而是:

1. 用 privileged motion tracking teacher 训出"理想身体轨迹"和"理想手指轨迹"
2. 把两个 teacher **蒸馏**成**仅依赖本体感觉(proprioception)的 latent prior**:
   - Body prior: $z_{\text{body}} = f_{\text{body}}(q_{\text{body}}, \dot q_{\text{body}}, \text{task ctx})$
   - Hand prior: $z_{\text{hand}} = f_{\text{hand}}(q_{\text{hand}}, \dot q_{\text{hand}}, \text{task ctx})$
3. **冻结(freeze)这两个 prior**,把它们作为**动作空间(action space)**

这样下游 RL 只需要学"如何在 prior 之上加残差",搜索空间从 30+ 维压到 latent 维(通常 4-8 维)。

### 关键创新点 2:Coordinated Residual Policy(协调式残差)

残差头有两个:

$$
\Delta a = \underbrace{\pi_{\text{body}}(z_{\text{body}}, c)}_{\text{body residual}} \oplus \underbrace{\pi_{\text{hand}}(z_{\text{hand}}, c)}_{\text{hand residual}}
$$

其中 $c$ 是**共享的任务上下文(shared task context)**——比如"目标物体位置 + 当前任务阶段"。这个共享 context 是关键:

- 让身体和手**同时看同一份任务信息**,避免两套策略各做各的
- 身体走偏时,手部会"知道"——而独立训练的两个 PPO 不会

### 关键创新点 3:三个接触丰富任务的成功演示

- **Walk-grasp-carry**:运动中抓取瓶子(经典 contact-rich 任务)
- **Fridge-door open on the move**:边后退边打开冰箱门
- **Cube pick-and-turn**:运动中取起并转动立方体

所有任务**禁止 stop-and-go**,要求"边走边做"。

### 与已有方法的本质区别

| 方法 | 身体-手耦合 | 动作空间 | 实际效果 |
|---|---|---|---|
| 独立 PPO × 2 | ❌ 解耦 | joint-space(30+ 维) | 同 budget 学不到 |
| Monolithic latent | ❌ 共享一个 latent | latent(单头) | 任务结构模糊 |
| **CoorDex** | ✅ 共享 task ctx + 分头残差 | 解耦 latent prior + residual | **唯一 trainable** |

## 核心公式提取

### 1. 协调残差

$$
a_t = a^{\text{prior}}_t + \underbrace{\pi_{\theta}\left(z^{\text{body}}_t, z^{\text{hand}}_t, c_t\right)}_{\text{协调残差}}
$$

### 2. Latent prior 蒸馏(用行为克隆拟合 teacher)

$$
\mathcal{L}_{\text{distill}} = \mathbb{E}_{(s,a^*) \sim \pi_{\text{teacher}}} \left[\| \underbrace{D_{\text{body}}(f_{\text{body}}(s))}_{a^{\text{prior}}_{\text{body}}} - a^*_{\text{body}} \|^2 + \| D_{\text{hand}}(f_{\text{hand}}(s)) - a^*_{\text{hand}} \|^2 \right]
$$

### 3. 下游 PPO 目标(在 latent 残差上)

$$
\max_{\theta} \; \mathbb{E}_{\tau \sim \pi_{\theta}} \left[ \sum_t \gamma^t r_t(s_t, a_t) \right], \quad a_t = a^{\text{prior}}_t + \pi_{\theta}(\cdot \mid z_t, c_t)
$$

**符号解释**:
- $a^{\text{prior}}_t$ —— frozen decoder 输出的关节目标
- $z^{\text{body}}_t, z^{\text{hand}}_t$ —— 解耦的本体条件 latent
- $c_t$ —— 共享任务上下文(目标位姿 + 阶段嵌入)
- $D_{\text{body}}, D_{\text{hand}}$ —— frozen decoder
- $r_t$ —— 接触奖励(抓握稳定度) + 任务奖励 + 平滑奖励

## 关键成果与贡献

作者通过 **Walk-grasp-carry** 的消融证明 latent-prior interface + coordinated residual 是关键:

| 方案 | 结果(同 PPO budget) |
|---|---|
| Joint-space PPO(全关节 30+ 维) | ❌ 不收敛 |
| Joint-space 身体 + 独立手 PPO | ❌ 不收敛 |
| Monolithic single latent | ❌ 接触频繁失败 |
| **CoorDex(full)** | ✅ 任务完成 |

- 仿真:在 Isaac Lab 中 Unitree G1 + 20-DoF Wuji 手上完成 3 类任务(视频佐证)
- 真机:在 Unitree G1 + 7-DoF Dex3-1 灵巧手上展示 Walk-grasp-carry、Fridge open on the move、Cube pick-and-turn(项目页有视频)
- **未在摘要/项目页公布具体成功率数字**——这是后续阅读论文全文时需要补的实验细节

## 局限性与未来展望

**作者自述 / 项目页可推断**:

1. **任务规模有限**:只展示了 3 类任务,没有覆盖"边走边折叠衣服 / 边走边插 USB"等更复杂的日常任务
2. **仿真与真机硬件不一致**:sim 用的 20-DoF Wuji 手,真机用 7-DoF Dex3-1 — 这意味着 latent prior 不能直接迁移,需要重新蒸馏
3. **依赖 privileged teacher**:teacher 在 sim 里要 ground-truth 状态,真机没这套信息,所以 teacher→prior 这步必须做 sim-to-real,但论文没说具体怎么处理

**我们阅读发现的潜在问题**:

- Latent prior 是 frozen,理论上能"学"的任务受限于 prior 表达力。如果 teacher 自己都学不会(比如特别别扭的物体),CoorDex 也没救
- 协调残差需要"任务上下文"输入,意味着需要外部感知(目标检测)来给 $c_t$ 喂信号
- 与 VLA 模型结合的可能性未在论文中讨论——目前还是 RL-only 范式

## 复现线索

- **代码**:<https://github.com/Skevinci/CoorDex>(已开源)
- **仿真**:Isaac Lab(NVIDIA),Unitree G1 URDF + 20-DoF Wuji 手 URDF
- **真机**:Unitree G1 + Dex3-1 灵巧手(7-DoF,因 G1 机械接口限制);需要 NVIDIA GPU 跑 Isaac Lab sim2real
- **数据**:完全在 Isaac Lab 中生成(无真实数据)
- **训练时长**:摘要未提供,根据 PPO + latent prior 规模,**估计 2-4 张 A100 训 24-48 小时**
- **依赖**:`isaac-lab`, `torch`, `rsl_rl`(PPO 实现)
- **复现难度评估**:**中**。代码已开 + 平台标准,但需要 Isaac Lab 完整安装 + 灵巧手硬件

## 应用与行业映射(本项目强制要求)

### 1. 应用方向

- **工业搬运 / 物流分拣**:流水线不停,机器人要边走边抓边放
- **零售 / 仓储**:货架之间移动,边走边取商品
- **服务机器人**:酒店送餐、商场导览,边走边开门 / 按电梯
- **家庭**:边走边收桌面、边走边开门

### 2. 行业玩家

| 厂商 | 现有方案 | 受益方式 |
|---|---|---|
| **Unitree**(G1 / H1) | 自家 RL 框架,单步操控 | 直接套 latent prior + 协调残差 |
| **Figure AI**(Figure 02) | Helix VLA,stop-and-go | 加 residual head 即可迁移到 on-the-move |
| **1X Technologies**(Neo) | 类人手机器人 | 灵巧手 + 移动耦合问题与本方法强相关 |
| **Tesla**(Optimus) | 单手 11-DoF + FSD 风格网络 | latent prior 思路能降低训练成本 |
| **Physical Intelligence** | π0 系列 VLA | 把 VLA 当 teacher,CoorDex 当 residual |
| **Agility Robotics**(Digit) | 仓储为主,夹爪简单 | 短期不直接受益,但长期灵巧手要补课 |
| **Skild AI**(背后) | robot foundation model | latent prior 范式与"脑 → 小脑"分层一致 |

### 3. 替代方案

- **Stop-and-go + 高水平规划**:简单,但吞吐率低(单次搬运 > 30s)
- **双臂移动平台(TIAGo++ / Mobile Aloha)**:用移动底座 + 双夹爪代替人形,牺牲拟人性换 throughput
- **Whole-body VLA end-to-end**:Figure Helix 路线,但参数大、训练贵、数据需求高
- **CoorDex**:RL + 协调残差,可解释、可模块化、易插入

### 4. 量产壁垒

| 环节 | 当前状态 | 关键卡点 |
|---|---|---|
| **硬件** | G1 量产中,Dex3-1 小批量 | 灵巧手成本 > $5k,降不下来难普及 |
| **sim2real** | 仿真用 20-DoF Wuji,真机 7-DoF,需重新蒸馏 | 手部 URDF 跨厂商不通用 |
| **训练数据** | 纯 sim,无 real data | 长尾场景(打翻物体、液体等)靠 sim 难覆盖 |
| **安全 / 认证** | 高速运动中手与人共处 — 碰撞检测缺失 | 欧盟 CE / 中国 GB 标准的力矩限幅 |
| **能效** | 协调残差每步多 1 次网络前向 | 边缘部署需要蒸馏到 ≤ 5W |

### 5. 时间窗估计

- **1 年内(2026-2027)**:G1 + Dex3-1 的研究 demo 普及;走 + 抓的 3 类任务在受控环境(实验室、demo 视频)落地
- **3 年内(2028-2029)**:物流分拣 / 仓储场景小规模商业试点(单 SKU、固定路线);灵巧手成本有望降到 $2k
- **5 年内(2030)**:真正"边走边做饭 / 边走边叠衣"还需 5+ 年 — VLA + 协调残差 + 安全认证三者都要齐备

## 横向对比(可选)

| 方法 | 核心思路 | 身体-手耦合 | 训练数据 | 性能 | 开源 |
|---|---|---|---|---|---|
| **CoorDex** | Latent prior + 协调残差 RL | ✅ 共享 task ctx | Isaac Lab 仿真 | 3 类 on-the-move 任务 | ✅ |
| Figure Helix | 双系统 VLA(慢思考 + 快反应) | 隐式,end-to-end | 真实遥操 + 仿真 | 复杂桌面操控 | ❌ |
| Tesla Optimus | FSD 风格 end-to-end | 隐式 | 工厂遥操 | 工厂内搬运 | ❌ |
| π0 / π0.5 | 通用 VLA + flow matching | VLM → 关节 | Open X-Embodiment | 多任务 | 部分(权重) |
| UMI(机械臂版) | 手持 gripper + iPad 录数据 | N/A(机械臂) | 真实人类操作 | 桌面操控 | ✅ |

## 概念关联(可选)

- [[../机器人_深度研读报告.md#2026-06-17 自动更新|MuseVLA(2026-06-17 报告)]]—— 多模态感知 VLA,可与 CoorDex 的 prior teacher 结合
- [[../机器人_深度研读报告.md#2026-06-18 自动更新|T-Rex(2026-06-18 报告)]]—— 触觉反应,适合作为 hand prior 的额外输入
- **sim2real**(Zettelkasten 待建)—— CoorDex 是 sim2real 在"全身 + 灵巧手"场景的代表案例
- **residual RL** —— 经典工作:Residual Policy Learning (Johannink et al., 2019),CoorDex 是其在 latent 空间上的扩展
