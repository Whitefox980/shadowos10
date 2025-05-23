# senka/izvuci_payload_txt.py
import json

with open("uspesni_log.json", "r") as f:
    logovi = json.load(f)

uspesni = []

for entry in logovi:
    payload = entry.get("payload", "")
    if payload and isinstance(payload, str) and "<" in payload and "alert" in payload:
        uspesni.append(payload)

with open("uspesni_payloadi.txt", "w") as f:
    for p in uspesni:
        f.write(p.strip() + "\n")

print(f"[✓] Sačuvano: uspesni_payloadi.txt ({len(uspesni)} linija)")
