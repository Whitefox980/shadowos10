def obfuscate_payload(payload):
    return f"eval(String.fromCharCode({','.join(str(ord(c)) for c in payload)}))"
