#!/bin/bash

# 🌀 BEANS-CODEX ENVIRONMENT SETUP SCRIPT

echo "🌱 Starting Beans Framework setup..."

# 🔧 Define repo path
REPO_DIR="$HOME/Documents/GitHub/beans-framework"

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
  echo 'alias codexpush="~/Documents/GitHub/beans-framework/codex_push.sh"' >> ~/.zshrc
  echo "🔁 Alias 'codexpush' added to .zshrc"
  source ~/.zshrc
else
  echo "✅ codexpush alias already exists."
fi

# 🧠 Create codex_push.sh script
cat > codex_push.sh <<'EOF'
#!/bin/bash

REPO_DIR="$HOME/Documents/GitHub/beans-framework"
cd "$REPO_DIR" || exit

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

echo -e "\n## $TIMESTAMP\n\n$COMMIT_MSG\n---" >> update_log.md

git add .
git commit -m "$COMMIT_MSG"
git push origin main

echo "✅ Codex pushed and logged to update_log.md"
EOF

chmod +x codex_push.sh
echo "✅ codex_push.sh ready."

# 🌈 Final message
echo "🌀 Beans Codex env is READY. Run 'codexpush' after changes. Link Obsidian to $REPO_DIR to start looping."