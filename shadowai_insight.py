import json

with open("reports/validated_hits.json", "r") as f:
    hits = json.load(f)

print("[SHADOWAI :: ANALYSIS REPORT]")
print("=" * 50)

for hit in hits:
    url = hit.get("url", "")
    attack_type = hit.get("type", "Unknown")
    notes = []

    if "eval(String.fromCharCode" in url:
        notes.append("Obfuscated payload, possibly bypassed WAF via encoding.")
    if attack_type == "XSS" and "<script>" in url:
        notes.append("Reflected XSS detected using standard payload.")
    if attack_type == "SQLi" and "OR '1'='1" in url:
        notes.append("Classic SQL injection via GET parameter detected.")

    print(f"- {attack_type}: {url}")
    for note in notes:
        print(f"    [AI Insight] {note}")
    print()

