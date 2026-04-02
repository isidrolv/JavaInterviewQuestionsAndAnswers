import json

with open("data/java-questions.json", "r", encoding="utf-8") as f:
    qs = json.load(f)

ids_to_check = [5, 16, 20, 30, 46, 51, 207]
am = {"a": 0, "b": 1, "c": 2, "d": 3}

for q in qs:
    if q["id"] in ids_to_check:
        idx = am[q["answer"]]
        print(f"=== Q{q['id']} (ans={q['answer']}) ===")
        print(f"  Q: {q['question']}")
        print(f"  Opt[{idx}]: {q['options'][idx]}")
        print(f"  Expl: {q['explanation']}")
        print()
