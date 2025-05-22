import random, time

def human_delay(mean=5.0, std=2.0, min_d=2, max_d=12):
    delay = random.gauss(mean, std)
    delay = max(min_d, min(max_d, delay))
    time.sleep(delay)
