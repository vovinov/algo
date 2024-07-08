"""
You are given an integer array nums consisting
of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k
that has the maximum average value and return this value.
"""


def findMaxAverage(nums, k: int) -> float:
    cur = sum(nums[:k])
    cur_max = cur

    for i in range(k, len(nums)):
        cur -= nums[i - k]
        cur += nums[i]
        cur_max = max(cur, cur_max)

    return cur_max / k


print(findMaxAverage([1, 12, -5, -6, 50, 3], 4))
print(findMaxAverage([5], 1))
print(findMaxAverage([-1], 1))
