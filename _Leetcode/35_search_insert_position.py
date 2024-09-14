def searchInsert(nums, target: int) -> int:
    for idx, val in enumerate(nums):
        if val < target:
            continue
        else:
            return idx

    return len(nums)


print(searchInsert([1, 3, 5, 6], 5))
print(searchInsert([1, 3, 5, 6], 2))
print(searchInsert([1, 3, 5, 6], 7))
