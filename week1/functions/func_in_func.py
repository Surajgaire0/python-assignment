# 10. Write a Python program to access a function inside a function

def map(func, list_a):
    return [func(ele) for ele in list_a]

increment = lambda x : x + 1


a = [1,2,3]
print (a)
print (map(increment, a))
