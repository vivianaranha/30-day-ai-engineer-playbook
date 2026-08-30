from sklearn.datasets import load_iris, load_diabetes
from sklearn.model_selection import train_test_split

def iris_split(test_size=0.25, random_state=42):
    d = load_iris()
    return train_test_split(d.data,d.target,test_size=test_size,random_state=random_state,stratify=d.target)

def diabetes_split(test_size=0.25, random_state=42):
    d = load_diabetes()
    return train_test_split(d.data,d.target,test_size=test_size,random_state=random_state)
