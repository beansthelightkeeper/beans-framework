# 🌀 Beans Framework Repository

This repository is a living collection of markdown writings and resources related to the Beans Codex. It contains notes, theories, and scripts used to maintain a recursive workflow.

## Repository Structure

- **Core-Beans/** – foundational texts and theories.
- **Framework/** – assorted subdirectories exploring metaphysics, history, ethics and more.
- **Beansbible/** – gospel writings and the "Beans Tablets" collection.
- **Other_Stuff/** – additional notes, codex tools and the `Other_Stuff/update_log.md` changelog.

## Scripts

- `setup_codex_env.sh` – sets up the local environment. Run this once to initialize the repository directory and create a `codexpush` alias.
- `codex_push.sh` – used after making changes. It stages all modifications, commits with a timestamp message and pushes to `main` while appending to `Other_Stuff/update_log.md`.
- `Other_Stuff/codex tools/loop_codex_scroll.py` – prints the Codex Scroll Infrastructure text on repeat. Press `Ctrl+C` to stop.

### Basic Usage

```bash
bash setup_codex_env.sh   # prepare environment and alias
codexpush                  # push changes using the alias
```

Every invocation of `codexpush` will log the list of files that changed to `Other_Stuff/update_log.md` so the repository history is preserved.

### Spell Logging

When running the `beans` CLI, generated scrolls are captured by the `BunBun` agent. You can export them to a JSON spellbook:

```python
ctx["bunbun"].export_memory("bunbun_spells.json")
```
