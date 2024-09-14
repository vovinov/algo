from typing import Counter


def isAnagram(s: str, t: str) -> bool:

    return Counter(s) == Counter(t)


print(isAnagram("anagram", "nagaram"))
print(isAnagram("rat", "car"))
