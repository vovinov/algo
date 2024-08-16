"""
Given an array nums of integers,
return how many of them contain an even number of digits.
"""


def findNumbers(nums) -> int:

    cnt = 0

    for number in nums:
        if len(str(number)) % 2 == 0:
            cnt += 1

    return cnt


print(findNumbers([12, 345, 2, 6, 7896]))  #  2
print(findNumbers([555, 901, 482, 1771]))  #  1
