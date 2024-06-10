# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.

# array, hash table

def twoSum(nums: list[int], target: int) -> list[int]:
    d = {}
    for i, num in enumerate(nums):
        if target - num in d:
            return [d[target - num], i]
        d[num] = i