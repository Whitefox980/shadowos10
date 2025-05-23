import random

def generisi_header():
    profili = [
        {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120",
            "Accept": "text/html,application/xhtml+xml",
            "Accept-Language": "en-US,en;q=0.9",
            "Connection": "keep-alive"
        },
        {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_3 like Mac OS X)",
            "Accept": "text/html",
            "Accept-Language": "en-US"
        },
        {
            "User-Agent": "curl/8.0.1",
            "Accept": "*/*"
        },
        {
            "User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)",
            "Accept": "text/html"
        },
        {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "Accept": "application/json"
        }
    ]
    return random.choice(profili)
