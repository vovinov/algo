"""
Given an integer array nums, move all 0's to the end
of it while maintaining the relative order of the non-zero elements.
"""


def moveZeroes(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    j = 0

    for i in range(len(nums)):
        if nums[i] == 0:
            nums[j], nums[i] = nums[i], nums[j]
        j += 1

    return nums


# print(moveZeroes([0, 1, 0, 3, 12]))  #  [1,3,12,0,0]
print(moveZeroes([1, 1, 0, 3, 12]))  #  [1,3,12,0,0]
# print(moveZeroes([0]))  #  [0]
