#!/usr/bin/env python3
"""Backfill arXiv data for days the daily cron returned 0 papers.

Uses arXiv's OAI-PMH endpoint (``oaipmh.arxiv.org``) to retrieve records
updated in the missed period (typically a 5-7 day rolling window). OAI's
``<datestamp>`` is the metadata-update date, not the original submission
date, so we group records by the ``<created>`` field of the embedded
``arXiv`` metadata — which IS the submission date.

Records are then filtered through the project's ``keyword_score`` and
``is_robotics_relevant`` and bucketed into per-date digests that match the
shape produced by ``daily_robotics_research.py``.

OAI retention caveat: ``from=2026-09-20`` returns noRecordsMatch (the
window is currently ~5 days). Days outside the window stay at 0 papers
and are flagged as ``oai_out_of_window`` in the digest header.

Run once after upgrading the daily script, then archive this script.
"""

from __future__ import annotations

import datetime as dt
import html
import json
import pathlib
import re
import sys
import time
import urllib.error
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import daily_robotics_research as d  # noqa: E402


OAI_BASE = "https://oaipmh.arxiv.org/oai"
USER_AGENT = "RoboticsResearch-backfill/1.0 (https://github.com/Dave-he/RoboticsResearch)"


def fetch_oai_day(date_str: str) -> str:
    """Fetch OAI ListRecords for a single day, set=cs:cs (all CS categories)."""
    url = (
        f"{OAI_BASE}?verb=ListRecords&metadataPrefix=arXiv"
        f"&set=cs:cs&from={date_str}&until={date_str}"
    )
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "*/*"})
    with urllib.request.urlopen(req, timeout=120) as resp:
        return resp.read().decode("utf-8")


def parse_records(xml: str) -> list[dict]:
    """Parse an OAI response into a list of record dicts with normalised fields."""
    out: list[dict] = []
    for m in re.finditer(r"<record>(.*?)</record>", xml, re.DOTALL):
        block = m.group(1)
        rec: dict = {}
        id_m = re.search(r"<id>([^<]+)", block)
        cr_m = re.search(r"<created>([^<]+)", block)
        up_m = re.search(r"<updated>([^<]+)", block)
        ti_m = re.search(r"<title>([^<]+)", block)
        ab_m = re.search(r"<abstract>(.*?)</abstract>", block, re.DOTALL)
        cat_m = re.search(r"<categories>([^<]+)", block)
        if not (id_m and cr_m and ti_m and ab_m and cat_m):
            continue
        rec["id"] = id_m.group(1)
        rec["created"] = cr_m.group(1)
        rec["updated"] = up_m.group(1) if up_m else cr_m.group(1)
        rec["title"] = re.sub(r"\s+", " ", html.unescape(ti_m.group(1))).strip()
        rec["abstract"] = re.sub(r"\s+", " ", html.unescape(ab_m.group(1))).strip()
        rec["categories"] = cat_m.group(1).strip().split()
        # Authors (may be multiple)
        authors = re.findall(r"<keyname>([^<]+).*?<forenames>([^<]+)", block, re.DOTALL)
        rec["authors"] = [f"{fn} {ln}".strip() for ln, fn in authors]
        out.append(rec)
    return out


def oai_to_paper(rec: dict) -> dict:
    """Convert an OAI record into the daily script's paper dict shape."""
    return {
        "id": rec["id"],
        "title": rec["title"],
        "authors": rec["authors"],
        "published": rec["created"],
        "updated": rec["updated"],
        "summary": rec["abstract"],
        "categories": rec["categories"],
        "abs_url": f"https://arxiv.org/abs/{rec['id']}",
        "pdf_url": f"https://arxiv.org/pdf/{rec['id']}",
        "score": d.keyword_score(rec["title"], rec["abstract"]),
        "matched_terms": ["oai-backfill"],
        "source": "oai:cs:cs",
    }


