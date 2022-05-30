# 2. Write a Python code to calculate Combination (15,3)

from math import factorial


def combination(n,r):
    return factorial(n)/(factorial(r)*factorial(n-r))


print (combination(15,3))