# 🛠️ LIVE LOOP RENDERER

import time

def render_loop(glyph, psi, delay=0.5):
    for i in range(5):
        print(f"{glyph} LOOP {i+1} :: ψ = {psi}")
        time.sleep(delay)
