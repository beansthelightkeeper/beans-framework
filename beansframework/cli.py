import sys
from beansframework.operator.boot_agents import initialize_operator_context

def main():
    print("🌀 BEANSFRAMEWORK RUNTIME")
    ctx = {}
    initialize_operator_context(ctx)

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
