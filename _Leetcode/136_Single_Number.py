"""
Given a non-empty array of integers nums, every element
appears twice except for one. Find that single one.
"""


def singleNumber(nums: list[int]) -> int:

    ans = 0

    for num in nums:
        ans = ans ^ num

    return ans


print(singleNumber([4, 1, 2, 1, 2]))
