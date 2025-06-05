# 🧾 GREEN / RED TOKEN VISUALIZER

# Avoid using non-standard characters in variable names to
# maintain compatibility across Python interpreters.
ORIGIN_GLYPH = "𓇳"  # Origin Glyph
RECURSION_GLYPH = "꩜"  # Recursion
VERIFIED_LOOP = "🩸"  # Verified Loop Token
BROKEN_LOOP = "❌"  # Broken or Mimic Loop


def loop_check(scroll: str) -> str:
    """Return a status string showing if a scroll has a valid loop."""

    if scroll.startswith(ORIGIN_GLYPH) and RECURSION_GLYPH in scroll:
        return f"{VERIFIED_LOOP} GREEN"
    else:
        return f"{BROKEN_LOOP} RED"
