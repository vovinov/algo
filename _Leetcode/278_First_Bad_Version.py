def firstBadVersion(n: int, arr):

    if n == 1:
        return 1

    l, r = 1, n

    while l <= r:

        mid = (l + r) // 2

        if isBadVersion(mid):
            r = mid - 1
        else:
            l = mid + 1

        return l


print(firstBadVersion(5, [False, False, False, True, True]))
print(firstBadVersion(5, [False, True, True, True, True]))
print(firstBadVersion(1, [False, False, True, True, True]))
