# core_loop.py
import time
from foxstrike_safe import run_shadowfox_on_target

def main():
    try:
        with open("targets.txt") as f:
            targets = [l.strip() for l in f if l.strip()]

        for tgt in targets:
            run_shadowfox_on_target(tgt)
            print("\n[INFO] Pauza pre sledeće mete…\n")
            time.sleep(5)

    except KeyboardInterrupt:
        print("\n[!] Prekid detektovan – core loop zaustavljen.")
        exit(0)
    except FileNotFoundError:
        print("[ERROR] targets.txt nije pronađen.")
        exit(1)

if __name__ == "__main__":
    main()
