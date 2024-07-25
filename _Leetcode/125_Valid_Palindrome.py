'''
A phrase is a palindrome if, after converting all uppercase letters into
lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward. Alphanumeric
characters include letters and numbers.
Given a string s, return true if it is a palindrome,
or false otherwise.
'''


def isPalindrome(s):

    l, r = 0, len(s) - 1

    while l <= r:

        if not s[l].isalnum():
            l += 1
            continue

        if not s[r].isalnum():
            r -= 1
            continue

        if s[l].lower() != s[r].lower():
            return False

        l += 1
        r -= 1

    return True


print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
print(isPalindrome(" "))
