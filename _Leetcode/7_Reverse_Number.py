def reverse(x: int):

    new_x = int(str(abs(x))[::-1])

    if new_x >= 2**31 - 1:
        return 0

    return new_x if x > 0 else int("-" + str(new_x))


print(reverse(123))  # 321
print(reverse(-123))  # 321
print(reverse(1534236469))  # 321
