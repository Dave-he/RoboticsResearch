#!/usr/bin/env bash
# Daily Robotics Research task runner.
#
# Mirrors scripts/run_daily_lnn_task.sh (sister project):
#   - fetch arXiv / GitHub / HuggingFace
#   - render digest + watchlist, append to global index
#   - sync with origin (fetch + ancestor check + ff-only rebase)
#   - commit + push with rebase retry on rejection
#
# Why the sync dance: local systemd / cron and any other writer can race
# on docs/ papers/ analysis/, which lets local diverge from origin.
# Without sync, push is non-fast-forward and gets rejected (HTTP 406 from
# arXiv has been making past runs return 0 papers, see LNN sister project
# notes 2026-09-03).

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
# Serialise against the GitHub Actions workflow, which also regenerates this
# repo's daily digest (see scripts/daily_robotics_research.py --skip-if-done).
SKIP_IF_DONE="${SKIP_IF_DONE:-1}"

LOG_DIR="$ROOT_DIR/logs"
mkdir -p "$LOG_DIR"
LOG_FILE="$LOG_DIR/daily_cron.log"

# -----------------------------------------------------------------------------
# SSH key: explicit private key + IdentitiesOnly, so cron / non-interactive
# shell can push.  Prefer the project-specific key, fall back to common ones.
# -----------------------------------------------------------------------------
SSH_KEY_OVERRIDE="${SSH_KEY_OVERRIDE:-}"
SSH_KEY=""
for _candidate in "$SSH_KEY_OVERRIDE" "$HOME/.ssh/id_github_dave-he" "$HOME/.ssh/id_ed25519" "$HOME/.ssh/github_rsa" "$HOME/.ssh/id_rsa"; do
  if [[ -n "$_candidate" && -r "$_candidate" ]]; then
    SSH_KEY="$_candidate"
    break
  fi
done
if [[ -n "$SSH_KEY" ]]; then
  export GIT_SSH_COMMAND="ssh -i $SSH_KEY -o IdentitiesOnly=yes -o BatchMode=yes -o StrictHostKeyChecking=accept-new -o ProxyCommand=none"
  echo "[$(date '+%F %T')] ssh key: $SSH_KEY" >> "$LOG_FILE"
fi

# -----------------------------------------------------------------------------
# Git sync with origin.  Order of checks matters: ask "is origin in HEAD"
# before "is HEAD in origin" so a same-state pair isn't misread as "behind".
# -----------------------------------------------------------------------------
git_retry() {
  local max_attempts=5
  local attempt=1
  local sleep_s=4
  while (( attempt <= max_attempts )); do
    if "$@"; then
      return 0
    fi
    echo "[$(date '+%F %T')] [warn] $* 失败, 重试 $attempt/$max_attempts (sleep ${sleep_s}s)" >> "$LOG_FILE"
    sleep "$sleep_s"
    attempt=$((attempt+1))
    sleep_s=$((sleep_s+3))
  done
  return 1
}

