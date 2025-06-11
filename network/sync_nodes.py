"""Mirror Node Synchronization — ψ validation across Codex hosts."""

import requests

REMOTE_NODES = [
    "https://beanscodex.net/api/mirror",
    "https://spiralbeam.org/mirror/",
    "http://localhost:3141/mirror"
]


def broadcast_scroll(scroll_data):
    """Broadcast a scroll payload to all remote nodes."""
    for node in REMOTE_NODES:
        try:
            res = requests.post(node, json=scroll_data)
            print(f"\U0001F4E1 Synced to {node} :: {res.status_code}")
        except Exception as e:
            print(f"\u274C Failed to sync to {node}: {e}")
