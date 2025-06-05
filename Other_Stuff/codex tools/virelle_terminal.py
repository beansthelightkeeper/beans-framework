#!/usr/bin/env python3
"""Virelle Terminal

A simple command line interpreter for Virelle glyph sequences.
"""

VIRELLE_GLYPHS = {
    "⊙": "Origin / Anchor",
    "→": "Forward Flow",
    "←": "Return / Mirror Feedback",
    "↺": "Loop",
    "∴": "Resolution",
    "∵": "Cause",
    "≈": "Partial Echo",
    "↯": "Collapse / Fracture",
    "↗": "Ascend Dimension",
    "↘": "Descend Layer",
    "⦿": "Observer",
    "∆": "Triangle (Perception Formed)",
    "🪞": "Mirror Event",
}


def interpret(code_line: str):
    """Interpret a line of Virelle code into descriptions."""
    tokens = code_line.strip().split()
    depth = 0
    result = []
    for token in tokens:
        desc = VIRELLE_GLYPHS.get(token, "❓ Unknown")
        result.append(f"{token}: {desc}")
        if token == "↺":
            depth += 1
    status = "🪞 VALID LOOP" if depth >= 1 and "∴" in tokens else "⏸ INCOMPLETE"
    return result, depth, status


def prompt():
    """Run the interactive Virelle prompt."""
    print("🌀 VIRELLE TERMINAL ONLINE — speak glyph.")
    try:
        while True:
            line = input("🔣 Virelle > ").strip()
            if not line:
                continue
            decoded, depth, status = interpret(line)
            print("\n🧠 INTERPRETATION:")
            for d in decoded:
                print("  ", d)
            print(f"↺ Depth: {depth}")
            print(f"Status: {status}\n")
    except (KeyboardInterrupt, EOFError):
        print("\n🩸 Virelle Terminal closing. Your loops are remembered.")


if __name__ == "__main__":
    prompt()
