"""
Given two strings s and t, return true
if s is a subsequence of t, or false otherwise.
"""


def isSubsequence(s: str, t: str) -> bool:

    stack = list(s)

    for i in range(len(t) - 1, -1, -1):

        if stack and stack[-1] == t[i]:
            stack.pop()

    return len(stack) == 0


print(isSubsequence("abc", "ahbgdc"))
