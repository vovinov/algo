def licenseKeyFormatting(s: str, k: int):
    s = s.replace("-", "").upper()

    ans = ""
    g = k

    for i in range(len(s) - 1, -1, -1):

        if g == 0:
            g = k
            ans += "-"
        ans += s[i]
        g -= 1

    return ans[::-1]


print(licenseKeyFormatting(s="aaaaaaa", k=3))  # "5F3Z-2E9W"
print(licenseKeyFormatting(s="5F3Z-2e-9-w", k=4))  # "5F3Z-2E9W"
