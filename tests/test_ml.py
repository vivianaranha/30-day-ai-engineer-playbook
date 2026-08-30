from ai_engineer.ml.datasets import iris_split,diabetes_split
from ai_engineer.ml.classification import train_classifier,evaluate_classifier
from ai_engineer.ml.regression import train_regressor,evaluate_regressor
def test_classifier():
 X_train,X_test,y_train,y_test=iris_split(); r=evaluate_classifier(train_classifier(X_train,y_train),X_test,y_test); assert r['accuracy']>0.8
def test_regressor():
 X_train,X_test,y_train,y_test=diabetes_split(); r=evaluate_regressor(train_regressor(X_train,y_train),X_test,y_test); assert r['mae']>0
