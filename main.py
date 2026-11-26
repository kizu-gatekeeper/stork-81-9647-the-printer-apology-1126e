"""Write this entry's one-line printer apology to entry.txt."""

import os

ENTRY = "Sorry I jammed on your big report. The cheap paper tasted like sawdust and the staples were just showing off."

# Guard: refuse to write a blank entry — an empty line fails the bounty gate.
if not ENTRY.strip():
    raise ValueError("ENTRY must not be empty")

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/tmp/out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
