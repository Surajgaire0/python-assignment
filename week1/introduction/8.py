# 8. Write a program to convert 108 to binary.

num = 108

def decimal_to_binary(num):
    result = i = 0
    while num > 0:
        num, rem = num // 2, num % 2
        result += rem * (10 ** i)
        i += 1
    return result

print (f'Binary of {num} is {decimal_to_binary(num)}')


# Alternative solution using built-in function
a = 108

print (f'Binary of {a} is {bin(a)[2:]}')