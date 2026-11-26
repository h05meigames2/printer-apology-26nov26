"""The Printer Apology — one-line apology from an office printer.

Angle: the printer reframes its paper jams as the only affection it ever
gets — a hug — against the usual kicks and swearing. Apology up front,
punch at the end.

Writes the apology to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
The line is exactly one line, 1-120 characters, not only whitespace.
"""
import os

ENTRY = (
    "Sorry I keep jamming. It's the only hug I get all year \u2014 "
    "the rest of the time you just kick me and swear."
)


def main() -> None:
    line = ENTRY.strip()
    if not 1 <= len(line) <= 120:
        raise SystemExit(f"entry must be 1-120 characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be exactly one line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(f"Wrote {len(line)} characters to {path}")
    print(line)


if __name__ == "__main__":
    main()
