from ai_engineer.llm.schemas import TicketAnalysis

def demo_ticket_analysis(subject, description):
    text=f'{subject} {description}'.lower()
    category='authentication' if any(x in text for x in ['login','password','authentication']) else 'general'
    priority='critical' if any(x in text for x in ['outage','all users','production down']) else 'normal'
    return TicketAnalysis(category=category,priority=priority,summary=f"{subject}: {' '.join(description.split())[:140]}",confidence=0.91 if category!='general' else 0.76)
