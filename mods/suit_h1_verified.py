suit = {
    "name": "H1_Verified",
    "headers": {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "X-HackerOne-Research": "Whitefox980_H1_Verified",
        "Referer": "https://google.com"
    },
    "params": ["q", "query", "input", "token"],
    "obfuscate": lambda payload: f"eval(String.fromCharCode({','.join(str(ord(c)) for c in payload)}))",
    "navigate": ["/", "/support", "/contact", "/about"],
    "delay": [3, 5, 7]
}
