#!/usr/bin/env python3
"""Daily Robotics Research Tracker.

Pulls arXiv (cs.RO / cs.AI / cs.CV / cs.LG / cs.MA) and GitHub updates
for general robotics topics and produces a human digest, raw JSON,
and a repo watchlist.

The script intentionally uses only Python's standard library so it can
run in any clean environment (laptop, server, GitHub Actions, etc.).
"""

from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import os
import pathlib
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from typing import Any


ROOT = pathlib.Path(__file__).resolve().parents[1]
USER_AGENT = "RoboticsResearch-tracker/1.0 (https://github.com/Dave-he/RoboticsResearch)"

# arXiv categories to query
ARXIV_CATEGORIES = ["cs.RO", "cs.AI", "cs.CV", "cs.LG", "cs.MA"]

# arXiv query terms - broad coverage of robotics
ARXIV_TERMS = [
    "manipulation",
    "dexterous manipulation",
    "grasping",
    "imitation learning",
    "reinforcement learning robotics",
    "sim-to-real",
    "sim2real",
    "embodied AI",
    "embodied agent",
    "robot foundation model",
    "vision-language-action",
    "VLA model",
    "humanoid robot",
    "humanoid locomotion",
    "bipedal locomotion",
    "whole-body control",
    "legged robot",
    "quadruped",
    "visual SLAM",
    "LiDAR SLAM",
    "visual odometry",
    "neural SLAM",
    "visual navigation",
    "path planning",
    "dexterous hand",
    "tactile sensing",
    "force control",
    "compliant control",
    "soft robotics",
    "RT-2",
    "OpenVLA",
    "Octo",
    "DreamerV3",
    "GR-1",
    "GR-2",
    "3D diffusion policy",
    "RDT",
]

# GitHub search queries
GITHUB_QUERIES = [
    "robotics manipulation",
    "humanoid robot",
    "dexterous hand",
    "VLA model",
    "visual SLAM",
    "imitation learning robot",
    "sim2real",
    "robot foundation model",
]

# HuggingFace search queries
HF_QUERIES = [
    "robotics",
    "manipulation",
    "VLA",
    "humanoid",
    "dexterous",
]

NOISE_TERMS = [
    "purely theoretical",
    "no robotics",
    "biological only",
]

# Top labs (for bonus scoring)
TOP_LABS = [
    "google deepmind", "deepmind", "meta fair", "meta ai",
    "stanford", "mit", "berkeley", "cmu", "nvidia", "sustech",
    "tsinghua", "sjtu", "pku", "eth zurich", "inria",
]


def request_json(url: str, headers: dict[str, str] | None = None) -> Any:
    merged = {"User-Agent": USER_AGENT, "Accept": "application/json"}
    if headers:
        merged.update(headers)
    request = urllib.request.Request(url, headers=merged)
    with urllib.request.urlopen(request, timeout=60) as response:
        return json.loads(response.read().decode("utf-8"))


def request_text(url: str, headers: dict[str, str] | None = None) -> str:
    merged = {"User-Agent": USER_AGENT}
    if headers:
        merged.update(headers)
    request = urllib.request.Request(url, headers=merged)
    with urllib.request.urlopen(request, timeout=60) as response:
        return response.read().decode("utf-8")


def clean_text(value: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(value or "")).strip()


def slugify(value: str, limit: int = 96) -> str:
    value = re.sub(r"[^\w\u4e00-\u9fff.-]+", "_", value, flags=re.UNICODE)
    value = re.sub(r"_+", "_", value).strip("._")
    return value[:limit] or "untitled"


def arxiv_id_from_url(url: str) -> str:
    return url.rstrip("/").split("/")[-1]


_ARXIV_TERMS_LOWER: tuple[str, ...] = tuple(t.lower() for t in ARXIV_TERMS)
_NOISE_TERMS_LOWER: tuple[str, ...] = tuple(t.lower() for t in NOISE_TERMS)


def keyword_score(title: str, summary: str) -> int:
    """Score paper relevance: title match * 5 + abstract match * 2 + bonuses."""
    title_lower = title.lower()
    text_lower = f"{title_lower} {summary.lower()}"
    score = 0
    # Membership check (not count) is sufficient — only the boolean matters.
    for term in _ARXIV_TERMS_LOWER:
        if term in text_lower:
            score += 5 if term in title_lower else 2
    # Bonus: top lab
    for lab in TOP_LABS:
        if lab in text_lower:
            score += 4
            break
    # Penalize: noise terms
    for noise in _NOISE_TERMS_LOWER:
        if noise in text_lower:
            score -= 3
    return score


