# smart_timing.py
import random, time
def adaptive_sleep(mean=5.0, std=2.0, lo=2, hi=12):
    d = max(lo, min(hi, random.gauss(mean, std)))
    time.sleep(d)
