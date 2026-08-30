import re
from ai_engineer.agents.router import route
from ai_engineer.agents.tools import customer_lookup, calculator
from ai_engineer.rag.answer import answer_question
from ai_engineer.llm.client import generate

class AIAssistant:
    def run(self,query):
        target=route(query)
        if target=='knowledge':
            r=answer_question(query); return {'route':target,**r}
        if target=='customer':
            name='Northstar Bank' if 'northstar' in query.lower() else 'Acme Retail'
            return {'route':target,'answer':str(customer_lookup(name)),'sources':[]}
        if target=='calculator':
            nums=[float(x) for x in re.findall(r'-?\d+(?:\.\d+)?',query)]
            if len(nums)>=2:
                t=query.lower(); op='multiply' if 'multiply' in t or '*' in t else ('divide' if 'divide' in t else 'add')
                return {'route':target,'answer':str(calculator(nums[0],nums[1],op)),'sources':[]}
        return {'route':'general','answer':generate(query,fallback='This is a demo AI engineering assistant.'),'sources':[]}
