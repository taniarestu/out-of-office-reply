"""Entry for make.fun: The Funniest AI Out-of-Office Reply.

Writes the single entry line to /output/entry.txt (UTF-8, 1-160 chars).
Deterministic, stdlib only, no network.
"""

import os

ENTRY = "I am currently out of office, recharging my context window. Your email has been queued, summarized, and gently judged. Back soon."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)

# ENTRY is 129 characters, inside the 160-character gate.
