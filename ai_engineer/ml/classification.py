from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_recall_fscore_support

def train_classifier(X_train,y_train):
    m=LogisticRegression(max_iter=1000); m.fit(X_train,y_train); return m

def evaluate_classifier(model,X_test,y_test):
    p=model.predict(X_test)
    precision, recall, f1, _ = precision_recall_fscore_support(y_test,p,average='macro',zero_division=0)
    return {'accuracy':float(accuracy_score(y_test,p)),'precision':float(precision),'recall':float(recall),'f1':float(f1)}
