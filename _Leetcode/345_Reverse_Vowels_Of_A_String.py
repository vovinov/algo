def reverseVowels(s: str) -> str:
    v = ["a", "e", "i", "o", "u"]

    s = list(s)  # type: ignore

    l, r = 0, len(s) - 1

    while l <= r:

        if s[l].lower() not in v:
            l += 1
            continue

        if s[r].lower() not in v:
            r -= 1
            continue

        s[l], s[r] = s[r], s[l]  # type: ignore
        l += 1
        r -= 1

    return "".join(s)


print(reverseVowels("IceCreAm"))  # "AceCreIm"
print(reverseVowels("leetcode"))  # "leotcede"
