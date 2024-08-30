"""
Given a string s, reverse the order of characters in
each word within a sentence while still preserving
whitespace and initial word order.
"""


def reverseWords(s: str) -> str:

    words = s.split(" ")
    res = []

    for word in words:
        res.append(word[::-1])

    return " ".join(res)


reverseWords("Let's take LeetCode contest")
reverseWords("Mr Ding")

assert reverseWords("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"
assert reverseWords("Mr Ding") == "rM gniD"
