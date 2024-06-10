
def singleNumber(nums: list[int]) -> int:

    ans = 0

    for num in nums:
        ans = ans ^ num

    return ans

print(singleNumber([4,1,2,1,2]))