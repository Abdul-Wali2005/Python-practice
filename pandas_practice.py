import pandas as pd 
data = { 
        'name': ['Ali', 'Sara', 'Ahmad', 'Wali'],
        'marks':[75 , 65, 88, 45],
        'section':['A', 'B', 'C', 'A']
         }

dr= pd.DataFrame(data)
print(dr)


print (dr ['marks'].mean())
print (dr ['marks'] > 70)
print (dr [dr ['marks'] > 70])
print (dr.shape)
print (dr['section']=='A')
print (f"Average marks of A section: {dr[dr['section']=='A']['marks'].mean()}")
print (f"Maximum marks: {dr['marks'].max()}")
