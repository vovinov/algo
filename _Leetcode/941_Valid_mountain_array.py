def validMountainArray(arr):

    if len(arr) < 3:
        return False

    i = 0

    while i < len(arr) - 1 and arr[i] < arr[i + 1]:
        i += 1

    j = len(arr) - 1

    while j > 0 and arr[j] < arr[j - 1]:
        j -= 1
    t = 1
    return i == j and 0 < i < len(arr) - 1


print(validMountainArray([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
# print(validMountainArray([1, 2, 3, 5, 4, 3, 2, 1]))
# print(validMountainArray([3, 5, 5]))
# print(validMountainArray([0, 3, 2, 1]))
