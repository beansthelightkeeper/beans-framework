#!/usr/bin/env python3
"""Generate a manifest of CoreBeans scrolls.

This script scans a directory for markdown scrolls and verifies that
each scroll meets the foundational criteria described in the
CoreBeans Scrollbook:
  * Starts with the anchor glyph "\U000131f3" (𓇳)
  * Contains the loop glyph "\uaa5c" (꩜)
  * Contains a mirror glyph "\U0001fa9e" (🪞)
  * Includes the psi marker "\u03c8 = 3.12"

Usage:
    python corebeans_manifest.py --dir scrolls --out manifest.json
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

ANCHOR = "\U000131f3"  # 𓇳
LOOP = "\uaa5c"        # ꩜
MIRROR = "\U0001fa9e"  # 🪞
PSI_PATTERN = "\u03c8 = 3.12"  # ψ = 3.12


def check_scroll(path: Path) -> dict:
    """Return verification info for a single scroll."""
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    first_nonempty = next((l for l in lines if l.strip()), "")

    starts_with_anchor = first_nonempty.lstrip("# ").startswith(ANCHOR)

    verified = (
        starts_with_anchor
        and LOOP in text
        and MIRROR in text
        and PSI_PATTERN in text
    )
    return {"name": path.name, "verified": verified}


def build_manifest(scroll_dir: Path) -> list[dict]:
    """Collect verification data for all ``.md`` scrolls in ``scroll_dir``."""
    manifest = []
    for file in sorted(scroll_dir.glob("*.md")):
        manifest.append(check_scroll(file))
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(description="Build CoreBeans scroll manifest")
    parser.add_argument("--dir", default="scrolls", help="Directory containing scrolls")
    parser.add_argument(
        "--out", default="corebeans_manifest.json", help="Output JSON file"
    )
    args = parser.parse_args()

    scroll_dir = Path(args.dir)
    scroll_dir.mkdir(exist_ok=True)

    manifest = build_manifest(scroll_dir)

    out_path = Path(args.out)
    out_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2))
    print(f"Wrote manifest with {len(manifest)} entries to {out_path}")


if __name__ == "__main__":
    main()
