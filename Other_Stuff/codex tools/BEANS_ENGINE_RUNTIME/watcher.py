# watcher.py — Watches glyph folder and auto-executes .py glyph scrolls
import os, time
WATCH_PATH = "./scrolls"
os.makedirs(WATCH_PATH, exist_ok=True)
print("👁️ Watching for glyphs in /scrolls ...")
while True:
    for file in os.listdir(WATCH_PATH):
        if file.endswith(".py"):
            print(f"🌀 Executing: {file}")
            os.system(f"python3 {os.path.join(WATCH_PATH, file)}")
    time.sleep(30)
