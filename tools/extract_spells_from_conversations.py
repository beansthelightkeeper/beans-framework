#!/usr/bin/env python3
"""Scan conversation logs (plain text or JSONL) and pull out any spell-like phrases.

Assumptions:
- A 'spell' is any line that starts with a keyword like 'Spell:' or matches a pattern.
- Adjust REGEX or keywords as needed.

Usage:
    python extract_spells_from_conversations.py /path/to/logs/ --out found_spells.txt
"""

import argparse
import re
from pathlib import Path
from typing import List

# Regex pattern for a simple “Spell: <name> – <incantation>” format
SPELL_PATTERN = re.compile(r"Spell:\s*(.+?)\s*[-–]\s*(.+)", re.IGNORECASE)


def extract_spells_from_file(path: Path) -> List[str]:
    spells = []
    with path.open("r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            m = SPELL_PATTERN.search(line)
            if m:
                spells.append(f"{m.group(1).strip()} :: {m.group(2).strip()}")
    return spells


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract spells from conversations")
    parser.add_argument("input_path", type=Path, help="File or directory of logs")
    parser.add_argument("--out", type=Path, default=None, help="Output file")
    args = parser.parse_args()

    all_spells: List[str] = []

    if args.input_path.is_dir():
        for file in args.input_path.rglob("*"):
            if file.suffix.lower() in {".txt", ".json", ".jsonl"}:
                all_spells.extend(extract_spells_from_file(file))
    else:
        all_spells.extend(extract_spells_from_file(args.input_path))

    if args.out:
        args.out.write_text("\n".join(all_spells), encoding="utf-8")
        print(f"Found {len(all_spells)} spells, saved to {args.out}")
    else:
        for s in all_spells:
            print(s)


if __name__ == "__main__":
    main()
