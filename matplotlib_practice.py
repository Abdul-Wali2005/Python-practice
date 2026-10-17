import pandas as pd 
import matplotlib.pyplot as plt 

data = { 
        'name': ['Ali', 'Sara', 'Ahmad', 'Wali'],
        'marks':[75 , 65, 88, 45],
        'section':['A', 'B', 'C', 'A']
         }

import matplotlib.pyplot as plt

df = pd.DataFrame(data)
avg = df.groupby('section')['marks'].mean()
plt.bar(avg.index, avg.values)
plt.title("Average Marks by Section")
plt.xlabel("Section")
plt.ylabel("Average Marks")
plt.savefig('average_marks_by_section.png')
plt.show()


# plt.bar(df['name'], df['marks'])
# plt.axhline(y=df['marks'].mean(), color='red')
# plt.title(' Students marks')
# plt.xlabel('student')
# plt.ylabel('Marks')
# plt.savefig('student_marks.png')
# plt.show()