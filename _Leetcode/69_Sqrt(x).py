"""
Given a non-negative integer x, return the square 
root of x rounded down to the nearest integer.
The returned integer should be non-negative as well.
"""


def mySqrt(x: int) -> int:

    if x < 2:
        return x

    l, r = 1, x // 2

    while l <= r:

        mid = (l + r) // 2

        sqr = mid * mid

        if sqr == x:
            return mid

        if sqr < x:
            l = mid + 1
        else:
            r = mid - 1

    return r


print(mySqrt(4))
print(mySqrt(8))
