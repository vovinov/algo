# Given a sorted array of distinct integers
# and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.

def searchInsert(nums, target: int) -> int:
    for idx, val in enumerate(nums):
        if val < target:
            continue
        else:
            return idx
    return len(nums)


print(searchInsert([1,3,5,6], 5))
print(searchInsert([1,3,5,6], 2))
print(searchInsert([1,3,5,6], 7))
