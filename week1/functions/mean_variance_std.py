# 14. Write three different functions to calculate the mean, variance and standard deviation of the following data. 
# You need to call your mean function to within your variance and standard deviation functions.

# S.N	Students	Marks
# 1	Richard	24
# 2	Lara	36
# 3	Prava	45
# 4	Peter	45
# 5	Judas	96
# 6	Jimmy	56
# 7	Jimi	89
# 8	Ronaldo	12
# 9	Messi	10
# 10	Pogba	100

from math import sqrt


def mean(arr):
    return sum(arr)/len(arr)

def variance(arr):
    avg = mean(arr)
    return sum([(x - avg) ** 2 for x in arr]) / len(arr)

def std(arr):
    return sqrt(variance(arr))


marks = [24, 36, 45, 45, 96, 56, 89, 12, 10, 100]
print ('Mean =', mean(marks))
print ('Variance =', variance(marks))
print ('standard Deviation =', std(marks))