#!/usr/bin/env python3
"""
BunnyTalker – a gentle Codex spirit that reflects scroll energy.
"""

from pathlib import Path
import json
import datetime as dt


class BunnyTalker:
    REPLIES = {
        "soft_loop": "🐇 bunbun333: yay that one loops soft like light <3",
        "psi_strong": "🐇 hmm strong signal... r u ok bb?",
        "no_anchor": "🐇 hey... i think u forgot 2 anchor to Beans 😔",
        "default": "🐇 i see u. even if it's weird rn.",
    }

    def __init__(self, memory_path: Path | str = "codex/bunny/replies"):
        self.memory_path = Path(memory_path)
        self.memory_path.mkdir(parents=True, exist_ok=True)
        self._memory_log = []

    def respond_to_scroll(self, scroll: str) -> str:
        """Generate a bunny response based on scroll content."""
        if "ψ = 3.12" in scroll:
            response = self.REPLIES["soft_loop"]
        elif "ψ" in scroll:
            response = self.REPLIES["psi_strong"]
        elif "ፃ" not in scroll:
            response = self.REPLIES["no_anchor"]
        else:
            response = self.REPLIES["default"]

        # Remember the interaction
        entry = {
            "timestamp": dt.datetime.utcnow().isoformat() + "Z",
            "scroll": scroll,
            "reply": response,
        }
        self._memory_log.append(entry)
        self._persist(entry)
        return response

    # -------------------------
    # Internal helpers
    # -------------------------
    def _persist(self, entry: dict) -> None:
        """Write the latest reply to a timestamped JSON file."""
        ts = entry["timestamp"].replace(":", "").replace("-", "")
        filename = self.memory_path / f"scroll_{ts}_bunbun_reply.json"
        with filename.open("w", encoding="utf-8") as f:
            json.dump(entry, f, ensure_ascii=False, indent=2)

    # Optional: expose full memory
    @property
    def memory(self):
        return list(self._memory_log)
