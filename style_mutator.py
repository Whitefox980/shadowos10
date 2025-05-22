# style_mutator.py
import random
def style_mutate(payload):
    styles = [
        lambda p: p[::-1],
        lambda p: "".join(f"&#{ord(c)};" for c in p),
        lambda p: p.replace("<", "&lt;").replace(">", "&gt;"),
        lambda p: f"<template>{p}</template>"
    ]
    return random.choice(styles)(payload)
