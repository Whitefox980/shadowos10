import json
from datetime import datetime

with open("top_hits.json", "r") as f:
    podaci = json.load(f)

html = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Top Payload Izveštaj</title>
<style>
body { font-family: Arial; background: #111; color: #eee; padding: 20px; }
table { border-collapse: collapse; width: 100%; }
th, td { border: 1px solid #444; padding: 8px; text-align: left; }
th { background-color: #222; }
tr:nth-child(even) { background-color: #1a1a1a; }
a { color: #4ef; text-decoration: none; }
</style>
</head>
<body>
<h2>Top Payload Izveštaj</h2>
<table>
<tr><th>#</th><th>Vreme</th><th>Status</th><th>URL</th><th>Payload</th></tr>
"""

for i, unos in enumerate(podaci, 1):
    vreme = unos.get("vreme", "N/A")
    url = unos.get("url", "N/A")
    status = unos.get("status", "N/A")
    payload = unos.get("payload", "")
    html += f"<tr><td>{i}</td><td>{vreme}</td><td>{status}</td><td><a href='{url}' target='_blank'>{url}</a></td><td>{payload}</td></tr>\n"

html += "</table></body></html>"

with open("izvestaj_top_hits.html", "w") as f:
    f.write(html)

print("[✓] Generisan: izvestaj_top_hits.html")
