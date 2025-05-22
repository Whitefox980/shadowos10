# fox_agent_behavior.py
import requests, random
from network_blender import blended_headers
from smart_timing import adaptive_sleep
from ai_analyzer import analyze_response

def simulate_user_behavior(target_url, payload):
    sess = requests.Session()
    sess.headers.update(blended_headers())

    # ➊ obilazak
    pages = ["/","/products","/about","/search?q=tea","/faq"]
    for path in random.sample(pages,3):
        try: sess.get(target_url.rstrip("/") + path); adaptive_sleep()
        except: pass

    # ➋ benigni POST
    try: sess.post(target_url,data={"note":"just visiting"}); adaptive_sleep()
    except: pass

    # ➌ Šapat payload-a
    try:
        final = f"{target_url}?q={payload}"
        res = sess.get(final)
        analyze_response(final,payload,res)
    except Exception as e:
        print(f"[X] Greška: {e}")
