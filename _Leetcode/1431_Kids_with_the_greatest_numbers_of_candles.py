def kidsWithCandies(candies, extraCandies):

    ans = []

    mx = max(candies)

    for i in candies:
        if i + extraCandies >= mx:
            ans.append(True)
        else:
            ans.append(False)

    return ans


print(kidsWithCandies([2, 3, 5, 1, 3], 3))
print(kidsWithCandies([4, 2, 1, 1, 2], 1))
print(kidsWithCandies([12, 1, 12], 10))
