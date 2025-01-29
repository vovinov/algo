from typing import Counter


def firstUniqChar1(s: str) -> int:

    mp = {}

    for ch in s:
        if ch not in mp:
            mp[ch] = 1
        else:
            mp[ch] += 1

    for i in range(len(s)):
        if mp[s[i]] == 1:
            return i

    return -1


def firstUniqChar2(s: str) -> int:

    counter = dict(Counter(s))

    for key, value in counter.items():
        if value == 1:
            return s.index(key)

    return -1


print(firstUniqChar2("leetcode"))
print(firstUniqChar2("loveleetcode"))
print(firstUniqChar2("aabb"))
