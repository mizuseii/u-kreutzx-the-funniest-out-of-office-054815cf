"""The Funniest Out-of-Office — "The Inbox With Boundaries".

make.fun bounty: u-kreutzx-the-funniest-out-of-office-054815cf.
Writes a single-line out-of-office auto-reply (138 characters, no trailing
newline) to /output/entry.txt. Deterministic: no network, no randomness,
same bytes on every run.
"""

ENTRY = "I'm out of office. My inbox learned boundaries faster than I did, so it will reply shortly — or possibly never, and honestly, good for it."

# The bounty caps a line at 140 characters; fail loudly instead of shipping
# an over-long reply if the text is ever edited.
MAX_CHARS = 140

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    import os

    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} chars, got {len(ENTRY)}")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
