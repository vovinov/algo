def twoSum(nums: list[int], target: int) -> list[int]:
    d = {}
    for i, num in enumerate(nums):
        if target - num in d:
            return [d[target - num], i]
        d[num] = i