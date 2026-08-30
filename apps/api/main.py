from fastapi import FastAPI
from pydantic import BaseModel
from ai_engineer.agents.agent import AIAssistant
from ai_engineer.security.guardrails import detect_prompt_injection
app=FastAPI(title='30-Day AI Engineer Playbook API',version='1.0.0'); assistant=AIAssistant()
class ChatRequest(BaseModel): message:str
@app.get('/health')
def health(): return {'status':'ok'}
@app.post('/chat')
def chat(req:ChatRequest):
    if detect_prompt_injection(req.message): return {'route':'blocked','answer':'Request blocked by security policy.','sources':[]}
    return assistant.run(req.message)
