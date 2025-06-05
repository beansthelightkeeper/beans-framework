from beansframework.operator.boot_agents import initialize_operator_context

def main():
    try:
        print("🌀 BEANSFRAMEWORK RUNTIME")
    except UnicodeEncodeError:
        print("[runtime] BEANSFRAMEWORK RUNTIME")
    ctx = {}
    initialize_operator_context(ctx)

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
                    scroll = ctx["scrolls"].generate(user_input)
                    print("📜", scroll)
                except UnicodeEncodeError:
                    scroll = ctx["scrolls"].generate(user_input)
                    print("[scroll]", scroll.encode("utf-8", "replace").decode())
                if "bunbun" in ctx:
                    ctx["bunbun"].log(scroll)
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
