# ai_analyzer.py
from colorama import Fore
import json, os
from payload_classifier import classify

def analyze_response(url, payload, res):
    status = res.status_code
    ptype = classify(payload)
    content = res.text[:300]
    confirmed = False

    # DUBINSKA DETEKCIJA
    if "root:x:" in res.text or "/bin/bash" in res.text:
        ptype = "LFI-Confirmed"
        confirmed = True
    elif "<script>alert(" in res.text or "xss" in res.text:
        ptype = "XSS-Confirmed"
        confirmed = True
    elif "syntax error" in res.text or "SQL" in res.text or "PDOException" in res.text:
        ptype = "SQLi-Confirmed"
        confirmed = True

    # Log boja
    color = Fore.GREEN if confirmed else (Fore.MAGENTA if status == 200 else Fore.RED)
    print(color + f"[{status} :: {ptype}] {url}")

    save_report(url, payload, status, ptype, content)
    update_memory(url, payload, status, ptype)

def save_report(url, payload, status, ptype, snippet):
    os.makedirs("reports", exist_ok=True)
    report = {
        "url": url, "status": status, "payload": payload,
        "type": ptype, "snippet": snippet
    }
    path = f"reports/{ptype}.json"
    data = []
    if os.path.exists(path):
        try:
            data = json.load(open(path))
        except: pass
    data.append(report)
    json.dump(data, open(path, "w"), indent=2)

def update_memory(url, payload, status, ptype):
    mem_path = "memory.json"
    memory = {}
    if os.path.exists(mem_path):
        try:
            memory = json.load(open(mem_path))
        except: pass
    dom = url.split("/")[2]
    memory.setdefault(dom, []).append({
        "payload": payload, "status": status, "type": ptype
    })
    json.dump(memory, open(mem_path, "w"), indent=2)
