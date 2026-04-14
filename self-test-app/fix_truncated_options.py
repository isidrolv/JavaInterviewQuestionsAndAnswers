#!/usr/bin/env python3
"""Fix truncated correct-answer options in java-questions.json.

For each question whose correct-answer option ends mid-sentence (no terminal
punctuation), replace it with the explanation text trimmed to the last
complete sentence.
"""
import json
import os

INPUT = os.path.join(os.path.dirname(__file__), 'data', 'java-questions.json')
ANSWER_MAP = {"a": 0, "b": 1, "c": 2, "d": 3}


def ends_cleanly(text: str) -> bool:
    """Return True if text ends with sentence-terminal punctuation."""
    t = text.strip()
    return bool(t) and t[-1] in ".!?:"


def trim_to_sentence(text: str) -> str:
    """Return text trimmed at the last sentence-ending character (. ! ?)."""
    t = text.strip()
    if not t:
        return t
    if t[-1] in ".!?":
        return t
    for i in range(len(t) - 1, 0, -1):
        if t[i] in ".!?":
            return t[: i + 1]
    return t


def main():
    with open(INPUT, "r", encoding="utf-8") as f:
        questions = json.load(f)

    updated = 0
    still_bad = []

    for q in questions:
        idx = ANSWER_MAP.get(q.get("answer"))
        if idx is None or idx >= len(q.get("options", [])):
            continue

        opt = q["options"][idx]
        expl = q.get("explanation", "")

        if not ends_cleanly(opt) and expl:
            new_opt = trim_to_sentence(expl)
            if new_opt != opt:
                q["options"][idx] = new_opt
                updated += 1
            if not ends_cleanly(new_opt):
                still_bad.append(q["id"])

    with open(INPUT, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"Total updated: {updated}")
    if still_bad:
        print(f"Still problematic IDs: {still_bad}")


if __name__ == "__main__":
    main()
