# auto_ai_strategy.py
def evaluate_response(response):
    if response.status_code >= 500:
        return "aggressive"
    elif "captcha" in response.text.lower():
        return "stealth"
    elif response.status_code == 403:
        return "waf_detected"
    elif "alert" in response.text.lower():
        return "vulnerable"
    return "neutral"
