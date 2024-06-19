"""
Given an array arr, replace every element in that array with the
greatest element among the elements to its right, and replace
the last element with -1.
"""


def replaceElements(arr):
    maximum = -1
    for idx in range(len(arr) - 1, -1, -1):
        tmp = arr[idx]
        arr[idx] = maximum
        if tmp > maximum:
            maximum = tmp
    return arr


print(replaceElements([17, 18, 5, 4, 6, 1]))  # [18,6,6,6,1,-1]
print(replaceElements([400]))  # [-1]
