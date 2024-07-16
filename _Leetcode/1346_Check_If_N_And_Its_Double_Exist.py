"""
Given an array arr of integers, check if there
exist two indices i and j such that :
---- i != j
---- 0 <= i, j < arr.length
---- arr[i] == 2 * arr[j]
"""


def checkIfExist(arr):
    seen = set()

    for num in arr:
        if num * 2 in seen or num / 2 in seen:
            return True
        seen.add(num)
    return False


print(checkIfExist([10, 2, 5, 3]))
print(checkIfExist([3, 1, 7, 11]))
