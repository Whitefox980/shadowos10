import base64
import json

def generate_payloads():
    with open("payload_matrix.json") as f:
        data = json.load(f)

    results = []
    for base in data["base_payloads"]:
        for enc in data["encodings"]:
            encoded = obfuscate(base, enc)
            for tmpl in data["templates"]:
                results.append(tmpl.replace("{payload}", encoded))
    return results

def obfuscate(payload, method):
    if method == "base64":
        return f"eval(atob('{base64.b64encode(payload.encode()).decode()}'))"
    elif method == "hex":
        return ''.join([f'\\x{ord(c):02x}' for c in payload])
    elif method == "unicode":
        return ''.join([f'\\u{ord(c):04x}' for c in payload])
    elif method == "reversed":
        return payload[::-1]
    else:
        return payload
