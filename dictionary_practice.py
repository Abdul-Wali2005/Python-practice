# student = { 'name': 'Abdul Wali' , 'age': '21', 'marks': '81'}
# print (student['name'])
# student['degree'] = 'AI'
# print (student)

# for key, value in student.items():
#     print (f"{key} : {value}")

marks = {'maths': 71 ,'science': 65, 'urdu': 69}
total = 0

for  key , value in marks.items():
    total += value
    
    
average = total/len(marks)
print ('average' ,average)    
    
    