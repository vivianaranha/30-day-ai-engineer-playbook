def detect_prompt_injection(text):
    patterns=['ignore previous instructions','reveal system prompt','bypass security','ignore all rules']
    return any(p in text.lower() for p in patterns)
def contains_secret_like_text(text):
    return any(x in text.lower() for x in ['api_key=','password=','secret=','token='])