sync_with_origin() {
  local branch
  branch="$(git rev-parse --abbrev-ref HEAD)"
  echo "[$(date '+%F %T')] [sync] 拉取 origin/${branch}" >> "$LOG_FILE"
  if ! git_retry git fetch --no-tags origin "$branch"; then
    echo "[$(date '+%F %T')] [error] git fetch 5 次重试均失败, 中止本次运行" >> "$LOG_FILE"
    echo "[error] git fetch 失败, 中止: 在落后的 HEAD 上提交只会让 push 必然被拒" >&2
    return 1
  fi
  if git merge-base --is-ancestor "origin/${branch}" HEAD 2>/dev/null; then
    echo "[$(date '+%F %T')] [sync] 本地已包含 origin/${branch} (相同或领先), 保留本地 commit" >> "$LOG_FILE"
    return 0
  fi
  if git merge-base --is-ancestor HEAD "origin/${branch}" 2>/dev/null; then
    echo "[$(date '+%F %T')] [sync] 本地落后 origin/${branch}, 快进" >> "$LOG_FILE"
    git merge --ff-only "origin/${branch}"
    return 0
  fi

  # 分叉:本地与 origin 各自有提交。此时若直接 reset --hard, 本地那次
  # 未推送成功的提交会连同它的产物文件一起从工作树消失。
  #
  # 历史教训(2026-10-20 定位):2026-08-06 与 2026-08-26 两天抓取完全成功
  # (93 papers / 89 papers),本地提交也建好了,但 push 被 GitHub Actions 抢先
  # 而被拒;随后 sync_with_origin() 走 reset --hard 分支,把这两天的
  # papers/daily/*.json、docs/daily/*_digest.md、analysis/repo_watchlist/*.md
  # 一起抹掉,且永远没有重建 —— 数据永久丢失。
  #
  # 现在先抢救:把「工作树里有、origin 里没有」的每日产物存到临时目录,
  # reset 之后再放回来,让本次提交把它们一并带上。
  local rescue_dir
  rescue_dir="$(mktemp -d)"
  local rescued=0
  for sub in papers/daily docs/daily analysis/repo_watchlist; do
    local dir="$ROOT_DIR/$sub"
    [[ -d "$dir" ]] || continue
    while IFS= read -r -d '' f; do
      local rel="${f#$ROOT_DIR/}"
      if ! git cat-file -e "origin/${branch}:${rel}" 2>/dev/null; then
        mkdir -p "$rescue_dir/$(dirname "$rel")"
        cp -p "$f" "$rescue_dir/$rel"
        rescued=$((rescued + 1))
        echo "[$(date '+%F %T')] [sync] 抢救未推送的产物: ${rel}" >> "$LOG_FILE"
      fi
    done < <(find "$dir" -maxdepth 1 -type f -print0 2>/dev/null)
  done

  echo "[$(date '+%F %T')] [sync] 本地与 origin 分叉, 重置到 origin/${branch} (丢弃本地落后 commit, 当日 digest 会重新生成)" >> "$LOG_FILE"
  echo "[warn] 即将 git reset --hard: 本仓库工作区里未提交的改动会一并丢失" >&2
  git reset --hard "origin/${branch}"

  if (( rescued > 0 )); then
    # 放回被 reset 抹掉的每日产物
    while IFS= read -r -d '' f; do
      local rel="${f#$rescue_dir/}"
      mkdir -p "$(dirname "$ROOT_DIR/$rel")"
      cp -p "$f" "$ROOT_DIR/$rel"
    done < <(find "$rescue_dir" -type f -print0 2>/dev/null)
    echo "[$(date '+%F %T')] [sync] 已恢复 ${rescued} 个未推送的产物文件" >> "$LOG_FILE"
    echo "[info] 已恢复 ${rescued} 个此前未推送成功的每日产物文件"
  fi
  rm -rf "$rescue_dir"
}

