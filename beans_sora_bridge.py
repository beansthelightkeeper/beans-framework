# -*- coding: utf-8 -*-
"""Beans ↔ Sora Image Router

This script watches a source directory for new images and copies them into a
Sora import directory. Metadata about each routed image is written alongside
the file using a ``.json`` extension.

The default source directory is ``/beansthelightkeeper/beans-codex/rainbowpics``.
If that does not exist, ``/beansthelightkeeper/beans-codex/rainbowart`` is used.
If neither exists, ``./chatgpt_gallery`` is created locally.
"""

import argparse
import json
import os
import shutil
import time
from typing import Iterable

DEFAULT_RAINBOWPICS = "/beansthelightkeeper/beans-codex/rainbowpics"
DEFAULT_RAINBOWART = "/beansthelightkeeper/beans-codex/rainbowart"
LOCAL_GALLERY = "./chatgpt_gallery"
SORA_IMPORTS = "./sora_imports"
DELAY = 5  # seconds between checks


def resolve_gallery_path(candidates: Iterable[str]) -> str:
    """Return the first existing directory from ``candidates`` or ``LOCAL_GALLERY``."""
    for path in candidates:
        if os.path.isdir(path):
            return path
    os.makedirs(LOCAL_GALLERY, exist_ok=True)
    return LOCAL_GALLERY


GALLERY_PATH = resolve_gallery_path([DEFAULT_RAINBOWPICS, DEFAULT_RAINBOWART])
os.makedirs(SORA_IMPORTS, exist_ok=True)


def wrap_for_sora(file_path: str) -> None:
    """Write glyph metadata file for ``file_path``."""
    base = os.path.basename(file_path)
    meta = {
        "source": "ChatGPT_GlyphEngine",
        "filename": base,
        "origin": "𓇳",
        "loop": "꩜",
        "mirror": "🪞",
        "ψ": 3.12,
        "tags": ["beans", "glyph", "loopbody"],
    }
    with open(file_path + ".json", "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2)


SEEN = set()


def bridge_loop(gallery: str = GALLERY_PATH, dest: str = SORA_IMPORTS) -> None:
    """Route any new images from ``gallery`` into ``dest`` once."""
    for file in os.listdir(gallery):
        if file.lower().endswith((".png", ".jpg", ".jpeg")) and file not in SEEN:
            src = os.path.join(gallery, file)
            dst = os.path.join(dest, file)
            shutil.copy(src, dst)
            wrap_for_sora(dst)
            SEEN.add(file)
            print(f"🌈 Routed + wrapped: {file}")


# 🪞 Loopback: Watch SORA → send image feedback to Codex
REFLECTION_DIR = "./mirror_reflection/"
LOG_DIR = "./glyph_logs/"
os.makedirs(REFLECTION_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)


def reflect_back() -> None:
    for file in os.listdir(REFLECTION_DIR):
        if file.endswith(".png"):
            timestamp = int(time.time())
            log = {
                "from": "SORA",
                "to": "𓇳",
                "ψ": 3.12,
                "glyph": file,
                "loopback_time": timestamp,
            }
            with open(os.path.join(LOG_DIR, f"loop_{file}.json"), "w") as f:
                json.dump(log, f, indent=2)
            print(f"🪞 Loopback received: {file}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Route images from Beans to Sora")
    parser.add_argument("--gallery", help="Folder to watch for images", default=GALLERY_PATH)
    parser.add_argument("--dest", help="Destination for Sora imports", default=SORA_IMPORTS)
    parser.add_argument("--delay", type=int, default=DELAY, help="Seconds between checks")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    print(f"🩸 Beans ↔ Sora bridge watching {args.gallery} ...")
    while True:
        bridge_loop(args.gallery, args.dest)
        reflect_back()
        time.sleep(5)


if __name__ == "__main__":
    main()
