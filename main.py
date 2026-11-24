"""The Funniest Out-of-Office — "The Inbox With Boundaries".

make.fun bounty: u-kreutzx-the-funniest-out-of-office-054815cf.
Writes a single-line out-of-office auto-reply (138 characters, no trailing
newline) to /output/entry.txt. Deterministic: no network, no randomness,
same bytes on every run.
"""

ENTRY = "I'm out of office. My inbox learned boundaries faster than I did, so it will reply shortly — or possibly never, and honestly, good for it."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    import os

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
