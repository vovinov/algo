def sortedSquares(nums: list[int]) -> list[int]:
    return sorted(num * num for num in nums)

print(sortedSquares([-4,-1,0,3,10]))