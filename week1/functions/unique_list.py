# 5. Write a Python function that takes a list and returns a new list with unique elements of the first list

def unique_list(arr):
    new_list = []

    for ele in arr:
        if ele not in new_list:
            new_list.append(ele)

    return new_list


a = [1, 4, 2, 'str', '3', 4, 6]
print (unique_list(a))