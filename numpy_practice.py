
import numpy as np

marks = np.array([55 , 72 , 88, 91, 64 ])

print ( f" average or mean is :{marks.mean()}")
print ( f" maximum is :{marks.max()}")
print ( f" minimum is :{marks.min()}")
print ( f" number of students with marks > 70 is :{(marks > 70).sum()}")
