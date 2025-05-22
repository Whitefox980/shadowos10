# shadow_strategy_engine.py
import json
from collections import defaultdict, Counter

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
            payload = e["payload"]
            status = e["status"]

            # Score logika:
            if status >= 500:
                scores[payload] += 5     # server error → velika šansa za propust
            elif status == 403:
                scores[payload] += 3     # WAF blokada → vredan payload
            elif status == 200:
                scores[payload] += 1     # prošao tiho → korisno za stealth
            else:
                scores[payload] -= 1     # nepoznato

    return Counter(scores).most_common(5)

def suggest_next_payloads():
    top = score_payloads()
    print("\n=== SHADOWFOX10 :: AI PREDLOŽENI NAPADI ===\n")
    for rank, (payload, score) in enumerate(top, 1):
        print(f"[{rank}] ({score} pt) → {payload}")
    print("\n")

if __name__ == "__main__":
    suggest_next_payloads()
