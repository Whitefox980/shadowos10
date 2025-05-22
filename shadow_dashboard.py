# shadow_dashboard.py
import json
from colorama import Fore, Style

def load_memory():
    try:
        with open("memory.json", "r") as f:
            return json.load(f)
    except:
        return {}

def show_dashboard():
    data = load_memory()

    print(Fore.CYAN + "\n==== SHADOWFOX10 :: DASHBOARD ====\n")
    if not data:
        print(Fore.RED + "[!] Nema podataka u memory.json")
        return

    for domain, entries in data.items():
        print(Fore.YELLOW + f"\n[+] META: {domain}")
        for e in entries[-5:]:  # zadnjih 5 napada
            status_color = Fore.GREEN if e["status"] == 200 else (
                           Fore.RED if e["status"] >= 500 else (
                           Fore.MAGENTA if e["status"] == 403 else Fore.WHITE))
            print(status_color + f"  ↳ {e['status']} :: {e['payload'][:60]}")

    print(Fore.CYAN + "\n==================================\n")

if __name__ == "__main__":
    show_dashboard()
