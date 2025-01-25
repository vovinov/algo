
from typing import List


def findErrorNums(nums: List[int]) -> List[int]:

    mp = {i: 0 for i in range(1, len(nums) + 1)}

    for a in nums:
        mp[a] -= 1

    dupl, missing = 0, 0

    for key, value in mp.items():
        if value == -2:
            dupl = key

        elif value == 0:
            missing = key

    return [dupl, missing]


# print(findErrorNums([1, 1]))
# print(findErrorNums([1, 2, 2, 4]))
# print(findErrorNums([3, 3, 1]))
# print(findErrorNums([8, 7, 3, 5, 3, 6, 1, 4]))
print(findErrorNums([1, 2, 2, 4]))
