# 5. A = ['a','b','c','d'] B = ['1','a','2','b']
# Find A union B and B union A.

a = ['a','b','c','d']
b = ['1','a','2','b']

setA = set(a)
setB = set(b)

print (f'A union B = {setA.union(setB)}')
print (f'A intersection B = {setA.intersection(setB)}')