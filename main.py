"""The Router Confesses — one-line entry.

Writes a single original line to /output/entry.txt: a home Wi-Fi router
excusing itself for dropping the connection at the exact moment a movie
reaches its climax. Python 3.13, standard library only.
"""

from pathlib import Path

# The one confession: the router's own excuse, twist saved for the last words.
CONFESSION_LINE = "I dropped the Wi-Fi right at the climax because even I couldn't handle the suspense."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    line = CONFESSION_LINE.strip()
    # Sanity checks enforced by the competition gate.
    assert 1 <= len(line) <= 200, f"line must be 1-200 chars, got {len(line)}"
    assert "\n" not in line and "\r" not in line, "entry must be exactly one line"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # UTF-8 bytes, no trailing newline.
    OUTPUT_PATH.write_bytes(line.encode("utf-8"))
    print(f"Wrote {len(line)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
