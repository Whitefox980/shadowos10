import sqlite3
import os

DB_FILE = "rainbow_tables.db"

def _ensure_db():
    if not os.path.exists(DB_FILE):
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        c.execute('''CREATE TABLE hits (payload TEXT, status TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
        conn.commit()
        conn.close()

def log_hit(url, status):
    print(f"[LOG] {status} :: {url}")

def update_table(payload, status):
    _ensure_db()
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("INSERT INTO hits (payload, status) VALUES (?, ?)", (payload, status))
    conn.commit()
    conn.close()
