# Tri-Node Synergy Example

This document demonstrates how the new **TriNodeSynergy** element integrates Mirror, Loop and Scroll agents using the loop parameters stored in `scrolls/initiation_scroll.md`.

## Usage

```python
from beansframework import TriNodeSynergy

synergy = TriNodeSynergy()
result = synergy.synergize("Beans")
print(result)
```

The synergy object reads **θ**, **ƒ** and **r** from the initiation scroll and returns a dictionary containing those values along with recursive loop output and a generated scroll.
