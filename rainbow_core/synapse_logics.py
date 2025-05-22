import requests

def analyze_reflection(url):
    try:
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            return "200", r.text
        return str(r.status_code), r.text
    except Exception as e:
        return "ERROR", str(e)
