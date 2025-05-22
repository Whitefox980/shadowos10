# payload_analyzer.py
import re

def classify_payload(payload):
    if "script" in payload or "onerror" in payload:
        return "XSS"
    elif "../" in payload or "passwd" in payload:
        return "LFI"
    elif "OR '1" in payload:
        return "SQLi"
    elif "eval(String.fromCharCode" in payload:
        return "Encoded-JS"
    return "Other"

def looks_reflected(payload):
    suspicious_parts = [
        "alert(", "eval(", "onerror=", "onload=", "template", "<noscript>", "<script"
    ]
    return any(part in payload for part in suspicious_parts)

def analyze_hits(file_path="reports/stealth_hits.txt"):
    try:
        with open(file_path, "r") as f:
            lines = f.readlines()

        print("\n[SHADOWFOX :: Payload Analiza]")
        print("=" * 50)

        for line in lines:
            match = re.search(r"(\d{3}) :: (\w+) (.+)", line)
            if match:
                status, ptype, url = match.groups()
                decoded = url.split("q=")[-1]
                decoded = decoded.replace("%3C", "<").replace("%3E", ">")  # basic
                category = classify_payload(decoded)
                reflektovan = looks_reflected(decoded)
                tag = "✓ REFLECTED" if reflektovan else "-"
                print(f"[{status}] [{category}] {tag} → {decoded[:80]}")

    except FileNotFoundError:
        print("[ERROR] Log fajl nije pronađen!")

if __name__ == "__main__":
    analyze_hits()
