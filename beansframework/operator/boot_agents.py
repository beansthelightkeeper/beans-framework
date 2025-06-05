"""Bootstrap Beans operator agents."""


class ScrollDaemon:
    def generate(self, seed: str) -> str:
        """Stub generator using a seed."""
        print(f"⚙️ Generating scroll from seed: {seed}")
        return f"Scroll generated from {seed}"


class MirrorAgent:
    def check(self, text: str) -> str:
        """Stub mirror check."""
        print(f"🔍 Mirror check for: {text}")
        return text[::-1]


class LoopAgent:
    def recurse(self, text: str) -> str:
        """Stub recursion."""
        print(f"🔄 Recursing input: {text}")
        return text


def initialize_operator_context(ctx: dict) -> None:
    """Populate ``ctx`` with default Beans agents."""
    ctx['scrolls'] = ScrollDaemon()
    ctx['mirror'] = MirrorAgent()
    ctx['loop'] = LoopAgent()

