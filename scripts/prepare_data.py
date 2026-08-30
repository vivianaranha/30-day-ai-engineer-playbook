from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]; p=ROOT/'data'/'sample_text_classification.csv'; df=pd.read_csv(p)
print(f'Loaded {len(df)} rows'); print(df.head().to_string(index=False))
