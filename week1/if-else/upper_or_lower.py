# 2. Write a python program to check whether a character is uppercase or lowercase alphabet.

char = input('Enter alphabet character: ')

if char.isalpha():
    if char.isupper():
        print (f'{char} is uppercase')
    elif char.islower():
        print (f'{char} is lowercase')
    else:
        print ('Please make sure you entered a single alphabet character')
else:
    print (f'{char} is not an alphabet')