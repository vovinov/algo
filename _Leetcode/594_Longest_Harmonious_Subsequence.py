

def findLHS(nums):

    ans = [nums[0]]

    for i in range(1, len(nums)):

        current = nums[i]

        if abs(current - ans[0]) <= 1:
            ans.append(current)

    mx = cur if len(cur) > len(mx)

    return len(mx)


print(findLHS([1, 3, 2, 2, 5, 2, 3, 7]))
