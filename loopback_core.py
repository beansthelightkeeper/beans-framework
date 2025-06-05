from trace_to_beans import process_text_input


class LoopbackCore:
    def __init__(self, agents):
        self.agents = agents
        print("✅ LoopbackCore initialized with Beans agents.")

    def route(self, input_text):
        print("🧬 Scanning for signal return...")
        process_text_input(input_text)
        if "𓇳" in input_text:
            print("🩸 Origin detected. Passing to ScrollDaemon.")
            return self.agents['scrolls'].generate(seed=input_text)
        if "🪞" in input_text:
            print("🪞 Mirror glyph detected. Running MirrorAgent check.")
            return self.agents['mirror'].check(input_text)
        return self.agents['loop'].recurse(input_text)

