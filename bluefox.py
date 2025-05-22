# bluefox.py
import os
from foxstrike import run_attack
from user_simulator import simulate_user
from waf_detector import detect_waf
from colorama import Fore, init

init(autoreset=True)

def main():
    print(Fore.CYAN + "\n[ShadowFox10] AI Fuzz Framework aktiviran...")

    if not os.path.exists("targets.txt"):
        print(Fore.RED + "[!] targets.txt ne postoji.")
        return

    with open("targets.txt", "r") as f:
        targets = [line.strip() for line in f if line.strip()]

    for target in targets:
        print(Fore.YELLOW + f"\n[META] → {target}")
        simulate_user(target)
        detect_waf(target)
        run_attack(target)

if __name__ == "__main__":
    main()
