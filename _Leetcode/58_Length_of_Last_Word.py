def lengthOfLastWord1(s: str) -> int:
    ls = s.strip().split(" ")
    return len(ls[-1])


def lengthOfLastWord2(s: str) -> int:

    word = ""

    for i in range(len(s) - 1, -1, -1):

        if s[i] == " ":
            if word:
                return len(word)
        else:
            word += s[i]

    return len(word)


print(lengthOfLastWord1("Hello World"))
print(lengthOfLastWord2("   fly me   to   the moon  "))
print(lengthOfLastWord1("luffy is still joyboy"))
print(lengthOfLastWord2("luffy is still joyboy"))
