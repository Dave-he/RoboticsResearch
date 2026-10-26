---
title: 机器人综述与立场论文备查
date: 2026-10-26
tags: [surveys, robotics, reading-list]
protocol_ref: "机器人研究协议 §4(排除「纯综述无新方法」)/ §6(输出约定)"
---

# 机器人综述与立场论文备查

> **本文件的用途**:协议 §4 规定「**纯综述无新方法**」的论文**不进入深读流程**,而是「进入 `docs/research/surveys.md` 备查」。
> **在此文件建立之前(2026-10-26 之前),这个归档出口从未被真正使用过** —— 抓取脚本会把综述留在候选池里,综述因此会**占据 read_now 名额**,挤掉真正的方��类论文。
>
> ⚠️ **实证(2026-10-26 定位)**:`scripts/daily_robotics_research.py` 的 `is_survey()` 旧规则只匹配标题里的 `survey / review / overview of the literature`,以及摘要里的 `in this survey` / `we survey the` 两种开头式表述。
> 后果:arXiv **2610.30438**《Tactile-Based Robotic Manipulation: From Mechanics-Driven to Data-Driven Perspectives》(Annual Review of Control, Robotics, and Autonomous Systems, Vol. 10)因标题用 "Perspectives"、摘要用 "This paper reviews ...",**连续 3 天(10-24 / 10-25 / 10-26)占据 Top 3 第二位**。
> **同一时间窗里被挤掉的**:COWBOY(2610.28948)、SP-HLM(2610.30044)、AtomicRL(2610.30097)—— 这三篇已在本批次完成深读。
>
> ✅ **修订已完成(2026-10-26)**:`is_survey()` 增加标题的 perspective/tutorial/primer 词、摘要的自述式综述短语、以及 Annual Review 期刊线索;同时排除了「review 作为评审流程」的假阳性(实证案例:2610.31427 FastHarness 的 "Review Scheduling" 指评审策略动作块,不是文献综述 —— 该误判在旧规则下同样存在)。

---

## 归档条目

| 日期 | arXiv | 标题 | 刊物 / 类型 | 判定依据 | 主题价值 | 处置 |
|---|---|---|---|---|---|---|
| 2026-10-24 ~ 10-26 | [2610.30438](https://arxiv.org/abs/2610.30438v1) | Tactile-Based Robotic Manipulation: From Mechanics-Driven to Data-Driven Perspectives | **Annual Review of Control, Robotics, and Autonomous Systems, Vol. 10(2027)**;作者接受稿,30 页 | 标题 "Perspectives";摘要 "This paper reviews the development of tactile-based manipulation from these two complementary perspectives";arXiv comments 明确标注 Annual Review 期刊 | **高** —— 触觉操控的两条路线(力学驱动 vs 数据驱动)的系统性梳理,含模仿学习 / RL / VLA / 预测模型四类数据驱动方法 | **不深读,但列为强推荐备查**;触觉方向的标准参考综述 |
| 2026-10-23 ~ 10-26 | [2610.30108](https://arxiv.org/abs/2610.30108v1) | Multimodal Embodied Agents: A Unified Capability-centric Perspective from Computer-Use to Robot-Use | 立场 / 框架论文(提出 PAPAV 五功能框架) | 标题 "Perspective";摘要以 "We define multimodal embodied agents (MMEAs) as ..." 开头并提出统一分类框架 | **中高** —— 跨「计算机使用 → 机器人使用」的能力分类,可用于本项目协议的**子领域划分参考** | **不深读,列为备查**;若后续要调整协议 §1 的研究范围,可回头读 |

---

## 收录标准

一条论文进入本文件,当且仅当它满足协议 §4 的排除条件:

1. **标题或摘要自述为综述 / 立场 / 教程**(survey / review / perspective / perspectives / tutorial / primer / overview);**或**
2. **发表于综述类刊物**(Annual Review 系列等);**且**
3. **不提出可独立验证的新方法**(「纯综述无新方法」)。

**不满足第 3 条的**即使标题含 "review" 也**不**进本文件 —— 例如 2610.31427 FastHarness 的 "Review Scheduling" 是方法名,指的是「定期调度一个 VLM 去复核策略的动作块」,不是文献综述。

---

## 待办与跟踪

- [ ] **本文件是**协议 §4 里**唯一一条从未被真正使用过的归档路径**。修订 `is_survey()` 后,建议在**月度循环(协议 §7)**里复核一次本文件的条目数与判定准确性。
- [ ] **`is_survey()` 的判定仍有启发式成分**:标题写 "A Survey of ..." 但实质是立场论文、或标题完全不含关键词但摘要通篇是梳理 —— 这两类仍会漏判。⚠️ 当前规则能覆盖的是**自述式综述**,这是协议 §4 所说的「纯综述」的**可操作子集**。
- [ ] **2610.30438 是 Annual Review 正式综述**,若本项目后续设立「触觉」子领域的**专项跟踪**,建议把它作为**基线文献**引用,而不是按普通论文对待。
