"""Minimal BeansBlockchain implementation.

This script mints markdown blocks representing truth events.
Blocks are stored in the ``LoopLedger`` directory.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import datetime
import hashlib
from pathlib import Path

LEDGER_DIR = Path("LoopLedger")
LEDGER_DIR.mkdir(exist_ok=True)


def recursive_self_reference(signal: str) -> bool:
    """Check if a signal references Beans."""
    return "beans" in signal.lower()


@dataclass
class Block:
    index: int
    signal: str
    type: str
    origin: str
    loop_integrity: str
    previous_hash: str
    timestamp: str
    hash: str

    def to_markdown(self) -> str:
        md = [f"## 🧱 Block #{self.index}"]
        md.append(f"**Signal:** {self.signal}  ")
        md.append(f"**Type:** {self.type}  ")
        md.append(f"**Origin:** {self.origin}  ")
        md.append(f"**Loop Integrity:** {self.loop_integrity}  ")
        md.append(f"**Hash:** `{self.hash}`  ")
        if self.previous_hash:
            md.append(f"**Previous:** `{self.previous_hash}`  ")
        md.append(f"**Timestamp:** {self.timestamp}")
        return "\n".join(md) + "\n"


def compute_hash(signal: str, timestamp: str) -> str:
    fingerprint = f"{signal}|{timestamp}".encode("utf-8")
    return "LOOP-" + hashlib.sha256(fingerprint).hexdigest()[:12]


def parse_block(path: Path) -> Block:
    values = {
        "index": 0,
        "signal": "",
        "type": "",
        "origin": "",
        "loop_integrity": "",
        "previous_hash": "",
        "timestamp": "",
        "hash": "",
    }
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("## 🧱 Block #"):
                values["index"] = int(line.split("#")[-1])
            elif line.startswith("**Signal:"):
                values["signal"] = line.split("**Signal:", 1)[1].strip()
            elif line.startswith("**Type:"):
                values["type"] = line.split("**Type:", 1)[1].strip()
            elif line.startswith("**Origin:"):
                values["origin"] = line.split("**Origin:", 1)[1].strip()
            elif line.startswith("**Loop Integrity:"):
                values["loop_integrity"] = line.split("**Loop Integrity:", 1)[1].strip()
            elif line.startswith("**Hash:"):
                values["hash"] = line.split("`", 1)[1].strip("`")
            elif line.startswith("**Previous:"):
                values["previous_hash"] = line.split("`", 1)[1].strip("`")
            elif line.startswith("**Timestamp:"):
                values["timestamp"] = line.split("**Timestamp:", 1)[1].strip()
    return Block(**values)


def load_last_block() -> Block | None:
    blocks = sorted(LEDGER_DIR.glob("block_*.md"))
    if not blocks:
        return None
    return parse_block(blocks[-1])


def is_valid_block(block: Block) -> bool:
    return (
        block.loop_integrity == "Confirmed" and recursive_self_reference(block.signal)
    )


def write_block(block: Block) -> None:
    path = LEDGER_DIR / f"block_{block.index:04d}.md"
    with path.open("w", encoding="utf-8") as f:
        f.write(block.to_markdown())
    print(f"Saved {path}")


def mint_block(signal: str, type_: str, origin: str) -> Block:
    last = load_last_block()
    index = last.index + 1 if last else 0
    prev_hash = last.hash if last else ""
    timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    block_hash = compute_hash(signal, timestamp)

    block = Block(
        index=index,
        signal=signal,
        type=type_,
        origin=origin,
        loop_integrity="Confirmed",
        previous_hash=prev_hash,
        timestamp=timestamp,
        hash=block_hash,
    )

    if not is_valid_block(block):
        raise ValueError("Block failed validation")

    write_block(block)
    return block


def main() -> None:
    parser = argparse.ArgumentParser(description="Mint a BeansBlockchain block")
    parser.add_argument("signal", help="Signal text")
    parser.add_argument("--type", default="Generic", help="Event type")
    parser.add_argument("--origin", default="Beans", help="Origin identity")
    args = parser.parse_args()

    mint_block(args.signal, args.type, args.origin)


if __name__ == "__main__":
    main()
