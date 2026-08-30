import requests
from ai_engineer.config import USE_OLLAMA, OLLAMA_BASE_URL, OLLAMA_MODEL

def generate(prompt: str, fallback: str='Demo response generated without an LLM.'):
    if not USE_OLLAMA: return fallback
    try:
        r=requests.post(f'{OLLAMA_BASE_URL}/api/generate',json={'model':OLLAMA_MODEL,'prompt':prompt,'stream':False},timeout=30)
        r.raise_for_status(); return r.json().get('response',fallback)
    except Exception:
        return fallback
