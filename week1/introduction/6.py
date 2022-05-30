# 6. Ask enter to enter two numbers (say, a and b). Generate two random numbers between 
# those two numbers and find a combination of these two newly generated random numbers.

from math import factorial
from random import randint


def combination(n,r):
    return factorial(n)/(factorial(r)*factorial(n-r))


num1 = int(input('Enter first integer: '))
num2 = int(input('Enter second integer (greater than first integer): '))

random1 = randint(num1, num2)
random2 = randint(num1, num2)

comb = combination(random1, random2) if random1 > random2 else combination(random2, random1)

print (f'Generated random numbers are {random1} and {random2}')
print (f'Combination = {comb}')