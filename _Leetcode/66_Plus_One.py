# You are given a large integer represented as an integer array digits,
# where each digits[i] is the ith digit of the integer.
# The digits are ordered from most significant to least significant
# in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

from collections import deque

def plusOne(digits):
  stack = []
  for d in digits:
    ...
    stack.append(d)


#print(plusOne([1,2,3])) # [1, 2, 4]
#print(plusOne([4,3,2,1]))  # [4,3,2,2]
#print(plusOne([9])) # [1,0]
print(plusOne([9, 9])) # [1,0,0]