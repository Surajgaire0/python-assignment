# 4. Write a Python code that inputs input from the user and calculate its square root.

from math import sqrt


num=float(input('Enter a number: '))
sq_root=sqrt(num) if num>=0 else str(sqrt(abs(num)))+'i'

print (f'Square root = {sq_root}')