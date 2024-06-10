from collections import deque


def remove_element(nums: list[int], val: int) -> int:
    i = 0

    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return i


print(remove_element([0, 1, 2, 2, 3, 0, 4, 2], 2))
