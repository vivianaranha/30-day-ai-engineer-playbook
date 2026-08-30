from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from ai_engineer.evaluation.run_eval import run
for x in run(str(ROOT/'data'/'eval_cases.json')): print(x)
