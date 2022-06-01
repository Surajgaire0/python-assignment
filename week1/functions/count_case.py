# 4. Write a Python function that accepts a string and calculates the number of uppercase letters and lowercase letters.

def count_case(string):
    up = low = 0

    for c in string:
        if 65 <= ord(c) <= 90:
            up += 1
        elif 97 <= ord(c) <= 122:
            low += 1
    
    return up, low


string = 'Hello Python3'

print (f'"{string}" has {count_case(string)[0]} uppercase characters and {count_case(string)[1]} lowercase characters.')