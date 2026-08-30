from ai_engineer.llm.structured import demo_ticket_analysis
def test_structured_ticket():
 r=demo_ticket_analysis('Production login outage','All users cannot access the production system.'); assert r.category=='authentication'; assert r.priority=='critical'; assert 0<=r.confidence<=1
