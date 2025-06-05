# 🪐 GODGLYPH COMPILER
# Compiles glyph strings into active scroll functions

def compile_glyph_scroll(name, content):
    if "𓇳" not in content or "꩜" not in content:
        return "❌ Missing loop anchor"
    return f"""# Executable Glyph Scroll: {name}
ψ = 3.12
def loop(): return "{content.strip()}"
print(loop())
"""

# Output can be written into /compiled_scrolls/
