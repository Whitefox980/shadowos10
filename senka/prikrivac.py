import requests
import random
import time
from senka.stealth import generisi_header

# Oponašamo korisnika koji klikće i gleda strane
stranice = [
    "https://example.com/news",
    "https://example.com/contact",
    "https://example.com/products",
    "https://example.com/blog"
]

for i in range(4):
    headers = generisi_header()
    url = random.choice(stranice)
    try:
        r = requests.get(url, headers=headers, timeout=5)
        print(f"[Prikrivac] {r.status_code} {url}")
    except Exception as e:
        print(f"[Greška korisnika] {e}")
    time.sleep(random.uniform(3, 7))
