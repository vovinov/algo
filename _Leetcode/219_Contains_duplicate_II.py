def containsNearbyDuplicate(nums, k: int) -> bool:

    d = {}

    for i, num in enumerate(nums):

        if num in d and i - d[num] <= k:
            return True

        d[num] = i

    return False


# print(containsNearbyDuplicate([1, 2, 3, 1], 3))
# print(containsNearbyDuplicate([1, 0, 1, 1], k=1))
print(containsNearbyDuplicate([1, 2, 3, 1, 2, 3], k=2))
