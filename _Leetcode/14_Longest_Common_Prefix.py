"""
Write a function to find the longest common prefix
string amongst an array of strings.
If there is no common prefix, return an empty string "".
"""


def longestCommonPrefix(strs):
    ans = ""

    for idx, val in enumerate(strs[0]):

        for w in strs[1:]:

            if len(w) < idx + 1 or w[idx] != val:
                return ans
        ans += val

    return ans


print(longestCommonPrefix(["flower", "flow", "flight"]))  # fl
print(longestCommonPrefix(["dog", "racecar", "car"]))  # ''
