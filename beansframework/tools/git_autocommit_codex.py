import os
import subprocess
from datetime import datetime

CODEX_DIR = "."  # adjust if needed
COMMIT_MESSAGE = f"\ud83d\udcdc auto-sync @ {datetime.utcnow().isoformat()}"

def has_changes():
    result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
    return result.stdout.strip() != ""

def commit_and_push():
    os.system("git add .")
    os.system(f"git commit -m \"{COMMIT_MESSAGE}\"")
    os.system("git push")
    print("\u2705 Codex scrolls committed + pushed to LoopCloud")

if __name__ == "__main__":
    if has_changes():
        print("\U0001fa9e Changes detected in Codex. Looping them back to Source...")
        commit_and_push()
    else:
        print("\u2600\ufe0f  No changes found. All scrolls already mirrored.")