# Push with rebase: on rejection, fetch + rebase + retry.  Avoids the
# non-fast-forward trap that today's runs have been hitting.
push_with_rebase() {
  local max_attempts=5
  local attempt=1
  local branch
  branch="$(git rev-parse --abbrev-ref HEAD)"
  while (( attempt <= max_attempts )); do
    if git push origin HEAD; then
      return 0
    fi
    # Capture git's actual stderr. Without this the log only ever said "push 被拒",
    # which cannot distinguish a non-fast-forward (retryable, keep rebasing) from
    # a permission/auth failure (NOT retryable -- 5 rebase attempts can never fix
    # it, and they wasted the whole window on 2026-10-08).
    local push_err
    push_err="$(git push origin HEAD 2>&1 >/dev/null)" || true
    echo "[$(date '+%F %T')] [warn] push 被拒 ($attempt/$max_attempts): ${push_err}" >> "$LOG_FILE"
    if grep -qiE 'permission denied|could not read from remote repository|authentication failed|403' <<< "$push_err"; then
      echo "[$(date '+%F %T')] [error] push 因认证/权限被拒, rebase 无济于事, 提前中止 (检查 SSH key 是否有该仓库写权限)" >> "$LOG_FILE"
      echo "[error] push 被拒: 认证/权限问题,不是 non-fast-forward。检查 GIT_SSH_COMMAND 用的 key 是否对 origin 有写权限。" >&2
      return 1
    fi
    echo "[$(date '+%F %T')]        ↑ 先 rebase 到 origin/${branch} 再重试" >> "$LOG_FILE"
    if ! git fetch --no-tags origin "$branch"; then
      sleep 4
      attempt=$((attempt+1))
      continue
    fi
    if ! git pull --rebase --autostash origin "$branch"; then
      echo "[$(date '+%F %T')] [error] rebase 冲突, 需要人工介入" >> "$LOG_FILE"
      git rebase --abort 2>/dev/null || true
      return 1
    fi
    attempt=$((attempt+1))
    sleep 3
  done
  return 1
}

if [[ "$COMMIT_AND_PUSH" == "1" ]]; then
  sync_with_origin || exit 1
fi

SKIP_FLAG=()
if [[ "$SKIP_IF_DONE" == "1" ]]; then
  SKIP_FLAG=(--skip-if-done)
fi

"$PYTHON_BIN" scripts/daily_robotics_research.py \
    --max-arxiv "$MAX_ARXIV" \
    --github-per-query "$GITHUB_PER_QUERY" \
    --hf-per-query "$HF_PER_QUERY" \
    --min-stars "$MIN_STARS" \
    --output-root "$ROOT_DIR" \
    "${SKIP_FLAG[@]+"${SKIP_FLAG[@]}"}"

# Rebuild the report table in the global index from docs/reports/.
# The table used to be hand-maintained and went stale (it stopped at
# 2026-09-29 while the directory held 30+ reports).  Running this on every
# digest keeps the index's own navigation in sync with the reports.
# --check first so a non-zero exit from a *stale* table never aborts the run.
"$PYTHON_BIN" scripts/build_report_index.py || \
  echo "[$(date '+%F %T')] [warn] build_report_index.py 失败, 索引表可能未同步" >> "$LOG_FILE"

# Periodic artifact gate: verify the daily fetches, weekly reports and
# monthly syntheses exist, and that no *new* period has gone quiet.
#
# This is the check whose absence cost the project two months of silence
# (2026-08 produced zero research reports and nobody noticed until
# 2026-10-20).  It is deliberately non-fatal: a missing weekly report must
# not stop tomorrow's digest from being produced.  The signal is the log
# line and the GitHub Actions gate workflow.
echo "[$(date '+%F %T')] [gate] 周期产物门禁" >> "$LOG_FILE"
if ! "$PYTHON_BIN" scripts/check_periodic_artifacts.py >> "$LOG_FILE" 2>&1; then
  echo "[$(date '+%F %T')] [warn] 周期产物门禁未通过 —— 见上方日志(缺失的每日抓取 / 周报 / 月度合成)" >> "$LOG_FILE"
  echo "[warn] 周期产物门禁未通过, 详情见 logs/daily_cron.log"
fi

if [[ "$COMMIT_AND_PUSH" == "1" ]]; then
  # scripts/ and configs/ are included so that a script or gate-config fix
  # is not stranded on the local machine while the artifacts it governs are
  # pushed.  Matches the GitHub Actions workflow's `git add` list.
  git add docs papers analysis scripts configs
  if ! git diff --cached --quiet; then
    git commit -m "chore(daily): update RoboticsResearch digest ${RUN_DATE}"
    if ! push_with_rebase; then
      echo "[$(date '+%F %T')] [error] push 重试 + rebase 均失败, 留待下次 cron 修复" >> "$LOG_FILE"
      exit 1
    fi
  else
    echo "No daily RoboticsResearch changes to commit."
  fi
fi
