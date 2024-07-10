"""
Given an integer num, repeatedly add all its digits
until the result has only one digit, and return it.
"""


def addDigits(num: int) -> int:

    def helper(num: int) -> int:
        res = 0
        while num:
            num, d = divmod(num, 10)
            res += d
        return res

    while num > 9:
        num = helper(num)

    return num


print(addDigits(38))  # 2
print(addDigits(381))  # 2
print(addDigits(1))  # 1
