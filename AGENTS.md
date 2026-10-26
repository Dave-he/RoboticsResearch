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
- **周期产物门禁** ✅(`scripts/check_periodic_artifacts.py` + `configs/periodic_gate.yaml` + `.github/workflows/periodic-artifacts-gate.yml`)
  - 存在性:每日抓取连续性 / 周报 / 月度合成
  - **内容契约**:周报与月度合成必须满足最小正文行数 + 至少 1 个表格 + 4 项必需内容(数据统计 / 研读清单 / 主题洞察 / 后续行动),**空壳产物无法通过**
- GitHub 配额感知 + 抓取诊断字段 ✅(`diagnostics` 写入每日 JSON,部分抓取在 digest 顶部显式告警)
- **综述筛选修复 + 归档路径建立** ✅(2026-10-26,`is_survey()` 修订 + **新建 `docs/research/surveys.md`**)
  - 旧规则漏判 `Annual Review` 综述(2610.30438 标题用 "Perspectives"、摘要用 "This paper reviews"),该综述**连续 3 天占据 Top 3 第二位**,挤掉同期方法类论文
  - 修订后:**标题补 perspective/tutorial/primer + 摘要补自述式综述短语 + Annual Review 期刊线索**,**并排除「评审流程」假阳性**(2610.31427 FastHarness 的 "Review Scheduling" 指复核策略动作块,非文献综述)
  - 附带修复:`update_global_index()` 补综述排除(与 digest 口径对齐);`--render-only` 补全局索引更新(此前遗漏,导致规则变更后索引残留旧 Top 5)
  - ⚠️ **教训**:协议 §4 的综述归档出口**空了三个多月无人察觉** —— 门禁只查产物存在、不查规则是否生效
- 研读报告 **40 份** ✅(`docs/reports/`,覆盖 16 个研读日;2026-10-26 批次 +3:COWBOY / SP-HLM / AtomicRL)
- 周报 W40–W44 ✅(`docs/research/<YYYY>-W<WW>_周报.md`;**W43 全周补齐(4 批次 / 13 篇)**,**W44 已开(第 1 日)**)
- 月度合成 2026-07 / 08 / 09 / 10 ✅(`docs/research/<YYYY>-<MM>_robotics_synthesis.md`)
- 每日抓取连续性 ✅(2026-08-06 / 08-26 两天已从悬空提交找回并补齐)
- 行业格局 §1–§15 ✅(`docs/机器人行业格局与产业链.md`;**§15 为 2026-10-26 批次洞察**:分层架构 / 零代码反转 / 语义结构化 RL)

## 已知待办

- [ ] **GitHub Search API 限额未根治** —— 未认证限额 10 次/分,脚本已做配额感知 + 重试 + 诊断记录,但**配置 `GITHUB_TOKEN` 后限额升至 30 次/分**才是根治。⚠️ **W43 后 5 天零失败,但根因未解**
- [ ] **HF Search 自 2026-10-24 起连续 3 天 `models=0`** —— 与 GitHub 无关的独立异常(HF 是协议 §3 声明的第三方数据源)。📌 **归零持续即应视为异常**,需定位
- [ ] **历史每日 JSON 缺 `diagnostics` 字段** —— 门禁对 2026-10-20 之前的部分抓取只能标为「未知」;历史限流次数仅 `logs/daily_cron.log` 留有 13 次记录
- [ ] 每日抓取的 GitHub 仓库数在部分日期明显偏低(10-14/10-15 为 58,10-20 为 47)—— ⚠️ **已定位为 Search API 限流(非本地问题)**,详见 `logs/daily_cron.log` 与抓取脚本注释
- [ ] 门禁的**内容契约只覆盖周报 / 月度合成**,研读报告本体(8 个模块)尚无结构检查
- [ ] **「论文声称开源 vs 实际可得」的兑现率无监控** —— 📌 **2026-10-26 批次实测 3/3 零代码**(COWBOY 无仓库 / SP-HLM 仅项目页 / AtomicRL 无发布声明),且**基座层全部开源、方法层全部闭源**。建议在抓取侧增加该字段
- [ ] **协议条款 → 执行路径的月度对账** —— 📌 协议 §4 的综述归档出口此前从未走通;当前门禁**只覆盖每日抓取 / 周报 / 月度合成**,§4 归档、§9 行业映射段落等无产物级检查
