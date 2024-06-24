'''
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
'''

def isIsomorphic(s: str, t: str):

    s2t, t2s = {}, {}

    for item in zip(s, t):
        print(item)

    for c1, c2 in zip(s, t):

        if c1 in s2t and s2t[c1] != c2:
            return False
        
        if c2 in t2s and t2s[c2] != c1:
            return False
        
        s2t[c1] = c2
        t2s[c2] = c1

    return True
    



print(isIsomorphic("egg", "add"))
# print(isIsomorphic("foo", "bar"))
# print(isIsomorphic("paper", "title"))