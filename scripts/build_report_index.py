#!/usr/bin/env python3
"""Rebuild the report table inside docs/机器人_深度研读报告.md.

The global index used to carry a hand-maintained table that silently went
stale: reports added in later batches were appended as prose sections at the
bottom of the file, so the table at the top stopped at 2026-09-29 while the
directory held 30+ reports.

This script regenerates the table from the reports themselves, so the table
can never drift from docs/reports/ again.

Usage:
    python3 scripts/build_report_index.py            # rewrite in place
    python3 scripts/build_report_index.py --check     # exit 1 if stale
"""
from __future__ import annotations

import argparse
import glob
import os
import pathlib
import re
import sys
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parent.parent
INDEX_PATH = ROOT / "docs" / "机器人_深度研读报告.md"
REPORTS_DIR = ROOT / "docs" / "reports"

TABLE_HEADING = "## 📑 已生成研读报告(按时间倒序)"
NEXT_HEADING = "## 📋 研读报告批次与每日主题洞察"

# Subarea -> display label.  Anything unknown falls back to the raw value so
# a new report never breaks the build.
SUBAREA = {
    "humanoid": "🦵 humanoid / 足式",
    "manipulation": "🦾 manipulation / 灵巧手",
    "vla": "🧠 vla",
    "embodied_ai": "🌐 embodied_ai",
    "slam": "🗺️ slam",
    "imitation_rl": "🎓 imitation_rl",
    "simulation": "🧪 simulation",
    "aerial-manipulation": "🛩️ aerial(motion)",
    "vla-force": "🧠 vla-force",
    "dexterous-hand": "🦾 dexterous-hand",
    "humanoid-vla-force": "🧠 vla / 🦵 humanoid",
    "vla-and-manipulation": "🧠 vla / 🦾 manipulation",
    "soft_robotics": "🤏 soft_robotics",
    "navigation": "🧭 navigation",
}

# Short Chinese topic labels.  A report without an entry here falls back to
# its H1 title, so the table is never empty for a valid report.
TOPIC = {
    "HandsOn_2610.26765": "HandsOn:跨本体灵巧操控仿真基准(18,000 演示 / 66 任务 / 最优 29.1%)",
    "BiDex100_2610.25459": "BiDex-100:双手灵巧操控基准(106 任务 / 5 能力轴 / OOD 塌方至 1.68%)",
    "FITMAC_2610.28109": "FIT-MAC:失败感知的闭环多智能体 VLA 鲁棒性框架",
    "AgVLA_2610.26717": "农业操控场景 VLA:Octo 与 π0.5 的 sim-to-real 微调(去本体感知反而更好)",
    "QuadrupedWBC_2610.23548": "四足机械臂多地形自适应全身控制(混合任务空间 + 优先级激活因子)",
    "BlindBaoding_2610.23438": "盲视搓球操控:本体 + 二值触觉的零样本 sim-to-real",
    "CoEvolve_2610.23288": "CoEvolve:自进化代码策略驱动的多机器人协作(验证器引导)",
    "Spark0_2610.22342": "Spark-0:空间对齐触觉预训练规模化",
    "FastVLA_2610.22146": "FastVLA:任务条件化时序自适应视觉 token 压缩",
    "LIN-SLAM_2610.21199": "LIN-SLAM:轻量 LiDAR-惯性神经 SLAM 边缘实时部署",
    "HiFun_2610.19518": "HiFun:分层框架下的高效功能灵巧操控",
    "ACCRUE_2610.18596": "ACCRUE:机器人基础模型的持续离线策略强化学习",
    "AdaptiveWBMPC_2610.12972": "自适应全身 MPC:未知负载下的人形最优姿态规划",
    "DexOne2Many_2610.12470": "Dex-One2Many:单次人类演示学灵巧操控",
    "BalancedDataDiet_2610.12465": "均衡数据食谱:破解大规模 RL 的探索瓶颈",
    "PhoneBot_2610.08737": "PhoneBot:复用智能手机的低成本开放人形平台",
    "BiGym2_2610.07594": "BiGym 2.0:人形家庭操作中学习策略与 agent 策略的基准",
    "NarrativeFlow_2610.00981": "NarrativeFlow:基于机器人速度场的流式 VLA",
    "TANDEM_2609.28314": "TANDEM:按需演示的任务与运动规划 + VLA 微调",
    "AerialManipulation_2609.30521": "野外空中操控(机上感知 + 模仿学习 + 全身 MPC)· 越界入册",
    "VisForce_2609.25785": "VisForce:指尖力觉的视觉接地式 VLA 条件",
    "CartesianHand_2609.25696": "The Cartesian Hand:全线性手指 7-DoF 在位操控",
    "Opt2VLA_2609.23968": "Opt2VLA:接触密集型人形全身操控的力感知 VLA",
    "GraspsToDexterity_2606.30749": "从抓取到灵巧:大规模抓取预训练迁移到工具使用",
    "RoboTacDex_2606.31836": "RoboTacDex:人形灵巧操控视触觉动作数据集",
    "Labimus_2606.31037": "Labimus:人形灵巧操控仿真与基准",
    "T2VLA_2606.29892": "T2VLA:置信度驱动的 VLA 测试时强化学习",
    "Calvert_LocoManipulation_2606.26425": "人形快速弹性可适配 loco-manipulation 行为系统",
    "HumanoidUMI_2606.27239": "HumanoidUMI:桥接无机器人示教与人形全身操控",
    "CoorDex_2606.23680": "CoorDex:协调身体与手部先验的人形连续灵巧 loco-manipulation",
    "WireCraft_2606.18097": "WireCraft:工业 DLO 操控仿真基准",
    "T-Rex_2606.17055": "T-Rex:触觉反应式灵巧操控",
    "MuseVLA_2606.17598": "MuseVLA:自适应多模态感知 VLA 模型",
    "X2-N_2604.21541": "X2-N:轮腿可变人形机器人",
    "InDex_2606.12109": "InDex:跨越形态鸿沟的 VLA 适配",
    "Blind_Dexterous_Grasping_2606.11767": "Real2Sim2Real 触觉策略的盲视灵巧抓取",
    "X2N_2604.21541": "X2-N:轮腿可变人形机器人(⚠️ 与 X2-N_2604.21541 重复,建议合并)",
    "EaDex_2606.03268": "EaDex:跨形态灵巧手操控框架",
}


