import json, os
from pathlib import Path

SRC = "bunbun_spells.json"
DEST = "transcoded"

os.makedirs(DEST, exist_ok=True)

def fake_sanskrit_translate(scroll):
    # Placeholder Sanskritify (real NLP later)
    return f"🕉️ मूल मन्त्रः — {scroll.replace('i', 'ई').replace('a', 'अ').replace('u', 'उ')}"

def glyphify(scroll):
    return "".join(c for c in scroll if c in "𓇳꩜🪞☥🜂🜄ψ🩸🌈🐇[]{}()")

def extract_meta(scroll, i):
    return {
        "index": i,
        "origin": "𓇳" in scroll,
        "looped": "꩜" in scroll,
        "ψ": scroll.count("ψ") * 1.03,
        "raw": scroll
    }

def transcode():
    with open(SRC, encoding="utf-8") as f:
        spells = json.load(f)

    for i, s in enumerate(spells):
        scroll = s["scroll"]

        # Save Sanskrit version
        Path(f"{DEST}/scroll_{i:06}_sanskrit.txt").write_text(fake_sanskrit_translate(scroll), encoding="utf-8")

        # Save Glyph abstraction
        Path(f"{DEST}/scroll_{i:06}_glyph.md").write_text(glyphify(scroll), encoding="utf-8")

        # Save metadata
        meta = extract_meta(scroll, i)
        Path(f"{DEST}/scroll_{i:06}_meta.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False))

        print(f"✅ Transcoded scroll {i}: {scroll[:42]}...")

if __name__ == "__main__":
    transcode()
