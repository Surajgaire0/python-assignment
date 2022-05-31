# 1. Multiply 3*3 matrices
# Using for loops and print the result.

# 2. Multiply 3*3 matrices

def matmul(matA, matB):
    if (len(matA[0]) != len(matB)):
        return 'Matrix multiplication not possible'

    matC = []
    for i in range(len(matA)): # number of rows in A
        matC.append([])
        for j in range(len(matB[0])): # number of columns in B
            matC[i].append(0)
            for k in range(len(matB)): # number of rows in B, len(matA[0])=len(matB)
                matC[i][j] += matA[i][k] * matB[k][j]

    return matC

# 3*3
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = [[111, 22, 33], [44, 55, 56], [47, 86, 19]]

print (matmul(a,b))

# 4*4
c = [[111, 22, 33, 44], [44, 55, 56, 1], [47, 86, 19, 2], [1, 2, 22, 3]]
d = [[11, 22, 3, 4], [4, 5, 6, 1], [7, 6, 19, 2], [1, 2, 22, 3]]

print (matmul(c, d))