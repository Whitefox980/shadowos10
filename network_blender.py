# network_blender.py
import random
def blended_headers():
    agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Mozilla/5.0 (Linux; Android 11; SM-G960F)",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0)"
    ]
    referers = [
        "https://google.com", "https://duckduckgo.com",
        "https://reddit.com", "https://youtube.com"
    ]
    return {
        "User-Agent": random.choice(agents),
        "Referer": random.choice(referers),
        "Accept-Encoding": "gzip, deflate",
        "X-Forwarded-For": ".".join(str(random.randint(1, 255)) for _ in range(4))
    }
