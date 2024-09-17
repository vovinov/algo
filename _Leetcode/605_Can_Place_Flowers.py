def canPlaceFlowers(flowerbed, n: int) -> bool:

    fl = [0] + flowerbed + [0]

    for i in range(1, len(fl) - 1):

        if fl[i - 1] == fl[i] == fl[i + 1] == 0:
            fl[i] = 1
            n -= 1

    return n <= 0


# print(canPlaceFlowers([1,0,0,0,1], 1))
print(canPlaceFlowers([1, 0, 0, 0, 1], 2))
print(canPlaceFlowers([1, 0, 0, 0, 0, 1], 2))
print(canPlaceFlowers([1, 0, 0, 0, 1, 0, 0], 2))
