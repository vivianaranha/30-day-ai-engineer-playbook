import json
from pathlib import Path
from ai_engineer.agents.agent import AIAssistant
from ai_engineer.evaluation.metrics import contains_expected, route_accuracy

def run(path='data/eval_cases.json'):
    cases=json.loads(Path(path).read_text(encoding='utf-8')); a=AIAssistant(); out=[]
    for c in cases:
        r=a.run(c['query']); out.append({'query':c['query'],'task_score':contains_expected(r['answer'],c.get('expected_contains',[])),'route_score':route_accuracy(c['expected_route'],r['route'])})
    return out
