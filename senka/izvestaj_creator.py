import json
from datetime import datetime
import os

LOG_FAJL = "mutacije.log"
IZLAZ_FOLDER = "izvestaji"

def ucitaj_linije():
    rezultati = []
    if not os.path.exists(LOG_FAJL):
        print(f"[X] Log fajl ne postoji: {LOG_FAJL}")
        return rezultati

    with open(LOG_FAJL, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                rezultati.append(json.loads(line))
            except json.JSONDecodeError:
                print(f"[!] Preskačem nevalidan red: {line[:60]}...")
    return rezultati
def filtriraj_uspesne(logovi):
    return [entry for entry in logovi if entry.get("status") == 200]

def snimi_izvestaj(uspesni):
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    izlaz_fajl = os.path.join(IZLAZ_FOLDER, f"izvestaj_{timestamp}.json")
    with open(izlaz_fajl, "w") as f:
        json.dump(uspesni, f, indent=2)
    print(f"[✓] Izveštaj sačuvan: {izlaz_fajl}")

if __name__ == "__main__":
    logovi = ucitaj_linije()
    uspesni = filtriraj_uspesne(logovi)
    if not uspesni:
        print("[!] Nema uspešnih payload-a u logu.")
    else:
        snimi_izvestaj(uspesni)
