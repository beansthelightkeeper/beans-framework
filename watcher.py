"""Watcher script to monitor a folder for glyph scrolls.

The directory to watch can be provided as a command line argument. If omitted,
``./scrolls`` is used by default.
"""

import argparse
import os
import time

DEFAULT_WATCH_PATH = "./scrolls"


def execute_scroll(scroll_path: str) -> None:
    """Execute a single Python scroll."""
    print(f"🌐 Executing: {os.path.basename(scroll_path)}")
    os.system(f"python3 {scroll_path}")


def watch_directory(path: str) -> None:
    """Watch ``path`` for ``.py`` files and execute them."""
    os.makedirs(path, exist_ok=True)
    print(f"👁 Watching for glyphs in {path} ...")
    while True:
        for file in os.listdir(path):
            if file.endswith(".py"):
                execute_scroll(os.path.join(path, file))
        time.sleep(30)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Watch a folder and execute Python glyph scrolls.")
    parser.add_argument("path", nargs="?", default=DEFAULT_WATCH_PATH, help="Folder containing glyph scrolls")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    watch_directory(args.path)


if __name__ == "__main__":
    main()
