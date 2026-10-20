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

# RSS fallback categories — used when /api/query is throttled by Varnish (HTTP 406).
# These mirror the categories most likely to contain robotics papers.
ARCHIVE_RSS_CATEGORIES = [
    "cs.RO",
    "cs.AI",
    "cs.CV",
    "cs.LG",
    "cs.MA",
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
    merged = {"User-Agent": USER_AGENT, "Accept": "application/json, */*"}
    if headers:
        merged.update(headers)
    request = urllib.request.Request(url, headers=merged)
    with urllib.request.urlopen(request, timeout=60) as response:
        return json.loads(response.read().decode("utf-8"))


def request_json_with_headers(
    url: str, headers: dict[str, str] | None = None
) -> tuple[Any, dict[str, str]]:
    """Like request_json, but also returns the response headers.

    The GitHub Search API reports its remaining quota in
    ``x-ratelimit-remaining`` / ``x-ratelimit-reset``.  Reading them is the
    only way to know whether a failing query is a rate limit (retryable
    after the window resets) or a genuine error.
    """
    merged = {"User-Agent": USER_AGENT, "Accept": "application/json, */*"}
    if headers:
        merged.update(headers)
    request = urllib.request.Request(url, headers=merged)
    with urllib.request.urlopen(request, timeout=60) as response:
        payload = json.loads(response.read().decode("utf-8"))
        resp_headers = {k.lower(): v for k, v in response.headers.items()}
        return payload, resp_headers


def request_text(url: str, headers: dict[str, str] | None = None) -> str:
    merged = {"User-Agent": USER_AGENT, "Accept": "application/atom+xml, application/xml;q=0.9, */*;q=0.8"}
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


# --- 已研读论文登记 ---------------------------------------------------
#
# 协议 §4 把「纯综述无新方法」排除在深读之外,§6 要求研读报告落到
# docs/reports/<slug>_研读报告.md。因此「哪篇已经深读过」的唯一权威
# 来源就是 docs/reports/ 下的报告文件本身。
#
# 引入这个登记表的直接原因:2026-10-20 的 digest 把 HiFun(2610.19518)
# 排进了「本日建议深读 Top 3」,而该篇早在 2026-10-16 就已完成研读报告
# —— 推荐列表与已读集合之间没有任何交叉检查,导致「建议深读」会反复
# 推送已读论文,浪费本项目最稀缺的资源(人工研读时间)。
#
ARXIV_ID_RE = re.compile(r"\b(\d{4}\.\d{4,5})\b")


def load_read_arxiv_ids(output_root: pathlib.Path) -> set[str]:
    """Return the set of arXiv IDs that already have a report in docs/reports/.

    The report files are the source of truth. The global index is *not*
    consulted on purpose: the daily script appends its own Top-5 entries
    there, and those papers have not been read.
    """
    reports_dir = output_root / "docs" / "reports"
    read_ids: set[str] = set()
    if not reports_dir.is_dir():
        return read_ids
    for report in reports_dir.glob("*.md"):
        try:
            text = report.read_text(encoding="utf-8")
        except OSError:
            continue
        # Prefer the frontmatter field, fall back to any bare arXiv id.
        match = re.search(r"^arxiv_id:\s*\"?(\d{4}\.\d{4,5})", text, re.M)
        if match:
            read_ids.add(match.group(1))
            continue
        read_ids.update(ARXIV_ID_RE.findall(text))
    return read_ids


def normalize_arxiv_id(arxiv_id: str) -> str:
    """Strip the version suffix (2610.19518v2 -> 2610.19518)."""
    return re.sub(r"v\d+$", "", arxiv_id or "").strip()


# Protocol §4: "纯综述无新方法" is excluded from deep reading.
SURVEY_TITLE_RE = re.compile(
    r"\b(a |an )?(comprehensive |systematic |brief |critical |short )?"
    r"(survey|review|overview of the literature)\b",
    re.IGNORECASE,
)


def is_survey(paper: dict[str, Any]) -> bool:
    """Heuristic survey detector, per protocol §4 (surveys go to docs/research/surveys.md)."""
    title = paper.get("title", "")
    if SURVEY_TITLE_RE.search(title):
        return True
    summary = (paper.get("summary", "") or "").lower()
    return summary.startswith("in this survey") or "we survey the" in summary


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


def fetch_arxiv_rss(max_results: int) -> list[dict[str, Any]]:
    """Fallback to arXiv category RSS feeds when /api/query is throttled (HTTP 406).

    Walks each category in ARCHIVE_RSS_CATEGORIES, extracts <item> entries, applies
    the same keyword filter (``keyword_score``), dedups by arxiv id. RSS feeds
    return atom-style items so parsing mirrors ``fetch_arxiv`` but iterates
    ``atom:item`` inside ``rss/channel``.
    """
    seen: set[str] = set()
    papers: list[dict[str, Any]] = []
    for category in ARCHIVE_RSS_CATEGORIES:
        url = f"https://export.arxiv.org/rss/{category}"
        try:
            feed = request_text(url)
        except Exception as exc:
            print(f"[warn] RSS fetch failed for {category}: {exc}", file=sys.stderr)
            time.sleep(1.5)
            continue
        try:
            root = ET.fromstring(feed)
        except ET.ParseError as exc:
            print(f"[warn] RSS parse failed for {category}: {exc}", file=sys.stderr)
            time.sleep(1.5)
            continue
        channel = root.find("channel")
        if channel is None:
            continue
        for item in channel.findall("item"):
            title = clean_text(item.findtext("title", default=""))
            summary = clean_text(item.findtext("description", default=""))
            score = keyword_score(title, summary)
            if score <= 0:
                continue
            link = clean_text(item.findtext("link", default=""))
            arxiv_id = arxiv_id_from_url(link)
            if not arxiv_id or arxiv_id in seen:
                continue
            seen.add(arxiv_id)
            authors_raw = clean_text(item.findtext("author", default=""))
            authors = [authors_raw] if authors_raw else []
            pub_raw = clean_text(item.findtext("pubDate", default=""))
            # RSS pubDate is RFC 822 ("Mon, 28 Sep 2026 00:00:00 +0000"); convert to ISO date.
            published = ""
            try:
                published = dt.datetime.strptime(pub_raw[:25], "%a, %d %b %Y %H:%M:%S").date().isoformat()
            except ValueError:
                published = pub_raw[:10]
            papers.append(
                {
                    "id": arxiv_id,
                    "title": title,
                    "authors": authors,
                    "published": published,
                    "updated": "",
                    "summary": summary,
                    "categories": [category],
                    "abs_url": link,
                    "pdf_url": link.replace("/abs/", "/pdf/") if "/abs/" in link else "",
                    "score": score,
                    "matched_terms": [f"rss:{category}"],
                    "source": f"rss:{category}",
                }
            )
            if len(papers) >= max_results:
                break
        if len(papers) >= max_results:
            break
        time.sleep(1.0)  # be polite between RSS feeds
    return papers


def fetch_github_repos(
    per_query: int, min_stars: int = 50
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Fetch recent robotics repos on GitHub.

    Returns ``(repos, failures)``.

    The unauthenticated GitHub *Search* API allows only 10 requests per
    minute, and this function issues one request per query (8 by default).
    That is within one window only if nothing else consumes the quota, so
    the tail queries used to fail with ``403 rate limit exceeded`` and --
    because the old code swallowed the exception -- the run silently
    produced a *partial* repository set.  Evidence: the stored JSON showed
    47 repos on 2026-10-20 where a full run yields 91-93, and
    logs/daily_cron.log records 13 such failures across 77 runs, always on
    the last queries of the list.

    Now the remaining quota is tracked from the response headers, and a
    rate-limited query waits for the window to reset and retries once.
    Failures are returned so they can be recorded in the output artifact
    instead of vanishing.
    """
    headers = {"Accept": "application/vnd.github+json"}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"

    repos: dict[str, dict[str, Any]] = {}
    failures: list[dict[str, Any]] = []
    remaining: int | None = None
    reset_at: int | None = None

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

        payload = None
        last_error = ""
        for attempt in range(2):
            try:
                payload, resp_headers = request_json_with_headers(url, headers=headers)
                remaining = int(resp_headers.get("x-ratelimit-remaining", remaining or 0))
                reset_at = int(resp_headers.get("x-ratelimit-reset", reset_at or 0))
                break
            except urllib.error.HTTPError as exc:
                last_error = f"HTTP {exc.code}: {exc.reason}"
                if exc.code == 403 and attempt == 0 and reset_at:
                    # Rate limited: wait for the window to reset, then retry once.
                    wait = max(0, reset_at - int(time.time())) + 2
                    if wait > 0:
                        print(
                            f"[warn] GitHub rate limit hit, waiting {wait}s for reset "
                            f"(query={query!r})",
                            file=sys.stderr,
                        )
                        time.sleep(wait)
                    continue
                last_error = f"HTTP {exc.code}: {exc.reason}"
                break
            except Exception as exc:  # noqa: BLE001 - keep the run alive
                last_error = str(exc)
                break

        if payload is None:
            print(
                f"[warn] GitHub query failed for {query!r}: {last_error}",
                file=sys.stderr,
            )
            failures.append({"query": query, "error": last_error})
            # Back off a little so the next query is not immediately throttled.
            time.sleep(2.0)
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

        # Stay clear of the 10/min window: keep at least two slots in reserve.
        if remaining is not None and remaining <= 2:
            wait = max(0, (reset_at or 0) - int(time.time())) + 2
            if wait > 0:
                print(
                    f"[info] GitHub quota nearly exhausted ({remaining} left), "
                    f"waiting {wait}s for reset",
                    file=sys.stderr,
                )
                time.sleep(wait)
        else:
            time.sleep(1.2)

    return (
        sorted(repos.values(), key=lambda r: (r.get("pushed_at") or "", r.get("stars") or 0), reverse=True),
        failures,
    )


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


def render_daily_digest(
    run_date: str,
    papers: list[dict[str, Any]],
    read_ids: set[str] | None = None,
    diagnostics: dict[str, Any] | None = None,
) -> str:
    """Render the daily human-readable digest."""
    read_ids = read_ids or set()
    diagnostics = diagnostics or {}
    lines: list[str] = []
    lines.append(f"# 机器人研究每日摘要 · {run_date}")
    lines.append("")
    lines.append(f"> 自动生成,共 {len(papers)} 篇命中论文。")
    lines.append("")

    # A partial fetch must be visible in the artifact, not just in stderr.
    if diagnostics and not diagnostics.get("complete", True):
        failed = diagnostics.get("github_queries_failed", 0)
        total = diagnostics.get("github_queries_total", 0)
        lines.append("> ⚠️ **本次抓取不完整** —— 以下内容缺失,引用前请注意:")
        if failed:
            names = "、".join(
                f.get("query", "?") for f in diagnostics.get("github_failures", [])
            )
            lines.append(f"> - GitHub 仓库: {failed}/{total} 个查询失败({names}),仓库条目可能偏少")
        if diagnostics.get("recovered_from_previous"):
            lines.append(
                f"> - 已沿用上一次的部分结果: {'、'.join(diagnostics['recovered_from_previous'])}"
            )
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
            # Mark papers that already have a report so the daily list does not
            # push them again (see load_read_arxiv_ids).
            already = normalize_arxiv_id(p["id"]) in read_ids
            if already:
                priority = "✅ 已研读"
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

    # Top-3 recommendation: skip papers that were already read (they have a
    # report) and pure surveys (protocol §4 routes them to surveys.md).
    candidates = [
        p for p in papers
        if normalize_arxiv_id(p["id"]) not in read_ids and not is_survey(p)
    ]
    top3 = candidates[:3]
    skipped_read = sum(1 for p in papers if normalize_arxiv_id(p["id"]) in read_ids)
    skipped_survey = sum(1 for p in papers if is_survey(p) and normalize_arxiv_id(p["id"]) not in read_ids)

    if top3:
        lines.append("**建议今日深读 (Top 3):**")
        for i, p in enumerate(top3, 1):
            lines.append(f"{i}. [{p['title']}]({p['abs_url']}) — score {p['score']}")
        lines.append("")
    else:
        lines.append("**今日无新的 read_now 候选**(命中论文均已研读或为综述)。")
        lines.append("")

    if skipped_read or skipped_survey:
        notes = []
        if skipped_read:
            notes.append(f"已研读跳过 {skipped_read} 篇")
        if skipped_survey:
            notes.append(f"综述跳过 {skipped_survey} 篇")
        lines.append(f"> 筛选说明:本次 Top 3 已排除({'、'.join(notes)})。")
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


def update_global_index(
    index_path: pathlib.Path,
    run_date: str,
    papers: list[dict[str, Any]],
    read_ids: set[str] | None = None,
) -> None:
    """Append a dated entry to the global research index.

    Two properties matter here:

    1. **Idempotence.**  The same run_date must never get two entries.  The
       local systemd timer and GitHub Actions both target the same day, and
       a re-run of either one used to append a second copy.
    2. **No read papers.**  Papers that already have a report live in the
       "研读报告批次" section of the index; repeating them in the automatic
       Top-5 feed only makes the index harder to navigate.
    """
    if not index_path.exists():
        return
    read_ids = read_ids or set()
    top5 = [
        p for p in papers
        if normalize_arxiv_id(p["id"]) not in read_ids
    ][:5]
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

    # Drop an existing entry for the same date (idempotence).
    entry_re = re.compile(
        rf"(?m)^### {re.escape(run_date)} 自动更新\n.*?(?=^### |\Z)",
        re.DOTALL,
    )
    if entry_re.search(text):
        text = entry_re.sub("", text, count=1)
        text = re.sub(r"\n{3,}", "\n\n", text)

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
    parser.add_argument(
        "--date",
        type=str,
        default=None,
        help=(
            "Run for a specific date (YYYY-MM-DD) instead of today. "
            "Needed to backfill a day whose artifacts were lost -- e.g. "
            "2026-08-06 and 2026-08-26, whose commits were discarded by the "
            "'git reset --hard' in sync_with_origin()."
        ),
    )
    parser.add_argument(
        "--skip-if-done",
        action="store_true",
        help=(
            "Exit 0 without fetching if today's digest already exists and has papers. "
            "Serialises the two schedulers (local systemd timer + GitHub Actions) that "
            "otherwise rewrite the same day's file and diverge the branch. A digest with "
            "0 papers does NOT count as done, so bad days still get retried."
        ),
    )
    parser.add_argument(
        "--render-only",
        action="store_true",
        help=(
            "Re-render the digest and watchlist from an existing "
            "papers/daily/<date>_robotics_research.json without fetching. "
            "Used to recover a day whose JSON survived but whose digest did "
            "not (e.g. after the 'git reset --hard' data loss of 2026-08-06)."
        ),
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.date:
        try:
            run_date = dt.date.fromisoformat(args.date).isoformat()
        except ValueError:
            print(f"[error] invalid --date {args.date!r}, expected YYYY-MM-DD", file=sys.stderr)
            return 2
    else:
        run_date = dt.date.today().isoformat()
    output_root: pathlib.Path = args.output_root.resolve()

    papers_dir = output_root / "papers" / "daily"
    daily_dir = output_root / "docs" / "daily"
    watchlist_dir = output_root / "analysis" / "repo_watchlist"
    for d in [papers_dir, daily_dir, watchlist_dir]:
        d.mkdir(parents=True, exist_ok=True)

    # Serialisation guard. Two schedulers write this repo's daily digest: the
    # local systemd timer (07:00 CST, run_date = CST date) and GitHub Actions
    # (22:30 UTC = 06:30 CST, run_date = UTC date). Because of the 14h offset
    # they target the *same* digest file ~23.5h apart with different arXiv
    # availability, so the second push always loses and rebases conflict on the
    # same JSON. Whoever runs second yields here.
    if args.skip_if_done:
        existing_path = papers_dir / f"{run_date}_robotics_research.json"
        if existing_path.exists():
            try:
                existing = json.loads(existing_path.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                existing = {}
            existing_papers = existing.get("papers") or []
            if existing_papers:
                print(
                    f"[skip] {run_date} 已有 {len(existing_papers)} 篇论文 "
                    f"({existing_path.relative_to(output_root)}), --skip-if-done 生效, 不重复生成"
                )
                return 0
            print(
                f"[warn] {run_date} 的 digest 存在但 0 篇, 视为未完成, 重新抓取以尝试恢复",
                file=sys.stderr,
            )

    print(f"[info] Fetching arXiv /api/query (max {args.max_arxiv})...")
    papers: list[dict[str, Any]] = []
    if args.render_only:
        # Re-render from stored JSON.  No network, no API budget.
        source = papers_dir / f"{run_date}_robotics_research.json"
        if not source.exists():
            print(f"[error] {source} 不存在, 无法 --render-only", file=sys.stderr)
            return 2
        stored = json.loads(source.read_text(encoding="utf-8"))
        papers = stored.get("papers") or []
        repos = stored.get("repos") or []
        models = stored.get("models") or []
        diagnostics = stored.get("diagnostics") or {}
        read_ids = load_read_arxiv_ids(output_root)
        print(
            f"[info] --render-only: 从 {source.name} 读取 "
            f"{len(papers)} papers / {len(repos)} repos / {len(models)} models"
        )
        digest_md = render_daily_digest(run_date, papers, read_ids, diagnostics)
        digest_path = daily_dir / f"{run_date}_robotics_research_digest.md"
        digest_path.write_text(digest_md, encoding="utf-8")
        print(f"[info] Digest:    {digest_path.relative_to(output_root)}")
        watch_md = render_repo_watchlist(run_date, repos, models)
        watch_path = watchlist_dir / f"{run_date}_robotics_repos.md"
        watch_path.write_text(watch_md, encoding="utf-8")
        print(f"[info] Watchlist: {watch_path.relative_to(output_root)}")
        print(f"[done] {run_date} · rendered from stored JSON · {len(papers)} papers")
        return 0
    try:
        papers = fetch_arxiv(args.max_arxiv)
        if not papers:
            raise RuntimeError("arXiv /api/query returned 0 papers (likely HTTP 406 throttle)")
    except Exception as exc:
        print(f"[warn] arXiv /api/query failed: {exc}", file=sys.stderr)
        # Fallback to RSS feeds (less likely to be Varnish-throttled).
        try:
            rss_papers = fetch_arxiv_rss(args.max_arxiv)
            if rss_papers:
                papers = rss_papers
                print(
                    f"[info] RSS fallback recovered {len(rss_papers)} papers across "
                    f"{', '.join(ARCHIVE_RSS_CATEGORIES)}"
                )
            else:
                print("[warn] arXiv RSS fallback returned 0 papers", file=sys.stderr)
        except Exception as rss_exc:
            print(f"[warn] arXiv RSS fallback failed: {rss_exc}", file=sys.stderr)
    print(f"[info] Found {len(papers)} relevant papers")

    print(f"[info] Fetching GitHub repos (per-query {args.github_per_query}, min stars {args.min_stars})...")
    repos, github_failures = fetch_github_repos(args.github_per_query, args.min_stars)
    print(f"[info] Found {len(repos)} repos")
    if github_failures:
        print(
            f"[warn] {len(github_failures)}/{len(GITHUB_QUERIES)} GitHub queries failed: "
            f"{', '.join(f['query'] for f in github_failures)}",
            file=sys.stderr,
        )

    print(f"[info] Fetching HuggingFace models (per-query {args.hf_per_query})...")
    models = fetch_huggingface_models(args.hf_per_query)
    print(f"[info] Found {len(models)} models")

    # Smart recovery: keep yesterday's papers/repos/models if today's run is
    # significantly smaller (avoid downgrading on a flaky network day).
    json_path = papers_dir / f"{run_date}_robotics_research.json"
    previous_payload: dict[str, Any] = {}
    if json_path.exists():
        try:
            previous_payload = json.loads(json_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            previous_payload = {}
    previous_papers = previous_payload.get("papers") or []
    previous_repos = previous_payload.get("repos") or []
    previous_models = previous_payload.get("models") or []
    recovered: list[str] = []
    if previous_papers and len(papers) < len(previous_papers):
        print(
            f"[warn] Keeping previous arXiv result set ({len(previous_papers)}) "
            f"because current run returned {len(papers)}",
            file=sys.stderr,
        )
        papers = previous_papers
        recovered.append("papers")
    if previous_repos and len(repos) < len(previous_repos):
        print(
            f"[warn] Keeping previous GitHub result set ({len(previous_repos)}) "
            f"because current run returned {len(repos)}",
            file=sys.stderr,
        )
        repos = previous_repos
        recovered.append("repos")
    if previous_models and len(models) < len(previous_models):
        print(
            f"[warn] Keeping previous HF result set ({len(previous_models)}) "
            f"because current run returned {len(models)}",
            file=sys.stderr,
        )
        models = previous_models
        recovered.append("models")

    # Save raw JSON
    #
    # `diagnostics` records how complete this run actually was.  Before this
    # field existed, a run whose GitHub queries were rate-limited produced a
    # JSON that looked exactly like a healthy one -- half the repositories
    # were simply missing, and nothing downstream could tell.
    diagnostics = {
        "github_queries_total": len(GITHUB_QUERIES),
        "github_queries_failed": len(github_failures),
        "github_failures": github_failures,
        "recovered_from_previous": recovered,
        "counts": {"papers": len(papers), "repos": len(repos), "models": len(models)},
        "complete": not github_failures and not recovered,
    }
    raw = {
        "run_date": run_date,
        "papers": papers,
        "repos": repos,
        "models": models,
        "diagnostics": diagnostics,
    }
    json_path.write_text(json.dumps(raw, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[info] Raw JSON: {json_path.relative_to(output_root)}")

    # Daily digest
    read_ids = load_read_arxiv_ids(output_root)
    print(f"[info] Already-read papers registered: {len(read_ids)}")
    digest_md = render_daily_digest(run_date, papers, read_ids, diagnostics)
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
        update_global_index(index_path, run_date, papers, read_ids)
        print(f"[info] Updated global index: {index_path.relative_to(output_root)}")

    print(f"[done] {run_date} · {len(papers)} papers · {len(repos)} repos · {len(models)} models")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
