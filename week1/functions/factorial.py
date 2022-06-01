# 3. Write a Python function to calculate the factorial of a number (a non-negative integer). 
# The function accepts the number as an argument.

def factorial(num):
    if num < 0:
        return 'Factorial of negative number is a complex number'
    elif num <= 1:
        return 1
    return num * factorial(num - 1)


print (factorial(9))