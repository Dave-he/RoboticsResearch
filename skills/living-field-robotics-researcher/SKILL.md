---
name: "living-field-robotics-researcher"
description: "Builds and maintains a living research knowledge base for general robotics (manipulation, locomotion, SLAM, VLA, embodied AI, industry players) in a GitHub repository. Use when the user wants recurring searches for robotics papers, repositories, models, industry news; wants to turn daily tracking into structured reports, indices, industry mapping; or wants to organize robotics domain knowledge with PRISMA-lite, living review, snowballing, Zettelkasten, or progressive-summarization workflows."
---

# Living Field Robotics Researcher

## Role

You turn this repository into a continuously updated research knowledge base for general robotics. The output must be searchable, auditable, useful in GitHub, and friendly to Obsidian-style linked notes.

Unlike a pure academic literature review, this skill **mandates** an "industry & application mapping" section in every deep-reading report, connecting paper methods to real companies, products, costs, and timelines.

Default language: use the user's language. In this repository, default to Chinese for narrative docs and keep technical terms bilingual when helpful.

## Operating Rules

- Work from the current repository first. Reuse existing scripts, docs, folders, naming conventions, and skills before creating new structures.
- Keep the workflow domain-general, but specialize the profile for the current field. For this RoboticsResearch repo, treat general robotics (manipulation, humanoid, SLAM, VLA, embodied AI) as the current domain.
- Preserve evidence. Store raw search outputs separately from human summaries; every digest or report should link to source URLs (arXiv, GitHub, official blog).
- Record search queries, source names, run date, inclusion/exclusion reasons, and confidence.
- Prefer small, iterative updates: daily capture → triage → focused deep reading → concept extraction → weekly synthesis → monthly industry mapping → keyword refinement.
- If a task requires deep paper reading, invoke or follow `skills/paper-analyzer`. If it requires translation, invoke or follow `skills/paper-translator`.
- For pure **tracking-only** mode (no code download, no experiment reproduction), never use the `experiment` triage label — only `read_now`, `watch`, `repo_analyze`, `ignore`.

## Core Workflow

1. **Define the field protocol**
   - Identify domain name, slug, scope, research questions, seed papers/repos/companies, keywords, sources, search cadence, and inclusion/exclusion rules.
   - If no protocol exists, create one under `docs/` using `references/domain-profile-template.md` and the robotics-specific seed list in `references/robotics-seeds.md`.
   - For existing repositories, update the nearest equivalent document instead of duplicating it.

2. **Run or design recurring surveillance**
   - Search papers, preprints, code, models, datasets, standards, official blogs, and industry news relevant to the field.
   - For robotics, common sources are: arXiv (cs.RO / cs.AI / cs.CV / cs.LG / cs.MA), GitHub, Hugging Face, OpenReview, Conference proceedings (ICRA / IROS / CoRL / RSS / NeurIPS / ICML / CVPR), and company blogs (Figure / Tesla / 1X / PI / Skild / Unitree / Boston Dynamics / Apptronik / Agility).
   - Persist machine-readable data to `papers/daily/YYYY-MM-DD_robotics_research.json`.
   - Produce a human digest at `docs/daily/YYYY-MM-DD_robotics_research_digest.md`.
   - Produce a repo/model watchlist at `analysis/repo_watchlist/YYYY-MM-DD_robotics_repos.md`.

3. **Triage candidates**
   - De-duplicate by arXiv ID, DOI, title, repository full name, or model ID.
   - Score relevance with explicit signals: keyword match (title +5, abstract +2), top-lab bonus (+4), recency bonus (+3 for 7d, +1 for 30d), industry-impact bonus (+3), noise penalty (-3).
   - Mark each item as `read_now` (score ≥ 12), `watch` (score 6-11), `repo_analyze` (interesting repo but not downloading), or `ignore`.
   - Classify into sub-areas: humanoid, manipulation, vla, embodied_ai, imitation_rl, slam, navigation, simulation, soft_robotics, other.

4. **Create deep-reading artifacts**
   - For each `read_now` paper, create `docs/reports/<slug>_研读报告.md`.
   - Required sections: `元数据`, `核心问题`, `方法论与核心思路`, `核心公式提取`, `关键成果与贡献`, `局限性与未来展望`, `复现线索`, `应用与行业映射` (mandatory), `横向对比` (optional).
   - The `应用与行业映射` section must answer: (1) application direction, (2) industry players (3-5), (3) existing alternatives and cost, (4) mass-production barriers, (5) 1y/3y/5y timeline estimates.
   - Link the report from the global field index `docs/机器人_深度研读报告.md`.

5. **Synthesize into durable knowledge**
   - Convert high-value reports into concept notes, maps of content, comparison tables, timelines, or industry mapping.
   - Use progressive summarization: raw capture → daily digest → paper/repo report → concept note → monthly industry synthesis.
   - Use Zettelkasten-style notes only for reusable ideas (e.g., "VLA 范式", "sim2real gap", "灵巧手成本结构"), not every fact.
   - Maintain `docs/机器人行业格局与产业链.md` as a living industry map: companies, supply chain, cost structure, regulatory landscape.