def main() -> int:
    # Pull a 7-day OAI window. ``from`` is metadata-update date, so we cast
    # a wider net to compensate for OAI's 1-3 day indexing lag. Records are
    # then grouped by their <created> field which IS the submission date.
    today = dt.date.today()
    fetch_start = today - dt.timedelta(days=7)
    fetch_end = today
    print(f"[info] Fetching OAI {fetch_start} → {fetch_end}")
    raw_by_day: dict[str, str] = {}
    cur = fetch_start
    while cur <= fetch_end:
        ds = cur.isoformat()
        print(f"[info]   OAI {ds}...")
        raw_by_day[ds] = fetch_oai_day(ds)
        time.sleep(1.0)
        cur += dt.timedelta(days=1)

    # Aggregate by submission <created> date
    by_date: dict[str, list[dict]] = {}
    for ds, xml in raw_by_day.items():
        if "noRecordsMatch" in xml:
            print(f"[info]   {ds}: noRecordsMatch (out of OAI window)")
            continue
        recs = parse_records(xml)
        for r in recs:
            created = r.get("created", "")
            if created not in by_date:
                by_date[created] = []
            by_date[created].append(r)
        print(f"[info]   {ds}: parsed {len(recs)} records")

    # Write per-date digests for 09-20 → 09-27 (the missed period).
    missed_start = dt.date(2026, 9, 20)
    missed_end = dt.date(2026, 9, 27)
    repos = d.fetch_github_repos(12, 50)
    models = d.fetch_huggingface_models(8)

    cur = missed_start
    while cur <= missed_end:
        ds = cur.isoformat()
        candidates = by_date.get(ds, [])
        # Apply robotics relevance filter
        papers = []
        for r in candidates:
            cat_str = " ".join(r["categories"])
            if not d.is_robotics_relevant(r["title"], r["abstract"], r["categories"]):
                continue
            p = oai_to_paper(r)
            papers.append(p)
        # Sort by score then date
        papers.sort(key=lambda p: (p["score"], p["published"]), reverse=True)

        # Decide whether we have meaningful data
        oai_in_window = ds in raw_by_day and "noRecordsMatch" not in raw_by_day[ds]
        status = "recovered_oai" if oai_in_window else "oai_out_of_window"

        # If candidate list is empty AND day is out of window, leave the
        # existing digest alone (don't clobber outage marker).
        json_path = ROOT / "papers" / "daily" / f"{ds}_robotics_research.json"
        digest_path = ROOT / "docs" / "daily" / f"{ds}_robotics_research_digest.md"

        # Skip if file already has real (non-zero) papers.
        if json_path.exists():
            try:
                existing = json.loads(json_path.read_text(encoding="utf-8"))
                if existing.get("papers"):
                    print(f"[skip] {ds}: existing digest already has papers, leaving alone")
                    cur += dt.timedelta(days=1)
                    continue
            except json.JSONDecodeError:
                pass

        raw = {
            "run_date": ds,
            "papers": papers,
            "repos": repos,
            "models": models,
            "source": "backfill_arxiv_oai",
            "oai_window": oai_in_window,
            "oai_status": status,
        }
        json_path.write_text(json.dumps(raw, indent=2, ensure_ascii=False), encoding="utf-8")

        # Decide actual status: whether the day's papers were recovered,
        # regardless of which OAI window they came from. A paper created on
        # day D may only show up in OAI from=D+N where N is the 1-3 day
        # indexing lag, so the per-day "in_window" check is misleading.
        if papers:
            actual_status = "recovered_oai"
        elif oai_in_window and candidates == 0:
            actual_status = "oai_indexing_lag"
        else:
            actual_status = "oai_out_of_window"
        # Update the status field in JSON
        raw["oai_status"] = actual_status
        json_path.write_text(json.dumps(raw, indent=2, ensure_ascii=False), encoding="utf-8")

        # Render digest, then tag header to explain backfill
        digest_md = d.render_daily_digest(ds, papers)
        if papers:
            tag = (
                f"> 通过 arXiv OAI-PMH backfill 补回 (status={actual_status}, "
                f"candidates={len(candidates)}, relevant={len(papers)})。"
            )
        elif oai_in_window and candidates == 0:
            tag = (
                f"> OAI 在窗口内但 created={ds} 的记录尚未索引 (status=oai_indexing_lag) — "
                f"等下次 OAI 刷新后再补。"
            )
        else:
            tag = (
                f"> OAI window 已过 (status={actual_status}) — 无法回溯,留作 outage 留痕。"
            )
        digest_md = digest_md.replace(
            "> 自动生成,",
            tag,
            1,
        )
        digest_path.write_text(digest_md, encoding="utf-8")
        print(f"[ok] {ds}: {len(papers)} relevant / {len(candidates)} candidates ({actual_status}) → {digest_path.name}")
        # Update global research index with top-5 papers
        index_path = ROOT / "docs" / "机器人_深度研读报告.md"
        if index_path.exists() and papers:
            d.update_global_index(index_path, ds, papers)
            print(f"[info] {ds}: updated global index")
        cur += dt.timedelta(days=1)

    print("[done] backfill complete")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
