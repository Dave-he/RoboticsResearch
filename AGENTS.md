---
title: AI Agents 协作规范
tags: [agent, workflow, automation, robotics]
date: 2026-06-07
---

# 🤖 RoboticsResearch 的 AI Agent 协作规范

本项目采用与 [LNN 项目](../LNN/AGENTS.md) 相同的「Living Field Researcher」范式,把每日抓取 → 研读报告 → 全局索引 → 行业映射做成可持续滚动的闭环。

## Agent 角色

### 1. 📄 Paper Tracker Agent (论文追踪)
- **目标**:每日监控 arXiv、GitHub、官方博客,获取机器人技术最新进展
- **职责**:
  - 基于 `configs/keywords.yaml` 检索 `cs.RO`、`cs.AI`、`cs.CV` 等分类
  - 自动落盘原始 JSON 到 `papers/daily/`
  - 生成人类可读摘要到 `docs/daily/`

### 2. 📝 Summarization Agent (研读报告生成)
- **目标**:对每日摘要中 `read_now` 的论文生成结构化研读报告
- **职责**:
  - 解析 PDF 或 arXiv 摘要
  - 按 SOP 输出到 `docs/reports/<slug>_研读报告.md`
  - 必含模块:元数据 / 核心问题 / 方法论 / 核心公式 / 关键成果 / 局限性 / 复现线索 / **应用与行业映射**

### 3. 🏭 Industry Mapping Agent (行业映射)
- **目标**:把论文中的方法映射到具体公司 / 产品 / 成本结构
- **职责**:
  - 维护 `docs/机器人行业格局与产业链.md`
  - 对每篇高价值论文标注:可能受益的厂商、替代方案、量产成本量级

### 4. 🔄 Loop Reviewer Agent (循环优化)
- **目标**:每周 / 每月审视 protocol,迭代关键词和筛选规则
- **职责**:
  - 统计漏检 / 误报,调整 `configs/keywords.yaml`
  - 更新种子集合与研究范围
  - 合并重复的概念笔记

## 工作流

```
[每日] 抓取 → 去重 → 评分 → 摘要 → Top3 去重已读
   ↓
[每日] 选 1-3 篇 read_now,生成研读报告
   ↓
[每周] 周报:跨论文主题洞察 + 行业格局增量 + 下轮必查
   ↓
[每月] 迭代:关键词 / 数据源 / 协议
```

## 与 LNN 项目共享的 Skill

- `skills/living-field-robotics-researcher/` 是本项目的"领域研究"专用 Skill
- 参考但不复用 LNN 的 `living-field-researcher` 完整模板
- 核心区别:本项目在研读报告 SOP 中强制加入「应用与行业映射」段落

## 当前已落地

- 仓库骨架 ✅
- 机器人研究协议 ✅(`docs/机器人研究协议.md`,§10 变更日志)
- 每日抓取管线 ✅(`scripts/daily_robotics_research.py` + systemd timer + GitHub Actions)
- 已研读论文登记与 Top 3 去重 ✅(2026-10-20,`load_read_arxiv_ids`)
- 全局索引主表自动重建 ✅(`scripts/build_report_index.py`,`--check` 可进 CI)
- 研读报告 **34 份** ✅(`docs/reports/`,覆盖 14 个研读日)
- 周报 W40–W43 ✅(`docs/research/<YYYY>-W<WW>_周报.md`)
- 月度合成 2026-07 / 08 / 09 / 10 ✅(`docs/research/<YYYY>-<MM>_robotics_synthesis.md`)
- 行业格局 §1–§13 ✅(`docs/机器人行业格局与产业链.md`)

## 已知待办

- [ ] **周期产物仍无自动门禁** —— 周报/月度合成的存在性检查仍是人工的;2026 年 7–9 月曾连续两个月断档而无告警(见 `docs/research/2026-08_robotics_synthesis.md`)。**这是当前最大的结构性风险**
- [ ] `docs/reports/X2N_2604.21541_研读报告.md` 与 `X2-N_2604.21541_研读报告.md` 为同一篇论文的重复文件,需合并
- [ ] 每日抓取的 GitHub 仓库数在部分日期明显偏低(10-14/10-15 为 58,10-20 为 47),需排查是否为 API 限流
- [ ] 2026-08 缺失 2 天抓取,原因未查
