# 1. Students = ['jack','jill','david','silva','ronaldo']
# Marks = ['55','56','57','66','76']
# Make a dictionary using lists above and delete the key-value (students:marks) pairs with lowest marks. 

students = ['jack','jill','david','silva','ronaldo']
marks = ['55','56','57','66','76']

student_marks = dict(zip(students, marks))
print (student_marks)

student_marks = {name:marks for name,marks in student_marks.items() if marks != min(student_marks.values())}
print ('Deleting key value pair with lowest marks')
print (student_marks)