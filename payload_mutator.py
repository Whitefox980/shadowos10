# payload_mutator.py
from shadow_ai_auto_mutator import generate_next_payloads
def generate_payloads():
    return generate_next_payloads()
import hashlib

def hash_payload(payload):
    return hashlib.md5(payload.encode()).hexdigest()[:8]

payload = "<script>alert(1)</script>"
payload_id = hash_payload(payload)
url = f"https://target.com?q={payload}#ID-{payload_id}"
