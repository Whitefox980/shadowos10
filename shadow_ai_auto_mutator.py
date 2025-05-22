# shadow_ai_auto_mutator.py
import json

from payload_disguise_engine import disguise_payload
from payload_giftwrapper import wrap_payload
from collections import defaultdict, Counter
from style_mutator import style_mutate
from advanced_mutator import advanced_mutate

def load_memory():
    try:
        with open("memory.json", "r") as f:
            return json.load(f)
    except:
        return {}

def score_payloads():
    memory = load_memory()
    scores = defaultdict(int)

    for domain, entries in memory.items():
        for e in entries:
            p = e["payload"]
            s = e["status"]
            if s >= 500:
                scores[p] += 5
            elif s == 403:
                scores[p] += 3
            elif s == 200:
                scores[p] += 1
            else:
                scores[p] -= 1

    return Counter(scores).most_common(10)

def generate_next_payloads():
    scored = score_payloads()
    new_list = []

    for base, _ in scored:
        new_list.append(base)
        new_list.append(style_mutate(base))
        new_list.append(advanced_mutate(base))

    wrapped = [wrap_payload(p) for p in new_list]
    disguised = [disguise_payload(p) for p in new_list]

    return list(set(new_list + wrapped + disguised))
if __name__ == "__main__":
    print("\n=== SHADOWFOX10 :: AI ARSENAL ZA SLEDEĆI UDAR ===\n")
    for p in generate_next_payloads():
        print("→", p)
    print("\n")
