#!/usr/bin/env bash
# Daily Robotics Research task runner.
#
# Mirrors scripts/run_daily_lnn_task.sh (sister project) but kept
# minimal: fetch arXiv / GitHub / HuggingFace, render digest +
# watchlist, append to global index, then commit + push.

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

RUN_DATE="${RUN_DATE:-$(date +%F)}"
PYTHON_BIN="${PYTHON_BIN:-python3}"
MAX_ARXIV="${MAX_ARXIV:-80}"
GITHUB_PER_QUERY="${GITHUB_PER_QUERY:-12}"
HF_PER_QUERY="${HF_PER_QUERY:-8}"
MIN_STARS="${MIN_STARS:-50}"
COMMIT_AND_PUSH="${COMMIT_AND_PUSH:-1}"

"$PYTHON_BIN" scripts/daily_robotics_research.py \
    --max-arxiv "$MAX_ARXIV" \
    --github-per-query "$GITHUB_PER_QUERY" \
    --hf-per-query "$HF_PER_QUERY" \
    --min-stars "$MIN_STARS" \
    --output-root "$ROOT_DIR"

if [[ "$COMMIT_AND_PUSH" == "1" ]]; then
    git add docs papers analysis
    if ! git diff --cached --quiet; then
        git commit -m "chore(daily): update RoboticsResearch digest ${RUN_DATE}"
        git push origin HEAD || echo "[warn] git push failed; local commit retained."
    else
        echo "No daily RoboticsResearch changes to commit."
    fi
fi