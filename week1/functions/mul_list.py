# 2. Write a Python function to multiply all the numbers in a list.

def mul_ele_of_list(arr):
    if not len(arr):
        return  None

    product = 1

    for ele in arr:
        product *= ele

    return product


a = [-1, 2, -1]
print (mul_ele_of_list(a))