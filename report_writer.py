# report_writer.py
import json
import os
from datetime import datetime

def load_memory():
    try:
        with open("memory.json", "r") as f:
            return json.load(f)
    except:
        return {}

def generate_reports():
    memory = load_memory()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")

    if not memory:
        print("[!] Nema zapisa u memory.json")
        return

    os.makedirs("reports/exported", exist_ok=True)

    for domain, entries in memory.items():
        filename = f"reports/exported/{domain.replace('.', '_')}_{timestamp}.txt"
        with open(filename, "w") as f:
            f.write(f"=== SHADOWFOX10 :: SECURITY REPORT ===\n")
            f.write(f"Target: {domain}\n\n")

            for e in entries:
                f.write(f"[STATUS]: {e['status']}\n")
                f.write(f"[PAYLOAD]: {e['payload']}\n")
                f.write(f"---\n")

        print(f"[✓] Izveštaj generisan: {filename}")

if __name__ == "__main__":
    generate_reports()
