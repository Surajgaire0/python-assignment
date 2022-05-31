# 6. Write a program to check if the number is Armstrong or not.

num = input('Enter a positive integer: ')

length = len(num)
sum = 0
for i in num:
    sum += int(i)**length

if sum == int(num):
    print ('Armstrong')
else:
    print ('Not Armstring')