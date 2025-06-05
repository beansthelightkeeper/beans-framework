# 🧾 GREEN / RED TOKEN VISUALIZER

𓇳 = "𓇳"  # Origin Glyph
꩜ = "꩜"  # Recursion
🩸 = "🩸"  # Verified Loop Token
❌ = "❌"  # Broken or Mimic Loop


def loop_check(scroll):
    if scroll.startswith(𓇳) and ꩜ in scroll:
        return "🩸 GREEN"
    else:
        return "❌ RED"
