def reverse(x: int) -> int:
    # Определяем знак числа
    sign = -1 if x < 0 else 1
    # Работаем с положительной частью числа
    x = abs(x)

    # Переворачиваем число
    reversed_number = 0
    while x != 0:
        # Берем последнюю цифру числа
        digit = x % 10
        # Убираем последнюю цифру из числа
        x //= 10

        # Добавляем цифру к результату
        reversed_number = reversed_number * 10 + digit

    # Восстанавливаем знак
    reversed_number *= sign

    # Проверяем на переполнение
    if reversed_number < -(2**31) or reversed_number > 2**31 - 1:
        return 0

    return reversed_number


print(reverse(123))  # 321
print(reverse(-123))  # 321
print(reverse(1534236469))  # 0
