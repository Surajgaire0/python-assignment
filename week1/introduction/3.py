# 3. Write a Python code that takes the degree as input from the user and convert it into radian.

from math import pi


def deg_to_rad(degree):
    'Converts degree to radian'
    return degree * pi / 180


degree=float(input('Enter degree: '))
print (f'{degree} degree is equal to {deg_to_rad(degree)} radian')