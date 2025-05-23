import time
import subprocess
from datetime import datetime

def log(m):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{now}] {m}")

def pokreni_posiljaoca():
    log("Pokrećem senka/posiljalac.py")
    subprocess.run(["python3", "senka/posiljalac.py"], env={"PYTHONPATH": "."})

def ciklus_napada():
    while True:
        pokreni_posiljaoca()
        log("Spavanje 180 sekundi...")
        time.sleep(180)

if __name__ == "__main__":
    log("Početak noćne misije ShadowFox: Senka aktivna.")
    try:
        ciklus_napada()
    except KeyboardInterrupt:
        log("Noćna misija prekinuta ručno.")
