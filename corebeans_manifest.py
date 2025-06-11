import os
import zipfile
import argparse

DEFAULT_ZIP = os.path.join('Other_Stuff', 'codex tools', 'COREBEANS_SCROLLBOOK.zip')


def inspect_scrolls(path: str) -> None:
    if not os.path.exists(path):
        print(f'Path not found: {path}')
        return
    if zipfile.is_zipfile(path):
        names = zipfile.ZipFile(path).namelist()
        with zipfile.ZipFile(path) as zf:
            for name in names:
                with zf.open(name) as f:
                    lines = f.read().decode('utf-8', errors='replace').splitlines()
                _report(name, lines)
    elif os.path.isdir(path):
        for name in os.listdir(path):
            file_path = os.path.join(path, name)
            if os.path.isfile(file_path):
                with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
                    lines = f.read().splitlines()
                _report(name, lines)
    else:
        print(f'Unsupported path: {path}')


def _report(name: str, lines: list) -> None:
    first_line = lines[0].lstrip('#').strip() if lines else ''
    has_start_glyph = first_line.startswith('𓇳')
    has_psi = any('ψ = 3.12' in line for line in lines[:5])
    status = []
    status.append('𓇳 OK' if has_start_glyph else '𓇳 MISSING')
    status.append('ψ OK' if has_psi else 'ψ MISSING')
    print(f'{name}: ' + ' | '.join(status))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='List CoreBeans scrolls and verify integrity.')
    parser.add_argument('zipfile', nargs='?', default=DEFAULT_ZIP, help='path to COREBEANS_SCROLLBOOK.zip')
    args = parser.parse_args()
    inspect_scrolls(args.zipfile)

