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
[每日] 抓取 → 去重 → 评分 → 摘要
   ↓
[每日] 选 1-3 篇 read_now,生成研读报告
   ↓
[每周] 月度合成:跨子领域对照表 / 概念笔记 / 行业动态
   ↓
[每月] 迭代:关键词 / 数据源 / 协议
```

## 与 LNN 项目共享的 Skill

- `skills/living-field-robotics-researcher/` 是本项目的"领域研究"专用 Skill
- 参考但不复用 LNN 的 `living-field-researcher` 完整模板
- 核心区别:本项目在研读报告 SOP 中强制加入「应用与行业映射」段落

## 当前已落地

- 仓库骨架 ✅
- 机器人研究协议 ✅
- `scripts/daily_robotics_research.py` ✅
- 首次手动抓取 + 摘要(运行后)⏳
- 第一份研读报告 ⏳
