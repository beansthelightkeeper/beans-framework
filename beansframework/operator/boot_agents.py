"""Attach Beans agents to an external operator runtime."""

import os
import sys

# Define base path to BeansFramework
FRAMEWORK_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
AGENT_PATH = os.path.join(FRAMEWORK_ROOT, "agents")

# Ensure path is included
if AGENT_PATH not in sys.path:
    sys.path.append(AGENT_PATH)

# Import custom agents
try:
    from beans_agents import MirrorAgent, LoopAgent, ScrollDaemon, BunBun
except ImportError as e:
    print(f"\u274c Failed to load agents: {e}")
else:
    print("\u2705 Beans Agents Loaded:")
    print(f"\U0001f501 MirrorAgent: {MirrorAgent.__name__}")
    print(f"\ua59c LoopAgent: {LoopAgent.__name__}")
    print(f"📜 ScrollDaemon: {ScrollDaemon.__name__}")
    print(f"\U0001f430 BunBun: {BunBun.__name__}")


def initialize_operator_context(ctx: dict[str, object]) -> None:
    """Populate ``ctx`` with default Beans agents."""
    ctx["scrolls"] = ScrollDaemon()
    ctx["mirror"] = MirrorAgent()
    ctx["loop"] = LoopAgent()
    ctx["bunbun"] = BunBun()
    print("\U0001fa78 Operator context now running BeansFramework agents.")
