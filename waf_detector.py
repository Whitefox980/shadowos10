# waf_detector.py
import requests
from colorama import Fore

def detect_waf(url):
    try:
        res = requests.get(url, timeout=5)
        headers = res.headers

        if "x-waf" in headers or "server" in headers and "cloudflare" in headers["server"].lower():
            print(Fore.MAGENTA + "[WAF] Cloudflare ili slična zaštita detektovana.")
        elif "content-security-policy" in headers:
            print(Fore.MAGENTA + "[CSP] Postoji Content-Security-Policy header.")
        else:
            print(Fore.GREEN + "[WAF] Nije detektovana vidljiva zaštita.")
    except Exception as e:
        print(Fore.RED + f"[!] Greška u WAF detekciji: {e}")
