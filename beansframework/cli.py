from beansframework.operator.boot_agents import initialize_operator_context
import json
import os


class BunBunLogger:
    """Simple logger that appends spells to ``bunbun_spells.json``."""

    def __init__(self, path: str = "bunbun_spells.json") -> None:
        self.path = path
        if not os.path.exists(self.path):
            with open(self.path, "w", encoding="utf-8") as f:
                json.dump([], f)

    def log(self, spell: str) -> None:
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            data = []
        data.append(spell)
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)


def push_to_loopcloud() -> None:
    os.system(
        "git add bunbun_spells.json && git commit -m '🌀 new scrolls from Beans CLI' && git push"
    )

def main():
    try:
        print("🌀 BEANSFRAMEWORK RUNTIME")
    except UnicodeEncodeError:
        print("[runtime] BEANSFRAMEWORK RUNTIME")
    ctx = {}
    initialize_operator_context(ctx)
    ctx["bunbun"] = BunBunLogger()

    while True:
        try:
            user_input = input("\u2600\ufe0f scroll> ")
            if user_input.lower() in ["exit", "quit"]:
                break
            if "mirror" in ctx:
                try:
                    print("\U0001fa9e", ctx["mirror"].check(user_input))
                except UnicodeEncodeError:
                    print("[mirror] ", ctx["mirror"].check(user_input).encode("utf-8", "replace").decode())
            if "loop" in ctx:
                try:
                    print("\ua7dc", ctx["loop"].recurse(user_input, depth=2))
                except UnicodeEncodeError:
                    print("[loop] ", ctx["loop"].recurse(user_input, depth=2).encode("utf-8", "replace").decode())
            if "scrolls" in ctx:
                # Print scroll output using a fallback when the terminal
                # cannot render certain Unicode characters.
                try:
                    scroll_output = ctx["scrolls"].generate(user_input)
                    print("📜", scroll_output)
                    print("🌈 VISUAL MODE:")
                    print("🟥🟧🟨🟩🟦🟪")
                    print(f"🌈  {user_input}")
                    print("🟥🟧🟨🟩🟦🟪")
                except UnicodeEncodeError:
                    scroll = ctx["scrolls"].generate(user_input)
                    print("[scroll]", scroll.encode("utf-8", "replace").decode())
            if "bunbun" in ctx:
                ctx["bunbun"].log(user_input)
                push_to_loopcloud()
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
