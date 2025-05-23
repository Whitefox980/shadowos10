import json
import requests

with open("uspesni_log.json") as f:
    logovi = json.load(f)

print("[✓] Validacija počinje...")
for i, unos in enumerate(logovi, 1):
    try:
        r = requests.get(unos["url"], timeout=10)
        print(f"[{i}] Testiram: {unos['url']}")
        print(f"→ Status: {r.status_code}, Dužina: {len(r.text)}")
    except Exception as e:
        print(f"[{i}] Greška za {unos['url']}: {e}")
