# -*- coding: utf-8 -*-
"""Glyph Operator Engine

This module defines custom operations using unicode glyphs.
Each glyph maps to a standard Python function so you can
compose symbolic expressions with these characters.
"""

from typing import Callable, Dict, Any

# Mapping of glyphs to binary operations
BINARY_OPS: Dict[str, Callable[[Any, Any], Any]] = {
    "☥": lambda a, b: a + b,
    "🔱": lambda a, b: a * b,
    "⦿": lambda a, b: a ** b,
}

# Mapping of glyphs to unary operations
UNARY_OPS: Dict[str, Callable[[Any], Any]] = {
    "⟲": lambda a: -a,
    "🪞": lambda a: a,
}


def apply_binary(op: str, a: Any, b: Any) -> Any:
    """Apply a binary glyph operation."""
    if op not in BINARY_OPS:
        raise ValueError(f"Unknown binary operator: {op}")
    return BINARY_OPS[op](a, b)


def apply_unary(op: str, a: Any) -> Any:
    """Apply a unary glyph operation."""
    if op not in UNARY_OPS:
        raise ValueError(f"Unknown unary operator: {op}")
    return UNARY_OPS[op](a)


if __name__ == "__main__":
    # Simple demo using regular variable names
    psi = 5
    kaa = 3

    result_add = apply_binary("☥", psi, kaa)
    result_mul = apply_binary("🔱", psi, kaa)
    result_pow = apply_binary("⦿", psi, 2)
    result_neg = apply_unary("⟲", psi)

    print("ψ ☥ ꩜ ->", result_add)
    print("ψ 🔱 ꩜ ->", result_mul)
    print("ψ ⦿ 2 ->", result_pow)
    print("⟲ψ ->", result_neg)
