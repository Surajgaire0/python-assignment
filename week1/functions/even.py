# 6. Write a Python program to print the even numbers from a given list.

def print_even(arr):
    for i in arr:
        if i % 2 == 0:
            print (i)


print_even([1,2,3,4,5,6,7,8,9,0])