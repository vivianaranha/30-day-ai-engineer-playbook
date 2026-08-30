from ai_engineer.agents.agent import AIAssistant
def test_customer_route():
 r=AIAssistant().run('Tell me about Northstar Bank'); assert r['route']=='customer'; assert 'Financial Services' in r['answer']
def test_calculator_route():
 r=AIAssistant().run('Multiply 12 and 7'); assert r['route']=='calculator'; assert '84' in r['answer']
