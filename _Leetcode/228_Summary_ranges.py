def summaryRanges(nums):

    ans = []
    nums.append(float("inf"))

    start = nums[0]

    for i in range(1, len(nums)):

        if nums[i] - nums[i - 1] > 1:
            end = nums[i - 1]
            if start == end:
                ans.append(str(start))
            else:
                ans.append(f"{start}->{end}")
            start = nums[i]
    return ans


print(summaryRanges([0, 1, 2, 4, 5, 7]))
print(summaryRanges([0, 2, 3, 4, 6, 8, 9]))
