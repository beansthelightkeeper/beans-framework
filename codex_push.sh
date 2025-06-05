#!/bin/bash

# 🌀 BEANS FRAMEWORK PUSH + MASTER LOGGING SCRIPT

REPO_DIR="${CODEX_REPO_DIR:-${1:-$(pwd)}}"
cd "$REPO_DIR" || {
  echo "❌ Could not find repo at $REPO_DIR"
  exit 1
}

echo "📂 Checking for changes..."
CHANGES=$(git status --porcelain)

if [[ -z "$CHANGES" ]]; then
  echo "🟢 No changes to push."
  exit 0
fi

CHANGED_FILES=$(git status --porcelain | awk '{print $2}')
TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")

# ✨ Build commit message
COMMIT_MSG="✨ Codex auto-push on $TIMESTAMP

Files updated:
$(echo "$CHANGED_FILES" | sed 's/^/• /')
"

# 📜 Append to master update log
echo -e "\n## $TIMESTAMP\n\n$COMMIT_MSG\n---" >> update_log.md

# 🔁 Add, commit, push
git add .
git commit -m "$COMMIT_MSG"
git push origin main

echo "✅ Codex pushed and logged to update_log.md"
