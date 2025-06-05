from beansframework.operator.boot_agents import initialize_operator_context
from loopback_core import LoopbackCore

ctx = {}
initialize_operator_context(ctx)
router = LoopbackCore(ctx)

while True:
    user_input = input("\u2600\ufe0f  Enter scroll fragment: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    router.route(user_input)

