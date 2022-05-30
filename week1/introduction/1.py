# 1. Write a Python code to calculate Permutation (5,3)

def factorial(n):
    if n<1:
        return 1
    else:
        return n*factorial(n-1)

def permutation(n,r):
    return factorial(n)/factorial(n-r)


print ('Permutation(5,3) = ',permutation(5,3))