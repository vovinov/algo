from collections import Counter
from typing import List


def majorityElement(nums: List[int]):

    ans = -float("inf")

    for item, counter in Counter(nums).items():
        if counter > len(nums) / 2 and item > ans:
            ans = item
    return ans


print(majorityElement([6, 5, 5]))
print(majorityElement([1000000000, 1000000000, -1000000000, -1000000000, -1000000000]))
print(majorityElement([2, 2, 1, 1, 1, 2, 2]))
print(majorityElement([3, 2, 3]))