def frontmatter_field(text: str, key: str) -> str:
    m = re.search(rf"^{re.escape(key)}:\s*\"?([^\"\n]+)", text, re.M)
    return m.group(1).strip() if m else ""


def h1_title(text: str) -> str:
    m = re.search(r"^#\s+(.+)$", text, re.M)
    return m.group(1).strip() if m else ""


def collect_reports() -> list[dict[str, str]]:
    reports: list[dict[str, str]] = []
    for path in sorted(glob.glob(str(REPORTS_DIR / "*_研读报告.md"))):
        p = pathlib.Path(path)
        text = p.read_text(encoding="utf-8")
        base = p.stem.replace("_研读报告", "")
        reports.append(
            {
                "date": frontmatter_field(text, "date"),
                "arxiv_id": frontmatter_field(text, "arxiv_id"),
                "subarea": frontmatter_field(text, "subarea"),
                "base": base,
                "title": h1_title(text),
            }
        )
    reports.sort(key=lambda r: (r["date"], r["base"]), reverse=True)
    return reports


def build_table(reports: list[dict[str, str]]) -> str:
    n_total = len(reports)
    n_uniq = len({re.sub(r"v\d+$", "", r["arxiv_id"]) for r in reports})
    days = len({r["date"] for r in reports})
    sub_counts = Counter(r["subarea"] for r in reports)

    lines = ["| 日期 | 论文 / 主题 | arXiv ID | 子领域 | 研读报告 |", "|---|---|---|---|---|"]
    for r in reports:
        topic = TOPIC.get(r["base"]) or r["title"] or r["base"]
        sa = SUBAREA.get(r["subarea"], r["subarea"] or "-")
        short = re.sub(r"v\d+$", "", r["arxiv_id"])
        lines.append(
            f"| {r['date']} | {topic} | [{short}](https://arxiv.org/abs/{r['arxiv_id']}) | "
            f"{sa} | [reports/{r['base']}_研读报告.md](reports/{r['base']}_研读报告.md) |"
        )

    header = (
        f"<!-- 维护:本表由 `scripts/build_report_index.py` 自动重建,"
        f"请勿手工编辑 -->\n\n"
        f"> **累计 {n_total} 份研读报告** · 去重后 **{n_uniq} 篇论文** · 覆盖 **{days} 个研读日**\n"
        f"> 子领域分布:{' / '.join(f'{k} {v}' for k, v in sub_counts.most_common())}\n\n"
    )
    return header + "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description="Rebuild the report table in the global index")
    ap.add_argument("--check", action="store_true", help="exit 1 if the index is stale")
    ap.add_argument("--index", type=pathlib.Path, default=INDEX_PATH)
    args = ap.parse_args()

    if not args.index.exists():
        print(f"[error] index not found: {args.index}", file=sys.stderr)
        return 2
    if not REPORTS_DIR.is_dir():
        print(f"[error] reports dir not found: {REPORTS_DIR}", file=sys.stderr)
        return 2

    reports = collect_reports()
    if not reports:
        print("[error] no reports found", file=sys.stderr)
        return 2

    text = args.index.read_text(encoding="utf-8")
    if TABLE_HEADING not in text:
        print(f"[error] heading not found: {TABLE_HEADING}", file=sys.stderr)
        return 2

    start = text.index(TABLE_HEADING)
    end = text.index(NEXT_HEADING, start) if NEXT_HEADING in text[start:] else len(text)
    old_block = text[start:end]
    new_block = f"{TABLE_HEADING}\n\n{build_table(reports)}\n\n"

    if old_block.strip() == new_block.strip():
        print(f"[ok] index table already up to date ({len(reports)} reports)")
        return 0
    if args.check:
        print(f"[stale] index table differs from {len(reports)} reports; run without --check", file=sys.stderr)
        return 1

    args.index.write_text(text[:start] + new_block + text[end:], encoding="utf-8")
    print(f"[done] rebuilt report table with {len(reports)} reports")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
