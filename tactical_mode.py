# tactical_mode.py
import os
from core_loop import main as start_mission
from shadow_dashboard import show_dashboard
from report_writer import generate_reports
from shadowlog_analyzer import analyze

def menu():
    while True:
        os.system("clear")
        print("=== SHADOWFOX10 :: TAKTIČKI MOD ===")
        print("[1] Pokreni AI misiju")
        print("[2] Pregledaj dashboard")
        print("[3] Analiza logova (Top payload-i)")
        print("[4] Exportuj izveštaje")
        print("[5] Izađi")
        izbor = input("Izbor: ")

        if izbor == "1":
            start_mission()
        elif izbor == "2":
            show_dashboard()
            input("\nPritisni ENTER za nastavak...")
        elif izbor == "3":
            analyze()
            input("\nPritisni ENTER za nastavak...")
        elif izbor == "4":
            generate_reports()
            input("\nIzveštaj završen. ENTER za nastavak...")
        elif izbor == "5":
            print("Zatvaram ShadowFox10.")
            break
        else:
            print("Nepoznat unos.")
            input("ENTER za pokušaj ponovo.")

if __name__ == "__main__":
    menu()
