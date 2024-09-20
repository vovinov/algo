def hammingDistance(x, y):

    ans = 0

    while x or y:

        ans += (x & 1) != (y & 1)
        x >>= 1
        y >>= 1

    return ans


print(hammingDistance(1, 4))
