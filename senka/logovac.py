import json
from datetime import datetime

def loguj(url, status, payload, fajl='uspesni_log.json'):
    try:
        with open(fajl, 'r') as f:
            try:
                svi = json.load(f)
            except json.JSONDecodeError:
                print("[!] Nevalidan JSON, kreiram novi.")
                svi = []
    except FileNotFoundError:
        svi = []

    novi_unos = {
        "vreme": datetime.utcnow().isoformat(),
        "url": url,
        "status": status,
        "payload": payload
    }

    svi.append(novi_unos)

    with open(fajl, 'w') as f:
        json.dump(svi, f, indent=2, ensure_ascii=False)

    print(f"[✓] Logovano: {url} ({status})")
