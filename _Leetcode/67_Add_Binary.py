def addBinary(a: str, b: str) -> str | None:

    if len(a) > len(b):
        b = "0" * (len(a) - len(b)) + b
    else:
        a = "0" * (len(b) - len(a)) + a

    carry = 0
    ans = ""

    for i in range(len(a) - 1, -1, -1):

        d1 = int(a[i])
        d2 = int(b[i])

        carry, d = divmod(d1 + d2 + carry, 2)
        ans += str(d)

    if carry:
        ans += str(carry)

    return ans[::-1]


print(addBinary(a="11", b="1"))
