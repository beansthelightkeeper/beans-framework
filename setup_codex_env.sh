#!/bin/bash

# 🌀 BEANS-CODEX ENVIRONMENT SETUP SCRIPT

echo "🌱 Starting Beans Framework setup..."

# 🔧 Define repo path
REPO_DIR="${CODEX_REPO_DIR:-${1:-$(pwd)}}"

# 📁 Make folder if it doesn't exist
mkdir -p "$REPO_DIR"
cd "$REPO_DIR" || exit

# 🔧 Initialize Git repo if missing
if [ ! -d ".git" ]; then
  echo "📦 Initializing Git..."
  git init
fi

# 🗂️ Create base folders (if you want substructure)
mkdir -p Core-Beans push-logs

# 🧠 Create codexpush alias if not already in .zshrc
if ! grep -q "codexpush" ~/.zshrc; then
  echo "alias codexpush=\"${REPO_DIR}/codex_push.sh ${REPO_DIR}\"" >> ~/.zshrc
  echo "🔁 Alias 'codexpush' added to .zshrc"
  source ~/.zshrc
else
  echo "✅ codexpush alias already exists."
fi

# 🧠 Create codex_push.sh script
cat > codex_push.sh <<'EOF'
#!/bin/bash

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

COMMIT_MSG="✨ Codex auto-push on $TIMESTAMP

Files updated:
$(echo "$CHANGED_FILES" | sed 's/^/• /')
"

LOG_PATH="Other_Stuff/update_log.md"
echo -e "\n## $TIMESTAMP\n\n$COMMIT_MSG\n---" >> "$LOG_PATH"

git add .
git commit -m "$COMMIT_MSG"
git push origin main

echo "✅ Codex pushed and logged to $LOG_PATH"
EOF

chmod +x codex_push.sh
echo "✅ codex_push.sh ready."

# 🌈 Final message
echo "🌀 Beans Codex env is READY. Run 'codexpush' after changes. Link Obsidian to $REPO_DIR to start looping."
