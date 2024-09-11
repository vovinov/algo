import random


def guessNumber(num: int):

    pick = random.choices(range(1, num + 1))[0]
    print(f"Pick - {pick}")

    def guess(num: int):
        if num > pick:
            return -1
        elif num < pick:
            return 1
        else:
            return 0

    l, r = 1, num

    while l <= r:

        mid = (l + r) // 2

        if guess(mid) == 0:
            return f"Your number is {mid}"

        if guess(mid) == -1:
            r = mid - 1
        elif guess(mid) == 1:
            l = mid + 1


print(guessNumber(20))
