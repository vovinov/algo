def isIsomorphic1(s: str, t: str):

    s2t, t2s = {}, {}

    for c1, c2 in zip(s, t):

        if c1 in s2t and s2t[c1] != c2:
            return False

        if c2 in t2s and t2s[c2] != c1:
            return False

        s2t[c1] = c2
        t2s[c2] = c1

    return True


def isIsomorphic2(s: str, t: str):

    s2t = {}
    t2s = {}

    for i in range(len(s)):
        cur_s = s[i]
        cur_t = t[i]

        # a -> e
        if cur_s in s2t:
            if s2t[cur_s] != cur_t:
                return False
        else:
            # e -> a
            if cur_t in t2s and t2s[cur_t] != cur_s:
                return False
            else:
                s2t[cur_s] = cur_t
                t2s[cur_t] = cur_s

    return True


print(isIsomorphic1("egg", "add"))
print(isIsomorphic2("egg", "add"))
# print(isIsomorphic("foo", "bar"))
# print(isIsomorphic("paper", "title"))
