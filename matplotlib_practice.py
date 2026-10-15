import pandas as pd 
import matplotlib.pyplot as plt 

data = { 
        'name': ['Ali', 'Sara', 'Ahmad', 'Wali'],
        'marks':[75 , 65, 88, 45],
        'section':['A', 'B', 'C', 'A']
         }

df = pd.DataFrame(data)
plt.bar(df['name'], df['marks'])
plt.axhline(y=df['marks'].mean(), color='red')
plt.title(' Students marks')
plt.xlabel('student')
plt.ylabel('Marks')
plt.savefig('student_marks.png')
plt.show()