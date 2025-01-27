from typing import List


def containsNearbyDuplicate(nums: List[int], k: int) -> bool:

    d = {}

    for i in range(len(nums)):

        cur = nums[i]
        if cur in d:
            if abs(i - d[nums[i]]) <= k:
                return True
        else:
            d[nums[i]] = i

    return False


print(containsNearbyDuplicate([1, 2, 3, 1], 3))
print(containsNearbyDuplicate([1, 0, 1, 1], k=1))
print(containsNearbyDuplicate([1, 2, 3, 1, 2, 3], k=2))