def is_robotics_relevant(title: str, summary: str, categories: list[str]) -> bool:
    """Hard filter: must be robotics-relevant by category OR by keyword hit."""
    cats_lower = [c.lower() for c in categories]
    if "cs.ro" in cats_lower:
        return True
    text_lower = f"{title} {summary}".lower()
    must_have = [
        "robot", "manipulat", "grasp", "humanoid", "legged", "bipedal",
        "quadruped", "slam", "navigation", "embodied", "dexterous",
        "tactile", "locomotion", "sim2real", "sim-to-real",
    ]
    return any(kw in text_lower for kw in must_have)


def fetch_arxiv(max_results: int) -> list[dict[str, Any]]:
    """Fetch recent arXiv papers matching our terms via per-term queries.

    arXiv API chokes on long OR queries, so we issue one short query per
    representative term and de-duplicate. This is slower but reliable.
    """
    # Curated short list — each term is high-signal and likely to find
    # robotics papers. Skip noisy generic terms.
    primary_terms = [
        "manipulation robot",
        "dexterous manipulation",
        "humanoid robot",
        "imitation learning robot",
        "sim-to-real",
        "vision-language-action",
        "visual SLAM",
        "dexterous hand",
        "tactile sensing robot",
        "embodied agent",
        "legged locomotion",
        "whole-body control",
        "neural SLAM",
        "robot foundation model",
    ]
    ns = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
    papers_by_id: dict[str, dict[str, Any]] = {}
    per_term = max(8, max_results // len(primary_terms))

    for term in primary_terms:
        cat_query = " OR ".join(f"cat:{c}" for c in ARXIV_CATEGORIES)
        query = f"({cat_query}) AND (all:\"{term}\")"
        params = urllib.parse.urlencode(
            {
                "search_query": query,
                "start": 0,
                "max_results": per_term,
                "sortBy": "submittedDate",
                "sortOrder": "descending",
            }
        )
        url = f"https://export.arxiv.org/api/query?{params}"
        try:
            feed = request_text(url)
        except Exception as exc:
            print(f"[warn] arXiv query failed for {term!r}: {exc}", file=sys.stderr)
            time.sleep(2)
            continue
        try:
            root = ET.fromstring(feed)
        except ET.ParseError as exc:
            print(f"[warn] arXiv parse failed for {term!r}: {exc}", file=sys.stderr)
            time.sleep(2)
            continue

        for entry in root.findall("atom:entry", ns):
            title = clean_text(entry.findtext("atom:title", default="", namespaces=ns))
            summary = clean_text(entry.findtext("atom:summary", default="", namespaces=ns))
            categories = [cat.attrib.get("term", "") for cat in entry.findall("atom:category", ns)]

            if not is_robotics_relevant(title, summary, categories):
                continue

            paper_id_url = clean_text(entry.findtext("atom:id", default="", namespaces=ns))
            arxiv_id = arxiv_id_from_url(paper_id_url)
            if arxiv_id in papers_by_id:
                papers_by_id[arxiv_id].setdefault("matched_terms", []).append(term)
                continue

            score = keyword_score(title, summary)
            if score <= 0:
                continue

            authors = [
                clean_text(author.findtext("atom:name", default="", namespaces=ns))
                for author in entry.findall("atom:author", ns)
            ]
            links = {link.attrib.get("title") or link.attrib.get("rel", ""): link.attrib.get("href", "") for link in entry.findall("atom:link", ns)}
            pdf_url = links.get("pdf", "")
            abs_url = links.get("alternate", paper_id_url)

            published_raw = clean_text(entry.findtext("atom:published", default="", namespaces=ns))[:10]
            try:
                pub_date = dt.date.fromisoformat(published_raw)
                days_old = (dt.date.today() - pub_date).days
                if days_old <= 7:
                    score += 3
                elif days_old <= 30:
                    score += 1
            except ValueError:
                pass

            papers_by_id[arxiv_id] = {
                "id": arxiv_id,
                "title": title,
                "authors": [a for a in authors if a],
                "published": published_raw,
                "updated": clean_text(entry.findtext("atom:updated", default="", namespaces=ns))[:10],
                "summary": summary,
                "categories": [c for c in categories if c],
                "abs_url": abs_url,
                "pdf_url": pdf_url,
                "score": score,
                "matched_terms": [term],
            }
        time.sleep(1.5)  # be polite to arXiv

    papers = list(papers_by_id.values())
    # Boost score for papers that matched multiple terms
    for p in papers:
        if len(p.get("matched_terms", [])) > 1:
            p["score"] += min(2, len(p["matched_terms"]) - 1)
    return sorted(papers, key=lambda p: (p["score"], p["published"]), reverse=True)


def fetch_github_repos(per_query: int, min_stars: int = 50) -> list[dict[str, Any]]:
    """Fetch recent robotics repos on GitHub."""
    headers = {"Accept": "application/vnd.github+json"}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"

    repos: dict[str, dict[str, Any]] = {}
    for query in GITHUB_QUERIES:
        # Add stars filter to query
        full_query = f"{query} stars:>={min_stars}"
        params = urllib.parse.urlencode(
            {
                "q": full_query,
                "sort": "updated",
                "order": "desc",
                "per_page": per_query,
            }
        )
        url = f"https://api.github.com/search/repositories?{params}"
        try:
            payload = request_json(url, headers=headers)
        except Exception as exc:
            print(f"[warn] GitHub query failed for {query!r}: {exc}", file=sys.stderr)
            continue

        for item in payload.get("items", []):
            full_name = item.get("full_name")
            if not full_name:
                continue
            current = repos.get(full_name)
            candidate = {
                "full_name": full_name,
                "description": clean_text(item.get("description") or ""),
                "html_url": item.get("html_url"),
                "stars": item.get("stargazers_count", 0),
                "forks": item.get("forks_count", 0),
                "language": item.get("language"),
                "updated_at": (item.get("updated_at") or "")[:10],
                "pushed_at": (item.get("pushed_at") or "")[:10],
                "topics": item.get("topics", []),
                "query": query,
            }
            if current is None or candidate["stars"] > current.get("stars", 0):
                repos[full_name] = candidate
        time.sleep(1.2)

    return sorted(repos.values(), key=lambda r: (r.get("pushed_at") or "", r.get("stars") or 0), reverse=True)


def fetch_huggingface_models(per_query: int) -> list[dict[str, Any]]:
    """Fetch recent robotics models on HuggingFace."""
    models: dict[str, dict[str, Any]] = {}
    for query in HF_QUERIES:
        params = urllib.parse.urlencode({"search": query, "limit": per_query, "sort": "lastModified", "direction": -1})
        url = f"https://huggingface.co/api/models?{params}"
        try:
            payload = request_json(url)
        except Exception as exc:
            print(f"[warn] Hugging Face query failed for {query!r}: {exc}", file=sys.stderr)
            continue

        for item in payload:
            model_id = item.get("modelId") or item.get("id")
            if not model_id:
                continue
            current = models.get(model_id)
            candidate = {
                "model_id": model_id,
                "author": item.get("author"),
                "last_modified": (item.get("lastModified") or "")[:10],
                "downloads": item.get("downloads", 0),
                "likes": item.get("likes", 0),
                "pipeline_tag": item.get("pipeline_tag"),
                "tags": item.get("tags", [])[:16],
                "url": f"https://huggingface.co/{model_id}",
                "query": query,
            }
            if current is None or candidate["downloads"] > current.get("downloads", 0):
                models[model_id] = candidate
        time.sleep(0.5)

    return sorted(models.values(), key=lambda m: (m.get("last_modified") or "", m.get("downloads") or 0), reverse=True)


def md_escape(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def truncate(value: str, limit: int = 280) -> str:
    value = clean_text(value)
    if len(value) <= limit:
        return value
    return value[: limit - 1].rstrip() + "…"


def classify_paper(paper: dict[str, Any]) -> str:
    """Classify paper into a sub-area based on title+summary keywords."""
    text_lower = f"{paper['title']} {paper['summary']}".lower()
    buckets = [
        ("humanoid", ["humanoid", "bipedal", "legged", "locomotion", "whole-body"]),
        ("manipulation", ["manipulat", "grasp", "dexterous", "tactile", "force control"]),
        ("vla", ["vision-language-action", "vla", "rt-2", "openvla", "octo", "π0", "pi0", "language-conditioned"]),
        ("embodied_ai", ["embodied", "embodied agent", "foundation model"]),
        ("imitation_rl", ["imitation learning", "reinforcement learning", "rl", "behavior cloning"]),
        ("slam", ["slam", "visual odometry", "lidar", "neural slam", "3d reconstruction"]),
        ("navigation", ["navigation", "path planning", "visual navigation"]),
        ("simulation", ["sim2real", "sim-to-real", "mujoco", "isaac", "simulation"]),
        ("soft_robotics", ["soft robot", "compliant"]),
    ]
    for label, kws in buckets:
        if any(kw in text_lower for kw in kws):
            return label
    return "other"


def render_daily_digest(run_date: str, papers: list[dict[str, Any]]) -> str:
    """Render the daily human-readable digest."""
    lines: list[str] = []
    lines.append(f"# 机器人研究每日摘要 · {run_date}")
    lines.append("")
    lines.append(f"> 自动生成,共 {len(papers)} 篇命中论文。")
    lines.append("")

    # Group by sub-area
    by_area: dict[str, list[dict[str, Any]]] = {}
    for p in papers:
        area = classify_paper(p)
        by_area.setdefault(area, []).append(p)

    area_titles = {
        "humanoid": "🦵 人形 / 足式机器人",
        "manipulation": "🦾 操控 / 灵巧手 / 抓取",
        "vla": "🧠 视觉-语言-动作模型 (VLA)",
        "embodied_ai": "🌐 具身智能 / 机器人基础模型",
        "imitation_rl": "🎓 模仿学习 / 强化学习",
        "slam": "🗺️ SLAM / 视觉里程计 / 3D 感知",
        "navigation": "🧭 导航 / 路径规划",
        "simulation": "🧪 仿真 / Sim2Real",
        "soft_robotics": "🤏 软体机器人 / 柔性控制",
        "other": "📦 其他机器人相关",
    }

    for area in ["vla", "embodied_ai", "humanoid", "manipulation", "imitation_rl", "slam", "navigation", "simulation", "soft_robotics", "other"]:
        items = by_area.get(area, [])
        if not items:
            continue
        lines.append(f"## {area_titles[area]} ({len(items)} 篇)")
        lines.append("")
        for i, p in enumerate(items[:10], 1):
            title = p["title"]
            arxiv_id = p["id"]
            score = p["score"]
            authors = ", ".join(p["authors"][:3])
            if len(p["authors"]) > 3:
                authors += " et al."
            cats = ", ".join(p["categories"][:3])
            summary = truncate(p["summary"], 360)
            pub = p["published"]
            priority = "🔥 read_now" if score >= 12 else ("👀 watch" if score >= 6 else "📌 info")
            lines.append(f"### {i}. {title}")
            lines.append("")
            lines.append(f"- **arXiv**: [{arxiv_id}]({p['abs_url']})  ·  **PDF**: [link]({p['pdf_url']})")
            lines.append(f"- **作者**: {authors}")
            lines.append(f"- **发表**: {pub}  ·  **类别**: {cats}")
            lines.append(f"- **相关性评分**: {score}  ·  **{priority}**")
            lines.append(f"- **摘要**: {summary}")
            lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## 📋 本日操作建议")
    lines.append("")
    top3 = papers[:3]
    if top3:
        lines.append("**建议今日深读 (Top 3):**")
        for i, p in enumerate(top3, 1):
            lines.append(f"{i}. [{p['title']}]({p['abs_url']}) — score {p['score']}")
        lines.append("")
    lines.append("- 对 read_now 的论文,按 `docs/机器人研究协议.md §9` 模板生成研读报告")
    lines.append("- 在 `docs/机器人_深度研读报告.md` 末尾追加新报告链接")
    lines.append("- 关注 `analysis/repo_watchlist/` 中的新增高 Star 仓库")
    lines.append("")
    return "\n".join(lines)


def render_repo_watchlist(run_date: str, repos: list[dict[str, Any]], models: list[dict[str, Any]]) -> str:
    """Render the daily repo/model watchlist."""
    lines: list[str] = []
    lines.append(f"# 机器人仓库与模型观察 · {run_date}")
    lines.append("")

    lines.append(f"## GitHub 仓库 (Top {len(repos)})")
    lines.append("")
    lines.append("| 仓库 | Stars | Forks | 语言 | 更新 | 描述 | 查询 |")
    lines.append("|---|---:|---:|---|---|---|---|")
    for r in repos[:25]:
        name = f"[{r['full_name']}]({r['html_url']})"
        desc = truncate(md_escape(r["description"] or ""), 120)
        lines.append(
            f"| {name} | {r['stars']} | {r['forks']} | {r['language'] or '-'} | "
            f"{r['pushed_at']} | {desc} | {r['query']} |"
        )
    lines.append("")

    lines.append(f"## HuggingFace 模型 (Top {len(models)})")
    lines.append("")
    lines.append("| 模型 | 作者 | 下载量 | Likes | 最后更新 | Pipeline | 链接 |")
    lines.append("|---|---|---:|---:|---|---|---|")
    for m in models[:25]:
        name = f"[{m['model_id']}]({m['url']})"
        lines.append(
            f"| {name} | {m['author'] or '-'} | {m['downloads']} | {m['likes']} | "
            f"{m['last_modified']} | {m['pipeline_tag'] or '-'} | {m['query']} |"
        )
    lines.append("")
    return "\n".join(lines)


def update_marked_section(path: pathlib.Path, marker: str, content: str) -> None:
    """Replace content between BEGIN/END markers in a markdown file."""
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    pattern = re.compile(
        rf"<!-- {re.escape(marker)}:begin -->.*?<!-- {re.escape(marker)}:end -->",
        re.DOTALL,
    )
    if pattern.search(text):
        new_text = pattern.sub(
            f"<!-- {marker}:begin -->\n{content}\n<!-- {marker}:end -->",
            text,
        )
    else:
        new_text = text + f"\n\n<!-- {marker}:begin -->\n{content}\n<!-- {marker}:end -->\n"
    path.write_text(new_text, encoding="utf-8")


def update_global_index(index_path: pathlib.Path, run_date: str, papers: list[dict[str, Any]]) -> None:
    """Append a dated entry to the global research index."""
    if not index_path.exists():
        return
    top5 = papers[:5]
    if not top5:
        return
    entry_lines = [f"### {run_date} 自动更新"]
    entry_lines.append("")
    for i, p in enumerate(top5, 1):
        entry_lines.append(
            f"{i}. **[{p['title']}]({p['abs_url']})** "
            f"(`{p['id']}`, score={p['score']}) — {truncate(p['summary'], 180)}"
        )
    entry_lines.append("")
    entry = "\n".join(entry_lines)

    text = index_path.read_text(encoding="utf-8")
    if "## 自动更新流" in text:
        # Append under the "## 自动更新流" heading
        parts = text.split("## 自动更新流", 1)
        header_part = parts[0] + "## 自动更新流\n\n"
        rest = parts[1].lstrip("\n")
        new_text = header_part + entry + "\n" + rest
    else:
        new_text = text + "\n\n## 自动更新流\n\n" + entry
    index_path.write_text(new_text, encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Daily robotics research tracker")
    parser.add_argument("--output-root", type=pathlib.Path, default=ROOT, help="Project root for outputs")
    parser.add_argument("--max-arxiv", type=int, default=80, help="Max arXiv results to fetch")
    parser.add_argument("--github-per-query", type=int, default=12, help="GitHub results per query")
    parser.add_argument("--hf-per-query", type=int, default=8, help="HuggingFace results per query")
    parser.add_argument("--min-stars", type=int, default=50, help="Minimum GitHub stars filter")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    run_date = dt.date.today().isoformat()
    output_root: pathlib.Path = args.output_root.resolve()

    papers_dir = output_root / "papers" / "daily"
    daily_dir = output_root / "docs" / "daily"
    watchlist_dir = output_root / "analysis" / "repo_watchlist"
    for d in [papers_dir, daily_dir, watchlist_dir]:
        d.mkdir(parents=True, exist_ok=True)

    print(f"[info] Fetching arXiv (max {args.max_arxiv})...")
    papers = fetch_arxiv(args.max_arxiv)
    print(f"[info] Found {len(papers)} relevant papers")

    print(f"[info] Fetching GitHub repos (per-query {args.github_per_query}, min stars {args.min_stars})...")
    repos = fetch_github_repos(args.github_per_query, args.min_stars)
    print(f"[info] Found {len(repos)} repos")

    print(f"[info] Fetching HuggingFace models (per-query {args.hf_per_query})...")
    models = fetch_huggingface_models(args.hf_per_query)
    print(f"[info] Found {len(models)} models")

    # Save raw JSON
    raw = {
        "run_date": run_date,
        "papers": papers,
        "repos": repos,
        "models": models,
    }
    json_path = papers_dir / f"{run_date}_robotics_research.json"
    json_path.write_text(json.dumps(raw, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[info] Raw JSON: {json_path.relative_to(output_root)}")

    # Daily digest
    digest_md = render_daily_digest(run_date, papers)
    digest_path = daily_dir / f"{run_date}_robotics_research_digest.md"
    digest_path.write_text(digest_md, encoding="utf-8")
    print(f"[info] Digest:    {digest_path.relative_to(output_root)}")

    # Repo watchlist
    watch_md = render_repo_watchlist(run_date, repos, models)
    watch_path = watchlist_dir / f"{run_date}_robotics_repos.md"
    watch_path.write_text(watch_md, encoding="utf-8")
    print(f"[info] Watchlist: {watch_path.relative_to(output_root)}")

    # Update global index
    index_path = output_root / "docs" / "机器人_深度研读报告.md"
    if index_path.exists():
        update_global_index(index_path, run_date, papers)
        print(f"[info] Updated global index: {index_path.relative_to(output_root)}")

    print(f"[done] {run_date} · {len(papers)} papers · {len(repos)} repos · {len(models)} models")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
