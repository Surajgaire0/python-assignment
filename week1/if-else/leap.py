# 5. Write a program to check whether the entered year is leap year or not.

year = int(input('Enter year: '))

if year%4 != 0:
    print ('Not leap year')
else:
    if year%400==0:
        print ('Leap year')
    elif year%100==0:
        print ('Not leap year')
    else:
        print ('Leap year')