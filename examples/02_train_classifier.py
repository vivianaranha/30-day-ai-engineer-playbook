from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))

from ai_engineer.ml.datasets import iris_split
from ai_engineer.ml.classification import train_classifier,evaluate_classifier
X_train,X_test,y_train,y_test=iris_split(); m=train_classifier(X_train,y_train); print(evaluate_classifier(m,X_test,y_test))
