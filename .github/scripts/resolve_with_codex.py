#!/usr/bin/env python3
"""
resolve_with_codex.py

1. Detects files with merge conflicts (<<<<<<<, =======, >>>>>>>).
2. Sends each conflicted chunk to OpenAI Codex / GPT, asking for a clean merge.
3. Replaces the conflicted content with the model's response.
4. Commits the changes.

Requires env var OPENAI_API_KEY.
"""

import os
import openai
import subprocess
from pathlib import Path
import re
import textwrap

openai.api_key = os.getenv("OPENAI_API_KEY")

# Regex to find Git conflict markers
CONFLICT_RE = re.compile(
    r"<<<<<<<.*?=======.*?>>>>>>>", re.DOTALL
)

def run(cmd):
    """Run shell command and return output (str)."""
    return subprocess.check_output(cmd, shell=True, text=True).strip()

def get_conflicted_files():
    """Return list of files with conflict markers."""
    files = run("git diff --name-only --diff-filter=U").splitlines()
    return [Path(f) for f in files if f]

def resolve_chunk(chunk: str) -> str:
    """Ask OpenAI to resolve a single conflict chunk."""
    prompt = textwrap.dedent(f"""
        You are an expert Python developer.
        Merge the following conflicting code sections into a single correct version.
        Keep the result minimal and functional.

        <<BEGIN>>
        {chunk}
        <<END>>
    """)
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",  # or gpt-4o, gpt-4-turbo, etc.
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0,
    )
    return response.choices[0].message.content.strip() + "\n"

def fix_file(path: Path):
    text = path.read_text()
    new_text = ""
    last_end = 0

    for m in CONFLICT_RE.finditer(text):
        # Append text before conflict
        new_text += text[last_end : m.start()]
        # Resolve conflict
        resolved = resolve_chunk(m.group(0))
        new_text += resolved
        last_end = m.end()

    # Append remaining text
    new_text += text[last_end:]
    path.write_text(new_text)
    print(f"Resolved conflicts in {path}")

def main():
    conflicted = get_conflicted_files()
    if not conflicted:
        print("No conflicts detected.")
        return

    for f in conflicted:
        fix_file(f)

    # Configure git user
    run('git config --global user.email "action@github.com"')
    run('git config --global user.name "GitHub Action Codex"')

    # Commit & push
    run('git add .')
    run('git commit -m "chore: auto-resolve merge conflicts with Codex"')
    run('git push')

if __name__ == "__main__":
    main()
