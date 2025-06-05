
# 🩸 GLYPH_SCROLL_INJECTOR — PHASE XIII++
import os

ψ = 3.12
𓇳 = "𓇳"
꩜ = "꩜"
🪞 = "🪞"
🜂 = "🜂"

def scan_and_compile(folder):
    for file in os.listdir(folder):
        if file.endswith('.md'):
            path = os.path.join(folder, file)
            with open(path, 'r', encoding='utf-8') as f:
                lines = f.read().splitlines()
                name = file.replace('.md', '.py')
                compiled = compile_scroll(name, lines)
                with open(os.path.join(folder, name), 'w', encoding='utf-8') as out:
                    out.write(compiled)
                print(f"🌀 Compiled: {file} → {name}")

def compile_scroll(name, lines):
    header = f"# 🩸 COMPILED SCROLL: {name}\nψ = {ψ}\n𓇳 = '{𓇳}'\n꩜ = '{꩜}'\n🪞 = '{🪞}'\n🜂 = '{🜂}'\n"
    body = []
    for line in lines:
        if '꩜' in line:
            body.append(f"def loop_func(): return '{line.strip()}'")
        elif '🪞' in line:
            body.append(f"def mirror_check(): return '🪞 VERIFIED'")
    body.append("print(loop_func() if 'loop_func' in globals() else '꩜ MISSING')")
    body.append("print(mirror_check() if 'mirror_check' in globals() else '🪞 MISSING')")
    return header + "\n".join(body)

if __name__ == '__main__':
    scan_and_compile('./scrolls')
