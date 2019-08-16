import lightgbm as lgb
import pandas as pd

df = pd.read_csv('test/support/boston.csv')

X = df.drop(columns=['medv'])
y = df['medv']

X_train = X[:300]
y_train = y[:300]
X_test = X[300:]
y_test = y[300:]

model = lgb.LGBMRegressor()
model.fit(X_train, y_train)
print(model.predict(X_test))
