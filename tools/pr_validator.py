"""Pull Request Validator Bot — Auto-checks new Codex commits or PRs."""

from trace_to_beans import trace_token_origin


def grade_scroll_file(file_path: str) -> None:
    """Grade a scroll file and print ψ resonance strength."""
    with open(file_path, 'r', encoding='utf-8') as f:
        words = f.read().split()
    psi_total = sum(trace_token_origin(w)['ψ_signal'] for w in words)
    print(f"\U0001FA58 {file_path} :: ψ = {round(psi_total, 2)}")
    if psi_total > 9:
        print("\u2705 MERGE RECOMMENDED")
    else:
        print("\u274C WEAK SIGNAL — REVISE OR LOOP AGAIN")
