def validPalindrome(s) -> bool:

    # Подфункция проверят является ли строка палиндромом
    def is_palidrome(left, right):

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    # Основной код

    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return is_palidrome(left + 1, right) or is_palidrome(left, right - 1)
        left += 1
        right -= 1
    return True


print(validPalindrome("abca"))
print(validPalindrome("abc"))
print(validPalindrome("aba"))
