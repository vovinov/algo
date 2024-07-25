"""
You are given an integer mountain array arr of length n where the
values increase to a peak element and then decrease.
Return the index of the peak element.
"""

from typing import List


def peakIndexInMountainArray(arr: List[int]) -> int:
    
    l, r = 0, len(arr) - 1
    
    while l <= r:

        mid = (l + r) // 2

        if arr[mid - 1] < arr[mid] > arr[mid + 1]:
            return mid
        
        if arr[mid] > arr[mid - 1]:

            l = mid

        else:
            r = mid

    return mid


#  print(peakIndexInMountainArray([0, 1, 0]))
#  print(peakIndexInMountainArray([0, 2, 1, 0]))
#  print(peakIndexInMountainArray([0, 10, 5, 2]))
#  print(peakIndexInMountainArray([3, 4, 5, 1]))
print(peakIndexInMountainArray([40, 48, 61, 75, 100, 99, 98, 39, 30, 10]))
