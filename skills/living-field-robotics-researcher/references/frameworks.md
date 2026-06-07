# Knowledge Frameworks for Living Field Research (Robotics)

Use this reference when designing or revising a repository-level research protocol for robotics.

## Living Systematic Review Pattern

Use for fast-moving fields where new papers and code can change conclusions. Robotics in 2025-2026 is a prime example: VLA models and humanoid prototypes are released at a pace where a 6-month-old review is stale.

- Define the review question, scope, search sources, search frequency, and update triggers before running the loop.
- Maintain continual evidence surveillance: scheduled arXiv pulls, GitHub watchers, Hugging Face model monitors, official RSS/blog subscriptions.
- Update the field synthesis when new evidence changes a claim, benchmark, taxonomy, or implementation priority.
- Keep a visible "what changed" trail in the daily digest, field index, or changelog-like section.
- For robotics specifically: a new foundation model release (e.g., π0, OpenVLA-OFT, GR-3) can invalidate the SOTA claim of a month-old paper.

Source basis: Cochrane describes living systematic reviews as continually updated reviews with new evidence incorporated as it becomes available, with explicit search methods and anticipated update frequency in the protocol.

Reference: https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-22

## PRISMA-Lite Traceability

Use PRISMA as a transparency checklist, not as a badge.

Track:
- Sources searched.
- Exact search strings or API parameters.
- Date of each search.
- Candidate counts before and after de-duplication.
- Screening criteria.
- Included, excluded, and deferred items with reasons.
- Links to raw data, PDFs, reports, and synthesis pages.

For robotics, an additional audit dimension is **which industry player / lab is responsible** for each item — this makes the "evidence" easier to map to "who will productize it".

## Backward/Forward Snowballing

Start from a small set of high-quality seed papers (RT-2, OpenVLA, Octo, π0, GR-1/2, 3D Diffusion Policy, RDT, DreamerV3, HPT, ManipLLM, etc.) and:
- Backward: walk the references of each seed to find older foundational work.
- Forward: walk the citations of each seed to find newer work that builds on it.
- One iteration at a time: don't recurse more than 2 levels in a single weekly pass, otherwise the scope explodes.
- Prefer a snowball that crosses subfields (e.g., from VLA → to dexterous hand hardware → to tactile sensing) over a deep dive in one niche.

## Zettelkasten / Evergreen Notes

For robotics, useful concept notes (one per file in `docs/concepts/`):
- `VLA.md` — Vision-Language-Action paradigm
- `sim2real_gap.md` — sim-to-real gap and the main mitigation techniques
- `dexterous_hand_cost.md` — cost structure and current state of dexterous hands
- `humanoid_supply_chain.md` — supply chain mapping for humanoid robots
- `manipulation_taxonomy.md` — taxonomy of manipulation tasks
- `tactile_sensing.md` — tactile sensing modalities
- `embodied_foundation_model.md` — what makes a "foundation model" for robotics

Each concept note should have:
1. One central claim / definition
2. 2-5 supporting observations with sources
3. Links to all related deep-reading reports
4. Open questions that the next research pass should answer

## Progressive Summarization

Layer summaries so each revisit creates a more compressed and reusable artifact:

1. **Layer 0 (raw)**: arXiv JSON, GitHub repo metadata, official blog post.
2. **Layer 1 (digest)**: daily digest `docs/daily/YYYY-MM-DD_robotics_research_digest.md` — bullet-level summary of every relevant item.
3. **Layer 2 (deep report)**: `docs/reports/<slug>_研读报告.md` — full SOP with formula extraction and industry mapping.
4. **Layer 3 (concept note)**: `docs/concepts/<idea>.md` — distilled, reusable across reports.
5. **Layer 4 (synthesis)**: `docs/research/YYYY-MM_robotics_synthesis.md` or `docs/机器人行业格局与产业链.md` — cross-cutting monthly view.

## Industry Mapping Framework

Unique to this project. Every `read_now` paper must be mapped to:

- **Application direction**: industrial / logistics / service / home / medical / specialty.
- **Industry players**: 3-5 specific companies + their product lines.
- **Alternative solutions**: what they use today, cost magnitude.
- **Mass-production barriers**: hardware cost, training data, reliability, safety certification.
- **Timeline**: 1y / 3y / 5y feasibility.

Maintain `docs/机器人行业格局与产业链.md` as the living map. Update it when:
- A company announces a new product, funding round, or partnership.
- A new benchmark changes the cost/performance frontier.
- A new regulation (UL, ISO, EU AI Act) is published.
- A supply-chain component (joint module, dexterous hand, tactile sensor) drops in cost by ≥ 30%.

## Anti-Patterns to Avoid

- **Topic-drift**: don't let the tracker expand into pure ML theory, neuroscience, or non-robotics AI. If a paper is about LLMs in general, skip it unless it has a robotics application.
- **Surface summarization**: don't write a "summary" that just paraphrases the abstract. Force every report to extract formulas, identify the key innovation precisely, and map to industry.
- **Industry fantasy**: when mapping to industry, distinguish "this is what the paper claims" from "this is what is actually feasible at scale today" and "this is our speculation".
- **Keyword over-fitting**: if a paper is on a related but different topic (e.g., NeRF for static scene reconstruction, not robotics), exclude it. The 3DGS example in `configs/keywords.yaml` should be qualified to "for robotics".

## Sources Beyond arXiv

For a holistic view, the protocol should also pull from:
- **Conference proceedings**: ICRA, IROS, CoRL, RSS, NeurIPS, ICML, CVPR, ECCV, ICCV — RSS/ICRA are the top venues.
- **Workshop papers**: CoRL workshop on mobile manipulation, IROS humanoid robots workshop, etc. Often contain the most forward-looking work.
- **Preprint servers**: arXiv (primary), OpenReview (for in-review papers at major conferences).
- **GitHub trending** in cs.RO-related topics.
- **Hugging Face** for new model releases.
- **Official blogs** of industry players.
- **Standards bodies**: ISO/TC 299 (robotics), ASTM F45 (robotics and automation).
- **Industry analysts**: IFR (International Federation of Robotics), IDC, Goldman Sachs research notes, Morgan Stanley research notes.
- **Patent filings**: USPTO / Google Patents for corporate IP moves.
