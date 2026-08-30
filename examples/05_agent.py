from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))

from ai_engineer.agents.agent import AIAssistant
a=AIAssistant()
for q in ['What is the travel reimbursement policy?','Tell me about Northstar Bank','Multiply 12 and 7']:
 print('\nQUERY:',q); print(a.run(q))