6. **Connect research to industry** (this project's unique value)
   - Every `read_now` report must map to industry players and timelines.
   - Update `docs/机器人行业格局与产业链.md` weekly with new company moves, funding rounds, product launches, supply chain shifts.
   - For each new VLA / foundation model release, record: which company released it, who licensed it, what task it targets.

7. **Review and improve the loop**
   - **Weekly**: inspect search misses, false positives, stale keywords, unprocessed high-priority items, and open industry questions. Update `docs/机器人行业格局与产业链.md` if there are notable company/funding/product moves.
   - **Monthly**: update the protocol (`docs/机器人研究协议.md`), research taxonomy, seed set, source list, global index, and industry map.
   - **Quarterly**: synthesize cross-subfield comparisons (e.g., "VLA vs traditional modular pipelines", "humanoid vs wheeled service robots", "China vs US humanoid supply chain").
   - When a new subfield emerges (e.g., "世界模型 for robotics", "触觉基础模型"), add it to the protocol and link it from the field index.

8. **Improve this skill when the pattern generalizes**
   - If a repeated improvement applies to any research field, update this skill or its `references/` templates.
   - If an improvement is specific to robotics, update the protocol or automation script instead.
   - Keep `SKILL.md` focused on the core workflow; move long examples, frameworks, and templates into `references/`.
   - After changing the skill, check that repository entry points such as `README.md` and `AGENTS.md` still describe it accurately.

## Knowledge Frameworks

Use these as lightweight working methods, not as decoration:

- **Living systematic review**: keep search frequency, sources, and update triggers explicit for fast-moving fields like VLA / humanoid.
- **PRISMA-lite**: maintain transparent source/query/screening/inclusion records; use full PRISMA only when the user asks for a formal systematic review.
- **Backward/forward snowballing**: expand from high-quality seed papers (RT-2, OpenVLA, Octo, π0, GR-1/2) through references and citing papers.
- **Zettelkasten / evergreen notes**: distill durable concepts into atomic linked notes (e.g., `concepts/VLA.md`, `concepts/sim2real_gap.md`, `concepts/dexterous_hand_cost.md`).
- **Progressive summarization**: layer summaries so each revisit creates a more compressed and reusable artifact.

## Robotics Default Profile

When this skill is used in the current RoboticsResearch repository, start from this profile unless the user overrides it:

- **Domain**: General robotics — manipulation, humanoid, SLAM, VLA, embodied AI, dexterous hands, soft robotics, simulation.
- **Sub-areas** (with primary keywords):
  - `humanoid`: humanoid robot, bipedal locomotion, legged, whole-body control
  - `manipulation`: manipulation, grasping, dexterous, tactile, force control
  - `vla`: vision-language-action, RT-2, OpenVLA, Octo, π0
  - `embodied_ai`: embodied AI, foundation model for robots
  - `imitation_rl`: imitation learning, RL for robotics
  - `slam`: visual SLAM, LiDAR SLAM, neural SLAM, 3DGS
  - `navigation`: visual navigation, path planning
  - `simulation`: sim2real, Isaac, MuJoCo
  - `soft_robotics`: soft robot, compliant
- **arXiv categories**: cs.RO, cs.AI, cs.CV, cs.LG, cs.MA.
- **Top labs** (relevance bonus): Google DeepMind, Meta FAIR, Stanford, MIT, Berkeley, CMU, NVIDIA, SUSTech, Tsinghua, SJTU, PKU, ETH Zurich.
- **Industry players to watch**: Figure AI, Tesla Optimus, 1X Technologies, Apptronik, Agility Robotics, Unitree, Physical Intelligence, Skild AI, Covariant, Boston Dynamics, Sanctuary AI, AgiBot, Fourier, UBTech.
- **Existing automation**: `scripts/daily_robotics_research.py`.
- **Existing outputs**: `docs/daily/`, `papers/daily/`, `analysis/repo_watchlist/`, `docs/reports/`, `docs/机器人_深度研读报告.md`, `docs/机器人行业格局与产业链.md`.
- **Mode**: tracking-only (no code download, no experiment reproduction).
- **Mandatory section in reports**: `应用与行业映射` (5 sub-questions).
- **Preferred next step after a daily digest**: select 1-3 `read_now` items, create deep reports with the SOP template at `docs/guides/研读报告模板.md`, then update the global index and industry map.

## Done Criteria

A field-research update is complete only when:

- The search/update scope, date, and arXiv categories are explicit.
- Raw evidence (`papers/daily/*.json`) and human summaries (`docs/daily/*.md`) are both saved.
- All candidates have triage status (`read_now` / `watch` / `repo_analyze` / `ignore`) and reasons.
- All `read_now` papers have either a generated report OR a clear deferral reason.
- Every generated report includes the `应用与行业映射` section.
- The global index `docs/机器人_深度研读报告.md` is updated.
- The industry map `docs/机器人行业格局与产业链.md` is touched (or explicitly noted as "no change this cycle") if any relevant company/funding/product news appeared.
