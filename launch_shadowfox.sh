#!/data/data/com.termux/files/usr/bin/bash

echo "🦊 Pokrećem ShadowFox10 lisicu..."

cd ~/shadowfox10 || exit 1

# 1. Kreiraj venv ako ne postoji
if [ ! -d "env" ]; then
    echo "[+] Virtuelno okruženje ne postoji – pravim..."
    python -m venv env
fi

# 2. Aktiviraj venv
if [ -f "env/bin/activate" ]; then
    source env/bin/activate
else
    echo "[ERROR] env/bin/activate nije pronađen."
    exit 1
fi

# 3. Instaliraj pakete ako treba
if ! python -c "import requests" &> /dev/null; then
    echo "[+] Instaliram zavisnosti..."
    pip install requests colorama beautifulsoup4
fi

# 4. Kreiraj tactical_mode.py ako ne postoji
if [ ! -f "tactical_mode.py" ]; then
    echo "[+] tactical_mode.py nije pronađen – kreiram minimalni fajl..."
    cat > tactical_mode.py <<EOF
def menu():
    print("ShadowFox10 taktički režim aktiviran.")
    print("[1] Demo režim lisice.")
    print("[X] Dodaj ceo kod kasnije.")
if __name__ == "__main__":
    menu()
EOF
fi

# 5. Kreiraj targets.txt ako fali
if [ ! -f "targets.txt" ]; then
    echo "https://juice-shop.herokuapp.com" > targets.txt
    echo "[+] Ubacujem default metu."
fi

# 6. Pokreni
echo "[✓] ShadowFox10 komandni centar aktivan."
python tactical_mode.py
