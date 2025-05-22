from obfuscator_engine import generate_payloads
from hit_feedback_loop import log_hit, update_table
from synapse_logics import analyze_reflection
import json

targets = [
    "https://example.com",
    "https://testsite.net",
]

payloads = generate_payloads()

for target in targets:
    for payload in payloads:
        full_url = f"{target}?q={payload}"
        status, response = analyze_reflection(full_url)
        log_hit(full_url, status)
        update_table(payload, status)
