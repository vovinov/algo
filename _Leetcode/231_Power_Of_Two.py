def isPowerOfTwo(num):

    if num < 1:
        return False
    if num == 1:
        return True

    return isPowerOfTwo(num / 2)


print(isPowerOfTwo(16))
print(isPowerOfTwo(3))
print(isPowerOfTwo(1))
