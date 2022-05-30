# 6. Calculate the mean and standard deviation of the following list:
# Numbers = [1,2,3,5,88,99,55,33,41,52]

from math import sqrt


numbers = [1,2,3,5,88,99,55,33,41,52]

mean = sum(numbers)/len(numbers)
std = sqrt(sum([(x-mean)**2 for x in numbers])/len(numbers))

print ('Mean = ', mean)
print ('standard deviation = ', std)