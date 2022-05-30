# 2. Write a program to calculate direction and magnitude of the vector described by the following points.
# A = (20,30)
# B = (30,40)

from math import sqrt, atan 
def calculate_mag_and_dir(p1, p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    mag = sqrt(dx*dx+dy*dy)
    dir = atan(dy/dx)
    return mag, dir


a = (20, 30)
b = (30, 40)

magnitude, direction = calculate_mag_and_dir(a, b)

print (f'Magnitude = {magnitude} units', f'Direction = {direction} radians', sep='\n')