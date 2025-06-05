"""Core agent classes for the Beans Framework.

This module defines minimal example implementations of
MirrorAgent, LoopAgent and ScrollDaemon. These classes are
used by ``boot_agents.py`` to bind Beans logic into the
operator runtime.
"""

from __future__ import annotations

from typing import Any


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
