"""
The Tribonacci sequence Tn is defined as follows: 
T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
Given n, return the value of Tn.
"""


def tribonacci(n: int) -> int:

    dp = [0, 1, 1]

    if n < 3:
        return dp[n]

    for i in range(3, n + 1):
        dp.append(dp[i - 3] + dp[i - 2] + dp[i - 1])
    return dp[-1]


print(tribonacci(4))  # 4
print(tribonacci(22))  # 1389537
