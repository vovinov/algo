'''
Given an integer x, return true if x is a palindrome, and false otherwise.
'''

# Solution1
def isPalindrome1(x: int):
    
    return str(x) == str(x)[::-1]


# Solution2
def isPalindrome2(x: int):

    if x < 0:
        return False
    
    new = 0
    orig = x

    while x:

        x, d = divmod(x, 10)

        new = new * 10 + d

    return new == orig


print(isPalindrome2(121))
print(isPalindrome2(-121))
print(isPalindrome2(10))
