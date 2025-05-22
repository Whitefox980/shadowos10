# payload_disguise_engine.py
import random, json
def disguise_payload(payload):
    disguises = [
        lambda p: json.dumps({"action":"sync","data":{"token":p}}),
        lambda p: f"<form action='/submit'><input name='note' value='{p}'></form>",
        lambda p: f"<!--URGENT:{p}-->",
        lambda p: f"<script data-info='init'>{p}</script>"
    ]
    return random.choice(disguises)(payload)
