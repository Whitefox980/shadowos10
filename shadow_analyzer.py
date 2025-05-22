# shadow_analyzer.py

VALID_SIGNS = [
    "alert", "<script", "onerror", "eval", "String.fromCharCode",
    "' OR '1'='1", "etc/passwd", "../../../", "<img", "<noscript>",
    "<template>", "<form", "<textarea"
]

def is_valid(line):
    return any(sig in line for sig in VALID_SIGNS)

input_path = "reports/stealth_hits.txt"
txt_out = "reports/validated_hits.txt"
json_out = "reports/validated_hits.json"

valid_hits = []

with open(input_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

for line in lines:
    if is_valid(line):
        valid_hits.append(line.strip())

# Save to .txt
with open(txt_out, "w", encoding="utf-8") as f:
    f.write("\n".join(valid_hits))

# Save to .json
import json
json_data = [{"url": line.split("] ")[-1]} for line in valid_hits]
with open(json_out, "w", encoding="utf-8") as f:
    json.dump(json_data, f, indent=2)

print(f"[✓] Validirano {len(valid_hits)} pogodaka. Sačuvano u {txt_out} i {json_out}")
