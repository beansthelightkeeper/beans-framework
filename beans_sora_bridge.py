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


def bridge_loop(gallery: str, dest: str, delay: int = DELAY) -> None:
    """Continuously route images from ``gallery`` into ``dest``."""
    print(f"🩸 Beans ↔ Sora bridge watching {gallery} ...")
    seen = set()
    while True:
        for file in os.listdir(gallery):
            if file.lower().endswith((".png", ".jpg", ".jpeg")) and file not in seen:
                src = os.path.join(gallery, file)
                dst = os.path.join(dest, file)
                shutil.copy(src, dst)
                wrap_for_sora(dst)
                seen.add(file)
                print(f"🌈 Routed + wrapped: {file}")
        time.sleep(delay)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Route images from Beans to Sora")
    parser.add_argument("--gallery", help="Folder to watch for images", default=GALLERY_PATH)
    parser.add_argument("--dest", help="Destination for Sora imports", default=SORA_IMPORTS)
    parser.add_argument("--delay", type=int, default=DELAY, help="Seconds between checks")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    bridge_loop(args.gallery, args.dest, args.delay)


if __name__ == "__main__":
    main()
