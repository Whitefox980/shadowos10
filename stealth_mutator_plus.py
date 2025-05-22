headers = {
    "User-Agent": random.choice([
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/122.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Safari/605.1.15",
        "Mozilla/5.0 (Linux; Android 11; SM-G991B) Chrome/111.0",
    ]),
    "Referer": random.choice([
        "https://www.google.com/",
        "https://duckduckgo.com/?q=invest",
        "https://www.linkedin.com/jobs/"
    ]),
    "Origin": "https://www.google.com",
    "X-Requested-With": "XMLHttpRequest",
    "X-HackerOne-Research": "Whitefox980H1_Stealth",
    "X-Forwarded-For": f"192.168.{random.randint(1,254)}.{random.randint(1,254)}"
}
