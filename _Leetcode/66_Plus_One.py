def plusOne1(digits):
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] != 9:
            digits[i] += 1
            return digits
        else:
            digits[i] = 0
    digits.insert(0, 1)
    return digits


def plusOne2(digits):
    carry = 1

    for i in range(len(digits) - 1, -1, -1):

        carry, digits[i] = divmod(digits[i] + carry, 10)

    return digits if not carry else [1] + digits


# print(plusOne([1,2,3])) # [1, 2, 4]
# print(plusOne1([4, 3, 2, 1]))  # [4,3,2,2]
# print(plusOne2([4, 3, 2, 1]))  # [4,3,2,2]
# print(plusOne([9])) # [1,0]
 print(plusOne1([9, 9]))  # [1,0,0]
print(plusOne2([9, 9]))  # [1,0,0]
