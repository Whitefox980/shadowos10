# payload_classifier.py
def classify(p):
    pl = p.lower()
    if "<script>" in pl or "alert(" in pl:             return "XSS"
    if "../" in pl or "etc/passwd" in pl:              return "LFI"
    if "' or " in pl or '" or ' in pl:                return "SQLi"
    if "onerror=" in pl or "<img" in pl:              return "Evt-XSS"
    return "Other"
