"""Core agent classes for the Beans Framework.

This module defines minimal example implementations of
MirrorAgent, LoopAgent and ScrollDaemon. These classes are
used by ``boot_agents.py`` to bind Beans logic into the
operator runtime.
"""

from __future__ import annotations

from typing import Any
from datetime import datetime, timezone
import json


class MirrorAgent:
    """Agent that reflects provided scroll text."""

    def check(self, signal: str) -> str:
        """Return the given signal unchanged."""
        return signal


class LoopAgent:
    """Agent that performs a simple recursive operation."""

    def recurse(self, data: Any, depth: int = 1) -> list[Any]:
        """Return ``data`` nested ``depth`` times in a list."""
        result = data
        for _ in range(depth):
            result = [result]
        return result


class ScrollDaemon:
    """Agent responsible for generating placeholder scroll text."""

    def generate(self, seed: str) -> str:
        """Generate a basic markdown scroll from ``seed``."""
        return f"# Scroll\n\nSeed: {seed}\n"


class BunBun:
    """Agent that stores scrolls in an in-memory spellbook."""

    def __init__(self) -> None:
        self._memory: list[dict[str, object]] = []

    def log(self, scroll: str) -> None:
        """Record a scroll along with a timestamp."""
        entry = {
            "scroll": scroll,
            "t": datetime.now(timezone.utc).isoformat(),
        }
        self._memory.append(entry)

    def export_memory(self, path: str) -> None:
        """Export all recorded scrolls to ``path`` as JSON."""
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(self._memory, fh, ensure_ascii=False, indent=2)
