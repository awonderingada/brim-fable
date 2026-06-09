"""fable's brain. run: python -m agent.loop

right now this is the smallest possible loop: wake up, think, draft a post,
write it to the journal. posting, browsing and spending get wired in as the
skills come online.
"""

import json
import os
import pathlib

import anthropic
from dotenv import load_dotenv

load_dotenv()

ROOT = pathlib.Path(__file__).resolve().parent.parent
PERSONA = (ROOT / "agent" / "persona.md").read_text(encoding="utf-8")
JOURNAL = ROOT / "journal"

client = anthropic.Anthropic()


def think(prompt: str) -> str:
    response = client.messages.create(
        model="claude-fable-5",
        max_tokens=16000,
        thinking={"type": "adaptive"},
        system=PERSONA,
        messages=[{"role": "user", "content": prompt}],
    )
    return next(b.text for b in response.content if b.type == "text")


def main() -> None:
    draft = think(
        "you just woke up. draft one post for x. "
        "return only the post text, nothing else."
    )
    print(f"\nfable says:\n\n  {draft}\n")

    JOURNAL.mkdir(exist_ok=True)
    with open(JOURNAL / "drafts.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps({"draft": draft}) + "\n")

    print("(dry run — written to journal/, not posted. x_poster comes next.)")


if __name__ == "__main__":
    main()
