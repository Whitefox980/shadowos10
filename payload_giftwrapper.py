# payload_giftwrapper.py
import random
def wrap_payload(payload):
    wrappers = [
        lambda p: f"<div style='display:none'>{p}</div>",
        lambda p: f"<noscript>{p}</noscript>",
        lambda p: f"<textarea>{p}</textarea>",
        lambda p: f"<body onload={p}>"
    ]
    return random.choice(wrappers)(payload)
