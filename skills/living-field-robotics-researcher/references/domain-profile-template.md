# Robotics Domain Profile Template

Copy or adapt this into `docs/机器人研究协议.md` when a repository lacks an explicit protocol.

```markdown
---
title: <DOMAIN> 持续研究协议
date: YYYY-MM-DD
tags: [research-protocol, living-review, <domain-slug>]
---

# <DOMAIN> 持续研究协议

## 1. 范围与研究问题

- 领域名称:通用机器人技术
- 领域 slug:robotics
- 当前阶段:<广覆盖建库期 / 纵深期 / 应用期>
- 核心研究问题:<列出 3-5 个>
- 暂不纳入范围:<无人机 / 纯控制论 / 纯生物力学等>

## 2. 关键词与查询式

| 组别 | 关键词 | 用途 | 噪声风险 |
|---|---|---|---|
| 核心方法 | manipulation, grasping, sim2real, VLA | 发现主线论文 | 中 |
| 基础模型 | RT-2, OpenVLA, Octo, π0 | 跟踪 SOTA 模型 | 中 |
| 人形 / 仿生 | humanoid, bipedal, legged | 跟踪波士顿 / Figure / 1X | 低 |
| 感知 / SLAM | visual SLAM, NeRF, 3DGS, visual navigation | 跟踪感知前沿 | 中 |
| 硬件 | dexterous hand, tactile, force control | 跟踪硬件进展 | 低 |
| 仿真 / 数据 | Isaac Sim, MuJoCo, RT-X, DROID | 跟踪实验生态 | 低 |
| 行业玩家 | Figure, Optimus, 1X, Unitree, PI, Skild | 跟踪产业化 | 低 |

## 3. 数据源

| 数据源 | 访问方式 | 频率 | 输出位置 | 备注 |
|---|---|---|---|---|
| arXiv | API(cs.RO/cs.AI/cs.CV/cs.LG/cs.MA) | 每日 | papers/daily/ | 主力源 |
| GitHub | Search API(Stars ≥ 50) | 每日 | analysis/repo_watchlist/ | 关注新增 / 高活跃 |
| Hugging Face | Search API | 每周 | analysis/repo_watchlist/ | 跟踪 VLA 模型与数据集 |
| 官方博客 | RSS / 抓取 | 每周 | docs/research/industry_news/ | Figure / PI / Tesla / 1X / Unitree / Skild |
| arXiv 月度 | API | 每月 | docs/research/YYYY-MM_monthly_synthesis.md | 跨子领域合成 |

## 4. 纳入与排除规则

**纳入**:
- 标题或摘要命中核心关键词(标题 +5, 摘要 +2)
- 来自顶 lab 的任何 cs.RO 论文(自动 read_now)
- 出现于 GitHub Trending(机器人分类)
- 行业玩家的技术博客 / 发布说明

**排除**:
- 命中 noise_terms
- 纯综述无新方法(进入 docs/research/surveys.md 备查)
- 重复 / 旧版本(以最新版本 arXiv ID 为准)

## 5. 评分与优先级

| 信号 | 说明 | 权重 |
|---|---:|---:|
| 主题相关性 | 标题 / 摘要命中核心关键词 | 5 / 2 |
| 新颖性 | 是否提出新方法 / 新数据 / 新 benchmark / 新理论 | +3 |
| 影响潜力 | 作者机构、引用、Star、社区讨论 | +4 |
| 可复现性 | 是否有代码 / 数据 / 明确指标 | +3 |
| 行业落地潜力 | 是否有明确应用方向、量产可行性 | +3 |
| 时效性 | 30 天内发布 | +2 |

**优先级标签**:
- read_now:本日内必读
- watch:持续关注
- repo_analyze:仓库分析(不下载代码,只做评价)
- ignore:纳入但不深读

## 6. 输出约定

| 产物 | 路径 | 频率 |
|---|---|---|
| 原始 JSON 数据 | papers/daily/YYYY-MM-DD_robotics_research.json | 每日 |
| 每日人类可读摘要 | docs/daily/YYYY-MM-DD_robotics_research_digest.md | 每日 |
| 单篇研读报告 | docs/reports/<slug>_研读报告.md | 按需 |
| 全局索引 | docs/机器人_深度研读报告.md | 持续追加 |
| 仓库观察 | analysis/repo_watchlist/YYYY-MM-DD_robotics_repos.md | 每日 |
| 行业格局 | docs/机器人行业格局与产业链.md | 每周迭代 |
| 月度合成 | docs/research/YYYY-MM_robotics_synthesis.md | 每月 |

## 7. 迭代节奏

- 每日:抓取 → 摘要 → 选 1-3 篇 read_now → 生成研读报告
- 每周:汇总本周 read_now → 写一条到 docs/research/weekly_<year>_<week>.md → 维护 docs/机器人行业格局与产业链.md
- 每月:合成月度跨子领域观察 → 更新本协议(关键词 / 数据源 / 种子集合)→ 重写全局索引概览

## 8. 当前种子集合(Seeds)

### 8.1 必读论文种子

- RT-2(Google DeepMind 2023)—— 视觉-语言-动作模型的开山
- OpenVLA —— 7B 参数开源 VLA
- Octo —— 通用机器人 transformer 策略
- π0(Physical Intelligence)—— 通用机器人基础模型
- DreamerV3 —— 通用世界模型
- GR-1 / GR-2(ByteDance)—— 视频生成驱动的机器人策略
- 3D Diffusion Policy —— DP3,高效 3D 操控
- RDT-1B —— 双手操控的双臂机器人基础模型

### 8.2 必看仓库种子

- google-deepmind/mujoco
- NVIDIA/Isaac-GR00T
- openvla/openvla
- octo-model/octo
- Physical-Intelligence/openpi
- unitreerobotics/unitree_sdk2

### 8.3 必看行业 RSS

- Figure AI Blog
- Tesla Optimus 官方更新
- 1X Technologies Blog
- Physical Intelligence Blog
- Boston Dynamics Blog
- Unitree 官方

## 9. 应用与行业映射要求(本项目特殊约束)

**每个研读报告必须包含「应用与行业映射」段落**,回答:

1. **应用方向**:哪些场景受益最大?(工业 / 物流 / 服务 / 家庭 / 医疗 / 特种)
2. **行业玩家**:谁在做?谁会受益?(列出 3-5 家公司及对应产品线)
3. **替代方案**:现有方案是什么?成本量级?
4. **量产壁垒**:硬件成本、训练数据、可靠性、安全认证,卡在哪?
5. **时间窗估计**:论文方法距离量产落地 1y / 3y / 5y 的可行性

## 10. 协议变更日志

- YYYY-MM-DD:首版协议建立
```
