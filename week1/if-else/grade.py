# 7. Write a program to compute the grade from marks. 

#     Marks	          Grade
# Marks<=50	           F
# 60>=marks>50	       E
# 70>= marks > 60	   D
# 80>= marks > 70      C
# 90 > = marks > 80	   B
# 100>= marks >90	   A

def compute_grade(marks):
    if marks <= 50:
        return 'F'
    elif marks <= 60:
        return 'E'
    elif marks <= 70:
        return 'D'
    elif marks <= 80:
        return 'C'
    elif marks <= 90:
        return 'B'
    else:
        return 'A'

marks = float(input('Enter marks (0 to 100): '))

print ('Grade: ', compute_grade(marks))