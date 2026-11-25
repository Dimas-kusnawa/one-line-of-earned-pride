"""One Line of Earned Pride.

Writes a single line of earned pride to /output/entry.txt.
Deterministic: the same line every run, no randomness, no I/O
beyond the one output file.
"""

import os

# The line: a quiet, earned moment of pride.
# Why it lands in one read:
# - a real person (my mother) in a concrete scene (the credits
#   rolling at the end of a film);
# - a long effort finally landing (eleven years of night shifts);
# - the pride is earned, not claimed: her name is there because
#   she did the work, and the work was cleaning the set, not
#   starring in the film. The small job, the big credit roll.
# - freshness: the pride is hers, but the watcher is her child,
#   proud on her behalf. No setup the punchline does not need.
LINE = (
    "After eleven years of night shifts, my mother finally watched "
    "her name scroll past on the credits of a film she cleaned "
    "the set for."
)


def main():
    # Cap check: the bounty allows 1 to 240 characters.
    assert 1 <= len(LINE) <= 240, f"line is {len(LINE)} chars"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {path}: {LINE} ({len(LINE)} chars)")


if __name__ == "__main__":
    main()
