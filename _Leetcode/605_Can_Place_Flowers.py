
'''
iven an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty,
and an integer n, return true if n new flowers can be planted in the flowerbed without violating
the no-adjacent-flowers rule and false otherwise.
'''

def canPlaceFlowers(flowerbed, n: int) -> bool:
    
    for i in range(len(flowerbed)):

        if n == 0:
            return True         
        
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
            flowerbed[i] = 1
            n -= 1
        
    return n == 0

# print(canPlaceFlowers([1,0,0,0,1], 1))
# print(canPlaceFlowers([1,0,0,0,1], 2))
print(canPlaceFlowers([1,0,0,0,1,0,0], 2))