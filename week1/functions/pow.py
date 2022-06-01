# 1. Write a function that calculates the X to the power Y 

def pow(x, y):
    product = 1

    for i in range(y):
        product *= x
    
    return product


a = 11
b = 2

print (f'{a} to the power {b} is {pow(a, b)}')