# senka/shadowpersona.py

import requests
import random
import json
import time

# Učitavanje ruta
with open("senka/routes.txt", "r") as f:
    routes = [line.strip() for line in f if line.strip()]

# Učitavanje stilizovanih payload-a
with open("senka/stylizovani.json", "r") as f:
    payloads = json.load(f)

# Učitavanje legitimnih zaglavlja
with open("senka/legit_headers.json", "r") as f:
    headers_list = json.load(f)

# Logovanje
log_file = open("senka/trace.log", "a")

# Glavni ciklus senke
def senka_walk():
    for route in routes:
        url = route + random.choice(["?q=", "?search=", "?input=", "?s=", "?query="])
        payload = random.choice(payloads)
        headers = random.choice(headers_list)

        try:
            response = requests.get(url + payload, headers=headers, timeout=10)
            status = response.status_code
            size = len(response.content)

            log = f"[{time.ctime()}] {url}{payload} → {status} [{size}B]"
            print(log)
            log_file.write(log + "\n")

        except Exception as e:
            err_log = f"[{time.ctime()}] ERROR: {e}"
            print(err_log)
            log_file.write(err_log + "\n")

# Pokretanje
if __name__ == "__main__":
    senka_walk()
    log_file.close()
