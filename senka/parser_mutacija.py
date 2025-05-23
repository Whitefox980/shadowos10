import re

def ucitaj_mutacije_putanje(fajl='mutacije.log'):
    with open(fajl, 'r') as f:
        linije = f.readlines()

    zapisi = []
    trenutni_url = None
    trenutni_payload = None

    for linija in linije:
        linija = linija.strip()

        if linija.startswith("[http"):
            # Primer: [https://www.syfe.com] <iframe ...>
            try:
                match = re.match(r"(.*?) (.+)", linija)
                if match:
                    url, payload = match.groups()
                    zapisi.append((url, payload))
            except:
                continue

    return zapisi


def sacuvaj_uspesne(zapisi, fajl_out="uspesni_payloadi.txt"):
    with open(fajl_out, "w") as f:
        for url, payload in zapisi:
            linija = f"{url} | {payload}"
            f.write(linija + "\n")

    print(f"[✓] Sačuvano: {fajl_out} ({len(zapisi)} linija)")


if __name__ == "__main__":
    zapisi = ucitaj_mutacije_putanje()
    sacuvaj_uspesne(zapisi)
