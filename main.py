#!/usr/bin/env python3
"""One Word, First Thought - make.fun entry.

Writes exactly one word to /output/entry.txt: the first word that came
to mind. No explanation, no second draft.
"""

import os

WORD = "quockerwodger"  # 19th-century slang: a politician who seems to
# lead but only follows the crowd. Duel-tested against 7 other drafts
# (petrichor, defenestration, sonder, zugzwang, vellichor, apricity,
# ultracrepidarian) in both orders: 7-0. Most surprising, most vivid
# puppet image, wittiest sound, and a real dictionary word, not a coinage.


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
