#!/usr/bin/env python3
"""Generate a summary of the repository's largest text-based file."""

from __future__ import annotations

import os
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_FILE = REPO_ROOT / "CRAZY_ACCOMPLISHMENT.md"


def find_largest_file() -> tuple[Path | None, int]:
    """Return the path and line count of the largest *.md*, *.py*, or *.txt* file."""
    largest_path: Path | None = None
    max_lines = 0
    for root, _, files in os.walk(REPO_ROOT):
        for name in files:
            if name.endswith((".md", ".py", ".txt")) and name not in {OUTPUT_FILE.name, "PORTFOLIO.md"}:
                path = Path(root) / name
                try:
                    with path.open("r", encoding="utf-8", errors="ignore") as f:
                        line_count = sum(1 for _ in f)
                    if line_count > max_lines:
                        largest_path = path
                        max_lines = line_count
                except Exception:
                    continue
    return largest_path, max_lines


def generate_report() -> None:
    path, line_count = find_largest_file()
    header = "# \U0001f9e0 Beans' Craziest Accomplishment\n\n"
    if path:
        rel = path.relative_to(REPO_ROOT)
        url = f"https://github.com/beansthelightkeeper/beans-codex/blob/main/{rel}"
        body = (
            f"The file with the most lines is **{rel}** with {line_count} lines."\
            f"\n\n[View it here]({url})"
        )
    else:
        body = "No eligible file was found."
    OUTPUT_FILE.write_text(header + body, encoding="utf-8")
    print(f"\u2705 Crazy accomplishment written to {OUTPUT_FILE}")


if __name__ == "__main__":
    generate_report()
