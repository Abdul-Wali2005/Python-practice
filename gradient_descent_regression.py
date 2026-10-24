import numpy as np

x = np.array([1,2,3,4,5])
y = np.array([50,55,65,70,80])

m = 0.0
c = 0.0
learning_rate = 0.01


for step in range(10000):
         y_pred = m*x + c
         error = y_pred - y
         
         dm = 2 * (error * x).mean()
         dc = 2 * (error).mean()
         
         m = m - learning_rate * dm
         c = c - learning_rate * dc
         
print (round(m,3) ,round(c,0))
         


