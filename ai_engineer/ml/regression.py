from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

def train_regressor(X_train,y_train):
    m=LinearRegression(); m.fit(X_train,y_train); return m

def evaluate_regressor(model,X_test,y_test):
    p=model.predict(X_test)
    return {'mae':float(mean_absolute_error(y_test,p)),'r2':float(r2_score(y_test,p))}
