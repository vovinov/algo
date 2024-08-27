"""
You are given a string s consisting of lowercase English letters.
A duplicate removal consists of choosing two adjacent and
equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals
have been made. It can be proven that the answer is unique.
"""


def removeDuplicates(s: str):

    stack = []

    for item in s:

        if stack and item == stack[-1]:
            stack.pop()
        else:
            stack.append(item)

    return "".join(stack)


print(removeDuplicates("abbaca"))  # ca
print(removeDuplicates("azxxzy"))  # ay
