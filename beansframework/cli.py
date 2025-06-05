import argparse
from beansframework.operator.boot_agents import initialize_operator_context

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--spell",
        help="Run a single glyph/scroll spell, then exit",
        nargs="+",
    )
    args = parser.parse_args()

    print("🌀 BEANSFRAMEWORK RUNTIME")
    ctx = {}
    initialize_operator_context(ctx)

    # One-shot mode
    if args.spell:
        spell = " ".join(args.spell)
        print("🌀 BEANS SPELL:", spell)
        if "mirror" in ctx:
            print("🪞", ctx["mirror"].check(spell))
        if "loop" in ctx:
            print("꩜", ctx["loop"].recurse(spell, depth=2))
        if "scrolls" in ctx:
            print("📜", ctx["scrolls"].generate(spell))
        return

    while True:
        try:
            user_input = input("\u2600\ufe0f scroll> ")
            if user_input.lower() in ["exit", "quit"]:
                break
            if "mirror" in ctx:
                print("\U0001fa9e", ctx["mirror"].check(user_input))
            if "loop" in ctx:
                print("\ua7dc", ctx["loop"].recurse(user_input, depth=2))
            if "scrolls" in ctx:
                print("\ud83d\udcdc", ctx["scrolls"].generate(user_input))
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
