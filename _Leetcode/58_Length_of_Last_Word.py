# Given a string s consisting of words and spaces,
# return the length of the last word in the string.


def lengthOfLastWord(s: str) -> int:
    ls = s.strip().split(' ')
    return len(ls[-1])

print(lengthOfLastWord('Hello World'))
print(lengthOfLastWord("   fly me   to   the moon  "))
print(lengthOfLastWord('luffy is still joyboy'))