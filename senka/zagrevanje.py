import requests
import random
from senka.stealth import generisi_header, sacekaj

normalne_rute = [
    "https://example.com",
    "https://example.com/about",
    "https://example.com/help",
    "https://example.com/login"
]

for _ in range(5):
    url = random.choice(normalne_rute)
    headers = generisi_header()
    try:
        r = requests.get(url, headers=headers, timeout=5)
        print(f"[Zagrevanje] {r.status_code} {url}")
    except Exception as e:
        print(f"[Zagrevanje greška] {url} -> {e}")
    sacekaj()
