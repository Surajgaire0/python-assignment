# 13. Write a python module with multiple sorting algorithms as its functions

def bubble_sort(a):
    for i in range(len(a) - 1):
        swapped = False
        for j in range(1, len(a) - i):
            if a[j -1] > a[j]:
                a[j -1], a[j] = a[j], a[j - 1]
                swapped = True
        if not swapped:
            break
    return a

def selection_sort(a):
    for i in range(len(a) - 1):
        min = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min]:
                min = j
        if min != i:
            a[min], a[i] = a[i], a[min]
    return a

def insertion_sort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j > 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


if __name__ == '__main__':
    k = [1, 5, 3, 23, 45, 2]

    print (insertion_sort(k[:]))
    print (selection_sort(k[:]))
    print (bubble_sort(k[:]))