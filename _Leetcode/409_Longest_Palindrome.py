from collections import Counter


def longestPalindrome(s: str) -> int | None:

    total = 0

    cnt = Counter(s)

    for item, value in cnt.items():
        cur = value - value % 2
        total += cur
        cnt[item] -= cur

    print(sum(cnt.values()))
    return total if not sum(cnt.values()) else total + 1


print(longestPalindrome("abccccdd"))  # 7
print(longestPalindrome("a"))  # 1
print(longestPalindrome("bb"))  # 2
