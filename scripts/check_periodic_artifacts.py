#!/usr/bin/env python3
"""Gate for the project's periodic artifacts.

Why this exists
---------------
The protocol (docs/机器人研究协议.md §7) asks for a weekly report and a
monthly synthesis, and a daily fetch.  Until 2026-10-20 all three were
purely descriptive: nothing verified that they existed.

The cost of that was real and is now documented:

* 2026-08-06 and 2026-08-26 were fetched successfully (93 and 89 papers),
  committed locally, and then *lost* -- the push was rejected by the
  GitHub Actions race and ``git reset --hard`` in ``sync_with_origin()``
  wiped the artifacts from the working tree.
* 2026-08 produced **zero** research reports and nobody noticed for two
  months.
* W40-W43 weekly reports and the 2026-07..2026-10 monthly syntheses were
  all missing.

This script turns those three failures into checkable invariants.

Checks
------
1. daily   -- every elapsed day has papers/daily/<date>_robotics_research.json
2. weekly  -- every *completed* ISO week has docs/research/<Y>-W<WW>_周报.md
3. monthly -- every *completed* month has docs/research/<Y>-<MM>_robotics_synthesis.md
4. output  -- completed weeks/months with zero research reports (process stall)
5. partial -- stored daily JSONs whose diagnostics say the fetch was partial
6. dupes   -- the same arXiv ID carrying more than one research report
7. content -- each weekly/monthly artifact satisfies the **content contract**:
   a minimum number of content lines, at least one markdown table, and every
   required element present.  Existence alone is not enough -- an empty-shell
   weekly report used to pass.

Usage
-----
    python3 scripts/check_periodic_artifacts.py            # human report
    python3 scripts/check_periodic_artifacts.py --json     # machine readable
    python3 scripts/check_periodic_artifacts.py --strict   # warnings are failures
    python3 scripts/check_periodic_artifacts.py --check    # quiet, exit code only

Exit codes: 0 = pass, 1 = violations found, 2 = internal error.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import pathlib
import re
import sys
from collections import defaultdict
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parent.parent
RESEARCH_DIR = ROOT / "docs" / "research"
REPORTS_DIR = ROOT / "docs" / "reports"
DAILY_JSON_DIR = ROOT / "papers" / "daily"

ARXIV_ID_RE = re.compile(r"^\d{4}\.\d{4,5}")
REPORT_MD_RE = re.compile(r"^arxiv_id:\s*\"?(\d{4}\.\d{4,5})", re.M)


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------
def iso_weeks_between(start: dt.date, end: dt.date) -> list[tuple[int, int]]:
    """All (iso_year, iso_week) pairs whose week *ended* on or before end.

    The current, not-yet-finished week is excluded on purpose: a weekly
    report is due when the week closes, not on its first day.
    """
    weeks: list[tuple[int, int]] = []
    cursor = start - dt.timedelta(days=start.weekday())  # Monday of start week
    while True:
        week_end = cursor + dt.timedelta(days=6)
        if week_end > end:
            break
        iso = cursor.isocalendar()
        weeks.append((iso.year, iso.week))
        cursor += dt.timedelta(days=7)
    return weeks


def months_between(start: dt.date, end: dt.date) -> list[tuple[int, int]]:
    """All (year, month) pairs whose month *ended* on or before end."""
    months: list[tuple[int, int]] = []
    year, month = start.year, start.month
    while True:
        if month == 12:
            next_month = dt.date(year + 1, 1, 1)
        else:
            next_month = dt.date(year, month + 1, 1)
        if next_month > end:
            break
        months.append((year, month))
        year, month = next_month.year, next_month.month
    return months


def first_artifact_date() -> dt.date | None:
    dates: list[dt.date] = []
    for path in DAILY_JSON_DIR.glob("*_robotics_research.json"):
        try:
            dates.append(dt.date.fromisoformat(path.name[:10]))
        except ValueError:
            continue
    if not dates:
        for path in RESEARCH_DIR.glob("*.md"):
            m = re.match(r"(\d{4}-\d{2})-", path.name)
            if m:
                try:
                    dates.append(dt.date.fromisoformat(m.group(1)))
                except ValueError:
                    continue
    return min(dates) if dates else None


def load_config(root: pathlib.Path) -> dict[str, Any]:
    """Read the baseline configuration.

    The project had two phases with very different cadences (see
    configs/periodic_gate.yaml), so the gate needs to know where the
    "everything must exist" invariant starts.  Without a baseline the gate
    reports 38 historical errors and drowns out real new problems.

    The config file is deliberately **flat** so that the PyYAML path and
    the no-PyYAML fallback parser produce identical results.  An earlier
    nested version (content_contract: weekly: required: [...]) parsed to
    an empty contract under the fallback -- which would have silently
    disabled the content gate on any machine without PyYAML.
    """
    config: dict[str, Any] = {
        "daily_since": "2026-07-01",
        "weekly_since": "2026-W40",
        "monthly_since": "2026-07",
        "allow_prefix_match": True,
        "acknowledged_stalls": [],
        "contract_weekly_min_lines": 25,
        "contract_weekly_required": [],
        "contract_monthly_min_lines": 25,
        "contract_monthly_required": [],
    }
    path = root / "configs" / "periodic_gate.yaml"
    if not path.exists():
        return config
    try:
        import yaml  # type: ignore
    except ImportError:
        # PyYAML is optional: fall back to a tiny parser for this flat file.
        return _parse_simple_yaml(path.read_text(encoding="utf-8"), config)
    try:
        loaded = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except Exception:  # noqa: BLE001
        return config
    if isinstance(loaded, dict):
        config.update(loaded)
    return config


def _parse_simple_yaml(text: str, defaults: dict[str, Any]) -> dict[str, Any]:
    """Minimal YAML reader for configs/periodic_gate.yaml.

    Handles the subset actually used there: ``key: value`` scalars and
    ``key:`` followed by a block list of ``- item`` entries.  Comment-only
    and blank lines are ignored.
    """
    parsed: dict[str, Any] = {}
    current_key: str | None = None
    for raw in text.splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        stripped = raw.strip()
        if stripped.startswith("- ") and current_key is not None:
            item = stripped[2:].strip().strip('"').strip("'")
            bucket = parsed.setdefault(current_key, [])
            if isinstance(bucket, list):
                bucket.append(item)
            continue
        if ":" not in stripped:
            continue
        key, _, value = stripped.partition(":")
        key = key.strip()
        value = value.split("#", 1)[0].strip().strip('"').strip("'")
        if value == "":
            # Either an empty scalar or the head of a block list.
            parsed[key] = []
            current_key = key
            continue
        if value.lower() in ("true", "false"):
            parsed[key] = value.lower() == "true"
        elif re.fullmatch(r"-?\d+", value):
            parsed[key] = int(value)
        else:
            parsed[key] = value
        current_key = None
    for key, value in defaults.items():
        if key not in parsed:
            parsed[key] = value
    # Keys that ended up as empty strings (e.g. a header with no items) fall
    # back to their default instead of becoming falsy-but-wrong values.
    for key, value in list(parsed.items()):
        if value == "":
            parsed[key] = defaults.get(key, value)
    return parsed


def parse_iso_week(value: str) -> tuple[int, int]:
    m = re.match(r"(\d{4})-W(\d{1,2})", str(value).strip())
    if not m:
        raise ValueError(f"bad ISO week: {value!r}")
    return int(m.group(1)), int(m.group(2))


def find_period_file(prefix: str, allow_prefix_match: bool) -> pathlib.Path | None:
    """Find the artifact for a period, tolerating legacy filename variants.

    e.g. 2026-06 may live in "2026-06-30_深度探索_xxx.md" rather than
    "2026-06_robotics_synthesis.md".
    """
    exact = RESEARCH_DIR / f"{prefix}"
    if exact.exists():
        return exact
    if not allow_prefix_match:
        return None
    for path in sorted(RESEARCH_DIR.glob(f"{prefix}*")):
        if path.is_file():
            return path
    return None


def report_dates_by_period() -> tuple[dict[tuple[int, int], int], dict[tuple[int, int], int]]:
    """Count research reports per completed ISO week and per month."""
    by_week: dict[tuple[int, int], int] = defaultdict(int)
    by_month: dict[tuple[int, int], int] = defaultdict(int)
    for path in REPORTS_DIR.glob("*_研读报告.md"):
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        m = re.search(r"^date:\s*(\d{4}-\d{2}-\d{2})", text, re.M)
        if not m:
            continue
        try:
            d = dt.date.fromisoformat(m.group(1))
        except ValueError:
            continue
        iso = d.isocalendar()
        by_week[(iso.year, iso.week)] += 1
        by_month[(d.year, d.month)] += 1
    return by_week, by_month


# --------------------------------------------------------------------------
# checks
# --------------------------------------------------------------------------
def check_daily(start: dt.date, today: dt.date, baseline: dt.date) -> list[dict[str, Any]]:
    problems: list[dict[str, Any]] = []
    cursor = max(start, baseline)
    while cursor <= today:
        iso = cursor.isoformat()
        json_path = DAILY_JSON_DIR / f"{iso}_robotics_research.json"
        digest_path = ROOT / "docs" / "daily" / f"{iso}_robotics_research_digest.md"
        missing: list[str] = []
        if not json_path.exists():
            missing.append("json")
        if not digest_path.exists():
            missing.append("digest")
        if missing:
            problems.append(
                {
                    "check": "daily",
                    "severity": "error",
                    "date": iso,
                    "message": f"缺少每日抓取产物: {', '.join(missing)}",
                }
            )
        cursor += dt.timedelta(days=1)
    return problems


def check_weekly(
    start: dt.date,
    today: dt.date,
    baseline: tuple[int, int],
    allow_prefix: bool,
    acknowledged: set[str],
) -> list[dict[str, Any]]:
    problems: list[dict[str, Any]] = []
    by_week, _ = report_dates_by_period()
    for year, week in iso_weeks_between(start, today):
        if (year, week) < baseline:
            continue
        prefix = f"{year}-W{week:02d}"
        if find_period_file(f"{prefix}_周报", allow_prefix) is None:
            problems.append(
                {
                    "check": "weekly",
                    "severity": "error",
                    "period": prefix,
                    "message": f"缺少周报: docs/research/{prefix}_周报.md",
                }
            )
        elif by_week.get((year, week), 0) == 0 and prefix not in acknowledged:
            problems.append(
                {
                    "check": "weekly-output",
                    "severity": "warning",
                    "period": prefix,
                    "message": f"{prefix} 有周报但 0 篇研读报告(流程可能断档)",
                }
            )
    return problems


def check_monthly(
    start: dt.date,
    today: dt.date,
    baseline: tuple[int, int],
    allow_prefix: bool,
    acknowledged: set[str],
) -> list[dict[str, Any]]:
    problems: list[dict[str, Any]] = []
    _, by_month = report_dates_by_period()
    for year, month in months_between(start, today):
        if (year, month) < baseline:
            continue
        prefix = f"{year}-{month:02d}"
        if find_period_file(f"{prefix}_robotics_synthesis", allow_prefix) is None:
            problems.append(
                {
                    "check": "monthly",
                    "severity": "error",
                    "period": prefix,
                    "message": f"缺少月度合成: docs/research/{prefix}_robotics_synthesis.md",
                }
            )
        elif by_month.get((year, month), 0) == 0 and prefix not in acknowledged:
            problems.append(
                {
                    "check": "monthly-output",
                    "severity": "warning",
                    "period": prefix,
                    "message": f"{prefix} 有月度合成但 0 篇研读报告(流程可能断档)",
                }
            )
    return problems


def check_partial_fetches() -> list[dict[str, Any]]:
    """Flag stored daily JSONs whose own diagnostics say the fetch was partial."""
    problems: list[dict[str, Any]] = []
    for path in sorted(DAILY_JSON_DIR.glob("*_robotics_research.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        diagnostics = data.get("diagnostics")
        if not isinstance(diagnostics, dict):
            # Stored before diagnostics existed.  Unknown, not a failure.
            continue
        if diagnostics.get("complete") is False:
            failed = diagnostics.get("github_queries_failed", 0)
            total = diagnostics.get("github_queries_total", 0)
            problems.append(
                {
                    "check": "partial-fetch",
                    "severity": "warning",
                    "date": path.name[:10],
                    "message": f"抓取不完整: GitHub {failed}/{total} 个查询失败",
                }
            )
    return problems


def check_duplicate_reports() -> list[dict[str, Any]]:
    """Flag one paper carrying more than one research report file."""
    problems: list[dict[str, Any]] = []
    by_id: dict[str, list[str]] = defaultdict(list)
    for path in sorted(REPORTS_DIR.glob("*_研读报告.md")):
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        m = REPORT_MD_RE.search(text)
        arxiv_id = m.group(1) if m else None
        if not arxiv_id:
            m2 = ARXIV_ID_RE.search(path.stem)
            arxiv_id = m2.group(0) if m2 else None
        if arxiv_id:
            by_id[arxiv_id].append(path.name)
    for arxiv_id, names in sorted(by_id.items()):
        if len(names) > 1:
            problems.append(
                {
                    "check": "duplicate-report",
                    "severity": "warning",
                    "arxiv_id": arxiv_id,
                    "message": f"同一论文存在多份研读报告: {', '.join(names)}",
                }
            )
    return problems


# --------------------------------------------------------------------------
# content contract: an artifact must not merely exist, it must have content
# --------------------------------------------------------------------------
def _count_content_lines(text: str) -> int:
    """Non-blank lines that are not pure YAML frontmatter or headings."""
    lines = text.splitlines()
    in_frontmatter = False
    count = 0
    for i, line in enumerate(lines):
        stripped = line.strip()
        if i == 0 and stripped == "---":
            in_frontmatter = True
            continue
        if in_frontmatter:
            if stripped == "---":
                in_frontmatter = False
            continue
        if not stripped or stripped.startswith("#"):
            continue
        count += 1
    return count


def _has_markdown_table(text: str) -> bool:
    return bool(re.search(r"(?m)^\|.*\|.*$", text)) and bool(
        re.search(r"(?m)^\|[\s:|-]+\|", text)
    )


def check_content(
    path: pathlib.Path,
    contract: dict[str, Any],
    kind: str,
    period: str,
) -> list[dict[str, Any]]:
    """Verify a periodic artifact has substance, not just existence."""
    problems: list[dict[str, Any]] = []
    if not path.exists():
        return problems
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        return [
            {
                "check": f"{kind}-content",
                "severity": "error",
                "period": period,
                "message": f"无法读取 {path.name}: {exc}",
            }
        ]

    min_lines = int(contract.get("min_content_lines", 25))
    content_lines = _count_content_lines(text)
    if content_lines < min_lines:
        problems.append(
            {
                "check": f"{kind}-content",
                "severity": "error",
                "period": period,
                "message": (
                    f"{path.name} 正文仅 {content_lines} 行(要求 ≥ {min_lines}),疑似空壳产物"
                ),
            }
        )

    if not _has_markdown_table(text):
        problems.append(
            {
                "check": f"{kind}-content",
                "severity": "error",
                "period": period,
                "message": f"{path.name} 不含任何 markdown 表格,疑似空壳产物",
            }
        )

    for item in contract.get("required") or []:
        name = str(item.get("name", "?"))
        pattern = str(item.get("pattern", ""))
        if not pattern:
            continue
        try:
            hit = re.search(pattern, text)
        except re.error as exc:
            problems.append(
                {
                    "check": f"{kind}-content",
                    "severity": "error",
                    "period": period,
                    "message": f"内容契约配置错误(pattern 无效): {name} — {exc}",
                }
            )
            continue
        if not hit:
            problems.append(
                {
                    "check": f"{kind}-content",
                    "severity": "error",
                    "period": period,
                    "message": f"{path.name} 缺少必需内容: {name}",
                }
            )
    return problems


def parse_contract_items(items: Any) -> list[dict[str, str]]:
    """Normalise contract items to [{name, pattern}, ...].

    The flat config format writes each requirement as "name=regex".  A dict
    form is also accepted so the contract can be expressed programmatically.
    """
    result: list[dict[str, str]] = []
    for item in items or []:
        if isinstance(item, dict):
            name = str(item.get("name", "?"))
            pattern = str(item.get("pattern", ""))
        else:
            text = str(item)
            name, _, pattern = text.partition("=")
            name = name.strip()
            pattern = pattern.strip()
        if not pattern:
            continue
        result.append({"name": name, "pattern": pattern})
    return result


def check_artifact_content(
    start: dt.date, today: dt.date, config: dict[str, Any]
) -> list[dict[str, Any]]:
    """Apply the content contract to every weekly / monthly artifact."""
    problems: list[dict[str, Any]] = []
    allow_prefix = bool(config.get("allow_prefix_match", True))

    weekly_contract = {
        "min_content_lines": int(config.get("contract_weekly_min_lines", 25)),
        "required": parse_contract_items(config.get("contract_weekly_required")),
    }
    monthly_contract = {
        "min_content_lines": int(config.get("contract_monthly_min_lines", 25)),
        "required": parse_contract_items(config.get("contract_monthly_required")),
    }
    if not weekly_contract["required"] and not monthly_contract["required"]:
        return problems

    weekly_baseline = parse_iso_week(str(config["weekly_since"]))
    monthly_baseline = (int(str(config["monthly_since"])[:4]), int(str(config["monthly_since"])[5:7]))

    for year, week in iso_weeks_between(start, today):
        if (year, week) < weekly_baseline:
            continue
        prefix = f"{year}-W{week:02d}"
        path = find_period_file(f"{prefix}_周报", allow_prefix)
        if path is not None:
            problems.extend(check_content(path, weekly_contract, "weekly", prefix))

    for year, month in months_between(start, today):
        if (year, month) < monthly_baseline:
            continue
        prefix = f"{year}-{month:02d}"
        path = find_period_file(f"{prefix}_robotics_synthesis", allow_prefix)
        if path is not None:
            problems.extend(check_content(path, monthly_contract, "monthly", prefix))
    return problems


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------
def collect(start: dt.date, today: dt.date, config: dict[str, Any]) -> list[dict[str, Any]]:
    problems: list[dict[str, Any]] = []
    allow_prefix = bool(config.get("allow_prefix_match", True))
    acknowledged = {str(x) for x in (config.get("acknowledged_stalls") or [])}
    daily_baseline = dt.date.fromisoformat(str(config["daily_since"]))
    weekly_baseline = parse_iso_week(str(config["weekly_since"]))
    monthly_baseline = (int(str(config["monthly_since"])[:4]), int(str(config["monthly_since"])[5:7]))
    problems.extend(check_daily(start, today, daily_baseline))
    problems.extend(check_weekly(start, today, weekly_baseline, allow_prefix, acknowledged))
    problems.extend(check_monthly(start, today, monthly_baseline, allow_prefix, acknowledged))
    problems.extend(check_partial_fetches())
    problems.extend(check_duplicate_reports())
    problems.extend(check_artifact_content(start, today, config))
    return problems


def main() -> int:
    ap = argparse.ArgumentParser(description="Check periodic artifacts exist")
    ap.add_argument("--json", action="store_true", help="emit JSON")
    ap.add_argument("--check", action="store_true", help="quiet, exit code only")
    ap.add_argument("--strict", action="store_true", help="treat warnings as failures")
    ap.add_argument("--root", type=pathlib.Path, default=ROOT)
    args = ap.parse_args()

    today = dt.date.today()
    config = load_config(args.root.resolve())
    start = first_artifact_date()
    if start is None:
        print("[error] no artifacts found, cannot determine project start", file=sys.stderr)
        return 2

    problems = collect(start, today, config)
    errors = [p for p in problems if p["severity"] == "error"]
    warnings = [p for p in problems if p["severity"] == "warning"]

    if args.json:
        print(
            json.dumps(
                {
                    "start": start.isoformat(),
                    "today": today.isoformat(),
                    "baselines": {
                        "daily_since": config["daily_since"],
                        "weekly_since": config["weekly_since"],
                        "monthly_since": config["monthly_since"],
                    },
                    "errors": errors,
                    "warnings": warnings,
                    "ok": not errors and not (args.strict and warnings),
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return 1 if (errors or (args.strict and warnings)) else 0

    if not args.check:
        print(f"周期产物门禁 · {start} ~ {today}")
        print(
            f"基线: 每日 ≥ {config['daily_since']} · 周报 ≥ {config['weekly_since']} "
            f"· 月度 ≥ {config['monthly_since']}"
        )
        print("=" * 68)
        if not problems:
            print("✅ 全部通过:每日抓取、周报、月度合成齐全,无部分抓取、无重复报告。")
        for p in problems:
            icon = "❌" if p["severity"] == "error" else "⚠️ "
            print(f"{icon} [{p['check']}] {p['message']}")
        print("-" * 68)
        print(f"错误 {len(errors)} · 警告 {len(warnings)}")

    return 1 if (errors or (args.strict and warnings)) else 0


if __name__ == "__main__":
    raise SystemExit(main())
