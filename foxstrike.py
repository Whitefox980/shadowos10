# foxstrike.py
from payload_mutator import generate_payloads
from fox_agent_behavior import simulate_user_behavior

def run_attack(target):
    for p in generate_payloads():
        simulate_user_behavior(target, p)
