import hashlib


def get_scroll_hash(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read().encode('utf-8')
    return hashlib.sha256(content).hexdigest()


def verify_scroll(path, known_hash):
    return get_scroll_hash(path) == known_hash

