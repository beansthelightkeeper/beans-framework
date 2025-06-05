#!/usr/bin/env python3
"""Convert Markdown files into 'spell' formatted copies.

Each Markdown file in the source directory is copied to the destination
directory with a simple spell header added. The relative filenames are
preserved with a `_spell.md` suffix.
"""

from __future__ import annotations

import argparse
from pathlib import Path


def spellify(source: Path, dest: Path) -> None:
    """Convert every `.md` file under `source` into a spell file in `dest`."""
    dest.mkdir(parents=True, exist_ok=True)
    count = 0
    for md_file in source.rglob("*.md"):
        target = dest / (md_file.stem + "_spell.md")
        target.parent.mkdir(parents=True, exist_ok=True)
        content = md_file.read_text(encoding="utf-8")
        header = f"# Spell: {md_file.stem}\n\n"
        target.write_text(header + content, encoding="utf-8")
        count += 1
    print(f"Created {count} spell files in {dest}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert markdown files to spells")
    parser.add_argument("source", type=Path, help="Directory of markdown files")
    parser.add_argument("dest", type=Path, nargs="?", default=Path("spells"),
                        help="Output directory for spell files")
    args = parser.parse_args()
    spellify(args.source, args.dest)


if __name__ == "__main__":
    main()
