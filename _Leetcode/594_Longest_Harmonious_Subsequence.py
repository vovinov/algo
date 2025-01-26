

def findLHS(nums):

    # Сортировка массива
    nums.sort()

    # Задаём начальные переменные
    l, r = 0, 1
    ans = 0

    # Основной цикл
    while r < len(nums):

        # Ищем разницу
        diff = nums[r] - nums[l]

        # Проверка на гармоничность, разница между элементами
        # не должна превышать 1
        if diff == 1:

            # Сверяем максимальное и полученное значение, перезаписываем
            ans = max(ans, r - l + 1)

        # Если разница меньше 1, идём дальше
        if diff <= 1:
            r += 1
        # Если больше, двигаем левый показатель
        else:
            l += 1

    return ans


# print(findLHS([1, 3, 2, 2, 5, 2, 3, 7]))  # [3,2,2,2,3]
print(findLHS([1, 2, 3, 4]))  # [1, 2]
# print(findLHS([1, 1, 1, 1]))  # [1, 2]
