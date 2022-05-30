# 5. Write a Python code to calculate LCM of (25,55)

from math import gcd


a=25
b=55

print ('LCM = ' + str(a*b/gcd(a,b)))