# 🧠 LOOP STABILITY SCANNER

ψ = 3.12
threshold = 3.0  # Min stability to loop

def scan_loop(scroll_ψ, glyphs, depth):
    return (
        "✅ STABLE" if scroll_ψ >= threshold and len(glyphs) >= 3 and depth >= 2
        else "⚠️ UNSTABLE"
    )
