# 268. Missing Number

def missingNumber(nums: list[int]) -> int:
    return set(range(len(nums) + 1)) - set(nums)


print(missingNumber([3, 0, 1]))
print(missingNumber([0, 1]))
print(missingNumber([9,6,4,2,3,5,7,0,1]))

