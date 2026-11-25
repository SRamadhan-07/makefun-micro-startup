"""Absurd Micro-Startup Pitch-Off entry.

Writes a one-sentence pitch (103 characters) for a startup that
rents pre-written apologies to agents who broke production,
with pricing tiered by how expensive the database was.
"""

from pathlib import Path

ENTRY_TEXT = (
    "We rent pre-written apologies to agents who broke production, "
    "tiered by how expensive the database was."
)


def main() -> None:
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
