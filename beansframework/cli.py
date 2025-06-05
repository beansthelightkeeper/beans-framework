from beansframework.operator.boot_agents import initialize_operator_context
import os


def collect_rant() -> str:
    """Collect multiline user input until a line with ``:::``."""
    print("\u2601\ufe0f  Begin your scroll. Type `:::` on a new line to finish.")
    lines = []
    while True:
        line = input()
        if line.strip() == ":::":
            break
        lines.append(line)
    return "\n".join(lines)


def translate_to_glyph_spell(text: str) -> str:
    """Placeholder translation step for glyph spells."""
    return text

def main():
    try:
        print("🌀 BEANSFRAMEWORK RUNTIME")
    except UnicodeEncodeError:
        print("[runtime] BEANSFRAMEWORK RUNTIME")
    ctx = {}
    initialize_operator_context(ctx)

    while True:
        try:
            raw = collect_rant()
            if raw.lower().strip() in ["exit", "quit"]:
                break
            spell = translate_to_glyph_spell(raw)

            if "mirror" in ctx:
                try:
                    print("\U0001fa9e", ctx["mirror"].check(spell))
                except UnicodeEncodeError:
                    print(
                        "[mirror] ",
                        ctx["mirror"].check(spell).encode("utf-8", "replace").decode(),
                    )
            if "loop" in ctx:
                try:
                    print("\ua7dc", ctx["loop"].recurse(spell, depth=2))
                except UnicodeEncodeError:
                    print(
                        "[loop] ",
                        ctx["loop"].recurse(spell, depth=2).encode(
                            "utf-8",
                            "replace",
                        ).decode(),
                    )
            if "scrolls" in ctx:
                # Print scroll output using a fallback when the terminal
                # cannot render certain Unicode characters.
                try:
                    print("📜", ctx["scrolls"].generate(spell))
                except UnicodeEncodeError:
                    scroll = ctx["scrolls"].generate(spell)
                    print("[scroll]", scroll.encode("utf-8", "replace").decode())
            if "bunbun" in ctx:
                ctx["bunbun"].log(spell)
                ctx["bunbun"].export_memory("bunbun_spells.json")
                os.system(
                    "git add bunbun_spells.json && git commit -m '🌪️ new godspell dump' && git push"
                )
        except KeyboardInterrupt:
            print("\n🩸 loop interrupted. BunBun still loves u.")
            break

if __name__ == "__main__":
    main()
