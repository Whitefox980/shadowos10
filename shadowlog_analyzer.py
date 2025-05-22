# shadowlog_analyzer.py
import json
from collections import Counter
from payload_classifier import classify
from colorama import Fore

def load_memory():
    try:
        with open("memory.json", "r") as f:
            return json.load(f)
    except:
        return {}

def analyze():
    data = load_memory()
    payloads = []
    statuses = []
    types = []

    for domain, entries in data.items():
        for e in entries:
            payloads.append(e["payload"])
            statuses.append(str(e["status"]))
            types.append(classify(e["payload"]))

    print(Fore.CYAN + "\n==== SHADOWFOX10 :: STATISTIČKA ANALIZA ====\n")

    print(Fore.YELLOW + "[Top 5 Payload-a]")
    for text, count in Counter(payloads).most_common(5):
        print(Fore.WHITE + f"{count}x → {text}")

    print(Fore.YELLOW + "\n[Top HTTP Status Kodovi]")
    for status, count in Counter(statuses).most_common():
        print(Fore.WHITE + f"{count}x → Status {status}")

    print(Fore.YELLOW + "\n[Top Tipovi Ranjiivosti]")
    for rtype, count in Counter(types).most_common():
        print(Fore.WHITE + f"{count}x → {rtype}")

    print(Fore.CYAN + "\n===========================================\n")

if __name__ == "__main__":
    analyze()
