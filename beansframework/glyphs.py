"""Glyph utilities for BeansFramework."""

import json
from pathlib import Path
from typing import List, Dict

# Path to glyph dataset included with repository
_GLYPH_PATH = Path(__file__).resolve().parent.parent / "glyphs.json"


def load_glyphs() -> List[Dict[str, str]]:
    """Load glyph definitions from ``glyphs.json``."""
    with open(_GLYPH_PATH, "r", encoding="utf-8") as fh:
        return json.load(fh)


_GLYPHS = load_glyphs()


def glyph(seed: int) -> str:
    """Return a glyph based on ``seed`` modulo the dataset length."""
    if not _GLYPHS:
        return ""
    index = seed % len(_GLYPHS)
    return _GLYPHS[index]["glyph"]
