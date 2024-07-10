"""
Given a positive integer num, return true
if num is a perfect square or false otherwise.

A perfect square is an integer that is the square of an integer.
In other words, it is the product of some integer with itself.
"""


def isPerfectSquare(num: int) -> bool:

    if num == 1:
        return True

    l, r = 1, num // 2

    while l <= r:
        mid = (l + r) // 2

        sqr = mid * mid

        if sqr == num:
            return True

        if sqr < num:
            l = mid + 1
        else:
            r = mid - 1

    return False


#  print(isPerfectSquare(16))
#  print(isPerfectSquare(14))
print(isPerfectSquare(36))
