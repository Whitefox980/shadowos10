# user_simulator.py
import requests, random, time
from colorama import Fore

def human_delay(mean=5.0, std=2.0, min_d=2, max_d=12):
    delay = random.gauss(mean, std)
    delay = max(min_d, min(max_d, delay))
    time.sleep(delay)

def blended_headers():
    agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Mozilla/5.0 (Linux; Android 11; SM-G960F)",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0)"
    ]
    referers = [
        "https://google.com",
        "https://duckduckgo.com",
        "https://reddit.com"
    ]
    return {
        "User-Agent": random.choice(agents),
        "Referer": random.choice(referers),
        "X-Forwarded-For": ".".join(str(random.randint(1, 255)) for _ in range(4)),
        "Accept-Encoding": "gzip, deflate"
    }

def fake_navigation(base_url, session):
    paths = ["/", "/about", "/search?q=vitamin", "/products", "/faq"]
    for path in random.sample(paths, k=random.randint(2, 4)):
        try:
            session.get(base_url.rstrip("/") + path)
            human_delay()
        except:
            pass

def simulate_user(base_url):
    print(Fore.GREEN + "[Simulacija] Korisnik se ponaša kao pravi...")

    session = requests.Session()
    session.headers.update(blended_headers())

    fake_navigation(base_url, session)

    print(Fore.GREEN + "[Simulacija] Sad šapćemo payload serveru...")
