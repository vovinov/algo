def isPowerOfFour(n) -> bool:

    if n < 1:
        return False

    if n == 1:
        return True

    return isPowerOfFour(n / 4)


print(isPowerOfFour(16))
print(isPowerOfFour(5))
print(isPowerOfFour(1))
