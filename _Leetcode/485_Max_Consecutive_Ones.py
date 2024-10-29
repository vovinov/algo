def findMaxConsecutiveOnes(nums) -> int:

    cur = 0
    max_cur = 0

    for i in range(len(nums)):
        if nums[i] == 1:
            cur += 1
            if max_cur < cur:
                max_cur = cur
        else:
            cur = 0

    return max_cur


print(findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
print(findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]))
