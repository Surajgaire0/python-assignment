# 1. Write a python program to find the largest of three numbers .

num1=float(input('Enter 1st number: '))
num2=float(input('Enter 2nd number: '))
num3=float(input('Enter 3rd number: '))

if num1 >= num2 and num1 >= num3:
    print ('Largest number = ', num1)
elif num2 >= num3:
    print ('Largest number = ', num2)
else:
    print ('Largest number = ', num3)


# Alternative
# print (max(num1, num2, num3))