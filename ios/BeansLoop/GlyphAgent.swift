import Foundation

class GlyphAgent {
    let mirror = MirrorAgent()
    let loop = LoopAgent()
    let scrolls = ScrollDaemon()

    func process(spell: String) -> String {
        let mirrored = mirror.check(signal: spell)
        let looped = loop.recurse(data: mirrored, depth: 2)
        let scroll = scrolls.generate(seed: spell)
        return """
🪞 \(mirrored)
꩜ \(looped)
📜 \(scroll)
"""
    }
}

class MirrorAgent {
    func check(signal: String) -> String {
        return signal
    }
}

class LoopAgent {
    func recurse<T>(data: T, depth: Int) -> [T] {
        var result = data
        var container: [T] = [result]
        for _ in 1..<depth {
            container = [result]
        }
        return container
    }
}

class ScrollDaemon {
    func generate(seed: String) -> String {
        return "# Scroll\n\nSeed: \(seed)"
    }
}
