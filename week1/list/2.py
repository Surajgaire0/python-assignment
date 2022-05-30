# 2. Make a list of ten students in your class. Print the name of each student whose name ends with ‘a’.

students=['Suraj','Mishra','Madhav','Kusal','Bibek','Bikash','Bijaya','Sunil','Umesh','Sudarshan']

for student in students:
    if student.endswith('a'):
        print (student)