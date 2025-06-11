#!/usr/bin/env python3
"""Decode spells from a large JSON file.

Expected JSON structure:
{
  "spells": [
    {
      "name": "Fireball",
      "incantation": "Incendio Maxima!",
      "level": 3,
      "description": "A blazing ball of fire..."
    },
    ...
  ]
}

Usage:
    python decode_spells.py spells.json --out spells.txt
"""

import argparse
import json
from pathlib import Path
from typing import List, Dict


def load_spells(json_path: Path) -> List[Dict]:
    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    # Adjust the key if your JSON schema differs
    return data.get("spells", [])


def format_spell(spell: Dict) -> str:
    """Return a nicely formatted string for each spell."""
    return (
        f"Name: {spell.get('name', 'Unknown')}\n"
        f"Incantation: {spell.get('incantation', 'N/A')}\n"
        f"Level: {spell.get('level', 'N/A')}\n"
        f"Description: {spell.get('description', '')}\n"
        "-----"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Decode spells from JSON")
    parser.add_argument("json_file", type=Path, help="Path to spells JSON file")
    parser.add_argument(
        "--out",
        type=Path,
        default=None,
        help="Optional output file (default: print to stdout)",
    )
    args = parser.parse_args()

    spells = load_spells(args.json_file)
    formatted = "\n".join(format_spell(s) for s in spells)

    if args.out:
        args.out.write_text(formatted, encoding="utf-8")
        print(f"Wrote {len(spells)} spells to {args.out}")
    else:
        print(formatted)


if __name__ == "__main__":
    main()
