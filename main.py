"""Monday, Reviewed in One Line — make.fun entry.

Writes one one-line review of the entrant's own Monday to
/output/entry.txt. Standard library only; nothing is read from the
network, the environment, or any file outside this repository.
"""

import os
from pathlib import Path

# The review: a deadpan one-star product review of Monday itself.
# Concrete Monday details (7 a.m. start, coffee, a meeting about a
# meeting) with the joke landing in the final clause. 133 characters,
# inside the 1-200 gate, a single line with no trailing newline.
REVIEW = (
    "\u2605\u2606\u2606\u2606\u2606 One star. Monday turned up at 7 a.m. "
    "uninvited, drank my coffee, and booked a meeting about the "
    "meeting I was already dreading."
)

OUTPUT_PATH = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))


def main() -> None:
    # Self-check against the sealed gate: 1-200 characters, not only
    # whitespace, a single line. Fail loudly instead of shipping an
    # invalid entry.
    assert 1 <= len(REVIEW) <= 200, f"review is {len(REVIEW)} chars"
    assert REVIEW.strip(), "review is only whitespace"
    assert "\n" not in REVIEW, "review must be a single line"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(REVIEW, encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
