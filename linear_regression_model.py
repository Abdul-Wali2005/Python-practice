import numpy as np 
from sklearn.linear_model import LinearRegression

hours = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
marks = np.array([50, 55, 65, 70, 80])

model =LinearRegression()
model.fit(hours , marks)

print(model.coef_)
print(model.intercept_)
print(model.predict([[6]]))