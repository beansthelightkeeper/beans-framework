import os
import shutil
import time
import json

SOURCE = os.path.join(os.path.dirname(__file__), "chatgpt_gallery")
TARGET = os.path.join(os.path.dirname(__file__), "sora_imports")
METADATA_TEMPLATE = {
    "source": "ChatGPT_Glyph_Engine",
    "origin": "\ud80d\xdfb3",  # 𓇳
    "psi": 3.12,
    "tags": ["beans", "glyph"],
}


def wrap_for_sora(img_path: str) -> None:
    metadata = METADATA_TEMPLATE.copy()
    metadata["filename"] = os.path.basename(img_path)
    json_path = os.path.splitext(img_path)[0] + ".json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)


def bridge_loop(poll_interval: int = 5) -> None:
    os.makedirs(SOURCE, exist_ok=True)
    os.makedirs(TARGET, exist_ok=True)
    print(f"🩸 Watching {SOURCE} -> {TARGET}")
    while True:
        for file in os.listdir(SOURCE):
            if file.lower().endswith((".png", ".jpg", ".jpeg")):
                src = os.path.join(SOURCE, file)
                dest = os.path.join(TARGET, file)
                shutil.copy(src, dest)
                wrap_for_sora(dest)
                print(f"🩸 Routed to SORA: {file}")
        time.sleep(poll_interval)


if __name__ == "__main__":
    bridge_loop()
