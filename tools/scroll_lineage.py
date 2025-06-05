# 🧬 SCROLL LINEAGE TRACKER
import os
import json

def lineage_trace(scroll_path):
    """Return lineage data for a single scroll."""
    with open(scroll_path, 'r', encoding='utf-8') as f:
        content = f.read()

    anchor = "\U000132f3" in content  # 𓇳
    loop = "\ua9dc" in content       # ꩜
    mirror = "\U0001fa9e" in content  # 🪞
    weight = 3.12 if loop and anchor else 0.0

    return {
        "name": os.path.basename(scroll_path),
        "origin": anchor,
        "loop": loop,
        "mirror": mirror,
        "ψ": weight
    }


def log_trace(path, out_file="lineage_log.json"):
    """Trace all scrolls in a directory and log results as JSON."""
    traces = []
    for scroll in os.listdir(path):
        if scroll.endswith(".md"):
            trace = lineage_trace(os.path.join(path, scroll))
            traces.append(trace)
    with open(out_file, "w", encoding='utf-8') as f:
        json.dump(traces, f, indent=2)

# 🩸 Paste scrolls into /scrolls/, then run this to trace them all
