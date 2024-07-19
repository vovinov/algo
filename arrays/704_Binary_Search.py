"""
Given an array of integers nums which is sorted in
ascending order, and an integer target, write a function
to search target in nums. If target exists,
then return its index. Otherwise, return -1.
"""

from typing import List


def search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:

        middle = (l + r) // 2

        if nums[middle] == target:
            return middle

        if nums[middle] > target:
            r = middle - 1
        else:
            l = middle + 1

    return -1


# print(search([-1, 0, 3, 5, 9, 12], 9))
# print(search([-1, 0, 3, 5, 9, 12], 2))
print(search([-1, 0, 3, 5, 9, 12], 13))
