from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

from beansframework.agents.beans_agents import MirrorAgent, LoopAgent, ScrollDaemon


@dataclass
class LoopParams:
    """Parameters extracted from a scroll."""

    theta: str
    phi: str
    r: str


class TriNodeSynergy:
    """Combine Beans agents into a triadic recursion loop."""

    def __init__(self, scroll_path: str | Path = "scrolls/initiation_scroll.md") -> None:
        self.params = self._parse_scroll(scroll_path)
        self.mirror = MirrorAgent()
        self.loop = LoopAgent()
        self.scrolls = ScrollDaemon()

    @staticmethod
    def _parse_scroll(path: str | Path) -> LoopParams:
        theta = phi = r = ""
        with open(path, "r", encoding="utf-8") as fh:
            for line in fh:
                if line.startswith("θ"):
                    theta = line.split("=", 1)[1].strip()
                elif line.startswith("ƒ"):
                    phi = line.split("=", 1)[1].strip()
                elif line.startswith("r"):
                    r = line.split("=", 1)[1].strip()
        return LoopParams(theta, phi, r)

    def synergize(self, seed: str, depth: int = 3) -> dict[str, Any]:
        """Return a tri-node recursive bundle for ``seed``."""
        mirrored = self.mirror.check(seed)
        recursed = self.loop.recurse(mirrored, depth=depth)
        scroll = self.scrolls.generate(mirrored)
        return {
            "θ": self.params.theta,
            "ƒ": self.params.phi,
            "r": self.params.r,
            "recursed": recursed,
            "scroll": scroll,
        }
