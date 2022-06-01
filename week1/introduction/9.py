# 9. Write a program to convert 1008 to hexadecimal.

num = 1008

def decimal_to_hexadecimal(num):
    result = ''
    replacements = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    while num > 0:
        num, rem = num // 16, num % 16
        rem = replacements[rem] if rem >= 10 else str(rem)
        result = rem + result
    return result

print (f'Hexadecimal of {num} is {decimal_to_hexadecimal(num)}')


# Alternative solution using built-in function
a = 1008

print (f'Hexadecimal of {a} is {hex(a)[2:]}')