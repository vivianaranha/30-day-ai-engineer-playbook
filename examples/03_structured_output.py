from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))

from ai_engineer.llm.structured import demo_ticket_analysis
print(demo_ticket_analysis('Production login outage','All users cannot access the production system.').model_dump())
