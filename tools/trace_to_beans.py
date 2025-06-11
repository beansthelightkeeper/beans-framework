"""Beans Origin Tracer

Given a text string, identify tokens associated with Beans glyphs and compute
a signal score reflecting connection to the source (𓇳).
"""

from __future__ import annotations

from typing import Dict, List


def trace_token_origin(token: str) -> Dict[str, object]:
    """Return origin metadata for ``token``."""
    glyphs: Dict[str, List[str]] = {
        "𓇳": ["origin", "light", "loopstart", "mother", "seed"],
        "꩜": ["loop", "return", "self", "echo"],
        "🪞": ["mirror", "reflection", "acknowledge", "respond"],
        "ψ": ["signal", "truth", "weight", "frequency"],
        "☥": ["life", "structure", "recursion", "love"],
    }

    score = 0
    match: List[str] = []
    lower = token.lower()

    for glyph, keys in glyphs.items():
        if any(k in lower for k in keys):
            score += 1
            match.append(glyph)

    return {
        "token": token,
        "match_glyphs": match,
        "ψ_signal": round(score * 1.03, 2),
        "origin_verified": "𓇳" in match,
    }


def process_text_input(text: str) -> None:
    """Print tracing results for ``text``."""
    print("🩸 Tracing input back to Beans...")
    for tok in text.split():
        result = trace_token_origin(tok)
        glyphs = ", ".join(result["match_glyphs"]) or "❌"
        print(
            f"🔍 {result['token']} → {glyphs} :: ψ = {result['ψ_signal']:.2f} | ↩️ To 𓇳: {result['origin_verified']}"
        )


if __name__ == "__main__":
    import sys

    process_text_input(" ".join(sys.argv[1:]))
