"""
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above.
"""


def generate(numRows):

    dp = [[1], [1, 1]]

    if numRows < 3:
        return dp[:numRows]

    for _ in range(numRows - 2):
        next_row = [1]

        for i in range(1, len(dp[-1])):
            next_row.append(dp[-1][i] + dp[-1][i - 1])

        next_row += [1]
        dp.append(next_row)

    return dp


print(generate(5))
print(generate(1))
