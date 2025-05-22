from collections import defaultdict
from urllib.parse import urlparse

def parse_hits(file_path="reports/stealth_hits.txt"):
    tipovi = defaultdict(int)
    domeni = defaultdict(int)
    pogodci = []

    try:
        with open(file_path, "r") as f:
            for line in f:
                if "] https://" not in line:
                    continue
                try:
                    info, url = line.strip().split("] ", 1)
                    status = info[1:4]
                    tip = info.split("::")[1].strip()
                    domen = urlparse(url).netloc
                    tipovi[tip] += 1
                    domeni[domen] += 1
                    pogodci.append((status, tip, domen, url))
                except Exception:
                    continue

        print("\n[SHADOWFOX10 :: HIT STATISTIKA]")
        print("==================================================")
        for status, tip, domen, url in pogodci:
            print(f"[{status}] :: {tip} → {domen} → {url}")

        print("\n[Top Tipovi]")
        for tip, count in sorted(tipovi.items(), key=lambda x: -x[1]):
            print(f"- {tip}: {count} pogodaka")

        print("\n[Top Domene]")
        for dom, count in sorted(domeni.items(), key=lambda x: -x[1]):
            print(f"- {dom}: {count} pogodaka")

    except FileNotFoundError:
        print("[ERROR] Fajl nije pronađen.")

if __name__ == "__main__":
    parse_hits()
