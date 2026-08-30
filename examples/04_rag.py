from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))

from ai_engineer.rag.answer import answer_question
print(answer_question('What is the travel reimbursement policy?'))
