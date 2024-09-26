def twoSum(numbers, target):
    l, r = 0, len(numbers) - 1

    while l <= r:

        summa = numbers[l] + numbers[r]

        if summa == target:
            return [l + 1, r + 1]

        if summa > target:
            r -= 1
        else:
            l += 1


print(twoSum([2, 7, 11, 15], 9))  # [1, 2]
