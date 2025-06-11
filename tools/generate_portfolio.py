#!/usr/bin/env python3
"""Generate a markdown index of notable repository files."""

from __future__ import annotations

import os
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_FILE = REPO_ROOT / "PORTFOLIO.md"


def extract_title(filepath: Path) -> str:
    """Return the first markdown header in ``filepath`` or the filename."""
    try:
        with filepath.open("r", encoding="utf-8") as f:
            for line in f:
                if line.strip().startswith("#"):
                    return line.strip("#").strip()
    except Exception:
        pass
    return filepath.name


def generate_portfolio() -> None:
    sections: list[str] = []
    for root, _, files in os.walk(REPO_ROOT):
        for name in files:
            if name.endswith((".md", ".py", ".txt")) and name != OUTPUT_FILE.name:
                path = Path(root) / name
                rel_path = path.relative_to(REPO_ROOT)
                title = extract_title(path)
                url = f"https://github.com/beansthelightkeeper/beans-codex/blob/main/{rel_path}"
                sections.append(f"- [{title}]({url})")

    header = (
        "# \U0001f30c Beans Codex Portfolio\n\n"
        "This auto-generated index reflects the recursive structure and active "
        "contributions of Beans across the Codex repositories.\n\n"
    )
    OUTPUT_FILE.write_text(header + "\n".join(sorted(sections)), encoding="utf-8")
    print(f"\u2705 Portfolio written to {OUTPUT_FILE}")


if __name__ == "__main__":
    generate_portfolio()
